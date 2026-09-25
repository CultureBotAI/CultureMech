# YAML Record Review: marinitoga_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml`
- Started UTC: 2026-09-24T00:20:24Z
- Finished UTC: 2026-09-24T00:21:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002071` |
| Name | `marinitoga_medium` |
| Original name | `MARINITOGA MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:904` |
| Generated status | Generated single-source merge output from 2026-08-06 |
| Merge fingerprint | `6731fa1ed7049024a733960cead1012c6f495ee845b96f156e218dbfd32b4b6c` |
| Maintained owner | `data/normalized_yaml/bacterial/marinitoga_medium.yaml` |

The reviewed file is generated from the direct MediaDive/DSMZ 904 normalized owner. Corrections belong in `data/normalized_yaml/bacterial/marinitoga_medium.yaml`, followed by regeneration of the single-source merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml --out /private/tmp/marinitoga_medium__6731fa1e.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validators were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The record identity is internally coherent: `CultureMech:002071`, `mediadive.medium:904`, `MARINITOGA MEDIUM`, and the DSMZ Medium 904 URL all point to the pH 7.0 Marinitoga Medium formulation.
- The inspected MediaDive 904 REST payload and DSMZ Medium 904 PDF support the representative identity, the PIPES buffer, pH 7.0, and the N2/anoxic preparation instructions. This is distinct from the pH 6.0 DSMZ 904a Marinitoga Hydrogenitolerans Medium.
- Existing mapped ingredient terms are broadly aligned with the source components: PIPES, D-glucose, sodium sulfide nonahydrate, and L-cysteine hydrochloride hydrate match the named DSMZ ingredients.
- An exact gitignore-independent scan found `CultureMech:002071` and `mediadive.medium:904` only in the reviewed generated file, `data/normalized_yaml/bacterial/marinitoga_medium.yaml`, and the MediaDive source index entries.

## Evidence

- MediaDive 904 and the DSMZ 904 PDF support pH 7.0 plus the listed 30 g/L sea salt, 6 g/L PIPES, 1 g/L yeast extract, 1 g/L tryptone, 0.0005 g/L sodium resazurin, 2.5 g/L D-glucose, 0.5 g/L Na2S x 9 H2O, and 0.5 g/L L-cysteine HCl x H2O.
- The sodium resazurin conversion is dimensionally faithful: MediaDive lists 0.5 ml of 0.1% w/v sodium resazurin per 1000 ml, equivalent to 0.0005 g/L.
- The retained preparation text is source-faithful: DSMZ 904 dissolves all ingredients except glucose, sulfide, and cysteine, adjusts pH to 7.0, makes the medium anoxic under 100% N2, dispenses under the same gas phase, autoclaves, and then adds sterile anoxic stock solutions.
- The generated record omits distilled water at 1000 ml, which appears as an explicit final-volume component in both the MediaDive REST recipe and the DSMZ PDF.

## Completeness

- A gitignore-independent exact field scan over the reviewed generated record and `data/normalized_yaml/bacterial/marinitoga_medium.yaml` found `ph_value` and `preparation_steps` in both files. It found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `references`, `solutions`, `sterilization`, `parent_media`, `variant_children`, or `variant_relationship` in either exact file.
- Empty `target_organisms` and `growth_metrics` are acceptable: DSMZ 904 is a recipe source, not a growth experiment with a measured outcome.
- The absent `solutions` block is acceptable because the DSMZ source gives final medium masses for glucose, Na2S x 9 H2O, and L-cysteine HCl x H2O, not concentrations for their sterile anoxic stock solutions.
- Missing `sterilization` is a non-blocking structural gap. The autoclave action is present in `preparation_steps`, but there is no separate structured field for the autoclave procedure.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The maintained MediaDive owner and generated merge omit the explicit final-volume water component. | MediaDive 904 and the DSMZ 904 PDF list 1000 ml distilled water. `data/normalized_yaml/bacterial/marinitoga_medium.yaml` and the generated target do not include water or another final-volume representation. | Add the supported water/final-volume component to `data/normalized_yaml/bacterial/marinitoga_medium.yaml`, then regenerate `data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml`. |

No blocker findings: the YAML is valid and the record denotes the intended DSMZ 904 medium.

No minor findings found.

## Recommended Edits

1. Add distilled water at 1000 ml, or another source-faithful final-volume representation, to `data/normalized_yaml/bacterial/marinitoga_medium.yaml`.
2. Add structured sterilization metadata for the DSMZ autoclave step while preserving the existing anoxic preparation text.
3. Add `references` for the MediaDive REST endpoint and the DSMZ Medium 904 PDF.
4. Regenerate the generated merge under `data/merge_yaml/merged/`.
5. Compare this corrected MediaDive DSMZ 904 owner with the TOGO M1052 and KOMODO 904 records before adding any future source-duplicate links.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation on the corrected normalized owner and regenerated generated record.
- Run `just verify-merges` to prove `data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml` is synchronized with `data/normalized_yaml/bacterial/marinitoga_medium.yaml`.
- Re-fetch MediaDive 904 or the DSMZ Medium 904 PDF and manually compare the water, PIPES, pH 7.0, and anoxic autoclave details after the edit.

## Additional Notes

- DSMZ Medium 904 and DSMZ Medium 904a are similar but not interchangeable. DSMZ 904 uses PIPES at pH 7.0, while DSMZ 904a uses MES at pH 6.0.
- The direct MediaDive 904 copy is intentionally still separate from the TOGO M1052 Marinitoga Medium copy in this generated layer.
