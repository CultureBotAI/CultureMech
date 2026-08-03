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


def test_resolve_media_file_accepts_relative_path():
    path = resolve_media_file("data/normalized_yaml/bacterial/ko2_no3.yaml")
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


# --- tiered resolution (#151 item 3) --------------------------------------


def test_exact_filename_wins_over_a_shared_name_field():
    """The bug that blocked slug-driven batches.

    2,291 record `name:` values are shared by more than one record, and every one
    is also some other record's filename. `lb_broth` matches
    `bacterial/lb_broth.yaml` by filename and `bacterial/TOGO_M3227_LB_broth.yaml`
    by its `name:` field; treating those as equally good made the resolver raise on
    all 2,291.
    """
    assert resolve_media_file("lb_broth").name == "lb_broth.yaml"


def test_culturemech_id_resolves_each_record_of_a_name_collision():
    """The id tier is the escape hatch — it must reach BOTH sides of a collision."""
    assert resolve_media_file("CultureMech:009646").name == "lb_broth.yaml"
    assert resolve_media_file("CultureMech:009666").name == "TOGO_M3227_LB_broth.yaml"


def test_the_issue_151_case_resolves():
    """`syntrophomonas_medium_for_syntrophospora_cellicola_19j_3` has a TOGO_M520_*
    sibling carrying the same recipe; #151 records it raising ValueError."""
    path = resolve_media_file("syntrophomonas_medium_for_syntrophospora_cellicola_19j_3")
    assert path.name == "syntrophomonas_medium_for_syntrophospora_cellicola_19j_3.yaml"


def test_a_genuine_cross_directory_filename_collision_still_raises():
    """Ranking must not paper over real ambiguity.

    `potato_dextrose_agar` exists in BOTH bacterial/ and fungal/ — two files with
    the same stem. No tier can separate them, so raising is correct; silently
    picking one would hide the collisions #151 tracks.
    """
    import pytest

    with pytest.raises(ValueError, match="equally specifically"):
        resolve_media_file("potato_dextrose_agar")


def test_an_absent_target_still_raises_not_found():
    import pytest

    with pytest.raises(FileNotFoundError):
        resolve_media_file("no_such_medium_anywhere_xyz")
