"""Transcribe the record10 chemical/source assessment into an unsaved draft.

Provenance date: 2026-11-15.
Context: CultureMech #751 (JCM547/M549 findings), #752 (helper provenance) and
#754 (remove the original machine-specific native-artifact path). The current
portable entry point requires an explicit original-native directory; exact
historical executed source remains in scripts/batch079_provenance/history.

Required inputs: --chemical-dir with the retained chemical-audit directory,
--issue with the actual CultureMech issue URL, and --original-native-dir with
inspection.json, targets.yaml and the original schema/strict/terms/reference
logs plus strict.tsv. Run from the checkout root with Python/PyYAML and the
retained record10 JCM/MediaDive captures, peer report, issue artifacts, canonical
receipt streams, TOGO-attempt receipt, current target/sole TOGO owner and
separate lowercase comparison record, schemas, MIM index and runner v2.
Outputs: exclusive copies under record10/original-native, targets.yaml,
claim-inventory.json, inspect-orchestration.json and review.yaml beneath
.temp/batch079-scientific-20261114; one native inspect through runner v2 with
its command receipt and streams; a console draft/hash summary.

Replay limits: embedded decisions transcribe a completed manual assessment,
not a new scientific review. Required retained evidence and original input
hashes must match; existing exclusive outputs prevent a direct rerun. It does
not rerun canonical validators, save bundles or repair recipes. The lowercase
record is context only. Earlier bundle-only publication strings are historical
and superseded by #752; documentation does not alter saved review attestations.
"""

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN = Path(".temp/batch079-scientific-20261114")
D = RUN / "record10"
TARGET = "CultureMech:009942"
G = "data/merge_yaml/merged/DESULFOTOMACULUM_PBE_MEDIUM.yaml"
OWNER_PATH = "data/normalized_yaml/bacterial/TOGO_M549_Desulfotomaculum_PBE_Medium.yaml"
C = "data/normalized_yaml/bacterial/desulfotomaculum_pbe_medium.yaml"
REPAIR = "scripts/repair_togo_m549_score15.py"
JCM = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=547"
API = "https://mediadive.dsmz.de/rest/medium/J547"
CHECKS = {
    "schema": "20261115T081824139492Z-record10-schema.json",
    "strict": "20261115T081824635873Z-record10-strict.json",
    "terms": "20261115T081825506772Z-record10-terms.json",
    "references": "20261115T081825245374Z-record10-references.json",
    "jcm": "20261115T081824917685Z-record10-fetch-jcm.json",
    "mediadive": "20261115T081824666858Z-record10-fetch-mediadive.json",
}


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def digest(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def load(p):
    return json.loads((ROOT / p).read_text())


def write(p, obj):
    with (ROOT / p).open("x") as h:
        json.dump(obj, h, indent=2, ensure_ascii=False)
        h.write("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chemical-dir", required=True)
    ap.add_argument("--issue", required=True)
    ap.add_argument("--original-native-dir", type=Path, required=True)
    a = ap.parse_args()
    assert Path.cwd().resolve() == ROOT
    assert a.issue.startswith("https://github.com/CultureBotAI/CultureMech/issues/")
    chem_dir = Path(a.chemical_dir)
    hist = a.original_native_dir.resolve()
    original = json.loads((hist / "inspection.json").read_text())
    for item in original["source"]["inputs"]:
        assert digest(Path(item["path"])) == item["sha256"], item["path"]
    assert (
        original["targets"][0]["owner_paths"][0]["path"] == OWNER_PATH
        and len(original["targets"][0]["owner_paths"]) == 1
    )
    for name in [
        "targets.yaml",
        "inspection.json",
        "schema.log",
        "strict.log",
        "strict.tsv",
        "terms.log",
        "references.log",
    ]:
        dest = D / "original-native" / name
        (ROOT / dest).parent.mkdir(exist_ok=True)
        with (ROOT / dest).open("xb") as h:
            h.write((hist / name).read_bytes())
    with (ROOT / D / "targets.yaml").open("xb") as h:
        h.write((hist / "targets.yaml").read_bytes())
    docs = {p: yaml.safe_load((ROOT / p).read_text()) for p in [G, OWNER_PATH, C]}
    assert docs[G]["merged_from"] == ["TOGO_M549_Desulfotomaculum_PBE_Medium"]
    rows = []
    for path, doc in docs.items():
        for i, item in enumerate(doc["ingredients"]):
            name = item["preferred_term"]
            q = item["concentration"]
            bad = path == G and name in ["Distilled water", "5% Sodium lactate (autoclaved)"]
            rationale = (
                "Source gives an addition volume; this mass-per-volume unit is unsupported without a density conversion."
                if bad
                else "Source supplies the named batch amount. Per-liter values are interpreted on the nominal assembled 1000-mL basis, not a directly stated measured final volume."
            )
            if name == "N2":
                rationale = "Source specifies the N2 atmosphere; VARIABLE is not a quantified dissolved-gas concentration."
            rows.append(
                {
                    "document": path,
                    "field": f"ingredients[{i}].concentration",
                    "name": name,
                    "retained": q,
                    "decision": "correct" if bad else "evidence_only",
                    "rationale": rationale,
                    "source": "JCM547 Solution A; stock table for sodium-lactate addition",
                }
            )
        for i, sol in enumerate(doc.get("solutions", [])):
            rows.append(
                {
                    "document": path,
                    "field": f"solutions[{i}].concentration",
                    "name": sol["preferred_term"],
                    "retained": sol["concentration"],
                    "decision": "correct" if path == G else "evidence_only",
                    "rationale": (
                        "Source gives stock addition volume, not added stock mass."
                        if path == G
                        else "Separate stock addition volume is supported on the nominal batch basis; do not replace it with a solute mass."
                    ),
                    "source": "JCM547 four stock additions after Solution A",
                }
            )
            for j, item in enumerate(sol.get("composition", [])):
                rows.append(
                    {
                        "document": path,
                        "field": f"solutions[{i}].composition[{j}].concentration",
                        "name": item["preferred_term"],
                        "retained": item["concentration"],
                        "decision": "correct",
                        "rationale": "Literal percentage is supported; PERCENT_W_V and notes asserting explicit w/v source support are not established. Preserve unspecified percentage basis rather than deriving a final solute concentration.",
                        "source": "JCM547 literal stock percentages 5%,5%,4%,1%",
                    }
                )
    assert len(rows) == 41
    write(
        D / "claim-inventory.json",
        {
            "scope": "All 41 direct, stock-addition and nested concentration fields across selected generated target, sole owner and context-only J547 record. Decisions transcribe manual assessment of fixed original hashes.",
            "rows": rows,
        },
    )
    receipts = {}
    inputs = {Path(x["path"]) for x in original["source"]["inputs"]}
    for label, name in CHECKS.items():
        p = RUN / name
        r = load(p)
        assert r["exit"] == 0
        for stream in ["stdout", "stderr"]:
            assert digest(Path(r[stream])) == r[stream + "_sha256"]
            inputs.add(Path(r[stream]))
        if label in ["schema", "strict", "terms", "references"]:
            assert r["argv"][:3] == ["just", "validate-" + label, G]
        receipts[label] = (p, r)
        inputs.add(p)
    for p in (ROOT / D).glob("original-native/*"):
        inputs.add(p.relative_to(ROOT))
    for p in (ROOT / chem_dir).glob("*.json"):
        inputs.add(p.relative_to(ROOT))
    catalog = load(chem_dir / "ols-capture-catalog.json")
    chemical = load(chem_dir / "chemical-identity-assessment.json")
    for entry in catalog:
        raw = Path(entry["raw_path"])
        assert digest(raw) == entry["sha256"]
        inputs.add(raw)
    inputs.update(
        Path(p)
        for p in [
            G,
            OWNER_PATH,
            C,
            REPAIR,
            "src/culturemech/merge/formulation.py",
            "src/culturemech/schema/culturemech.yaml",
            "schema/record_review.yaml",
            "scripts/record_review.py",
            "scripts/batch079_build_record10_review.py",
            "scripts/batch079_run_check_v2.py",
            "AGENTS.md",
            "docs/record-reviews.md",
            "docs/record-review-profile.md",
            ".claude/skills/review-yaml-record/SKILL.md",
            ".claude/skills/curate-yaml-record/references/review-checklist.md",
            ".claude/skills/review-ingredient-concentrations/references/evidence-contract.md",
            "src/culturemech/data/mediaingredientmech/label_index.csv",
            "src/culturemech/data/mediaingredientmech/label_index.metadata.json",
        ]
    )
    inputs.update(
        D / x
        for x in [
            "jcm547.html",
            "mediadive-J547.json",
            "peer-review.md",
            "targets.yaml",
            "claim-inventory.json",
            "strict.tsv",
            "issue-body-20261115.md",
            "issue-filing-receipt-20261115.json",
        ]
    )
    togo = sorted((ROOT / RUN).glob("*-record10-fetch-togo.json"))
    assert len(togo) == 1
    tp = togo[0].relative_to(ROOT)
    tr = load(tp)
    inputs.add(tp)
    for stream in ["stdout", "stderr"]:
        assert digest(Path(tr[stream])) == tr[stream + "_sha256"]
        inputs.add(Path(tr[stream]))
    argv = [
        str(ROOT / ".venv/bin/python"),
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(D / "targets.yaml"),
    ]
    for p in sorted(inputs):
        argv.extend(["--input", str(p)])
    out = subprocess.run(
        [
            str(ROOT / ".venv/bin/python"),
            "scripts/batch079_run_check_v2.py",
            "record10-inspect-final",
            *argv,
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    write(
        D / "inspect-orchestration.json",
        {"argv": argv, "exit": out.returncode, "stdout": out.stdout, "stderr": out.stderr},
    )
    assert out.returncode == 0, out.stderr
    ip = Path(json.loads(out.stdout.splitlines()[0])["receipt"])
    ir = load(ip)
    assert ir["argv"] == argv and ir["exit"] == 0
    assert digest(Path(ir["stdout"])) == ir["stdout_sha256"]
    inspected = load(Path(ir["stdout"]))
    for item in inspected["source"]["inputs"]:
        assert digest(Path(item["path"])) == item["sha256"]
    now = datetime.now(timezone.utc)
    finish = now.isoformat().replace("+00:00", "Z")
    rid = now.strftime("%Y%m%dT%H%M%SZ") + "-batch079-record10-desulfotomaculum"
    owners = inspected["targets"][0]["owner_paths"]
    evidence = []

    def ev(
        key, kind, ref, summary, locator=None, snapshot=None, access=finish, support="context_only"
    ):
        x = {
            "evidence_id": key,
            "kind": kind,
            "reference": str(ref),
            "accessed_at": access,
            "support": support,
            "summary": summary,
        }
        if locator:
            x["locator"] = locator
        if snapshot:
            x["snapshot_sha256"] = snapshot
        evidence.append(x)

    ev(
        "E-record",
        "record_content",
        G,
        "Complete generated target, sole normalized TOGO owner and separate context-only J547 file read; all original inspection hashes match.",
        snapshot=digest(Path(G)),
    )
    ev(
        "E-jcm",
        "primary_source",
        JCM,
        "Exact recipe gives batch masses, water and separate stock volumes with literal percentages; default autoclave condition is explicit. Percentage basis and final pH are not specified in the fully read source.",
        "Full recipe547, Solution A and subsequent stock table; default sterilization header",
        digest(D / "jcm547.html"),
        receipts["jcm"][1]["started_at"],
        "partial",
    )
    ev(
        "E-api",
        "database",
        API,
        "Provider points to exact JCM source, but Solution A volume990 and g_l values conflict with nominal1000-mL assembly. Last unit ml] is also present in primary JCM text; computed rates are not independent concentration support.",
        "$.data.solutions[1], full recipe and steps",
        digest(D / "mediadive-J547.json"),
        receipts["mediadive"][1]["started_at"],
        "partial",
    )
    ev(
        "E-owner",
        "record_content",
        OWNER_PATH,
        "Owner already repairs volume units, four nested stock definitions and staged sterilization; its eight percentage-unit/notes assertions still overstate w/v support.",
        snapshot=digest(Path(OWNER_PATH)),
    )
    ev(
        "E-context",
        "record_content",
        C,
        "Full similarly named CultureMech:002894 file is source-duplicate context only, not an asserted merge input or repair owner for this selected generated target.",
        snapshot=digest(Path(C)),
    )
    ev(
        "E-repair",
        "record_content",
        REPAIR,
        "Full maintained repair script read without execution. Its _stock_solution hardcodes PERCENT_W_V and writes source-explicit w/v notes; future correction must prevent reintroduction and preserve historical events.",
        snapshot=digest(Path(REPAIR)),
    )
    ev(
        "E-peer",
        "prior_review",
        D / "peer-review.md",
        "Independent source report rechecked against current exact JCM/API/local inputs before adopting bounded findings.",
        snapshot=digest(D / "peer-review.md"),
    )
    ev(
        "E-quantities",
        "record_content",
        D / "claim-inventory.json",
        "Every current direct amount, stock addition and nested strength assessed with retained values and nominal-batch/percentage limits.",
        snapshot=digest(D / "claim-inventory.json"),
    )
    ev(
        "E-chemistry",
        "record_content",
        chem_dir / "chemical-identity-assessment.json",
        "Independent identifier audit; exact primary authority captures and packaged resolver statuses are separate evidence.",
        snapshot=digest(chem_dir / "chemical-identity-assessment.json"),
    )
    ev(
        "E-togo",
        "validation",
        tp,
        "Bounded exact TOGO endpoint request exit "
        + str(tr["exit"])
        + "; usable direct source corroboration remains unavailable if timeout. This is separate from successful native diagnostics.",
        snapshot=digest(tp),
        access=tr["started_at"],
    )
    for entry in catalog:
        t = entry["exact_terms"][0] if entry.get("exact_terms") else {}
        ev(
            "E-" + entry["id"].replace(":", "-"),
            "authority",
            entry["url"],
            str(t.get("label", "Exact authority response retained"))
            + "; active status and supplied-form assessment retained in chemical audit.",
            entry["id"],
            entry["sha256"],
            entry["started_at"],
        )
    checks = []
    notes = {
        "schema": "Schema structure only.",
        "strict": "One file, schema layer, zero errors; no corpus QC claim.",
        "terms": "Configured routes only; direct identifier assessment is separate.",
        "references": "ZERO evidence assertions checked on generated target; owner bibliography is not claim-level support.",
    }
    for key in ["schema", "strict", "terms", "references"]:
        p, r = receipts[key]
        checks.append(
            {
                "check_id": "C-" + key,
                "name": "Native " + key,
                "status": "passed",
                "required": True,
                "target_ids": [TARGET],
                "exit_code": r["exit"],
                "command": " ".join(r["argv"]),
                "summary": notes[key],
                "scope_note": str(p),
            }
        )
    checks += [
        {
            "check_id": "C-inspect",
            "name": "Native input inspection",
            "status": "passed",
            "required": True,
            "target_ids": [TARGET],
            "exit_code": 0,
            "summary": "Complete assessment inputs hashed against unchanged current bytes.",
            "scope_note": str(ip),
        },
        {
            "check_id": "C-science",
            "name": "Primary-source scientific assessment",
            "status": "failed",
            "required": True,
            "target_ids": [TARGET],
            "summary": "Assessment completed; generated representation and unsupported percentage-basis claims prevent scientific acceptance.",
            "evidence_ids": ["E-jcm", "E-owner", "E-record"],
        },
        {
            "check_id": "C-togo",
            "name": "Exact direct TOGO corroboration",
            "status": "unavailable",
            "required": False,
            "target_ids": [TARGET],
            "exit_code": tr["exit"],
            "command": " ".join(tr["argv"]),
            "summary": "Direct source unavailable in bounded current retrieval; linked JCM primary source supports the limited assessment.",
            "evidence_ids": ["E-togo"],
        },
    ]
    assessments = []

    def assess(key, area, topic, outcome, summary, refs, details=None):
        x = {
            "assessment_id": key,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [TARGET],
            "evidence_ids": refs,
        }
        if details:
            x["details"] = details
        assessments.append(x)

    assess(
        "A-identity",
        "identity",
        "Exact generated target, sole owner and context",
        "supported",
        "Current merge history identifies only TOGO_M549 as owner. Its imported JCM547 attribution agrees with the source title and maintained formulation; exact current direct TOGO data remain unavailable. The context-only002894 file is not promoted to merge ownership.",
        ["E-record", "E-owner", "E-context", "E-jcm", "E-togo"],
    )
    assess(
        "A-amounts",
        "quantity",
        "All direct, stock and nested amounts",
        "concern",
        "All41 concentration fields reviewed. Five generated volume amounts are misrepresented as mass. Owner/context stock additions preserve their nominal batch roles, but eight nested percentage fields assert an unsupported w/v basis. Source batch numbers and derived per-liter labels must remain distinct.",
        ["E-jcm", "E-api", "E-quantities", "E-owner"],
        "\n".join(
            f"{x['document']}::{x['field']} {x['name']}; retained={x['retained']}; decision={x['decision']}; {x['rationale']}"
            for x in rows
        ),
    )
    assess(
        "A-preparation",
        "scope",
        "Sequential sterilization and source default",
        "concern",
        "JCM explicitly supports121C/15min as its default. Owner/context preserve N2 base autoclaving, separately autoclaved phosphate/lactate and filter-sterilized iron/ascorbate before aseptic anaerobic addition. Generated output omits these structured instructions; stock names alone do not preserve the full sequence.",
        ["E-jcm", "E-record", "E-owner"],
    )
    assess(
        "A-class",
        "identity",
        "Complex mixture, physical state and biological scope",
        "supported",
        "Peptone and beef extract support COMPLEX/UNDEFINED with LIQUID physical state. Generic cultivation is supported; no organism growth, optimality, missing final pH or percentage convention is inferred.",
        ["E-jcm", "E-record", "E-owner"],
    )
    chemtext = "\n".join(
        x["id"] + "; " + x["status"] + "; " + x["rationale"] for x in chemical["assessments"]
    )
    assess(
        "A-chemistry",
        "grounding",
        "All asserted ontology identities",
        "concern",
        "All asserted IDs were inspected separately from native term checks; supplied hydrate forms, counterions, mixture scope and stereochemical limits are recorded per identifier. A supported identity does not establish stock percentage basis or concentration. MICRO:0000178 specifies an enzymatic mammalian-protein digest, beyond the generic Peptone wording in JCM; that specificity remains unconfirmed, with no forced replacement.",
        ["E-chemistry"] + ["E-" + x["id"].replace(":", "-") for x in catalog],
        chemtext,
    )
    assess(
        "A-evidence",
        "provenance",
        "History, references and current source limits",
        "concern",
        "Generated August6 artifact predates owner September11 repair event and preserves the old units/preparation structure. Existing event history and ingredients_curated flags are retained as historical statements. Owner/context bibliography does not support the stronger w/v assertion; target reference validation inspected zero evidence assertions. JCM/API lack final pH, but direct TOGO absence cannot be independently asserted.",
        ["E-record", "E-owner", "E-context", "E-repair", "E-jcm", "E-api", "E-togo"],
    )
    findings = []

    def finding(key, severity, category, title, desc, fields, refs):
        findings.append(
            {
                "finding_id": key,
                "issue_key": "batch079-record10-" + key.lower(),
                "severity": severity,
                "category": category,
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": desc,
                "field_paths": fields,
                "target_ids": [TARGET],
                "evidence_ids": refs,
                "owner_paths": owners,
                "external_issues": [a.issue],
                "rule_id": "CultureMech.single-record-checklist." + category,
                "native_severity": severity,
                "normalization_reason": "Severity follows the concrete unsupported representation or source claim; technical validator success is not scientific acceptance.",
            }
        )

    finding(
        "F-volume",
        "major",
        "quantity",
        "Generated source volumes are encoded as masses",
        "Generated water900, sodium-lactate stock70 and three stock additions10 use G_PER_L although primary table gives volumes. The owner already uses ML_PER_L and separates stock dose/strength. No density conversion justifies the old mass units.",
        [
            "ingredients[0].concentration",
            "ingredients[7].concentration",
            "solutions[*].concentration",
        ],
        ["E-record", "E-owner", "E-jcm"],
    )
    finding(
        "F-method",
        "major",
        "scope",
        "Generated target loses existing staged preparation",
        "Generated target has neither preparation_steps nor sterilization, while its owner and JCM distinguish base atmosphere, sequence and stock sterilization methods. Credit the supported121C/15min default; preserve stock-specific exceptions.",
        ["preparation_steps", "sterilization"],
        ["E-record", "E-owner", "E-jcm"],
    )
    finding(
        "F-percent",
        "major",
        "evidence",
        "Owner asserts a percentage basis absent from inspected source",
        "Four owner composition units and their notes assert PERCENT_W_V/source-explicit w/v. Current JCM and API only give5%,5%,4%,1%. The repair helper hardcodes this claim. Retain literal percentages with explicit uncertainty until basis is verified, preserving currently supported stock doses and avoiding final-mass conversion. Context002894 has the same issue but is not an additional target or owner.",
        ["solutions[*].composition[0].concentration.unit", "solutions[*].composition[0].notes"],
        ["E-owner", "E-jcm", "E-api", "E-repair", "E-context"],
    )
    finding(
        "F-linkage",
        "minor",
        "provenance",
        "Evidence linkage and exact-source specificity remain limited",
        "Target has no evidence assertions; owner/context reference URLs are not exact support for every quantity or basis. Direct TOGO is unavailable, so their universal statement that TOGO reports no final pH is not independently corroborated. Preserve the linked JCM identity and qualify current-source scope rather than inventing pH or stronger equivalence. Owner/context MICRO:0000178 specifies an enzymatic mammalian digest that the generic primary Peptone label does not establish; this is an unconfirmed specificity, not a demonstrated wrong product.",
        ["notes", "references", "evidence", "parent_media", "owner::ingredients[0].term"],
        ["E-record", "E-owner", "E-context", "E-jcm", "E-api", "E-togo", "E-chemistry"],
    )
    actions = [
        {
            "action_id": "ACT-source",
            "description": "Resolve the exact percentage convention and source attribution in the sole authoritative TOGO owner and relevant maintained repair logic; otherwise preserve an explicit unspecified basis. Keep supported stock volume and preparation repairs.",
            "finding_ids": ["F-percent", "F-linkage"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "acceptance_checks": [
                "Attach narrow primary-source evidence or preserve explicit percentage-basis uncertainty; do not invent density, final mass or final pH.",
                "Verify generic mixture grounding without assuming a peptone digest process or animal source.",
                "Preserve existing history; the old repair helper replaces matching historical events, so do not blindly rerun it for a new correction.",
                "Keep context-only002894 outside this target ownership; separately coordinate any shared-transform effect.",
            ],
        },
        {
            "action_id": "ACT-output",
            "description": "After source decisions, regenerate the selected output through the maintained merge workflow with its verified owner and review the exact product diff.",
            "finding_ids": ["F-volume", "F-method"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "depends_on": ["ACT-source"],
            "generator": "src/culturemech/merge/merge_recipes.py with explicitly scoped verified owner set",
            "acceptance_checks": [
                "Preserve stable identity and source-specific stock additions/strengths, N2 atmosphere and stock-method exceptions.",
                "Run documented schema/strict/term/reference and applicable merge/ID gates on changed surfaces, then independent scientific review.",
                "Do not infer a current merger-code defect from this stale output or hand-edit generated YAML.",
            ],
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": rid,
        "kind": "record",
        "repository": "CultureBotAI/CultureMech",
        "title": "Recovered batch079 record10: JCM547 / TOGO M549 scientific assessment",
        "started_at": receipts["mediadive"][1]["started_at"],
        "finished_at": finish,
        "reviewer": {
            "identity": "Codex recovery reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Did not author or modify the existing scientific inputs. Independent primary-source and identifier contributions were checked against exact current bytes; this is not human approval.",
        },
        "skill": ".claude/skills/review-yaml-record/SKILL.md",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Completed bounded assessment identifies three major defects and one minor provenance limitation. Existing owner volume/preparation repairs are credited; percentage-basis support and generated freshness remain unresolved. No scientific source was edited.",
        "source": inspected["source"],
        "scope": {
            "description": "One exact generated target with its sole normalized TOGO owner and separate context-only J547 record; full files, all direct/nested amounts, IDs, conditions, history and evidence scope inspected.",
            "selection": "Recovered batch079 record10 explicit manifest, not a name-similarity selection.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
            "exclusions": [
                {
                    "target": "Other batch079 records, PR692, variant queue and catalog repair",
                    "reason": "Separate scopes; no full-batch completion or release readiness is asserted.",
                },
                {
                    "target": "CultureMech:002894 as a curation target or merge owner",
                    "reason": "Inspected only as source/variant context.",
                },
            ],
        },
        "targets": inspected["targets"],
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Completed assessment is a needs_curation verdict, not scientific acceptance. Technical passes and historical ingredients_curated flags do not resolve findings.",
            "Per-liter interpretation uses the nominal900+10+70+10+10mL assembly; neither a measured final volume nor stock percentage basis is invented. API990-mL computed rates are not adopted.",
            "Direct current TOGO corroboration is unavailable. JCM and provider attribution support this limited source review, not unseen current TOGO content.",
            "Reference validation inspected zero evidence assertions on the selected generated target. Owner/context bibliography remains distinct from narrow assertion evidence.",
            "No scientific file, historical event or generated product was changed; follow-up is filed. Broad corpus, merge-freshness and export gates are not claimed executed.",
            "Raw evidence and one-run helper scripts remain in the durable checkout; publication scope is immutable review bundles only.",
        ],
        "notes": [
            "started_at uses the first recorded current source-capture time; full-file reading began earlier without a separately persisted timestamp. Original technical receipts remain preserved.",
            "Current JCM explicitly supplies the121C/15min default; it is retained as supported, not flagged as inferred.",
        ],
        "links": [
            a.issue,
            "https://github.com/CultureBotAI/CultureMech/issues/408",
            "https://github.com/CultureBotAI/CultureMech/issues/150",
        ],
        "tags": ["batch079", "record10", "needs_curation", "source_review"],
    }
    with (ROOT / D / "review.yaml").open("x") as h:
        yaml.dump(review, h, Dumper=Dumper, sort_keys=False, allow_unicode=True)
    print(
        json.dumps(
            {
                "draft": str(D / "review.yaml"),
                "sha256": digest(D / "review.yaml"),
                "review_id": rid,
                "inputs": len(inspected["source"]["inputs"]),
                "fields": len(rows),
            }
        )
    )


if __name__ == "__main__":
    main()
