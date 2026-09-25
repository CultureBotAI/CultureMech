# YAML Record Review: marinithermus_hydrothermalis_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marinithermus_hydrothermalis_medium__51a2d5de.yaml
- Started UTC: 2026-09-24T00:13:39Z
- Finished UTC: 2026-09-24T00:14:39Z
- Verdict: needs curation

## Target

- Reviewed generated record:
  `data/merge_yaml/merged/marinithermus_hydrothermalis_medium__51a2d5de.yaml`
- Maintained upstream owner:
  `data/normalized_yaml/bacterial/TOGO_M2295_Marinithermus_Hydrothermalis_Medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:008881`
- Source identity: `TOGO:M2295`
- Source label: `Marinithermus Hydrothermalis Medium`
- DSMZ source URL in TOGO: `DSMZ_Medium973.pdf`
- Generated status: single-source merge of
  `TOGO_M2295_Marinithermus_Hydrothermalis_Medium.yaml`.

## Validation

| Check | Result |
|---|---|
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinithermus_hydrothermalis_medium__51a2d5de.yaml` | Passed; printed `No issues found`. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinithermus_hydrothermalis_medium__51a2d5de.yaml --out /private/tmp/marinithermus_hydrothermalis_medium__51a2d5de.strict.tsv --workers 1 --quiet` | Passed; summary reported 1 scanned file, 0 files with errors, and 0 total error rows. The TSV had one header line only. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinithermus_hydrothermalis_medium__51a2d5de.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total reference checks. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinithermus_hydrothermalis_medium__51a2d5de.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository's `just validate-history` target validates standalone files under `history/`, not embedded recipe events. |

## Identity and Grounding

- TOGO `M2295`, MediaDive REST medium 973, and the DSMZ Medium 973 PDF all
  identify the source as `MARINITHERMUS HYDROTHERMALIS MEDIUM`.
- The normalized TOGO copy has the right source identity but the wrong
  representation: TOGO embedded the DSMZ main solution and trace solution in one
  payload, and later cleanup summed same-named components across those two
  different solution scopes.
- `mediadive.medium:973` (`CultureMech:002155`) and `komodo.medium:973`
  (`CultureMech:006931`) are already linked as source duplicates for the same
  DSMZ medium. The reviewed TOGO record is not linked to that group.
- `MgSO4 x 7 H2O` has a correct primary term, `CHEBI:31795`, but its companion
  `mediaingredientmech_chebi_term` is stale and still points to generic
  `CHEBI:32599`/magnesium sulfate.

## Evidence

- Supported:
  - DSMZ supports the main-solution identity, pH 7.0, 1 g yeast extract, 1 g
    tryptone, 30 g NaCl, 0.14 g K2HPO4, 0.14 g CaCl2 x 2 H2O, 0.25 g NH4Cl,
    3.4 g MgSO4 x 7 H2O, 4.18 g MgCl2 x 6 H2O, 0.33 g KCl, 0.5 mg NiCl2 x 6
    H2O, 0.5 mg Na2Se3 x 5 H2O, 10 mg Fe(NH4)2(SO4)2 x 6 H2O, 10 ml trace
    element solution, and 990 ml distilled water.
  - MediaDive REST medium 973 expands the trace element solution as `Modified
    Wolin's mineral solution II`; those stock components match the additional
    chemicals present in the reviewed TOGO record.
- Unsupported or misrepresented:
  - Root quantities for water, MgSO4 x 7 H2O, NaCl, CaCl2 x 2 H2O, and NiCl2 x
    6 H2O are sums across the final medium and its trace stock. For example,
    DSMZ Medium 973 has 3.4 g/l MgSO4 x 7 H2O in the final recipe and 3 g/l in
    Modified Wolin's mineral solution II, but the record stores 6.4 g/l as if
    both masses were in the final medium.
  - Small main-medium ingredients were scaled from milligrams to grams before
    summing: the source has 0.5 mg/l NiCl2 x 6 H2O, 0.5 mg/l Na2Se3 x 5 H2O,
    and 10 mg/l Fe(NH4)2(SO4)2 x 6 H2O, while the record stores 0.53, 0.5, and
    10 `G_PER_L`, respectively.
  - The trace solution chemistry is duplicated as root medium chemistry even
    though the final recipe calls for 10 ml of the stock per liter.
  - The `KOH` variable ingredient belongs to Modified Wolin's mineral solution
    II pH adjustment, not to the final Marinithermus medium as a root component.

## Completeness

- The record is not complete as a final medium recipe because final-medium
  ingredients and trace-stock ingredients are conflated.
- The linked `mediadive.solution:6187` placeholder keeps the trace solution
  accession, but the record also expands that solution at the wrong hierarchy.
- The relationship to the existing MediaDive/KOMODO DSMZ 973 source-duplicate
  group is missing.
- Empty target-organism and growth-metric slots are acceptable for this source
  recipe because the inspected TOGO, DSMZ, and MediaDive records do not assert
  primary growth evidence.
- A gitignore-independent exact scan of the reviewed normalized and merged YAML
  files found no `sources`, `source_data`, `references`, `target_organisms`,
  `growth_metrics`, `parent_media`, `variant_children`, or
  `variant_relationship` fields in the current TOGO target.
- A gitignore-independent exact scan of normalized indexes and exact sibling
  paths found the existing MediaDive `CultureMech:002155` and KOMODO
  `CultureMech:006931` records for DSMZ Medium 973.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Main-medium quantities were summed with trace-stock quantities. | The record stores 1990 g/l water, 6.4 g/l MgSO4 x 7 H2O, 31 g/l NaCl, 0.24 g/l CaCl2 x 2 H2O, and 0.53 g/l NiCl2 x 6 H2O after merging main-solution and Modified Wolin's mineral solution II values. DSMZ calls for 10 ml/l of the trace stock, not full-strength addition of those stock components. | `data/normalized_yaml/bacterial/TOGO_M2295_Marinithermus_Hydrothermalis_Medium.yaml`; if recurring, fix TOGO nested-solution import and duplicate cleanup. |
| major | Several milligram components were scaled as grams. | DSMZ lists 0.5 mg NiCl2 x 6 H2O, 0.5 mg Na2Se3 x 5 H2O, and 10 mg Fe(NH4)2(SO4)2 x 6 H2O in the main solution; the record stores numeric values `0.53`, `0.5`, and `10` as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M2295_Marinithermus_Hydrothermalis_Medium.yaml`. |
| major | The trace stock pH reagent is a root final-medium ingredient. | `KOH` appears as a variable root ingredient, but TOGO and MediaDive place KOH only in the trace solution preparation text for pH adjustment. | `data/normalized_yaml/bacterial/TOGO_M2295_Marinithermus_Hydrothermalis_Medium.yaml`. |
| major | The TOGO copy is not linked to the existing DSMZ 973 source-duplicate group. | `CultureMech:002155` and `CultureMech:006931` already represent MediaDive and KOMODO copies of DSMZ Medium 973; `CultureMech:008881` names the same DSMZ PDF but remains a separate single-source merge. | The TOGO normalized record and the existing `data/normalized_yaml/bacterial/marinithermus_hydrothermalis_medium.yaml` duplicate group. |
| minor | `mediaingredientmech_chebi_term` for MgSO4 x 7 H2O is stale. | The primary term was re-grounded to `CHEBI:31795`, but `mediaingredientmech_chebi_term` still points at `CHEBI:32599` on the same ingredient. | `data/normalized_yaml/bacterial/TOGO_M2295_Marinithermus_Hydrothermalis_Medium.yaml`. |

## Recommended Edits

1. Rebuild the TOGO M2295 normalized record from DSMZ Medium 973 without summing
   main-medium and Modified Wolin's mineral solution II components.
2. Preserve `Trace element solution` as a 10 ml/l stock addition and keep its
   stock composition nested or referenced through `mediadive.solution:6187`.
3. Correct NiCl2 x 6 H2O, Na2Se3 x 5 H2O, and Fe(NH4)2(SO4)2 x 6 H2O
   milligram-scale quantities.
4. Move KOH under trace-solution preparation or remove it from the root final
   medium.
5. Link `CultureMech:008881` into the existing DSMZ 973 source-duplicate group
   after its composition signature matches the MediaDive/KOMODO signature.
6. Refresh the stale MgSO4 x 7 H2O `mediaingredientmech_chebi_term`.
7. Add a curation-history event describing the source-backed repair.

## Follow-up Checks

- Re-run the focused LinkML, strict, term, and reference validators on the
  edited TOGO normalized record.
- Run `just validate-media-variant-links` after adding the source-duplicate
  relation.
- Regenerate merged records and verify that the TOGO, KOMODO, and MediaDive
  DSMZ 973 copies collapse or link as one source-duplicate set.
- Manually compare the edited record against TOGO M2295, the DSMZ Medium 973
  PDF, and MediaDive REST medium 973.

## Additional Notes

- The report relies on exact `TOGO:M2295`, `mediadive.medium:973`,
  `komodo.medium:973`, and `CultureMech:*` searches scoped to normalized
  indexes and the three exact sibling records.
