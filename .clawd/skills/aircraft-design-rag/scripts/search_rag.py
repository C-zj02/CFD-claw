#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence


WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]+")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")
BLANK_RE = re.compile(r"\s+")


@dataclass
class Chunk:
    path: Path
    heading: str
    start_line: int
    end_line: int
    text: str
    tokens: list[str] = field(default_factory=list)
    tf: Counter[str] = field(default_factory=Counter)

    @property
    def length(self) -> int:
        return max(len(self.tokens), 1)

    def relative_path(self, root: Path) -> str:
        return str(self.path.resolve().relative_to(root.resolve()))


@dataclass
class SearchHit:
    chunk: Chunk
    score: float


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search Markdown files in a local RAG-data folder and return the most relevant chunks."
    )
    parser.add_argument("--data-dir", required=True, help="Directory containing Markdown knowledge files.")
    parser.add_argument("--query", required=True, help="Query to search for.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of hits to print.")
    parser.add_argument("--chunk-lines", type=int, default=28, help="Lines per chunk.")
    parser.add_argument("--overlap-lines", type=int, default=8, help="Line overlap between chunks.")
    parser.add_argument("--max-snippet-chars", type=int, default=280, help="Maximum snippet length.")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    requested_data_dir = Path(args.data_dir).expanduser().resolve()
    data_dir = resolve_data_dir(requested_data_dir)
    query = args.query.strip()

    if not query:
        print("error: --query must not be empty", file=sys.stderr)
        return 2
    if data_dir is None:
        print(f"error: data directory not found: {requested_data_dir}", file=sys.stderr)
        return 2

    files = sorted(data_dir.rglob("*.md"))
    if not files:
        print(f"No Markdown files found under: {data_dir}")
        return 0

    chunks, document_frequency, avg_length = build_index(
        files,
        chunk_lines=args.chunk_lines,
        overlap_lines=args.overlap_lines,
    )
    hits = search_chunks(
        chunks,
        query,
        document_frequency=document_frequency,
        avg_length=avg_length,
    )

    print(f"Query: {query}")
    print(f"Data directory: {data_dir}")
    print(f"Markdown files scanned: {len(files)}")
    print(f"Chunks indexed: {len(chunks)}")
    print()

    if not hits:
        print("No relevant chunks found.")
        return 0

    print("Top hits:")
    for index, hit in enumerate(hits[: max(args.top_k, 1)], start=1):
        chunk = hit.chunk
        snippet = make_snippet(chunk.text, args.max_snippet_chars)
        rel_path = chunk.relative_path(data_dir.parent)
        print(
            f"{index}. score={hit.score:.3f} file={rel_path} "
            f"lines={chunk.start_line}-{chunk.end_line} heading={chunk.heading or '-'}"
        )
        print(f"   snippet: {snippet}")
    return 0


def resolve_data_dir(requested: Path, *, script_path: Path | None = None) -> Path | None:
    requested = requested.expanduser().resolve()
    if requested.exists() and requested.is_dir():
        return requested

    source = (script_path or Path(__file__)).expanduser().resolve()
    for parent in source.parents:
        candidate = parent / "RAG-data"
        if candidate.exists() and candidate.is_dir():
            print(
                f"warning: data directory not found: {requested}; using {candidate.resolve()}",
                file=sys.stderr,
            )
            return candidate.resolve()

    return None


def build_index(
    paths: Iterable[Path],
    *,
    chunk_lines: int,
    overlap_lines: int,
) -> tuple[list[Chunk], Counter[str], float]:
    chunks: list[Chunk] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        chunks.extend(split_markdown(path, text, chunk_lines=chunk_lines, overlap_lines=overlap_lines))

    document_frequency: Counter[str] = Counter()
    for chunk in chunks:
        chunk.tokens = tokenize(chunk.text)
        chunk.tf = Counter(chunk.tokens)
        for token in set(chunk.tokens):
            document_frequency[token] += 1

    avg_length = sum(chunk.length for chunk in chunks) / max(len(chunks), 1)
    return chunks, document_frequency, avg_length


def search_chunks(
    chunks: Sequence[Chunk],
    query: str,
    *,
    document_frequency: Counter[str],
    avg_length: float,
) -> list[SearchHit]:
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    total_chunks = max(len(chunks), 1)
    unique_query_tokens = list(dict.fromkeys(query_tokens))
    query_compact = compact_text(query)
    hits: list[SearchHit] = []

    for chunk in chunks:
        score = bm25_score(
            chunk=chunk,
            query_tokens=unique_query_tokens,
            document_frequency=document_frequency,
            total_chunks=total_chunks,
            avg_length=avg_length,
        )
        score += heuristic_boost(chunk, unique_query_tokens, query_compact)
        if score > 0:
            hits.append(SearchHit(chunk=chunk, score=score))

    hits.sort(
        key=lambda item: (
            round(item.score, 6),
            item.chunk.start_line * -1,
            item.chunk.path.name,
        ),
        reverse=True,
    )
    return hits


def bm25_score(
    *,
    chunk: Chunk,
    query_tokens: Sequence[str],
    document_frequency: Counter[str],
    total_chunks: int,
    avg_length: float,
) -> float:
    score = 0.0
    k1 = 1.5
    b = 0.75

    for token in query_tokens:
        tf = chunk.tf.get(token, 0)
        if tf <= 0:
            continue
        df = document_frequency.get(token, 0)
        idf = math.log(1 + (total_chunks - df + 0.5) / (df + 0.5))
        denom = tf + k1 * (1 - b + b * (chunk.length / max(avg_length, 1.0)))
        score += idf * ((tf * (k1 + 1)) / max(denom, 1e-9))
    return score


def heuristic_boost(chunk: Chunk, query_tokens: Sequence[str], query_compact: str) -> float:
    if not query_tokens:
        return 0.0

    lowered_text = chunk.text.lower()
    compact_chunk = compact_text(chunk.text)
    heading = chunk.heading.lower()
    compact_heading = compact_text(chunk.heading)
    path_str = str(chunk.path).lower()
    boost = 0.0

    joined_query = " ".join(query_tokens)
    if joined_query and joined_query in lowered_text:
        boost += 1.5
    if query_compact and query_compact in compact_chunk:
        boost += 6.0
    if query_compact and query_compact in compact_heading:
        boost += 6.0

    matched_terms = sum(1 for token in query_tokens if token in chunk.tf)
    if matched_terms == len(query_tokens):
        boost += 2.5
    else:
        boost += matched_terms * 0.3

    designation_tokens = [token for token in query_tokens if has_designation_shape(token)]
    for token in query_tokens:
        if token in heading:
            boost += 0.7
        if token in path_str:
            boost += 0.4
        if has_designation_shape(token) and token in heading:
            boost += 3.0
        if has_designation_shape(token) and token in compact_chunk:
            boost += 1.2
    for token in designation_tokens:
        if token in compact_heading:
            boost += 25.0
        elif token in compact_chunk:
            boost += 15.0
        else:
            boost -= 8.0

    if appears_exact_designation(query_compact, compact_chunk):
        boost += 3.0
    boost -= image_noise_penalty(chunk.text)

    return boost


def appears_exact_designation(query_compact: str, compact_chunk: str) -> bool:
    if not query_compact:
        return False
    has_digit = any(char.isdigit() for char in query_compact)
    has_alpha = any(char.isalpha() for char in query_compact)
    if has_digit and has_alpha and query_compact in compact_chunk:
        return True
    return False


def has_designation_shape(token: str) -> bool:
    return any(char.isdigit() for char in token) and any(char.isalpha() for char in token)


def image_noise_penalty(text: str) -> float:
    summary_count = text.count("图片摘要")
    image_count = text.count("![](")
    caption_count = text.count("系统图")
    return summary_count * 2.2 + image_count * 1.2 + caption_count * 0.4


def split_markdown(path: Path, text: str, *, chunk_lines: int, overlap_lines: int) -> list[Chunk]:
    lines = text.splitlines()
    if not lines:
        return []

    chunks: list[Chunk] = []
    step = max(chunk_lines - overlap_lines, 1)

    sections: list[tuple[str, int, int]] = []
    current_heading = path.stem
    section_start = 1

    for line_number, line in enumerate(lines, start=1):
        match = HEADING_RE.match(line)
        if not match:
            continue

        heading_text = clean_heading(match.group(1)) or path.stem
        if line_number > section_start:
            sections.append((current_heading, section_start, line_number - 1))
        current_heading = heading_text
        section_start = line_number

    sections.append((current_heading, section_start, len(lines)))

    for heading, start_line, end_line in sections:
        section_lines = lines[start_line - 1 : end_line]
        start_index = 0

        while start_index < len(section_lines):
            end_index = min(start_index + chunk_lines, len(section_lines))
            chunk_start_line = start_line + start_index
            chunk_end_line = start_line + end_index - 1
            chunk_text = "\n".join(section_lines[start_index:end_index]).strip()

            if chunk_text:
                chunks.append(
                    Chunk(
                        path=path,
                        heading=heading,
                        start_line=chunk_start_line,
                        end_line=chunk_end_line,
                        text=chunk_text,
                    )
                )

            if end_index >= len(section_lines):
                break
            start_index += step

    return chunks


def tokenize(text: str) -> list[str]:
    lowered = text.lower()
    tokens: list[str] = []
    tokens.extend(WORD_RE.findall(lowered))

    for span in CJK_RE.findall(text):
        compact_span = compact_text(span)
        if not compact_span:
            continue

        if len(compact_span) <= 4:
            tokens.append(compact_span)

        max_n = 3
        for n in range(2, max_n + 1):
            if len(compact_span) < n:
                continue
            for index in range(len(compact_span) - n + 1):
                tokens.append(compact_span[index : index + n])

    return tokens


def compact_text(text: str) -> str:
    return BLANK_RE.sub("", text.lower())


def clean_heading(text: str) -> str:
    return BLANK_RE.sub(" ", text.strip())


def make_snippet(text: str, max_chars: int) -> str:
    kept_lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("图片摘要："):
            continue
        if "![](" in line:
            continue
        kept_lines.append(line)

    cleaned = BLANK_RE.sub(" ", " ".join(kept_lines)).strip()
    if not cleaned:
        cleaned = BLANK_RE.sub(" ", text).strip()
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 3].rstrip() + "..."


if __name__ == "__main__":
    raise SystemExit(main())
