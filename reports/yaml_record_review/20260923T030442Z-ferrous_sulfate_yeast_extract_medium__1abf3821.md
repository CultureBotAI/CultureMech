# YAML Record Review: ferrous_sulfate_yeast_extract_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferrous_sulfate_yeast_extract_medium__1abf3821.yaml
- Started UTC: 2026-09-23T03:03:18Z
- Finished UTC: 2026-09-23T03:04:42Z
- Verdict: needs curation

## Target

CultureMech:010443 is the generated merged record for DSMZ Medium 1190, `FERROUS SULFATE/YEAST EXTRACT MEDIUM`, plus two KOMODO organism-specific DSMZ 1190 variants for DSM 19497 and DSM 19514.

DSMZ 1190 defines a 1 L medium made from 0.20 g yeast extract, 20 ml 50x Heterotrophic basal salts solution, 20 ml 27.8% ferrous sulfate solution, and 960 ml distilled water. The DSMZ page also defines a 50x basal-salts stock, a ferrous sulfate stock, a pH 2.0 adjustment for DSM 19497, and a pH 1.8-2.0 adjustment for DSM 19514.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` exited 0 and the TSV contained only the header row.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The generated record points to the intended DSMZ 1190 recipe and correctly lists the KOMODO 1190_19497 and 1190_19514 sources as synonyms for the merged bacterial variants.

The simple salts are grounded to specific CHEBI terms. `Yeast extract` is an undefined component and appropriately lacks a single CHEBI term.

The generated `ph_value: 2.0` matches the base DSMZ record and the DSM 19497 adjustment but loses the DSM 19514-specific 1.8-2.0 range that was present in `data/normalized_yaml/bacterial/medium_1190_modified_for_dsm_19514.yaml`.

## Evidence

The three source records share the same ingredients and stock concentrations, so deduplicating them is reasonable at the composition level.

The generated ingredient list, however, flattens stock recipes at full stock concentration. DSMZ uses only 20 ml of the 50x Heterotrophic basal salts solution per liter, but the generated record has the full stock values: 7.5 g/L Na2SO4 x 10 H2O, 22.5 g/L ammonium sulfate, 25 g/L MgSO4 x 7 H2O, and related salts. DSMZ uses 20 ml of 27.8% ferrous sulfate solution per liter, but the generated record stores the 278 g/L stock concentration as the medium's FeSO4 x 7 H2O concentration.

The generated preparation steps retain the DSMZ instruction to autoclave the yeast-extract and basal-salts medium and add filter-sterilized ferrous sulfate after cooling.

## Completeness

The generated record is identity-complete for all three merged sources, but it is not composition-complete as a final medium because the basal-salts and ferrous-sulfate stocks are not scaled or nested.

The merge also loses the organism-specific pH distinction for DSM 19514.

## Findings

1. The 50x Heterotrophic basal salts stock is flattened at full strength instead of represented as a 20 ml/L stock addition or scaled 50-fold lower.
2. The 27.8% ferrous sulfate stock is flattened at 278 g/L instead of represented as a 20 ml/L stock addition or scaled to its final contribution.
3. The DSM 19514-specific pH range 1.8-2.0 is collapsed into the canonical `ph_value: 2.0`.

## Recommended Edits

1. Recurate DSMZ 1190 with the 50x basal-salts and 27.8% ferrous-sulfate solutions preserved as nested stocks, or scale their constituents by 20 ml/L before flattening.
2. Preserve the DSM 19514 pH range in a variant record or in merge provenance instead of discarding it during fingerprint merging.
3. Keep the current DSM 1190, KOMODO 1190_19497, and KOMODO 1190_19514 source identities attached after the composition fix.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after recurating the stock additions.
- Confirm the final top-level FeSO4 x 7 H2O amount is no longer the 278 g/L stock concentration.
- Confirm DSM 19497 and DSM 19514 pH requirements remain discoverable.

## Additional Notes

The DSMZ Medium 1190 PDF was fetched and rendered to text with `mutool`; its stock formulas and organism-specific pH notes match the MediaDive REST payload and the normalized KOMODO variant metadata used for this review.
