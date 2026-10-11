"""Independent Allisonella source projection, quantity coverage and provenance audit."""

import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
SHA = "dae45cfd1b14facc31aa8691044e6718031b2cd9f8f258b4e5ae141553bfc61f"
ACTION = "RESTORED_ALLISONELLA_ACID_IDENTITIES_AND_STOCK_SCOPES_WITH_EVIDENCE"


def get(node, path):
    for part in path:
        node = node[part]
    return node


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for key, value in node.items():
            yield from walk(value, path + (key,))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk(value, path + (i,))


def liters(value):
    return {"value": format((Decimal(str(value)) / 1000).normalize(), "f"), "unit": "L"}


def check(before, after, item):
    raw = (HERE / "context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.safe_load(spec["before_text"])
    assert before["id"] == after["id"] == spec["id"]
    assert item["path"] == spec["path"] and item["action"] == ACTION
    texts, titles = {}, {}
    for source, capture in context["sources"].items():
        body, meta = capture["raw"], capture["metadata"]
        assert hashlib.sha256(body.encode()).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), body, meta)
        texts[source], titles[source] = parsed.content, parsed.title
    old, lb = {}, set()
    for i, node in enumerate(before["ingredients"]):
        if "LB Medium" in node.get("supplier_catalog", {}).get("supplier_name", ""):
            lb.add(("ingredients", i))
        else:
            name = node["preferred_term"].casefold()
            assert name not in old
            old[name] = ("ingredients", i)
    assert len(lb) == 3
    expected = {}

    def add(path, label, q, sp, kind, *, old_name=None, descriptor=False, fresh_identity=False):
        assert path not in expected
        expected[path] = {
            "label": label,
            "quantity": q,
            "source_pointer": sp,
            "kind": kind,
            "old_pointer": None if descriptor else old.get((old_name or label).casefold()),
            "descriptor": descriptor,
            "fresh_identity": fresh_identity,
        }

    if key == "K1006":
        soup = BeautifulSoup(context["sources"][key]["raw"], "html.parser")
        tables = [t for t in soup.find_all("table") if "Gram Amount" in t.get_text()]
        assert len(tables) == 1
        table = [
            [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
            for tr in tables[0].find_all("tr")
        ]
        assert table[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"]
        assert len(table) == 22 and len(after["ingredients"]) == 21 and after["solutions"] == []
        renamed = {
            "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
            "Resazurin": "Sodium resazurin",
            "Trypticase": "Trypticase peptone",
        }
        for i, row in enumerate(table[1:]):
            assert len(row) == 5
            q = None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"}
            add(
                ("ingredients", i),
                row[0],
                q,
                ["recipe_table", i + 1],
                "unquantified" if q is None else "provider_medium_rate",
                old_name=renamed.get(row[0]),
                fresh_identity=row[0] in {"Resazurin", "Cysteine-HCl x H2O"},
            )
        nodes = {n["preferred_term"]: n for n in after["ingredients"]}
        assert nodes["Resazurin"]["concentration"] == {"value": "9.97E-4", "unit": "G_PER_L"}
        for n in (
            "DL-2-Methyl butyric acid",
            "Acetic acid",
            "Propionic acid",
            "Butyric acid",
            "n-Valeric acid",
            "iso-Valeric acid",
            "iso-Butyric acid",
            "CO2",
            "Distilled water",
        ):
            assert "concentration" not in nodes[n]
        assert "Is Aerobic: true" in after["notes"] and "source conflict" in after["notes"]
    else:
        body = json.loads(context["sources"][key]["raw"])
        ss = body["data"]["solutions"]
        assert [s["id"] for s in ss] == [2052, 608]
        assert [len(s["recipe"]) for s in ss] == [14, 7]
        assert len(after["ingredients"]) == 12 and len(after["solutions"]) == 2
        pos = 0
        for ri, row in enumerate(ss[0]["recipe"]):
            sp = ["data", "solutions", 0, "recipe", ri]
            label = row.get("compound", row.get("solution"))
            if ri == 9:
                assert (
                    label == "Sodium resazurin"
                    and row["attribute"] == "0.1% w/v"
                    and row["amount"] == 0.5
                )
                add(
                    ("solutions", 0),
                    "Sodium resazurin (0.1% w/v)",
                    liters(0.5),
                    sp,
                    "stock_dose",
                    descriptor=True,
                )
                assert len(after["solutions"][0]["composition"]) == 1
                add(
                    ("solutions", 0, "composition", 0),
                    label,
                    {"value": "0.1", "unit": "PERCENT_W_V"},
                    sp,
                    "stock_strength",
                )
            elif ri == 11:
                assert (
                    label == "Volatile fatty acid mixture"
                    and row["solution_id"] == 608
                    and row["amount"] == 3.1
                )
                add(("solutions", 1), label, liters(3.1), sp, "stock_dose", descriptor=True)
                assert len(after["solutions"][1]["composition"]) == 7
                for j, acid in enumerate(ss[1]["recipe"]):
                    assert acid["unit"] == "ml"
                    add(
                        ("solutions", 1, "composition", j),
                        acid["compound"],
                        liters(acid["amount"]),
                        ["data", "solutions", 1, "recipe", j],
                        "stock_liquid_input",
                    )
            else:
                q = liters(row["amount"]) if row["unit"] == "ml" else None
                if q is not None:
                    assert label == "Distilled water" and row["amount"] == 1000
                add(("ingredients", pos), label, q, sp, "water_input" if q else "batch_mass")
                if q is None:
                    assert f"{row['amount']} {row['unit']}" in after["ingredients"][pos]["notes"]
                    assert (
                        "not an independently verified final-medium"
                        in after["ingredients"][pos]["notes"]
                    )
                pos += 1
        assert after["preparation_steps"] == before["preparation_steps"]
        assert (
            "1004 ml" in after["notes"]
            and "not evidence of measured final volume" in after["notes"]
        )

    nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "solutions"} and "preferred_term" in n
    }
    assert nodes == set(expected)
    lineage = []
    for path, wanted in expected.items():
        node, old_path = get(after, path), wanted["old_pointer"]
        assert (
            node["preferred_term"] == wanted["label"]
            and node.get("concentration") == wanted["quantity"]
        )
        assert "LB Medium" not in node.get("supplier_catalog", {}).get("supplier_name", "")
        ignored = {"notes", "concentration", "preferred_term", "evidence"}
        if wanted["descriptor"]:
            assert node["name"] == node["preferred_term"] and "evidence" not in node
            ignored |= {"name", "composition"}
        if old_path and not wanted["fresh_identity"]:
            original = get(before, old_path)
            assert {k: v for k, v in node.items() if k not in ignored} == {
                k: v for k, v in original.items() if k not in ignored
            }
            assert node["notes"].startswith(original.get("notes", ""))
        else:
            assert not {k: v for k, v in node.items() if k not in ignored}
        if wanted["fresh_identity"]:
            assert "Withdraw the copied annotations" in node["notes"]
            assert any(
                c["old_pointer"] == ["ingredients"]
                and c["old"] == before["ingredients"]
                and c["kind"] == "copied_identity_archived"
                for c in item["claims"]
            )
        if wanted["kind"] == "stock_liquid_input":
            assert "liquid input volume" in node["notes"] and "not grams" in node["notes"]
        if key == "K1006":
            assert (
                "Gram & Mol amounts are per Liter of medium." in node["evidence"][0]["explanation"]
            )
            assert "SEED aggregate" in node["notes"]
        lineage.append(
            {
                "pointer": list(path),
                "old_pointer": list(old_path) if old_path else None,
                "source": key,
                "source_pointer": wanted["source_pointer"],
                "label": wanted["label"],
                "kind": wanted["kind"],
            }
        )
    assert sorted(lineage, key=str) == sorted(item["lineage"], key=str)

    other = "D1006" if key == "K1006" else "K1006"
    ref = after["parent_media"] if key == "K1006" else after["variant_children"][0]
    assert {k: ref[k] for k in ("path", "id", "name", "relationship")} == {
        "path": specs[other]["path"],
        "id": specs[other]["id"],
        "name": yaml.safe_load(specs[other]["before_text"])["name"],
        "relationship": "DERIVED_FROM",
    }
    assert "does not prove an exact duplicate" in ref["notes"]
    assert "Instructions:" in ref["evidence"][0]["snippet"]
    assert ref["evidence"][0]["reference"] == context["sources"]["K1006"]["metadata"]["url"]
    if key == "K1006":
        assert after["variant_relationship"] == "DERIVED_FROM" and after[
            "variant_modifications"
        ] == [ref["notes"]]
    else:
        assert len(after["variant_children"]) == 1 and "parent_media" not in after

    claims = item["claims"]
    old_quantities = {p + ("concentration",) for p, node in walk(before) if "concentration" in node}
    assert old_quantities == {
        tuple(c["old_pointer"])
        for c in claims
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert {p + ("concentration",) for p in expected} == {
        tuple(c["pointer"]) for c in claims if c["pointer"][-1] == "concentration"
    }
    assert {tuple(c["old_pointer"][:-1]) for c in claims if c["kind"] == "false_lb_removed"} == lb
    claimed = set()
    for c in claims:
        p, old_path, source = c["pointer"], c["old_pointer"], c["source"]
        assert c["new"] == get(after, p[:-1]).get(p[-1])
        assert c["old"] == (get(before, old_path[:-1]).get(old_path[-1]) if old_path else None)
        assert c["snippet"] and c["snippet"] in texts[source]
        assert c["reference"] == context["sources"][source]["metadata"]["url"]
        assert c["evidence_pointer"] is not None
        entries = [
            e
            for e in get(after, c["evidence_pointer"])["evidence"]
            if e["reference"] == c["reference"]
        ]
        assert len(entries) == 1 and c["explanation"] in entries[0]["explanation"]
        assert (
            c["snippet"] == entries[0]["snippet"]
            or "Additional exact excerpt: " + c["snippet"] in entries[0]["explanation"]
        )
        claimed.add((tuple(c["evidence_pointer"]), c["reference"]))
    actual = set()
    for p, node in walk(after):
        if "evidence" not in node:
            continue
        assert len(node["evidence"]) == len({e["reference"] for e in node["evidence"]})
        for e in node["evidence"]:
            source = next(
                k for k, s in context["sources"].items() if s["metadata"]["url"] == e["reference"]
            )
            assert e["supports"] == "SUPPORT" and e["snippet"] and e["snippet"] in texts[source]
            assert e["explanation"]
            actual.add((p, e["reference"]))
    assert actual == claimed
    refs = after["references"]
    assert len(refs) == len({r["reference"] for r in refs})
    assert {r["reference"] for r in refs} == {c["reference"] for c in claims}
    for ref in refs:
        source = next(
            k for k, s in context["sources"].items() if s["metadata"]["url"] == ref["reference"]
        )
        assert ref["title"] == titles[source] and "authors" not in ref and "year" not in ref
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                context["sources"][source]["metadata"]["sha256"],
            )
        )
    changed = {
        "ingredients",
        "solutions",
        "notes",
        "evidence",
        "references",
        "curation_history",
        "parent_media",
        "variant_children",
        "variant_relationship",
        "variant_modifications",
    }
    assert {k: v for k, v in after.items() if k not in changed} == {
        k: v for k, v in before.items() if k not in changed
    }
    assert "Superseded historical provenance (not a current formulation claim)" in after["notes"]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in claims
    ]
    return {
        "source_nodes": len(expected),
        "old_quantity_slots": len(old_quantities),
        "claims": len(claims),
        "new_evidence": len(actual),
        "new_references": len(refs),
        "new_curation_history": 1,
    }


if __name__ == "__main__":
    plan = json.loads((HERE / "plan.json").read_text())
    print(
        json.dumps(
            {
                r["key"]: check(
                    yaml.safe_load(r["before_text"]), yaml.safe_load(r["after_text"]), r
                )
                for r in plan["records"]
            },
            indent=2,
        )
    )
