"""Thread-safe background job management for deterministic design runs."""

from __future__ import annotations

import json
import shutil
import threading
from concurrent.futures import Future, ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from uuid import uuid4

from src.design_execution.models import AircraftDesignRequest, DesignRunEvent, DesignRunStatus
from src.design_execution.runner import AircraftDesignRunResult, AircraftDesignRunner


TERMINAL_JOB_STATUSES = {
    "completed",
    "nonconverged",
    "engineering_infeasible",
    "failed",
    "cancelled",
    "timed_out",
}


class DesignJobQueueFullError(RuntimeError):
    """Raised when all worker and queue slots are occupied."""


@dataclass
class AircraftDesignJob:
    job_id: str
    request: AircraftDesignRequest
    timeout_seconds: float
    status: str = "queued"
    stage: str = "queued"
    progress: int = 0
    message: str = "任务已进入队列"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    started_at: str | None = None
    finished_at: str | None = None
    retry_of: str | None = None
    events: list[dict[str, Any]] = field(default_factory=list)
    result: AircraftDesignRunResult | None = None
    error: str | None = None
    cancel_event: threading.Event = field(default_factory=threading.Event, repr=False)
    condition: threading.Condition = field(default_factory=threading.Condition, repr=False)

    @property
    def terminal(self) -> bool:
        return self.status in TERMINAL_JOB_STATUSES

    def to_dict(
        self,
        *,
        include_events: bool = True,
        include_result_details: bool = True,
    ) -> dict[str, Any]:
        result = self.result.to_dict() if self.result is not None else None
        request = self.request.to_dict()
        if result is not None and not include_result_details:
            result = {
                "status": result["status"],
                "output_dir": result["output_dir"],
                "duration_seconds": result["duration_seconds"],
                "converged": result["converged"],
                "engineering": {
                    key: result["engineering"].get(key)
                    for key in (
                        "numerical_converged",
                        "engineering_feasible",
                        "overall_status",
                        "blocking_failed_count",
                    )
                },
                "summary": result["summary"],
                "issues": result["issues"][:5],
            }
        if not include_result_details:
            request.pop("provenance", None)
        data = {
            "job_id": self.job_id,
            "status": self.status,
            "stage": self.stage,
            "progress": self.progress,
            "message": self.message,
            "request": request,
            "timeout_seconds": self.timeout_seconds,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "retry_of": self.retry_of,
            "error": self.error,
            "terminal": self.terminal,
            "last_sequence": self.events[-1]["sequence"] if self.events else 0,
            "result": result,
        }
        if include_events:
            data["events"] = list(self.events)
        return data

    @classmethod
    def from_dict(
        cls,
        value: dict[str, Any],
        *,
        generated_root: Path,
    ) -> "AircraftDesignJob":
        if not isinstance(value, dict):
            raise ValueError("persisted design job must be an object")
        request = AircraftDesignRequest.from_dict(value.get("request"))
        result_value = value.get("result")
        result = (
            AircraftDesignRunResult.from_dict(
                result_value,
                request=request,
                allowed_root=generated_root,
            )
            if result_value is not None
            else None
        )
        events = value.get("events", [])
        if not isinstance(events, list) or not all(isinstance(event, dict) for event in events):
            raise ValueError("persisted design job events must be an object list")
        sequences = [event.get("sequence") for event in events]
        if sequences != list(range(1, len(events) + 1)):
            raise ValueError("persisted design job events are not sequential")
        timeout_seconds = value.get("timeout_seconds", 180.0)
        if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, (int, float)):
            raise ValueError("persisted timeout_seconds must be a number")
        persisted_status = str(value.get("status") or "failed")
        persisted_stage = str(value.get("stage") or "failed")
        persisted_message = str(value.get("message") or "")
        if (
            result is not None
            and persisted_status == DesignRunStatus.COMPLETED.value
            and result.status is not DesignRunStatus.COMPLETED
        ):
            persisted_status = result.status.value
            persisted_stage = result.status.value
            persisted_message = {
                DesignRunStatus.NONCONVERGED: "任务完成，但设计结果未收敛",
                DesignRunStatus.ENGINEERING_INFEASIBLE: "任务已收敛，但方案未通过工程约束",
                DesignRunStatus.FAILED: "历史结果未通过新版工程契约校验",
            }.get(result.status, persisted_message)
        return cls(
            job_id=str(value.get("job_id") or ""),
            request=request,
            timeout_seconds=float(timeout_seconds),
            status=persisted_status,
            stage=persisted_stage,
            progress=max(0, min(100, int(value.get("progress") or 0))),
            message=persisted_message,
            created_at=str(value.get("created_at") or ""),
            started_at=str(value["started_at"]) if value.get("started_at") else None,
            finished_at=str(value["finished_at"]) if value.get("finished_at") else None,
            retry_of=str(value["retry_of"]) if value.get("retry_of") else None,
            events=[dict(event) for event in events],
            result=result,
            error=str(value["error"]) if value.get("error") else None,
        )


class AircraftDesignJobManager:
    """Execute aircraft design requests in bounded background worker threads."""

    def __init__(
        self,
        runner: AircraftDesignRunner,
        *,
        metadata_root: Path,
        max_concurrent_jobs: int = 2,
        max_queued_jobs: int = 8,
        max_history_jobs: int = 100,
        history_ttl_days: int | None = 30,
        artifact_root: Path | None = None,
    ) -> None:
        if max_concurrent_jobs < 1:
            raise ValueError("max_concurrent_jobs must be at least 1")
        if max_queued_jobs < 0:
            raise ValueError("max_queued_jobs must not be negative")
        if max_history_jobs < 1:
            raise ValueError("max_history_jobs must be at least 1")
        if history_ttl_days is not None and history_ttl_days < 1:
            raise ValueError("history_ttl_days must be at least 1 or null")
        self.runner = runner
        self.metadata_root = Path(metadata_root).resolve()
        self.metadata_root.mkdir(parents=True, exist_ok=True)
        self.max_concurrent_jobs = max_concurrent_jobs
        self.max_queued_jobs = max_queued_jobs
        self.max_history_jobs = max_history_jobs
        self.history_ttl_days = history_ttl_days
        self.artifact_root = Path(artifact_root).resolve() if artifact_root is not None else None
        self._jobs: dict[str, AircraftDesignJob] = {}
        self._lock = threading.RLock()
        self._capacity = threading.BoundedSemaphore(max_concurrent_jobs + max_queued_jobs)
        self._executor = ThreadPoolExecutor(
            max_workers=max_concurrent_jobs,
            thread_name_prefix="aircraft-design",
        )
        self._futures: dict[str, Future[None]] = {}
        self._load_persisted_jobs()
        self.prune_history()

    def submit(
        self,
        request: AircraftDesignRequest,
        *,
        timeout_seconds: float = 180.0,
        retry_of: str | None = None,
    ) -> dict[str, Any]:
        if timeout_seconds <= 0 or timeout_seconds > 3_600:
            raise ValueError("timeout_seconds must be between 0 and 3600")
        if not self._capacity.acquire(blocking=False):
            raise DesignJobQueueFullError("aircraft design job queue is full")
        job_id = f"job-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid4().hex[:8]}"
        job = AircraftDesignJob(
            job_id=job_id,
            request=request,
            timeout_seconds=float(timeout_seconds),
            retry_of=retry_of,
        )
        self._append_event(job, "queued", "任务已进入执行队列", 0)
        with self._lock:
            self._jobs[job_id] = job
        self._persist(job)
        try:
            future = self._executor.submit(self._run_job, job)
        except Exception:
            self._capacity.release()
            with self._lock:
                self._jobs.pop(job_id, None)
            (self.metadata_root / f"{job_id}.json").unlink(missing_ok=True)
            raise
        with self._lock:
            self._futures[job_id] = future
        future.add_done_callback(lambda _future, completed_id=job_id: self._job_finished(completed_id))
        return job.to_dict()

    def get(self, job_id: str) -> dict[str, Any]:
        return self._require_job(job_id).to_dict()

    def list(self) -> list[dict[str, Any]]:
        with self._lock:
            jobs = list(self._jobs.values())
        jobs.sort(key=lambda job: job.created_at, reverse=True)
        return [
            job.to_dict(include_events=False, include_result_details=False)
            for job in jobs
        ]

    def cancel(self, job_id: str) -> dict[str, Any]:
        job = self._require_job(job_id)
        with job.condition:
            if not job.terminal:
                job.cancel_event.set()
                job.message = "正在取消任务"
                self._append_event(job, job.stage, job.message, job.progress)
                job.condition.notify_all()
        with self._lock:
            future = self._futures.get(job_id)
        if future is not None and future.cancel():
            self._finish_without_result(job, "cancelled", "任务在启动前已取消")
        self._persist(job)
        return job.to_dict()

    def retry(self, job_id: str) -> dict[str, Any]:
        job = self._require_job(job_id)
        if not job.terminal:
            raise ValueError("only terminal jobs can be retried")
        return self.submit(job.request, timeout_seconds=job.timeout_seconds, retry_of=job.job_id)

    def events_after(self, job_id: str, sequence: int = 0) -> dict[str, Any]:
        job = self._require_job(job_id)
        return {
            "job_id": job.job_id,
            "events": [event for event in job.events if event["sequence"] > sequence],
            "last_sequence": job.events[-1]["sequence"] if job.events else sequence,
            "terminal": job.terminal,
            "status": job.status,
        }

    def wait_for_events(
        self,
        job_id: str,
        *,
        after_sequence: int,
        timeout_seconds: float = 15.0,
    ) -> dict[str, Any]:
        job = self._require_job(job_id)
        with job.condition:
            job.condition.wait_for(
                lambda: job.terminal or bool([e for e in job.events if e["sequence"] > after_sequence]),
                timeout=timeout_seconds,
            )
        return self.events_after(job_id, after_sequence)

    def _run_job(self, job: AircraftDesignJob) -> None:
        if job.cancel_event.is_set():
            self._finish_without_result(job, "cancelled", "任务在启动前已取消")
            return
        job.status = "running"
        job.started_at = datetime.now().isoformat(timespec="seconds")
        self._append_event(job, "preparing", "后台工作线程已启动", 5)
        self._persist(job)

        def progress(event: DesignRunEvent) -> None:
            self._append_event(
                job,
                event.stage.value,
                event.message,
                event.progress,
                event.detail,
            )
            self._persist(job)

        try:
            result = self.runner.run(
                job.request,
                timeout_seconds=job.timeout_seconds,
                cancel_event=job.cancel_event,
                on_progress=progress,
                run_id=job.job_id,
            )
        except Exception as exc:
            job.error = str(exc)
            self._finish_without_result(job, "failed", f"任务执行异常：{exc}")
            return

        job.result = result
        job.status = result.status.value
        job.stage = result.status.value
        job.progress = 100
        job.message = self._result_message(result.status)
        job.finished_at = datetime.now().isoformat(timespec="seconds")
        self._persist(job)
        with job.condition:
            job.condition.notify_all()

    def _finish_without_result(self, job: AircraftDesignJob, status: str, message: str) -> None:
        job.status = status
        job.stage = status
        job.progress = 100
        job.message = message
        job.finished_at = datetime.now().isoformat(timespec="seconds")
        self._append_event(job, status, message, 100)
        self._persist(job)

    def _append_event(
        self,
        job: AircraftDesignJob,
        stage: str,
        message: str,
        progress: int,
        detail: dict[str, Any] | None = None,
    ) -> None:
        with job.condition:
            job.stage = stage
            job.message = message
            job.progress = max(0, min(100, int(progress)))
            job.events.append(
                {
                    "sequence": len(job.events) + 1,
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "stage": stage,
                    "message": message,
                    "progress": job.progress,
                    "detail": detail,
                }
            )
            job.condition.notify_all()

    def _require_job(self, job_id: str) -> AircraftDesignJob:
        with self._lock:
            job = self._jobs.get(job_id)
        if job is None:
            raise KeyError(f"Unknown design job: {job_id}")
        return job

    def _persist(self, job: AircraftDesignJob) -> None:
        with job.condition:
            path = self.metadata_root / f"{job.job_id}.json"
            temp = path.with_suffix(f".{threading.get_ident()}.tmp")
            temp.write_text(json.dumps(job.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
            temp.replace(path)

    def _load_persisted_jobs(self) -> None:
        generated_root = self.runner.generated_root.resolve()
        for path in sorted(self.metadata_root.glob("job-*.json")):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
                job = AircraftDesignJob.from_dict(value, generated_root=generated_root)
                if not job.job_id or job.job_id != path.stem:
                    raise ValueError("persisted design job id does not match its filename")
            except (OSError, ValueError, json.JSONDecodeError):
                continue
            self._jobs[job.job_id] = job
            original_status = str(value.get("status") or "failed")
            if original_status != job.status:
                self._append_event(
                    job,
                    job.stage,
                    job.message,
                    100,
                    {
                        "reason": "engineering_revalidation",
                        "previous_status": original_status,
                    },
                )
                self._persist(job)

        for job in list(self._jobs.values()):
            if job.terminal:
                continue
            job.status = "failed"
            job.error = "service_restarted"
            job.finished_at = datetime.now().isoformat(timespec="seconds")
            self._append_event(
                job,
                "interrupted",
                "服务重启前任务未完成，已标记为中断",
                100,
                {"reason": "service_restarted"},
            )
            self._persist(job)

    def _job_finished(self, job_id: str) -> None:
        with self._lock:
            self._futures.pop(job_id, None)
        self._capacity.release()
        self.prune_history()

    def prune_history(self) -> list[str]:
        """Remove expired terminal metadata and its deterministic run directory."""
        with self._lock:
            terminal = [job for job in self._jobs.values() if job.terminal]
        terminal.sort(key=self._history_timestamp, reverse=True)
        remove_ids = {job.job_id for job in terminal[self.max_history_jobs :]}
        if self.history_ttl_days is not None:
            cutoff = datetime.now() - timedelta(days=self.history_ttl_days)
            remove_ids.update(
                job.job_id for job in terminal if self._history_timestamp(job) < cutoff
            )

        generated_root = self.runner.generated_root.resolve()
        removed: list[str] = []
        for job_id in sorted(remove_ids):
            with self._lock:
                job = self._jobs.get(job_id)
                if job is None or not job.terminal or job_id in self._futures:
                    continue
                self._jobs.pop(job_id, None)
            (self.metadata_root / f"{job_id}.json").unlink(missing_ok=True)
            task_dir = (generated_root / job_id).resolve()
            try:
                task_dir.relative_to(generated_root)
            except ValueError:
                continue
            if task_dir.is_dir():
                shutil.rmtree(task_dir)
            if self.artifact_root is not None:
                artifact_dir = (self.artifact_root / job_id).resolve()
                try:
                    artifact_dir.relative_to(self.artifact_root)
                except ValueError:
                    artifact_dir = self.artifact_root
                if artifact_dir != self.artifact_root and artifact_dir.is_dir():
                    shutil.rmtree(artifact_dir)
            removed.append(job_id)
        return removed

    def shutdown(self, *, wait: bool = True, cancel_pending: bool = False) -> None:
        if cancel_pending:
            with self._lock:
                pending_ids = list(self._futures)
            for job_id in pending_ids:
                self.cancel(job_id)
        self._executor.shutdown(wait=wait, cancel_futures=cancel_pending)

    @staticmethod
    def _history_timestamp(job: AircraftDesignJob) -> datetime:
        raw = job.finished_at or job.created_at
        try:
            return datetime.fromisoformat(raw)
        except (TypeError, ValueError):
            return datetime.min

    def _result_message(self, status: DesignRunStatus) -> str:
        return {
            DesignRunStatus.COMPLETED: "任务完成，结果已通过工程校验",
            DesignRunStatus.NONCONVERGED: "任务完成，但设计结果未收敛",
            DesignRunStatus.ENGINEERING_INFEASIBLE: "任务已收敛，但方案未通过工程约束",
            DesignRunStatus.CANCELLED: "任务已取消",
            DesignRunStatus.TIMED_OUT: "任务执行超时",
            DesignRunStatus.FAILED: "任务执行失败",
        }[status]
