# YAML Record Review: Cyanobacteria Medium BG11-

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml
- Started UTC: 2026-09-22T12:31:00Z
- Finished UTC: 2026-09-22T12:33:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001069 |
| Name | cyanobacteria_medium_bg11 |
| Source | DSMZ / MediaDive medium 1592 |
| Media term | mediadive.medium:1592, DSMZ Medium 1592 |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/cyanobacteria_medium_bg11.yaml |
| Shared solution input | data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml |

This generated record is the nitrate-free DSMZ 1592 BG11- recipe. It is a
distinct sibling of DSMZ 1593 BG11+, even though both normalize to the same
`cyanobacteria_medium_bg11` slug.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml --out /private/tmp/cyanobacteria_medium_bg11_e6d564be.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing validation result covers schema shape only; unsupported
concentrations are still present.

## Identity and Grounding

The generated file and its normalized input correctly identify DSMZ / MediaDive
medium 1592, "Cyanobacteria Medium BG11-". The live MediaDive
`/download/medium/1592/json` export confirms the same ID, label, DSMZ source,
and DSMZ Medium 1592 PDF link.

A gitignore-independent `rg --no-ignore --hidden` search for
`mediadive.medium:1592`, `Cyanobacteria Medium BG11-`, `DSMZ Medium 1592`, and
`cyanobacteria_medium_bg11` over `data/normalized_yaml`, `data/raw`, and this
generated file found the BG11- normalized source, the DSMZ 1593 BG11+ sibling,
the BG11+ TES-buffered sibling, and no local raw DSMZ 1592 capture under
`data/raw`.

The Mg(SO4) x 7 H2O row lacks a CHEBI or MediaIngredientMech grounding.

## Evidence

BG11- is BG11 without nitrate. DSMZ and MediaDive support these nitrate-free
main-solution additions:

| Component | Source addition | Generated record |
|---|---:|---:|
| Mg(SO4) x 7 H2O | 10 ml of 7.5 g/L stock = 0.075 g/L | 10 g/L |
| CaCl2 x 2 H2O | 10 ml of 3.6 g/L stock = 0.036 g/L | 10 g/L |
| Na3-citrate x 2 H2O | 10 ml of 0.6 g/L stock = 0.006 g/L | 10 g/L |
| Na-EDTA x 2 H2O | 10 ml of 0.1 g/L stock = 0.001 g/L | 10 g/L |
| K2HPO4 x 3 H2O | BG11-Mix, 1 ml/L of a 20 g/L stock = 0.02 g/L | 2 g/L |
| Na2CO3 | BG11-Mix, 1 ml/L of a 10 g/L stock = 0.01 g/L | 2 g/L |
| Fe(NH4)citrate | BG11-Mix, 1 ml/L of a 3 g/L stock = 0.003 g/L | 1 g/L |
| Vitamin B12 | 1 ml of 0.02 g/L stock = 0.00002 g/L | 1 g/L |

The generated record retains raw source volumes as final grams per liter for
every parent ingredient and loses the BG11-Mix stock boundary. It also flattens
MediaDive solution `5734`, Trace metal mix, into six top-level final-medium
ingredients. The final preparation step that makes the trace stock to 1000 ml
is therefore attached to BG11- instead of to the stock solution.

## Completeness

- The generated record has no `references`, `source_data`, `target_organisms`,
  or `growth_metrics`. Empty organism and growth slots are acceptable for a DSMZ
  recipe record, but source retrieval details should be structured.
- The DSMZ BG11-Mix stock is missing as a preparation boundary; K2HPO4, Na2CO3,
  and Fe(NH4)citrate are projected as direct final ingredients.
- MediaDive solution `5734` exists as a reusable normalized SolutionRecipe, but
  this BG11- parent does not reference it structurally.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | BG11- stock additions were converted to raw `G_PER_L` values. | DSMZ 1592 lists 10 ml, 2 ml, and 1 ml stock additions; the generated record stores those raw values as grams per liter for Mg(SO4), CaCl2, citrate, EDTA, K2HPO4, Na2CO3, Fe(NH4)citrate, and B12. | `data/normalized_yaml/bacterial/cyanobacteria_medium_bg11.yaml` and the MediaDive importer |
| major | BG11-Mix and Trace metal mix stock boundaries are missing. | Source 1592 uses BG11-Mix and 1 ml/L Trace metal mix; generated YAML has only their ingredients as top-level rows and appends the trace-stock make-up step to final-medium preparation. | Normalized BG11- parent and solution merge logic |
| minor | Mg(SO4) x 7 H2O is ungrounded. | The row has no `term` or MediaIngredientMech link. | Normalized BG11- parent or MediaDive compound 2154 mapping |
| minor | Provenance is free-text only. | The DSMZ PDF URL is stored in `notes`, with no structured reference or source-data object. | Normalized BG11- parent |

## Recommended Edits

1. Repair BG11- stock additions against DSMZ Medium 1592 so every final amount
   is either structurally represented as a stock addition or computed from the
   source stock strength and volume.
2. Represent the DSMZ BG11-Mix boundary instead of treating K2HPO4, Na2CO3, and
   Fe(NH4)citrate as unsupported final 2/2/1 g/L ingredients.
3. Link BG11- to MediaDive Trace metal mix `5734` at 1 ml/L.
4. Ground Mg(SO4) x 7 H2O and add structured DSMZ/MediaDive 1592 provenance.
5. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_bg11__e6d564be.yaml`
   from the repaired normalized input.

## Follow-up Checks

- Run open-schema, strict, reference, and term validation on the repaired BG11-
  normalized record.
- Regenerate the merge and verify the nitrate-free DSMZ 1592 final formula:
  0.075 g/L Mg(SO4) x 7 H2O, 0.036 g/L CaCl2 x 2 H2O, 0.006 g/L citrate,
  0.001 g/L EDTA, 0.02 g/L K2HPO4, 0.01 g/L Na2CO3, 0.003 g/L Fe(NH4)citrate,
  and 0.00002 g/L vitamin B12.
- Verify that Trace metal mix rows no longer appear as top-level final
  ingredients in the regenerated BG11- record.

## Additional Notes

- No NaNO3 row is expected here; the absence of nitrate is the defining
  difference between DSMZ 1592 BG11- and DSMZ 1593 BG11+.
