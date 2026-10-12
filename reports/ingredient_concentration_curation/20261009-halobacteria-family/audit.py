"""Independently check the Halobacteria proposal against captured source rows."""

import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

from culturemech.validation.recipe_references import parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent


def get(node, pointer):
    for part in pointer:
        node = node[part]
    return node


def walk(node, pointer=()):
    if isinstance(node, dict):
        if "preferred_term" in node:
            yield pointer, node
        for field in ("ingredients", "solutions", "composition"):
            for i, child in enumerate(node.get(field, [])):
                yield from walk(child, pointer + (field, i))


def label(name):
    name = {
        "Casamino acids": "Casamino acids (BD-Difco)",
        "Yeast extract": "Yeast extract (BD-Difco)",
        "Na glutamate": "Sodium glutamate",
    }.get(name, name)
    return name.replace(" x ", "\u00b7").replace("\u30fb", "\u00b7").replace(" H2O", "H2O")


def changes(old, new, path=()):
    if isinstance(old, dict) and isinstance(new, dict):
        for key in old.keys() | new.keys():
            yield from changes(old.get(key), new.get(key), path + (key,))
    elif isinstance(old, list) and isinstance(new, list):
        for i in range(max(len(old), len(new))):
            yield from changes(
                old[i] if i < len(old) else None,
                new[i] if i < len(new) else None,
                path + (i,),
            )
    elif old != new:
        if old is None and isinstance(new, dict) and new:
            for key, value in new.items():
                yield from changes(None, value, path + (key,))
        elif old is None and isinstance(new, list) and new:
            for i, value in enumerate(new):
                yield from changes(None, value, path + (i,))
        else:
            yield path


def check(item, *, applied=False, current_text=None):
    context_path = HERE / "captures-approved.json"
    assert (
        hashlib.sha256(context_path.read_bytes()).hexdigest()
        == "51b2cbe0e68dafaa7d155bd838c04e863169fc1de75e6ec64a856e77d7617bc3"
    )
    context = json.loads(context_path.read_text())
    inspected_path = HERE / "source-inspection.json"
    assert (
        hashlib.sha256(inspected_path.read_bytes()).hexdigest()
        == "ac02f2b62e0309aa079e09d5016f23da70c98f18ea877cf9eb134ff038e65b6d"
    )
    inspected = json.loads(inspected_path.read_text())
    (spec,) = [r for r in context["records"] if r["key"] == item["key"]]
    assert all(
        item[field] == spec[field] for field in ("path", "id", "before_text", "before_sha256")
    )
    assert hashlib.sha256(item["after_text"].encode()).hexdigest() == item["after_sha256"]
    actual = Path(item["path"]).read_text() if current_text is None else current_text
    assert actual == item["after_text" if applied else "before_text"]
    before, after = yaml.load(item["before_text"], Loader=yaml.CSafeLoader), yaml.load(
        item["after_text"], Loader=yaml.CSafeLoader
    )
    key, modified = item["key"], item["key"] in {"J1007", "M1064"}
    texts = {}
    for source, capture in context["sources"].items():
        meta = capture["metadata"]
        assert hashlib.sha256(capture["raw"].encode()).hexdigest() == meta["sha256"]
        assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
        texts[meta["url"]] = (
            parse_recipe(recipe_source(meta["url"]), capture["raw"], meta).content
            if source.startswith("JCM")
            else capture["raw"]
        )
    base = {
        label(name): (Decimal(amount), "MG_PER_L" if unit == "mg" else "G_PER_L")
        for name, amount, unit in inspected["sources"]["JCM168"]["table_rows"]
    }
    expected = dict(base)
    expected["distilled water"] = None
    if modified:
        expected["MgSO4\u00b77H2O"] = (Decimal(1), "G_PER_L")
        expected["sodium pyruvate"] = (Decimal(1), "G_PER_L")
    if key == "M160":
        expected["agar"] = (Decimal(20), "G_PER_L")
    assert {label(n["preferred_term"]) for n in after["ingredients"]} == set(expected)
    assert len(after["ingredients"]) == len(expected)
    for i, node in enumerate(after["ingredients"]):
        name = label(node["preferred_term"])
        rate = expected[name]
        if rate is None:
            assert "concentration" not in node and "make-up" not in str(
                node.get("concentration", {})
            )
            assert "individual input volume and mass are unspecified" in node["notes"]
        else:
            assert set(node["concentration"]) == {"value", "unit"}
            assert (
                Decimal(node["concentration"]["value"]),
                node["concentration"]["unit"],
            ) == rate
        assert node["evidence"] and node["notes"]
        if i < len(before["ingredients"]):
            old = copy.deepcopy(before["ingredients"][i])
            new = copy.deepcopy(node)
            for field in ("concentration", "notes", "evidence"):
                old.pop(field, None)
                new.pop(field, None)
            assert old == new
        else:
            assert set(node) <= {"preferred_term", "concentration", "notes", "evidence"}
        if modified and name.startswith("MgSO4"):
            assert "preparation ambiguity" in node["notes"] and "not claim" in node["notes"]
    assert after.get("high_metal") == before.get("high_metal")
    assert after.get("preparation_steps") == before.get("preparation_steps")
    assert (
        after["physical_state"]
        == before["physical_state"]
        == ("SOLID_AGAR" if key == "M160" else "LIQUID")
    )
    if modified:
        assert after["ph_value"] == 8.0 and "ph_range" not in after
        (stock,) = after["solutions"]
        assert (
            stock["preferred_term"] == stock["name"] == "Na2CO3 solution"
            and stock["composition"] == []
        )
        assert stock.get("concentration") == (
            before["solutions"][0]["concentration"] if key == "M1064" else None
        )
        assert "stock strength" in stock["notes"] and "pH to 8.0" in stock["notes"]
    else:
        assert after["ph_range"] == {"min": 7.0, "max": 7.2} and "ph_value" not in after
        assert not after.get("solutions")
    j168 = next(r for r in context["records"] if r["key"] == "J168")
    j1007 = next(r for r in context["records"] if r["key"] == "J1007")
    if key == "J1007":
        assert after["parent_media"] == {
            "path": j168["path"],
            "relationship": "DERIVED_FROM",
            "id": j168["id"],
            "name": "halobacteria_medium",
        }
        assert after["variant_relationship"] == "DERIVED_FROM"
        assert "preparation ambiguity" in after["variant_modifications"][0]
    if key == "J168":
        for old, new in zip(before["variant_children"], after["variant_children"], strict=True):
            if old["id"] == j1007["id"]:
                assert new["path"] == j1007["path"] and new["relationship"] == "DERIVED_FROM"
            else:
                assert old == new
    old_quantities = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    claim_old = {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert old_quantities == claim_old
    for claim in item["claims"]:
        pointer, old_pointer = claim["pointer"], claim["old_pointer"]
        assert claim["new"] == get(after, pointer[:-1]).get(pointer[-1])
        assert claim["old"] == (
            get(before, old_pointer[:-1]).get(old_pointer[-1]) if old_pointer else None
        )
        assert claim["snippet"] and claim["snippet"] in texts[claim["reference"]]
        evidence = get(after, claim["evidence_pointer"])["evidence"]
        (entry,) = [e for e in evidence if e["reference"] == claim["reference"]]
        assert claim["snippet"] in entry["snippet"] + "\n" + entry["explanation"]
        assert claim["explanation"] in entry["explanation"]
    all_evidence = [e for _, node in walk(after) for e in node.get("evidence", [])] + after.get(
        "evidence", []
    )
    for entry in all_evidence:
        assert entry["supports"] == "SUPPORT" and entry["snippet"] in texts[entry["reference"]]
    refs = after["references"]
    assert len({r["reference"] for r in refs}) == len(refs)
    assert {r["reference"] for r in refs} == {e["reference"] for e in all_evidence}
    assert all(
        "authors" not in r
        and "year" not in r
        and "source_type=" in r["notes"]
        and "discovery_mode=" in r["notes"]
        for r in refs
    )
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    assert after["curation_history"][-1]["action"] == "CURATED_HALOBACTERIA_SOURCE_CONCENTRATIONS"
    prefixes = [tuple(c["pointer"]) for c in item["claims"]]
    for path in changes(before, after):
        if path[0] in {"references", "curation_history"} or "evidence" in path:
            continue
        assert any(path[: len(prefix)] == prefix for prefix in prefixes), (
            "Unaccounted edit",
            path,
        )
    return {
        "old_quantities": len(old_quantities),
        "nodes": sum(1 for _ in walk(after)),
        "claims": len(item["claims"]),
        "evidence": len(all_evidence),
        "references": len(refs),
    }
