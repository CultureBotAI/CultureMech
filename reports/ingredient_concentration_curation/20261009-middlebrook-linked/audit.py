"""Independent source projection and evidence/accounting audit for the linked cohort."""

import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
SHA = "de800cece2575a52bf0a6016c0e356d44d5459b653c3063e4945994dc63a98e6"
ACTION = "RESTORED_LINKED_MIDDLEBROOK_FORMULATIONS_AND_VARIANT_SCOPES_WITH_EVIDENCE"


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


def name(value):
    return "sodium citrate" if value == "Na-citrate" else value.lower()


def number(value):
    return format(Decimal(str(value)).normalize(), "f")


def check(before, after, item):
    raw = (HERE / "context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert before["id"] == after["id"] == spec["id"]
    assert item["path"] == spec["path"] and item["action"] == ACTION
    texts, titles, data = {}, {}, {}
    for source, capture in context["sources"].items():
        body, meta = capture["raw"], capture["metadata"]
        assert (
            hashlib.sha256(body.encode(meta.get("encoding", "utf-8"))).hexdigest() == meta["sha256"]
        )
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), body, meta)
        texts[source], titles[source] = parsed.content, parsed.title
        if source.startswith("K"):
            soup = BeautifulSoup(body, "html.parser")
            tables = [t for t in soup.find_all("table") if "Gram Amount" in t.get_text()]
            assert len(tables) == 1
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            assert rows[0] == [
                "Name",
                "Semi unique name",
                "Unique Name",
                "Gram Amount",
                "Mol Amount",
            ]
            data[source] = rows[1:]
        elif source.startswith("D") and not source.startswith("DSMZ"):
            data[source] = json.loads(body)

    old, lb = {}, []
    for i, node in enumerate(before["ingredients"]):
        p = ("ingredients", i)
        if "LB Medium" in node.get("supplier_catalog", {}).get("supplier_name", ""):
            lb.append(p)
        else:
            assert name(node["preferred_term"]) not in old
            old[name(node["preferred_term"])] = p
    assert len(lb) == 3
    expected, alternatives = {}, []

    def add(p, label, quantity, sp, kind):
        assert p not in expected
        expected[p] = {
            "label": label,
            "quantity": quantity,
            "source_pointer": sp,
            "kind": kind,
            "old_pointer": old.get(name(label)),
        }

    if key.startswith("K"):
        rows = data[key]
        assert len(after["ingredients"]) == len(rows) and after["solutions"] == []
        assert "PH Info: null" in texts[key]
        for i, row in enumerate(rows):
            assert len(row) == 5
            quantity = None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"}
            add(
                ("ingredients", i),
                row[0],
                quantity,
                ["recipe_table", i + 1],
                "unquantified" if quantity is None else "provider_medium_rate",
            )
        if key == "K645a":
            nodes = {n["preferred_term"]: n for n in after["ingredients"]}
            assert "Glycerol" not in nodes
            assert nodes["hemin"]["concentration"] == {"value": "0.04", "unit": "G_PER_L"}
            assert "concentration" not in nodes["NAOH"]
            assert all(
                "60 micromoles" in nodes[n]["notes"]
                and "without a volume denominator" in nodes[n]["notes"]
                and "1N NAOH" in nodes[n]["notes"]
                for n in ("hemin", "NAOH")
            )
            assert "not evidence" in after["notes"]
    else:
        ss = data[key]["data"]["solutions"]
        main_offset = int(key == "D645")
        assert len(after["ingredients"]) == 2 + main_offset
        assert len(after["solutions"]) == (1 if key == "D645" else 2)
        if key == "D645":
            add(
                ("ingredients", 0),
                ss[0]["recipe"][0]["compound"],
                None,
                ["data", "solutions", 0, "recipe", 0],
                "commercial_batch_mass",
            )
            variant = after["variants"][0]
            assert (
                len(after["variants"]) == 1
                and variant["relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
            )
            assert (
                "alternative preparation" in variant["description"]
                and "not simultaneous" in variant["description"]
            )
            assert len(variant["modifications"]) == len(ss[1]["recipe"]) + 1
            for i, row in enumerate(ss[1]["recipe"]):
                assert (
                    variant["modifications"][i]
                    == f"Alternative preparation input: {row['compound']} {row['amount']} {row['unit']}; not an additional input to the commercial preparation. No final-medium concentration is inferred."
                )
                alternatives.append(
                    {
                        "pointer": ["variants", 0],
                        "old_pointer": (
                            list(old[name(row["compound"])])
                            if name(row["compound"]) in old
                            else None
                        ),
                        "source": key,
                        "source_pointer": ["data", "solutions", 1, "recipe", i],
                        "kind": "alternative_input",
                        "label": row["compound"],
                    }
                )
            assert all(
                s in variant["modifications"][-1]
                for s in ("1000 ml", "900 ml", "Do not sum", "6.6 +/- 0.2", "25 C")
            )
            assert (
                "term" not in after["ingredients"][0]
                and "mediaingredientmech_chebi_term" not in after["ingredients"][0]
            )
        else:
            add(
                ("solutions", 0),
                ss[0]["recipe"][0]["solution"],
                None,
                ["data", "solutions", 0, "recipe", 0],
                "commercial_base_detail",
            )
            assert len(after["solutions"][0]["composition"]) == len(ss[1]["recipe"])
            assert (
                "21 g" in after["solutions"][0]["notes"]
                and "not another" in after["solutions"][0]["notes"]
            )
            for i, row in enumerate(ss[1]["recipe"]):
                q = (
                    {"value": number(Decimal(str(row["amount"])) / 1000), "unit": "L"}
                    if row["unit"] == "ml"
                    else None
                )
                add(
                    ("solutions", 0, "composition", i),
                    row["compound"],
                    q,
                    ["data", "solutions", 1, "recipe", i],
                    "base_detail",
                )
            assert after["ph_range"] == {"min": 6.4, "max": 6.8}
        for i, ri in enumerate((1, 2)):
            row = ss[0]["recipe"][ri]
            add(
                ("ingredients", main_offset + i),
                row["compound"],
                {"value": number(Decimal(str(row["amount"])) / 1000), "unit": "L"},
                ["data", "solutions", 0, "recipe", ri],
                "batch_volume",
            )
        stock = ("solutions", len(after["solutions"]) - 1)
        add(
            stock,
            ss[2]["name"],
            {"value": "0.1", "unit": "L"},
            ["data", "solutions", 0, "steps", 0, "step"],
            "stock_dose",
        )
        assert "Add 100 ml" in ss[0]["steps"][0]["step"]
        assert len(get(after, stock)["composition"]) == 6
        for i, row in enumerate(ss[2]["recipe"]):
            q = (
                {"value": number(Decimal(str(row["amount"])) / 1000), "unit": "L"}
                if row["unit"] == "ml"
                else {"value": number(row["g_l"]), "unit": "G_PER_L"}
            )
            add(
                stock + ("composition", i),
                row["compound"],
                q,
                ["data", "solutions", 2, "recipe", i],
                "stock_rate",
            )
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "HEAT", "description": ss[0]["steps"][0]["step"]}
        ]

    nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "solutions"} and "preferred_term" in n
    }
    assert nodes == set(expected)
    ledger = []
    for p, e in expected.items():
        node, old_path = get(after, p), e["old_pointer"]
        assert name(node["preferred_term"]) == name(e["label"])
        assert node.get("concentration") == e["quantity"]
        assert "LB Medium" not in node.get("supplier_catalog", {}).get("supplier_name", "")
        ledger.append(
            {
                "pointer": list(p),
                "old_pointer": list(old_path) if old_path else None,
                "source": key,
                "source_pointer": e["source_pointer"],
                "kind": e["kind"],
                "label": e["label"],
            }
        )
        ignored = {"notes", "concentration", "name", "composition", "evidence"}
        if key == "D645" and p == ("ingredients", 0):
            ignored |= {"term", "mediaingredientmech_chebi_term"}
        if old_path:
            original = get(before, old_path)
            assert {k: v for k, v in node.items() if k not in ignored} == {
                k: v for k, v in original.items() if k not in ignored
            }
            assert node["notes"].startswith(original.get("notes", ""))
        else:
            assert not any(
                k in node for k in ("term", "supplier_catalog", "mediaingredientmech_chebi_term")
            )
        if p[0] == "solutions" and len(p) == 2:
            assert node["name"] == node["preferred_term"] and "evidence" not in node
        if key.startswith("K"):
            assert "Mol Amount" in node["notes"]
            assert (
                "Gram & Mol amounts are per Liter of medium." in node["evidence"][0]["explanation"]
            )
        elif e["kind"] == "base_detail":
            assert "not an additional simultaneous" in node["notes"]
        elif e["kind"] == "stock_rate" and e["quantity"]["unit"] == "G_PER_L":
            assert "not a finished-medium concentration" in node["notes"]
        if (
            e["quantity"] is None
            and not key.startswith("K")
            and e["kind"] != "commercial_base_detail"
        ):
            row = get(data[key], e["source_pointer"])
            assert f"{row['amount']} {row['unit']}" in node["notes"]
    ledger.extend(alternatives)
    assert sorted(ledger, key=lambda row: str(row)) == sorted(
        item["lineage"], key=lambda row: str(row)
    )

    relations = {
        "K645": ("D645", "DERIVED_FROM"),
        "K645a": ("D645", "UNCERTAIN"),
        "K911": ("D911", "DERIVED_FROM"),
        "K911_44536": ("K911", "STRAIN_SPECIFIC_VARIANT"),
    }
    relations.update(
        {
            "K645_" + n: ("K645", "STRAIN_SPECIFIC_VARIANT")
            for n in ("44338", "44339", "44482", "44483", "44680")
        }
    )

    def link_check(link, target, relation, child):
        assert {k: link[k] for k in ("path", "id", "name", "relationship")} == {
            "path": specs[target]["path"],
            "id": specs[target]["id"],
            "name": yaml.load(specs[target]["before_text"], Loader=yaml.CSafeLoader)["name"],
            "relationship": relation,
        }
        source = "DSMZ645a" if child == "K645a" else child
        assert link["evidence"][0]["reference"] == context["sources"][source]["metadata"]["url"]
        if child == "K645a":
            assert (
                "Middlebrook 7H10" in link["evidence"][0]["snippet"]
                and "Candidate" in link["notes"]
            )
        elif "_" in child:
            assert "MODIFIED FOR DSM " + child.split("_")[1] in link["evidence"][0]["snippet"]
            assert "does not identify" in link["notes"]
        else:
            assert "Instructions:" in link["evidence"][0]["snippet"]

    if key in relations:
        parent, relation = relations[key]
        link_check(after["parent_media"], parent, relation, key)
        assert after["variant_relationship"] == relation and after["variant_modifications"] == [
            after["parent_media"]["notes"]
        ]
    else:
        assert not any(
            k in after for k in ("parent_media", "variant_relationship", "variant_modifications")
        )
    children = [child for child, (parent, _) in relations.items() if parent == key]
    assert len(after.get("variant_children", [])) == len(children)
    for link, child in zip(after.get("variant_children", []), children, strict=True):
        link_check(link, child, relations[child][1], child)

    claims = item["claims"]
    quantities = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert quantities == {
        tuple(c["old_pointer"])
        for c in claims
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert {p + ("concentration",) for p in expected} == {
        tuple(c["pointer"]) for c in claims if c["pointer"][-1] == "concentration"
    }
    assert {tuple(c["old_pointer"][:-1]) for c in claims if c["kind"] == "false_lb_removed"} == set(
        lb
    )
    if key == "D645":
        assert any(
            c["old_pointer"] == ["ingredients"] and c["old"] == before["ingredients"]
            for c in claims
        )
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
    claimed = {(tuple(c["evidence_pointer"]), c["reference"]) for c in claims}
    actual = set()
    for p, node in walk(after):
        if "evidence" in node:
            assert len(node["evidence"]) == len({e["reference"] for e in node["evidence"]})
            for e in node["evidence"]:
                source = next(
                    k
                    for k, s in context["sources"].items()
                    if s["metadata"]["url"] == e["reference"]
                )
                assert e["supports"] == "SUPPORT" and e["snippet"] and e["snippet"] in texts[source]
                assert e["explanation"]
                actual.add((p, e["reference"]))
    assert actual == claimed
    assert len(after["references"]) == len({r["reference"] for r in after["references"]})
    assert {r["reference"] for r in after["references"]} == {c["reference"] for c in claims}
    for ref in after["references"]:
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
    allowed = {
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
    if key == "D645":
        allowed.add("variants")
    if key.startswith("D"):
        allowed.add("preparation_steps")
    assert {k: v for k, v in after.items() if k not in allowed} == {
        k: v for k, v in before.items() if k not in allowed
    }
    assert "Superseded historical provenance (not a current formulation claim)" in after["notes"]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in claims
    ]
    return {
        "source_nodes": len(ledger),
        "old_quantity_slots": len(quantities),
        "claims": len(claims),
        "new_evidence": len(actual),
        "new_references": len(after["references"]),
        "new_curation_history": 1,
    }


if __name__ == "__main__":
    plan = json.loads((HERE / "plan.json").read_text())
    print(
        json.dumps(
            {
                r["key"]: check(
                    yaml.load(r["before_text"], Loader=yaml.CSafeLoader),
                    yaml.load(r["after_text"], Loader=yaml.CSafeLoader),
                    r,
                )
                for r in plan["records"]
            },
            indent=2,
        )
    )
