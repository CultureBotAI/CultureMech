# YAML Record Review: Columbia Blood Agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar__06261cb5.yaml`
- Started UTC: `2026-09-22T10:27:45Z`
- Finished UTC: `2026-09-22T10:31:15Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009114` for TOGO Medium `M2545`, `Columbia Blood Agar`, generated from `data/normalized_yaml/bacterial/TOGO_M2545_Columbia_Blood_Agar.yaml` on merge fingerprint `06261cb5c8e609949373f921603a60fa7739b4bab1157901377a4a69beef3b12`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar__06261cb5.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The top-level TOGO identity is coherent: TOGO `M2545` points to DSMZ Medium 429, `COLUMBIA BLOOD AGAR`.

The scientific identity is wrong below that top-level source. DSMZ 429 defines Columbia blood agar as Columbia agar base supplemented with 4% horse blood. The record instead expands `Brain Heart Infusion` as if BHI were the agar base.

An ignored-inclusive generated-record search found multiple related Columbia blood agar branches, including three `columbia_blood_agar__*.yaml` generated records and several blood-source variants. The search included ignored files.

## Evidence

The DSMZ Medium 429 PDF supports exactly one formulation statement for this medium: Columbia agar base supplemented with 4% horse blood. It then names DSMZ media 545, 215, and 1 as liquid rehydration media for freeze-dried ampoules, with medium 215 specifically used to rehydrate Helicobacter and Campylobacter species.

TOGO M2545 correctly points back to DSMZ Medium 429, but its parsed component list incorrectly includes 37 g `Brain Heart Infusion (Difco)` from the downstream DSMZ Medium 215 BHI block. That BHI component is not a Columbia Blood Agar ingredient.

The local BHI expansion is therefore also unsupported: calf brains, beef heart, Proteose peptone, dextrose, sodium chloride, and disodium phosphate were expanded from an ingredient that should not be in this record.

## Completeness

The record is missing the required Columbia agar base component. It also lacks 4% horse blood as a volume or percentage addition; the imported 4% value was stored as `PERCENT_W_V`.

The physical state is `LIQUID`, but DSMZ Medium 429 is an agar medium.

No target organism or growth evidence is present. That is an empty optional area in this source-only branch.

## Findings

- Severe: the record expands an unrelated BHI rehydration-medium ingredient instead of modeling DSMZ 429 as Columbia agar base plus horse blood.
- Major: the actual DSMZ 429 Columbia agar base component is absent.
- Major: 4% horse blood is represented as `PERCENT_W_V`, even though the source is a blood supplement percentage for agar preparation.
- Major: `physical_state` is `LIQUID`, but the source medium is agar.
- Major: this TOGO M2545 branch remains unmerged with other DSMZ 429 / KOMODO 429 Columbia blood agar branches because the formulation fingerprint is dominated by the wrong BHI expansion.

## Recommended Edits

- In `data/normalized_yaml/bacterial/TOGO_M2545_Columbia_Blood_Agar.yaml`, remove the BHI expansion rows and the external Brain Heart Infusion commercial-product note.
- Replace the unsupported BHI-derived ingredient list with an ungrounded or product-backed `Columbia agar base` component plus 4% horse blood, matching the DSMZ 429 wording.
- Change `physical_state` to `SOLID_AGAR`.
- Model horse blood as a 4% liquid supplement rather than `PERCENT_W_V`.
- Regenerate `data/merge_yaml/merged/` and merge or deliberately link the repaired TOGO M2545 branch with the other DSMZ 429 / KOMODO 429 Columbia blood agar inputs.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm no BHI-derived calf brain, beef heart, Proteose peptone, dextrose, NaCl, or disodium phosphate rows remain.
- Confirm `Columbia agar base` and 4% horse blood remain as source-supported components.
- Confirm the physical state is solid agar.
- Confirm repaired DSMZ 429 branches merge or are linked as source duplicates.

## Additional Notes

Empty optional fields are not defects.
