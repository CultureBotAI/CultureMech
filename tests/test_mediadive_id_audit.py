"""Pin the MediaDive id audit's classification logic (#244).

The audit's conclusion — that the corpus's own `mediadive.medium:` ids are sound and
the KOMODO->DSMZ mapping is what misleads — rests entirely on how a record name is
compared to a catalogue name. These tests fix that comparison so the conclusion
cannot quietly change.

The corpus-wide numbers are NOT asserted here: the audit calls the live MediaDive
catalogue, and a network-dependent assertion would make the suite fail on MediaDive's
availability rather than on this repo's correctness.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def ami():
    return _load("audit_mediadive_ids")


def test_names_match_accepts_the_same_medium_written_differently(ami):
    assert ami.names_match(["Bacto Marine Broth"], "BACTO MARINE BROTH (DIFCO 2216)")
    assert ami.names_match(["bacto_marine_broth_difco_2216"], "BACTO MARINE BROTH (DIFCO 2216)")
    assert ami.names_match(["NUTRIENT AGAR"], "Nutrient agar")


def test_names_match_rejects_a_different_medium(ami):
    """The case the whole audit turns on: KOMODO 294 resolves to a MediaDive medium
    that is a different organism's medium entirely."""
    assert not ami.names_match(["PELOBACTER ACIDIGALLICI MEDIUM"], "SYNTROPHUS HQGo1 MEDIUM")
    assert not ami.names_match(["Artificial SEAWATER MEDIUM"], "DESULFOPILA CORRODENS MEDIUM")


def test_names_match_needs_a_catalogue_name(ami):
    assert not ami.names_match(["anything"], "")


def test_known_upstream_renames_are_documented_not_bare(ami):
    """Each entry claims the corpus id is right despite a name change, so each must
    carry the evidence that was checked by hand — otherwise it is an unexplained
    suppression of a real finding."""
    assert ami.KNOWN_UPSTREAM_RENAMES, "the rename allowlist vanished"
    for mid, why in ami.KNOWN_UPSTREAM_RENAMES.items():
        assert mid.isdigit(), f"{mid!r} is not a MediaDive medium number"
        assert "pH" in why or "same medium" in why, (
            f"rename {mid} is allowlisted without stating what was verified: {why!r}")


def test_audit_classifies_the_four_cases(ami):
    """End to end over a fake catalogue, so no network is touched."""
    catalogue = {"1": "NUTRIENT AGAR", "294": "SYNTROPHUS HQGo1 MEDIUM"}
    names = ["NUTRIENT AGAR"]
    assert ami.names_match(names, catalogue["1"])
    assert not ami.names_match(["PELOBACTER ACIDIGALLICI MEDIUM"], catalogue["294"])
    # an id absent from the catalogue is NOT_IN_MEDIADIVE, never silently AGREE
    assert "9999" not in catalogue
