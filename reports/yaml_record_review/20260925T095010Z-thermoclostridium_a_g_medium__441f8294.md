# YAML Record Review: THERMOCLOSTRIDIUM A-G MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoclostridium_a_g_medium__441f8294.yaml`
- Started UTC: `2026-09-25T09:50:10Z`
- Finished UTC: `2026-09-25T09:51:11Z`
- Verdict: needs curation

## Target
Generated bacterial recipe `CultureMech:001427`, `thermoclostridium_a_g_medium`, with medium term `mediadive.medium:326` and label `THERMOCLOSTRIDIUM (A-GO) MEDIUM`.

It merges the MediaDive DSMZ 326 source with two KOMODO DSMZ 326 aliases: `komodo.medium:326` and the stalely named sucrose variant.

## Validation
- LinkML schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The generated branch is correctly grounded to DSMZ Medium 326. DSMZ 326 itself uses sucrose, so the KOMODO source name that mentions replacing cellobiose with sucrose is a stale alias after normalization, not an active cellobiose variant in this generated record.

The same DSMZ 326 recipe remains split into the TOGO M2756 branch `data/merge_yaml/merged/thermoclostridium_a_g_medium.yaml`.

Reviewed ingredient groundings on this branch are internally consistent for the flattened SL-10 and vitamin rows.

## Evidence
DSMZ Medium 326 and MediaDive 326 specify direct main-solution rows for KH2PO4, MgCl2 x 6 H2O, 12 mg CoCl2 x 6 H2O, 1 ml Trace element solution SL-10, yeast extract, trypticase peptone, resazurin, carbonate, sucrose, 1 ml Wolin's vitamin solution 10x, cysteine, sulfide, and water.

The generated MediaDive/KOMODO branch preserves the main 12 mg cobalt row at `0.011976 G_PER_L`, but it then flattens SL-10 at stock concentrations. The stock `CoCl2 x 6 H2O` row at `0.19 G_PER_L` is merged with the direct row, producing `0.201976 G_PER_L`.

SL-10's HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O also appear as top-level final ingredients instead of remaining inside the 1 ml/L stock addition.

The generated branch likewise flattens Wolin's vitamin solution 10x into top-level vitamin rows at 1 L stock concentrations, including `Biotin` at `0.02 G_PER_L`, `Pyridoxine hydrochloride` at `0.1 G_PER_L`, and `Vitamin B12` at `0.001 G_PER_L`.

## Completeness
The DSMZ preparation step is preserved, including N2/CO2 sparging, separately prepared stock additions for carbonate, sucrose, vitamins, cysteine, and sulfide, and final pH adjustment.

The SL-10 preparation step is preserved textually, but its components are no longer scoped to the SL-10 stock.

## Findings
1. Needs curation: Trace element solution SL-10 was flattened into the final ingredient list and its cobalt row was merged with the direct 12 mg cobalt addition.
2. Needs curation: Wolin's vitamin solution 10x was flattened into final top-level vitamin rows.
3. Needs curation: TOGO M2756 remains an unmerged duplicate branch for the same DSMZ 326 source.

## Recommended Edits
1. Normalize the MediaDive, KOMODO, and TOGO DSMZ 326 source records, not the generated merge files, so SL-10 and Wolin's vitamin solution 10x remain nested 1 ml/L stock additions.
2. Preserve the direct 12 mg CoCl2 x 6 H2O row separately from the SL-10 cobalt row.
3. Keep the DSMZ preparation text and SL-10 preparation text attached to the correct main or stock recipe after regeneration.
4. Merge `mediadive.medium:326`, `komodo.medium:326`, and `TOGO:M2756` by exact DSMZ 326 source identity once all branches represent stocks consistently.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:326`, `komodo.medium:326`, `TOGO:M2756`, and `DSMZ_Medium326.pdf` and confirm that DSMZ 326 regenerates as one canonical output.

## Additional Notes
Exact duplicate-source searches included ignored files.
