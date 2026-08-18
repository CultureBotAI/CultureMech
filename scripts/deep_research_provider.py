#!/usr/bin/env python3
"""Triage deep-research providers for a Mech-specific research focus.

The provider facts mirror deep-research-client/DisMech, while the YAML profile
keeps each Mech's evidence target, sources, and stage weights local to that KB.
No provider is called and no credential value is read or printed.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Provider:
    name: str
    label: str
    source_scope: str
    synthesis: str
    cost: str
    time: str
    capabilities: frozenset[str]
    best_for: str
    limitation: str


PROVIDERS: dict[str, Provider] = {
    "asta": Provider(
        "asta",
        "Asta",
        "scientific corpus",
        "none",
        "low",
        "fast",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "snippets",
            }
        ),
        "fast paper and passage discovery",
        "retrieval packet only; no narrative synthesis",
    ),
    "falcon": Provider(
        "falcon",
        "Edison / Falcon",
        "scientific literature",
        "deep",
        "high",
        "slow",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "synthesis",
            }
        ),
        "scientific evidence synthesis",
        "academic sources only; paid and slower",
    ),
    "openscientist": Provider(
        "openscientist",
        "OpenScientist",
        "PubMed and scientific literature",
        "agentic",
        "high",
        "very_slow",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "hypothesis_tracking",
            }
        ),
        "iterative mechanism and hypothesis research",
        "long-running and PubMed-focused",
    ),
    "claude_code": Provider(
        "claude_code",
        "Claude Code",
        "open web",
        "agentic",
        "medium",
        "slow",
        frozenset(
            {
                "web_search",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "structured_databases",
            }
        ),
        "broad web/database source coverage",
        "quality depends on web access and local CLI authentication",
    ),
    "openai": Provider(
        "openai",
        "OpenAI Deep Research",
        "open web",
        "deep",
        "very_high",
        "very_slow",
        frozenset(
            {
                "web_search",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "real_time_data",
                "structured_databases",
            }
        ),
        "comprehensive multi-source synthesis",
        "highest cost and long response times",
    ),
    "perplexity": Provider(
        "perplexity",
        "Perplexity",
        "open web",
        "deep",
        "high",
        "slow",
        frozenset(
            {
                "web_search",
                "citation_tracking",
                "synthesis",
                "real_time_data",
                "multi_language",
                "structured_databases",
            }
        ),
        "current web research with source links",
        "less specialized for primary scientific evidence",
    ),
    "consensus": Provider(
        "consensus",
        "Consensus",
        "peer-reviewed literature",
        "summary",
        "low",
        "fast",
        frozenset({"academic_search", "citation_tracking", "scientific_literature"}),
        "quick peer-reviewed evidence checks",
        "limited depth and no general web/database search",
    ),
    "cyberian": Provider(
        "cyberian",
        "Cyberian",
        "agent-selected web and literature",
        "agentic",
        "high",
        "very_slow",
        frozenset(
            {
                "web_search",
                "academic_search",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "structured_databases",
            }
        ),
        "custom iterative research workflows",
        "requires local agent tooling and careful authority limits",
    ),
    "cborg": Provider(
        "cborg",
        "CBORG proxy",
        "model-dependent open web",
        "deep",
        "medium",
        "slow",
        frozenset(
            {"web_search", "citation_tracking", "synthesis", "code_interpretation"}
        ),
        "OpenAI-compatible research through the LBL proxy",
        "capabilities depend on the selected proxy model",
    ),
    "mock": Provider(
        "mock",
        "Mock",
        "fixtures",
        "none",
        "low",
        "fast",
        frozenset(),
        "tests and dry runs",
        "never supplies real evidence",
    ),
    "deeper_med": Provider(
        "deeper_med",
        "DeepER-Med",
        "biomedical databases",
        "agentic",
        "high",
        "slow",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "synthesis",
                "structured_databases",
            }
        ),
        "future biomedical evidence workflows",
        "stub: no public API is available",
    ),
}

ALIASES = {"edison": "falcon", "futurehouse": "falcon", "claude-code": "claude_code"}
COST_VALUE = {"low": 1, "medium": 2, "high": 3, "very_high": 4}
TIME_VALUE = {"fast": 1, "medium": 2, "slow": 3, "very_slow": 4}
SYNTHESIS_VALUE = {"none": 0, "summary": 1, "deep": 2, "agentic": 3}


def canonical_provider(name: str) -> str:
    key = name.strip().casefold().replace(" ", "_")
    return ALIASES.get(key, key)


def provider_status(
    provider: str, environ: Mapping[str, str] | None = None
) -> tuple[str, str]:
    """Return status and a safe explanation without exposing credential values."""
    env = os.environ if environ is None else environ
    if provider == "deeper_med":
        return "stub", "no public API"
    if provider == "mock":
        enabled = env.get("ENABLE_MOCK_PROVIDER", "").casefold() in {"1", "true", "yes"}
        return (
            ("available", "enabled")
            if enabled
            else ("unavailable", "set ENABLE_MOCK_PROVIDER=true")
        )
    if provider == "claude_code":
        return (
            ("available", "local CLI")
            if shutil.which("claude")
            else ("unavailable", "claude CLI not found")
        )
    if provider == "cyberian":
        installed = importlib.util.find_spec("cyberian") is not None
        return (
            ("available", "local package")
            if installed
            else ("unavailable", "install the cyberian extra")
        )

    credentials = {
        "asta": ("ASTA_API_KEY",),
        "falcon": ("EDISON_API_KEY", "EDISON_PLATFORM_API_KEY", "FUTUREHOUSE_API_KEY"),
        "openscientist": ("OPENSCIENTIST_API_KEY",),
        "openai": ("OPENAI_API_KEY",),
        "perplexity": ("PERPLEXITY_API_KEY",),
        "consensus": ("CONSENSUS_API_KEY",),
        "cborg": ("CBORG_API_KEY",),
    }
    keys = credentials.get(provider, ())
    if any(env.get(key) for key in keys):
        return "available", "credential configured"
    return "unavailable", f"set {' or '.join(keys)}"


def load_config(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Provider profile must be a YAML mapping: {path}")
    focuses = data.get("focuses")
    if not isinstance(focuses, dict) or not focuses:
        raise ValueError("Provider profile requires a non-empty 'focuses' mapping")
    default_focus = data.get("default_focus")
    if default_focus not in focuses:
        raise ValueError(
            f"default_focus {default_focus!r} is not defined under focuses"
        )
    for focus_name, focus in focuses.items():
        if not isinstance(focus, dict) or not isinstance(focus.get("stages"), dict):
            raise ValueError(f"Focus {focus_name!r} requires a 'stages' mapping")
        for stage_name, stage in focus["stages"].items():
            if not isinstance(stage, dict):
                raise ValueError(f"Stage {focus_name}.{stage_name} must be a mapping")
            capabilities = stage.get("capabilities", {})
            if not isinstance(capabilities, dict):
                raise ValueError(
                    f"Stage {focus_name}.{stage_name}.capabilities must be a mapping"
                )
    return data


def _score(
    provider: Provider, stage: Mapping[str, Any], adjustments: Mapping[str, Any]
) -> float:
    capabilities = stage.get("capabilities", {})
    score = sum(
        float(weight)
        for capability, weight in capabilities.items()
        if capability in provider.capabilities
    )
    score += (
        float(stage.get("synthesis_weight", 0)) * SYNTHESIS_VALUE[provider.synthesis]
    )
    score += float(stage.get("speed_weight", 0)) * (5 - TIME_VALUE[provider.time])
    score += float(stage.get("cost_weight", 0)) * (5 - COST_VALUE[provider.cost])
    score += float(adjustments.get(provider.name, 0))
    return score


def rank_stage(
    config: Mapping[str, Any], focus_name: str, stage_name: str
) -> list[dict[str, Any]]:
    focus = config["focuses"][focus_name]
    stage = focus["stages"][stage_name]
    adjustments = focus.get("provider_adjustments", {})
    raw = {
        name: _score(provider, stage, adjustments)
        for name, provider in PROVIDERS.items()
    }
    high = max(raw.values()) or 1.0
    rows = []
    for name, provider in PROVIDERS.items():
        status, reason = provider_status(name)
        rows.append(
            {
                "provider": name,
                "label": provider.label,
                "status": status,
                "status_reason": reason,
                "fit": round(100 * max(0.0, raw[name]) / high),
                "cost": provider.cost,
                "time": provider.time,
                "synthesis": provider.synthesis,
                "source_scope": provider.source_scope,
                "best_for": provider.best_for,
                "limitation": provider.limitation,
            }
        )
    return sorted(rows, key=lambda row: (-row["fit"], row["provider"]))


def build_report(config: Mapping[str, Any], focus_name: str) -> dict[str, Any]:
    focus = config["focuses"][focus_name]
    stages = []
    for stage_name, stage in focus["stages"].items():
        ranking = rank_stage(config, focus_name, stage_name)
        available = [
            row
            for row in ranking
            if row["status"] == "available" and row["provider"] != "mock"
        ]
        stages.append(
            {
                "name": stage_name,
                "objective": stage.get("objective", ""),
                "ranking": ranking,
                "recommended_available": available[0] if available else None,
                "fallback_available": available[1] if len(available) > 1 else None,
            }
        )
    return {
        "mech": config.get("mech", "Mech"),
        "target": config.get("target", ""),
        "focus": focus_name,
        "focus_label": focus.get("label", focus_name),
        "objective": focus.get("objective", ""),
        "evidence_policy": config.get("evidence_policy", ""),
        "source_priorities": focus.get("source_priorities", []),
        "stages": stages,
    }


def _table(rows: list[dict[str, Any]]) -> str:
    headers = ("Provider", "Status", "Fit", "Cost", "Time", "Synthesis", "Source scope")
    values = [headers]
    for row in rows:
        values.append(
            (
                row["provider"],
                row["status"],
                str(row["fit"]),
                row["cost"],
                row["time"],
                row["synthesis"],
                row["source_scope"],
            )
        )
    widths = [
        max(len(str(row[index])) for row in values) for index in range(len(headers))
    ]
    lines = [
        "  ".join(
            str(value).ljust(widths[index]) for index, value in enumerate(values[0])
        )
    ]
    lines.append("  ".join("-" * width for width in widths))
    lines.extend(
        "  ".join(str(value).ljust(widths[index]) for index, value in enumerate(row))
        for row in values[1:]
    )
    return "\n".join(lines)


def print_report(report: Mapping[str, Any], provider_name: str | None = None) -> None:
    print(f"{report['mech']} deep-research provider triage")
    print(f"Target: {report['target']}")
    print(f"Focus: {report['focus']} — {report['focus_label']}")
    print(f"Objective: {report['objective']}")
    print(f"Evidence gate: {report['evidence_policy']}")
    if report["source_priorities"]:
        print("Source priorities: " + "; ".join(report["source_priorities"]))

    for stage in report["stages"]:
        print(f"\n[{stage['name']}] {stage['objective']}")
        rows = stage["ranking"]
        if provider_name:
            rows = [row for row in rows if row["provider"] == provider_name]
        print(_table(rows))
        if provider_name and rows:
            row = rows[0]
            print(f"Best for: {row['best_for']}")
            print(f"Limitation: {row['limitation']}")
            print(f"Availability: {row['status_reason']}")
        elif stage["recommended_available"]:
            primary = stage["recommended_available"]
            fallback = stage["fallback_available"]
            message = f"Route now: {primary['provider']} ({primary['best_for']})"
            if fallback:
                message += f"; cross-check/fallback: {fallback['provider']}"
            print(message)
        else:
            print(
                "Route now: no real provider is currently available; configure a listed credential or CLI."
            )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", type=Path, required=True, help="Mech provider profile YAML"
    )
    parser.add_argument(
        "--focus", help="Research focus from the profile (default: profile default)"
    )
    parser.add_argument(
        "--provider", help="Show one provider (aliases such as edison are accepted)"
    )
    parser.add_argument(
        "--list-focuses", action="store_true", help="List domain-specific focuses"
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit machine-readable triage JSON"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = load_config(args.config)
    if args.list_focuses:
        for name, focus in config["focuses"].items():
            marker = " (default)" if name == config["default_focus"] else ""
            print(f"{name}{marker}: {focus.get('label', name)}")
        return 0
    focus_name = args.focus or config["default_focus"]
    if focus_name not in config["focuses"]:
        choices = ", ".join(config["focuses"])
        raise ValueError(f"Unknown focus {focus_name!r}; choose one of: {choices}")
    provider_name = canonical_provider(args.provider) if args.provider else None
    if provider_name and provider_name not in PROVIDERS:
        raise ValueError(
            f"Unknown provider {args.provider!r}; choose one of: {', '.join(PROVIDERS)}"
        )
    report = build_report(config, focus_name)
    if args.json:
        if provider_name:
            for stage in report["stages"]:
                stage["ranking"] = [
                    row for row in stage["ranking"] if row["provider"] == provider_name
                ]
        print(json.dumps(report, indent=2))
    else:
        print_report(report, provider_name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
