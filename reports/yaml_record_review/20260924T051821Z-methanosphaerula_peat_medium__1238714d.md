# YAML Record Review: METHANOSPHAERULA (PEAT) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml
- Started UTC: 2026-09-24T05:16:24Z
- Finished UTC: 2026-09-24T05:18:21Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml`, a generated `MediaRecipe` for `CultureMech:000525` with `name: methanosphaerula_peat_medium`, `original_name: METHANOSPHAERULA (PEAT) MEDIUM`, and medium grounding `mediadive.medium:1094`.

The record was merged from two normalized duplicate inputs:

- `data/normalized_yaml/archaea/methanosphaerula_peat_medium.yaml`, imported from DSMZ/MediaDive 1094.
- `data/normalized_yaml/archaea/methanosphaerula_medium.yaml`, imported from KOMODO 1094 and enriched with DSMZ 1094 ingredient data.

Future ingredient, preparation, and duplicate-link fixes belong in those maintained inputs and, for repeated stock-flattening errors, in the DSMZ/MediaDive import path that created the flat ingredients.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml --out /private/tmp/methanosphaerula_peat_medium__1238714d.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The DSMZ identity is correct: `mediadive.medium:1094` is DSMZ medium 1094, `METHANOSPHAERULA (PEAT) MEDIUM`, with final pH 5.7 and source PDF `DSMZ_Medium1094.pdf`.

The KOMODO source duplicate also resolves to DSMZ medium 1094, but its normalized `notes` say `Aerobic: Yes`, which conflicts with DSMZ 1094's explicitly anoxic N2/CO2, N2, and H2/CO2 handling. That contradictory KOMODO flag was not propagated into the merged record's top-level `notes`, but the duplicate source should not keep an aerobic classification for this methanogen medium.

## Evidence

Supported source claims:

- The ID, DSMZ name, `mediadive.medium:1094` grounding, pH 5.7, and DSMZ source URL match MediaDive medium 1094 and the DSMZ 1094 PDF.
- The three main preparation paragraphs, Solution C pH 7.5 adjustment, and trace-element stock pH 7 instructions all come from MediaDive/DSMZ text.
- The merged-from pair is a real duplicate lineage: the DSMZ/MediaDive record and the KOMODO record both point at DSMZ 1094.

Unsupported or over-scoped generated claims:

- The record treats all DSMZ 1094 solution children as top-level ingredients. DSMZ 1094 is a nested formulation with a final medium made from Solution A-G; Solution A contains 0.1% salt stocks plus 1 ml trace stock; Solution D contains 1 ml Wolin 10x vitamin stock; and Solutions E-G are separate 10 ml anoxic stocks.
- Several generated `G_PER_L` values are the MediaDive concentration within a stock solution, not the final medium. The trace-element rows, such as `Na2-EDTA: 37.23 G_PER_L`, and Wolin vitamin rows, such as `Pyridoxine hydrochloride: 0.1 G_PER_L`, are stock concentrations that should be diluted through their parent stocks before any final concentration is asserted.
- Several liquid stock volumes are not masses at all. `Tris-HCl buffer: 7.2 G_PER_L` is sourced from 7.2 ml of 1.0 M buffer in Solution B, and the source supplies no gram mass for that buffer row.
- Water rows and final Solution A-G amounts are absent. Following the record as written would omit the source solvents and the actual final assembly from 943 ml Solution A, 13 ml Solution B, 20 ml Solution C, 1 ml Solution D, 10 ml Solution E, 10 ml Solution F, and 10 ml Solution G.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; the evidence, discussion, and growth omissions are not defects by themselves for this imported medium.

Consequential gaps:

- The empty `solutions` array is consequential because the DSMZ source is explicitly stock-based.
- The record loses MediaDive solution IDs 2201-2208 and 5980 for Solution A-G, the trace element stock, and Wolin's vitamin solution.
- The preparation steps are present but no longer scoped to their solutions. Solution C's pH step and the trace-element preparation were appended after the final-medium inoculation and storage warnings, rather than remaining inside Solution C and the trace element stock.
- Duplicate metadata points to stale bacterial paths. A gitignore-independent `find` over `data/normalized_yaml` found `data/normalized_yaml/archaea/methanosphaerula_medium.yaml` and `data/normalized_yaml/archaea/methanosphaerula_peat_medium.yaml`, but did not find the referenced `data/normalized_yaml/bacterial/methanosphaerula_medium.yaml` or `data/normalized_yaml/bacterial/methanosphaerula_peat_medium.yaml` paths.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The merged record contains a broken duplicate path reference. | `parent_media.path` names `data/normalized_yaml/bacterial/methanosphaerula_medium.yaml`; `find data/normalized_yaml` found only the `archaea/` records for both duplicate inputs. The sibling normalized record also points at `data/normalized_yaml/bacterial/methanosphaerula_peat_medium.yaml`. | `data/normalized_yaml/archaea/methanosphaerula_peat_medium.yaml` and `data/normalized_yaml/archaea/methanosphaerula_medium.yaml`; duplicate relationship generation. |
| Major | The DSMZ stock hierarchy was flattened into top-level ingredients. | DSMZ/MediaDive 1094 has Solution A-G, a trace element stock nested under Solution A, and a Wolin 10x stock nested under Solution D. The generated YAML has only final top-level `ingredients` and no `solutions`. | Both normalized inputs; DSMZ/MediaDive importer and KOMODO DSMZ enrichment. |
| Major | Stock concentrations and liquid volumes were misrepresented as final `G_PER_L` ingredient concentrations. | Trace salts and vitamins keep their stock `g_l` values; Tris-HCl keeps a 7.2 ml amount as `7.2 G_PER_L`; and Solution C/E/F/G chemicals keep their 20 ml or 10 ml stock concentrations instead of being scoped to stocks or diluted into the final 1007 ml. | Both normalized inputs; DSMZ/MediaDive importer and concentration mapping. |
| Major | Source solvent and final assembly rows are missing. | DSMZ 1094 specifies 943 ml Solution A, 13 ml Solution B, 20 ml Solution C, 1 ml Solution D, 10 ml each Solution E-G, and water rows for Solution A, Solution C, the trace stock, the Wolin stock, and Solutions E-G. None of those rows survive as scoped solution additions. | Both normalized inputs; DSMZ/MediaDive importer and solution support. |
| Major | Preparation steps lost stock scope and executable order. | Solution C and trace-element preparation are nested under separate MediaDive solutions, but the record appends them after the final-medium anoxic preparation, H2/CO2 pressurization, and short-stability note. | Both normalized inputs; DSMZ/MediaDive preparation importer. |
| Minor | The KOMODO duplicate carries an anaerobe-inconsistent aerobic flag. | `data/normalized_yaml/archaea/methanosphaerula_medium.yaml` says `Aerobic: Yes`; DSMZ 1094 requires anoxic Solution A, N2-prepared stocks, and H2/CO2 overpressure after inoculation. | `data/normalized_yaml/archaea/methanosphaerula_medium.yaml`; KOMODO import or DSMZ resolver enrichment. |

## Recommended Edits

1. Fix the duplicate relationship paths in the two normalized records so they point at the existing `archaea/` paths, or regenerate those paths from the current category.
2. Rework the DSMZ/MediaDive import for medium 1094 to preserve Solution A-G, Trace element solution, and Wolin's vitamin solution as solution records with MediaDive solution IDs 2201-2208 and 5980.
3. Keep source liquid volumes and stock concentrations scoped to the source rows instead of copying MediaDive helper `g_l` fields into final top-level ingredient concentrations.
4. Retain the final assembly from Solution A-G and every stock water row inside its parent solution.
5. Move the Solution C and trace-element pH/preparation steps back under their stock solutions, while keeping the three main-medium preparation and stability steps at the final-medium level.
6. Correct or remove the unsupported `Aerobic: Yes` KOMODO note for `methanosphaerula_medium`.
7. Regenerate `data/merge_yaml/merged/methanosphaerula_peat_medium__1238714d.yaml` after the maintained records and import mapping are fixed.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated merged record.
- Run a gitignore-independent search for the stale `data/normalized_yaml/bacterial/methanosphaerula_medium.yaml` and `data/normalized_yaml/bacterial/methanosphaerula_peat_medium.yaml` strings and confirm they are gone or explicitly archived.
- Compare the regenerated solution tree to MediaDive medium 1094 and verify that rows from Solution A-G, the trace element stock, and Wolin's vitamin solution remain in the same parent scopes.
- Manually confirm no top-level ingredient retains a raw per-stock `g_l` helper value from MediaDive.

## Additional Notes

- Empty optional evidence, discussion, and growth fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, and the path existence check used `find`, so ignored files were included when resolving `CultureMech:000525` and the two normalized duplicate inputs.
