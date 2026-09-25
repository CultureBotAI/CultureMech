# YAML Record Review: LACTOBACILLUS medium III

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml
- Started UTC: 2026-09-23T18:25:13Z
- Finished UTC: 2026-09-23T18:25:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml` |
| Generated status | Generated canonical merge from four DSMZ Medium 638 source records; do not edit directly |
| Schema class | `MediaRecipe` |
| CultureMech ID | `CultureMech:006159` |
| Name | `lactobacillus_medium_iii` |
| Original name | `LACTOBACILLUS medium III` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Source accessions | `komodo.medium:638`, `mediadive.medium:638`, `komodo.medium:638_17896`, `komodo.medium:638_22696` |
| Merge fingerprint | `99c3c68ae1252a78754d7c21a5b191da39477240143245b6799b0fe634ac204b` |
| Maintained owners inspected | `KOMODO_638_LACTOBACILLUS_medium_III.yaml`, `lactobacillus_medium_iii.yaml`, `medium_638_modified_for_dsm_17896.yaml`, `medium_638_modified_for_dsm_22696.yaml` |

The generated target merges one DSMZ/MediaDive Medium 638 owner, one KOMODO
Medium 638 owner, and two KOMODO strain-modified Medium 638 owners with the same
ingredient signature. The source identity is coherent, but every upstream owner
omits DSMZ's 1000 ml distilled-water row and stores Tween 80's 1 ml source
amount as a mass concentration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml` | Passed; no output |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml --out /private/tmp/lactobacillus_medium_iii__99c3c68a.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:006159` identifies KOMODO Medium 638, and its `parent_media`
  points to the DSMZ/MediaDive Medium 638 owner, `CultureMech:001771`.
- Live MediaDive `/rest/medium/638` resolves to DSMZ `LACTOBACILLUS MEDIUM III`,
  pH 6.3, and the DSMZ Medium 638 PDF URL.
- The DSMZ PDF confirms the Lactobacillus Medium III identity and the same
  ingredient list represented by the generated record, except for the missing
  distilled water.
- The `medium_638_modified_for_dsm_17896` and
  `medium_638_modified_for_dsm_22696` owners also state DSMZ Medium 638
  provenance and have the same source-derived ingredient signature.
- Most hydrate-sensitive groundings are exact, including sodium acetate
  trihydrate, magnesium sulfate heptahydrate, and manganese sulfate
  tetrahydrate. `K2HPO4 x 3 H2O`, however, is grounded to an anhydrous
  dipotassium hydrogen phosphate label.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and
`reports/archive` for the four exact CultureMech IDs, the digit-bounded
KOMODO/MediaDive accessions, all four normalized filenames, and the full merge
fingerprint found only the generated target, its four normalized owners,
normalized source indexes, old validation reports, and the archived
DSMZ/KOMODO source-duplicate review.

## Evidence

Supported in inspected sources:

- DSMZ Medium 638 lists Tryptone 10 g, Meat extract 5 g, Yeast extract 5 g,
  Glucose 7 g, Fructose 7 g, Maltose 7 g, Na-gluconate 2 g,
  Na-acetate x 3 H2O 5 g, ammonium citrate 2 g, K2HPO4 x 3 H2O 2.6 g,
  MgSO4 x 7 H2O 0.10 g, MnSO4 x 4 H2O 0.05 g, Cysteine-HCl x H2O 0.50 g,
  Tween 80 1 ml, and Distilled water 1000 ml, followed by adjustment to pH 6.3.
- MediaDive `/rest/medium/638` reports the same formula, pH 6.3, and the same
  1000 ml main-solution volume.
- The four merged normalized source records all have the same 14 non-water
  component signature, supporting the generated duplicate merge by fingerprint.

Unsupported or stale in the generated target:

- Distilled water is absent from all four normalized owners and from the
  generated merge, despite appearing in DSMZ and MediaDive as 1000 ml.
- `Tween 80` is stored as `1 G_PER_L`; DSMZ and MediaDive report 1 ml.
- The generated target has `ph_value: 6.3` but no preparation step for the DSMZ
  pH adjustment, even though the DSMZ/MediaDive owner carries it.
- `K2HPO4 x 3 H2O` uses an anhydrous `CHEBI:131527` grounding.
- The target has no `references` list for the DSMZ PDF or the MediaDive 638
  REST record.

## Completeness

Consequential gaps:

- Distilled water is missing from the recipe.
- Tween 80 needs volume-aware quantity handling.
- The K2HPO4 trihydrate row needs hydrate-specific grounding.
- DSMZ pH adjustment should be preserved in the merge output.
- Source references are absent.

Empty or absent fields that are not defects for this generated DSMZ recipe:

- `target_organisms`, growth metrics, genome assembly, atmospheric conditions,
  storage, and shelf-life fields can remain empty without strain-level evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Major | DSMZ/MediaDive water is missing from all merged owners. | DSMZ Medium 638 and MediaDive medium 638 both include Distilled water 1000 ml; none of the four normalized owners or the generated target contains a water row. | The four normalized owners, or their shared DSMZ/KOMODO import enrichment path if water omission is systemic. |
| Major | Tween 80 is represented as a mass concentration. | DSMZ and MediaDive report Tween 80 as 1 ml; the generated target stores `1 G_PER_L`. | The four normalized owners. |
| Major | `K2HPO4 x 3 H2O` is grounded to an anhydrous term. | The source label explicitly includes `x 3 H2O`, while the record's term label is `dipotassium hydrogen phosphate` without trihydrate specificity. | The four normalized owners. |
| Major | The generated merge loses source preparation detail. | DSMZ says to adjust pH to 6.3 and the DSMZ/MediaDive owner has that preparation step; the KOMODO-canonical generated merge does not. | Preserve parent preparation metadata in `src/culturemech/merge/merge_recipes.py` or copy the pH step into every normalized source duplicate. |
| Major | Source references are absent from generated and normalized records. | The records carry source URLs in free-text notes only; no `references` list points to DSMZ Medium 638 or MediaDive medium 638. | All normalized Medium 638 owners. |

## Recommended Edits

1. Add the DSMZ/MediaDive 1000 ml distilled-water row to the DSMZ/MediaDive
   owner and propagate the same source-corrected component to the three KOMODO
   Medium 638 owners.
2. Correct Tween 80 so its 1 ml source amount is not represented as `G_PER_L`.
3. Re-ground or de-ground `K2HPO4 x 3 H2O`; do not keep an anhydrous primary
   term on a trihydrate source label.
4. Preserve the pH 6.3 adjustment and DSMZ/MediaDive references across the
   four-way duplicate merge.
5. Regenerate `data/merge_yaml/merged/` and verify that
   `lactobacillus_medium_iii__99c3c68a.yaml` still merges only the four DSMZ 638
   source records.

## Follow-up Checks

- Rerun the focused open, strict, reference, and term validators against all
  four normalized owners after the water, Tween 80, K2HPO4, pH, and reference
  edits.
- Re-query the DSMZ Medium 638 PDF and MediaDive `/rest/medium/638` to confirm
  all ingredient amounts and the pH adjustment.
- Run `just merge-recipes`, then rerun the focused validators against
  `data/merge_yaml/merged/lactobacillus_medium_iii__99c3c68a.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm this generated
  file is not drifted.
- Search with ignored files included for exact `komodo.medium:638`,
  `komodo.medium:638_17896`, `komodo.medium:638_22696`, and
  `mediadive.medium:638` to confirm the intended source-duplicate set remains.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe
  schema section, the generated target, all four normalized owners, live
  MediaDive medium 638, and the DSMZ Medium 638 PDF.
- The two DSM-number-specific KOMODO rows are currently exact recipe duplicates
  rather than source-supported formulation variants; their names are retained as
  synonyms in the generated merge.
