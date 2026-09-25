# YAML Record Review: tepidanaerobacter_acetatoxydans_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tepidanaerobacter_acetatoxydans_medium__3dbd7947.yaml`
- Started UTC: 2026-09-25T09:11:39Z
- Finished UTC: 2026-09-25T09:12:56Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008931` for `tepidanaerobacter_acetatoxydans_medium`, the TOGO M2343 import of DSMZ Medium 1301 merged from `TOGO_M2343_Tepidanaerobacter_Acetatoxydans_Medium.yaml` with fingerprint `3dbd79477aec112b6081c9d738b0e987e0c1d6d776e98a113e6ea67d7a9ea46f`.

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; 1 file scanned and 0 error rows written to `/private/tmp/tepidanaerobacter_acetatoxydans_medium__3dbd7947.strict.tsv`.
- Reference validation: Passed; 1 file validated, 0 external checks.
- Term validation: Passed.
- Embedded `curation_history`: Not checked; `just validate-history` validates standalone `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

The generated `TOGO:M2343` record correctly points to DSMZ Medium 1301, TEPIDANAEROBACTER ACETATOXYDANS MEDIUM. The same DSMZ formulation is represented by `mediadive.medium:1301` in `data/normalized_yaml/bacterial/tepidanaerobacter_acetatoxydans_medium.yaml` and by `komodo.medium:1301` in `data/normalized_yaml/bacterial/KOMODO_1301_TEPIDANAEROBACTER_ACETATOXYDANS_medium.yaml`.

Exact searches for `mediadive.medium:1301`, `komodo.medium:1301`, and the Tepidanaerobacter acetatoxydans labels found the expected TOGO, DSMZ/MediaDive, and KOMODO records.

## Evidence

The DSMZ Medium 1301 PDF, MediaDive 1301, and TOGO M2343 all describe a liter-scale medium with KH2PO4, Na2HPO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NaCl, NH4Cl, 0.2 g yeast extract, 0.5 mL 0.1% sodium resazurin, 1.5 g Na2CO3, 1.8 g D-glucose, 0.3 g Na2S x 9 H2O, 0.5 g L-cysteine HCl x H2O, and 1000 mL distilled water.

The same sources represent trace elements, selenite-tungstate, and Wolin vitamins as stock additions to the final medium: 1 mL trace element solution, 1 mL selenite-tungstate solution, and 2 mL Wolin's vitamin solution.

## Completeness

The target has all expected ingredient identities, but the stock solution topology is wrong. The generated record both expands the stock components as top-level ingredients and keeps the three stock solutions as unresolved `Unknown solution` rows.

The generated output is stale relative to the September repair in `data/normalized_yaml/bacterial/TOGO_M2343_Tepidanaerobacter_Acetatoxydans_Medium.yaml`: the normalized source has already collapsed the imported fourfold distilled-water row from `4000.0` to `1000.0`.

## Findings

- Distilled water is summed to `4000.0 G_PER_L` in generated YAML from four duplicate 1000 mL stock-carrier rows.
- Trace element stock entries are imported as raw stock amounts in grams per liter; examples include 36 mg Na2MoO4 x 2 H2O becoming `36 G_PER_L`, 6 mg H3BO3 becoming `6 G_PER_L`, and 190 mg CoCl2 x 6 H2O becoming `190 G_PER_L`.
- The selenite-tungstate stock is also inflated: 3 mg Na2SeO3 x 5 H2O and 4 mg Na2WO4 x 2 H2O are stored as `3 G_PER_L` and `4 G_PER_L`.
- The Wolin vitamin stock is inflated by the same milligrams-as-grams pattern, for example 2 mg biotin as `2 G_PER_L` and 0.1 mg vitamin B12 as `0.1 G_PER_L`.
- Three source stock additions survive as `solutions` rows with `G_PER_L` units even though the upstream recipe adds them as 1 mL, 1 mL, and 2 mL.
- The `Carbon dioxide gas` and `Nitrogen gas` notes still carry non-ASCII source text for the GMO gas property.
- The generated TOGO record missed the existing DSMZ/KOMODO Medium 1301 source-duplicate group.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2343_Tepidanaerobacter_Acetatoxydans_Medium.yaml`, then regenerate merged YAML; do not hand-edit generated merge YAML.
- Preserve the stock additions as named solution rows with 1 mL trace element solution, 1 mL selenite-tungstate solution, and 2 mL Wolin's vitamin solution, or scale every expanded stock component to the final volume.
- Remove duplicated stock-carrier water from the ingredient list and keep only the DSMZ main 1000 mL water carrier if water is represented.
- Sanitize imported gas-property notes to ASCII and avoid carrying raw GMO property labels.
- Merge the repaired TOGO M2343 source with the DSMZ Medium 1301 source-duplicate set that already links the MediaDive and KOMODO imports.

## Follow-up Checks

- Revalidate the regenerated Tepidanaerobacter acetatoxydans record with schema, strict, reference, and term validators.
- Search exact `TOGO:M2343`, `mediadive.medium:1301`, and `komodo.medium:1301`, including ignored files, to confirm DSMZ Medium 1301 no longer emits independent TOGO, DSMZ, and KOMODO generated records.
- Search the repaired TOGO normalized YAML for raw `G_PER_L` values copied from stock milligram rows, including ignored files, before accepting the regeneration.

## Additional Notes

Exact identity searches used `rg --no-ignore --hidden`, so ignored files were included.
