# YAML Record Review: INORGANIC SALTS-MALTOSE medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/inorganic_salts_maltose_medium.yaml
- Started UTC: 2026-09-23T15:00:05Z
- Finished UTC: 2026-09-23T15:03:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:006406 |
| Name | inorganic_salts_maltose_medium |
| Original name | INORGANIC SALTS-MALTOSE medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 7.5 |
| Source identity | KOMODO Medium 754, derived from DSMZ/MediaDive Medium 754 |
| Generated path reviewed | data/merge_yaml/merged/inorganic_salts_maltose_medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/inorganic_salts_maltose_medium.yaml |

The reviewed file is generated from the maintained KOMODO/DSMZ owner above.
Future fixes should update that normalized record, source-duplicate links to
the direct MediaDive owner, and preparation-step merging before regenerating
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/inorganic_salts_maltose_medium.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/inorganic_salts_maltose_medium.yaml --out /private/tmp/inorganic_salts_maltose_medium.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/inorganic_salts_maltose_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/inorganic_salts_maltose_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `komodo.medium:754` source term, and source notes
  identify the KOMODO import of DSMZ Medium 754.
- A gitignore-independent exact search for `CultureMech:006406` over normalized
  records, normalized indexes, and merged records found only this KOMODO owner,
  its generated merged copy, and index entries.
- A gitignore-independent exact search for `komodo.medium:754` over the same
  paths found only this KOMODO owner, its generated merged copy, and index
  entries.
- A gitignore-independent exact search for `mediadive.medium:754` found a
  separate direct DSMZ/MediaDive owner and generated record for the same source
  DSMZ medium.

## Evidence

- DSMZ and MediaDive define the recipe as 2 g peptone, 4 g yeast extract,
  980 ml inorganic salt solution, and 20 ml of a filter-sterilized 25% maltose
  solution after autoclaving.
- The KOMODO record has the correct final peptone, yeast extract, maltose,
  CaCl2 x 2 H2O, NaCl, and MgSO4 x 7 H2O quantities, but it flattens the 980 ml
  inorganic salt stock into final ingredients without naming that stock.
- DSMZ and MediaDive instruct users to adjust pH to 7.5 with KOH before
  autoclaving. The YAML extracted KOH as a variable final ingredient instead of
  preserving it only as a preparation reagent.
- DSMZ and MediaDive say to add the salts in listed order to avoid a
  precipitate, and to use 0.75% agar when agar medium is desired. The KOMODO
  record has no preparation steps and no agar note.
- A direct DSMZ/MediaDive normalized owner for `mediadive.medium:754` already
  carries the two DSMZ preparation steps, but it remains a separate generated
  record instead of being linked as the canonical source duplicate.

## Completeness

- The final major ingredients and pH are present.
- Preparation timing is incomplete: maltose must be filter-sterilized and added
  after autoclaving, while the source record does not treat KOH as a final
  culture-medium constituent.
- The inorganic salt solution boundary, salt-order instruction, and optional
  agar concentration are absent.
- Empty optional fields for synonyms, direct publication references, organism
  targets, discussions, variants, and quality flags are acceptable only after
  the source-duplicate relationship and DSMZ preparation instructions are
  represented explicitly.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ preparation steps are missing. | DSMZ/MediaDive describe pH adjustment with KOH, autoclaving, post-sterilization addition of 20 ml 25% maltose, ordered salt dissolution, and optional 0.75% agar; the KOMODO YAML has no `preparation_steps`. | `data/normalized_yaml/bacterial/inorganic_salts_maltose_medium.yaml`; KOMODO/DSMZ duplicate enrichment. |
| Major | KOH was imported as a final variable ingredient. | DSMZ uses KOH only to adjust pH to 7.5 before autoclaving; the YAML has `KOH` in `ingredients` with `VARIABLE` concentration. | `data/normalized_yaml/bacterial/inorganic_salts_maltose_medium.yaml`; pH-buffer extraction. |
| Minor | The inorganic salt solution structure is flattened. | DSMZ/MediaDive use 980 ml of an inorganic salt solution containing CaCl2, NaCl, MgSO4, and water; the YAML records the three salts directly and omits the stock name. | `data/normalized_yaml/bacterial/inorganic_salts_maltose_medium.yaml`; KOMODO/DSMZ enrichment. |
| Minor | The direct DSMZ/MediaDive duplicate is not merged. | This record is `komodo.medium:754`; `data/normalized_yaml/fungal/inorganic_salts_maltose_medium.yaml` is `mediadive.medium:754` with the same formula and DSMZ preparation steps. | Duplicate detection across KOMODO 754 and MediaDive 754. |

## Recommended Edits

1. Link the KOMODO 754 record to the direct DSMZ/MediaDive 754 record as a
   source duplicate and preserve the DSMZ preparation steps in the canonical
   merged output.
2. Move KOH out of final ingredients and keep it as a pH-adjustment reagent for
   pH 7.5.
3. Preserve the 980 ml inorganic salt solution and the post-autoclave 20 ml 25%
   maltose stock addition rather than representing only flattened final
   concentrations.
4. Add the ordered-salt dissolution instruction and optional 0.75% agar
   instruction from DSMZ.
5. Regenerate `data/merge_yaml/merged/` after the normalized sources are
   corrected.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after correcting
   the KOMODO 754 owner and source-duplicate links.
2. Diff the regenerated canonical Medium 754 record against the direct
   MediaDive owner to confirm the two DSMZ preparation steps survive merging.
3. Recompare the regenerated record to the DSMZ PDF and MediaDive 754 payload,
   checking the 20 ml 25% maltose stock and the 980 ml inorganic salt solution.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
