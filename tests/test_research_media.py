"""Tests for CultureMech deep research command wiring."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_media import (  # noqa: E402
    build_command,
    build_provider_command,
    load_media,
    provider_args,
    research_env,
    resolve_media_file,
    template_vars,
)


def test_resolve_media_file_finds_slug_record():
    path = resolve_media_file("ko2_no3")
    assert path == REPO_ROOT / "data" / "normalized_yaml" / "bacterial" / "ko2_no3.yaml"


def test_resolve_media_file_finds_culturemech_identifier():
    path = resolve_media_file("CultureMech:008318")
    assert path == REPO_ROOT / "data" / "normalized_yaml" / "bacterial" / "ko2_no3.yaml"


def test_template_vars_include_media_context():
    path = resolve_media_file("ko2_no3")
    variables = template_vars(load_media(path), path)
    assert variables["media_id"] == "CultureMech:008318"
    assert variables["media_name"] == "ko2_no3"
    assert variables["original_name"] == "KO2(NO3)"
    assert variables["category"] == "bacterial"
    assert "NaNO3" in variables["ingredients"]
    assert variables["record_path"] == "data/normalized_yaml/bacterial/ko2_no3.yaml"


def test_provider_args_mirror_dismech_cborg_shortcut():
    assert provider_args("falcon") == ["--provider", "falcon"]
    assert provider_args("cborg") == ["--use-cborg"]


def test_build_command_for_falcon_media_research():
    command = build_command(
        provider="falcon",
        template=Path("templates/media_growth_research.md"),
        output_file=Path("research/media/bacterial/ko2_no3-deep-research-falcon.md"),
        citations_file=Path("research/media/bacterial/ko2_no3-deep-research-falcon.md.citations.md"),
        variables={"media_name": "ko2_no3", "media_id": "CultureMech:008318"},
        passthrough_args=["--max-cost", "1"],
    )
    assert command[:4] == [
        "deep-research-client",
        "research",
        "--template",
        "templates/media_growth_research.md",
    ]
    assert "--provider" in command
    assert "falcon" in command
    assert "--separate-citations" in command
    assert "research/media/bacterial/ko2_no3-deep-research-falcon.md.citations.md" in command
    assert command[-2:] == ["--max-cost", "1"]


def test_build_provider_command_for_falcon():
    assert build_provider_command(provider="falcon") == [
        "deep-research-client",
        "providers",
        "--provider",
        "falcon",
    ]


def test_research_env_maps_futurehouse_key_to_edison(monkeypatch):
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "test-key")
    env = research_env("falcon")
    assert env["EDISON_API_KEY"] == "test-key"
