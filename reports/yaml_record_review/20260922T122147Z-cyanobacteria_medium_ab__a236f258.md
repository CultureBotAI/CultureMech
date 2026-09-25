# YAML Record Review: Cyanobacteria Medium AB +

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml
- Started UTC: 2026-09-22T12:19:15Z
- Finished UTC: 2026-09-22T12:21:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001127 |
| Name | cyanobacteria_medium_ab |
| Source | DSMZ / MediaDive medium 1644 |
| Media term | mediadive.medium:1644, DSMZ Medium 1644 |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/cyanobacteria_medium_ab.yaml |
| Maintained solution input | data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml |

This is the nitrate-containing DSMZ 1644 "Cyanobacteria Medium AB +" sibling.
It is a distinct generated merge from DSMZ 1645 "Cyanobacteria Medium AB-"
despite sharing the normalized `cyanobacteria_medium_ab` slug.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml --out /private/tmp/cyanobacteria_medium_ab_a236f258.strict.tsv --workers 1 --quiet` | Passed |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

All automated shape and CURIE checks pass. The scientific defects are
solution-boundary and dilution errors that require source comparison.

## Identity and Grounding

The record identity is correct for DSMZ / MediaDive medium `1644`. The
generated file and its normalized input both cite `mediadive.medium:1644` with
the label "Cyanobacteria Medium AB +", and MediaDive
`/download/medium/1644/json` identifies the same DSMZ medium, source, and PDF
link.

A gitignore-independent `rg --no-ignore --hidden` search for
`mediadive.medium:1644`, `DSMZ_1644`, and `Cyanobacteria Medium AB +` over
`data/normalized_yaml`, `data/raw`, and `data/merge_yaml/merged` found the AB +
normalized file and this hash-suffixed generated merge. The same search did not
find a local raw DSMZ 1644 capture under `data/raw`.

The AB + parent shares MediaDive solution `5734`, `Trace metal mix`, with AB-.
That reusable SolutionRecipe is present as
`data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml`, but the
AB + normalized parent embeds a partial local trace mix instead of linking to
the complete source-owned stock recipe.

## Evidence

DSMZ and MediaDive agree that AB + differs from AB- by adding nitrate:
3.75 ml/L of a 300 g/L NaNO3 stock, giving the 1.125 g/L final NaNO3 row in
the generated record. The major cations, citrate, EDTA, phosphate, carbonate,
ferric ammonium citrate, and vitamin B12 rows also match MediaDive's computed
final `g_l` values.

The trace metals do not match the source role. MediaDive medium 1644 adds
1 ml/L of `Trace metal mix` solution `5734`; the reviewed generated record
lists that stock's constituents as peer final-medium ingredients:

| Component | Source role | Generated record |
|---|---|---|
| H3BO3 | 2.86 g in 1 L Trace metal mix, then 1 ml stock per L medium | 2.9 g/L final medium |
| MnCl2 x 4 H2O | 1.81 g in 1 L Trace metal mix, then 1 ml/L | 1.81 g/L final medium |
| ZnSO4 x 7 H2O | 0.22 g in 1 L Trace metal mix, then 1 ml/L | 0.22 g/L final medium |
| Na2MoO4 x 2 H2O | 0.39 g in 1 L Trace metal mix, then 1 ml/L | 0.39 g/L final medium |
| CuSO4 x 5 H2O | 10 ml of 8 g/L stock into 1 L Trace metal mix, then 1 ml/L | 10 g/L final medium |
| Co(NO3)2 x 6 H2O | 10 ml of 5 g/L stock into 1 L Trace metal mix, then 1 ml/L | 10 g/L final medium |

The normalized AB + record has an embedded `Trace metal mix`, but that partial
repair only moved H3BO3, MnCl2, and CuSO4. It left ZnSO4, Na2MoO4, and
Co(NO3)2 at final-medium scope. The embedded CuSO4 row is also wrong because it
stores 10 g/L instead of a 10 ml addition of an 8 g/L copper stock.

The source-owned `mediadive_5734_Trace_metal_mix.yaml` is complete for all six
trace constituents, but it has the same inherited representation defect for
CuSO4 and Co(NO3)2: 10 ml source additions are stored as `PERCENT_V_V`.

## Completeness

- The generated record has no `references`, `source_data`, `target_organisms`,
  or `growth_metrics`. Empty organism and growth slots are acceptable for this
  database recipe, but the DSMZ/MediaDive retrieval URL should be structured
  rather than only embedded in `notes`.
- A gitignore-independent search over `data/normalized_yaml`, `data/raw`, and
  `data/merge_yaml/merged` found the reusable `mediadive_5734_Trace_metal_mix.yaml`
  SolutionRecipe and no local raw DSMZ 1644 capture under `data/raw`.
- The generated file does not retain the AB + normalized file's local
  `solutions` block, so the generated ingredient list looks fully flattened
  even though the maintained input has a partial nesting attempt.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge flattened the AB + Trace metal mix into final-medium ingredients. | MediaDive and DSMZ add 1 ml/L Trace metal mix; the generated YAML lists six trace-mix members directly as final `G_PER_L` rows. | Merge logic for local `solutions` entries and `data/normalized_yaml/bacterial/cyanobacteria_medium_ab.yaml` |
| major | The normalized AB + parent only partially nested the Trace metal mix. | H3BO3, MnCl2, and CuSO4 are embedded in a local stock, but ZnSO4, Na2MoO4, and Co(NO3)2 remain top-level final-medium ingredients. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ab.yaml` |
| major | CuSO4 and Co(NO3)2 are volume additions into the trace stock, not 10 g/L concentrations. | MediaDive solution `5734` adds 10 ml of 8 g/L CuSO4 stock and 10 ml of 5 g/L Co(NO3)2 stock to the one-liter trace mix; CultureMech projects raw `10` values as concentrations. | `data/normalized_yaml/bacterial/mediadive_5734_Trace_metal_mix.yaml` and the AB + normalized parent |
| minor | NaNO3 still uses the deprecated `mediaingredientmech_term` field. | The record has a valid CHEBI primary term for sodium nitrate, but its MIM cross-link remains `MediaIngredientMech:000171` while other ingredients migrated to `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ab.yaml` |
| minor | Provenance is mostly free text. | The normalized record names the DSMZ PDF in `notes`, but the generated record has no structured `references` or `source_data` entry for MediaDive medium 1644. | `data/normalized_yaml/bacterial/cyanobacteria_medium_ab.yaml` |

## Recommended Edits

1. Regenerate or curate `cyanobacteria_medium_ab.yaml` so the final medium links
   to the complete MediaDive `Trace metal mix` at 1 ml/L instead of embedding
   only three stock constituents.
2. Repair `mediadive_5734_Trace_metal_mix.yaml` so CuSO4 x 5 H2O and
   Co(NO3)2 x 6 H2O keep their source representation as 10 ml stock additions.
3. Ensure the AB + parent, the AB- parent, and MediaDive solution `5734` share
   one complete source-aligned representation of Trace metal mix.
4. Replace the stale NaNO3 `mediaingredientmech_term` with the CHEBI-keyed
   cross-link style used by the other ingredients.
5. Add structured DSMZ/MediaDive 1644 provenance.
6. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_ab__a236f258.yaml`
   from the maintained normalized inputs; do not edit the generated file.

## Follow-up Checks

- Run schema, strict, reference, and term validation on the repaired AB + record
  and `mediadive_5734_Trace_metal_mix.yaml`.
- Regenerate the merge and verify that H3BO3, MnCl2, ZnSO4, Na2MoO4, CuSO4, and
  Co(NO3)2 no longer appear as top-level final `G_PER_L` ingredients.
- Compare regenerated AB + against MediaDive `/download/medium/1644/json`,
  verifying the nitrate row, each bulk final `g_l`, the 1 ml/L trace-mix
  addition, and the nested Cu/Co stock additions.
- Re-run the same trace-mix checks on the AB- sibling because both records share
  solution `5734`.

## Additional Notes

- The source formula leaves no ambiguity about AB + vs AB-: AB + has a NaNO3
  row and DSMZ medium ID 1644, while AB- lacks nitrate and uses ID 1645.
- MediaDive solution `5734` is shared, so a single repair to the source-owned
  trace-mix record should be propagated to both cyanobacteria AB variants.
