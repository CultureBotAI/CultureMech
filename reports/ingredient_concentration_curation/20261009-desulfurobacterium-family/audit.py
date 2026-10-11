"""Independent source-stage projection, evidence and old-slot audit for medium 829.

Does not import or execute the repair builder. Quantities are checked against
the earlier, hash-pinned source decisions and independently reconstructed stages.
"""

import argparse
import hashlib
import json
from decimal import Decimal
from functools import cache
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "ef9c0aa87ab3f6b939c9b088337f801601151ba34e0797406b69bb038a29a0be"
ACTION = "RESTORED_MEDIUM_829_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"


def get(node, path):
    for part in path:
        node = node[part]
    return node


def value(node, path):
    parent = get(node, path[:-1])
    return parent[path[-1]] if isinstance(parent, list) else parent.get(path[-1])


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for key, child in node.items():
            yield from walk(child, path + (key,))
    elif isinstance(node, list):
        for i, child in enumerate(node):
            yield from walk(child, path + (i,))


def liters(amount):
    return {"value": format((Decimal(str(amount)) / 1000).normalize(), "f"), "unit": "L"}


@cache
def snapshot(raw):
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    decisions, texts, titles, data = {}, {}, {}, {}
    for path, digest in context["preparation_receipt_sha256"].items():
        body = (ROOT / path).read_bytes()
        assert hashlib.sha256(body).hexdigest() == digest
        if Path(path).name in {"next-829-source-review.json", "next-829-expanded-review.json"}:
            for row in json.loads(body)["source_decisions"]:
                marker = (row["source"], tuple(row["pointer"]))
                assert marker not in decisions
                decisions[marker] = row
    assert len(decisions) == 435
    for key, capture in context["sources"].items():
        body, meta = capture["raw"], capture["metadata"]
        assert hashlib.sha256(body.encode()).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), body, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("K"):
            tables = [
                t
                for t in BeautifulSoup(body, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
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
            data[key] = rows[1:]
        elif not key.startswith("DSMZ"):
            data[key] = json.loads(body)
    for (key, _), row in decisions.items():
        assert row["snippet"] in texts[key]
        assert row["reference"] == context["sources"][key]["metadata"]["url"]
    return context, decisions, texts, titles, data


def check(before, after, item):
    context, decisions, texts, titles, data = snapshot((HERE / "context.json").read_bytes())
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.safe_load(spec["before_text"])
    assert before["id"] == after["id"] == spec["id"] and item["path"] == spec["path"]
    assert item["action"] == ACTION
    expected, old = {}, []
    for p, n in walk(before):
        if (
            len(p) >= 2
            and p[0] in {"ingredients", "solutions", "composition"}
            and "preferred_term" in n
        ):
            if "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", ""):
                old.append((p, n))
    aliases = {
        "MES": "MES [2-(N-morpholino) ethane sulfonic acid]",
        "D(+)-Biotin": "D-(+)-biotin",
        "Pyridoxine HCl": "Pyridoxine hydrochloride",
        "Na2-dithionite": "Na2S2O4",
        "H2O": "Distilled water",
    }

    def add(path, label, sp, quantity=None, *, descriptor=False, extra=False):
        assert path not in expected
        decision = decisions.get((key, tuple(sp)))
        if not extra:
            assert decision is not None
            quantity = decision.get("proposed_concentration")
            batch = decision.get("batch_input", {})
            # Early source-only reviews retained ml in notes. The schema's L
            # enum can carry that exact input without inventing a denominator.
            if batch.get("unit") == "ml" and (
                descriptor or not label.startswith("Sodium resazurin")
            ):
                quantity = liters(batch["amount"])
            if descriptor and label.startswith("Sodium resazurin"):
                quantity = liters("0.5")
        original_label = aliases.get(label, label) if key.startswith("K") else label
        matches = [
            p
            for p, n in old
            if n["preferred_term"].casefold() == original_label.casefold()
            and (p[-2] == "solutions") == descriptor
        ]
        assert len(matches) <= 1
        expected[path] = {
            "label": label,
            "quantity": quantity,
            "sp": sp,
            "descriptor": descriptor,
            "old": matches[0] if matches else None,
        }

    if key.startswith("K"):
        assert "solutions" not in after and len(after["ingredients"]) == len(data[key])
        for i, row in enumerate(data[key]):
            add(("ingredients", i), row[0], ["recipe_table", i + 1])
            assert expected[("ingredients", i)]["quantity"] == (
                None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"}
            )
        ph = (
            next(line for line in texts[key].splitlines() if line.startswith("PH Info:"))[8:]
            .strip()
            .split(",")[0]
        )
        if ph == "null":
            assert not {"ph_value", "ph_range"} & after.keys()
        elif "-" in ph:
            lo, hi = (float(n) for n in ph.split("-"))
            assert after["ph_range"] == {"min": lo, "max": hi} and "ph_value" not in after
        else:
            assert after["ph_value"] == float(ph) and "ph_range" not in after
        if key == "K829a":
            assert after["medium_type"] == after["composition_type"] == "DEFINED"
        if key == "K2027":
            assert (
                after["record_kind"] == "SOLUTION"
                and after["preparation_steps"] == before["preparation_steps"]
            )
        else:
            assert "preparation_steps" not in after
            assert "anoxic" in after["notes"] and "provider" in after["notes"]
            if key != "K829a":
                assert "sodium carbonate" in after["notes"] and "dithionite" in after["notes"]
        assert "variants" not in after
    elif key.startswith("D"):
        stages = data[key]["data"]["solutions"]
        ni, ns = 0, 0
        for ri, row in enumerate(stages[0]["recipe"]):
            sp = ["data", "solutions", 0, "recipe", ri]
            if "solution_id" in row or row.get("compound") == "Sodium resazurin":
                p = ("solutions", ns)
                ns += 1
                label = row.get("solution", row.get("compound"))
                if "compound" in row:
                    label += " (0.1% w/v)"
                add(p, label, sp, descriptor=True)
                assert expected[p]["quantity"] == liters(row["amount"])
                if "compound" in row:
                    add(p + ("composition", 0), "Sodium resazurin", sp)
                    assert len(get(after, p)["composition"]) == 1
                else:
                    si = next(i for i, s in enumerate(stages) if s["id"] == row["solution_id"])
                    stock = stages[si]
                    for j, component in enumerate(stock["recipe"]):
                        add(
                            p + ("composition", j),
                            component["compound"],
                            ["data", "solutions", si, "recipe", j],
                        )
                    steps = stock.get("steps", [])
                    assert get(after, p).get("preparation_notes", "") == "\n\n".join(
                        s["step"] for s in steps
                    )
                    titrant = {1680: "NaOH", 241: "KOH", 34: "H2SO4"}.get(stock["id"])
                    if titrant:
                        assert len(steps) == 1
                        add(
                            p + ("composition", len(stock["recipe"])),
                            titrant,
                            ["data", "solutions", si, "steps", 0, "step"],
                            extra=True,
                        )
                    assert len(get(after, p)["composition"]) == len(stock["recipe"]) + bool(titrant)
            else:
                add(("ingredients", ni), row["compound"], sp)
                ni += 1
        assert len(after["ingredients"]) == ni and len(after["solutions"]) == ns
        assert after["preparation_steps"] == before["preparation_steps"][: len(stages[0]["steps"])]
        if key == "D829a":
            assert "1020.5 ml" in after["notes"] and "no final-volume heading" in after["notes"]
        else:
            volume = {"D829": "1005", "D829b": "1005", "D829c": "1011", "D829d": "1020"}[key]
            assert f"final volume {volume} ml" in after["notes"]
            liquid_sum = sum(
                Decimal(str(r["amount"])) for r in stages[0]["recipe"] if r["unit"] == "ml"
            )
            assert str(liquid_sum) + " ml" in after["notes"]
        if key in {"D829", "D829c"}:
            assert len(after["variants"]) == 1
            variant = after["variants"][0]
            assert variant["relationship"] == "STRAIN_SPECIFIC_VARIANT"
            quote = variant["evidence"][0]["snippet"]
            assert quote in texts["DSMZ" + key[1:]] and quote.startswith("For DSM ")
            assert variant["modifications"] == [" ".join(quote.split()).split(": ", 1)[1]]
        else:
            assert "variants" not in after
    elif key == "M2587":
        sections = data[key]["components"]
        section_by_name = {s["subcomponent_name"]: s for s in sections if s["subcomponent_name"]}
        destinations = {1: ("ingredients",)}
        counts = {}
        for si, section in enumerate(sections):
            stage = section["paragraph_index"]
            for ri, row in enumerate(section["items"]):
                label = row["component_name"]
                descriptor = stage == 1 and (
                    label in section_by_name or label.startswith("Sodium resazurin")
                )
                parent = ("solutions",) if descriptor else destinations[stage]
                p = parent + (counts.get(parent, 0),)
                counts[parent] = p[-1] + 1
                sp = ["components", si, "items", ri]
                add(p, label, sp, descriptor=descriptor)
                if descriptor:
                    if label.startswith("Sodium resazurin"):
                        add(p + ("composition", 0), "Sodium resazurin", sp)
                        counts[p + ("composition",)] = 1
                    else:
                        destinations[section_by_name[label]["paragraph_index"]] = p + (
                            "composition",
                        )
        for p, count in counts.items():
            assert len(get(after, p)) == count
        main = [r for r in data[key]["comments"] if r["comment"] and r["paragraph_index"] < 8]
        assert [s["description"] for s in after["preparation_steps"]] == [
            r["comment"] for r in main
        ]
        for section in sections[1:]:
            stage = section["paragraph_index"]
            stop = min(
                (s["paragraph_index"] for s in sections if s["paragraph_index"] > stage),
                default=999,
            )
            notes = "\n\n".join(
                r["comment"]
                for r in data[key]["comments"]
                if stage < r["paragraph_index"] < stop and r["comment"]
            )
            assert get(after, destinations[stage][:-1]).get("preparation_notes", "") == notes
        assert after["ph_value"] == float(data[key]["meta"]["ph"]) and "high_metal" not in after
        assert "hydrogen-gas item" in after["notes"] and "80% N2" in after["notes"]
        assert "bicarbonate" in after["notes"] and "0.50 ml of 1 N NaOH" in after["notes"]
    else:
        assert key == "S1680" and after["composition"][:6] == before["composition"][:6]
        assert (
            not {"source_data", "evidence", "ingredients", "data_quality_flags", "solutions"}
            & after.keys()
        )
        rows = data[key]["data"]["recipe"]
        for i, row in enumerate(rows):
            add(("composition", i), row["compound"], ["data", "recipe", i])
        add(("composition", 7), "NaOH", ["data", "steps", 0, "step"], extra=True)
        assert (
            len(after["composition"]) == 8
            and after["preparation_notes"] == before["preparation_notes"]
        )

    actual_nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "solutions", "composition"} and "preferred_term" in n
    }
    assert actual_nodes == set(expected)
    lineage = {tuple(n["pointer"]): n for n in item["lineage"]}
    assert len(lineage) == len(item["lineage"]) and set(lineage) == set(expected)
    ids = {
        "term",
        "chebi_term",
        "mediaingredientmech_chebi_term",
        "mediaingredientmech_term",
        "synonyms",
    }
    for p, want in expected.items():
        node = get(after, p)
        assert (
            node["preferred_term"] == want["label"]
            and node.get("concentration") == want["quantity"]
        ), (key, p, want)
        assert "LB Medium" not in node.get("supplier_catalog", {}).get("supplier_name", "")
        line = lineage[p]
        assert (
            line["source"] == key
            and line["source_pointer"] == want["sp"]
            and line["label"] == want["label"]
        )
        assert line["old_pointer"] == (list(want["old"]) if want["old"] else None)
        original = get(before, want["old"]) if want["old"] else {}
        ignore = {"preferred_term", "concentration", "notes", "evidence"}
        if want["descriptor"]:
            assert (
                node["name"] == want["label"]
                and not (ids | {"evidence", "concentration_candidates"}) & node.keys()
            )
            assert set(node) <= {
                "name",
                "preferred_term",
                "concentration",
                "notes",
                "composition",
                "preparation_notes",
            }
        else:
            if want["label"] in {"NiCl2 x 6 H2O", "Sodium resazurin", "Calcium D-(+)-pantothenate"}:
                assert not ids & node.keys()
                ignore |= ids
            if key == "K2027":
                assert "source" not in node
                ignore.add("source")
            assert {k: v for k, v in node.items() if k not in ignore} == {
                k: v for k, v in original.items() if k not in ignore
            }
        if "[Merged" in original.get("notes", "") or "[Collapsed" in original.get("notes", ""):
            assert node["notes"].startswith(
                "Superseded flattening history, not a current quantity:"
            )
        d = decisions.get((key, tuple(want["sp"])))
        if (
            d
            and want["quantity"] is None
            and "batch_input" in d
            and d["batch_input"]["amount"] is not None
        ):
            inp = d["batch_input"]
            assert f"{inp['amount']} {inp['unit']}" in node["notes"]

    check_links(key, before, after, specs)
    claims = item["claims"]
    old_quantities = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert old_quantities == {
        tuple(c["old_pointer"])
        for c in claims
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    old_candidates = {
        p + ("concentration_candidates", i)
        for p, n in walk(before)
        for i in range(len(n.get("concentration_candidates", [])))
    }
    assert old_candidates == {
        tuple(c["old_pointer"]) for c in claims if c["kind"] == "old_candidate_accounted"
    }
    assert {p + ("concentration",) for p in expected} == {
        tuple(c["pointer"]) for c in claims if c["pointer"][-1] == "concentration"
    }
    archives = {
        c["old_pointer"][0]: c["old"] for c in claims if c["kind"] == "prior_nodes_archived"
    }
    assert archives == {f: before[f] for f in ("ingredients", "solutions") if before.get(f)}
    claimed = set()
    for c in claims:
        assert c["new"] == value(after, c["pointer"])
        assert c["old"] == (value(before, c["old_pointer"]) if c["old_pointer"] else None)
        assert c["snippet"] and c["snippet"] in texts[c["source"]]
        assert c["reference"] == context["sources"][c["source"]]["metadata"]["url"]
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
    urls = {s["metadata"]["url"]: k for k, s in context["sources"].items()}
    for p, node in walk(after):
        if "evidence" not in node:
            continue
        assert len(node["evidence"]) == len({e["reference"] for e in node["evidence"]})
        for e in node["evidence"]:
            assert (
                e["supports"] == "SUPPORT"
                and e["snippet"]
                and e["snippet"] in texts[urls[e["reference"]]]
            )
            actual.add((p, e["reference"]))
    assert actual == claimed
    old_refs = {r["reference"]: r for r in before.get("references", [])}
    refs = {r["reference"]: r for r in after["references"]}
    assert len(refs) == len(after["references"])
    assert set(refs) == set(old_refs) | {c["reference"] for c in claims}
    for url, ref in refs.items():
        original = old_refs.get(url, {})
        if url not in {c["reference"] for c in claims}:
            assert ref == original
            continue
        source = urls[url]
        expected_title = titles[source] if key == "S1680" else original.get("title", titles[source])
        assert ref["title"] == expected_title and not {"authors", "year"} & (
            ref.keys() - original.keys()
        )
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                context["sources"][source]["metadata"]["sha256"],
            )
        )
        assert ref["notes"].startswith(original.get("notes", ""))
    allowed = {
        "ingredients",
        "solutions",
        "composition",
        "notes",
        "evidence",
        "references",
        "curation_history",
        "parent_media",
        "variant_children",
        "variant_relationship",
        "variant_modifications",
        "preparation_steps",
        "variants",
    }
    if key.startswith("K") or key == "M2587":
        allowed |= {"ph_value", "ph_range"}
    if key == "K829a":
        allowed |= {"composition_type", "medium_type"}
    if key == "K2027":
        allowed.add("record_kind")
    if key == "S1680":
        allowed.add("data_quality_flags")
    if key == "M2587":
        allowed.add("high_metal")
    assert {k: v for k, v in after.items() if k not in allowed} == {
        k: v for k, v in before.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in claims
    ]
    prior_evidence = sum(len(n.get("evidence", [])) for _, n in walk(before))
    return {
        "source_nodes": len(expected),
        "old_quantity_slots": len(old_quantities),
        "old_candidate_slots": len(old_candidates),
        "claims": len(claims),
        "new_evidence": len(actual) - prior_evidence,
        "new_references": len(refs) - len(old_refs),
        "new_curation_history": 1,
    }


def check_links(key, before, after, specs):
    parents = {
        "K829": "D829",
        "K829a": "D829a",
        **dict.fromkeys(("K829.1", "K829.2", "K829.3", "K829_16661"), "K829"),
    }
    children = {
        "D829": ["K829"],
        "D829a": ["K829a"],
        "K829": ["K829.1", "K829.2", "K829.3", "K829_16661"],
    }

    def relation(k):
        return "DERIVED_FROM" if k in {"K829", "K829a"} else "STRAIN_SPECIFIC_VARIANT"

    def check_ref(ref, target, rel):
        expected = specs[target]
        assert {f: ref[f] for f in ("id", "path", "name", "relationship")} == {
            "id": expected["id"],
            "path": expected["path"],
            "name": yaml.safe_load(expected["before_text"])["name"],
            "relationship": rel,
        }
        assert ref["evidence"] and ref["notes"]

    if key in parents:
        check_ref(after["parent_media"], parents[key], relation(key))
        assert after["variant_relationship"] == relation(key)
        assert after["variant_modifications"] == [after["parent_media"]["notes"]]
    else:
        for field in ("parent_media", "variant_relationship", "variant_modifications"):
            assert after.get(field) == before.get(field)
    if key in children:
        assert len(after["variant_children"]) == len(children[key])
        for ref, target in zip(after["variant_children"], children[key], strict=True):
            check_ref(ref, target, relation(target))
    else:
        assert after.get("variant_children") == before.get("variant_children")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan-v2.json")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    results = {}
    for item in plan["records"]:
        results[item["key"]] = check(
            yaml.safe_load(item["before_text"]), yaml.safe_load(item["after_text"]), item
        )
        print(json.dumps({"key": item["key"], **results[item["key"]]}), flush=True)
    print(
        json.dumps(
            {
                "total": {
                    k: sum(r[k] for r in results.values()) for k in next(iter(results.values()))
                }
            }
        )
    )
