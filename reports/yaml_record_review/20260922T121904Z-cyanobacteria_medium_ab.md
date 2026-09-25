# YAML Record Review: Cyanobacteria Medium AB-

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_ab.yaml
- Started UTC: 2026-09-22T12:16:00Z
- Finished UTC: 2026-09-22T12:19:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001128 |
| Name | cyanobacteria_medium_ab |
| Source | DSMZ / MediaDive medium 1645 |
| Media term | mediadive.medium:1645, DSMZ Medium 1645 |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_ab.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/DSMZ_1645_Cyanobacteria_Medium_AB-.yaml |
| Maintained solution input | data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml |

This generated record is the DSMZ 1645 "Cyanobacteria Medium AB-" merge, not
the DSMZ 1644 "Cyanobacteria Medium AB +" sibling that normalizes to the same
`cyanobacteria_medium_ab` name and appears in a separate hash-suffixed merged
file.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_ab.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_ab.yaml --out /private/tmp/cyanobacteria_medium_ab.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_ab.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_ab.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The validation gates do not catch solution flattening, stock arithmetic, or
source-vs-derived concentration mismatches.

## Identity and Grounding

The record identity is correct for DSMZ / MediaDive medium `1645`.
The local generated record and its maintained input both point to
`mediadive.medium:1645`; the live MediaDive JSON export for
`/download/medium/1645/json` gives ID `1645`, name "Cyanobacteria Medium AB-",
source `DSMZ`, complex flag `no`, and the DSMZ Medium 1645 PDF link.

A gitignore-independent `rg --no-ignore --hidden` search for
`DSMZ_1645_Cyanobacteria_Medium_AB`, `mediadive.medium:1645`, and
`Cyanobacteria Medium AB-` over `data/normalized_yaml`, `data/raw`, and
`data/merge_yaml/merged` found one normalized MediaRecipe and this generated
merge for MediaDive medium 1645. A separate normalized file,
`data/normalized_yaml/bacterial/cyanobacteria_medium_ab.yaml`, is DSMZ medium
1644 "Cyanobacteria Medium AB +" and is not the target reviewed here.

The source also has a reusable SolutionRecipe identity for MediaDive solution
`5734`, `Trace metal mix`, at
`data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml`. The
maintained AB- parent currently embeds a local `Trace metal mix` instead of
linking to that source-owned solution record.

## Evidence

The live MediaDive JSON and text export for medium 1645 preserve the main
solution as a 1000 ml recipe with a 1 ml/L addition of `Trace metal mix`
solution `5734`. The normalized AB- file already tries to repair some of that
with an embedded local `solutions` entry, but it moved only H3BO3, MnCl2 x
4 H2O, and CuSO4 x 5 H2O. ZnSO4 x 7 H2O, Na2MoO4 x 2 H2O, and Co(NO3)2 x
6 H2O remain top-level ingredients even though they are trace-mix members.

| Component | MediaDive / DSMZ source role | Generated record |
|---|---|---|
| H3BO3 | 2.86 g in a 1 L trace-metal stock; add 1 ml stock per L medium | 2.9 g/L final medium |
| MnCl2 x 4 H2O | 1.81 g in a 1 L trace-metal stock; add 1 ml/L | 1.81 g/L final medium |
| ZnSO4 x 7 H2O | 0.22 g in a 1 L trace-metal stock; add 1 ml/L | 0.22 g/L final medium |
| Na2MoO4 x 2 H2O | 0.39 g in a 1 L trace-metal stock; add 1 ml/L | 0.39 g/L final medium |
| CuSO4 x 5 H2O | 10 ml of an 8 g/L stock into the trace mix; add 1 ml/L trace mix | 10 g/L final medium |
| Co(NO3)2 x 6 H2O | 10 ml of a 5 g/L stock into the trace mix; add 1 ml/L trace mix | 10 g/L final medium |

Because the final medium receives only 1 ml of trace mix per liter, the first
four rows are high by about 1000x if interpreted as final grams per liter. The
copper and cobalt rows are worse: the source 10 ml additions first have to be
diluted into the 1 L trace mix, then the trace mix has to be diluted 1:1000 into
the final medium.

The generated record's bulk salts and post-autoclave K2HPO4, Na2CO3,
Fe(NH4)citrate, and vitamin B12 rows match MediaDive's computed final `g_l`
values, except for calcium chloride. The MediaDive JSON represents CaCl2 x
2 H2O as 10 ml of a 26.8 g/L stock, and the DSMZ PDF lists two 5 ml CaCl2 x
2 H2O stock additions that sum to 0.268 g/L; the record says 0.134 g/L. That is
half of the source-supported concentration.

The live MediaDive text export and current normalized record agree on the main
preparation sequence: make up to 1000 ml, autoclave 20 min at 121 deg C, cool,
then add the filter-sterilized K2HPO4, Na2CO3, Fe(NH4)citrate, and vitamin B12
stock additions. Those preparation steps are supported.

## Completeness

- The generated record has no `references`, `source_data`, `target_organisms`,
  or `growth_metrics`. The empty organism and growth slots are acceptable for a
  database recipe; the missing source URL is only a provenance gap because the
  DSMZ URL is at least present in `notes`.
- A gitignore-independent search over `data/normalized_yaml`, `data/raw`, and
  this merged target found `data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml`
  for the MediaDive trace solution. The parent AB- record should reference or
  synchronize with this maintained solution instead of carrying a second,
  incomplete local copy.
- The generated merge lacks the local `solutions` block from
  `DSMZ_1645_Cyanobacteria_Medium_AB-.yaml`, so even the partial
  `apply_cocktail_nesting.py` repair is absent from the reviewed output.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge flattened the AB- trace-metal stock into final-medium ingredients. | MediaDive and DSMZ add 1 ml/L Trace metal mix; the generated YAML lists H3BO3, MnCl2, ZnSO4, Na2MoO4, CuSO4, and Co(NO3)2 directly as final `G_PER_L` rows. | Merge logic for local `solutions` entries and `data/normalized_yaml/bacterial/DSMZ_1645_Cyanobacteria_Medium_AB-.yaml` |
| major | The normalized AB- parent only partially nested the Trace metal mix. | Its `solutions` block includes H3BO3, MnCl2, and CuSO4, while source rows for ZnSO4, Na2MoO4, and Co(NO3)2 are still top-level final ingredients. | `data/normalized_yaml/bacterial/DSMZ_1645_Cyanobacteria_Medium_AB-.yaml` |
| major | The embedded CuSO4 and Co(NO3)2 trace rows do not preserve the MediaDive nested stock arithmetic. | The source adds 10 ml of 8 g/L CuSO4 stock and 10 ml of 5 g/L Co(NO3)2 stock to the one-liter Trace metal mix; the source-owned SolutionRecipe stores those as `PERCENT_V_V`, and the local AB- solution stores CuSO4 as `10 G_PER_L` while omitting cobalt from the nested stock. | `data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml` and the AB- normalized parent |
| major | CaCl2 x 2 H2O is half of the source-supported final concentration. | MediaDive's 10 ml addition of 26.8 g/L stock and DSMZ's two 5 ml additions sum to 0.268 g/L, not the 0.134 g/L recorded in AB-. | `data/normalized_yaml/bacterial/DSMZ_1645_Cyanobacteria_Medium_AB-.yaml` or the MediaDive importer |
| minor | Provenance is mostly free text. | The normalized input records the DSMZ PDF in `notes`, but the generated record has no structured `references` or `source_data` entry for the inspected MediaDive/DSMZ export. | `data/normalized_yaml/bacterial/DSMZ_1645_Cyanobacteria_Medium_AB-.yaml` |

## Recommended Edits

1. Rebuild `DSMZ_1645_Cyanobacteria_Medium_AB-.yaml` so the final medium keeps
   only bulk final concentrations and a 1 ml/L link to the authoritative
   MediaDive `Trace metal mix` stock.
2. Repair `mediadive_5734_Trace_metal_mix.yaml` so CuSO4 x 5 H2O and
   Co(NO3)2 x 6 H2O remain 10 ml stock additions, not raw `10 PERCENT_V_V`
   concentrations.
3. Include all six trace-mix constituents in the normalized AB- solution path,
   either by linking the source-owned SolutionRecipe or by copying a complete,
   source-synchronized stock definition.
4. Correct AB- CaCl2 x 2 H2O from 0.134 g/L to 0.268 g/L if a fresh DSMZ /
   MediaDive check still shows 10 ml of 26.8 g/L stock.
5. Add structured provenance for DSMZ Medium 1645 / MediaDive medium 1645.
6. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_ab.yaml` after
   normalized curation; do not patch the generated merge directly.

## Follow-up Checks

- Run open-schema, strict, reference, and term validation for the repaired
  `DSMZ_1645_Cyanobacteria_Medium_AB-.yaml` and `mediadive_5734_Trace_metal_mix.yaml`.
- Regenerate this merge and assert that no trace-mix constituent appears as a
  top-level final-medium `G_PER_L` ingredient.
- Compare the regenerated AB- record row by row against MediaDive
  `/download/medium/1645/json`, including amount, unit, stock concentration,
  final `g_l`, and solution ID `5734`.
- Check the sibling AB + record after any shared importer or solution repair;
  it has the same local `Trace metal mix` pattern.

## Additional Notes

- The normalized AB- input was partially repaired on 2026-08-07 by
  `apply_cocktail_nesting.py`, but the repair did not move ZnSO4, Na2MoO4, or
  Co(NO3)2 and did not survive generation into `data/merge_yaml/merged`.
- This record uses the no-nitrate AB- formulation. The same slug without source
  disambiguation also refers to DSMZ 1644 AB +, which contains NaNO3 and has a
  distinct permanent ID.
