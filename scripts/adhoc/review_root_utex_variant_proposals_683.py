#!/usr/bin/env python3
"""Package independent root55/UTEX claim review (#683/#763, 2026-11-16).

Inputs: frozen proposals, source captures, maintained recipes and manual source
judgments below. Outputs: new native inspection and review draft; no recipe writes.
This records the agent's source reading, not an automated scientific certification.
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
PROPOSALS = {
    "remaining-families-683.json": "bdbfd610071cb3e1983a627ea30e799c2c5a786bddcba52fab2f31958d2d992f",
    "utex-optional-683.json": "d56794675b4a8a3a1bcbceed428f16d734bf624c7331d89e175020c804ec539f",
}
SOURCE_FILES = [
    ".temp/variant-683/sources/dsmz-645/source.pdf",
    ".temp/variant-683/sources/dsmz-670/source.pdf",
    ".temp/variant-683/sources/villasenor-2011/source.xml",
    ".temp/variant-683/sources/mattanovich-2009/verified-s3.xls",
    ".temp/variant-683/sources/mattanovich-2009/s3-cells.json",
]
GROUP_JUDGMENTS = {
    "batch_medium": "Mattanovich Additional file 3 A13–A22 supports chemostat quantities per liter; A24–A33 separately defines trace stock per liter; A39 distinguishes dynamic ammonium-hydroxide pH control from initial HCl. The proposal retains stock doses/compositions in separate stages, removes the old flattened entries and does not infer final constituent molarity. Exact chemical forms and amounts agree with the inspected XLS cells.",
    "for_dsm": "Current official DSMZ670 (2022) prescription supports the strain-specific sulfur/glucose/yeast-extract additions, ferrous-sulfate omissions, pH titrant strengths and retained FeSO4 stock for DSM9468. Water-batch change is explicitly held; normality is not converted. This does not certify the historical imported parent's version.",
    "middlebrook": "Official DSMZ645 alternative table supports all fifteen named inputs and literal batch masses/volume. Each ADD belongs to the from-scratch alternative to the commercial route; it does not materialize a union with the commercial parent. The separate OADC formula and full executable preparation are outside these rows.",
    "mm_biotin": "Villasenor Methods explicitly states final 10 micrograms/mL biotin and thiamine, separately sterilized calcium dihydrate and iron hexahydrate, and MM without the MMP calcium-pantothenate supplement. Negative event is omission, not positive ingredient presence or physical removal.",
    "mmp_biotin": "Villasenor Methods supports the same vitamin/salt preparation plus 1 micromolar calcium pantothenate in MMP. Source amount denotes calcium salt; no doubling, anion reinterpretation or molecular-weight conversion is introduced.",
    "ms10": "Nordkvist original ASM Methods and Figure 1/Table 2 independently read: MnSO4 mass concentration, timed 0.3 g/L sodium acetate after 7 h 38 min, and separate 0.82 g/L acetate without DL-6,8-thioctic acid agree with the proposal. Preculture phosphate basis remains explicitly held; growth outcomes are not recertified.",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, value):
    with path.open("x", encoding="utf-8") as stream:
        yaml.safe_dump(json.loads(json.dumps(value)), stream, sort_keys=False, allow_unicode=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    proposals, all_targets = [], []
    for filename, digest in PROPOSALS.items():
        path = ROOT / "conf/variant_ingredient_curation" / filename
        if sha(path) != digest:
            raise ValueError("frozen proposal drift: " + filename)
        proposal = json.loads(path.read_text())
        proposals.append(proposal)
        all_targets.extend(targets(proposal))
        for record in proposal["records"]:
            raw = (ROOT / record["path"]).read_bytes()
            if hashlib.sha256(raw).hexdigest() != record["expected_sha256"]:
                raise ValueError("target drift: " + record["path"])
            actual = yaml.safe_load(raw)
            for variant in record["variants"]:
                source = actual["variants"][variant["variant_index"]]
                if source["name"] != variant["variant_name"]:
                    raise ValueError("variant identity drift")
                for change in variant["ingredient_changes"]:
                    if (
                        source["modifications"][change["source_modification_index"]]
                        != change["source_text"]
                    ):
                        raise ValueError("exact source coordinate drift")
    target_path = directory / "targets.yaml"
    write_new(target_path, {"targets": all_targets})
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(target_path.relative_to(ROOT)),
    ]
    for path in ["conf/variant_ingredient_curation/" + name for name in PROPOSALS] + SOURCE_FILES:
        command.extend(["--input", path])
    result = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True)
    inspection = json.loads(result.stdout)
    (directory / "inspection.json").write_text(result.stdout)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    review_id = now.replace("-", "").replace(":", "") + "-root55-utex-independent-claims"
    ids = [t["target_id"] for t in all_targets]
    root_ids = [r["recipe_id"] for r in proposals[0]["records"]]
    evidence = []
    assessments = []
    for pi, proposal in enumerate(proposals):
        for record in proposal["records"]:
            stem = Path(record["path"]).stem
            eid = "claims-" + record["recipe_id"].split(":")[-1]
            refs = sorted(
                {
                    e["reference"]
                    for v in record["variants"]
                    for c in v["ingredient_changes"]
                    for e in c["evidence"]
                }
            )
            if pi == 1:
                judgment = "Independently read the exact UTEX collection recipe page and optional-preparation instruction. Named carbonate, agar, water and thiosulfate inputs agree with the source; 200 mL batch or separate 500 mL portions and cooling/combining stages are retained. Source does not quantify thiosulfate on the salt-variant pages; no linked-base dose is inherited. J Medium's source-designated 1.25% agar is supported by its paired 12.5 g and 1 L instruction."
            else:
                judgment = next(
                    value for prefix, value in GROUP_JUDGMENTS.items() if stem.startswith(prefix)
                )
            evidence.append(
                {
                    "evidence_id": eid,
                    "kind": "primary_source",
                    "reference": refs[0],
                    "locator": "; ".join(
                        sorted(
                            {
                                e["explanation"].split(". Primary source")[0]
                                for v in record["variants"]
                                for c in v["ingredient_changes"]
                                for e in c["evidence"]
                            }
                        )
                    ),
                    "accessed_at": now,
                    "support": "supports",
                    "summary": judgment,
                }
            )
            assessments.append(
                {
                    "assessment_id": eid,
                    "area": "scope",
                    "topic": record["variants"][0]["variant_name"],
                    "outcome": "supported",
                    "summary": judgment
                    + " Quantity-evidence excerpts require the issue763 repair before application; this is not whole-record approval.",
                    "target_ids": [record["recipe_id"]],
                    "evidence_ids": [eid],
                    "dimensions": [
                        {
                            "name": "native_concentration_decision",
                            "value": "evidence_only",
                            "definition": "Primary values/forms/stages support the proposed events; stronger exact amount/basis quotations remain needed. No new scientific quantity inferred.",
                            "evidence_ids": [eid],
                        }
                    ],
                }
            )
    review = {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Independent scientific review of root55 and optional UTEX variant proposals",
        "started_at": "2026-11-16T21:23:00Z",
        "finished_at": now,
        "reviewer": {
            "identity": "codex-independent-variant-reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Did not author these root55 or UTEX proposal decisions and made no changes to them during this review. Authored shared schema/validator and other source-family proposals; this scope independently compares these authors' frozen claims to primary content.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "needs_curation",
        "native_verdict": "Scientific quantities/forms/stages supported for the 95 proposed events; exact attached quantity/basis evidence repair #763 remains required. No source recipe was edited.",
        "scientific_review": True,
        "summary": "Independent source comparison found no additional quantity, form, stage or positive/negative accounting defect in this bounded proposal scope. Filed #763 for insufficient quantitative excerpts. Root55 contains explicit holds and alternative preparations; those are not silently promoted.",
        "source": inspection["source"],
        "scope": {
            "description": "55 root-family rows plus 17 UTEX optional rows, 24 exact normalized-record targets and 95 proposed events.",
            "selection": "Two frozen proposal SHA256s in retained provenance helper; exact source coordinates checked against maintained recipes.",
            "coverage": "partial",
            "population_size": 24,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Other record ingredients, identity/growth claims and unrelated variants",
                    "reason": "Not scientifically recertified; proposal review does not approve complete recipe equivalence.",
                },
                {
                    "target": "Held phosphate/water quantities and executable variant expansion",
                    "reason": "Existing explicit holds retained; no missing quantity basis or component inheritance inferred.",
                },
            ],
        },
        "targets": all_targets,
        "checks": [
            {
                "check_id": "native-inputs",
                "name": "Native exact-input inspection and coordinate check",
                "status": "passed",
                "required": True,
                "summary": "24 recipe hashes/variant names/source texts matched frozen proposals; native inspector captured proposal and available primary-source bytes.",
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in evidence],
            },
            {
                "check_id": "source-content",
                "name": "Independent primary-source reading",
                "status": "passed",
                "required": True,
                "summary": "Read DSMZ645/670 PDFs, Villasenor Methods, verified Mattanovich XLS cell extraction, Nordkvist ASM Methods and Figure1/Table2, and all13 exact UTEX source pages. Direct web sources lack local byte snapshots; no claim of local source-hash verification for those.",
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in evidence],
            },
            {
                "check_id": "application",
                "name": "Central guarded application",
                "status": "not_applicable",
                "required": False,
                "summary": "No application performed by reviewer. Existing native presentation guard failures are separately owned and do not change the scientific source assessment.",
                "target_ids": ids,
            },
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": [
            {
                "finding_id": "quantity-excerpts",
                "issue_key": "variant-quantity-excerpts-763",
                "category": "provenance",
                "severity": "minor",
                "status": "open",
                "certainty": "confirmed",
                "title": "Quantified events need exact amount/unit/basis excerpts",
                "description": "Many source-supported quantities have label-only snippets. Quote source quantities with their units and separately quoted table/preparation bases before application; preserve scientific payload and original review.",
                "target_ids": root_ids,
                "field_paths": ["variants[].ingredient_changes[].evidence[]"],
                "evidence_ids": [e["evidence_id"] for e in evidence[: len(root_ids)]],
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CultureMech",
                        "path": "conf/variant_ingredient_curation/remaining-families-683.json",
                        "role": "proposal evidence owner",
                    }
                ],
                "external_issues": ["https://github.com/CultureBotAI/CultureMech/issues/763"],
            }
        ],
        "actions": [
            {
                "action_id": "repair-quantity-excerpts",
                "description": "Preserve frozen originals, strengthen the exact amount/unit/basis evidence excerpts, and independently re-review the quote-only corrections before application.",
                "finding_ids": ["quantity-excerpts"],
                "target_ids": root_ids,
                "ownership_note": "Proposal authors; central workflow owns application and subsequent validation.",
                "acceptance_checks": [
                    "Exact source amount and unit quoted",
                    "Separately located basis quoted with locator",
                    "Scientific payload and source coordinates unchanged",
                    "Focused independent review of corrected proposals",
                ],
            }
        ],
        "limitations": [
            "Independent scientific claim review, not whole-record human approval, completed curation or release acceptance.",
            "Native presentation/schema/application gates remain owned by the central application workflow.",
            "UTEX and Nordkvist source content was read with the web reader; no retained local source digest is claimed for those pages.",
            "The source-specific alternative preparations and negative events must not be materialized as universal parent-plus-additions recipes.",
            "Issue763 evidence repair and focused independent re-review remain before application.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/763",
            "https://github.com/CultureBotAI/CultureMech/issues/683",
        ],
    }
    write_new(directory / "review.yaml", review)
    print(
        json.dumps(
            {"review": str((directory / "review.yaml").relative_to(ROOT)), "review_id": review_id}
        )
    )


if __name__ == "__main__":
    main()
