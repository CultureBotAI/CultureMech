"""Fleet contract for shared provider-triage behavior.

This suite performs only local scoring and status stubbing. It never invokes a
research provider and cannot spend provider credits. Domain profiles and richer
Mech-specific status models remain intentionally local.
"""

from __future__ import annotations

import copy
import importlib
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
drp = importlib.import_module("deep_research_provider")
CONFIG_PATH = REPO_ROOT / "conf" / "deep_research_provider.yaml"


def _all_available(provider: str, environ=None) -> tuple[str, str]:
    del provider, environ
    return "available", "contract fixture; no provider call"


def _first_stage(config):
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))
    return focus_name, stage_name


def test_policy_flags_are_a_shared_cli_contract():
    args = drp.parse_args(["--config", str(CONFIG_PATH), "--allow", "asta", "--no-paid"])
    assert args.allow == "asta"
    assert args.no_paid is True


def test_allowlist_and_no_paid_constrain_every_recommendation(monkeypatch):
    monkeypatch.setattr(drp, "provider_status", _all_available)
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]

    allowlisted = drp.build_report(config, focus_name, allow=frozenset({"asta"}), no_paid=False)
    for stage in allowlisted["stages"]:
        assert stage["recommended_available"]["provider"] == "asta"
        assert stage["fallback_available"] is None

    no_paid = drp.build_report(config, focus_name, no_paid=True)
    for stage in no_paid["stages"]:
        for key in ("recommended_available", "fallback_available"):
            row = stage[key]
            if row:
                assert row["cost"] not in drp.PAID_COSTS


def test_all_negative_scores_keep_their_relative_order(monkeypatch):
    monkeypatch.setattr(drp, "provider_status", _all_available)
    config = copy.deepcopy(drp.load_config(CONFIG_PATH))
    focus_name, stage_name = _first_stage(config)
    stage = config["focuses"][focus_name]["stages"][stage_name]
    stage["capabilities"] = {}
    stage["synthesis_weight"] = 0
    stage["speed_weight"] = 0
    stage["cost_weight"] = 0

    expected = sorted(drp.PROVIDERS, reverse=True)
    config["focuses"][focus_name]["provider_adjustments"] = {
        provider: -(index + 1) for index, provider in enumerate(expected)
    }
    rows = drp.rank_stage(config, focus_name, stage_name)

    assert {row["fit"] for row in rows} == {0}
    assert [row["provider"] for row in rows] == expected


def test_provider_filtered_json_is_internally_consistent(monkeypatch, capsys):
    monkeypatch.setattr(drp, "provider_status", _all_available)
    assert (
        drp.main(
            [
                "--config",
                str(CONFIG_PATH),
                "--provider",
                "asta",
                "--json",
            ]
        )
        == 0
    )
    report = json.loads(capsys.readouterr().out)
    for stage in report["stages"]:
        ranked = {row["provider"] for row in stage["ranking"]}
        for key in ("recommended_available", "fallback_available"):
            row = stage[key]
            if row:
                assert row["provider"] in ranked
        if "selected" in stage:
            assert stage["selected"]["provider"] == "asta"
            assert "asta" in ranked
        else:
            assert ranked == {"asta"}


def test_unknown_capability_is_rejected_before_scoring(tmp_path):
    config = copy.deepcopy(drp.load_config(CONFIG_PATH))
    focus_name, stage_name = _first_stage(config)
    config["focuses"][focus_name]["stages"][stage_name]["capabilities"]["not_a_real_capability"] = 1
    path = tmp_path / "bad-provider-profile.yaml"
    path.write_text(yaml.safe_dump(config))

    with pytest.raises(ValueError, match="unknown capability"):
        drp.load_config(path)
