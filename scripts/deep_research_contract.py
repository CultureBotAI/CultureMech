#!/usr/bin/env python3
"""Fleet contract for native Codex research and provider canaries.

``culturebotai-claw`` is the canonical copy. Mechs vendor this file
byte-for-byte and pin the immutable claw revision that supplied it.

The Codex lane deliberately does not route through deep-research-client's
``cyberian`` adapter. It invokes ``codex --search exec`` directly, requires a
JSON-schema response, validates the response locally, and only then publishes
the markdown report with an atomic rename.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import tempfile
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

DEFAULT_MIN_CHARS = 1_000
DEFAULT_MIN_SOURCES = 3
DEFAULT_TIMEOUT = 1_800
OPENSCIENTIST_KEY = "OPENSCIENTIST_API_KEY"
OPENSCIENTIST_URL = "OPENSCIENTIST_URL"
_URL = re.compile(r"https?://[^\s)\]>,]+", re.IGNORECASE)
_PLACEHOLDER = re.compile(r"\{([a-z][a-z0-9_]*)\}")


class ContractError(RuntimeError):
    """A provider or output failed the fleet research contract."""


@dataclass(frozen=True)
class ValidationSummary:
    characters: int
    sources: int


@dataclass(frozen=True)
class CanaryResult:
    provider: str
    ok: bool
    detail: str


def _canonical_url(value: str) -> str:
    value = value.strip().rstrip(".,;:")
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ContractError(f"invalid source URL: {value!r}")
    return urlunsplit(
        (
            parsed.scheme.casefold(),
            parsed.netloc.casefold(),
            parsed.path,
            parsed.query,
            "",
        )
    )


def codex_output_schema(min_sources: int = DEFAULT_MIN_SOURCES) -> dict[str, Any]:
    """Schema passed to ``codex exec --output-schema`` and rechecked locally."""
    if min_sources < 1:
        raise ValueError("min_sources must be at least 1")
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["report_markdown", "sources", "limitations"],
        "properties": {
            "report_markdown": {"type": "string"},
            "sources": {
                "type": "array",
                "minItems": min_sources,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["title", "url"],
                    "properties": {
                        "title": {"type": "string"},
                        "url": {"type": "string"},
                    },
                },
            },
            "limitations": {"type": "array", "items": {"type": "string"}},
        },
    }


def render_prompt_template(template: Path, variables: Mapping[str, str]) -> str:
    """Fill a Mech prompt and refuse to send unresolved named placeholders."""
    body = template.read_text(encoding="utf-8")
    for key, value in variables.items():
        body = body.replace("{" + key + "}", str(value))
    missing = sorted(set(_PLACEHOLDER.findall(body)))
    if missing:
        raise ContractError(f"unfilled research template placeholders: {missing}")
    return body


def build_codex_command(
    *,
    repo_root: Path,
    schema_path: Path,
    response_path: Path,
    executable: str = "codex",
) -> list[str]:
    """Build the canonical non-interactive, web-enabled, read-only command."""
    return [
        executable,
        "--search",
        "--ask-for-approval",
        "never",
        "exec",
        "--ephemeral",
        "--sandbox",
        "read-only",
        "--cd",
        str(repo_root),
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(response_path),
        "-",
    ]


def validate_codex_payload(
    payload: Any,
    *,
    min_chars: int = DEFAULT_MIN_CHARS,
    min_sources: int = DEFAULT_MIN_SOURCES,
) -> ValidationSummary:
    """Apply semantic checks JSON Schema alone cannot express."""
    if not isinstance(payload, dict):
        raise ContractError("Codex response must be a JSON object")
    if set(payload) != {"report_markdown", "sources", "limitations"}:
        raise ContractError("Codex response has missing or unexpected top-level fields")

    report = payload["report_markdown"]
    if not isinstance(report, str) or len(report.strip()) < min_chars:
        actual = len(report.strip()) if isinstance(report, str) else 0
        raise ContractError(
            f"research report is too short: {actual} characters; require {min_chars}"
        )
    limitations = payload["limitations"]
    if not isinstance(limitations, list) or not all(
        isinstance(item, str) and item.strip() for item in limitations
    ):
        raise ContractError("limitations must be a list of non-empty strings")

    sources = payload["sources"]
    if not isinstance(sources, list):
        raise ContractError("sources must be a list")
    urls: set[str] = set()
    for source in sources:
        if not isinstance(source, dict) or set(source) != {"title", "url"}:
            raise ContractError("each source must contain exactly title and url")
        if not isinstance(source["title"], str) or not source["title"].strip():
            raise ContractError("each source title must be non-empty")
        if not isinstance(source["url"], str):
            raise ContractError("each source URL must be a string")
        urls.add(_canonical_url(source["url"]))
    if len(urls) < min_sources:
        raise ContractError(
            f"research report has {len(urls)} distinct sources; require {min_sources}"
        )
    return ValidationSummary(characters=len(report.strip()), sources=len(urls))


def render_codex_payload(payload: Mapping[str, Any]) -> str:
    """Render validated structured output as the fleet's markdown artifact."""
    lines = [str(payload["report_markdown"]).strip(), "", "## Sources", ""]
    for source in payload["sources"]:
        lines.append(f"- [{source['title']}]({source['url']})")
    if payload["limitations"]:
        lines.extend(["", "## Limitations", ""])
        lines.extend(f"- {item}" for item in payload["limitations"])
    return "\n".join(lines).rstrip() + "\n"


def run_codex_research(
    prompt: str,
    destination: Path,
    *,
    repo_root: Path,
    timeout: int = DEFAULT_TIMEOUT,
    min_chars: int = DEFAULT_MIN_CHARS,
    min_sources: int = DEFAULT_MIN_SOURCES,
    executable: str = "codex",
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> ValidationSummary:
    """Run Codex and atomically publish a report only after full validation."""
    if not prompt.strip():
        raise ContractError("research prompt must not be empty")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="codex-research-") as temp_dir:
        temp = Path(temp_dir)
        schema_path = temp / "output.schema.json"
        response_path = temp / "response.json"
        schema_path.write_text(
            json.dumps(codex_output_schema(min_sources), indent=2) + "\n",
            encoding="utf-8",
        )
        command = build_codex_command(
            repo_root=repo_root,
            schema_path=schema_path,
            response_path=response_path,
            executable=executable,
        )
        try:
            completed = runner(
                command,
                input=prompt,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise ContractError(
                f"codex exec timed out after {timeout} seconds"
            ) from exc
        if completed.returncode:
            detail = (completed.stderr or completed.stdout or "").strip()[-800:]
            raise ContractError(
                f"codex exec failed with exit {completed.returncode}: {detail}"
            )
        if not response_path.is_file():
            raise ContractError(
                "codex exec succeeded without writing its structured response"
            )
        try:
            payload = json.loads(response_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ContractError("codex exec returned invalid JSON") from exc
        summary = validate_codex_payload(
            payload, min_chars=min_chars, min_sources=min_sources
        )
        rendered = render_codex_payload(payload)
        publish_path = destination.with_name(f".{destination.name}.tmp")
        publish_path.write_text(rendered, encoding="utf-8")
        os.replace(publish_path, destination)
        return summary


def validate_openscientist_credential(environ: Mapping[str, str]) -> str:
    """Validate documented ``name:secret`` shape without returning the secret."""
    raw = environ.get(OPENSCIENTIST_KEY, "")
    if not raw:
        raise ContractError(f"set {OPENSCIENTIST_KEY}=name:secret")
    name, separator, secret = raw.partition(":")
    if not separator or not name.strip() or not secret.strip():
        raise ContractError(f"{OPENSCIENTIST_KEY} must use the name:secret format")
    return name.strip()


def codex_canary(
    *,
    executable: str = "codex",
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> CanaryResult:
    """Check CLI capabilities and authentication without starting research."""
    if shutil.which(executable) is None and executable == "codex":
        return CanaryResult("codex", False, "codex executable not found on PATH")
    checks: Sequence[tuple[list[str], tuple[str, ...]]] = (
        ([executable, "--help"], ("--search",)),
        ([executable, "exec", "--help"], ("--output-schema", "--output-last-message")),
        ([executable, "login", "status"], ("Logged in",)),
    )
    for command, required in checks:
        try:
            completed = runner(
                command, capture_output=True, text=True, timeout=20, check=False
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return CanaryResult(
                "codex", False, f"could not run {' '.join(command[:2])}: {exc}"
            )
        output = (completed.stdout or "") + (completed.stderr or "")
        if completed.returncode or any(token not in output for token in required):
            return CanaryResult(
                "codex", False, f"{' '.join(command[:2])} failed the capability check"
            )
    return CanaryResult(
        "codex", True, "CLI authenticated; web search and schema output supported"
    )


def openscientist_canary(
    *,
    environ: Mapping[str, str] | None = None,
    client_command: str = "deep-research-client",
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> CanaryResult:
    """Check credential shape and client discovery without submitting a paid job."""
    env = os.environ if environ is None else environ
    try:
        validate_openscientist_credential(env)
    except ContractError as exc:
        return CanaryResult("openscientist", False, str(exc))
    try:
        completed = runner(
            [*shlex.split(client_command), "providers"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            env=dict(env),
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return CanaryResult("openscientist", False, f"provider discovery failed: {exc}")
    output = (completed.stdout or "") + (completed.stderr or "")
    if completed.returncode or "openscientist" not in output.casefold():
        return CanaryResult(
            "openscientist", False, "deep-research-client did not list openscientist"
        )
    return CanaryResult(
        "openscientist",
        True,
        "credential shape valid and provider discovered; no job submitted",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provider", choices=("codex", "openscientist", "all"))
    parser.add_argument("--codex-command", default="codex")
    parser.add_argument("--client-command", default="deep-research-client")
    args = parser.parse_args(argv)
    results: list[CanaryResult] = []
    if args.provider in {"codex", "all"}:
        results.append(codex_canary(executable=args.codex_command))
    if args.provider in {"openscientist", "all"}:
        results.append(openscientist_canary(client_command=args.client_command))
    for result in results:
        label = "OK" if result.ok else "BLOCKED"
        print(f"{label}: {result.provider}: {result.detail}")
    return 0 if all(result.ok for result in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
