#!/usr/bin/env python3
"""Check a Mech's governed files against an immutable claw revision.

This file is deliberately standalone and uses only the Python standard
library.  The canonical copy is vendored into every Mech, but it obtains the
artifact set from claw's single manifest at the exact commit recorded in
``scripts/.vendored_canon_ref``.  No provider or model API is involved.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any

CANONICAL_REPOSITORY = "CultureBotAI/culturebotai-claw"
CANONICAL_MANIFEST_PATH = "src/kg_microbe_governance/vendored_artifacts.json"
DEFAULT_PIN_PATH = "scripts/.vendored_canon_ref"
DEFAULT_TIMEOUT_SECONDS = 5.0
MAX_DOWNLOAD_BYTES = 8 * 1024 * 1024

_SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_KEY_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
_PATH_PART_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")
_GITHUB_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?/"
    r"[A-Za-z0-9_.-]+$"
)


class GovernanceError(ValueError):
    """Raised when a governance input cannot be trusted."""


class CanonicalFetchError(GovernanceError):
    """Raised for a potentially transient canonical-source fetch failure."""


@dataclass(frozen=True)
class Consumer:
    key: str
    github: str
    package_path: str


@dataclass(frozen=True)
class Artifact:
    artifact_id: str
    source: str
    target: str
    consumers: tuple[str, ...]
    sha256: str
    mode: int

    def applies_to(self, consumer_key: str) -> bool:
        return not self.consumers or consumer_key in self.consumers


@dataclass(frozen=True)
class GovernanceManifest:
    canonical_repository: str
    pin_path: str
    consumers: Mapping[str, Consumer]
    artifacts: tuple[Artifact, ...]

    def consumer_for(self, identity: str) -> Consumer:
        lowered = identity.lower()
        for consumer in self.consumers.values():
            if consumer.key.lower() == lowered or consumer.github.lower() == lowered:
                return consumer
        known = ", ".join(
            consumer.github for consumer in self.consumers.values()
        )
        raise GovernanceError(
            f"Unknown Mech repository identity {identity!r}; expected one of: {known}"
        )

    def artifacts_for(self, consumer: Consumer) -> tuple[Artifact, ...]:
        return tuple(
            artifact
            for artifact in self.artifacts
            if artifact.applies_to(consumer.key)
        )


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise GovernanceError(f"Governance manifest has duplicate key {key!r}")
        result[key] = value
    return result


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise GovernanceError(f"{label} must be an object")
    return value


def _strict_keys(
    value: Mapping[str, Any], allowed: set[str], required: set[str], label: str
) -> None:
    unknown = set(value) - allowed
    missing = required - set(value)
    if unknown:
        raise GovernanceError(
            f"{label} has unknown keys: {', '.join(sorted(unknown))}"
        )
    if missing:
        raise GovernanceError(
            f"{label} is missing keys: {', '.join(sorted(missing))}"
        )


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise GovernanceError(f"{label} must be a non-empty trimmed string")
    if any(character in value for character in ("\x00", "\r", "\n", "\t")):
        raise GovernanceError(f"{label} contains a control character")
    return value


def _relative_path(value: Any, label: str, *, template: bool = False) -> str:
    path = _string(value, label)
    if unicodedata.normalize("NFC", path) != path:
        raise GovernanceError(f"{label} must use canonical Unicode spelling")
    if "\\" in path:
        raise GovernanceError(f"{label} must use POSIX separators")
    if path.startswith(":"):
        raise GovernanceError(f"{label} must not use Git pathspec magic")
    if template and (
        path.count("{package_path}") > 1
        or any(
            "{package_path}" in part and part != "{package_path}"
            for part in path.split("/")
        )
    ):
        raise GovernanceError(
            f"{label} may contain {{package_path}} once as a complete path segment"
        )
    probe = path.replace("{package_path}", "package") if template else path
    if "{" in probe or "}" in probe:
        raise GovernanceError(f"{label} contains an unsupported template field")
    pure = PurePosixPath(probe)
    if (
        pure.is_absolute()
        or not pure.parts
        or pure.as_posix() != probe
        or any(part in {"", ".", ".."} for part in pure.parts)
    ):
        raise GovernanceError(f"{label} must be a safe canonical relative path")
    if any(part.casefold() == ".git" for part in pure.parts):
        raise GovernanceError(f"{label} must not address Git metadata")
    if any(
        part != "{package_path}" and not _PATH_PART_PATTERN.fullmatch(part)
        for part in path.split("/")
    ):
        raise GovernanceError(
            f"{label} contains characters unsafe for Git and canonical URLs"
        )
    if any(any(character in part for character in "*?[]") for part in pure.parts):
        raise GovernanceError(f"{label} must not contain glob syntax")
    return path


def _portable_parts(path: str) -> tuple[str, ...]:
    return tuple(
        unicodedata.normalize("NFC", part).casefold()
        for part in PurePosixPath(path).parts
    )


def _paths_conflict(left: str, right: str) -> bool:
    """Detect aliases and file/descendant conflicts on portable filesystems."""

    left_parts = _portable_parts(left)
    right_parts = _portable_parts(right)
    shared = min(len(left_parts), len(right_parts))
    return left_parts[:shared] == right_parts[:shared]


def parse_manifest(data: bytes) -> GovernanceManifest:
    """Parse and validate the canonical JSON manifest fail-closed."""

    try:
        document = json.loads(data.decode("utf-8"), object_pairs_hook=_reject_duplicate_pairs)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise GovernanceError(f"Unable to parse governance manifest: {exc}") from exc
    root = _mapping(document, "Governance manifest")
    _strict_keys(
        root,
        {"version", "canonical_repository", "pin_path", "consumers", "artifacts"},
        {"version", "canonical_repository", "pin_path", "consumers", "artifacts"},
        "Governance manifest",
    )
    if (
        not isinstance(root["version"], int)
        or isinstance(root["version"], bool)
        or root["version"] != 1
    ):
        raise GovernanceError("Governance manifest version must be integer 1")
    canonical_repository = _string(
        root["canonical_repository"], "canonical_repository"
    )
    if canonical_repository != CANONICAL_REPOSITORY:
        raise GovernanceError(
            "Governance manifest canonical_repository does not match the "
            f"checker authority {CANONICAL_REPOSITORY}"
        )
    pin_path = _relative_path(root["pin_path"], "pin_path")

    raw_consumers = _mapping(root["consumers"], "consumers")
    if not raw_consumers:
        raise GovernanceError("consumers must not be empty")
    consumers: dict[str, Consumer] = {}
    github_identities: set[str] = set()
    package_paths: set[str] = set()
    for raw_key, raw_consumer in raw_consumers.items():
        key = _string(raw_key, "consumer key")
        if not _KEY_PATTERN.fullmatch(key):
            raise GovernanceError(f"Invalid consumer key {key!r}")
        consumer_mapping = _mapping(raw_consumer, f"consumers.{key}")
        _strict_keys(
            consumer_mapping,
            {"github", "package_path"},
            {"github", "package_path"},
            f"consumers.{key}",
        )
        github = _string(consumer_mapping["github"], f"consumers.{key}.github")
        if (
            not _GITHUB_PATTERN.fullmatch(github)
            or github.rsplit("/", 1)[-1] in {".", ".."}
        ):
            raise GovernanceError(
                f"consumers.{key}.github must be an owner/repository identity"
            )
        package_path = _relative_path(
            consumer_mapping["package_path"], f"consumers.{key}.package_path"
        )
        if github.lower() in github_identities:
            raise GovernanceError(f"Duplicate consumer GitHub identity {github!r}")
        if package_path in package_paths:
            raise GovernanceError(f"Duplicate consumer package path {package_path!r}")
        github_identities.add(github.lower())
        package_paths.add(package_path)
        consumers[key] = Consumer(key, github, package_path)

    raw_artifacts = root["artifacts"]
    if not isinstance(raw_artifacts, list) or not raw_artifacts:
        raise GovernanceError("artifacts must be a non-empty array")
    artifacts: list[Artifact] = []
    artifact_ids: set[str] = set()
    targets_by_consumer: dict[str, list[str]] = {
        key: [pin_path] for key in consumers
    }
    for index, raw_artifact in enumerate(raw_artifacts):
        label = f"artifacts[{index}]"
        artifact_mapping = _mapping(raw_artifact, label)
        _strict_keys(
            artifact_mapping,
            {"id", "source", "target", "consumers", "sha256", "mode"},
            {"id", "source", "target", "consumers", "sha256", "mode"},
            label,
        )
        artifact_id = _string(artifact_mapping["id"], f"{label}.id")
        if not _KEY_PATTERN.fullmatch(artifact_id):
            raise GovernanceError(f"{label}.id is not a valid identifier")
        if artifact_id in artifact_ids:
            raise GovernanceError(f"Duplicate artifact id {artifact_id!r}")
        artifact_ids.add(artifact_id)
        source = _relative_path(artifact_mapping["source"], f"{label}.source")
        if not source.startswith("src/kg_microbe_governance/artifacts/"):
            raise GovernanceError(
                f"{label}.source must be under the canonical artifact directory"
            )
        target = _relative_path(
            artifact_mapping["target"], f"{label}.target", template=True
        )
        raw_scope = artifact_mapping["consumers"]
        if raw_scope == "all":
            scope: tuple[str, ...] = ()
        elif isinstance(raw_scope, list) and raw_scope:
            scope_values = [
                _string(value, f"{label}.consumers") for value in raw_scope
            ]
            if len(scope_values) != len(set(scope_values)):
                raise GovernanceError(f"{label}.consumers contains duplicates")
            unknown_consumers = set(scope_values) - set(consumers)
            if unknown_consumers:
                raise GovernanceError(
                    f"{label}.consumers names unknown consumers: "
                    f"{', '.join(sorted(unknown_consumers))}"
                )
            scope = tuple(scope_values)
        else:
            raise GovernanceError(
                f"{label}.consumers must be 'all' or a non-empty key array"
            )
        digest = _string(artifact_mapping["sha256"], f"{label}.sha256")
        if not _SHA256_PATTERN.fullmatch(digest):
            raise GovernanceError(f"{label}.sha256 must be 64 lowercase hex digits")
        mode_text = _string(artifact_mapping["mode"], f"{label}.mode")
        if mode_text not in {"0644", "0755"}:
            raise GovernanceError(f"{label}.mode must be 0644 or 0755")
        mode = int(mode_text, 8)
        artifact = Artifact(artifact_id, source, target, scope, digest, mode)
        for consumer in consumers.values():
            if not artifact.applies_to(consumer.key):
                continue
            expanded = expand_target(artifact, consumer)
            for existing in targets_by_consumer[consumer.key]:
                if _paths_conflict(existing, expanded):
                    raise GovernanceError(
                        f"Conflicting targets {existing!r} and {expanded!r} "
                        f"for consumer {consumer.key}"
                    )
            targets_by_consumer[consumer.key].append(expanded)
        artifacts.append(artifact)

    for consumer in consumers.values():
        if not any(artifact.applies_to(consumer.key) for artifact in artifacts):
            raise GovernanceError(f"Consumer {consumer.key} has no governed artifacts")
    return GovernanceManifest(
        canonical_repository=canonical_repository,
        pin_path=pin_path,
        consumers=MappingProxyType(consumers),
        artifacts=tuple(artifacts),
    )


def expand_target(artifact: Artifact, consumer: Consumer) -> str:
    """Expand the sole supported target placeholder and revalidate the result."""

    expanded = artifact.target.replace("{package_path}", consumer.package_path)
    return _relative_path(expanded, f"expanded target for {artifact.artifact_id}")


def read_pin(root: Path, pin_path: str = DEFAULT_PIN_PATH) -> str:
    """Read an exact immutable commit pin from a regular, non-symlink file."""

    root = root.resolve()
    relative = _relative_path(pin_path, "pin path")
    path = _safe_local_file(root, relative)
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise GovernanceError(f"Unable to read canonical pin {relative}: {exc}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise GovernanceError(f"Canonical pin {relative} must be a regular file")
    if metadata.st_mode & 0o111:
        raise GovernanceError(f"Canonical pin {relative} must not be executable")
    if metadata.st_mode & (stat.S_IWGRP | stat.S_IWOTH):
        raise GovernanceError(
            f"Canonical pin {relative} must not be group/other-writable"
        )
    try:
        content = path.read_text(encoding="ascii")
    except (OSError, UnicodeError) as exc:
        raise GovernanceError(f"Unable to read canonical pin {relative}: {exc}") from exc
    pin = content.strip()
    if not _SHA_PATTERN.fullmatch(pin):
        raise GovernanceError(
            f"Canonical pin {relative} must contain exactly one 40-character SHA"
        )
    if content not in {pin, pin + "\n"}:
        raise GovernanceError(f"Canonical pin {relative} contains extra content")
    return pin


def raw_url(ref: str, relative_path: str) -> str:
    if not _SHA_PATTERN.fullmatch(ref):
        raise GovernanceError("Canonical ref must be a full 40-character SHA")
    safe_path = _relative_path(relative_path, "canonical path")
    return (
        "https://raw.githubusercontent.com/"
        f"{CANONICAL_REPOSITORY}/{ref}/{safe_path}"
    )


def fetch_url(url: str, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> bytes:
    """Fetch a size- and wall-time-bounded canonical artifact."""

    if timeout <= 0:
        raise GovernanceError("Canonical fetch timeout must be positive")
    request = urllib.request.Request(url, headers={"User-Agent": "kg-microbe-governance/1"})
    deadline = time.monotonic() + timeout
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            final_url = urllib.parse.urlsplit(response.geturl())
            if (
                final_url.scheme != "https"
                or final_url.hostname != "raw.githubusercontent.com"
            ):
                destination = (
                    f"{final_url.scheme or '<missing-scheme>'}://"
                    f"{final_url.hostname or '<missing-host>'}"
                )
                raise CanonicalFetchError(
                    "Canonical fetch redirected outside raw.githubusercontent.com: "
                    f"{destination}"
                )
            declared = response.headers.get("Content-Length")
            if declared is not None and (
                int(declared) < 0 or int(declared) > MAX_DOWNLOAD_BYTES
            ):
                raise CanonicalFetchError(
                    f"Canonical artifact exceeds {MAX_DOWNLOAD_BYTES} bytes"
                )
            data = bytearray()
            while len(data) <= MAX_DOWNLOAD_BYTES:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise CanonicalFetchError(
                        f"Canonical artifact fetch exceeded {timeout:g} seconds"
                    )
                # CPython's HTTPS response exposes the active socket here. Set
                # each blocking read to the remaining total budget; the
                # fallback still checks the deadline between chunks.
                try:
                    response.fp.raw._sock.settimeout(max(0.001, remaining))
                except AttributeError:
                    pass
                chunk = response.read(
                    min(64 * 1024, MAX_DOWNLOAD_BYTES + 1 - len(data))
                )
                if not chunk:
                    break
                data.extend(chunk)
    except (OSError, ValueError, urllib.error.URLError) as exc:
        raise CanonicalFetchError(
            f"Unable to fetch canonical artifact {url}: {exc}"
        ) from exc
    if len(data) > MAX_DOWNLOAD_BYTES:
        raise CanonicalFetchError(
            f"Canonical artifact exceeds {MAX_DOWNLOAD_BYTES} bytes"
        )
    return bytes(data)


def _git_environment() -> dict[str, str]:
    """Return an environment with repository-routing Git variables removed."""

    environment = {
        key: value
        for key, value in os.environ.items()
        if not key.upper().startswith("GIT_")
    }
    # Replacement refs can make object inspection differ from what the recorded
    # commit would push. Promisor lazy-fetches would also evade the explicitly
    # bounded canonical HTTPS path. Both must fail closed for local evidence.
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    environment["GIT_NO_LAZY_FETCH"] = "1"
    return environment


def _run_git(root: Path, arguments: Sequence[str], *, timeout: float = 5) -> str:
    try:
        result = subprocess.run(
            ["git", "-c", "core.fsmonitor=false", *arguments],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=_git_environment(),
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise GovernanceError(f"Git repository inspection failed at {root}") from exc
    return result.stdout


def _normalize_remote(remote: str) -> str:
    patterns = (
        r"^https://github\.com/(?P<identity>[^/]+/[^/]+?)(?:\.git)?$",
        r"^git@github\.com:(?P<identity>[^/]+/[^/]+?)(?:\.git)?$",
        r"^ssh://git@github\.com/(?P<identity>[^/]+/[^/]+?)(?:\.git)?$",
    )
    for pattern in patterns:
        match = re.fullmatch(pattern, remote)
        if match:
            return match.group("identity")
    raise GovernanceError("Unsupported or non-GitHub origin URL")


def _remote_identity(root: Path) -> str:
    remotes: list[str] = []
    for arguments in (
        ("remote", "get-url", "--all", "origin"),
        ("remote", "get-url", "--push", "--all", "origin"),
    ):
        output = _run_git(root, arguments)
        values = [line.strip() for line in output.splitlines() if line.strip()]
        if not values:
            raise GovernanceError("Git origin must define fetch and push URLs")
        remotes.extend(values)
    identities = {_normalize_remote(remote).lower(): remote for remote in remotes}
    if len(identities) != 1:
        raise GovernanceError(
            "Every origin fetch and push URL must identify the same GitHub repository"
        )
    return _normalize_remote(next(iter(identities.values())))


def _validate_git_repository(root: Path) -> tuple[Path, str]:
    """Require a real exact worktree root and return its verified origin identity."""

    try:
        metadata = root.lstat()
    except OSError as exc:
        raise GovernanceError(f"Repository root is unavailable: {root}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
        raise GovernanceError(f"Repository root must be a real directory: {root}")
    resolved = root.resolve()
    top_level = Path(_run_git(resolved, ("rev-parse", "--show-toplevel")).strip()).resolve()
    if top_level != resolved:
        raise GovernanceError(
            f"Repository root must be the exact Git worktree root: {resolved} != {top_level}"
        )
    return resolved, _remote_identity(resolved)


def _safe_local_file(root: Path, relative_path: str) -> Path:
    resolved_root = root.resolve()
    safe_relative = _relative_path(relative_path, "local artifact path")
    parts = PurePosixPath(safe_relative).parts
    candidate = resolved_root / safe_relative
    current = resolved_root
    for index, part in enumerate(parts):
        current = current / part
        if not current.exists() and not current.is_symlink():
            continue
        metadata = current.lstat()
        if stat.S_ISLNK(metadata.st_mode):
            raise GovernanceError(f"Local artifact path traverses a symlink: {current}")
        if index < len(parts) - 1 and not stat.S_ISDIR(metadata.st_mode):
            raise GovernanceError(
                f"Local artifact parent is not a directory: {current}"
            )
    try:
        candidate.resolve(strict=False).relative_to(resolved_root)
    except (OSError, ValueError) as exc:
        raise GovernanceError(
            f"Local artifact path escapes repository root: {relative_path}"
        ) from exc
    return candidate


def check_repository(
    root: Path,
    repository: str | None = None,
    *,
    fetch: Callable[[str], bytes] | None = None,
) -> tuple[int, tuple[str, ...]]:
    """Return ``(checked_count, problems)`` without modifying the repository."""

    root, actual_identity = _validate_git_repository(root)
    pin = read_pin(root)
    fetcher = fetch or fetch_url
    manifest_bytes = fetcher(raw_url(pin, CANONICAL_MANIFEST_PATH))
    manifest = parse_manifest(manifest_bytes)
    consumer = manifest.consumer_for(actual_identity)
    asserted_identity = repository or os.environ.get("GITHUB_REPOSITORY")
    if asserted_identity is not None:
        asserted_consumer = manifest.consumer_for(asserted_identity)
        if asserted_consumer.key != consumer.key:
            raise GovernanceError(
                f"Asserted repository {asserted_identity!r} disagrees with "
                f"origin {actual_identity!r}"
            )
    if manifest.pin_path != DEFAULT_PIN_PATH:
        raise GovernanceError(
            f"Canonical manifest pin path is {manifest.pin_path!r}; checker expects "
            f"{DEFAULT_PIN_PATH!r}"
        )

    checked = 0
    problems: list[str] = []
    for artifact in manifest.artifacts_for(consumer):
        canonical = fetcher(raw_url(pin, artifact.source))
        digest = hashlib.sha256(canonical).hexdigest()
        if digest != artifact.sha256:
            problems.append(
                f"CANONICAL ERROR: {artifact.source} checksum differs from manifest"
            )
            continue
        target = expand_target(artifact, consumer)
        try:
            local_path = _safe_local_file(root, target)
        except GovernanceError as exc:
            problems.append(f"UNSAFE: {target}: {exc}")
            continue
        if not local_path.is_file():
            problems.append(f"MISSING: {target}")
            continue
        try:
            local = local_path.read_bytes()
            local_mode = local_path.stat().st_mode
            executable = bool(local_mode & stat.S_IXUSR)
        except OSError as exc:
            problems.append(f"ERROR: cannot read {target}: {exc}")
            continue
        if local != canonical:
            problems.append(
                f"DRIFT: {target} differs from {CANONICAL_REPOSITORY}@{pin[:8]}"
            )
        expected_executable = bool(artifact.mode & stat.S_IXUSR)
        if executable != expected_executable:
            expected = "executable" if expected_executable else "non-executable"
            problems.append(f"MODE: {target} must be {expected}")
        if local_mode & (stat.S_IWGRP | stat.S_IWOTH):
            problems.append(f"MODE: {target} must not be group/other-writable")
        checked += 1
    return checked, tuple(problems)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check vendored Mech artifacts against an immutable claw commit"
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--repository",
        help="Mech key or exact owner/repository identity (normally auto-detected)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        checked, problems = check_repository(args.root, args.repository)
    except CanonicalFetchError as exc:
        print(f"FETCH ERROR: {exc}", file=sys.stderr)
        return 1
    except GovernanceError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print(
            f"Vendored drift detected ({len(problems)} problem(s), {checked} checked).",
            file=sys.stderr,
        )
        return 1
    print(f"OK: {checked} governed artifacts match the pinned claw revision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
