"""Tests for CultureMech deep research command wiring."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_media import (  # noqa: E402
    DEFAULT_FOCUS,
    FOCUS_TEMPLATES,
    build_command,
    build_provider_command,
    focus_template,
    load_media,
    output_name,
    parse_args,
    provider_args,
    research_env,
    resolve_focus,
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
        output_file=Path(
            "research/media/bacterial/ko2_no3-deep-research-growth_evidence-falcon.md"
        ),
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
    assert command[-2:] == ["--max-cost", "1"]


# --- citation artifact contract (#289) ------------------------------------


def test_separate_citation_sidecars_are_never_requested():
    """The client's sidecar is a regex over report prose and is not evidence.

    CultureMech produced exactly one before this was disabled
    (`research/media/algae/2asw-deep-research-falcon.md.citations.md`): it
    re-emits the whole rendered prompt as "Query", lists the bare string `Na+`
    as entry 12 of 27, and repeats 10.1101/2024.06.09.598106 three times over
    (entries 16, 17, 24) differing only in trailing punctuation. TraitMech
    reached the same verdict over 353 sidecars.

    The authoritative citation record is the report's own References section.
    """
    command = build_command(
        provider="claude_code",
        template=Path("templates/media_growth_research.md"),
        output_file=Path("research/media/bacterial/x.md"),
        variables={},
        passthrough_args=[],
    )
    assert "--separate-citations" not in command
    assert not any(arg.endswith(".citations.md") for arg in command)


# --- entity-runner contract (#289) ----------------------------------------


def test_every_focus_maps_to_a_template_that_exists():
    """A focus that names a missing prompt would fail only at dispatch time."""
    for name, template in FOCUS_TEMPLATES.items():
        assert template.exists(), f"focus {name} points at a missing template"


def test_each_focus_selects_a_distinct_template():
    """The defect #289 names: focuses that all fall back to the default prompt.

    Ranking providers for `formulation` and then rendering the growth prompt is
    exactly the disconnect between triage and dispatch that the issue reports.
    """
    templates = [t.name for t in FOCUS_TEMPLATES.values()]
    assert len(set(templates)) == len(templates)
    assert FOCUS_TEMPLATES["growth_evidence"].name == "media_growth_research.md"
    assert FOCUS_TEMPLATES["formulation"].name == "media_recipe_validation.md"


def test_focus_defaults_and_validates():
    assert resolve_focus(None) == DEFAULT_FOCUS
    assert resolve_focus("formulation") == "formulation"
    assert focus_template("formulation").name == "media_recipe_validation.md"

    import pytest

    with pytest.raises(ValueError, match="Unknown focus"):
        resolve_focus("no_such_focus")


def test_output_name_carries_the_focus_even_for_the_default():
    """A caller must be able to predict the path from (slug, focus, provider)
    alone, without also knowing which focus happens to be the default."""
    assert output_name(
        media_slug="ko2_no3", focus="growth_evidence", provider="falcon"
    ) == "ko2_no3-deep-research-growth_evidence-falcon.md"
    assert output_name(
        media_slug="ko2_no3", focus="formulation", provider="claude_code"
    ) == "ko2_no3-deep-research-formulation-claude_code.md"


def test_focus_and_provider_both_change_the_output_path():
    """Two focuses must not collide on one filename and overwrite each other."""
    names = {
        output_name(media_slug="m", focus=f, provider=p)
        for f in FOCUS_TEMPLATES
        for p in ("falcon", "claude_code")
    }
    assert len(names) == 2 * len(FOCUS_TEMPLATES)


def test_cli_defaults_to_the_default_focus_and_no_template_override():
    args = parse_args(["--provider", "falcon", "--target", "ko2_no3"])
    assert args.focus == DEFAULT_FOCUS
    assert args.template is None


def test_cli_rejects_an_unknown_focus():
    import pytest

    with pytest.raises(SystemExit):
        parse_args(["--provider", "falcon", "--target", "x", "--focus", "nope"])


def test_the_research_media_alias_takes_no_positional_focus():
    """Pins the signature that keeps existing callers working.

    Adding a positional `focus` to `research-media` silently broke the
    documented form ``just research-media claude_code ko2_no3 --dry-run``:
    `--dry-run` bound to `focus`, so the runner received `--focus --dry-run`,
    failed argparse, and never ran the dry run. Flags may follow the target
    directly here; `research-entity` is the recipe that takes a positional
    focus.
    """
    recipes = [
        line.strip().rstrip(":")
        for line in (REPO_ROOT / "project.justfile").read_text().splitlines()
        if line.startswith(("research-media ", "research-entity "))
    ]
    assert len(recipes) == 2, f"expected both recipes, found {recipes}"
    assert 'research-media provider target *args=""' in recipes
    assert 'research-entity provider target focus="growth_evidence" *args=""' in recipes


def test_the_recipes_quote_the_values_that_can_contain_spaces():
    """Record `name:` values contain spaces, and a target may be one.

    `just research-media claude_code "LB Broth"` expands `{{target}}` unquoted,
    so the shell split it into two words. The alias made that worse by expanding
    it a second time through the recursive `just` call: `LB` became the target
    and `Broth` became the focus. Quoted, the resolver receives `LB Broth` whole
    and answers properly — here, that it is ambiguous between
    `lb_broth.yaml` and `TOGO_M3227_LB_broth.yaml`, which is the useful answer.

    `{{args}}` is deliberately NOT quoted: it is a word list, and quoting it
    would collapse `--max-cost 1` into a single argument.
    """
    body = (REPO_ROOT / "project.justfile").read_text()
    for fragment in (
        '--provider "{{provider}}"',
        '--target "{{target}}"',
        '--focus="{{focus}}"',
        '@just research-entity "{{provider}}" "{{target}}" growth_evidence {{args}}',
    ):
        assert fragment in body, f"unquoted expansion, expected: {fragment}"


def test_explicit_template_still_overrides_the_focus():
    """Special-purpose prompts (the #150 stock-solution repair, axis
    classification, phase-2 extraction) stay reachable without inventing a
    standing focus for each."""
    args = parse_args(
        [
            "--provider", "falcon", "--target", "x",
            "--template", "templates/media_stock_solution_research.md",
        ]
    )
    assert args.template == Path("templates/media_stock_solution_research.md")


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
