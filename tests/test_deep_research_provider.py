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


# --- policy and machine-readable consistency (#290) ------------------------


def test_a_measured_dead_provider_is_not_recommended():
    """The tool used to contradict the justfile beside it.

    #284 measured falcon returning HTTP 402 and cyberian HTTP 500, and recorded
    both in the provider table. The triage tool still routed every stage to
    falcon, because "available" only ever meant "an env var is set".
    """
    status, reason = drp.provider_status("falcon", {"EDISON_API_KEY": "secret"})
    assert status == "blocked"
    assert "402" in reason
    assert "secret" not in reason

    config = drp.load_config(CONFIG_PATH)
    report = drp.build_report(config, config["default_focus"])
    for stage in report["stages"]:
        recommended = stage["recommended_available"]
        assert recommended is None or recommended["provider"] not in drp.KNOWN_BLOCKED


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
