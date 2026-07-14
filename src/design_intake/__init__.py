"""Structured requirement intake contracts for aircraft design."""

from .coverage import (
    MODEL_COVERAGE_MATRIX,
    assess_model_coverage,
    canonical_coverage_key,
    coverage_for_requirement,
    coverage_matrix_as_dict,
)
from .models import (
    ChangeProposal,
    ClarificationQuestion,
    DesignIntent,
    DesignIntentStatus,
    FeasibilityDiagnosis,
    ModelCoverageRecord,
    ModelCoverageStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)
from .outcome import build_solver_outcome_revision
from .parser import (
    PARSER_VERSION,
    looks_like_design_request,
    looks_like_requirement_change,
    parse_design_intent,
)
from .preflight import diagnose_design_intent, preflight_design_intent
from .projection import (
    complete_intent_with_solver_defaults,
    intent_from_aircraft_request,
    solver_request_from_intent,
)
from .store import DesignRevisionStore
from .workflow import (
    DesignRequirementWorkflow,
    DesignWorkflowError,
    WorkflowActionError,
    WorkflowStateError,
)

__all__ = [
    "MODEL_COVERAGE_MATRIX",
    "PARSER_VERSION",
    "ChangeProposal",
    "ClarificationQuestion",
    "DesignRequirementWorkflow",
    "DesignRevisionStore",
    "DesignIntent",
    "DesignIntentStatus",
    "DesignWorkflowError",
    "FeasibilityDiagnosis",
    "ModelCoverageRecord",
    "ModelCoverageStatus",
    "RequirementField",
    "RequirementRole",
    "RequirementSource",
    "WorkflowActionError",
    "WorkflowStateError",
    "assess_model_coverage",
    "build_solver_outcome_revision",
    "canonical_coverage_key",
    "complete_intent_with_solver_defaults",
    "coverage_for_requirement",
    "coverage_matrix_as_dict",
    "diagnose_design_intent",
    "intent_from_aircraft_request",
    "looks_like_design_request",
    "looks_like_requirement_change",
    "parse_design_intent",
    "preflight_design_intent",
    "solver_request_from_intent",
]
