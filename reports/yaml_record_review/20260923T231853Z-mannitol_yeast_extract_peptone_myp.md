# YAML Record Review: mannitol_yeast_extract_peptone_myp

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mannitol_yeast_extract_peptone_myp.yaml
- Started UTC: 2026-09-23T23:18:53Z
- Finished UTC: 2026-09-23T23:18:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003739 |
| name | mannitol_yeast_extract_peptone_myp |
| original_name | MANNITOL-Yeast extract-Peptone (MYP) |
| category | bacterial |
| categories | bacterial, fungal |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | SOLID_AGAR |
| source term | komodo.medium:1087, MANNITOL-Yeast extract-Peptone (MYP) |
| generated path | data/merge_yaml/merged/mannitol_yeast_extract_peptone_myp.yaml |
| maintained owners | data/normalized_yaml/bacterial/mannitol_yeast_extract_peptone_myp.yaml; data/normalized_yaml/fungal/mannitol_yeast_extract_peptone_myp.yaml |

The reviewed YAML is a derived merge artifact. Its terminal curation events report that the bacterial KOMODO/DSMZ owner and the fungal DSMZ owner were merged as duplicate recipes on fingerprint `ab2ae452253cfeb500ef69e651bd3d7b83707b986e00df4344a309afc8e60fce`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:003739`, `komodo.medium:1087`, `mediadive.medium:1087`, `DSMZ Medium 1087`, and `MANNITOL-Yeast extract-Peptone` found the expected bacterial KOMODO owner, fungal DSMZ owner, generated merge, and derived indexes. The same exact `mediadive.medium:1087` source ID was found on the fungal owner and as `kg_microbe_match` provenance on the KOMODO owner.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mannitol_yeast_extract_peptone_myp.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/mannitol_yeast_extract_peptone_myp.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The merged record denotes DSMZ/MediaDive Medium 1087, `MANNITOL-YEAST EXTRACT-PEPTONE (MYP)`, with a KOMODO mirror as one source owner. The bacterial and fungal normalized records contain the same four non-water components and correctly merge as duplicate source imports.

MediaDive REST and the DSMZ PDF both support:

| Ingredient | Amount |
|---|---:|
| D-Mannitol | 25.0 g |
| Yeast extract | 5.0 g |
| Peptone | 3.0 g |
| Agar | 15.0 g |
| Distilled water | 1000.0 ml |

The D-mannitol and agar CHEBI links match the DSMZ labels. Yeast extract and peptone are correctly left ungrounded.

## Evidence

The merged record correctly preserves D-mannitol, yeast extract, peptone, agar, the solid-agar state, and the cross-category duplicate merge.

The 1000 ml distilled-water row is missing from both normalized owners and from the generated merge. The water row is present in both independent inspected sources for Medium 1087: MediaDive's REST payload and DSMZ's Medium 1087 PDF.

## Completeness

Missing or incomplete:

- Add the 1000 ml distilled-water row to both normalized owners.
- Clarify duplicate provenance after merge. The generated `merged_from` list contains the same stem twice, and the merge curation event says `Sources: mannitol_yeast_extract_peptone_myp, mannitol_yeast_extract_peptone_myp`, which is ambiguous because the two owners live in different category directories.

Complete enough:

- No pH, preparation step, or stock-solution reference is present in DSMZ Medium 1087.
- The duplicate merge itself is chemically correct.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source water row is missing. | MediaDive REST for Medium 1087 and the DSMZ Medium 1087 PDF list `Distilled water` at 1000 ml; neither normalized owner nor the generated merge contains a distilled-water ingredient. | data/normalized_yaml/bacterial/mannitol_yeast_extract_peptone_myp.yaml and data/normalized_yaml/fungal/mannitol_yeast_extract_peptone_myp.yaml |
| minor | Duplicate merge provenance loses the category-qualified owner paths. | The generated `merged_from` list has two identical `mannitol_yeast_extract_peptone_myp` values because both source files share the same stem; a reader cannot distinguish the bacterial KOMODO owner from the fungal DSMZ owner from that list alone. | merge_recipes.py output for generated merge metadata |

## Recommended Edits

1. Add `Distilled water` at `1000 ML_PER_L` to both normalized owners.
2. Regenerate the merge and verify that Medium 1087 still merges across the bacterial KOMODO and fungal DSMZ owners.
3. Improve generated merge provenance for same-stem records from different category directories so `merged_from` or merge notes retain enough path context to identify both owners.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on both normalized owners and on the regenerated merged record.
- Regenerate merges and run the focused merge-freshness check or `just verify-merges` for Medium 1087.
- Re-fetch MediaDive REST and the DSMZ PDF for Medium 1087 and confirm the regenerated merge has all five ingredients.

## Additional Notes

None found.
