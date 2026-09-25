# YAML Record Review: DESULFOHALOBIUM medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.yaml
- Started UTC: 2026-09-22T18:45:53Z
- Finished UTC: 2026-09-22T18:50:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:005632 |
| Name | desulfohalobium_medium |
| Original name | DESULFOHALOBIUM medium |
| Media term | komodo.medium:499, KOMODO Medium 499 |
| Source | KOMODO 499, enriched from DSMZ Medium 499 |
| Category | bacterial |
| Generated status | Generated canonical merge in `data/merge_yaml/merged/`; do not edit directly |
| Maintained canonical source chosen by merge | `data/normalized_yaml/bacterial/KOMODO_499_DESULFOHALOBIUM_medium.yaml` |
| Maintained DSMZ duplicate parent | `data/normalized_yaml/bacterial/desulfohalobium_medium.yaml` |
| Merge fingerprint | 2d1ac1fa6af4c4230be2b46f6fa8bc8f28749af8f2061329975d281e12a4948d |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.yaml --out /private/tmp/desulfohalobium_medium__2d1ac1fa.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run printed the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` equivalent | Not checked: the documented history validator validates standalone `history/*.yaml` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The generated record has the formula for DSMZ Medium 499, but the canonical identity is the lower-authority KOMODO source duplicate. The record's ID, accession, original label, and notes identify `komodo.medium:499`; its own `parent_media` says that this KOMODO record is a `SOURCE_DUPLICATE` of `data/normalized_yaml/bacterial/desulfohalobium_medium.yaml`, which is the direct DSMZ/MediaDive import for `mediadive.medium:499`.

MediaDive medium 499 and the DSMZ Medium 499 PDF confirm the recipe identity, DSMZ source, complex/undefined formulation, pH 7.0, 1002 ml MediaDive final volume, and the 1 ml additions of Trace element solution SL-10 and Selenite-tungstate solution. The major salts, acetate, peptone, yeast extract, L-lactate, resazurin, and sulfide quantities in the generated record are source-supported.

## Evidence

The two merged normalized records are an exact ingredient/concentration duplicate pair, and the KOMODO child truthfully records DSMZ Medium 499 provenance. However, picking the KOMODO child as the canonical generated record discards the DSMZ parent's inspected preparation steps. The generated record has no `preparation_steps`, while the DSMZ parent says to sparge with 100% N2, adjust pH to 6.8-7.0 before dispensing and autoclaving, add sulfide from a sterile anoxic stock, adjust the complete medium to pH 7.0 if needed, and tolerate the small white precipitate after autoclaving.

The generated record has no `solutions` block. HCl through Na2MoO4 x 2 H2O are the ingredients of Trace element solution SL-10, and NaOH through Na2WO4 x 2 H2O are the ingredients of Selenite-tungstate solution; DSMZ and MediaDive add those stocks to the final medium as 1 ml solution rows rather than as final-medium ingredient rows.

The generated ingredient labels also omit two brand attributes from the source: `Trypticase peptone (BD BBL)` and `Yeast extract (OXOID)`.

## Completeness

The final medium is missing two structured stock additions and both stock compositions. That also means the SL-10 stock-specific HCl/FeCl2 preparation instruction present in the DSMZ normalized parent has no correct solution target in the generated canonical.

The record correctly leaves explicit target-organism growth evidence empty because the inspected DSMZ and MediaDive recipe sources do not report an organism growth experiment.

Gitignore-independent `rg --no-ignore --hidden` over normalized YAML, merge YAML, import-tracking reports, the ID registry, and the recipe catalog found the chosen KOMODO record, the DSMZ/MediaDive parent, related TOGO/JCM Desulfohalobium records, the generated merge products, and concentration-plausibility warnings for the FeCl2 x 4 H2O stock ingredient. A `find` under `data/normalized_yaml/bacterial` also found the Desulfohalobium source files without honoring `.gitignore`. A `find` under `reports/yaml_record_review` found no pre-existing review report for `desulfohalobium_medium__2d1ac1fa`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The merge chose the KOMODO duplicate as the generated canonical identity even though that normalized record says it is a source duplicate of the DSMZ/MediaDive parent. | Generated `CultureMech:005632` carries `komodo.medium:499` and `parent_media` pointing to `CultureMech:001626`; the DSMZ normalized parent carries `mediadive.medium:499`, the DSMZ PDF URL, and the final-medium preparation instructions. | Merge priority in the generator and/or normalized duplicate links for `data/normalized_yaml/bacterial/KOMODO_499_DESULFOHALOBIUM_medium.yaml` and `data/normalized_yaml/bacterial/desulfohalobium_medium.yaml`. |
| Major | Trace element solution SL-10 and Selenite-tungstate solution are flattened into final-medium chemicals. | DSMZ and MediaDive list 1 ml of each stock in the final recipe; the generated YAML lists the SL-10 and selenite-tungstate stock contents directly as top-level ingredients and has no `solutions` block. | `data/normalized_yaml/bacterial/desulfohalobium_medium.yaml`; mirror or regenerate `data/normalized_yaml/bacterial/KOMODO_499_DESULFOHALOBIUM_medium.yaml` after repair. |
| Major | The generated canonical record omits all final-medium preparation details. | DSMZ and MediaDive provide anaerobic N2 sparging, pH adjustment, autoclaving, sulfide addition, and precipitate notes; the generated KOMODO-canonical record has no `preparation_steps`. | Prefer the DSMZ parent during merge or copy source-supported preparation into the authoritative DSMZ normalized record before regeneration. |
| Minor | Two source ingredient attributes are dropped. | MediaDive records `Trypticase peptone` with `BD BBL` and `Yeast extract` with `OXOID`; the generated YAML only stores the generic ingredient names. | `data/normalized_yaml/bacterial/desulfohalobium_medium.yaml` if the schema has a maintained way to preserve supplier attributes. |

## Recommended Edits

1. Change duplicate merge priority so the DSMZ/MediaDive record `CultureMech:001626` remains canonical and `CultureMech:005632` stays a `SOURCE_DUPLICATE` child, then regenerate the merged record.
2. In the DSMZ normalized parent, replace the flattened SL-10 and Selenite-tungstate ingredient rows with 1 ml solution additions and modeled stock compositions.
3. Move the SL-10-specific FeCl2/HCl dissolution step onto the SL-10 stock solution and keep the N2/autoclave/sulfide/pH/precipitate step on the final medium.
4. Rebuild or mirror the KOMODO duplicate from the repaired DSMZ parent so it no longer carries stock components as final ingredients.
5. Preserve `BD BBL` and `OXOID` as supplier attributes if the schema has a durable field for MediaDive compound attributes.
6. Regenerate `data/merge_yaml/merged/desulfohalobium_medium__2d1ac1fa.yaml`.

## Follow-up Checks

1. Re-run open-schema, strict, reference, and term validation on both repaired normalized records and the regenerated merged canonical record.
2. Re-run merge verification to confirm DSMZ Medium 499 remains canonical over KOMODO 499.
3. Re-run concentration-plausibility reporting for `CultureMech:001626` and `CultureMech:005632`; the FeCl2 x 4 H2O `TRACE_SALT_AS_STOCK` rows should disappear.
4. Manually compare the regenerated record to DSMZ Medium 499 and MediaDive medium 499 for the pH 7.0 target, direct final-medium ingredients, two 1 ml stock additions, anaerobic preparation, sulfide addition, and SL-10 preparation boundary.

## Additional Notes

There are separate TOGO and JCM Desulfohalobium records in the normalized corpus and generated merge directory. They were discovered with ignored files included, but this review did not audit those non-merged records because `desulfohalobium_medium__2d1ac1fa.yaml` only merges KOMODO 499 with the DSMZ/MediaDive parent.
