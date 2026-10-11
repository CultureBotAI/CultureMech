#!/usr/bin/env python3
"""Guarded evidence-only review of the inspected P3 and P6 direct formulations."""

from __future__ import annotations

import argparse
import copy
import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
ACTION = "ADDED_PUBLIC_DIRECT_CONCENTRATION_EVIDENCE"
ACCESSED = "2026-10-07"
BASE = "https://mediadive.dsmz.de/medium/"
ARTICLE = "doi:10.3390/microorganisms8091359"
ARTICLE_URL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7564587/"
CORRECTION_URL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8306464/"
SECTION = "sec2dot2dot1-microorganisms-08-01359"
ARTICLE_BASE_SHA = "12d90255948a61079316a9a395daad421a506ebbb03d9c4cfab9414c7871024d"
AUTHORS = ["Sarah Azinheiro", "Joana Carvalho", "Marta Prado", "Alejandro Garrido-Maestu"]
TITLE = (
    "Multiplex Detection of Salmonella spp., E. coli O157 and L. monocytogenes "
    "by qPCR Melt Curve Analysis in Spiked Infant Formula"
)
ARTICLE_QUOTES = [
    "10 g/L Tryptose",
    "5 g/L Beef extract",
    "5 g/L Yeast extract",
    "5 g/L NaCl",
    "3.4 g/L KH2PO4",
    "19.3 g/L Na2HPO4",
]
ARTICLE_HASHES = {
    "P6-article-PMC7564587.html": "4ba4130ab6f9e90804020f94a01f214a23fd3e2b1957d4934a8efefd7a77ffdc",
    "P6-correction-PMC8306464.html": "0d478c33c9abef1ebfacffda39f04bb84ff9a5b8394b679e00da89aed9280bf1",
}
TARGETS = {
    "P3": {
        "path": "data/normalized_yaml/bacterial/king_b.yaml",
        "id": "CultureMech:010433",
        "name": "king_b",
        "title": "King B",
        "before_sha256": "4a2776ae69ffc1e5945dfdaa962c97044f6851632af4277fd57f37107d736eb0",
        "source_sha256": "5ef4a1c49d241bfd226d2b343c94f3693832d3f93b29ab9ed5b976febc449e1b",
        "creator": "Perrine Portier (INRAE)",
        "published": "21.06.23",
        "rows": [
            ["K2HPO4", "1.5", "g", "1.5", "8.612", "10"],
            ["MgSO4 x 7 H2O", "1.5", "g", "1.5", "6.086", "8"],
            ["Proteose peptone no. 3", "20.0", "g", "20", "-", "316"],
            ["Glycerol", "10.0", "ml", "-", "-", "72"],
            ["Agar", "15.0", "g", "15", "-", "3"],
        ],
    },
    "P6": {
        "path": "data/normalized_yaml/bacterial/mta10.yaml",
        "id": "CultureMech:010436",
        "name": "mta10",
        "title": "mTA10",
        "before_sha256": "38a4d4634f878024c47e9c981c3ac7858883f6596c1a037e9c576148751b7c76",
        "source_sha256": "d308ad98c3128738c64a92d2666a8e17202c1f80aaa1ff3f99143c0848b091db",
        "creator": "Alejandro Garrido-Maestu (International Iberian Nanotechnology Laboratory)",
        "published": "01.11.23",
        "rows": [
            ["Tryptose", "10.0", "g", "10", "-", "819"],
            ["Beef extract", "5.0", "g", "5", "-", "85"],
            ["Yeast extract", "5.0", "g", "5", "-", "16"],
            ["NaCl", "5.0", "g", "5", "85.558", "43"],
            ["KH2PO4", "3.4", "g", "3.4", "24.984", "11"],
            ["Na2HPO4", "19.3", "g", "19.3", "135.955", "233"],
        ],
    },
}


class HTMLTree(HTMLParser):
    """Keep element boundaries and concatenate inline subscripts without new spaces."""

    VOID = set("area base br col embed hr img input link meta param source track wbr".split())

    def __init__(self, raw):
        super().__init__()
        self.root = {"tag": "root", "attrs": {}, "children": []}
        self.stack = [self.root]
        self.feed(raw)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "children": []}
        self.stack[-1]["children"].append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1]["children"].append(data)


def nodes(node, tag=None, **attrs):
    result = []
    for child in node["children"]:
        if isinstance(child, dict):
            if (tag is None or child["tag"] == tag) and all(
                child["attrs"].get(k) == v for k, v in attrs.items()
            ):
                result.append(child)
            result.extend(nodes(child, tag, **attrs))
    return result


def content(node):
    def pieces(n):
        for child in n["children"]:
            yield child if isinstance(child, str) else "".join(pieces(child))

    return " ".join("".join(pieces(node)).split())


def one(items):
    runner.require(len(items) == 1, "Source locator missing or ambiguous")
    return items[0]


def inspect_page(raw, mid):
    spec = TARGETS[mid]
    tree = HTMLTree(raw).root
    datasets = [
        json.loads(content(n))
        for n in nodes(tree, "script", type="application/ld+json")
        if json.loads(content(n)).get("@type") == "Dataset"
    ]
    dataset = one(datasets)
    runner.require(
        dataset["identifier"]["value"] == mid
        and dataset["name"] == spec["title"]
        and dataset["url"] == BASE + mid,
        "Wrong public dataset identity",
    )
    tables = [
        n for n in nodes(tree, "table") if "solution-table" in n["attrs"].get("class", "").split()
    ]
    table = one(tables)
    solution = one(
        [n for n in nodes(tree, "div") if "solution" in n["attrs"].get("class", "").split()]
    )
    runner.require(
        solution["attrs"]["id"] == "sol-0" and table in nodes(solution, "table"),
        "Stock topology changed",
    )
    volume = one(nodes(solution, "input", id="main-sol-vol"))
    runner.require(
        volume["attrs"]["value"] == volume["attrs"]["data-volume"] == "1000"
        and [content(n) for n in nodes(solution, "span", **{"class": "input-group-text"})]
        == ["ml"],
        "Unreviewed recipe scale or volume unit",
    )
    rows = nodes(table, "tr")
    runner.require(
        [content(n) for n in nodes(rows[0], "th")]
        == ["Compound", "Amount", "Unit", "Conc. [g/L]", "Conc. [mM]"],
        "Source column meanings changed",
    )
    observed, snippets = [], []
    for index, row in enumerate(rows[1:]):
        cells = [content(n) for n in nodes(row, "td")]
        link = one(nodes(row, "a"))["attrs"]["href"]
        runner.require(row["attrs"].get("id") == f"recipe-{index}", "Recipe row order changed")
        runner.require(link.startswith("/ingredients/"), "Wrong ingredient link")
        observed.append(cells + [link.removeprefix("/ingredients/")])
        snippets.append(" ".join(cells))
    runner.require(
        observed == spec["rows"], "Source ingredient, form, amount, or preparation drift"
    )
    metadata = [
        [content(n) for n in nodes(row, "td")] for row in nodes(tree, "tr") if row not in rows
    ]
    for expected in [
        ["Creator:", spec["creator"]],
        ["Published:", spec["published"]],
        ["Last modified:", spec["published"]],
        ["Source:", "MediaDive: public"],
        ["Final pH:", "7.2"],
    ]:
        runner.require(metadata.count(expected) == 1, "Source bibliographic/context drift")
    return snippets


def inspect_article(raw, correction):
    tree = HTMLTree(raw).root

    def meta(doc, name):
        return [n["attrs"]["content"] for n in nodes(doc, "meta", name="citation_" + name)]

    runner.require(
        meta(tree, "doi") == [ARTICLE.removeprefix("doi:")]
        and meta(tree, "title") == [TITLE]
        and meta(tree, "author") == AUTHORS
        and one(meta(tree, "publication_date")).startswith("2020"),
        "Article bibliographic identity drift",
    )
    section = one(nodes(tree, "section", id=SECTION))
    paragraphs = [content(n) for n in nodes(section, "p")]
    method = one([p for p in paragraphs if "Three medias were tested, mTA10 (" in p])
    method = method.partition("Three medias were tested, mTA10 (")[2]
    base, separator, variants = method.partition("), mTA10 replacing the KH2PO4 and Na2HPO4 by ")
    runner.require(separator and "MOPS" in variants, "Unresolved base/variant boundary")
    runner.require(runner.sha(base.encode()) == ARTICLE_BASE_SHA, "Base formulation context drift")
    runner.require(all(base.count(q) == 1 for q in ARTICLE_QUOTES), "Base formulation quote drift")
    corrected = HTMLTree(correction).root
    runner.require(meta(corrected, "doi") == ["10.3390/microorganisms9071482"], "Wrong correction")
    correction_text = " ".join(content(n) for n in nodes(corrected, "p"))
    runner.require(
        "There is a mistake in the primer sequences provided in Table 2" in correction_text,
        "Correction scope requires renewed review",
    )
    return method


def read_sources(cache, mid):
    runner.require(mid in TARGETS, "Unreviewed public medium")
    page = (cache / f"{mid}-medium-page.html").read_bytes()
    runner.require(runner.sha(page) == TARGETS[mid]["source_sha256"], "Page capture hash drift")
    snippets = inspect_page(page.decode(), mid)
    hashes = {f"{mid}-medium-page.html": runner.sha(page)}
    text = "\n".join(snippets)
    if mid == "P6":
        captures = {}
        for name, digest in ARTICLE_HASHES.items():
            value = (cache / name).read_bytes()
            runner.require(runner.sha(value) == digest, "Article/correction capture hash drift")
            captures[name] = value.decode()
            hashes[name] = digest
        text += "\n" + inspect_article(*captures.values())
    return text, {
        "mid": mid,
        "snippets": snippets,
        "hashes": hashes,
        "sha256": runner.sha(json.dumps(hashes, sort_keys=True).encode()),
        "accessed_at": ACCESSED,
    }


def review(doc, source, meta, timestamp):
    mid, after = meta["mid"], copy.deepcopy(doc)
    spec = TARGETS[mid]
    runner.require(
        doc["id"] == spec["id"]
        and doc["name"] == spec["name"]
        and doc["original_name"] == spec["title"]
        and doc["media_term"]["term"] == {"id": "mediadive.medium:" + mid, "label": spec["title"]},
        "Local source/record identity drift",
    )
    claims = runner.all_claims(doc)
    runner.require(
        len(claims) == len(spec["rows"]) == len(doc["ingredients"]), "Local topology drift"
    )
    runner.require(
        not any(doc.get(k) for k in ("solutions", "variants", "variant_children", "parent_media")),
        "Unreviewed stock or variant",
    )
    evidence_claims = []
    for index, (claim, row) in enumerate(zip(claims, spec["rows"], strict=True)):
        expected = (
            {"value": "10", "unit": "ML_PER_L"}
            if row[2] == "ml"
            else {"value": row[3], "unit": "G_PER_L"}
        )
        runner.require(
            claim["pointer"] == ["ingredients", index]
            and claim["ingredient"] == row[0]
            and claim["old"] == expected,
            "Local ingredient identity, order or concentration drift",
        )
        sources = [(BASE + mid, meta["snippets"][index], f"sol-0 / recipe-{index}")]
        if mid == "P6":
            sources.append((ARTICLE, ARTICLE_QUOTES[index], "Section 2.2.1, base mTA10 clause"))
        for reference, snippet, locator in sources:
            runner.require(snippet in source, "Inexact source excerpt")
            if reference == ARTICLE:
                scope = (
                    "Directly reported g/L in the base mTA10 clause, independently matching the "
                    "complete six-ingredient P6 formulation. No MOPS, glucose, supplement, "
                    "supplier restriction, growth or performance claim is imported. "
                    f"Full text inspected at {ARTICLE_URL}; the published correction at "
                    f"{CORRECTION_URL} concerns primer sequences, not this formulation."
                )
            else:
                scope = (
                    "User-contributed dataset formulation, not a verified sterilization/makeup "
                    "protocol. Table columns are Compound, Amount, Unit, Conc. [g/L], Conc. [mM]; "
                    "the main-sol-vol value/data-volume both declare 1000 and the adjacent unit "
                    "is ml. No molarity is asserted from the calculated mM column. "
                )
                scope += (
                    "The 10 ml glycerol amount / declared 1 L recipe scale = 10 ML_PER_L; "
                    "no density or mass conversion is made."
                    if row[2] == "ml"
                    else "The existing mass rate matches the source's g/L column exactly."
                )
            explanation = (
                f"Supports {claim['field']} ({row[0]}) only; locator: {locator}. {scope} "
                f"Accessed {ACCESSED}; source capture hashes: {json.dumps(meta['hashes'], sort_keys=True)}. "
                "HTML entities decoded, inline subscripts concatenated and whitespace collapsed."
            )
            entry = {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": explanation,
            }
            evidence = after["ingredients"][index].setdefault("evidence", [])
            runner.require(
                not any(e["reference"] == reference for e in evidence),
                "Existing source evidence requires separate reconciliation",
            )
            evidence.append(entry)
            evidence_claims.append(
                {
                    **claim,
                    "new": expected,
                    "status": "evidence_only",
                    "reference": reference,
                    "snippet": snippet,
                    "locator": locator,
                    "explanation": explanation,
                }
            )
    references = after.setdefault("references", [])
    page_reference = {
        "reference": BASE + mid,
        "title": f"{spec['title']} - MediaDive public Medium {mid}",
        "authors": spec["creator"],
        "year": 2023,
        "notes": f"source_type=user_contributed_dataset_page; discovery_mode=existing_record_reference; accessed_on={ACCESSED}; "
        f"page creator credited as author; displayed publication/last-modified date={spec['published']}; "
        "year refers to this dataset page, not a journal publication. The legacy bacmedia reference is retained.",
    }
    additions = [page_reference]
    if mid == "P6":
        additions.append(
            {
                "reference": ARTICLE,
                "title": TITLE,
                "authors": "; ".join(AUTHORS),
                "year": 2020,
                "notes": f"source_type=journal_article; discovery_mode=manual_web_search; accessed_on={ACCESSED}; "
                f"full_text={ARTICLE_URL}; locator=Section 2.2.1, base mTA10 clause; "
                f"correction_checked={CORRECTION_URL}; no correction to the medium formulation. "
                "This is independent formulation evidence; the existing 2013 Food Control reference's methods remain unverified.",
            }
        )
    for entry in additions:
        runner.require(
            not any(r["reference"] == entry["reference"] for r in references),
            "Reference already present",
        )
        references.append(entry)
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join(r["reference"] for r in additions),
        changes="Added concentration evidence only: "
        + "; ".join(
            f"{c['field']} {c['ingredient']} retains {json.dumps(c['old'], sort_keys=True)}"
            for c in claims
        ),
        notes="Exact source formulation checked; all quantities, ingredient forms, ontology annotations, "
        "pH, state, existing references and prior history preserved. No new growth association or variant.",
    )
    return after, evidence_claims


def adapter():
    return runner.ReviewAdapter(
        "medium_id", "MediaRecipe", read_sources, review, runner.all_claims, ("solutions",)
    )


def rebuild(plan, cache):
    runner.require(
        [r["medium_id"] for r in plan["records"]] == list(TARGETS), "Wrong reviewed target set"
    )
    for item in plan["records"]:
        spec = TARGETS[item["medium_id"]]
        runner.require(
            all(item[k] == spec[k] for k in ("path", "id", "name", "before_sha256")),
            "Target baseline drift",
        )
        before = item["before_text"]
        runner.require(
            runner.sha(before.encode()) == spec["before_sha256"], "Unreviewed before record"
        )
        source, meta = read_sources(cache, item["medium_id"])
        after, claims = review(runner.load_yaml(before), source, meta, plan["created_at"])
        runner.require(
            claims == item["claims"]
            and meta["sha256"] == item["source_sha256"]
            and meta["accessed_at"] == item["source_accessed_at"]
            and runner.sha(runner.render(before, after)) == item["after_sha256"],
            "Frozen evidence plan changed",
        )
        runner.require(not runner.errors(after, "MediaRecipe"), "Invalid reconstructed record")


def reports(folder, plan, applied):
    for item in plan["records"]:
        lines = [
            f"# Public Direct Concentration Review: {item['name']}",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- State: {'changed locally; evidence only' if applied else 'preview'}",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Result SHA256: `{item['after_sha256']}`",
            f"- Source bundle SHA256: `{item['source_sha256']}`",
            f"- Accessed: {ACCESSED}",
            f"- Baseline/post schema errors: {item['baseline_errors']} / {item['post_errors']}",
            f"- Failure: {item['failure'] or 'none'}",
            "",
            "All ingredient amounts are unchanged. Table snippets preserve rendered cell order; "
            "HTML entities/subscripts are decoded and whitespace collapsed. Metadata in YAML "
            "distinguishes dataset pages from the inspected journal methods. No growth evidence "
            "is added. Broader validation outcomes are recorded separately in validation.json.",
            "",
            "| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Scope / arithmetic | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for claim in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(claim[k])
                    for k in (
                        "field",
                        "ingredient",
                        "old",
                        "new",
                        "status",
                        "reference",
                        "snippet",
                        "locator",
                        "explanation",
                    )
                )
                + (" | applied |" if applied else " | proposed |")
            )
        path = folder / "records" / (item["name"] + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        plan = json.loads(args.plan.read_text())
        rebuild(plan, args.source_dir)
        outcome = (runner.apply if args.apply else runner.verify)(
            ROOT, plan, args.source_dir, adapter=adapter()
        )
    else:
        runner.require(not args.plan.exists(), "Refuse to overwrite reviewed plan")
        items = [
            {**{k: s[k] for k in ("path", "id", "name", "before_sha256")}, "medium_id": mid}
            for mid, s in TARGETS.items()
        ]
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        plan = runner.preview(ROOT, items, args.source_dir, commit, adapter=adapter())
        for item in plan["records"]:
            item["before_text"] = (ROOT / item["path"]).read_text()
        rebuild(plan, args.source_dir)
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        outcome = runner.summary(plan)
    if args.reports:
        reports(args.reports, plan, args.apply or args.verify)
    print(json.dumps(outcome, indent=2))


if __name__ == "__main__":
    main()
