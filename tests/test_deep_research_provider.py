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
    status, reason = drp.provider_status(
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
