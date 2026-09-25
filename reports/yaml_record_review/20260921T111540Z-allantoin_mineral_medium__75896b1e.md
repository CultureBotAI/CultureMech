# YAML Record Review: allantoin_mineral_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml`
- Started UTC: 2026-09-21T11:14:49Z
- Finished UTC: 2026-09-21T11:15:41Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008240` |
| Name | `allantoin_mineral_medium` |
| Original name | `Allantoin Mineral Medium` |
| Source identity | TOGO Medium M1681, original source NBRC M886 |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml` |

The generated record is a one-source merge of the TOGO import for NBRC M886.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml --out /private/tmp/allantoin_mineral_medium__75896b1e.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The generated ID, TOGO source, NBRC original source, and normalized owner agree:

- `id: CultureMech:008240`
- `name: allantoin_mineral_medium`
- `media_term.term.id: TOGO:M1681`
- `notes: Original source: NBRC - NBRC_M886`
- `notes: Original URL: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=886`

NBRC Medium No. 886 and the TOGO M1681 API both identify the recipe as Allantoin Mineral Medium. The ingredient grounding is exact for water, magnesium sulfate heptahydrate, calcium chloride dihydrate, potassium dihydrogen phosphate, dipotassium hydrogen phosphate, allantoin, and agar. The `FeSO4 x 7 H2O` and `MnSO4 x H2O` primary `term` values are exact hydrated salts but lack mirrored `mediaingredientmech_chebi_term` entries.

## Evidence

Inspected source documents:

- NBRC Medium No. 886 at `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=886`
- TOGO Medium M1681 API at `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1681`

Supported claims:

- NBRC and TOGO both support the Allantoin Mineral Medium identity and the NBRC_M886 accession.
- NBRC directly supports 0.8 g K2HPO4, 0.2 g KH2PO4, 0.5 g MgSO4 x 7 H2O, 0.05 g CaCl2 x 2 H2O, 0.01 g FeSO4 x 7 H2O, 20 g allantoin, 15 g agar, 1 L distilled water, and pH 7.2.
- The TOGO API supports the same ingredients and annotates their expected GMO roles.

Unsupported or mismatched claims:

- NBRC and TOGO both list `MnSO4 x H2O` as 1 mg, but the CultureMech record stores `1 G_PER_L`.
- NBRC and TOGO both list water as 1 L, but the CultureMech record stores `Distilled water` as `1 G_PER_L`.
- TOGO exposes pH 7.2 in both `meta.ph` and a comment; the CultureMech record lacks `ph_value`.

## Completeness

Consequential gaps:

- The manganese sulfate amount is 1000-fold too high.
- The NBRC pH value is absent.
- Distilled water is modeled with the wrong unit dimension.
- The NBRC/TOGO copy is not reconciled with the DSMZ/KOMODO Allantoin Mineral Medium duplicate cluster.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- NBRC M886 has an empty comment field, so the lack of `preparation_steps` is consistent with the inspected primary source.
- No storage conditions or gas conditions were asserted.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*allantoin_mineral_medium__75896b1e.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the record slug, the uppercase original name, and `75896b1e` found the TOGO M1681 owner, this generated record, a DSMZ Medium 6 owner, KOMODO Medium 6 owners, and the older generated duplicate cluster rooted at `data/merge_yaml/merged/ALLANTOIN_MINERAL_MEDIUM.yaml`.

## Findings

### Blocker

None found.

### Major

1. **NBRC M886 manganese sulfate is off by a factor of 1000.**

   Evidence: NBRC M886 lists `MnSO4 x H2O` as 1 mg, and TOGO M1681 preserves `volume: 1` with `unit: "mg"`. `data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml` stores the same reagent as `1 G_PER_L`.

   Owner: correct the mg-to-g conversion in `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml` or the TOGO importer, then regenerate.

2. **NBRC M886 distilled water is modeled as 1 g/L.**

   Evidence: both NBRC and TOGO list distilled water as a 1 L solvent row. The generated CultureMech record stores `Distilled water` with `value: '1'` and `unit: G_PER_L`, which turns a volume basis into a gram-per-liter ingredient and changes the merge fingerprint relative to DSMZ Medium 6 imports that omit this solvent row.

   Owner: remove the solvent row from `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml` or represent it with a volume unit if the schema supports solvent amounts, then regenerate.

3. **The source pH 7.2 value was dropped.**

   Evidence: the TOGO API exposes `meta.ph: "7.2"` and a comment containing the same pH; NBRC M886 also gives pH 7.2 after the composition table. The generated record lacks `ph_value`.

   Owner: import NBRC/TOGO pH into `ph_value` for `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml`, then regenerate.

4. **The NBRC/TOGO import is still split from same-formulation DSMZ and KOMODO Allantoin Mineral Medium records.**

   Evidence: the ignored-inclusive slug search found `data/normalized_yaml/bacterial/allantoin_mineral_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_6_ALLANTOIN_MINERAL_MEDIUM.yaml`, and `data/normalized_yaml/bacterial/medium_6_modified_for_dsm_1306.yaml`, all carrying DSMZ Medium 6 or copied-DSMZ provenance with the same non-solvent ingredient list once NBRC's 1 mg manganese sulfate is converted to 0.001 g/L. Those three source records are already joined in `data/merge_yaml/merged/ALLANTOIN_MINERAL_MEDIUM.yaml`, but the TOGO/NBRC record remains isolated by the manganese and water import errors.

   Owner: after correcting TOGO M1681, rerun merge generation and verify the NBRC/TOGO copy joins the existing source-duplicate cluster or is explicitly linked to it.

### Minor

1. **Two exact hydrated salt terms are missing mirrored MediaIngredientMech links.**

   Evidence: `FeSO4 x 7 H2O` and `MnSO4 x H2O` have exact ChEBI `term` entries, but neither row has `mediaingredientmech_chebi_term`.

   Owner: rerun ingredient enrichment over `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml` after correcting the manganese amount.

## Recommended Edits

1. Correct TOGO M1681 manganese sulfate to 0.001 g/L or preserve it as 1 mg/L in `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml`.
2. Remove or volume-model the 1 L distilled-water row so it no longer appears as a 1 g/L solute.
3. Add `ph_value: 7.2` from the NBRC and TOGO sources.
4. Fill exact `mediaingredientmech_chebi_term` mirrors for FeSO4 x 7 H2O and MnSO4 x H2O.
5. Regenerate generated merge records and rendered products.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected TOGO M1681 normalized owner and regenerated output.
- Rerun duplicate merging and confirm the corrected TOGO/NBRC import no longer fingerprints as `75896b1e3d6a94c98e22bb11c426b6cf06cd1b2786043ce48ead92e7309ca551`.
- Manually diff the regenerated output against NBRC M886 and verify 0.001 g/L manganese sulfate, pH 7.2, 20 g/L allantoin, and 15 g/L agar.
- Inspect the regenerated duplicate cluster to confirm the NBRC/TOGO import is reconciled with DSMZ Medium 6 and KOMODO Medium 6.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/allantoin_mineral_medium__75896b1e.yaml`, its normalized owner, adjacent duplicate records, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/TOGO_M1681_Allantoin_Mineral_Medium.yaml` or the TOGO import/merge/enrichment rules that own the bad transform.
