# Chopped meat medium with carbohydrates: source boundaries and stale merged formulation

- Review: 20261028T085912Z-chopped-meat-carbohydrates-batch061
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:32:52.215176Z
- Finished UTC: 2026-10-28T08:59:12.223256Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Four major findings concern stale base/child merging, extraction/stock quantities, omitted source supplements and inherited preparation; one minor finding concerns claim-level provenance. Current official sources, all18 concentration fields and existing chemical IDs were assessed. All four canonical checks and pinned MIM integrity passed; unknown percentage/final-mixture bases remain explicit.

## Scope And Provenance

One full generated target and its two maintained contributors;15 quantity decisions cover all18 concentration fields and source-only boundaries.

Selection: Batch061 item10 in Python path order after533 of6325 records were covered by successful native validated lists.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002813 | data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml | generated | chopped_meat_medium_with_carbohydrates |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:002813 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:002813 | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch061/record10/strict.tsv |
| validate-terms | passed | True | CultureMech:002813 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:002813 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| check-mim-label-index | passed | True | CultureMech:002813 | MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9<br>Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350<br>uv run python scripts/check_mim_label_index.py |
| Embedded history and identity registry read | passed | False | CultureMech:002813 | All target/owner events and exact registry rows inspected. RESOLVED_REFERENCE records copying six rows; it does not establish source completeness. No embedded-history validator is claimed. |
| Full-corpus ID/product/merge gates | skipped | False | CultureMech:002813 | No scientific records/schema/generator changed. Full-corpus assign-ids-check, validate-products, verify-merges and audit-merge-freshness were not run; the narrow in-memory pair comparison is not a replacement. |

## Scientific And Domain Assessments

### JCM465 identity and base-medium boundary

identity: concern. Targets: CultureMech:002813.

Exact target and both maintained owners resolve, but the stored merge collapses baseJ461 and supplementedJ465. The J461 synonym and KG match do not prove full formulation equivalence.

Current merger rejects the owners. Same-label reports describe other stable IDs and were not imported as coverage. Native complex/undefined/liquid classification is consistent with the default recipe; no clinical or organism-specific application is inferred.

### Every concentration field and source stage

quantity: concern. Targets: CultureMech:002813.

Six conflict decisions cover all18 local concentration fields; source-only decisions preserve four carbohydrates, cysteine, solvent, makeup and alternatives. No final-medium mass concentration is silently repaired.

{
  "created_at": "2026-10-28T08:41:12.189356Z",
  "target": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
  "scope": "All18 concentration fields in the target and two owners, plus source-only additions and boundaries.",
  "decisions": [
    {
      "decision_id": "Q01",
      "ingredient": "Ground beef",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[0].concentration",
          "value": {
            "value": "487.805",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml",
          "field": "ingredients[0].concentration",
          "value": {
            "value": "487.805",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[0].concentration",
          "value": {
            "value": "487.805",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "table row and preparation boundary; MediaDive $.data.solutions[0].recipe[0]",
      "snippet": "Ground beef (fat free) 500.0 g",
      "explanation": "This is extraction input, after which solids and filtrate are separated and later recombined by a particle/fluid ratio. Neither dissolved beef recovery nor a fixed final mass concentration follows from the input mass.",
      "calculation": "500 / 1.025 = 487.804878... reproduces provider g_l only; 1.025 L is the summed initial liquid input, not the later made-up filtrate or final particle mixture.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q02",
      "ingredient": "NaOH",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[1].concentration",
          "value": {
            "value": "25",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml",
          "field": "ingredients[1].concentration",
          "value": {
            "value": "25",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[1].concentration",
          "value": {
            "value": "25",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "table row and preparation boundary; MediaDive $.data.solutions[0].recipe[2]",
      "snippet": "1 N NaOH 25.0 ml",
      "explanation": "Source specifies volume and strength of a stock used during extraction. The local mass concentration changes both unit and stage. Do not infer residual free NaOH after meat treatment.",
      "calculation": "No conversion from the stock addition to residual final-medium NaOH is supported.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q03",
      "ingredient": "Casitone",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[2].concentration",
          "value": {
            "value": "29.2683",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml",
          "field": "ingredients[2].concentration",
          "value": {
            "value": "29.2683",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[2].concentration",
          "value": {
            "value": "29.2683",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "table row and preparation boundary; MediaDive $.data.solutions[0].recipe[3]",
      "snippet": "Casitone (BD-Difco) 30.0 g",
      "explanation": "Source adds this amount after the filtrate is made up to1.0L. Provider divides by the earlier1025ml extraction input instead; retain the source amount and stage rather than asserting a falsely precise final-mixture concentration.",
      "calculation": "30 g / 1.025 L = 29.26829268 g/L reproduces stored 29.2683; this denominator conflicts with the later1.0L filtrate makeup.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q04",
      "ingredient": "Yeast extract",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[3].concentration",
          "value": {
            "value": "4.87805",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml",
          "field": "ingredients[3].concentration",
          "value": {
            "value": "4.87805",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[3].concentration",
          "value": {
            "value": "4.87805",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "table row and preparation boundary; MediaDive $.data.solutions[0].recipe[4]",
      "snippet": "Yeast extract (BD-Difco) 5.0 g",
      "explanation": "Source adds this amount after the filtrate is made up to1.0L. Provider divides by the earlier1025ml extraction input instead; retain the source amount and stage rather than asserting a falsely precise final-mixture concentration.",
      "calculation": "5 g / 1.025 L = 4.87804878 g/L reproduces stored 4.87805; this denominator conflicts with the later1.0L filtrate makeup.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q05",
      "ingredient": "K2HPO4",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[4].concentration",
          "value": {
            "value": "4.87805",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml",
          "field": "ingredients[4].concentration",
          "value": {
            "value": "4.87805",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[4].concentration",
          "value": {
            "value": "4.87805",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "table row and preparation boundary; MediaDive $.data.solutions[0].recipe[5]",
      "snippet": "K2HPO4 5.0 g",
      "explanation": "Source adds this amount after the filtrate is made up to1.0L. Provider divides by the earlier1025ml extraction input instead; retain the source amount and stage rather than asserting a falsely precise final-mixture concentration.",
      "calculation": "5 g / 1.025 L = 4.87804878 g/L reproduces stored 4.87805; this denominator conflicts with the later1.0L filtrate makeup.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q06",
      "ingredient": "Resazurin",
      "decision": "conflict",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[5].concentration",
          "value": {
            "value": "0.00097561",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml",
          "field": "ingredients[5].concentration",
          "value": {
            "value": "0.00097561",
            "unit": "G_PER_L"
          }
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients[5].concentration",
          "value": {
            "value": "0.00097561",
            "unit": "G_PER_L"
          }
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "table row and preparation boundary; MediaDive $.data.solutions[0].recipe[6]",
      "snippet": "Resazurin 1.0 mg",
      "explanation": "Source adds this amount after the filtrate is made up to1.0L. Provider divides by the earlier1025ml extraction input instead; retain the source amount and stage rather than asserting a falsely precise final-mixture concentration.",
      "calculation": "0.001 g / 1.025 L = 0.0009756097561 g/L reproduces stored 0.00097561; this denominator conflicts with the later1.0L filtrate makeup.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q07",
      "ingredient": "Distilled water",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "first source table",
      "snippet": "Distilled water 1.0 L",
      "explanation": "Extraction solvent and later makeup water; not an additional nutrient. Absence from ingredient edges alone is not an error.",
      "calculation": "None; preserve source stage and unresolved basis.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q08",
      "ingredient": "Made-up filtrate",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "between first and second tables",
      "snippet": "Add water to the filtrate to a final volume of 1.0 L",
      "explanation": "The source explicitly resets the liquid basis before supplements. Distinguish this stage from extraction inputs and the final meat-particle mixture.",
      "calculation": "None; preserve source stage and unresolved basis.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q09",
      "ingredient": "glucose",
      "decision": "add",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465",
      "locator": "sole recipe sentence",
      "snippet": "0.4% glucose",
      "explanation": "The component and literal percentage are present in source prose and the child preparation step but absent from ingredients. Add the component with source evidence; resolve percentage basis before asserting a typed numerical concentration.",
      "calculation": "No conversion to g/L: source does not explicitly identify w/v, w/w or v/v.",
      "proposed": "Preserve literal percentage in evidence/notes; no concentration enum or converted amount proposed."
    },
    {
      "decision_id": "Q10",
      "ingredient": "cellobiose",
      "decision": "add",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465",
      "locator": "sole recipe sentence",
      "snippet": "0.1% cellobiose",
      "explanation": "The component and literal percentage are present in source prose and the child preparation step but absent from ingredients. Add the component with source evidence; resolve percentage basis before asserting a typed numerical concentration.",
      "calculation": "No conversion to g/L: source does not explicitly identify w/v, w/w or v/v.",
      "proposed": "Preserve literal percentage in evidence/notes; no concentration enum or converted amount proposed."
    },
    {
      "decision_id": "Q11",
      "ingredient": "maltose",
      "decision": "add",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465",
      "locator": "sole recipe sentence",
      "snippet": "0.1% maltose",
      "explanation": "The component and literal percentage are present in source prose and the child preparation step but absent from ingredients. Add the component with source evidence; resolve percentage basis before asserting a typed numerical concentration.",
      "calculation": "No conversion to g/L: source does not explicitly identify w/v, w/w or v/v.",
      "proposed": "Preserve literal percentage in evidence/notes; no concentration enum or converted amount proposed."
    },
    {
      "decision_id": "Q12",
      "ingredient": "soluble starch",
      "decision": "add",
      "fields": [
        {
          "path": "data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        },
        {
          "path": "data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml",
          "field": "ingredients (missing source supplement)"
        }
      ],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465",
      "locator": "sole recipe sentence",
      "snippet": "0.1% soluble starch",
      "explanation": "The component and literal percentage are present in source prose and the child preparation step but absent from ingredients. Add the component with source evidence; resolve percentage basis before asserting a typed numerical concentration.",
      "calculation": "No conversion to g/L: source does not explicitly identify w/v, w/w or v/v.",
      "proposed": "Preserve literal percentage in evidence/notes; no concentration enum or converted amount proposed."
    },
    {
      "decision_id": "Q13",
      "ingredient": "L-cysteine hydrochloride monohydrate",
      "decision": "add",
      "fields": [],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "post-makeup preparation",
      "snippet": "0.5 g L-cysteine·HCl·H2O",
      "explanation": "Base-owner prose retains the addition but the six ingredient rows omit it. Child/target do not expose the inherited preparation. Exact supplied form must remain explicit; no substitute ontology identifier is invented.",
      "calculation": "None; preserve source stage and unresolved basis.",
      "proposed": "Add a stage-scoped source amount only after the base preparation is represented."
    },
    {
      "decision_id": "Q14",
      "ingredient": "Agar slant option",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "conditional alternative",
      "snippet": "15 g agar per 1.0 L medium",
      "explanation": "Optional solid variant; do not add agar to the selected liquid default.",
      "calculation": "None; preserve source stage and unresolved basis.",
      "proposed": "No final-medium numerical value certified."
    },
    {
      "decision_id": "Q15",
      "ingredient": "Commercial cooked-meat alternative",
      "decision": "evidence_only",
      "fields": [],
      "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461",
      "locator": "commercial alternative supplements",
      "snippet": "5 g/L yeast extract",
      "explanation": "Commercial products are an alternative to the extraction route. The source lists four separate supplements; do not blend that route into the default extraction formulation.",
      "calculation": "Commercial route: yeast extract5g/L, phosphate5g/L, resazurin1mg/L, cysteine hydrochloride monohydrate0.5g/L are explicit alternative-route facts, not support for the copied default amounts.",
      "proposed": "Keep a separate alternative and product/version boundary; no inferred proprietary composition."
    }
  ],
  "local_concentration_field_count": 18,
  "decision_count": 15,
  "conditions": {
    "source_base_ph": 7.0,
    "target_and_child_ph": "absent",
    "scope": "Preparation pH, not a growth optimum.",
    "base_preparation": "Full source and owner prose assessed; boiling15min, dispensing7ml and particle:fluid1:4–5, nitrogen atmosphere, stopper and121C30min are preparation context. Default page-wide121C15min does not override the specific recipe. No incubation/growth temperature inferred."
  }
}

### Reachable base preparation and supplied forms

completeness: concern. Targets: CultureMech:002813.

The child/target retain only the carbohydrate sentence and lack a structured parent/base link. The base has the full source prose but misclassifies coarse filtering as FILTER_STERILIZE; the source separates boiling, filtration and later autoclaving.

Preserve the source extraction and supplementation stages, preparation pH and conditional agar/commercial branches. No incubation temperature, tested organism or growth assertion is supplied by these source pages.

### Existing exact chemical IDs and packaged MIM decisions

grounding: supported. Targets: CultureMech:002813.

All18 asserted chemical slots resolve to three active ChEBI IDs with matching labels; source wording supports the three named chemical identities. Pinned MIM answers all six input labels.

MIM also returns FOODON/MICRO identifiers for three undefined mixtures; these are snapshot diagnostics, not new reviewed ontology assignments. A source normality is a stock-strength qualifier, not a different sodium-hydroxide identity. The source does not specify a sodium resazurin salt; no counterion is added. Native chemistry term validation does not certify these IDs, so the external objects were inspected separately.

### Source provenance, historical findings and claim placement

evidence: concern. Targets: CultureMech:002813.

Official JCM and MediaDive access succeeds. Target and owners have source links in notes but no claim-level evidence or bibliography; native reference validation performs zero checks.

Five exact-target/owner reports were read fully. Eighteen same-label candidate reports were retained as metadata comparisons only; their scientific contents do not support this verdict. Old source-access timestamps remain historical; current API bytes match their stored source digests. No structured issue is closed.

### Required native validators and declared scope

schema: supported. Targets: CultureMech:002813.

All four canonical checks and the MIM integrity check passed. All target YAML bytes and both owner records were read.

No organism, strain, gene, protein or transcriptomic assertion exists in the selected target and two owners; iModulonDB is not applicable. No universal negative literature claim or experimental growth claim is made.

## Findings

### F1: Stored merge equates the supplemented medium with its base

major / open / confirmed; issue key: cm002813-base-supplemented-merge-collapse.

The source defines JCM465 as a derivative of JCM461. Copied base-only ingredients collapse their ingredient fingerprint, creating a misleading synonym and J461 KG match. Current formulation-aware merging rejects the pair, so the stored product remains stale.

### F2: Copied extraction quantities use an unsupported final-medium basis

major / open / confirmed; issue key: cm002813-extraction-denominator-stock-unit.

All six direct amounts in the target and owners have a stage/unit conflict. Five reproduce division by the initial1025ml liquid inputs even though the source later makes the filtrate to1L; NaOH changes a volume of1N stock to a mass concentration. Meat extraction recovery and the final particle mixture prevent simplistic final-medium replacement values.

### F3: Source additions remain absent from structured formulation

major / open / confirmed; issue key: cm002813-source-supplements-missing.

JCM465 carbohydrate additions survive only in prose, while inherited cysteine is present only in base preparation. Copying six base rows did not resolve the whole formulation. Literal carbohydrate percentages have no explicit basis and must not be converted by assumption.

### F4: Inherited preparation cannot be followed through the child record

major / open / confirmed; issue key: cm002813-base-preparation-boundary.

The target and child have no structured parent link exposing the base extraction/preparation. The maintained base prose is present, but FILTER_STERILIZE labels coarse meat filtration as a sterile filtration step. Source-specific treatment and alternatives require distinct representation.

### F5: Source links lack claim-level evidence and bibliography

minor / open / confirmed; issue key: cm002813-claim-provenance-gap.

The notes URLs resolve but no structured formulation evidence or reference entry is attached. The reference validator therefore checks zero references. Preserve both source identities and exact claim stages when adding evidence.

## Recommended Actions And Acceptance Checks

### A1

Curate the two maintained owners from exact JCM source boundaries: retain the base extraction and stock identities, restore source-specific component representation, and preserve unsupported final concentrations and percentage bases as unresolved. Append an actual curation event only when edits occur.

- Reconcile all18 existing amount fields against the15 retained decisions; no1025ml denominator reused after filtrate makeup and no mass unit substituted for a stock volume.
- Keep carbohydrate percentages literal until basis is established; do not blend agar or commercial alternatives into the liquid default.
- Coarse filtration must not be labeled sterile filtration; inherited base preparation and exact chemical forms must be reachable.
- Attach narrow exact-source evidence and bibliography, then run the four native validators for each edited owner.

### A2

After maintained source curation, regenerate with the current formulation-aware merge path and reassess the J461 KG association without treating ingredient identity alone as recipe identity.

- BaseJ461 and supplementedJ465 remain distinct; generated identity, synonyms and source accessions follow the represented formulation.
- Generated source claims and newly attached evidence are retained; no direct generated-YAML patch.
- Run just verify-merges and just audit-merge-freshness plus applicable product gates after the separately authorized change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml; entire file | supports | Complete YAML read: all ingredients, quantities, identifiers, preparation, provenance and history. |
| base-owner | data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml; entire file | supports | Complete YAML read: all ingredients, quantities, identifiers, preparation, provenance and history. |
| child-owner | data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml; entire file | supports | Complete YAML read: all ingredients, quantities, identifiers, preparation, provenance and history. |
| jcm465 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465; complete source response | supports | Official JCM465 identifies a carbohydrate-supplemented derivative of JCM461; no organism or growth experiment is claimed. |
| jcm461 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461; complete source response | supports | Official JCM461 distinguishes extraction inputs, made-up filtrate, supplements, dispensing, and alternative solid/commercial routes. |
| api461 | https://mediadive.dsmz.de/rest/medium/J461; complete source response | supports | Full current MediaDive source object read, including every recipe row, metadata and preparation step; provider projections are assessed against JCM. |
| api465 | https://mediadive.dsmz.de/rest/medium/J465; complete source response | supports | Full current MediaDive source object read, including every recipe row, metadata and preparation step; provider projections are assessed against JCM. |
| ols32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; complete source response | supports | Exact active ChEBI object read: canonical ID, label, formula, charge and description. Existing name/ID pairing is supported; this is not amount evidence. |
| ols131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; complete source response | supports | Exact active ChEBI object read: canonical ID, label, formula, charge and description. Existing name/ID pairing is supported; this is not amount evidence. |
| ols8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; complete source response | supports | Exact active ChEBI object read: canonical ID, label, formula, charge and description. Existing name/ID pairing is supported; this is not amount evidence. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; entire file | supports | Exact six label decisions and all42 selected rows inspected; packaged publication identity may use FOODON/MICRO for mixtures. No missing CHEBI is invented. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; entire file | supports | Full pinned source commit/hash/count metadata verified. |
| importer | src/culturemech/import/mediadive_importer.py; entire file | supports | Conversion, composition, stock detection, unit mapping and preparation classifier read. Current parser recognizes percentage stocks but does not recognize a normality-only attribute as a stock; it skips water and trusts provider g_l. Raw-import historical causality remains bounded. |
| merge-formulation | src/culturemech/merge/formulation.py; entire file | supports | Full current content projection and evidence merger read; unequal formulations are rejected. |
| merger | src/culturemech/merge/merger.py; entire file | supports | merge_group and canonical selection read; current merger rejects the two exact owners. |
| kg-writer | scripts/enrich_with_kg_microbe_matches.py; entire file | supports | Writer invokes ingredient matching and persists the returned medium ID; no fresh external KG graph was loaded. |
| registry | data/culturemech_id_registry.tsv; entire file | supports | Exact CM002810 and CM002813 rows resolve the two maintained owners. |
| project-recipes | project.justfile; entire file | supports | Actual focused schema, strict, term and reference recipes inspected; chemistry slots are not bound in the term gate. |
| diagnostics | REVIEW_WORK/batch061/record10/diagnostics.json; entire file | supports | All18 local concentration fields,25 external identifier slots, registry rows, MIM decisions and current merger result inventoried. Same-label historical reports have explicitly bounded metadata-only scope. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml.md; entire file | supports | Entire exact-target/owner historical report read. Derivative evidence only; October7 source digests match fresh responses and the unresolved extraction-denominator conflict remains. |
| history2 | reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml.md; entire file | supports | Entire exact-target/owner historical report read. Derivative evidence only; October7 source digests match fresh responses and the unresolved extraction-denominator conflict remains. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.md; entire file | supports | Entire exact-target/owner historical report read. Derivative evidence only; October7 source digests match fresh responses and the unresolved extraction-denominator conflict remains. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.md; entire file | supports | Entire exact-target/owner historical report read. Derivative evidence only; October7 source digests match fresh responses and the unresolved extraction-denominator conflict remains. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.md; entire file | supports | Entire exact-target/owner historical report read. Derivative evidence only; October7 source digests match fresh responses and the unresolved extraction-denominator conflict remains. |
| quantity-inventory | REVIEW_WORK/batch061/record10/quantity-inventory.json; entire file | supports | Fifteen scoped decisions cover every local concentration field plus missing additions, water, makeup and alternate routes; arithmetic is separate from source text. |
| validate-schema | REVIEW_WORK/batch061/record10/validate-schema-result.json; entire file | supports | Actual complete command/result and stdout/stderr read. |
| validate-strict | REVIEW_WORK/batch061/record10/validate-strict-result.json; entire file | supports | Actual complete command/result and stdout/stderr read. |
| validate-terms | REVIEW_WORK/batch061/record10/validate-terms-result.json; entire file | supports | Actual complete command/result and stdout/stderr read. |
| validate-references | REVIEW_WORK/batch061/record10/validate-references-result.json; entire file | supports | Actual complete command/result and stdout/stderr read. |
| check-mim-label-index | REVIEW_WORK/batch061/record10/check-mim-label-index-result.json; entire file | supports | Actual complete command/result and stdout/stderr read. |

## Limits And Additional Notes

- No final particle-mixture concentration or percent basis is inferred where source text does not supply it. Known extraction and makeup stages are retained without inventing recovery, density or volume additivity.
- The attempted MDP=1 URLs returned the same HTML, not PDF; actual HTML and REST responses support this review. Initial /api endpoints404 were preserved before correct /rest endpoint captures succeeded.
- The original raw-import captures at three exact documented paths are unavailable in this isolated checkout (lexists check includes ignored paths). This is not a claim that they are absent elsewhere; historical causality is inferred only where current bytes and writer behavior support it.
- Four canonical checks apply to the selected target; contributors were read as context. Full-corpus gates, fresh external KG graph matching and experimental growth validation were not performed.
- Same-label candidate-report contents were not adopted as evidence or coverage. No previous structured finding is retired, no record history is changed and no scientific status is promoted.
- Private quantity inventory preserves source amount/unit/stage decisions and hashes; generated data and maintained records were not edited.
- Current merger safeguard and already-preserved base prose are credited; remaining issues describe the stored scientific record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T085912Z-chopped-meat-carbohydrates-batch061
kind: record
repository: CultureBotAI/CultureMech
title: 'Chopped meat medium with carbohydrates: source boundaries and stale merged
  formulation'
started_at: '2026-10-28T08:32:52.215176Z'
finished_at: '2026-10-28T08:59:12.223256Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify target or maintained scientific
    inputs; source-grounded review without experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Four major findings concern stale base/child merging, extraction/stock quantities,
  omitted source supplements and inherited preparation; one minor finding concerns
  claim-level provenance. Current official sources, all18 concentration fields and
  existing chemical IDs were assessed. All four canonical checks and pinned MIM integrity
  passed; unknown percentage/final-mixture bases remain explicit.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    sha256: 36c33c91f4ea5ab46233e1877205b805fa48a23ec55e86428cbd474915cbc0ea
    role: target
  - path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    sha256: e5d3f434e82f13c393a2ede599500ce704aa96e10a4664c0eee04a5b24efc270
    role: context
  - path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    sha256: ffb0ccecbe5b7d1e43b42901c2bede7b7ea2d89da65032070af88959eddf2869
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml.md
    sha256: d23194a24a2f51e851b1b645bdafce76fed0bd65c86913228f79338481857f36
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml.md
    sha256: e62546330dba1eced27fcbaab6070feac639dc4ff9338496417e757860672459
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.md
    sha256: 95f558b38cb7bf26c219eefdba448f049af01c9c4ef1e01d942da206ff54b77e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__05390fed.md
    sha256: 3c8b774a16b5300cf7c5a464ddea6ed599f962482cbc0eaed0e38a32fc5f0de0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__1c531ecc.md
    sha256: 3ff6dfe1fd7d6366e9a36e674cb9735bdb45dd54699273e16498341cd9a19c73
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__284e9255.md
    sha256: 320bda1d561566c6c53efd59c3fbcdf2c50b21d8187636c7d736d8798a95a377
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__89660db2.md
    sha256: 2df23704d3b1bfcc636872a4631a4126520e47bc49fc10f4fc69ce3898cd765d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.md
    sha256: ea8cdfcebb52ea636070bfb85ab42cbe94fd9680b7aec90bf832517088f3d2ea
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.md
    sha256: 4abde072df4ed99dee2a984b144f7342e6082580450eee169022cc412b048555
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__a7fbb591.md
    sha256: d33eaa2f133581b6131a1c205a8c8f8125d2ca48b47deb71aad60655a85a513c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__aa0ad6dd.md
    sha256: b8fe8983c239c49ec3e581f89764e6b04b8ccc66502b6e527f9f8de3acc139c5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__f2dd06fe.md
    sha256: ccb07235ac7d58989d64edbce1f0037a88e2e28e282dc08880d0554809de2c1c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.md
    sha256: 3c3048517120a395ce80647989777b3e22b87d6d3307d200278b67e85990826a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.md
    sha256: ce58c478536e19b7f3bf6956ec9a119f1c71a961af004b7cd936519032d54f92
    role: context
  - path: reports/yaml_record_review/20260922T082516Z-chopped_meat_medium_with_carbohydrates__05390fed.md
    sha256: ac7259a0e8603b4934da119b0932d92e8f3334cb5985d3f65cc1e022786f599d
    role: context
  - path: reports/yaml_record_review/20260922T082729Z-chopped_meat_medium_with_carbohydrates__1c531ecc.md
    sha256: 787ec4246c57598fcdb78351db13c04f5f961e96c1de5d251669ef54b1a4720d
    role: context
  - path: reports/yaml_record_review/20260922T083237Z-chopped_meat_medium_with_carbohydrates__284e9255.md
    sha256: ce396551a2a597519d1ebea9f77c8a02d136f66a74f12a531e4012fb6ab49cc3
    role: context
  - path: reports/yaml_record_review/20260922T083630Z-chopped_meat_medium_with_carbohydrates__89660db2.md
    sha256: d859ab9e5e32485589e3eaa56842d38c2f6294707af5c4ea6730b4fd01cf51d9
    role: context
  - path: reports/yaml_record_review/20260922T083900Z-chopped_meat_medium_with_carbohydrates__8ad0d89d.md
    sha256: e55d7a91c295335d104aa72d082aeea107a0260806e0e830e0595bc6f1003663
    role: context
  - path: reports/yaml_record_review/20260922T084110Z-chopped_meat_medium_with_carbohydrates__960dd33a.md
    sha256: e733223bf8e810827fb2d26638e9230969fec9ee79734f6a6024d3773a6667f3
    role: context
  - path: reports/yaml_record_review/20260922T084340Z-chopped_meat_medium_with_carbohydrates__a7fbb591.md
    sha256: 5728f02a42708bb4b76fbe7d6d0791a59ada696a07297ac1a9c158c9f726097c
    role: context
  - path: reports/yaml_record_review/20260922T084556Z-chopped_meat_medium_with_carbohydrates__aa0ad6dd.md
    sha256: f366105025e3729f0518e4d196483e79b789ffaab3ded24b2765884d5d13ef14
    role: context
  - path: reports/yaml_record_review/20260922T084832Z-chopped_meat_medium_with_carbohydrates__f2dd06fe.md
    sha256: dc3210fe8c2f6a6c283d95b5f11c49a1ada4996e9331b8aa01df4123f8fdb784
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One full generated target and its two maintained contributors;15 quantity
    decisions cover all18 concentration fields and source-only boundaries.
  selection: Batch061 item10 in Python path order after533 of6325 records were covered
    by successful native validated lists.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002813
  exclusions:
  - target: Other same-label records and historical same-label scientific claims
    reason: Only selected exact target and two source owners are assessed;18 candidate
      reports were screened by metadata only.
  - target: New growth assertions, experimental execution and proprietary commercial
      formulations
    reason: Official recipe sources do not establish tested strains or authorize optimization.
targets:
- target_id: CultureMech:002813
  path: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
  label: chopped_meat_medium_with_carbohydrates
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:002813
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    --workers 1 --out REVIEW_WORK/batch061/record10/strict.tsv
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:002813
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch061/record10/strict.tsv"
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:002813
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:002813
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  evidence_ids:
  - validate-references
- check_id: check-mim-label-index
  name: check-mim-label-index
  command: just check-mim-label-index
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:002813
  summary: 'MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9

    Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350

    uv run python scripts/check_mim_label_index.py'
  evidence_ids:
  - check-mim-label-index
- check_id: embedded-history
  name: Embedded history and identity registry read
  status: passed
  required: false
  target_ids:
  - CultureMech:002813
  summary: All target/owner events and exact registry rows inspected. RESOLVED_REFERENCE
    records copying six rows; it does not establish source completeness. No embedded-history
    validator is claimed.
  evidence_ids:
  - target
  - base-owner
  - child-owner
  - registry
- check_id: corpus-gates
  name: Full-corpus ID/product/merge gates
  status: skipped
  required: false
  target_ids:
  - CultureMech:002813
  summary: No scientific records/schema/generator changed. Full-corpus assign-ids-check,
    validate-products, verify-merges and audit-merge-freshness were not run; the narrow
    in-memory pair comparison is not a replacement.
  evidence_ids:
  - project-recipes
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263110Z'
  support: supports
  summary: 'Complete YAML read: all ingredients, quantities, identifiers, preparation,
    provenance and history.'
  snapshot_sha256: 36c33c91f4ea5ab46233e1877205b805fa48a23ec55e86428cbd474915cbc0ea
- evidence_id: base-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263117Z'
  support: supports
  summary: 'Complete YAML read: all ingredients, quantities, identifiers, preparation,
    provenance and history.'
  snapshot_sha256: e5d3f434e82f13c393a2ede599500ce704aa96e10a4664c0eee04a5b24efc270
- evidence_id: child-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263119Z'
  support: supports
  summary: 'Complete YAML read: all ingredients, quantities, identifiers, preparation,
    provenance and history.'
  snapshot_sha256: ffb0ccecbe5b7d1e43b42901c2bede7b7ea2d89da65032070af88959eddf2869
- evidence_id: jcm465
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465
  locator: complete source response
  accessed_at: '2026-10-28T08:33:19.224335Z'
  support: supports
  summary: Official JCM465 identifies a carbohydrate-supplemented derivative of JCM461;
    no organism or growth experiment is claimed.
  snapshot_sha256: 0dfaee8e2e44b3e6d0c1ee11b05fc19500f4908e0fa7a5f38a4db580de0c9bd1
- evidence_id: jcm461
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461
  locator: complete source response
  accessed_at: '2026-10-28T08:33:19.224365Z'
  support: supports
  summary: Official JCM461 distinguishes extraction inputs, made-up filtrate, supplements,
    dispensing, and alternative solid/commercial routes.
  snapshot_sha256: ec75d8b21488c8b4996ea5a6dc45e9f1a40a56cd484edac3b11991aa58bebfe1
- evidence_id: api461
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J461
  locator: complete source response
  accessed_at: '2026-10-28T08:34:26.996986Z'
  support: supports
  summary: Full current MediaDive source object read, including every recipe row,
    metadata and preparation step; provider projections are assessed against JCM.
  snapshot_sha256: bf59d4ab53a55a09dee2f3401fcb0fd5f3aec2549d11d9325beb1f6330bb50ba
- evidence_id: api465
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J465
  locator: complete source response
  accessed_at: '2026-10-28T08:34:26.989244Z'
  support: supports
  summary: Full current MediaDive source object read, including every recipe row,
    metadata and preparation step; provider projections are assessed against JCM.
  snapshot_sha256: 45907a66dd2144472795e8298857a58b403ad64e7bba850b3cec0633fbcbc172
- evidence_id: ols32145
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: complete source response
  accessed_at: '2026-10-28T08:33:20.013293Z'
  support: supports
  summary: 'Exact active ChEBI object read: canonical ID, label, formula, charge and
    description. Existing name/ID pairing is supported; this is not amount evidence.'
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: ols131527
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: complete source response
  accessed_at: '2026-10-28T08:33:20.259243Z'
  support: supports
  summary: 'Exact active ChEBI object read: canonical ID, label, formula, charge and
    description. Existing name/ID pairing is supported; this is not amount evidence.'
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: ols8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: complete source response
  accessed_at: '2026-10-28T08:33:20.396890Z'
  support: supports
  summary: 'Exact active ChEBI object read: canonical ID, label, formula, charge and
    description. Existing name/ID pairing is supported; this is not amount evidence.'
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263124Z'
  support: supports
  summary: Exact six label decisions and all42 selected rows inspected; packaged publication
    identity may use FOODON/MICRO for mixtures. No missing CHEBI is invented.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-metadata
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263125Z'
  support: supports
  summary: Full pinned source commit/hash/count metadata verified.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263126Z'
  support: supports
  summary: Conversion, composition, stock detection, unit mapping and preparation
    classifier read. Current parser recognizes percentage stocks but does not recognize
    a normality-only attribute as a stock; it skips water and trusts provider g_l.
    Raw-import historical causality remains bounded.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: merge-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263127Z'
  support: supports
  summary: Full current content projection and evidence merger read; unequal formulations
    are rejected.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263128Z'
  support: supports
  summary: merge_group and canonical selection read; current merger rejects the two
    exact owners.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: kg-writer
  kind: record_content
  reference: scripts/enrich_with_kg_microbe_matches.py
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263129Z'
  support: supports
  summary: Writer invokes ingredient matching and persists the returned medium ID;
    no fresh external KG graph was loaded.
  snapshot_sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
- evidence_id: registry
  kind: record_content
  reference: data/culturemech_id_registry.tsv
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263129Z'
  support: supports
  summary: Exact CM002810 and CM002813 rows resolve the two maintained owners.
  snapshot_sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
- evidence_id: project-recipes
  kind: record_content
  reference: project.justfile
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263130Z'
  support: supports
  summary: Actual focused schema, strict, term and reference recipes inspected; chemistry
    slots are not bound in the term gate.
  snapshot_sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
- evidence_id: diagnostics
  kind: record_content
  reference: REVIEW_WORK/batch061/record10/diagnostics.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263131Z'
  support: supports
  summary: All18 local concentration fields,25 external identifier slots, registry
    rows, MIM decisions and current merger result inventoried. Same-label historical
    reports have explicitly bounded metadata-only scope.
  snapshot_sha256: f345439283c95ece3a9cbbc2cc763112522bb2705cda8c40408f8c92403910b7
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml.md
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263132Z'
  support: supports
  summary: Entire exact-target/owner historical report read. Derivative evidence only;
    October7 source digests match fresh responses and the unresolved extraction-denominator
    conflict remains.
  snapshot_sha256: d23194a24a2f51e851b1b645bdafce76fed0bd65c86913228f79338481857f36
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2000-2500/records/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml.md
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263133Z'
  support: supports
  summary: Entire exact-target/owner historical report read. Derivative evidence only;
    October7 source digests match fresh responses and the unresolved extraction-denominator
    conflict remains.
  snapshot_sha256: e62546330dba1eced27fcbaab6070feac639dc4ff9338496417e757860672459
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.md
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263134Z'
  support: supports
  summary: Entire exact-target/owner historical report read. Derivative evidence only;
    October7 source digests match fresh responses and the unresolved extraction-denominator
    conflict remains.
  snapshot_sha256: ce58c478536e19b7f3bf6956ec9a119f1c71a961af004b7cd936519032d54f92
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.md
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263135Z'
  support: supports
  summary: Entire exact-target/owner historical report read. Derivative evidence only;
    October7 source digests match fresh responses and the unresolved extraction-denominator
    conflict remains.
  snapshot_sha256: 3c3048517120a395ce80647989777b3e22b87d6d3307d200278b67e85990826a
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.md
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263135Z'
  support: supports
  summary: Entire exact-target/owner historical report read. Derivative evidence only;
    October7 source digests match fresh responses and the unresolved extraction-denominator
    conflict remains.
  snapshot_sha256: 95f558b38cb7bf26c219eefdba448f049af01c9c4ef1e01d942da206ff54b77e
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch061/record10/quantity-inventory.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263136Z'
  support: supports
  summary: Fifteen scoped decisions cover every local concentration field plus missing
    additions, water, makeup and alternate routes; arithmetic is separate from source
    text.
  snapshot_sha256: e40bd1b0a327c1737c380c1c620e408782ac0955643638f606bf19496247c062
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record10/validate-schema-result.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263137Z'
  support: supports
  summary: Actual complete command/result and stdout/stderr read.
  snapshot_sha256: aac48837038f5315e93be10f908103d2848681976909ba81f3c97e998b771faa
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record10/validate-strict-result.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263138Z'
  support: supports
  summary: Actual complete command/result and stdout/stderr read.
  snapshot_sha256: ab2374a9a0a00e112292b3fac2b459691709587d9f37ae79909fd7b1ba68eb89
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record10/validate-terms-result.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263139Z'
  support: supports
  summary: Actual complete command/result and stdout/stderr read.
  snapshot_sha256: 9aa992e427aa42674cec9d073b376cb2639eb3ade21a0d096c488d83d3c288d4
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch061/record10/validate-references-result.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263140Z'
  support: supports
  summary: Actual complete command/result and stdout/stderr read.
  snapshot_sha256: f64d19d44654f84dd7dbaf279521cdb7182ed079fffb2627570a2ba39293b668
- evidence_id: check-mim-label-index
  kind: validation
  reference: REVIEW_WORK/batch061/record10/check-mim-label-index-result.json
  locator: entire file
  accessed_at: '2026-10-28T08:41:59.263141Z'
  support: supports
  summary: Actual complete command/result and stdout/stderr read.
  snapshot_sha256: a9ff7377dedf30e6a746c446177dbaba49347e01f01e1c01a208341d38b39221
assessments:
- assessment_id: identity
  area: identity
  topic: JCM465 identity and base-medium boundary
  outcome: concern
  summary: Exact target and both maintained owners resolve, but the stored merge collapses
    baseJ461 and supplementedJ465. The J461 synonym and KG match do not prove full
    formulation equivalence.
  target_ids:
  - CultureMech:002813
  evidence_ids:
  - target
  - base-owner
  - child-owner
  - jcm465
  - api465
  - api461
  - diagnostics
  details: Current merger rejects the owners. Same-label reports describe other stable
    IDs and were not imported as coverage. Native complex/undefined/liquid classification
    is consistent with the default recipe; no clinical or organism-specific application
    is inferred.
- assessment_id: quantity
  area: quantity
  topic: Every concentration field and source stage
  outcome: concern
  summary: Six conflict decisions cover all18 local concentration fields; source-only
    decisions preserve four carbohydrates, cysteine, solvent, makeup and alternatives.
    No final-medium mass concentration is silently repaired.
  target_ids:
  - CultureMech:002813
  evidence_ids:
  - quantity-inventory
  - jcm461
  - jcm465
  - api461
  - api465
  details: "{\n  \"created_at\": \"2026-10-28T08:41:12.189356Z\",\n  \"target\": \"\
    data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\",\n  \"scope\"\
    : \"All18 concentration fields in the target and two owners, plus source-only\
    \ additions and boundaries.\",\n  \"decisions\": [\n    {\n      \"decision_id\"\
    : \"Q01\",\n      \"ingredient\": \"Ground beef\",\n      \"decision\": \"conflict\"\
    ,\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[0].concentration\",\n          \"value\"\
    : {\n            \"value\": \"487.805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[0].concentration\",\n          \"value\"\
    : {\n            \"value\": \"487.805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[0].concentration\",\n          \"value\"\
    : {\n            \"value\": \"487.805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"table row and preparation boundary; MediaDive $.data.solutions[0].recipe[0]\"\
    ,\n      \"snippet\": \"Ground beef (fat free) 500.0 g\",\n      \"explanation\"\
    : \"This is extraction input, after which solids and filtrate are separated and\
    \ later recombined by a particle/fluid ratio. Neither dissolved beef recovery\
    \ nor a fixed final mass concentration follows from the input mass.\",\n     \
    \ \"calculation\": \"500 / 1.025 = 487.804878... reproduces provider g_l only;\
    \ 1.025 L is the summed initial liquid input, not the later made-up filtrate or\
    \ final particle mixture.\",\n      \"proposed\": \"No final-medium numerical\
    \ value certified.\"\n    },\n    {\n      \"decision_id\": \"Q02\",\n      \"\
    ingredient\": \"NaOH\",\n      \"decision\": \"conflict\",\n      \"fields\":\
    \ [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[1].concentration\",\n          \"value\"\
    : {\n            \"value\": \"25\",\n            \"unit\": \"G_PER_L\"\n     \
    \     }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[1].concentration\",\n          \"value\"\
    : {\n            \"value\": \"25\",\n            \"unit\": \"G_PER_L\"\n     \
    \     }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[1].concentration\",\n          \"value\"\
    : {\n            \"value\": \"25\",\n            \"unit\": \"G_PER_L\"\n     \
    \     }\n        }\n      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"table row and preparation boundary; MediaDive $.data.solutions[0].recipe[2]\"\
    ,\n      \"snippet\": \"1 N NaOH 25.0 ml\",\n      \"explanation\": \"Source specifies\
    \ volume and strength of a stock used during extraction. The local mass concentration\
    \ changes both unit and stage. Do not infer residual free NaOH after meat treatment.\"\
    ,\n      \"calculation\": \"No conversion from the stock addition to residual\
    \ final-medium NaOH is supported.\",\n      \"proposed\": \"No final-medium numerical\
    \ value certified.\"\n    },\n    {\n      \"decision_id\": \"Q03\",\n      \"\
    ingredient\": \"Casitone\",\n      \"decision\": \"conflict\",\n      \"fields\"\
    : [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[2].concentration\",\n          \"value\"\
    : {\n            \"value\": \"29.2683\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[2].concentration\",\n          \"value\"\
    : {\n            \"value\": \"29.2683\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[2].concentration\",\n          \"value\"\
    : {\n            \"value\": \"29.2683\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"table row and preparation boundary; MediaDive $.data.solutions[0].recipe[3]\"\
    ,\n      \"snippet\": \"Casitone (BD-Difco) 30.0 g\",\n      \"explanation\":\
    \ \"Source adds this amount after the filtrate is made up to1.0L. Provider divides\
    \ by the earlier1025ml extraction input instead; retain the source amount and\
    \ stage rather than asserting a falsely precise final-mixture concentration.\"\
    ,\n      \"calculation\": \"30 g / 1.025 L = 29.26829268 g/L reproduces stored\
    \ 29.2683; this denominator conflicts with the later1.0L filtrate makeup.\",\n\
    \      \"proposed\": \"No final-medium numerical value certified.\"\n    },\n\
    \    {\n      \"decision_id\": \"Q04\",\n      \"ingredient\": \"Yeast extract\"\
    ,\n      \"decision\": \"conflict\",\n      \"fields\": [\n        {\n       \
    \   \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[3].concentration\",\n          \"value\"\
    : {\n            \"value\": \"4.87805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[3].concentration\",\n          \"value\"\
    : {\n            \"value\": \"4.87805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[3].concentration\",\n          \"value\"\
    : {\n            \"value\": \"4.87805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"table row and preparation boundary; MediaDive $.data.solutions[0].recipe[4]\"\
    ,\n      \"snippet\": \"Yeast extract (BD-Difco) 5.0 g\",\n      \"explanation\"\
    : \"Source adds this amount after the filtrate is made up to1.0L. Provider divides\
    \ by the earlier1025ml extraction input instead; retain the source amount and\
    \ stage rather than asserting a falsely precise final-mixture concentration.\"\
    ,\n      \"calculation\": \"5 g / 1.025 L = 4.87804878 g/L reproduces stored 4.87805;\
    \ this denominator conflicts with the later1.0L filtrate makeup.\",\n      \"\
    proposed\": \"No final-medium numerical value certified.\"\n    },\n    {\n  \
    \    \"decision_id\": \"Q05\",\n      \"ingredient\": \"K2HPO4\",\n      \"decision\"\
    : \"conflict\",\n      \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[4].concentration\",\n          \"value\"\
    : {\n            \"value\": \"4.87805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[4].concentration\",\n          \"value\"\
    : {\n            \"value\": \"4.87805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[4].concentration\",\n          \"value\"\
    : {\n            \"value\": \"4.87805\",\n            \"unit\": \"G_PER_L\"\n\
    \          }\n        }\n      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"table row and preparation boundary; MediaDive $.data.solutions[0].recipe[5]\"\
    ,\n      \"snippet\": \"K2HPO4 5.0 g\",\n      \"explanation\": \"Source adds\
    \ this amount after the filtrate is made up to1.0L. Provider divides by the earlier1025ml\
    \ extraction input instead; retain the source amount and stage rather than asserting\
    \ a falsely precise final-mixture concentration.\",\n      \"calculation\": \"\
    5 g / 1.025 L = 4.87804878 g/L reproduces stored 4.87805; this denominator conflicts\
    \ with the later1.0L filtrate makeup.\",\n      \"proposed\": \"No final-medium\
    \ numerical value certified.\"\n    },\n    {\n      \"decision_id\": \"Q06\"\
    ,\n      \"ingredient\": \"Resazurin\",\n      \"decision\": \"conflict\",\n \
    \     \"fields\": [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[5].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.00097561\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml\"\
    ,\n          \"field\": \"ingredients[5].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.00097561\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        },\n        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients[5].concentration\",\n          \"value\"\
    : {\n            \"value\": \"0.00097561\",\n            \"unit\": \"G_PER_L\"\
    \n          }\n        }\n      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"table row and preparation boundary; MediaDive $.data.solutions[0].recipe[6]\"\
    ,\n      \"snippet\": \"Resazurin 1.0 mg\",\n      \"explanation\": \"Source adds\
    \ this amount after the filtrate is made up to1.0L. Provider divides by the earlier1025ml\
    \ extraction input instead; retain the source amount and stage rather than asserting\
    \ a falsely precise final-mixture concentration.\",\n      \"calculation\": \"\
    0.001 g / 1.025 L = 0.0009756097561 g/L reproduces stored 0.00097561; this denominator\
    \ conflicts with the later1.0L filtrate makeup.\",\n      \"proposed\": \"No final-medium\
    \ numerical value certified.\"\n    },\n    {\n      \"decision_id\": \"Q07\"\
    ,\n      \"ingredient\": \"Distilled water\",\n      \"decision\": \"evidence_only\"\
    ,\n      \"fields\": [],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"first source table\",\n      \"snippet\": \"Distilled\
    \ water 1.0 L\",\n      \"explanation\": \"Extraction solvent and later makeup\
    \ water; not an additional nutrient. Absence from ingredient edges alone is not\
    \ an error.\",\n      \"calculation\": \"None; preserve source stage and unresolved\
    \ basis.\",\n      \"proposed\": \"No final-medium numerical value certified.\"\
    \n    },\n    {\n      \"decision_id\": \"Q08\",\n      \"ingredient\": \"Made-up\
    \ filtrate\",\n      \"decision\": \"evidence_only\",\n      \"fields\": [],\n\
    \      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"between first and second tables\",\n      \"snippet\"\
    : \"Add water to the filtrate to a final volume of 1.0 L\",\n      \"explanation\"\
    : \"The source explicitly resets the liquid basis before supplements. Distinguish\
    \ this stage from extraction inputs and the final meat-particle mixture.\",\n\
    \      \"calculation\": \"None; preserve source stage and unresolved basis.\"\
    ,\n      \"proposed\": \"No final-medium numerical value certified.\"\n    },\n\
    \    {\n      \"decision_id\": \"Q09\",\n      \"ingredient\": \"glucose\",\n\
    \      \"decision\": \"add\",\n      \"fields\": [\n        {\n          \"path\"\
    : \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\",\n  \
    \        \"field\": \"ingredients (missing source supplement)\"\n        },\n\
    \        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        }\n\
    \      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465\"\
    ,\n      \"locator\": \"sole recipe sentence\",\n      \"snippet\": \"0.4% glucose\"\
    ,\n      \"explanation\": \"The component and literal percentage are present in\
    \ source prose and the child preparation step but absent from ingredients. Add\
    \ the component with source evidence; resolve percentage basis before asserting\
    \ a typed numerical concentration.\",\n      \"calculation\": \"No conversion\
    \ to g/L: source does not explicitly identify w/v, w/w or v/v.\",\n      \"proposed\"\
    : \"Preserve literal percentage in evidence/notes; no concentration enum or converted\
    \ amount proposed.\"\n    },\n    {\n      \"decision_id\": \"Q10\",\n      \"\
    ingredient\": \"cellobiose\",\n      \"decision\": \"add\",\n      \"fields\"\
    : [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        },\n\
    \        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        }\n\
    \      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465\"\
    ,\n      \"locator\": \"sole recipe sentence\",\n      \"snippet\": \"0.1% cellobiose\"\
    ,\n      \"explanation\": \"The component and literal percentage are present in\
    \ source prose and the child preparation step but absent from ingredients. Add\
    \ the component with source evidence; resolve percentage basis before asserting\
    \ a typed numerical concentration.\",\n      \"calculation\": \"No conversion\
    \ to g/L: source does not explicitly identify w/v, w/w or v/v.\",\n      \"proposed\"\
    : \"Preserve literal percentage in evidence/notes; no concentration enum or converted\
    \ amount proposed.\"\n    },\n    {\n      \"decision_id\": \"Q11\",\n      \"\
    ingredient\": \"maltose\",\n      \"decision\": \"add\",\n      \"fields\": [\n\
    \        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        },\n\
    \        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        }\n\
    \      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465\"\
    ,\n      \"locator\": \"sole recipe sentence\",\n      \"snippet\": \"0.1% maltose\"\
    ,\n      \"explanation\": \"The component and literal percentage are present in\
    \ source prose and the child preparation step but absent from ingredients. Add\
    \ the component with source evidence; resolve percentage basis before asserting\
    \ a typed numerical concentration.\",\n      \"calculation\": \"No conversion\
    \ to g/L: source does not explicitly identify w/v, w/w or v/v.\",\n      \"proposed\"\
    : \"Preserve literal percentage in evidence/notes; no concentration enum or converted\
    \ amount proposed.\"\n    },\n    {\n      \"decision_id\": \"Q12\",\n      \"\
    ingredient\": \"soluble starch\",\n      \"decision\": \"add\",\n      \"fields\"\
    : [\n        {\n          \"path\": \"data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        },\n\
    \        {\n          \"path\": \"data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml\"\
    ,\n          \"field\": \"ingredients (missing source supplement)\"\n        }\n\
    \      ],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=465\"\
    ,\n      \"locator\": \"sole recipe sentence\",\n      \"snippet\": \"0.1% soluble\
    \ starch\",\n      \"explanation\": \"The component and literal percentage are\
    \ present in source prose and the child preparation step but absent from ingredients.\
    \ Add the component with source evidence; resolve percentage basis before asserting\
    \ a typed numerical concentration.\",\n      \"calculation\": \"No conversion\
    \ to g/L: source does not explicitly identify w/v, w/w or v/v.\",\n      \"proposed\"\
    : \"Preserve literal percentage in evidence/notes; no concentration enum or converted\
    \ amount proposed.\"\n    },\n    {\n      \"decision_id\": \"Q13\",\n      \"\
    ingredient\": \"L-cysteine hydrochloride monohydrate\",\n      \"decision\": \"\
    add\",\n      \"fields\": [],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"post-makeup preparation\",\n      \"snippet\": \"0.5 g\
    \ L-cysteine·HCl·H2O\",\n      \"explanation\": \"Base-owner prose retains the\
    \ addition but the six ingredient rows omit it. Child/target do not expose the\
    \ inherited preparation. Exact supplied form must remain explicit; no substitute\
    \ ontology identifier is invented.\",\n      \"calculation\": \"None; preserve\
    \ source stage and unresolved basis.\",\n      \"proposed\": \"Add a stage-scoped\
    \ source amount only after the base preparation is represented.\"\n    },\n  \
    \  {\n      \"decision_id\": \"Q14\",\n      \"ingredient\": \"Agar slant option\"\
    ,\n      \"decision\": \"evidence_only\",\n      \"fields\": [],\n      \"reference\"\
    : \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\",\n      \"locator\"\
    : \"conditional alternative\",\n      \"snippet\": \"15 g agar per 1.0 L medium\"\
    ,\n      \"explanation\": \"Optional solid variant; do not add agar to the selected\
    \ liquid default.\",\n      \"calculation\": \"None; preserve source stage and\
    \ unresolved basis.\",\n      \"proposed\": \"No final-medium numerical value\
    \ certified.\"\n    },\n    {\n      \"decision_id\": \"Q15\",\n      \"ingredient\"\
    : \"Commercial cooked-meat alternative\",\n      \"decision\": \"evidence_only\"\
    ,\n      \"fields\": [],\n      \"reference\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=461\"\
    ,\n      \"locator\": \"commercial alternative supplements\",\n      \"snippet\"\
    : \"5 g/L yeast extract\",\n      \"explanation\": \"Commercial products are an\
    \ alternative to the extraction route. The source lists four separate supplements;\
    \ do not blend that route into the default extraction formulation.\",\n      \"\
    calculation\": \"Commercial route: yeast extract5g/L, phosphate5g/L, resazurin1mg/L,\
    \ cysteine hydrochloride monohydrate0.5g/L are explicit alternative-route facts,\
    \ not support for the copied default amounts.\",\n      \"proposed\": \"Keep a\
    \ separate alternative and product/version boundary; no inferred proprietary composition.\"\
    \n    }\n  ],\n  \"local_concentration_field_count\": 18,\n  \"decision_count\"\
    : 15,\n  \"conditions\": {\n    \"source_base_ph\": 7.0,\n    \"target_and_child_ph\"\
    : \"absent\",\n    \"scope\": \"Preparation pH, not a growth optimum.\",\n   \
    \ \"base_preparation\": \"Full source and owner prose assessed; boiling15min,\
    \ dispensing7ml and particle:fluid1:4–5, nitrogen atmosphere, stopper and121C30min\
    \ are preparation context. Default page-wide121C15min does not override the specific\
    \ recipe. No incubation/growth temperature inferred.\"\n  }\n}"
- assessment_id: preparation
  area: completeness
  topic: Reachable base preparation and supplied forms
  outcome: concern
  summary: The child/target retain only the carbohydrate sentence and lack a structured
    parent/base link. The base has the full source prose but misclassifies coarse
    filtering as FILTER_STERILIZE; the source separates boiling, filtration and later
    autoclaving.
  target_ids:
  - CultureMech:002813
  evidence_ids:
  - base-owner
  - child-owner
  - target
  - jcm461
  - importer
  details: Preserve the source extraction and supplementation stages, preparation
    pH and conditional agar/commercial branches. No incubation temperature, tested
    organism or growth assertion is supplied by these source pages.
- assessment_id: grounding
  area: grounding
  topic: Existing exact chemical IDs and packaged MIM decisions
  outcome: supported
  summary: All18 asserted chemical slots resolve to three active ChEBI IDs with matching
    labels; source wording supports the three named chemical identities. Pinned MIM
    answers all six input labels.
  target_ids:
  - CultureMech:002813
  evidence_ids:
  - ols32145
  - ols131527
  - ols8806
  - mim
  - mim-metadata
  - check-mim-label-index
  - diagnostics
  details: MIM also returns FOODON/MICRO identifiers for three undefined mixtures;
    these are snapshot diagnostics, not new reviewed ontology assignments. A source
    normality is a stock-strength qualifier, not a different sodium-hydroxide identity.
    The source does not specify a sodium resazurin salt; no counterion is added. Native
    chemistry term validation does not certify these IDs, so the external objects
    were inspected separately.
- assessment_id: evidence
  area: evidence
  topic: Source provenance, historical findings and claim placement
  outcome: concern
  summary: Official JCM and MediaDive access succeeds. Target and owners have source
    links in notes but no claim-level evidence or bibliography; native reference validation
    performs zero checks.
  target_ids:
  - CultureMech:002813
  evidence_ids:
  - target
  - base-owner
  - child-owner
  - jcm465
  - jcm461
  - api465
  - api461
  - validate-references
  - history1
  - history2
  - history3
  - history4
  - history5
  details: Five exact-target/owner reports were read fully. Eighteen same-label candidate
    reports were retained as metadata comparisons only; their scientific contents
    do not support this verdict. Old source-access timestamps remain historical; current
    API bytes match their stored source digests. No structured issue is closed.
- assessment_id: structure
  area: schema
  topic: Required native validators and declared scope
  outcome: supported
  summary: All four canonical checks and the MIM integrity check passed. All target
    YAML bytes and both owner records were read.
  target_ids:
  - CultureMech:002813
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
  - check-mim-label-index
  details: No organism, strain, gene, protein or transcriptomic assertion exists in
    the selected target and two owners; iModulonDB is not applicable. No universal
    negative literature claim or experimental growth claim is made.
findings:
- finding_id: F1
  issue_key: cm002813-base-supplemented-merge-collapse
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Stored merge equates the supplemented medium with its base
  description: The source defines JCM465 as a derivative of JCM461. Copied base-only
    ingredients collapse their ingredient fingerprint, creating a misleading synonym
    and J461 KG match. Current formulation-aware merging rejects the pair, so the
    stored product remains stale.
  target_ids:
  - CultureMech:002813
  field_paths:
  - merged_from
  - synonyms
  - kg_microbe_match
  - merge_fingerprint
  evidence_ids:
  - target
  - child-owner
  - base-owner
  - jcm465
  - api465
  - api461
  - merge-formulation
  - merger
  - diagnostics
  rule_id: P2.5
  native_severity: P2
  normalization_reason: Material variant identity and source-boundary error; the selected
    record itself is unambiguous.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
- finding_id: F2
  issue_key: cm002813-extraction-denominator-stock-unit
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Copied extraction quantities use an unsupported final-medium basis
  description: All six direct amounts in the target and owners have a stage/unit conflict.
    Five reproduce division by the initial1025ml liquid inputs even though the source
    later makes the filtrate to1L; NaOH changes a volume of1N stock to a mass concentration.
    Meat extraction recovery and the final particle mixture prevent simplistic final-medium
    replacement values.
  target_ids:
  - CultureMech:002813
  field_paths:
  - ingredients[*].concentration
  evidence_ids:
  - quantity-inventory
  - jcm461
  - api461
  - importer
  rule_id: P2.3
  native_severity: P2
  normalization_reason: Dimension and stage errors materially alter formulation interpretation;
    not a style issue.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
- finding_id: F3
  issue_key: cm002813-source-supplements-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source additions remain absent from structured formulation
  description: JCM465 carbohydrate additions survive only in prose, while inherited
    cysteine is present only in base preparation. Copying six base rows did not resolve
    the whole formulation. Literal carbohydrate percentages have no explicit basis
    and must not be converted by assumption.
  target_ids:
  - CultureMech:002813
  field_paths:
  - ingredients
  - preparation_steps
  - data_quality_flags
  evidence_ids:
  - target
  - base-owner
  - child-owner
  - quantity-inventory
  - jcm465
  - jcm461
  rule_id: P3.1
  native_severity: P3
  normalization_reason: Raised to major because omitted source components change the
    represented medium; RESOLVED_REFERENCE is not completeness evidence.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
- finding_id: F4
  issue_key: cm002813-base-preparation-boundary
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Inherited preparation cannot be followed through the child record
  description: The target and child have no structured parent link exposing the base
    extraction/preparation. The maintained base prose is present, but FILTER_STERILIZE
    labels coarse meat filtration as a sterile filtration step. Source-specific treatment
    and alternatives require distinct representation.
  target_ids:
  - CultureMech:002813
  field_paths:
  - preparation_steps
  - parent_media
  - ph_value
  - data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml::preparation_steps[0].action
  evidence_ids:
  - base-owner
  - child-owner
  - target
  - jcm461
  - importer
  rule_id: P3.4
  native_severity: P3
  normalization_reason: Raised to major because a preparation boundary and material
    handling meaning are lost, while existing base prose is credited.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
- finding_id: F5
  issue_key: cm002813-claim-provenance-gap
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source links lack claim-level evidence and bibliography
  description: The notes URLs resolve but no structured formulation evidence or reference
    entry is attached. The reference validator therefore checks zero references. Preserve
    both source identities and exact claim stages when adding evidence.
  target_ids:
  - CultureMech:002813
  field_paths:
  - evidence
  - references
  - ingredients[*].evidence
  evidence_ids:
  - target
  - base-owner
  - child-owner
  - validate-references
  - jcm465
  - jcm461
  rule_id: P4.3
  native_severity: P4
  normalization_reason: Minor recoverability/claim-placement gap; source identity
    remains recoverable through notes.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
actions:
- action_id: A1
  description: 'Curate the two maintained owners from exact JCM source boundaries:
    retain the base extraction and stock identities, restore source-specific component
    representation, and preserve unsupported final concentrations and percentage bases
    as unresolved. Append an actual curation event only when edits occur.'
  finding_ids:
  - F2
  - F3
  - F4
  - F5
  target_ids:
  - CultureMech:002813
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Reconcile all18 existing amount fields against the15 retained decisions; no1025ml
    denominator reused after filtrate makeup and no mass unit substituted for a stock
    volume.
  - Keep carbohydrate percentages literal until basis is established; do not blend
    agar or commercial alternatives into the liquid default.
  - Coarse filtration must not be labeled sterile filtration; inherited base preparation
    and exact chemical forms must be reachable.
  - Attach narrow exact-source evidence and bibliography, then run the four native
    validators for each edited owner.
- action_id: A2
  description: After maintained source curation, regenerate with the current formulation-aware
    merge path and reassess the J461 KG association without treating ingredient identity
    alone as recipe identity.
  finding_ids:
  - F1
  target_ids:
  - CultureMech:002813
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J461_CHOPPED_MEAT_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/JCM_J465_CHOPPED_MEAT_MEDIUM_WITH_CARBOHYDRATES.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
  depends_on:
  - A1
  generator: python -m culturemech.merge.merge_recipes
  acceptance_checks:
  - BaseJ461 and supplementedJ465 remain distinct; generated identity, synonyms and
    source accessions follow the represented formulation.
  - Generated source claims and newly attached evidence are retained; no direct generated-YAML
    patch.
  - Run just verify-merges and just audit-merge-freshness plus applicable product
    gates after the separately authorized change.
limitations:
- No final particle-mixture concentration or percent basis is inferred where source
  text does not supply it. Known extraction and makeup stages are retained without
  inventing recovery, density or volume additivity.
- The attempted MDP=1 URLs returned the same HTML, not PDF; actual HTML and REST responses
  support this review. Initial /api endpoints404 were preserved before correct /rest
  endpoint captures succeeded.
- The original raw-import captures at three exact documented paths are unavailable
  in this isolated checkout (lexists check includes ignored paths). This is not a
  claim that they are absent elsewhere; historical causality is inferred only where
  current bytes and writer behavior support it.
- Four canonical checks apply to the selected target; contributors were read as context.
  Full-corpus gates, fresh external KG graph matching and experimental growth validation
  were not performed.
- Same-label candidate-report contents were not adopted as evidence or coverage. No
  previous structured finding is retired, no record history is changed and no scientific
  status is promoted.
notes:
- Private quantity inventory preserves source amount/unit/stage decisions and hashes;
  generated data and maintained records were not edited.
- Current merger safeguard and already-preserved base prose are credited; remaining
  issues describe the stored scientific record.
tags:
- review-only
- batch061
- source-boundaries
- quantity-inventory
```
