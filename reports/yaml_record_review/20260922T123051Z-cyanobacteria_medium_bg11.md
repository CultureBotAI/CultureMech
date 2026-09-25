# YAML Record Review: Cyanobacteria Medium BG11+

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml
- Started UTC: 2026-09-22T12:28:35Z
- Finished UTC: 2026-09-22T12:30:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001070 |
| Name | cyanobacteria_medium_bg11 |
| Source | DSMZ / MediaDive medium 1593 |
| Media term | mediadive.medium:1593, DSMZ Medium 1593 |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/DSMZ_1593_Cyanobacteria_Medium_BG11.yaml |
| Shared solution input | data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml |

This generated file is DSMZ 1593 BG11+. DSMZ 1592 BG11- also normalizes to
`cyanobacteria_medium_bg11`, but it is a separate source record and is not part
of this merge.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml --out /private/tmp/cyanobacteria_medium_bg11.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The automated validators accept the raw stock quantities as syntactically valid
`G_PER_L` values.

## Identity and Grounding

The generated record has the correct identity for DSMZ / MediaDive medium 1593,
"Cyanobacteria Medium BG11+". Live MediaDive JSON for
`/download/medium/1593/json` gives the same medium ID, source, title, and DSMZ
Medium 1593 PDF link.

A gitignore-independent `rg --no-ignore --hidden` search for
`mediadive.medium:1593`, `DSMZ_1593_Cyanobacteria_Medium_BG11`, and
`Cyanobacteria Medium BG11+` over `data/normalized_yaml`, `data/raw`, and this
generated file found exactly this normalized BG11+ parent and the BG11+
TES-buffered sibling `mediadive.medium:1593a`; it found no local raw DSMZ 1593
capture under `data/raw`.

The Mg(SO4) x 7 H2O row is ungrounded despite denoting magnesium sulfate
heptahydrate, and the NaNO3 row still uses a legacy
`mediaingredientmech_term`.

## Evidence

DSMZ and MediaDive support a 1000 ml BG11+ main solution with 5 ml NaNO3 stock,
10 ml additions of Mg(SO4), CaCl2, citrate, and EDTA stocks, a 2 ml BG11-Mix
addition represented in MediaDive as K2HPO4 plus Na2CO3 plus Fe(NH4)citrate,
a 1 ml Trace metal mix addition, and 1 ml vitamin B12 after autoclaving.

| Component | Source addition | Generated record |
|---|---:|---:|
| NaNO3 | 5 ml of 300 g/L stock = 1.5 g/L | 1.5 g/L |
| Mg(SO4) x 7 H2O | 10 ml of 7.5 g/L stock = 0.075 g/L | 10 g/L |
| CaCl2 x 2 H2O | 10 ml of 3.6 g/L stock = 0.036 g/L | 10 g/L |
| Na3-citrate x 2 H2O | 10 ml of 0.6 g/L stock = 0.006 g/L | 10 g/L |
| Na-EDTA x 2 H2O | 10 ml of 0.1 g/L stock = 0.001 g/L | 10 g/L |
| K2HPO4 x 3 H2O | 2 ml of 20 g/L stock = 0.04 g/L | 2 g/L |
| Na2CO3 | 2 ml of 10 g/L stock = 0.02 g/L | 2 g/L |
| Fe(NH4)citrate | 1 ml of 6 g/L stock = 0.006 g/L | 1 g/L |
| Vitamin B12 | 1 ml of 0.02 g/L stock = 0.00002 g/L | 1 g/L |

Everything except NaNO3 is stored as the raw stock-addition number, not the
final concentration. Trace metal mix is also flattened: DSMZ and MediaDive add
solution `5734` at 1 ml/L, but H3BO3, MnCl2, ZnSO4, Na2MoO4, CuSO4, and
Co(NO3)2 appear as top-level final `G_PER_L` ingredients in the generated
record.

The fourth generated preparation step, "Make up to 1000 ml with MilliQ water",
belongs to the Trace metal mix stock, not to the final BG11+ medium, and is a
symptom of the same flattening.

## Completeness

- The generated record has no `references`, `source_data`, `target_organisms`,
  or `growth_metrics`. Empty organism and growth slots are acceptable for this
  database recipe; structured DSMZ/MediaDive provenance should still be added.
- The BG11-Mix grouping in the DSMZ PDF is not represented. MediaDive has
  already expanded it to K2HPO4, Na2CO3, and Fe(NH4)citrate rows, which is
  acceptable if the rows keep the source stock/dilution context.
- The shared MediaDive solution `5734` is available as a maintained
  SolutionRecipe, but this parent does not reference it structurally.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Most final-medium rows are stock volumes or stock-local values mislabeled as `G_PER_L`. | Mg(SO4), CaCl2, citrate, EDTA, phosphate, carbonate, iron, and B12 carry raw 10, 2, or 1 values from the source instead of diluted final concentrations. | `data/normalized_yaml/bacterial/DSMZ_1593_Cyanobacteria_Medium_BG11.yaml` and the MediaDive importer |
| major | Trace metal mix was flattened into the final ingredient list. | Source medium 1593 adds 1 ml/L of MediaDive solution `5734`; the generated record lists six trace-stock constituents directly and appends a trace-stock make-up step to final-medium preparation. | Normalized BG11+ parent and merge logic for solution references |
| minor | Mg(SO4) x 7 H2O is ungrounded. | The generated row has no CHEBI or MediaIngredientMech term. | Normalized BG11+ parent or MediaDive compound 2154 mapping |
| minor | NaNO3 still uses `mediaingredientmech_term`. | Sodium nitrate has a correct CHEBI primary term but keeps the deprecated `MediaIngredientMech:000171` link. | Normalized BG11+ parent |
| minor | Source provenance is free-text only. | The DSMZ PDF URL is only in `notes`, with no structured reference/source-data entry. | Normalized BG11+ parent |

## Recommended Edits

1. Re-curate DSMZ 1593 so Mg(SO4), CaCl2, citrate, EDTA, BG11-Mix, and vitamin
   B12 stock additions preserve their source units or dimensionally correct
   final concentrations.
2. Link BG11+ to source solution `5734` at 1 ml/L instead of flattening Trace
   metal mix constituents into the final medium.
3. Keep the BG11+ and BG11- normalized records separate despite the shared
   `cyanobacteria_medium_bg11` slug.
4. Ground Mg(SO4) x 7 H2O, migrate the NaNO3 MIM cross-link, and add
   structured DSMZ/MediaDive 1593 provenance.
5. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_bg11.yaml` after
   repairing the maintained input.

## Follow-up Checks

- Run open-schema, strict, reference, and term validation on the repaired BG11+
  normalized record and the `mediadive_5734_Trace_metal_mix.yaml` stock if it
  changes.
- Regenerate the merge and verify the DSMZ 1593 final concentrations:
  0.075 g/L Mg(SO4) x 7 H2O, 0.036 g/L CaCl2 x 2 H2O, 0.006 g/L citrate,
  0.001 g/L EDTA, 0.04 g/L K2HPO4, 0.02 g/L Na2CO3, 0.006 g/L Fe(NH4)citrate,
  1.5 g/L NaNO3, and 0.00002 g/L vitamin B12.
- Verify that Trace metal mix rows do not appear as top-level final ingredients
  in the regenerated 1593 merge.

## Additional Notes

- The current BG11- record at
  `data/normalized_yaml/bacterial/cyanobacteria_medium_bg11.yaml` has the same
  raw stock-volume import pattern and should receive the same repair when DSMZ
  1592 is curated.
