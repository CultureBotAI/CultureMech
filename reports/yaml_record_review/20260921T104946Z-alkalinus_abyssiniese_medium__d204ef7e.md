# YAML Record Review: ALKALINUS ABYSSINIESE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml
- Started UTC: 2026-09-21T10:48:33Z
- Finished UTC: 2026-09-21T10:49:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003323` |
| Name | `alkalinus_abyssiniese_medium` |
| Original name | `ALKALINUS ABYSSINIESE MEDIUM` |
| Category | `bacterial` |
| Generated status | Generated merge from one maintained normalized source |
| Maintained owner | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` |
| Upstream source | JCM GRMD `974` through the direct MediaDive/JCM import |
| Merge fingerprint | `d204ef7e6256f7070a11b53fb90f3a3aa32d43eb8d8060bcf5e1ac097affe028` |

The target is a generated merge of the direct JCM J974 normalized parent. Its
future fix belongs in that maintained parent or in the direct MediaDive/JCM
import that produced `data/normalized_yaml/bacterial/mediadive_4997_Main_sol_J974.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml --out /private/tmp/alkalinus_abyssiniese_medium__d204ef7e.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning |
| Embedded curation history | Not checked | No focused validator is documented for embedded `MediaRecipe.curation_history`; `just validate-history` validates standalone files under `history/` |

The usual `just` wrappers were not rerun here because target-specific `just
validate-schema`, `just validate-strict`, and `just validate-terms` currently
fail before target validation while the project `uv` environment attempts to
build `llvmlite==0.46.0` under Python 3.13. The no-project validator commands
above use Python 3.11 and the cached validator packages instead.

## Identity and Grounding

The record identity points to JCM Medium J974 and its GRMD 974 URL, and the
single `merged_from` value resolves to
`data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml`. Live JCM
GRMD 974 now returns `Nothing found`; TOGO M1025 and M1026 are recoverable
snapshots of the same source family and were used to judge the JCM 974
formulation and stock scopes.

The exact ignored-files-including search:

```bash
rg -n "d204ef7e|CultureMech:003323|J974|GRMD=974|JCM Medium J974" data/normalized_yaml/bacterial data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml --glob '*.yaml' --no-ignore --hidden
```

found the intended parent, this generated merge, its MediaDive `Main sol. J974`
solution source, the related TOGO M1025/M1026 snapshots, and one unrelated
`CultureMech:002474` hit in `thiorhodovibrio_medium.yaml` from the broad
numeric ID pattern. It found no prior exact report for
`alkalinus_abyssiniese_medium__d204ef7e`.

CHEBI grounding is mostly compatible for the named salts. The NiCl2 x 6H2O row
is still grounded to anhydrous nickel dichloride and should either be corrected
to a verified hexahydrate term or left unresolved.

## Evidence

The maintained normalized parent and `mediadive_4997_Main_sol_J974` both show
the same direct-import arithmetic: the MediaDive solution says `Original
volume: 115 mL`, and the generated medium scales the 900 ml base components to
that 115 ml volume. That is not the source recipe volume; 115 ml is the sum of
the three post-autoclave additions from TOGO M1025/M1026: 10 ml trace-mineral
stock, 100 ml 10% Na2CO3, and 5 ml 10% glucose.

The recoverable TOGO snapshots show the base recipe uses 900 ml distilled water
with 117 g NaCl, 5 g yeast extract, 5 g peptone, 0.2 g MgSO4 x 7H2O, 0.2 g
CaCl2 x 2H2O, and 0.1 g KH2PO4 before adding the three separately autoclaved
stock solutions. The generated record has no water and reports the base
ingredients as 1017.39, 43.4783, 43.4783, 1.73913, 1.73913, and
0.869565 g/L because of the erroneous 115 ml denominator.

The trace minerals are stock ingredients from M1025, not final-medium
ingredients. The direct J974 import lists them at their stock recipe
concentrations in the final medium and omits the fact that only 10 ml of that
stock is added to the 900 ml base.

The generated `Glucose` and `Na2CO3` rows are flattened from 5 ml and 100 ml
10% stock additions. They are not source rows added directly as 5 g/L glucose
and 100 g/L sodium carbonate in the basal medium.

The preparation text is present, but all operations are collapsed into one
`AUTOCLAVE` step. The source distinguishes base autoclaving, cooling, separate
stock autoclaving, and aseptic addition after cooling.

No claim-level `evidence` objects or structured `references` are present. The
JCM URL is retained only as free text in `notes`.

## Completeness

Consequential gaps:

- The 900 ml source water row is missing entirely.
- Base ingredient concentrations use the wrong 115 ml denominator.
- Three post-autoclave stock additions are flattened as top-level final
  ingredients.
- Trace-mineral stock ingredients are inlined as final-medium ingredients.
- Separate stock boundaries, stock volumes, and the M1025 trace-mineral stock
  reference are missing.
- Preparation is collapsed into a single autoclave step.
- The optional 20 g/L agar solid formulation in the preparation text is not
  modeled as a variant.
- JCM provenance is not structured, and the live JCM page is no longer a source
  of recoverable tabular formulation data.

Empty optional slots that are not automatic defects:

- `target_organisms` and `growth_metrics` can remain empty because the inspected
  TOGO snapshots are formulation/protocol records.
- Undefined yeast extract and peptone can remain ungrounded.

The prior-report search:

```bash
find reports/yaml_record_review -name '*alkalinus_abyssiniese_medium__d204ef7e*' -print
```

included ignored report files and found no existing report for this exact
generated record before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The base medium was scaled to 115 ml instead of the 900 ml base/final formulation. NaCl, yeast extract, peptone, MgSO4 x 7H2O, CaCl2 x 2H2O, and KH2PO4 are therefore inflated roughly 8.7-fold. | `mediadive_4997_Main_sol_J974.yaml` records `Original volume: 115 mL`; TOGO M1025/M1026 show 115 ml is only the sum of 10 ml + 100 ml + 5 ml stock additions. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_4997_Main_sol_J974.yaml`, or the direct JCM/MediaDive importer |
| Major | Water is missing. The source base starts from 900 ml distilled water, but the generated record has no water row. | TOGO M1025/M1026 both list 900 ml distilled water in the base. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml`, or the direct JCM/MediaDive importer |
| Major | Stock additions were flattened. Glucose, Na2CO3, and every trace-mineral stock component are represented as final-medium ingredients instead of preserving 5 ml 10% glucose, 100 ml 10% Na2CO3, and 10 ml M1025 trace-mineral stock additions. | TOGO M1025/M1026 preserve those stock additions and the M1025 trace-mineral stock boundary. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml`, or the direct JCM/MediaDive importer |
| Major | Preparation structure is incomplete. The generated record has one `AUTOCLAVE` step that also describes post-autoclave stock additions, but it does not model cooling, separate stock autoclaving, or aseptic addition. | TOGO M1025/M1026 state those operations in the preparation comment. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` |
| Major | The NiCl2 x 6H2O ingredient is grounded to anhydrous nickel dichloride. | The source stock specifies the hexahydrate. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` |
| Minor | The optional 20 g/L agar solid formulation is present only as prose. | The preparation text mentions 20 g/L agar for solid medium, but the record is only the liquid form. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` |
| Minor | JCM provenance is free-text only and the live JCM GRMD 974 URL now returns no formulation table. | The source URL is in `notes`; fetching JCM GRMD 974 returned `Nothing found`. | `data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` |

No blocker findings were found.

## Recommended Edits

1. Rebuild the recipe from the JCM/TOGO source structure instead of the
   MediaDive 115 ml denominator: restore the 900 ml base, base masses, and
   separate 10 ml/100 ml/5 ml stock additions.
2. Represent M1025 trace minerals as a referenced stock addition rather than
   final-medium ingredients.
3. Represent 10% glucose and 10% Na2CO3 as stock additions rather than direct
   final-medium glucose and sodium-carbonate rows.
4. Split the preparation text into distinct base autoclaving, cooling, separate
   stock autoclaving, and aseptic-addition steps.
5. Remove or correct the anhydrous nickel dichloride term from `NiCl2 x 6H2O`.
6. Move JCM GRMD 974 provenance into structured source/reference fields and
   note that the live JCM page now returns no table.
7. Regenerate `data/merge_yaml/merged/alkalinus_abyssiniese_medium__d204ef7e.yaml`
   and generated pages from the maintained source.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` after correcting the nickel salt and stock structure.
- Run `just validate-references data/normalized_yaml/bacterial/alkalinus_abyssiniese_medium.yaml` after adding structured JCM/TOGO provenance.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
- Manually compare the regenerated direct J974 record to TOGO M1025/M1026 for
  the base denominator, 900 ml water, 10 ml trace-mineral addition, 100 ml
  carbonate addition, 5 ml glucose addition, and autoclave/cool/aseptic-add
  procedure.

## Additional Notes

- This direct J974 record should become source-equivalent to the TOGO
  M1025/M1026 pair but not necessarily identical: the TOGO pair keeps separate
  liquid and solid records, while this parent currently imports only one direct
  JCM recipe.
- The `mediadive_4997_Main_sol_J974.yaml` solution record is a useful focused
  place to test the denominator repair because it contains the explicit
  `Original volume: 115 mL` clue.
