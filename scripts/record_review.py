"""Validate immutable Mech reviews without executing their recorded commands.

This module is the canonical, standalone payload used by CLAW and its Mechs.
The self-contained LinkML schema defines shape; the checks below enforce scope,
reference closure, provenance, and honest review/triage lifecycle semantics.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import importlib
import json
import math
import os
import re
import secrets
import stat
import subprocess
import sys
import threading
from collections.abc import Sequence
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse

import yaml
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.linkml_model.meta import SchemaDefinition

VERSION = "1.0.0"
REPORT_ROOT = "reviews/structured"
SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema/record_review.yaml"
OPEN_STATUSES = frozenset({"open", "deferred"})


class ReviewError(ValueError):
    """A review cannot be trusted as a structured observation."""


class _ReviewDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _dump_document(review: dict) -> str:
    return yaml.dump(review, Dumper=_ReviewDumper, allow_unicode=True, sort_keys=False)


class _ReviewLoader(yaml.SafeLoader):
    yaml_implicit_resolvers = {
        key: [item for item in values if item[0] != "tag:yaml.org,2002:timestamp"]
        for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
    }
    yaml_path_resolvers: dict[Any, Any] = {}

    def compose_node(self, parent, index):
        event = self.peek_event()
        if (self.check_event(yaml.AliasEvent) or getattr(event, "anchor", None)
                or getattr(event, "tag", None)):
            raise ReviewError("review YAML must not contain aliases, anchors, or explicit tags")
        return super().compose_node(parent, index)

    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise ReviewError(f"duplicate or non-string YAML key: {key!r}")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


class _LinkMLLoader(yaml.SafeLoader):
    """Keep LinkML parsing independent of C-loader import order and foreign resolvers."""

    yaml_path_resolvers: dict[Any, Any] = {}

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ReviewError(f"duplicate LinkML YAML key: {key!r}")
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


_linkml_yaml_loader = importlib.import_module("linkml_runtime.loaders.yaml_loader")
# Vendored copies and the research contract mutate the same process-global loader.
_LINKML_LOADER_LOCK = vars(_linkml_yaml_loader).setdefault(
    "_claw_linkml_loader_lock", threading.RLock()
)


@contextmanager
def _pure_linkml_loader():
    loader = _linkml_yaml_loader
    with _LINKML_LOADER_LOCK:
        original = loader.DupCheckYamlLoader
        loader.DupCheckYamlLoader = _LinkMLLoader
        try:
            yield
        finally:
            loader.DupCheckYamlLoader = original


def load_document(raw: str | bytes) -> dict:
    """Read YAML/JSON with duplicate-key and non-finite-number rejection."""
    try:
        data = yaml.load(raw, Loader=_ReviewLoader)
    except (yaml.YAMLError, UnicodeError, RecursionError) as exc:
        raise ReviewError(f"invalid review YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ReviewError("document must contain one mapping")
    try:
        json.dumps(data, allow_nan=False)
    except (TypeError, ValueError, RecursionError) as exc:
        raise ReviewError(f"document must contain finite JSON-compatible values: {exc}") from exc
    return data


def relative_path(value: str) -> PurePosixPath:
    """Accept only unambiguous repository-relative file paths, not locators."""
    if (not isinstance(value, str) or not value or value.startswith("/")
            or "\\" in value or any(ord(c) < 32 for c in value)
            or any(c in value for c in ":?#%")
            or any(part in {"", ".", ".."} for part in value.split("/"))):
        raise ReviewError(f"unsafe repository-relative path: {value!r}")
    return PurePosixPath(value)


def timestamp(value: str) -> datetime:
    if not isinstance(value, str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?Z", value
    ):
        raise ReviewError("timestamps must be explicit ISO 8601 UTC strings ending in Z")
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise ReviewError(f"invalid UTC timestamp: {value}") from exc


@lru_cache(maxsize=8)
def _schema_validator(schema_text: str):
    schema = load_document(schema_text)
    if schema.get("imports"):
        raise ReviewError("review schema must be self-contained; remote imports are forbidden")
    with _pure_linkml_loader():
        generated = json.loads(JsonSchemaGenerator(
            SchemaDefinition(**schema), topClass="RecordReview", not_closed=False,
            include_null=False,
        ).serialize())
    validator = validator_for(generated)
    validator.check_schema(generated)
    return validator(generated)


def _unique(values: list, label: str) -> set:
    if len(values) != len(set(values)):
        raise ReviewError(f"{label} contains duplicates")
    return set(values)


def _references(values: list, allowed: set, label: str) -> None:
    selected = _unique(values, label)
    if not selected <= allowed:
        raise ReviewError(f"{label} contains dangling references: {sorted(selected - allowed)}")


def _owners(item: dict, label: str) -> None:
    owners = item.get("owner_paths", [])
    for owner in owners:
        relative_path(owner["path"])
    if not owners and not item.get("ownership_note"):
        raise ReviewError(f"{label} requires maintained owner paths or an explicit ownership limit")


def _acyclic(actions: list[dict]) -> None:
    pending = {item["action_id"]: set(item.get("depends_on", [])) for item in actions}
    while pending:
        ready = {key for key, dependencies in pending.items() if not dependencies}
        if not ready:
            raise ReviewError("action dependencies contain a cycle")
        pending = {key: dependencies - ready for key, dependencies in pending.items()
                   if key not in ready}


def validate_review(review: dict, schema_path: Path = SCHEMA_PATH) -> None:
    """Validate shape and semantics only, without reading current target files.

    Historical reviews remain valid observations when records later change.
    Persistence separately binds the supplied provenance to the current bytes.
    """
    try:
        json.dumps(review, allow_nan=False)
        validator = _schema_validator(schema_path.read_text(encoding="utf-8"))
    except (OSError, TypeError, ValueError, RecursionError) as exc:
        raise ReviewError(f"cannot validate review: {exc}") from exc
    errors = sorted(validator.iter_errors(review), key=lambda error: str(list(error.path)))
    if errors:
        raise ReviewError("; ".join(
            f"{'.'.join(map(str, error.path)) or '<root>'}: {error.message}"
            for error in errors[:20]
        ))
    start, finish = timestamp(review["started_at"]), timestamp(review["finished_at"])
    if finish < start:
        raise ReviewError("review finished_at precedes started_at")
    if not review["review_id"].startswith(finish.strftime("%Y%m%dT%H%M%SZ") + "-"):
        raise ReviewError("review_id must begin with the finished UTC timestamp and a hyphen")
    targets = _unique([item["target_id"] for item in review["targets"]], "target IDs")
    _unique([(item["path"], item.get("selector")) for item in review["targets"]], "target locators")
    inputs = _unique([item["path"] for item in review["source"]["inputs"]], "input paths")
    for name in inputs:
        relative_path(name)
    for item in review["targets"]:
        relative_path(item["path"])
        if item["path"] not in inputs:
            raise ReviewError("each target path must identify a hashed source input")
        if item["kind"] == "snapshot_row" and not item.get("selector"):
            raise ReviewError("snapshot-row targets require an exact selector")
        _owners(item, f"target {item['target_id']}")
    scope = review["scope"]
    _references(scope["reviewed_target_ids"], targets, "reviewed target IDs")
    if scope["population_size"] < len(targets):
        raise ReviewError("population_size is smaller than the explicitly selected targets")
    if scope["coverage"] == "full" and scope["population_size"] != len(scope["reviewed_target_ids"]):
        raise ReviewError("full coverage requires every population member to be reviewed")
    if scope["coverage"] == "sampled" and not scope.get("sampling_method"):
        raise ReviewError("sampled reviews require a sampling method")
    if review["kind"] == "record" and (len(targets) != 1 or scope["population_size"] != 1):
        raise ReviewError("a record review must identify exactly one record")
    if review["completion"] == "completed" and set(scope["reviewed_target_ids"]) != targets:
        raise ReviewError("completed review has explicitly selected targets left unreviewed")
    if review["kind"] == "category" and not review.get("boundary_decisions"):
        raise ReviewError("category reviews require explicit lump/split/retain/defer decisions")
    evidence = _unique([item["evidence_id"] for item in review["evidence"]], "evidence IDs")
    _unique([item["check_id"] for item in review["checks"]], "check IDs")
    _unique([item["assessment_id"] for item in review["assessments"]], "assessment IDs")
    findings = _unique([item["finding_id"] for item in review["findings"]], "finding IDs")
    _unique([item["issue_key"] for item in review["findings"]], "issue keys within a review")
    actions = _unique([item["action_id"] for item in review["actions"]], "action IDs")
    for group in (review["checks"], review["assessments"], review["findings"],
                  review["actions"], review.get("boundary_decisions", [])):
        for item in group:
            _references(item["target_ids"], targets, "target references")
            _references(item.get("evidence_ids", []), evidence, "evidence references")
    for item in review["evidence"]:
        if timestamp(item["accessed_at"]) > finish:
            raise ReviewError("evidence cannot be accessed after the review finished")
        if item["kind"] == "search" and not item.get("search_scope"):
            raise ReviewError("search evidence requires a bounded search scope")
    unavailable_required = []
    failed_required = []
    for check in review["checks"]:
        status = check["status"]
        if status in {"skipped", "unavailable", "not_applicable"} and (
            "exit_code" in check or "expected_exit_code" in check
        ):
            raise ReviewError("an unexecuted check cannot have an exit code")
        if check.get("command") and status in {"passed", "failed"} and "exit_code" not in check:
            raise ReviewError("executed command checks require their actual exit code")
        if status == "passed" and check.get("exit_code", 0) != check.get("expected_exit_code", 0):
            raise ReviewError("a passed command cannot have a failing exit code")
        if "expected_exit_code" in check and "exit_code" not in check:
            raise ReviewError("expected exit codes require an actual command result")
        if check["required"] and status in {"skipped", "unavailable"}:
            unavailable_required.append(check["check_id"])
        if check["required"] and status == "failed":
            failed_required.append(check["check_id"])
    if unavailable_required and review["completion"] == "completed":
        raise ReviewError("unavailable required checks cannot be a completed review")
    if (review["completion"] != "completed" or scope["coverage"] != "full"
            or unavailable_required) and not review["limitations"]:
        raise ReviewError("partial, failed, or sampled reviews must state their limitations")
    for assessment in review["assessments"]:
        if assessment["outcome"] == "supported" and not assessment["evidence_ids"]:
            raise ReviewError("supported assessments require inspected evidence")
        dimensions = assessment.get("dimensions", [])
        _unique([item["name"] for item in dimensions], "assessment dimension names")
        for dimension in dimensions:
            _references(dimension["evidence_ids"], evidence, "dimension evidence references")
        for metric in assessment.get("metrics", []):
            value = metric["value"]
            if not math.isfinite(value):
                raise ReviewError("metrics must be finite")
            if metric.get("minimum", value) > value or metric.get("maximum", value) < value:
                raise ReviewError("metric value is outside its declared scale")
    assessed = {target for item in review["assessments"] for target in item["target_ids"]}
    if set(scope["reviewed_target_ids"]) - assessed:
        raise ReviewError("every reviewed target requires an explicit scoped assessment")
    disposition_assessed = {target for item in review["assessments"]
                            if item["outcome"] in {"supported", "concern"} and item["evidence_ids"]
                            for target in item["target_ids"]}
    open_severe = []
    for finding in review["findings"]:
        _owners(finding, f"finding {finding['finding_id']}")
        if finding.get("native_severity") and not finding.get("normalization_reason"):
            raise ReviewError("native severity requires an explicit normalization reason")
        if finding["status"] != "open" and not finding.get("disposition_reason"):
            raise ReviewError("non-open findings require a disposition reason")
        if finding["status"] in {"resolved", "rejected", "accepted_risk"}:
            if not finding.get("previous_occurrences"):
                raise ReviewError("closed dispositions require an explicit previous finding")
            if (review["completion"] == "failed"
                    or not set(finding["target_ids"]) <= set(scope["reviewed_target_ids"])
                    or not set(finding["target_ids"]) <= disposition_assessed):
                raise ReviewError("terminal findings require actually reviewed, evidence-assessed targets")
        predecessors = finding.get("previous_occurrences", [])
        _unique([(p["repository"].lower(), p["review_id"], p["finding_id"]) for p in predecessors],
                "previous occurrences")
        for previous in predecessors:
            if (previous["repository"].lower() != review["repository"].lower()
                    or previous["review_id"] == review["review_id"]):
                raise ReviewError("previous_occurrences must identify an earlier review in this repository")
        if finding["status"] in OPEN_STATUSES and finding["severity"] in {"blocker", "major"}:
            open_severe.append(finding["finding_id"])
    for action in review["actions"]:
        _owners(action, f"action {action['action_id']}")
        _references(action["finding_ids"], findings, "action finding references")
        _references(action.get("depends_on", []), actions, "action dependencies")
    _acyclic(review["actions"])
    actionable = {f["finding_id"] for f in review["findings"]
                  if f["status"] == "open" and f["severity"] != "informational"}
    planned = {finding_id for action in review["actions"] for finding_id in action["finding_ids"]}
    if actionable - planned:
        raise ReviewError("open findings require proposed actions and acceptance checks")
    for decision in review.get("boundary_decisions", []):
        members = set(decision["target_ids"])
        proposed = decision.get("proposed_groups", [])
        for group in proposed:
            _references(group["target_ids"], members, "proposed group members")
        if decision["action"] == "split":
            flattened = [target for group in proposed for target in group["target_ids"]]
            if len(proposed) < 2 or _unique(flattened, "split members") != members:
                raise ReviewError("a split requires a complete, disjoint partition into at least two groups")
        if decision["action"] == "lump" and len(members) < 2:
            raise ReviewError("a lump requires at least two targets")
        if decision["action"] in {"lump", "split"} and not decision["evidence_ids"]:
            raise ReviewError("lump and split decisions require evidence")
    if review["verdict"] in {"pass", "pass_with_limitations"} and (open_severe or failed_required):
        raise ReviewError("a passing verdict cannot conceal unresolved major/blocker findings or failed required checks")
    if review["verdict"] == "pass" and (
        review["completion"] != "completed" or unavailable_required
        or any(f["status"] in OPEN_STATUSES for f in review["findings"])
    ):
        raise ReviewError("pass requires a completed review with no unresolved findings")
    if review["completion"] == "failed" and review["verdict"] not in {"blocked", "not_assessed"}:
        raise ReviewError("a failed review cannot carry an assessed verdict")
    if review["scientific_review"] and (
        review["verdict"] == "seed_only" or review["reviewer"]["kind"] == "deterministic"
    ):
        raise ReviewError("seed metadata and deterministic validation are not scientific review")
    if review["verdict"] == "pass_with_limitations" and not review["limitations"]:
        raise ReviewError("pass_with_limitations requires explicit limitations")
    if review["verdict"] in {"pass", "pass_with_limitations"}:
        supportive_evidence = {e["evidence_id"] for e in review["evidence"] if e["support"] == "supports"}
        positive = {target for item in review["assessments"]
                    if item["outcome"] == "supported" and supportive_evidence.intersection(item["evidence_ids"])
                    for target in item["target_ids"]}
        if not scope["reviewed_target_ids"] or not set(scope["reviewed_target_ids"]) <= positive:
            raise ReviewError("passing verdicts require positive evidence-linked assessment of reviewed targets")
        if review["verdict"] == "pass" and any(
            item["outcome"] in {"unknown", "concern"} for item in review["assessments"]
        ):
            raise ReviewError("pass cannot conceal unknown or concerning assessments; qualify the verdict")


def content_sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


@contextmanager
def _directory(root: Path, relative: str | None = None, *, create: bool = False):
    """Pin every path component to a no-follow directory descriptor."""
    root = root.absolute()
    if ".." in root.parts:
        raise ReviewError("repository root must not contain parent traversal")
    fd = os.open(root.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for component in root.parts[1:]:
            child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        if relative is not None:
            for component in relative_path(relative).parts:
                if create:
                    try:
                        os.mkdir(component, dir_fd=fd)
                    except FileExistsError:
                        pass
                child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                os.close(fd)
                fd = child
        yield fd
    finally:
        os.close(fd)


@contextmanager
def _input(root: Path, relative: str):
    path = relative_path(relative)
    parent = str(path.parent) if str(path.parent) != "." else None
    with _directory(root, parent) as directory:
        fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            os.close(fd)
            raise ReviewError(f"source must be a regular file: {relative}")
        with os.fdopen(fd, "rb") as stream:
            yield stream


def read_bytes(root: Path, relative: str, *, max_bytes: int = 32 * 1024 * 1024) -> bytes:
    with _input(root, relative) as stream:
        raw = stream.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise ReviewError(f"review document exceeds the {max_bytes} byte limit: {relative}")
    return raw


def file_sha256(root: Path, relative: str) -> str:
    digest = hashlib.sha256()
    with _input(root, relative) as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _git(root: Path, *args: str) -> bytes:
    try:
        return subprocess.check_output(["git", "-C", str(root), *args],
                                       stderr=subprocess.PIPE, timeout=60,
                                       env={**os.environ, "GIT_NO_LAZY_FETCH": "1",
                                            "GIT_TERMINAL_PROMPT": "0"})
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ReviewError(f"Git provenance check failed: {' '.join(args)}") from exc


def repository_identity(root: Path) -> str:
    with _directory(root):
        pass
    top = Path(_git(root, "rev-parse", "--show-toplevel").decode().strip())
    if top != root.absolute():
        raise ReviewError("repo-root must be the exact Git worktree root")
    remote = _git(root, "remote", "get-url", "origin").decode().strip()
    if remote.startswith("git@github.com:"):
        identity = remote.removeprefix("git@github.com:")
    else:
        parsed = urlparse(remote)
        if (parsed.scheme != "https" or parsed.netloc != "github.com"
                or parsed.query or parsed.fragment):
            raise ReviewError("origin must identify an explicit GitHub repository")
        identity = parsed.path.lstrip("/")
    identity = identity.removesuffix(".git")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*/[A-Za-z0-9_.-]+", identity):
        raise ReviewError("invalid GitHub origin identity")
    return identity


def inspect_source(root: Path, targets: list[dict], extra_inputs: Sequence[str] = ()) -> dict:
    """Capture working inputs; this is not a saved or scientifically assessed review."""
    repository = repository_identity(root)
    before = _git(root, "rev-parse", "HEAD").decode().strip()
    paths = sorted({item["path"] for item in targets} | set(extra_inputs))
    if not paths:
        raise ReviewError("inspection requires at least one input")
    inputs = [{"path": name, "sha256": file_sha256(root, name),
               "role": "target" if any(t["path"] == name for t in targets) else "context"}
              for name in paths]
    source = {"git_revision": before, "state": "working_tree", "inputs": inputs}
    assert_current_source(root, {"repository": repository, "source": source})
    return {"status": "inspection_only", "repository": repository, "source": source,
            "targets": targets}


def assert_current_source(root: Path, review: dict) -> None:
    if repository_identity(root).lower() != review["repository"].lower():
        raise ReviewError("review repository does not match the worktree origin")
    source = review["source"]
    if source["state"] == "working_tree":
        if _git(root, "rev-parse", "HEAD").decode().strip() != source["git_revision"]:
            raise ReviewError("working-tree base changed; inspect and reassess")
        for item in source["inputs"]:
            if file_sha256(root, item["path"]) != item["sha256"]:
                raise ReviewError(f"reviewed input changed: {item['path']}")
    else:
        revision = source["git_revision"]
        for item in source["inputs"]:
            relative_path(item["path"])
            mode = _git(root, "ls-tree", "--format=%(objectmode)", revision, "--", item["path"])
            if mode.strip() not in {b"100644", b"100755"}:
                raise ReviewError(f"Git input is not a regular tracked file: {item['path']}")
            raw = _git(root, "cat-file", "blob", f"{revision}:{item['path']}")
            if content_sha256(raw) != item["sha256"]:
                raise ReviewError(f"committed input digest disagrees: {item['path']}")


def _text(value: Any) -> str:
    return html.escape(str(value), quote=False).replace("|", "&#124;").replace("`", "&#96;")


def _table(headers: list[str], rows: list[list]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_text(value).replace("\n", "<br>") for value in row) + " |")
    return lines


def render_markdown(review: dict, schema_path: Path = SCHEMA_PATH) -> str:
    """Derive a human report from the same validated data, never a second verdict."""
    validate_review(review, schema_path)
    source, scope = review["source"], review["scope"]
    lines = [f"# {_text(review['title'])}", "", f"- Review: {_text(review['review_id'])}",
             f"- Repository: {_text(review['repository'])}",
             f"- Started UTC: {review['started_at']}", f"- Finished UTC: {review['finished_at']}",
             f"- Reviewer: {_text(review['reviewer']['identity'])} ({review['reviewer']['independence']})",
             f"- Completion: {review['completion']}", f"- Verdict: {review['verdict']}",
             f"- Scientific review: {str(review['scientific_review']).lower()}",
             "", "## Summary", "", _text(review["summary"]), "", "## Scope And Provenance", "",
             _text(scope["description"]), "", f"Selection: {_text(scope['selection'])}",
             f"Coverage: {scope['coverage']}; {len(scope['reviewed_target_ids'])} reviewed / "
             f"{scope['population_size']} in the declared population.",
             f"Source: {source['state']} at Git base {source['git_revision']}.",
             "Working-tree hashes do not imply those bytes were committed.", ""]
    lines += _table(["Target", "Path / selector", "Kind", "Label"], [
        [t["target_id"], t["path"] + (" # " + t["selector"] if t.get("selector") else ""),
         t["kind"], t["label"]] for t in review["targets"]])
    lines += ["", "## Validation", ""]
    lines += _table(["Check", "Status", "Required", "Targets", "Result"], [
        [c["name"], c["status"], c["required"], ", ".join(c["target_ids"]), c["summary"]]
        for c in review["checks"]])
    lines += ["", "## Scientific And Domain Assessments", ""]
    for item in review["assessments"]:
        lines += [f"### {_text(item['topic'])}", "",
                  f"{item['area']}: {item['outcome']}. Targets: {_text(', '.join(item['target_ids']))}.",
                  "", _text(item["summary"]), ""]
        if item.get("details"):
            lines += [_text(item["details"]), ""]
    lines += ["## Findings", ""]
    if not review["findings"]:
        lines += ["No findings recorded within this review's declared scope.", ""]
    for item in review["findings"]:
        lines += [f"### {_text(item['finding_id'])}: {_text(item['title'])}", "",
                  f"{item['severity']} / {item['status']} / {item['certainty']}; "
                  f"issue key: {_text(item['issue_key'])}.", "", _text(item["description"]), ""]
        if item.get("disposition_reason"):
            lines += ["Disposition: " + _text(item["disposition_reason"]), ""]
    lines += ["## Recommended Actions And Acceptance Checks", ""]
    for item in review["actions"]:
        lines += [f"### {_text(item['action_id'])}", "", _text(item["description"]), ""]
        lines += ["- " + _text(check) for check in item["acceptance_checks"]]
        lines += [""]
    lines += ["## Category Boundaries", ""]
    for item in review.get("boundary_decisions", []):
        lines += [f"- {item['action']}: {_text(', '.join(item['target_ids']))}. " + _text(item["rationale"])]
    lines += ["", "## Evidence", ""]
    lines += _table(["Evidence", "Reference / locator", "Support", "Observation"], [
        [e["evidence_id"], e["reference"] + ("; " + e["locator"] if e.get("locator") else ""),
         e["support"], e["summary"]] for e in review["evidence"]])
    lines += ["", "## Limits And Additional Notes", ""]
    lines += ["- " + _text(note) for note in review["limitations"] + review.get("notes", [])]
    raw = _dump_document(review)
    fence = "`" * max(3, 1 + max((len(m.group()) for m in re.finditer(r"`+", raw)), default=0))
    lines += ["", "## Complete Structured Record", "", "The sibling review.yaml is authoritative.",
              "", fence + "yaml", raw.rstrip(), fence, ""]
    return "\n".join(lines)


def _write_new(directory: int, name: str, data: bytes) -> None:
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=directory)
    with os.fdopen(fd, "wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def save_review(root: Path, review: dict, schema_path: Path = SCHEMA_PATH) -> Path:
    """Append one YAML/Markdown bundle; review.yaml is the atomic commit marker."""
    validate_review(review, schema_path)
    if timestamp(review["finished_at"]) > datetime.now(timezone.utc):
        raise ReviewError("cannot save a review with a future completion time")
    assert_current_source(root, review)
    raw = _dump_document(review).encode("utf-8")
    markdown = render_markdown(review, schema_path).encode("utf-8")
    if max(len(raw), len(markdown)) > 32 * 1024 * 1024:
        raise ReviewError("review document exceeds the byte limit")
    name = review["review_id"]
    relative = f"{REPORT_ROOT}/{name}"
    try:
        with _directory(root, REPORT_ROOT):
            pass
    except FileNotFoundError:
        pass
    # Gitignore checks are prospective: silent local-only reports cannot be fleet evidence.
    ignored = subprocess.run(["git", "-C", str(root), "check-ignore", "--no-index", "--stdin", "-z"],
                             input=f"{relative}/review.yaml\0{relative}/review.md\0".encode(),
                             capture_output=True, timeout=30)
    if ignored.returncode not in {0, 1}:
        raise ReviewError("could not establish review artifact Git visibility")
    if ignored.returncode == 0:
        raise ReviewError("structured review artifacts are ignored; adopt the review path before saving")
    with _directory(root, REPORT_ROOT, create=True) as parent:
        try:
            os.mkdir(name, dir_fd=parent)
        except FileExistsError as exc:
            raise ReviewError("review ID already exists; previous reviews are immutable") from exc
        child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
        temporary = ".review-" + secrets.token_hex(12)
        published = False
        try:
            _write_new(child, "review.md", markdown)
            _write_new(child, temporary, raw)
            assert_current_source(root, review)
            os.link(temporary, "review.yaml", src_dir_fd=child, dst_dir_fd=child,
                    follow_symlinks=False)
            published = True
            os.unlink(temporary, dir_fd=child)
            os.fsync(child)
            os.fsync(parent)
        finally:
            if not published:
                for owned in (temporary, "review.md"):
                    try:
                        os.unlink(owned, dir_fd=child)
                    except FileNotFoundError:
                        pass
            os.close(child)
            if not published:
                os.rmdir(name, dir_fd=parent)
    return root.absolute() / relative / "review.yaml"


def parse_review_bundle(
    relative: str, raw: bytes, markdown: bytes, schema_path: Path = SCHEMA_PATH,
) -> dict:
    """Validate a captured pair from disk or an immutable Git tree."""
    path = relative_path(relative)
    if (len(path.parts) != 4 or path.parts[:2] != tuple(REPORT_ROOT.split("/"))
            or path.name != "review.yaml"):
        raise ReviewError("review must identify a canonical structured bundle")
    review = load_document(raw)
    validate_review(review, schema_path)
    if path.parent.name != review["review_id"]:
        raise ReviewError("review directory and review ID disagree")
    if markdown.decode("utf-8") != render_markdown(review, schema_path):
        raise ReviewError("Markdown does not match the authoritative structured review")
    return review


def read_review(root: Path, relative: str, schema_path: Path = SCHEMA_PATH) -> dict:
    path = relative_path(relative)
    review = parse_review_bundle(relative, read_bytes(root, relative),
                                 read_bytes(root, str(path.with_name("review.md"))), schema_path)
    provenance = source_provenance(root, review)
    if provenance["status"] in {"invalid", "unverified"}:
        raise ReviewError(f"source provenance {provenance['status']}: {provenance['reason']}")
    return review


def source_provenance(root: Path, review: dict) -> dict:
    """Verify retained Git provenance without requiring historical bytes to be current."""
    source = review["source"]
    revision = source["git_revision"]
    try:
        _git(root, "rev-parse", "--verify", f"{revision}^{{commit}}")
        if source["state"] == "working_tree":
            return {"status": "working_tree_attestation",
                    "reason": "Git base exists; dirty input hashes are a reviewer attestation, not committed-byte proof."}
        for item in source["inputs"]:
            mode = _git(root, "ls-tree", "--format=%(objectmode)", revision, "--", item["path"])
            if mode.strip() not in {b"100644", b"100755"}:
                return {"status": "invalid", "reason": f"claimed committed input is absent or nonregular: {item['path']}"}
            raw = _git(root, "cat-file", "blob", f"{revision}:{item['path']}")
            if content_sha256(raw) != item["sha256"]:
                return {"status": "invalid", "reason": f"claimed committed input hash disagrees: {item['path']}"}
        return {"status": "git_commit_verified", "reason": "Historical regular-file blobs match the declared hashes."}
    except (OSError, ReviewError) as exc:
        return {"status": "unverified", "reason": str(exc)}


def review_paths(root: Path) -> list[str]:
    """Include hidden/ignored bundles; refuse symlinks or incomplete publication."""
    try:
        with _directory(root, REPORT_ROOT) as parent:
            entries = sorted(os.listdir(parent))
    except FileNotFoundError:
        return []
    paths = []
    for name in entries:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,159}", name):
            raise ReviewError(f"unexpected entry in structured reviews: {name}")
        relative = f"{REPORT_ROOT}/{name}"
        with _directory(root, relative) as directory:
            if sorted(os.listdir(directory)) != ["review.md", "review.yaml"]:
                raise ReviewError(f"incomplete or unexpected review bundle: {relative}")
        paths.append(f"{relative}/review.yaml")
    return paths


def assert_append_only(root: Path, base: str) -> None:
    """Compare actual retained bytes with a trusted Git base, including dirty edits."""
    revision = _git(root, "rev-parse", "--verify", "--end-of-options", f"{base}^{{commit}}").decode().strip()
    entries = _git(root, "ls-tree", "-r", "-z", revision, "--", REPORT_ROOT)
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        metadata, encoded_path = entry.split(b"\t", 1)
        mode, kind, object_id = metadata.split(b" ")
        relative = encoded_path.decode("utf-8")
        relative_path(relative)
        if mode not in {b"100644", b"100755"} or kind != b"blob":
            raise ReviewError(f"review baseline contains a nonregular entry: {relative}")
        size = int(_git(root, "cat-file", "-s", object_id.decode()).strip())
        if size > 32 * 1024 * 1024:
            raise ReviewError(f"review baseline exceeds the byte limit: {relative}")
        original = _git(root, "cat-file", "blob", object_id.decode())
        try:
            current = read_bytes(root, relative)
        except OSError as exc:
            raise ReviewError(f"structured reviews are append-only; missing or unsafe: {relative}") from exc
        if current != original:
            raise ReviewError(f"structured reviews are append-only; changed: {relative}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH,
                        help="Canonical LinkML schema; vendored callers supply its explicit local path.")
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="capture inputs; not a saved review")
    inspect.add_argument("--targets", type=Path, required=True,
                         help="YAML/JSON mapping containing a targets list")
    inspect.add_argument("--input", action="append", default=[], help="additional context input path")
    validate = commands.add_parser("validate", help="validate supplied structured records, not source freshness")
    validate.add_argument("paths", type=Path, nargs="+")
    save = commands.add_parser("save", help="append supplied completed content as a YAML/Markdown bundle")
    save.add_argument("--content", type=Path, required=True)
    render = commands.add_parser("render", help="render supplied structured content to stdout")
    render.add_argument("--content", type=Path, required=True)
    check = commands.add_parser("check", help="validate all retained bundles, including ignored files")
    check.add_argument("--require-reviews", action="store_true")
    check.add_argument("--base", default=os.environ.get("RECORD_REVIEW_BASE", "HEAD"),
                       help="trusted Git base for append-only checks; CI must supply its event base")
    commands.add_parser("list", help="emit validated review metadata")
    args = parser.parse_args(argv)
    try:
        if not args.schema.is_file() or args.schema.is_symlink():
            raise ReviewError("supply --schema with the regular canonical record_review.yaml file")
        if args.command == "inspect":
            spec = load_document(args.targets.read_bytes())
            if set(spec) != {"targets"} or not isinstance(spec["targets"], list) or not spec["targets"]:
                raise ReviewError("inspection requires a nonempty targets list")
            for target in spec["targets"]:
                if not isinstance(target, dict) or not isinstance(target.get("path"), str):
                    raise ReviewError("inspection targets require explicit repository-relative paths")
            print(json.dumps(inspect_source(args.repo_root, spec["targets"], args.input), indent=2))
        elif args.command == "validate":
            for path in args.paths:
                validate_review(load_document(path.read_bytes()), args.schema)
            print(json.dumps({"valid_reviews": len(args.paths)}))
        elif args.command in {"save", "render"}:
            content = load_document(args.content.read_bytes())
            if args.command == "save":
                path = save_review(args.repo_root, content, args.schema)
                print(json.dumps({"review": str(path), "markdown": str(path.with_name("review.md"))}))
            else:
                print(render_markdown(content, args.schema), end="")
        else:
            identity = repository_identity(args.repo_root)
            if args.command == "check":
                assert_append_only(args.repo_root, args.base)
            paths = review_paths(args.repo_root)
            if getattr(args, "require_reviews", False) and not paths:
                raise ReviewError("no structured reviews exist; absence is not reviewed coverage")
            records = []
            for relative in paths:
                review = read_review(args.repo_root, relative, args.schema)
                if review["repository"].lower() != identity.lower():
                    raise ReviewError(f"foreign review found in {identity}: {relative}")
                records.append({"path": relative, **{key: review[key] for key in (
                    "review_id", "repository", "kind", "finished_at", "completion", "verdict",
                    "scientific_review", "scope", "targets",
                )}})
            print(json.dumps(records if args.command == "list" else {
                "repository": identity, "valid_reviews": len(records),
                "coverage": "no_structured_reviews" if not records else "declared_scopes_only",
            }, indent=2))
    except (ReviewError, OSError, UnicodeError, TypeError, subprocess.TimeoutExpired) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
