# YAML Record Review: CLOSTRIDIUM THERMOSULFUROGENES MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_thermosulfurogenes_medium__1011fb53.yaml`
- Started UTC: `2026-09-22T09:56:44Z`
- Finished UTC: `2026-09-22T09:57:56Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:003086` for MediaDive/JCM Medium `J743`, generated from `data/normalized_yaml/bacterial/clostridium_thermosulfurogenes_medium.yaml` on merge fingerprint `1011fb535597ae074f4e848835eebe106f0e0b387024c77abba7cdb2437d6df8`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_thermosulfurogenes_medium__1011fb53.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The record identity is plausible but points to a stale JCM URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=743` now returns a small `Nothing found` page. The TOGO duplicate `M768` records the same original JCM source and preserves the JCM 743 formula as `Clostridium Thermosulfurogenes Medium`, confirming this generated record is intended to be the direct MediaDive branch for that JCM medium.

The direct branch has better unit conversion than the TOGO branch for the base milligram rows. `FeSO4 x 7 H2O` is `0.00147783 G_PER_L` and resazurin is `0.000985222 G_PER_L`, matching a 1.015 L final-volume correction of the TOGO source masses. Most ingredient terms are grounded and linked.

The ignored-inclusive duplicate search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found an unmerged TOGO `M768` sibling for the same JCM `GRMD=743` URL. Ignored files were included.

## Evidence

TOGO `M768` records the same JCM `GRMD=743` source with a base solution containing 1 L water, 1 g yeast extract, 0.3 g KH2PO4, 1 g NH4Cl, 1 mg resazurin, 0.2 g MgCl2 x 6 H2O, 0.5 g Na2S x 9 H2O, 1.5 mg FeSO4 x 7 H2O, 5.3 g Na2HPO4 x 12 H2O, 5 g glucose, 10 ml trace element solution, and 5 ml trace vitamins from JCM Medium 190.

The trace element solution is a separate 1 L stock in TOGO `M768`, not a set of final-medium additions. Its recipe starts with 1 L distilled water plus 12.8 g nitrilotriacetic acid, 1 g NaCl, 0.2 g FeCl2 x 4 H2O, 0.1 g MnCl2 x 4 H2O, 0.17 g CoCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 0.1 g ZnCl2, 20 mg CuCl2, 10 mg H3BO3, 10 mg Na2MoO4 x 2 H2O, 26 mg NiCl2 x 6 H2O, 20 mg Na2SeO3 x 5 H2O, and KOH for pH adjustment.

TOGO `M768` carries the preparation notes needed to keep those stocks distinct: adjust pH to 6.0-6.5, prepare sodium sulfide separately as a 5% w/v solution under nitrogen and neutralize it with 1 N HCl, sterilize glucose separately, and dissolve nitrilotriacetic acid first for the trace solution before adjusting it to pH 6.5 with KOH.

## Completeness

The record has useful preparation steps, including the sodium sulfide, glucose, and nitrilotriacetic-acid handling notes.

However, the trace element stock and the Medium 190 trace-vitamin addition have been flattened into top-level final ingredients. The generated direct branch does not have `solutions` rows for either `10 ml/L` trace elements or `5 ml/L` trace vitamins, and therefore omits the assembly structure that distinguishes final base ingredients from stock contents.

No target organism or growth evidence is present.

## Findings

- Severe: trace-element stock contents were flattened into final top-level ingredients. `Nitrilotriacetic acid`, `NaCl`, `FeCl2 x 4 H2O`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `CaCl2 x 2 H2O`, `ZnCl2`, `CuCl2`, `H3BO3`, `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, and `Na2SeO3 x 5 H2O` are stock components added through 10 ml/L trace element solution.
- Severe: the Medium 190 trace-vitamin cross-reference is expanded as top-level vitamin rows, so all vitamin concentrations are stock-strength rather than final concentrations after the 5 ml/L addition.
- Major: the sibling TOGO `M768` branch is unmerged and worse; it preserves empty solution shells but also flattens the same trace stock and keeps several source milligram values as final grams per liter.
- Minor: JCM Medium 743 is no longer retrievable at the recorded source URL, so future curation must reconcile the direct MediaDive import with the TOGO snapshot or another archived source.

## Recommended Edits

- Represent `Trace element solution` as a 10 ml/L stock addition and move its internal ingredients out of the top-level final formula.
- Represent `Trace vitamins (see Medium [M190])` as a 5 ml/L stock addition or a resolved link to the concrete JCM 190 vitamin solution, then remove the flattened vitamin rows from the final formula.
- Preserve the final base rows and the corrected FeSO4 and resazurin milligram conversions from the direct branch.
- After fixing TOGO `M768` unit handling, regenerate and merge the direct JCM and TOGO branches for JCM Medium 743.
- Record that the current JCM `GRMD=743` URL no longer serves the formula if no live replacement source exists.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the trace stock solvent is not counted as a second final water liter.
- Confirm no trace element or vitamin stock row remains as a top-level final ingredient.
- Confirm `FeSO4 x 7 H2O` and resazurin stay in milligram-derived final quantities, not TOGO `1.5` and `1 G_PER_L`.
- Confirm the TOGO `M768` duplicate merges with this direct MediaDive/JCM branch.

## Additional Notes

Empty optional fields are not defects. The live JCM source fetch was checked during review and returned `Nothing found`; the unmerged TOGO `M768` snapshot was therefore used only to cross-check the direct branch, not as proof that the current JCM page still serves the recipe.
