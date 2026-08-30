from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = REPO_ROOT / "scripts" / "deep_research_provider.py"
CONFIG_PATH = REPO_ROOT / "conf" / "deep_research_provider.yaml"
SPEC = importlib.util.spec_from_file_location("deep_research_provider", MODULE_PATH)
assert SPEC and SPEC.loader
drp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = drp
SPEC.loader.exec_module(drp)


def _run_json(extra):
    """Run main() with --json and return the parsed document."""
    import contextlib
    import io
    import json

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        drp.main(["--config", str(CONFIG_PATH), "--json", *extra])
    return json.loads(buf.getvalue())


def _run_text(extra):
    """Run main() without --json and return the printed text."""
    import contextlib
    import io

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        drp.main(["--config", str(CONFIG_PATH), *extra])
    return buf.getvalue()


def test_profile_has_domain_specific_default_and_three_stage_triage():
    config = drp.load_config(CONFIG_PATH)
    focus = config["focuses"][config["default_focus"]]

    assert config["mech"].endswith("Mech")
    assert config["target"]
    assert set(focus["stages"]) == {"discovery", "synthesis", "verification"}
    assert focus["source_priorities"]


@pytest.mark.parametrize("alias", ["edison", "futurehouse", "Falcon"])
def test_edison_aliases_resolve_to_falcon(alias):
    assert drp.canonical_provider(alias) == "falcon"


def test_falcon_platform_key_is_recognized_without_exposing_it():
    """Credential RECOGNITION, asked of `credential_status`.

    `provider_status` now reports falcon as blocked whatever the credential says
    (#290), so this has to ask the lower-level question or adding a provider to
    KNOWN_BLOCKED would silently drop the check that its env-var aliases are
    spelled right.
    """
    status, reason = drp.credential_status(
        "falcon", {"EDISON_PLATFORM_API_KEY": "secret"}
    )
    assert status == "available"
    assert reason == "credential configured"
    assert "secret" not in reason


def test_explicit_empty_environment_does_not_fall_back_to_process_credentials():
    status, reason = drp.provider_status("asta", {})
    assert status == "unavailable"
    assert reason == "set ASTA_API_KEY"


def test_codex_is_a_native_cli_provider(monkeypatch):
    monkeypatch.setattr(
        drp.shutil, "which", lambda name: "/bin/codex" if name == "codex" else None
    )
    status, reason = drp.provider_status("codex", {})
    assert status == "available"
    assert "contract canary" in reason
    assert "codex" in drp.PROVIDERS


def test_every_focus_ranks_all_real_and_stub_providers(monkeypatch):
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)

    for focus_name in config["focuses"]:
        report = drp.build_report(config, focus_name)
        for stage in report["stages"]:
            names = {row["provider"] for row in stage["ranking"]}
            assert names == set(drp.PROVIDERS)
            assert stage["recommended_available"] is not None
            assert stage["recommended_available"]["status"] == "available"


def test_unknown_default_focus_is_rejected(tmp_path):
    profile = tmp_path / "bad.yaml"
    profile.write_text("default_focus: absent\nfocuses:\n  present:\n    stages: {}\n")
    with pytest.raises(ValueError, match="default_focus"):
        drp.load_config(profile)


# --- provider_adjustments / capabilities validation -------------------------


def test_provider_adjustments_alias_key_is_canonicalized(tmp_path):
    profile = tmp_path / "aliased.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      edison: 3\n"
        "      Claude Code: 2\n"
    )
    config = drp.load_config(profile)
    adjustments = config["focuses"]["f"]["provider_adjustments"]
    assert adjustments == {"falcon": 3, "claude_code": 2}


def test_provider_adjustments_explicit_null_is_rejected(tmp_path):
    """focus.get("provider_adjustments", {}) only supplies the {} default
    when the key is absent — an explicit YAML `provider_adjustments: null`
    still returns None, which used to skip validation entirely (guarded
    behind `if adjustments is not None:`) and crash later in
    rank_stage/_score with AttributeError instead of this clean
    ValueError."""
    profile = tmp_path / "nulladj.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments: null\n"
    )
    with pytest.raises(ValueError, match="provider_adjustments must be a mapping"):
        drp.load_config(profile)


def test_provider_adjustments_null_value_is_rejected(tmp_path):
    """The key-shape validation above (unknown/duplicate keys) never checked
    that the VALUE is numeric — a profile with provider_adjustments:
    {asta: null} loaded cleanly and crashed later in _score's
    float(adjustments.get(...)) with an uncaught TypeError instead of this
    ValueError."""
    profile = tmp_path / "nulladjvalue.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      asta: null\n"
    )
    with pytest.raises(ValueError, match="must be a number"):
        drp.load_config(profile)


def test_provider_adjustments_unknown_key_is_rejected(tmp_path):
    profile = tmp_path / "typo.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      flacon: 3\n"  # typo of "falcon"
    )
    with pytest.raises(ValueError, match="unknown provider"):
        drp.load_config(profile)


def test_provider_adjustments_colliding_aliases_are_rejected(tmp_path):
    """Two raw keys that canonicalize to the same provider (edison/falcon)
    must not silently let the second overwrite the first."""
    profile = tmp_path / "collision.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      edison: 3\n"
        "      falcon: 5\n"
    )
    with pytest.raises(ValueError, match="multiple"):
        drp.load_config(profile)


def test_stage_capabilities_unknown_key_is_rejected(tmp_path):
    profile = tmp_path / "badcap.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery:\n"
        "        capabilities:\n"
        "          acadmic_search: 5\n"  # typo of "academic_search"
    )
    with pytest.raises(ValueError, match="unknown capability"):
        drp.load_config(profile)


def test_stage_capabilities_yaml_bool_key_still_raises_value_error(tmp_path):
    """PyYAML's safe_load (YAML 1.1) parses an unquoted `no:` key as the
    Python bool False. Mixed into a dict with a genuine unknown string
    capability, `sorted(unknown_caps)` used to raise TypeError comparing
    str to bool instead of the intended ValueError."""
    profile = tmp_path / "boolkey.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery:\n"
        "        capabilities:\n"
        "          no: 5\n"
        "          acadmic_search: 3\n"
    )
    with pytest.raises(ValueError, match="unknown capability"):
        drp.load_config(profile)


def test_provider_adjustment_actually_changes_rank_order(monkeypatch):
    """Config-loading validation alone doesn't prove the bonus reaches the
    ranking — this proves it does."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))

    baseline = drp.rank_stage(config, focus_name, stage_name)
    target = min(baseline, key=lambda row: row["fit"])["provider"]
    baseline_fit = {row["provider"]: row["fit"] for row in baseline}

    config["focuses"][focus_name]["provider_adjustments"] = {target: 1000}
    boosted = drp.rank_stage(config, focus_name, stage_name)
    boosted_fit = {row["provider"]: row["fit"] for row in boosted}

    assert boosted_fit[target] > baseline_fit[target]
    assert boosted[0]["provider"] == target


def test_exact_zero_max_score_does_not_divide_by_zero(monkeypatch):
    """`high = max(raw.values()); if high <= 0: high = 1.0` exists to guard
    an exact-zero max (every raw score landing at 0, e.g. through cancelling
    adjustments) from a ZeroDivisionError. It does NOT make the ranking
    meaningful when every score is negative — that's CultureMech#315, a
    separate, harder problem (0.0 divided by any nonzero number, positive or
    negative, is still 0.0, so this guard is a no-op for the negative case).
    This test covers only what the guard actually does."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))
    # Zero out every capability weight and adjustment so every raw score is
    # exactly 0.0 — the precise edge case `or 1.0` was written for.
    stage = config["focuses"][focus_name]["stages"][stage_name]
    stage["capabilities"] = {}
    stage["synthesis_weight"] = 0
    stage["speed_weight"] = 0
    stage["cost_weight"] = 0
    config["focuses"][focus_name]["provider_adjustments"] = {}

    rows = drp.rank_stage(config, focus_name, stage_name)  # must not raise ZeroDivisionError
    assert all(row["fit"] == 0 for row in rows)


def test_negative_nonzero_max_score_does_not_divide_by_zero_either(monkeypatch):
    """Distinct code path from the exact-zero test above (max(raw.values())
    is a genuinely negative number here, not exactly 0, so this exercises
    the `high <= 0` half of the guard's condition rather than only the
    `high == 0` half). The *outcome* is unavoidably identical either way —
    `fit = round(100 * max(0.0, raw[name]) / high)` clamps any negative raw
    score to 0.0 in the numerator before the division even happens, so no
    test can make the divisor's value (old `or 1.0`'s actual-negative-number
    vs. this guard's 1.0 fallback) produce a different result. That's
    exactly the CultureMech#315 problem: for negative scores, `high`'s value
    is provably irrelevant. This test only pins down "doesn't crash and
    yields 0" for a non-uniform negative distribution, which the exact-zero
    test's uniform-zero input doesn't exercise."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))
    stage = config["focuses"][focus_name]["stages"][stage_name]
    stage["capabilities"] = {}
    stage["synthesis_weight"] = 0
    stage["speed_weight"] = 0
    stage["cost_weight"] = 0
    # Every provider negative, but not uniformly so — max(raw.values()) is a
    # genuinely negative number rather than exactly 0.
    config["focuses"][focus_name]["provider_adjustments"] = {
        name: (-2 if name == "asta" else -1) for name in drp.PROVIDERS
    }

    rows = drp.rank_stage(config, focus_name, stage_name)  # must not raise ZeroDivisionError
    assert all(row["fit"] == 0 for row in rows)


# --- policy and machine-readable consistency (#290) ------------------------


def test_a_measured_dead_provider_is_not_recommended(monkeypatch):
    """The tool used to contradict the justfile beside it.

    #284 measured falcon returning HTTP 402 and cyberian HTTP 500, and recorded
    both in the provider table. The triage tool still routed every stage to
    falcon, because "available" only ever meant "an env var is set".
    """
    status, reason = drp.provider_status("falcon", {"EDISON_API_KEY": "secret"})
    assert status == "blocked"
    assert "402" in reason
    assert "secret" not in reason

    # Exercise the override end-to-end through rank_stage/build_report, not
    # just the direct provider_status() call above. With no credentials set
    # at all every provider is "unavailable" and recommended_available is
    # None for an unrelated reason, making an assertion against
    # build_report() vacuous unless falcon is actually made
    # "available"-but-blocked here.
    monkeypatch.setenv("EDISON_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    report = drp.build_report(config, config["default_focus"])
    for stage in report["stages"]:
        falcon_row = next(row for row in stage["ranking"] if row["provider"] == "falcon")
        assert falcon_row["status"] == "blocked"
        # Checking recommended_available's None-or-not-blocked would still
        # pass vacuously if nothing else happens to be available either —
        # assert against recommendable() directly instead, which has no
        # None-branch escape hatch.
        assert "falcon" not in {row["provider"] for row in drp.recommendable(stage["ranking"])}


def test_provider_filtered_json_never_recommends_a_provider_it_did_not_rank(monkeypatch):
    """`--provider asta --json` recommended claude_code out of a document whose
    only ranked provider was asta. The human path took a different branch, so
    only machine consumers saw it."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    out = _run_json(["--provider", "asta"])
    for stage in out["stages"]:
        ranked = {row["provider"] for row in stage["ranking"]}
        assert ranked == {"asta"}
        recommended = stage["recommended_available"]
        assert recommended is None or recommended["provider"] in ranked
        fallback = stage["fallback_available"]
        assert fallback is None or fallback["provider"] in ranked


def test_no_paid_keeps_the_medium_cost_provider(monkeypatch):
    """`medium` is not "paid" here: claude_code is the medium-cost provider and
    keeping it is the point of asking."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    report = drp.build_report(config, config["default_focus"], no_paid=True)
    for stage in report["stages"]:
        recommended = stage["recommended_available"]
        if recommended:
            assert recommended["cost"] not in drp.PAID_COSTS


def test_an_allowlist_confines_the_recommendation(monkeypatch):
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    report = drp.build_report(config, config["default_focus"],
                              allow=frozenset({"asta"}))
    for stage in report["stages"]:
        recommended = stage["recommended_available"]
        assert recommended is None or recommended["provider"] == "asta"
        # The full ranking is still reported — the allowlist bounds the
        # RECOMMENDATION, it does not hide what else exists.
        assert len(stage["ranking"]) == len(drp.PROVIDERS)


def test_an_unknown_provider_in_the_allowlist_is_rejected():
    with pytest.raises(ValueError, match="Unknown provider"):
        drp.main(["--config", str(CONFIG_PATH), "--allow", "not_a_provider"])


def test_allow_mock_is_rejected_rather_than_silently_unrecommendable():
    """mock passes the "is it a known provider" check in --allow (it's a real
    PROVIDERS key), but recommendable() unconditionally excludes it — so
    --allow mock used to run without error and silently never recommend
    anything, with no diagnostic explaining why."""
    with pytest.raises(ValueError, match="mock"):
        drp.main(["--config", str(CONFIG_PATH), "--allow", "mock"])


def test_stage_capability_null_weight_is_rejected(tmp_path):
    """Same null-vs-absent gap as provider_adjustments, for the values
    _score() calls float() on: an explicit `capabilities: {x: null}` used to
    load successfully and crash later in _score with an uncaught TypeError
    instead of this clean ValueError."""
    profile = tmp_path / "nullcap.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery:\n"
        "        capabilities:\n"
        "          academic_search: null\n"
    )
    with pytest.raises(ValueError, match="must be a number"):
        drp.load_config(profile)


def test_stage_weight_scalar_null_is_rejected(tmp_path):
    """Same gap as above, for the stage-level synthesis_weight/speed_weight/
    cost_weight scalars."""
    profile = tmp_path / "nullweight.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery:\n"
        "        synthesis_weight: null\n"
    )
    with pytest.raises(ValueError, match="synthesis_weight must be a number"):
        drp.load_config(profile)


def test_stage_capability_bool_weight_is_rejected(tmp_path):
    """bool is a subclass of int, so isinstance(cap_weight, (int, float))
    alone would silently accept a YAML boolean (e.g. an unquoted `yes`) as a
    1.0/0.0 weight. The explicit `or isinstance(cap_weight, bool)` exclusion
    guards against that; this pins it down so the exclusion clause can't be
    silently dropped or inverted without a test failing."""
    profile = tmp_path / "boolcap.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery:\n"
        "        capabilities:\n"
        "          academic_search: true\n"
    )
    with pytest.raises(ValueError, match="must be a number"):
        drp.load_config(profile)


def test_stage_weight_scalar_bool_is_rejected(tmp_path):
    """Same bool-vs-int gap as the capability weight above, for the
    stage-level weight scalars."""
    profile = tmp_path / "boolweight.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery:\n"
        "        speed_weight: true\n"
    )
    with pytest.raises(ValueError, match="speed_weight must be a number"):
        drp.load_config(profile)


def test_provider_adjustments_bool_value_is_rejected(tmp_path):
    """Same bool-vs-int gap, for provider_adjustments values."""
    profile = tmp_path / "booladj.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      asta: true\n"
    )
    with pytest.raises(ValueError, match="must be a number"):
        drp.load_config(profile)


def test_recommendable_no_paid_actually_excludes_a_high_cost_row():
    """test_no_paid_keeps_the_medium_cost_provider above can pass even with
    no_paid filtering fully removed, if the ambient environment never makes a
    genuinely paid provider available. This exercises recommendable()
    directly against a hand-built row set that guarantees a high-cost
    candidate is in contention, so the filter has something real to
    exclude. Also guards PAID_COSTS itself: mutation-verified that without a
    medium-cost row in contention, nothing catches PAID_COSTS silently
    growing to include "medium"."""
    rows = [
        {"provider": "cheap", "status": "available", "cost": "low"},
        {"provider": "midpriced", "status": "available", "cost": "medium"},
        {"provider": "pricey", "status": "available", "cost": "very_high"},
    ]
    with_paid = drp.recommendable(rows, no_paid=False)
    without_paid = drp.recommendable(rows, no_paid=True)
    assert {r["provider"] for r in with_paid} == {"cheap", "midpriced", "pricey"}
    assert {r["provider"] for r in without_paid} == {"cheap", "midpriced"}


def test_an_empty_allowlist_string_is_rejected():
    """--allow "" (an explicitly empty string, distinct from omitting the flag
    entirely) used to be indistinguishable from "not passed" because Python
    treats "" as falsy — `if args.allow` silently fell through to allow=None,
    bypassing the "did not contain any provider names" check below it and
    recommending with no filtering at all."""
    with pytest.raises(ValueError, match="did not contain any provider names"):
        drp.main(["--config", str(CONFIG_PATH), "--allow", ""])


def test_policy_filtered_empty_recommendation_names_the_actual_cause(monkeypatch):
    """The fallback "no real provider is currently available; configure a
    listed credential or CLI" message predates --allow/--no-paid and is wrong
    when one of those, not missing credentials, emptied the recommendation:
    real, working providers exist but were excluded by policy, not absence."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    # An ambient OPENAI_API_KEY would make the --allow'd openai itself
    # "available", taking the pre-existing recommended-provider branch instead
    # of the one this test exercises — this test asserts an exact message, so
    # unlike its permissive siblings it cannot tolerate that.
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    out = _run_text(["--allow", "openai"])
    assert "no provider passes the current --allow/--no-paid filters" in out
    assert "configure a listed credential or CLI" not in out

def test_all_negative_scores_keep_their_relative_order():
    """Fit may floor at zero, but routing must still prefer the least-bad score."""
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))
    stage = config["focuses"][focus_name]["stages"][stage_name]
    stage["capabilities"] = {}
    stage["synthesis_weight"] = 0
    stage["speed_weight"] = 0
    stage["cost_weight"] = 0

    # Deliberately make reverse-alphabetical order the raw-score order.  The
    # old fit-only sort returned alphabetical order once every fit floored to 0.
    expected = sorted(drp.PROVIDERS, reverse=True)
    config["focuses"][focus_name]["provider_adjustments"] = {
        provider: -(index + 1) for index, provider in enumerate(expected)
    }

    rows = drp.rank_stage(config, focus_name, stage_name)
    assert all(row["fit"] == 0 for row in rows)
    assert [row["provider"] for row in rows] == expected
