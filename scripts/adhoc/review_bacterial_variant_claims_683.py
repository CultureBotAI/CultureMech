#!/usr/bin/env python3
"""Record independent source review of 46 bacterial/specialized events, 2026-11-16.

Inputs: frozen reviewed proposal, exact recipes and retained primary captures.
Outputs: native inspection and review draft for #683/#763; no recipe writes.
Manual source judgments below record the root reviewer's reading, not an
automated claim that parsing or matching a quotation proves scientific truth.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from review_variant_family_proposals_683 import targets

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = "conf/variant_ingredient_curation/bacterial-specialized-683.json"
DIGEST = "f3ae005ac2d08bdb104330cca0303979ebbf0c3ade4eade7c0e588919533b08f"
SOURCE_JUDGMENTS = {
    "spectrum": "Methods supports reported 1.5 M NaCl; does not establish the complete imported basal formula.",
    "emami": "Methods supports HCl acidification, 1.06e-4 M silicate, 29.4 mM nitrate and separate 200/50 microgram/mL antibiotic treatments. Chemical forms and untreated controls are not inferred.",
    "hiibel": "Strains and media supports 33.6 g/L sea salts and replacement with the named 2ASW vitamin solution. No constituent expansion or complete parent equivalence asserted.",
    "751": "Official liquid-medium instruction omits corn meal agar; changed absolute phosphate batch masses remain held under #760.",
    "125": "Official preparation provides 5 mL methanol as an alternative to methane-air cultivation. Quantity remains a batch amount; final volume/purity unspecified.",
    "956": "Official alternatives state 0.5% methanol or 0.3% methylamine without percent basis. Literal doses remain notes; no simultaneous use or percent-unit inference.",
    "1021": "Official Solution A specifies 8.10 g casein hydrolysate as the lactalbumin-hydrolysate alternative. Undefined mixtures, batch amount and serum context preserved.",
    "829": "Official DSM16661/21157 instruction omits growth-stimulating factors. Gas headspace remains a condition.",
    "nbrc": "NBRC1002 preparation supports 10 mg/L hydrated FeSO4 plus 0.25 g/L yeast extract in the heterotrophic arm and 13.9 g/L FeSO4 in the autotrophic arm; pH1.7 acid titration has no inferred dose.",
    "blumer": "Methods explicitly omits Trypticase, cysteine-HCl and resazurin. Sulfide stock 10% wt/vol versus final 0.5% without independently stated basis remains literal text, not a converted concentration.",
    "teusink": "Table1 header establishes g/liter; pantothenate0.001 and minimal-subset biotin0.0025 mass concentrations match. Boldface subset membership checked in original HTML; no molar conversion.",
    "wendisch": "Methods supports sodium[1-13C]acetate10 g/L, unlabeled glucose10 g/L and D-[5-13C]glucose20 g/L. Figure1 35 mM glucose is a separate arm; isotope positions/counterion and nominal Table2 molarity remain distinct.",
    "kaminskyj": "20X nitrate stock specifies 5.2 g anhydrous MgSO4 per liter as the hydrated-salt alternative; MM uses18 g agar, distinct from CM15 g. Stock and final-medium quantities are not conflated.",
    "10609610": "Primary abstract supports reported medium100 g NaCl/L only; complete basal formula and every growth level are not certified.",
    "38194015": "Primary abstract supports 5 g/L yeast-extract enrichment only, with no inferred basal-plus-supplement total.",
    "12420179": "Primary abstract supports the separate300 mM aluminum-sulfate exposure; hydration and whole-parent equivalence remain unresolved.",
    "19826864": "Primary abstract supports L-phenylalanine as sole nitrogen source; dose and displaced basal nitrogen identities remain unresolved.",
    "15931519": "Primary abstract supports dextrose omission and separate soluble-starch/maltose arms at0.5 or1.0% w/v. No union of alternative substrate arms is implied.",
    "37088211": "Primary abstract supports10 mg/L Cr(VI) exposure only; administered salt/counterion is unspecified and not inferred.",
    "35960254": "Held claim remains outside the46 accepted events; no inaccessible detailed methods claim is promoted.",
    "7520742": "Primary abstract supports10% serum with unspecified basis and the reported3.5 mM peroxide exposure. Neither is a complete recommended growth formulation.",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", required=True, type=Path)
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    raw = (ROOT / PROPOSAL).read_bytes()
    if sha(raw) != DIGEST:
        raise ValueError("frozen proposal changed")
    document = json.loads(raw)
    selected = targets(document)
    count = 0
    for record in document["records"]:
        data = (ROOT / record["path"]).read_bytes()
        if sha(data) != record["expected_sha256"]:
            raise ValueError("target changed: " + record["path"])
        actual = yaml.safe_load(data)
        for variant in record["variants"]:
            original = actual["variants"][variant["variant_index"]]
            assert original["name"] == variant["variant_name"]
            for change in variant["ingredient_changes"]:
                assert (
                    original["modifications"][change["source_modification_index"]]
                    == change["source_text"]
                )
                count += 1
    assert count == 46 and len(selected) == 26
    target_file = directory / "targets.yaml"
    target_file.write_text(yaml.safe_dump({"targets": selected}, sort_keys=False))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(target_file.relative_to(ROOT)),
        "--input",
        PROPOSAL,
    ]
    evidence = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for source in document["source_inspections"]:
        if sha((ROOT / source["path"]).read_bytes()) != source["sha256"]:
            raise ValueError("primary capture changed: " + source["key"])
        command.extend(["--input", source["path"]])
        evidence.append(
            {
                "evidence_id": source["key"],
                "kind": "primary_source",
                "reference": source["reference"],
                "locator": source["locator"],
                "accessed_at": now,
                "support": "supports",
                "summary": SOURCE_JUDGMENTS[source["key"]],
            }
        )
    result = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    inspection = json.loads(result.stdout)
    (directory / "inspection.json").write_text(result.stdout)
    ids = [item["target_id"] for item in selected]
    review_id = now.replace("-", "").replace(":", "") + "-bacterial-variant-independent-claims"
    review = {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Independent scientific review of46 bacterial and specialized variant events",
        "started_at": "2026-11-16T21:26:00Z",
        "finished_at": now,
        "reviewer": {
            "identity": "codex-root-independent-claim-reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Reviewer did not author this cohort's46 proposal events or evidence repairs. Separate read-only primary-source comparison; reviewer authored the shared applicator and different cohorts, which are outside this independence claim.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "native_verdict": "The46 bounded proposed events are supported at their stated stages; strengthened exact quantitative excerpts address #763 for this cohort. No held claim is promoted.",
        "summary": "Primary values, chemical forms, stock/final bases, isotope positions and negative/alternative events agree with the frozen proposal. Abstract-only evidence supports only explicitly stated identities/doses. Complete recipe equivalence and unrelated claims are not approved.",
        "source": inspection["source"],
        "scope": {
            "description": "46 proposed events in26 source-hash-pinned recipes selected from the126-row cohort.",
            "selection": "Exact frozen proposal SHA256 recorded by the retained helper.",
            "coverage": "partial",
            "population_size": 26,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Held and condition-only rows; unrelated recipe content",
                    "reason": "No scientific clearance of inaccessible details, ambiguous batch quantities, whole formulations or growth claims.",
                }
            ],
        },
        "targets": selected,
        "checks": [
            {
                "check_id": "frozen-inputs",
                "name": "Exact proposal, recipe, source and text coordinates",
                "status": "passed",
                "required": True,
                "summary": "46event/26record count and every expected hash, variant name and source text checked; native input inspection retained.",
                "target_ids": ids,
            },
            {
                "check_id": "primary-claims",
                "name": "Independent primary source and quantitative evidence reading",
                "status": "passed",
                "required": True,
                "summary": "Source-specific judgments below support the frozen scientific payload and repaired quantity/basis excerpts. No automated source matching is presented as scientific review.",
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in evidence],
            },
        ],
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "bounded-claims",
                "area": "scope",
                "topic": "46 source-bound variant ingredient events",
                "outcome": "supported",
                "summary": "Independent source judgments support the proposed identities, doses and stages within the explicitly bounded scope; #763 quantitative excerpts have been repaired.",
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in evidence],
            }
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Bounded agent scientific review, not human approval or whole-record certification.",
            "Native writer/corpus/export acceptance and release adoption remain separate gates.",
            "Held source/model rows and abstract-only limitations remain explicit in the126-row disposition ledger.",
            "Unsupported numeric conversion, unknown percent basis, chemical salt or hydrate identity is not inferred.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/683",
            "https://github.com/CultureBotAI/CultureMech/issues/763",
        ],
    }
    (directory / "review.yaml").write_text(
        yaml.safe_dump(json.loads(json.dumps(review)), sort_keys=False, allow_unicode=True)
    )
    print(
        json.dumps(
            {"review_id": review_id, "review": str((directory / "review.yaml").relative_to(ROOT))}
        )
    )


if __name__ == "__main__":
    main()
