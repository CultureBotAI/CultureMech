# YAML Record Review: modified_sour_dough_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml
- Started UTC: 2026-09-24T13:15:55Z
- Finished UTC: 2026-09-24T13:16:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:010199 |
| Name | modified_sour_dough_medium |
| Original name | Modified Sour Dough Medium |
| Category | bacterial |
| Source identity | TOGO:M78, imported from JCM Medium 87 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/TOGO_M78_Modified_Sour_Dough_Medium.yaml` or the TOGO/JCM import rules. |

An ignored-file-inclusive exact search for `CultureMech:010199`, `TOGO:M78`, `TOGO_M78_Modified_Sour_Dough_Medium`, `M78`, `4add828e`, and `GRMD=87` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this generated merge, its maintained TOGO owner, the MediaDive/JCM 87 sibling, index and aggregate QA rows, and the immediately prior review report for that sibling. The reviewed generated record is a singleton merge from `TOGO_M78_Modified_Sour_Dough_Medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml --out /private/tmp/modified_sour_dough_medium__4add828e.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record denotes the intended TOGO entry: live TOGO M78 resolves to `Modified Sour Dough Medium`, names `JCM_M87` as `original_media_id`, links to the JCM `GRMD=87` page, and reports pH 5.6. JCM Medium 87 is the same liquid modified sour dough medium.

The protein and surfactant ingredients match the source. The maltose grounding is too narrow: the source says `Maltose`, while the YAML uses `CHEBI:18167` / alpha-maltose. No source inspected here states the anomeric form.

## Evidence

The live TOGO M78 payload reproduces the JCM quantities for yeast extract, Tween 80, maltose, and Trypticase peptone. It also carries the JCM pH text as a comment and exposes pH 5.6 in `meta.ph`.

Three imported claims are not source-faithful:

- The 1 L distilled-water basis is represented as `1 G_PER_L`.
- `lactic acid` is modeled as a variable carbon-source ingredient even though it appears only as one of two optional pH-adjustment reagents in the source comment.
- The pH 5.6 value and pH-adjustment comment are absent from `ph_value` and `preparation_steps`.

## Completeness

The generated TOGO branch is missing all preparation detail: JCM's pH 5.6 adjustment is present in the TOGO payload but not in YAML, and the JCM default autoclaving instruction is not present in either TOGO M78 or the generated record.

`target_organisms` and `growth_evidence` are empty. Those empty optional fields are acceptable because TOGO M78 and JCM 87 are recipe sources, not growth-evidence assertions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Source-supported pH and preparation instructions were dropped. | TOGO M78 reports `ph: 5.6` and repeats the JCM comment about adjusting pH to 5.6 with lactic acid or HCl, while the YAML has no `ph_value` or `preparation_steps`. JCM also supplies a default 121 C, 15 min autoclaving instruction that is absent from the TOGO branch. | `data/normalized_yaml/bacterial/TOGO_M78_Modified_Sour_Dough_Medium.yaml`; TOGO/JCM pH and preparation import. |
| major | The 1 L water basis was converted to a false grams-per-liter concentration. | TOGO and JCM both state 1 L distilled water; the generated YAML has `Distilled water` at `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M78_Modified_Sour_Dough_Medium.yaml`; TOGO unit normalization. |
| major | Lactic acid was promoted from a pH reagent option to a variable carbon-source ingredient. | The only source mention is in the phrase adjusting pH with 20% lactic acid or 1 N to 6 N HCl; neither reagent is a medium nutrient in the JCM table. | `data/normalized_yaml/bacterial/TOGO_M78_Modified_Sour_Dough_Medium.yaml`; TOGO pH-reagent handling. |
| major | Maltose is over-grounded to alpha-maltose. | TOGO/JCM say `Maltose` without specifying an anomer; the YAML ChEBI row is `CHEBI:18167` / alpha-maltose. | `data/normalized_yaml/bacterial/TOGO_M78_Modified_Sour_Dough_Medium.yaml`; ChEBI enrichment. |
| minor | The TOGO M78 and direct MediaDive/JCM 87 branches need source-duplicate reconciliation. | Both branches cite the same JCM `GRMD=87` page but currently produce separate generated records, `modified_sour_dough_medium__4add828e.yaml` and `modified_sour_dough_medium__38815cbb.yaml`. | Merge/source-duplicate curation for JCM GRMD 87. |

No blocker findings.

## Recommended Edits

1. Restore `ph_value: 5.6` and add the pH-adjustment step from the TOGO/JCM comment.
2. Preserve the JCM default autoclaving instruction as a preparation step.
3. Remove the top-level variable `lactic acid` carbon-source ingredient; represent lactic acid and HCl only as alternative pH-adjustment reagents in the preparation text.
4. Convert the 1 L distilled-water row either to a volume/final-volume representation or omit it as a concentration-bearing ingredient after preserving the 1 L basis elsewhere.
5. Replace the over-specific alpha-maltose grounding with a generic maltose ChEBI term or leave the row explicitly unresolved until an exact source-supported term is verified.
6. Reconcile the TOGO M78 and MediaDive/JCM 87 branches once their formulations agree on ingredients and preparation.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml`.
- Inspect the regenerated YAML against both TOGO M78 and JCM 87 to confirm the pH, pH reagents, autoclaving, maltose grounding, and 1 L basis are all scoped correctly.
- Re-run merge freshness and confirm JCM 87 is not left as two independent generated sour-dough liquid records when the TOGO M78 and MediaDive versions have equivalent source support.

## Additional Notes

The JCM page names `Trypticase peptone (BD-BBL)`, and the TOGO branch preserves that full string. Its extra specificity is source-supported and is not a defect.
