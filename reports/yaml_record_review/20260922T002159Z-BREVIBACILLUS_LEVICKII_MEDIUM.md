# YAML Record Review: BREVIBACILLUS LEVICKII MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml
- Started UTC: 2026-09-22T00:21:59Z
- Finished UTC: 2026-09-22T00:23:27Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml` |
| Maintained owners | `data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml`; `data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml` |
| Class | `MediaRecipe` |
| Canonical generated ID | `CultureMech:003647` |
| Duplicate parent ID | `CultureMech:000497` |
| Name | `brevibacillus_levickii_medium` |
| Source grounding | `komodo.medium:1064`, cross-linked to `mediadive.medium:1064` |
| Merge fingerprint | `66f71f273274a64789066565d3a723e19154b1bb7af40538660c8c058f2ddf3b` |

This is a generated duplicate merge of a KOMODO import and a MediaDive/DSMZ Medium 1064 import.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml` | Pass |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml --out /private/tmp/BREVIBACILLUS_LEVICKII_MEDIUM.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

The generated identity is coherent: KOMODO 1064 and MediaDive/DSMZ 1064 both denote BREVIBACILLUS LEVICKII MEDIUM, and the local duplicate metadata correctly links `CultureMech:003647` and `CultureMech:000497` as source duplicates with the same medium number and matching ingredient/concentration signature.

A gitignore-independent exact search covering `data`, `reports`, and the repository root found the two expected normalized owners, the generated merge, expected normalized indexes, old archive/import references, and the archived DSMZ/KOMODO source-duplicate review for `CultureMech:003647`, `CultureMech:000497`, `komodo.medium:1064`, `mediadive.medium:1064`, both duplicate slugs, and the merge fingerprint. Separate `find` checks under `data/normalized_yaml` confirmed that there is only one KOMODO owner and one lowercase MediaDive owner matching the live duplicate stems.

## Evidence

Supported:

- DSMZ Medium 1064 names this recipe `BREVIBACILLUS LEVICKII MEDIUM`; KOMODO 1064 is explicitly annotated in the KOMODO record as DSMZ Medium 1064.
- The generated agar state and pH 5.5 match DSMZ 1064.
- The ingredient set and all masses match the DSMZ PDF: 2 g yeast extract, 1.25 g ammonium sulfate, 1.5 g potassium dihydrogen phosphate, 2.50 mg manganese(II) sulfate monohydrate, 0.10 g magnesium sulfate heptahydrate, 12.50 mg calcium chloride dihydrate, and 18.00 g agar in 1000 ml distilled water.
- The generated `0.0025 G_PER_L` manganese salt and `0.0125 G_PER_L` calcium salt correctly convert DSMZ's milligram quantities to grams per liter.
- The ammonium sulfate, KH2PO4, MnSO4 monohydrate, MgSO4 heptahydrate, CaCl2 dihydrate, and agar CHEBI groundings are chemically appropriate.

Unsupported or over-scoped:

- `Yeast extract` remains ungrounded, although the source term itself is present.
- `notes` says `Aerobic: No` from the KOMODO import. DSMZ 1064 itself does not state an oxygen condition in the fetched PDF, so the record should not expose the KOMODO flag as if it were a DSMZ-backed growth condition without a cited KOMODO row or an explicit lower-confidence provenance note.

## Completeness

Consequential gaps:

- The generated merge has no `preparation_steps`, even though the MediaDive normalized owner still carries the DSMZ-supported instruction to adjust pH to 5.5 and autoclave at 121 C for 15 minutes.
- The generated merge does not represent the 1000 ml distilled water row from the DSMZ PDF. That is lower impact because the other concentrations have already been normalized to grams per liter.

Empty optional slots that are acceptable as empty:

- DSMZ 1064 gives no strain, temperature, atmosphere, or citation on the fetched one-page PDF. The organism and incubation-condition fields should stay empty unless another inspected source supports them.

Bounded searches:

- A gitignore-independent exact search for both CultureMech IDs, `komodo.medium:1064`, `mediadive.medium:1064`, both duplicate slugs, and `66f71f273274a64789066565d3a723e19154b1bb7af40538660c8c058f2ddf3b` covered `data`, `reports`, and the repository root. It found no third live YAML owner.
- `find data/normalized_yaml -name '*BREVIBACILLUS_LEVICKII*' -print` found only `data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml`.
- `find data/normalized_yaml -name '*brevibacillus_levickii*' -print` found only `data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml`.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*BREVIBACILLUS_LEVICKII_MEDIUM.md' -print` found no prior report with this stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated duplicate merge dropped the source preparation step. | DSMZ 1064 instructs curators to adjust pH to 5.5 and autoclave at 121 C for 15 minutes. `data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml` stores that step, but the generated merge chose the KOMODO-side record, which lacks `preparation_steps`. | `data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml`; `scripts/merge_recipes.py` |
| minor | The `Aerobic: No` note is not source-scoped tightly enough. | The note is present on the KOMODO import, but the fetched DSMZ 1064 PDF does not state an oxygen requirement and the generated record has no structured oxygen field or evidence object for the KOMODO flag. | `data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml` |

## Recommended Edits

1. Preserve the DSMZ-supported pH/autoclave instruction in the generated duplicate, either by adding the MediaDive owner `preparation_steps` to `data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml` when the KOMODO record is enriched from DSMZ 1064 or by teaching `scripts/merge_recipes.py` to merge non-conflicting preparation steps across source duplicates.
2. Add a term for `Yeast extract` if an appropriate local or ontology term is available.
3. Re-scope or remove the unstructured `Aerobic: No` note unless the KOMODO table can be cited as the source of an anaerobic flag distinct from DSMZ 1064.
4. Regenerate `data/merge_yaml/merged/BREVIBACILLUS_LEVICKII_MEDIUM.yaml` from the maintained normalized owners after curation.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch DSMZ Medium 1064 and manually compare pH, the seven ingredient amounts, water-to-concentration arithmetic, and the autoclave step.
- Repeat the gitignore-independent duplicate-owner searches for both source accessions and both CultureMech IDs to confirm the SOURCE_DUPLICATE relationship remains one-to-one.

## Additional Notes

The exact search also found `data/curation/organism_candidates.json` and `data/curation/organism_review.csv` entries for the KOMODO owner. Those rows are raw candidate/review metadata, not additional maintained YAML records.
