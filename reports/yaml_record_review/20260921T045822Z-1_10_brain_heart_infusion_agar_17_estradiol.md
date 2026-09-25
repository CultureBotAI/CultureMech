# YAML Record Review: 1_10_brain_heart_infusion_agar_17_estradiol

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml`
- Started UTC: 20260921T045657Z
- Finished UTC: 20260921T045822Z
- Verdict: needs curation

## Target

| Field | Observed value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:008495` |
| Label | `1_10_brain_heart_infusion_agar_17_estradiol` |
| Original label | `1/10 Brain Heart Infusion Agar + 17beta-Estradiol` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact under `data/merge_yaml/merged/`; future edits belong in `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml`, TOGO/NBRC import normalization, or merge regeneration |
| Merge owner | `merged_from: [1_10_brain_heart_infusion_agar_17_estradiol]` |
| Maintained owner | `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml` |

This generated singleton is the TOGO Medium M1917 import of NBRC Medium 1181 plus a later manual expansion of the commercial Brain Heart Infusion ingredient.

## Validation

Repository `just` entrypoints were blocked before target-specific validation because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml` | Pass |
| Closed schema / strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml --out /private/tmp/1_10_brain_heart_infusion_agar_17_estradiol.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 files with `ERROR`, TSV at `/private/tmp/1_10_brain_heart_infusion_agar_17_estradiol.strict.tsv` |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone files under `history/` |

## Identity and Grounding

The record correctly identifies TOGO Medium M1917 / NBRC Medium 1181, `1/10 Brain Heart Infusion Agar + 17beta-Estradiol`.

The ingredient representation no longer matches the source:

- NBRC Medium 1181 uses 3.7 g Bacto Brain Heart Infusion (Difco), 1 mg 17beta-Estradiol, 1 L distilled water, and optional 15 g agar.
- The YAML dropped the top-level 3.7 g/L Bacto Brain Heart Infusion powder and replaced it with individual full-strength Brain Heart Infusion constituents.
- The YAML stores 17beta-Estradiol as 1 g/L instead of the NBRC 1 mg/L amount.

## Evidence

Supported by inspected source text:

- NBRC supports the M1181 identity, Bacto Brain Heart Infusion commercial ingredient, 17beta-Estradiol, distilled water, and optional agar.
- NBRC supports the optional 15 g agar row.

Unsupported or malformed in the generated record:

- The Brain Heart Infusion component expansion is not supported by NBRC Medium 1181, which lists only the opaque commercial product.
- Even if Brain Heart Infusion were expanded against a supplier formulation, the YAML component rows are not scaled to the 3.7 g/L powder amount that NBRC specifies.
- The `supplier_catalog` provenance for those expanded rows cites a Microbe Notes article as the product URL while naming Difco/BD and catalog `237500`; the inspected Microbe Notes page is not a Difco/BD catalog sheet and did not substantiate that catalog number.
- 17beta-Estradiol and water have the wrong units.

## Completeness

- The record has no structured `references` block for NBRC M1181, TOGO M1917, or the commercial-product source used for the expansion.
- Empty growth-evidence slots are acceptable for this imported provider recipe because the NBRC page does not state an organism-specific growth observation.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:008495`, `TOGO:M1917`, `NBRC_M1181`, the NBRC 1181 URL slug, and the merge fingerprint found only this normalized owner, this generated singleton, and ID/catalog entries.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The 3.7 g/L Bacto Brain Heart Infusion source ingredient was replaced by unsupported, unscaled component rows. | NBRC Medium 1181 lists 3.7 g Bacto Brain Heart Infusion (Difco) per liter; the YAML has no Bacto Brain Heart Infusion ingredient and instead lists full-strength calf brain, beef heart, proteose peptone, dextrose, sodium chloride, and disodium phosphate rows. | `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml`. |
| Major | The 17beta-Estradiol concentration is 1000-fold too high. | NBRC lists 1 mg 17beta-Estradiol in the 1 L recipe; the YAML stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml` or the TOGO/NBRC unit conversion. |
| Major | The distilled-water row has the wrong dimension. | NBRC lists distilled water as 1 L; the generated and normalized YAML store it as `1 G_PER_L`. | `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml` or the TOGO/NBRC volume import mapping. |
| Major | The commercial-product provenance is not a supplier catalog. | The expanded BHI component rows name `Difco/BD Brain Heart Infusion`, catalog `237500`, and a Microbe Notes URL as `supplier_catalog`; the inspected URL is a third-party BHI Agar article, not a Difco/BD catalog specification for that catalog number. | `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml`. |
| Minor | Structured references are absent. | Source URLs are present only in `notes`; the generated file has no `references` block, so `linkml-reference-validator` performed zero checks. | `data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml`. |

## Recommended Edits

1. Restore `Bacto Brain Heart Infusion (Difco)` as an opaque 3.7 g/L top-level ingredient unless an inspected primary supplier sheet can support a properly scaled subcomposition.
2. Correct 17beta-Estradiol to the NBRC 1 mg/L amount.
3. Correct distilled water so NBRC's 1 L volume is not represented as grams per liter.
4. Remove the unsupported BHI `supplier_catalog` rows or replace them with a true inspected supplier catalog and scaled component concentrations.
5. Add structured references for TOGO Medium M1917, NBRC Medium 1181, and any primary commercial-product source retained after the expansion is revised.
6. Regenerate `data/merge_yaml/merged/` after the normalized owner is corrected.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml` after normalized edits.
- `just validate-references data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml` after adding structured references.
- `just verify-merges` to prove merge regeneration preserves a singleton M1917 canonical.
- `just validate-strict` and `just validate-terms` on the regenerated `1_10_brain_heart_infusion_agar_17_estradiol.yaml` merge artifact.
- Manual comparison to NBRC Medium 1181 for the 3.7 g BHI powder, 1 mg 17beta-Estradiol, 1 L water, and optional 15 g agar rows.

## Additional Notes

- A direct fetch of TOGO Medium M1917 returned only the TogoMedium JavaScript shell; the local record points to NBRC Medium 1181, and that NBRC source page resolved.
- `linkml-reference-validator` performed zero checks because the generated record has no `references` block.
