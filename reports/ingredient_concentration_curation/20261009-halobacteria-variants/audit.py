"""Independent source projection for variant amounts and preparation boundaries."""

import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
PARENTS = {"J168", "M159", "M160"}
PREPARED = {"J1132", "M1212"}
MAKEUP = "Add components to distilled water and bring volume to 1.0 L."
AGAR = "For preparation of solid medium, add 20.0 g/L agar."
LINKS = {
    "J572": ("J168", "DERIVED_FROM"),
    "M576": ("M159", "DERIVED_FROM"),
    "J1008": ("J168", "DERIVED_FROM"),
    "M1065": ("M159", "DERIVED_FROM"),
    "J914": ("J168", "SALINITY_VARIANT"),
    "M959": ("M159", "SALINITY_VARIANT"),
    "M960": ("M160", "SALINITY_VARIANT"),
    "J377": ("J168", "SALINITY_VARIANT"),
    "J1132": ("J168", "PH_VARIANT"),
    "M1212": ("M159", "PH_VARIANT"),
}


def get(node, path):
    for part in path:
        node = node[part]
    return node


def value(node, path):
    parent = get(node, path[:-1])
    return parent.get(path[-1]) if isinstance(parent, dict) else parent[path[-1]]


def walk(node, path=()):
    if isinstance(node, dict):
        if "preferred_term" in node:
            yield path, node
        for field in ("ingredients", "composition", "solutions"):
            for i, child in enumerate(node.get(field, [])):
                yield from walk(child, path + (field, i))


def label(name):
    name = {
        "Casamino acids": "Casamino acids (BD-Difco)",
        "Yeast extract": "Yeast extract (BD-Difco)",
        "Na glutamate": "Sodium glutamate",
        "Distilled water": "distilled water",
    }.get(name, name)
    return name.replace(" x ", "\u00b7").replace("\u30fb", "\u00b7").replace(" H2O", "H2O")


def changes(old, new, path=()):
    if isinstance(old, dict) and isinstance(new, dict):
        for key in old.keys() | new.keys():
            yield from changes(old.get(key), new.get(key), path + (key,))
    elif isinstance(old, list) and isinstance(new, list):
        for i in range(max(len(old), len(new))):
            yield from changes(
                old[i] if i < len(old) else None, new[i] if i < len(new) else None, path + (i,)
            )
    elif old != new:
        if old is None and isinstance(new, dict) and new:
            for k, v in new.items():
                yield from changes(None, v, path + (k,))
        elif old is None and isinstance(new, list) and new:
            for i, v in enumerate(new):
                yield from changes(None, v, path + (i,))
        else:
            yield path


def evidence(node):
    result = []
    if isinstance(node, dict):
        result.extend(node.get("evidence", []))
        for key, child in node.items():
            if key not in {"evidence", "curation_history"}:
                result.extend(evidence(child))
    elif isinstance(node, list):
        for child in node:
            result.extend(evidence(child))
    return result


def check(row, *, applied=False, current_text=None):
    raw = (HERE / "context.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "5c32dabb73da826f5ad4a3fc1750bb701e077f4541fcb708522970538979cb33"
    )
    context = json.loads(raw)
    specs = {r["key"]: r for r in context["records"]}
    key, spec = row["key"], specs[row["key"]]
    assert all(
        row[f] == spec[f]
        for f in ("path", "id", "before_text", "before_sha256", "scope", "target_class")
    )
    assert hashlib.sha256(row["before_text"].encode()).hexdigest() == row["before_sha256"]
    assert hashlib.sha256(row["after_text"].encode()).hexdigest() == row["after_sha256"]
    current = Path(row["path"]).read_text() if current_text is None else current_text
    assert current == row["after_text" if applied else "before_text"]
    before, after = yaml.safe_load(row["before_text"]), yaml.safe_load(row["after_text"])
    assert before["id"] == after["id"] == row["id"]
    texts, tables = {}, {}
    for name, src in context["sources"].items():
        meta, body = src["metadata"], src["raw"]
        assert hashlib.sha256(body.encode()).hexdigest() == meta["sha256"]
        assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
        text = (
            body
            if name == "E1132"
            else parse_recipe(recipe_source(meta["url"]), body, meta).content
        )
        assert text == src["parsed_text"]
        texts[meta["url"]] = text if name.startswith("J") else body
        if name in {"J168", "J377"}:
            cells = [
                [" ".join(td.get_text().split()) for td in tr.find_all("td")]
                for tr in BeautifulSoup(body, "html.parser").find_all("tr")
            ]
            assert cells == src["table_rows"] and len(cells) == 9
            tables[name] = {
                label(n): (Decimal(a), "MG_PER_L" if u == "mg" else "G_PER_L") for n, a, u in cells
            }
    base = "J377" if key in {"J377", "M371", "M372"} else "J168"
    expected = dict(tables[base])
    expected["distilled water"] = None
    if key in {"J572", "M576"}:
        assert "2.0 g/L MgSO4\u00b77H2O (final)" in context["sources"]["J572"]["parsed_text"]
        expected["MgSO4\u00b77H2O"] = (Decimal(2), "G_PER_L")
    elif key in {"J1008", "M1065"}:
        assert (
            "270.0 g/L NaCl (final) and 15.0 g/L MgSO4\u00b77H2O"
            in context["sources"]["J1008"]["parsed_text"]
        )
        expected.update(
            {"MgSO4\u00b77H2O": (Decimal(15), "G_PER_L"), "NaCl": (Decimal(270), "G_PER_L")}
        )
    elif key in {"J914", "M959", "M960"}:
        assert "150.0 g/L (final) NaCl" in context["sources"]["J914"]["parsed_text"]
        expected["NaCl"] = (Decimal(150), "G_PER_L")
    if key in {"M372", "M960", "M160"}:
        assert AGAR in context["sources"][base]["parsed_text"]
        expected["agar"] = (Decimal(20), "G_PER_L")
    if key == "M1212":
        for salt in ("FeCl2\u00b74H2O", "MnCl2\u00b74H2O"):
            expected[salt] = (expected[salt][0] / 1000, "G_PER_L")
    prefix = (
        ("solutions", 0, "composition")
        if key in PREPARED
        else ("composition",) if key == "S3823" else ("ingredients",)
    )
    components = get(after, prefix)
    assert len(components) == len(expected)
    assert {label(n["preferred_term"]) for n in components} == set(expected)
    for node in components:
        rate = expected[label(node["preferred_term"])]
        if rate is None:
            assert "concentration" not in node
            assert "unspecified" in node["notes"]
        else:
            assert set(node["concentration"]) == {"value", "unit"}
            assert (Decimal(node["concentration"]["value"]), node["concentration"]["unit"]) == rate
        assert node["evidence"] and node["notes"]
    if key in PARENTS:
        assert after["ingredients"] == before["ingredients"]
        assert after["ph_range"] == before["ph_range"]
        prior = Path(spec["prior_concentration_validation"])
        assert (
            hashlib.sha256(prior.read_bytes()).hexdigest()
            == spec["prior_concentration_validation_sha256"]
        )
    else:
        old_field = "composition" if key == "S3823" else "ingredients"
        for old, new in zip(before[old_field], components, strict=False):
            old, new = copy.deepcopy(old), copy.deepcopy(new)
            for field in ("concentration", "notes", "evidence"):
                old.pop(field, None)
                new.pop(field, None)
            assert old == new, "Ingredient identities or roles changed"
        assert all(
            set(node) <= {"preferred_term", "notes", "evidence"}
            for node in components[len(before[old_field]) :]
        )
    if key in PREPARED:
        assert after["ingredients"] == [] and len(after["solutions"]) == 1
        stock = after["solutions"][0]
        assert stock["concentration"] == {"value": "1", "unit": "L"}
        assert "post-titration" in stock["notes"] and "unspecified" in stock["notes"]
        assert stock["preparation_notes"] == MAKEUP + "\nAdjust pH to 7.0-7.2.\n" + AGAR
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 8.0."}
        ]
        assert after["ph_value"] == 8 and "ph_range" not in after
        if key == "J1132":
            assert stock["term"] == {"id": "mediadive.solution:3823", "label": "Main sol. J168"}
            assert "Nothing found" in after["notes"] and "not a recovered" in after["notes"]
        else:
            assert "term" not in stock
            assert after["references"][:2] == before["references"]
    elif key == "S3823":
        assert "ingredients" not in after and "data_quality_flags" not in after
        assert "concentration" not in after and "evidence" not in after
        assert after["preparation_notes"] == before["preparation_notes"]
    elif key not in PARENTS:
        assert after.get("preparation_steps") == before.get("preparation_steps")
        if key in {"J572", "M576", "J1008", "M1065"}:
            assert after["ph_value"] == 7.5 and "ph_range" not in after
        else:
            assert after["ph_range"] == {"min": 7, "max": 7.2} and "ph_value" not in after
        if key in {"J572", "M576"}:
            (titrant,) = after["solutions"]
            assert titrant["name"] == titrant["preferred_term"] == "Na2CO3 solution"
            assert titrant["composition"] == []
            assert titrant.get("concentration") == (
                {"value": "variable", "unit": "VARIABLE"} if key == "M576" else None
            )
            assert "unspecified" in titrant["notes"]
        else:
            assert not after.get("solutions")
        if key in {"J1008", "M1065"}:
            assert "operational ambiguity" in after["notes"] and "35 g/L" in after["notes"]
    assert after.get("physical_state") == before.get("physical_state")
    assert after.get("high_metal") == before.get("high_metal")
    for child, (parent, relation) in LINKS.items():
        if key == child:
            target, link = specs[parent], after["parent_media"]
            assert after["variant_relationship"] == relation
            assert "SOURCE_DUPLICATE" not in after["variant_modifications"]
        elif key == parent:
            target = specs[child]
            (link,) = [r for r in after["variant_children"] if r["id"] == target["id"]]
        else:
            continue
        assert link["id"] == target["id"] and link["path"] == target["path"]
        assert link["relationship"] == relation
        assert link["name"] == yaml.safe_load(target["before_text"])["name"]
    if key in PARENTS:
        affected = {specs[c]["id"] for c, (parent, _) in LINKS.items() if parent == key}
        assert [r for r in after["variant_children"] if r["id"] not in affected] == [
            r for r in before["variant_children"] if r["id"] not in affected
        ]
        assert len(after["variant_children"]) == len(before["variant_children"]) + (key == "J168")
    old_quantities = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    accounted = {
        tuple(c["old_pointer"])
        for c in row["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert accounted == (set() if key in PARENTS else old_quantities)
    if key in PARENTS:
        assert row["lineage"] == []
    else:
        pointers = [tuple(item["pointer"]) for item in row["lineage"]]
        assert len(pointers) == len(set(pointers))
        assert set(pointers) == {p for p, _ in walk(after) if p}
        for item in row["lineage"]:
            node = get(after, item["pointer"])
            assert item["label"] == node["preferred_term"]
            if item["old_pointer"]:
                assert get(before, item["old_pointer"])["preferred_term"] == item["label"]
    for claim in row["claims"]:
        assert claim["old"] == (
            value(before, claim["old_pointer"]) if claim["old_pointer"] else None
        )
        assert claim["new"] == value(after, claim["pointer"])
        assert claim["snippet"] and claim["snippet"] in texts[claim["reference"]]
        (entry,) = [
            e
            for e in get(after, claim["evidence_pointer"])["evidence"]
            if e["reference"] == claim["reference"]
        ]
        assert entry["supports"] == "SUPPORT"
        assert claim["snippet"] in entry["snippet"] + "\n" + entry["explanation"]
        assert claim["explanation"] in entry["explanation"]
    for entry in evidence(after):
        assert entry["supports"] == "SUPPORT" and entry["snippet"] in texts[entry["reference"]]
    for old in evidence(before):
        assert any(
            e["reference"] == old["reference"]
            and e["snippet"] == old["snippet"]
            and e["explanation"].startswith(old["explanation"])
            for e in evidence(after)
        )
    refs = after["references"]
    assert len({r["reference"] for r in refs}) == len(refs)
    assert refs[: len(before.get("references", []))] == before.get("references", [])
    for ref in refs[len(before.get("references", [])) :]:
        assert ref["reference"] in texts and ref["title"]
        assert "source_type=" in ref["notes"] and "discovery_mode=" in ref["notes"]
        assert "authors" not in ref and "year" not in ref
    assert {e["reference"] for e in evidence(after)} <= {r["reference"] for r in refs}
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    assert (
        after["curation_history"][-1]["action"]
        == "CURATED_HALOBACTERIA_VARIANT_CONCENTRATIONS_AND_PREPARATION_STAGES"
    )
    prefixes = [tuple(c["pointer"]) for c in row["claims"]]
    for path in changes(before, after):
        if path[0] in {"references", "curation_history"} or "evidence" in path:
            continue
        assert any(path[: len(p)] == p for p in prefixes), ("Unaccounted edit", path)
    return {
        "old_quantities": len(old_quantities),
        "old_quantities_reviewed": 0 if key in PARENTS else len(old_quantities),
        "nodes": sum(bool(p) for p, _ in walk(after)),
        "claims": len(row["claims"]),
        "new_evidence": len(evidence(after)) - len(evidence(before)),
        "new_references": len(refs) - len(before.get("references", [])),
    }
