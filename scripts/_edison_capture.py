"""Shared Edison-response capture helpers for the deep-research scripts.

Goal: when we spend credits on an Edison job, we want to save every
useful piece of the response — answer, formatted answer, reasoning,
agent-state trace, citations, generated files, and the full raw
response — so the work is reusable for provenance, audit, debugging,
and downstream curation without re-querying.

Files written per task (under ``out_dir``):

    {stem}.md                  Primary human-readable answer
                               (formatted_answer if present, else answer).
    {stem}-meta.yaml           Compact provenance summary (task_id,
                               status, costs, query, template_vars, ...).
                               Always written.
    {stem}-response.json       Full ``response.model_dump(mode='json')``.
                               Every SDK-exposed field, future-proof
                               against new ones.
    {stem}-citations.md        Parsed reference list from
                               ``formatted_answer`` (PaperQA convention,
                               matches the falcon citations.md sidecar).
    {stem}-agent-state.json    ``agent_state`` (tool-call trace) +
                               ``environment_frame`` + verbose
                               ``metadata``. Only written when verbose
                               fetch yields any of those fields.
    {stem}-files.json          ``client.list_files(trajectory_id)``
                               output — artifacts Edison may have
                               generated during the run. Empty list
                               written when none are present, so the
                               existence of the file means "we asked".

where ``{stem}`` is the slug the caller chose (e.g.
``archaeoglobus_medium_dsm_399-edison-literature``).

The ``capture_full_response`` entry point handles all of the above and
returns the meta dict the caller should also yaml-dump as
``{stem}-meta.yaml``. Idempotent: re-invoking overwrites; existing
sibling files are not read.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# -- citation extraction --------------------------------------------------

_NUMBERED_REF_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$", re.MULTILINE)
_URL_RE = re.compile(r"https?://[^\s<>)\]]+", re.IGNORECASE)
_PMID_RE = re.compile(r"\bPMID[:\s]+(\d+)", re.IGNORECASE)
_DOI_RE = re.compile(r"\b(?:doi[:\s]+|https?://(?:dx\.)?doi\.org/)(10\.[^\s<>)\]]+)",
                     re.IGNORECASE)


def parse_citations(formatted_answer: str | None) -> list[dict[str, Any]]:
    """Best-effort citation extraction from a PaperQA ``formatted_answer``.

    PaperQA's answer text typically ends with a ``References`` section
    using either a numbered list (``1. Author2020paper pages 1-3``) or
    a free-text block. This pulls both numbered entries and any
    PMID/DOI/URL hits, deduping by reference text and identifier.

    Returns a list of dicts with optional keys: ``ordinal``, ``text``,
    ``pmid``, ``doi``, ``urls``. Each entry corresponds to one
    distinct citation. Empty list when the input is empty or no
    references parse out — callers should still write the file so
    "we parsed but found nothing" is distinguishable from "we never
    tried".
    """
    if not formatted_answer:
        return []

    # PaperQA convention: References section starts at "References" or
    # the first numbered line. Look for the last occurrence of the
    # word "References" (case-insensitive) and treat everything after
    # it as the reference block; fall back to scanning the full text.
    text = formatted_answer
    m = re.search(r"\n\s*references\s*\n", text, re.IGNORECASE)
    block = text[m.end():] if m else text

    out: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    for match in _NUMBERED_REF_RE.finditer(block):
        ordinal = int(match.group(1))
        body = match.group(2).strip()
        if not body:
            continue
        entry: dict[str, Any] = {"ordinal": ordinal, "text": body}
        pmid_m = _PMID_RE.search(body)
        if pmid_m:
            entry["pmid"] = pmid_m.group(1)
        doi_m = _DOI_RE.search(body)
        if doi_m:
            entry["doi"] = doi_m.group(1).rstrip(".,;)")
        urls = _URL_RE.findall(body)
        if urls:
            entry["urls"] = [u.rstrip(".,;)") for u in urls]
        key = entry.get("pmid") or entry.get("doi") or body
        if key in seen_keys:
            continue
        seen_keys.add(key)
        out.append(entry)

    # If the numbered scan caught nothing, fall back to whatever URLs
    # appear in the answer body — better something than nothing.
    if not out:
        for url in dict.fromkeys(_URL_RE.findall(formatted_answer)):
            key = url.rstrip(".,;)")
            if key in seen_keys:
                continue
            seen_keys.add(key)
            out.append({"text": url, "urls": [key]})
    return out


def render_citations_md(citations: list[dict[str, Any]],
                        query: str | None = None) -> str:
    """Render the parsed citations as a human-readable markdown sidecar."""
    lines: list[str] = ["# Citations", ""]
    if query:
        lines.append(f"_From a query of {len(query)} chars (see `*-meta.yaml`)._")
        lines.append("")
    if not citations:
        lines.append("_No citations parsed._")
        return "\n".join(lines) + "\n"
    for c in citations:
        bits: list[str] = []
        if "ordinal" in c:
            bits.append(f"**{c['ordinal']}.**")
        bits.append(c.get("text", "(no text)"))
        ids: list[str] = []
        if "pmid" in c:
            ids.append(f"PMID:{c['pmid']}")
        if "doi" in c:
            ids.append(f"doi:{c['doi']}")
        if ids:
            bits.append("(" + ", ".join(ids) + ")")
        lines.append("- " + " ".join(bits))
        for url in c.get("urls", []):
            lines.append(f"    - <{url}>")
    return "\n".join(lines) + "\n"


# -- helpers --------------------------------------------------------------

def query_sha256(query: str) -> str:
    """Stable hash of the rendered query — useful for dedup / cache keys."""
    return hashlib.sha256(query.encode("utf-8")).hexdigest()


def _safe_model_dump(obj: Any) -> Any:
    """Best-effort serialization of a pydantic response (or anything).

    Returns the JSON-mode model dump when ``obj`` is a pydantic model;
    falls back to ``__dict__`` or repr.
    """
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        try:
            return obj.model_dump(mode="json")
        except Exception:  # pylint: disable=broad-except
            try:
                return obj.model_dump()
            except Exception:
                pass
    if hasattr(obj, "__dict__"):
        return {k: _safe_model_dump(v) for k, v in obj.__dict__.items()
                if not k.startswith("_")}
    if isinstance(obj, (list, tuple)):
        return [_safe_model_dump(v) for v in obj]
    if isinstance(obj, dict):
        return {k: _safe_model_dump(v) for k, v in obj.items()}
    try:
        json.dumps(obj)
        return obj
    except (TypeError, ValueError):
        return repr(obj)


def _get_attr(response: Any, name: str, default: Any = None) -> Any:
    return getattr(response, name, default)


def _fetch_verbose(client: Any, task_id: str) -> Any | None:
    """Pull the verbose response for a completed task.

    No new compute on the Edison side — this is a metadata fetch from
    cached task results. Returns ``None`` and swallows errors so a
    verbose-fetch failure never breaks the primary capture path.
    """
    if not client or not task_id:
        return None
    try:
        return client.get_task(task_id=task_id, verbose=True)
    except Exception:  # pylint: disable=broad-except
        return None


def _try_list_files(client: Any, task_id: str) -> Any:
    """Pull the artifact-file list for a task. Returns None on failure."""
    if not client or not task_id:
        return None
    try:
        return client.list_files(trajectory_id=task_id)
    except Exception:  # pylint: disable=broad-except
        return None


# Internal PaperQA artifacts we never want to download (giant pickles
# carrying the indexed corpus — useful to PaperQA, not to curators).
_INTERNAL_ARTIFACT_PREFIXES = ("pqa:",)

# Hard cap on per-artifact size; protects against accidentally pulling
# multi-GB binaries. Curation tables are typically < 100 KB.
_DEFAULT_ARTIFACT_MAX_BYTES = 2_000_000


def _safe_artifact_name(raw_name: str) -> str:
    """Sanitize an Edison data-storage name for use as a filename."""
    safe = "".join(c if c.isalnum() or c in "._- " else "_"
                   for c in raw_name).strip().rstrip(".")
    safe = "_".join(safe.split())  # collapse whitespace
    return safe[:120] or "artifact"


def _fetch_artifact_content(client: Any, data_storage_id: str) -> tuple[str, str | bytes] | None:
    """Fetch one artifact's content. Returns (ext, content) or None on failure.

    The SDK may return either a ``Path`` (GCS-backed, possibly extracted
    zip) or a ``RawFetchResponse``-like object with a ``.content``
    attribute. Both are handled — we always write the raw payload as
    text when possible, falling back to bytes.
    """
    try:
        result = client.fetch_data_from_storage(data_storage_id=data_storage_id)
    except Exception:  # pylint: disable=broad-except
        return None
    if result is None:
        return None
    # RawFetchResponse-ish: has .content
    if hasattr(result, "content"):
        content = getattr(result, "content")
        if isinstance(content, bytes):
            try:
                return ("txt", content.decode("utf-8"))
            except UnicodeDecodeError:
                return ("bin", content)
        return ("txt", str(content))
    # Path-ish (single file): read it
    if hasattr(result, "read_text"):
        try:
            return ("txt", result.read_text())
        except (UnicodeDecodeError, OSError):
            try:
                return ("bin", result.read_bytes())
            except OSError:
                return None
    # list[Path]: write index plus contents in order
    if isinstance(result, list):
        parts: list[str] = []
        for i, p in enumerate(result):
            if hasattr(p, "read_text"):
                try:
                    parts.append(f"# file {i}: {p.name if hasattr(p, 'name') else p}\n"
                                 + p.read_text())
                except Exception:  # pylint: disable=broad-except
                    parts.append(f"# file {i}: <binary, not inlined>")
        return ("txt", "\n\n".join(parts))
    return None


def fetch_named_artifacts(
    *,
    client: Any,
    files_listing: Any,
    out_dir: Path,
    stem: str,
    max_bytes: int = _DEFAULT_ARTIFACT_MAX_BYTES,
) -> list[dict[str, Any]]:
    """Download named curation artifacts referenced by ``list_files``.

    Writes per-artifact files under ``{stem}-artifacts/`` and returns a
    manifest summarizing what was fetched, skipped, or failed. The
    manifest is intentionally compact — full per-artifact metadata is
    already in ``{stem}-files.json``.

    Skips:
      - PaperQA internal artifacts (name prefix ``pqa:`` — large pickles).
      - Artifacts whose declared size exceeds ``max_bytes``.

    Idempotent: an existing file in the artifacts dir is overwritten
    (Edison artifacts are immutable per task, so re-fetching is fine).
    """
    manifest: list[dict[str, Any]] = []
    if files_listing is None or client is None:
        return manifest

    # Normalize: list_files may return a dict with 'data', a list, or a
    # pydantic-y object — pull the iterable of file entries.
    entries: list[Any]
    if isinstance(files_listing, dict) and isinstance(files_listing.get("data"), list):
        entries = files_listing["data"]
    elif isinstance(files_listing, list):
        entries = files_listing
    else:
        return manifest

    artifacts_dir = out_dir / f"{stem}-artifacts"
    fetched_any = False
    for entry in entries:
        ds = entry.get("data_storage") if isinstance(entry, dict) else None
        if not isinstance(ds, dict):
            continue
        ds_id = ds.get("id") or entry.get("data_storage_id")
        name = ds.get("name") or "artifact"
        if not ds_id:
            continue
        # Skip internal PaperQA cache
        if any(name.lower().startswith(p) for p in _INTERNAL_ARTIFACT_PREFIXES):
            manifest.append({"name": name, "id": str(ds_id), "status": "skipped-internal"})
            continue
        size = (ds.get("metadata") or {}).get("size")
        if isinstance(size, int) and size > max_bytes:
            manifest.append({"name": name, "id": str(ds_id),
                             "status": "skipped-too-large", "size": size})
            continue
        fetched = _fetch_artifact_content(client, str(ds_id))
        if fetched is None:
            manifest.append({"name": name, "id": str(ds_id), "status": "fetch-failed"})
            continue
        ext, content = fetched
        safe = _safe_artifact_name(name)
        out_path = artifacts_dir / f"{safe}.{ext}"
        if not fetched_any:
            artifacts_dir.mkdir(parents=True, exist_ok=True)
            fetched_any = True
        if isinstance(content, bytes):
            out_path.write_bytes(content)
        else:
            out_path.write_text(content)
        manifest.append({"name": name, "id": str(ds_id), "status": "fetched",
                         "path": str(out_path.relative_to(out_dir)),
                         "chars": len(content) if isinstance(content, str) else None})
    return manifest


# -- main entry point -----------------------------------------------------

def capture_full_response(
    *,
    response: Any,
    client: Any,
    out_dir: Path,
    stem: str,
    query: str,
    base_meta: dict[str, Any],
) -> dict[str, Any]:
    """Persist every reusable piece of an Edison response.

    Writes the sibling files documented at the top of this module and
    returns the final meta dict the caller should yaml-dump as
    ``{stem}-meta.yaml``. The caller still owns writing the meta yaml
    so that the meta file format stays in one place (yaml.safe_dump
    knobs may vary).

    ``response`` is the SDK response object (``run_tasks_until_done``
    returns a list; pass one element here).

    ``client`` is the live ``EdisonClient`` instance. Pass ``None`` to
    skip the verbose-and-files fetch (e.g. in dry-run modes).

    ``base_meta`` is the caller's pre-built meta dict (slug, media
    path, template path, etc.); fields are merged with the new
    response-derived fields, with response-derived fields winning.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / f"{stem}.md"
    response_json_path = out_dir / f"{stem}-response.json"
    citations_md_path = out_dir / f"{stem}-citations.md"
    agent_state_path = out_dir / f"{stem}-agent-state.json"
    files_path = out_dir / f"{stem}-files.json"

    # Primary answer markdown
    answer = _get_attr(response, "answer")
    formatted_answer = _get_attr(response, "formatted_answer")
    answer_reasoning = _get_attr(response, "answer_reasoning")
    body = formatted_answer or answer or "(no answer field on this job's response type)"
    md_path.write_text(body)

    # Full raw response dump (every SDK field, future-proof)
    response_dump = _safe_model_dump(response)
    response_json_path.write_text(json.dumps(response_dump, indent=2, default=str))

    # Citations sidecar
    citations = parse_citations(formatted_answer or answer)
    citations_md_path.write_text(render_citations_md(citations, query=query))

    # Verbose + files via secondary fetches (no extra billing)
    task_id = str(_get_attr(response, "task_id") or "")
    verbose = _fetch_verbose(client, task_id) if task_id else None
    if verbose is not None:
        agent_state = _safe_model_dump(_get_attr(verbose, "agent_state"))
        environment_frame = _safe_model_dump(_get_attr(verbose, "environment_frame"))
        verbose_metadata = _safe_model_dump(_get_attr(verbose, "metadata"))
        if any(x is not None for x in (agent_state, environment_frame, verbose_metadata)):
            agent_state_path.write_text(json.dumps({
                "task_id": task_id,
                "agent_state": agent_state,
                "environment_frame": environment_frame,
                "metadata": verbose_metadata,
            }, indent=2, default=str))

    files_listing = _try_list_files(client, task_id) if task_id else None
    artifacts_manifest: list[dict[str, Any]] = []
    if files_listing is not None:
        files_path.write_text(json.dumps(_safe_model_dump(files_listing),
                                         indent=2, default=str))
        # Pull the actual content of named curation artifacts (small,
        # not internal PaperQA pickles) into a sibling artifacts/ dir.
        artifacts_manifest = fetch_named_artifacts(
            client=client,
            files_listing=_safe_model_dump(files_listing),
            out_dir=out_dir,
            stem=stem,
        )

    # Build the meta dict the caller will yaml-dump
    meta: dict[str, Any] = dict(base_meta)
    meta.update({
        "task_id": task_id,
        "status": _get_attr(response, "status"),
        "job_name": _get_attr(response, "job_name"),
        "user": _get_attr(response, "user"),
        "agent_name": _get_attr(response, "agent_name"),
        "build_owner": _get_attr(response, "build_owner"),
        "environment_name": _get_attr(response, "environment_name"),
        "project_id": str(_get_attr(response, "project_id") or "") or None,
        "share_status": _get_attr(response, "share_status"),
        "created_at": _to_iso(_get_attr(response, "created_at")),
        "answer_received_at": datetime.now(timezone.utc).isoformat(),
        "total_cost": _get_attr(response, "total_cost"),
        "total_queries": _get_attr(response, "total_queries"),
        "has_successful_answer": _get_attr(response, "has_successful_answer"),
        "has_answer_reasoning": bool(answer_reasoning),
        "answer_chars": len(answer or ""),
        "formatted_answer_chars": len(formatted_answer or ""),
        "answer_reasoning_chars": len(answer_reasoning or ""),
        "citations_parsed": len(citations),
        "query_sha256": query_sha256(query),
        "sidecar_files": _existing_sidecars(out_dir, stem),
        "artifacts_fetched": [a for a in artifacts_manifest if a.get("status") == "fetched"],
        "artifacts_skipped": [a for a in artifacts_manifest if a.get("status") != "fetched"],
    })
    return meta


def capture_dry_run(
    *,
    out_dir: Path,
    stem: str,
    query: str,
    base_meta: dict[str, Any],
) -> dict[str, Any]:
    """Dry-run capture: write meta-only artifacts; never write the .md.

    Used by the ``--dry-run`` flag in both edison scripts so prompts
    are auditable without spending credits.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    meta: dict[str, Any] = dict(base_meta)
    meta.update({
        "status": "dry-run",
        "query_chars": len(query),
        "query": query,
        "query_sha256": query_sha256(query),
    })
    return meta


def _existing_sidecars(out_dir: Path, stem: str) -> dict[str, bool]:
    """Snapshot which sidecar files exist for this stem — for the meta."""
    return {
        "answer_md": (out_dir / f"{stem}.md").exists(),
        "response_json": (out_dir / f"{stem}-response.json").exists(),
        "citations_md": (out_dir / f"{stem}-citations.md").exists(),
        "agent_state_json": (out_dir / f"{stem}-agent-state.json").exists(),
        "files_json": (out_dir / f"{stem}-files.json").exists(),
    }


def _to_iso(dt: Any) -> str | None:
    """ISO-format a datetime or return the str it already is."""
    if dt is None:
        return None
    if hasattr(dt, "isoformat"):
        return dt.isoformat()
    return str(dt)
