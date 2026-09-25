# YAML Record Review: freshwater_iron_gel_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_iron_gel_medium__d012b865.yaml
- Started UTC: 2026-09-23T04:24:22Z
- Finished UTC: 2026-09-23T04:26:13Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:003011` / `freshwater_iron_gel_medium`, a one-source merge of JCM Medium J665.
- Compared it with maintained source `data/normalized_yaml/bacterial/freshwater_iron_gel_medium.yaml`.
- Cross-checked the current MediaDive REST payload for medium J665 and the linked public JCM GRMD=665 URL.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J665` correctly identifies FRESHWATER IRON GEL MEDIUM from the JCM import in MediaDive.
- The maintained and generated records are identical for the substantive fields; future formula fixes belong in `data/normalized_yaml/bacterial/freshwater_iron_gel_medium.yaml` or the MediaDive/JCM import transform.
- Exact ignored-inclusive lookup for `mediadive.medium:J665`, `JCM Medium J665`, and `FRESHWATER IRON GEL MEDIUM` across normalized and generated YAML found this single JCM J665 owner.
- The linked JCM URL for GRMD=665 returned a `Nothing found` page during review, so the original JCM page could not be inspected directly.

## Evidence

- MediaDive models J665 with a main solution containing NaHCO3, NH4Cl, NaH2PO4 x H2O, KCl, 100 mM poorly crystalline iron(III) oxide, 1 mM Na2SeO4, vitamin solution, trace mineral solution, 130 mM FeCl2, 0.4 percent CaCl2 x 2 H2O, and pH 7.0 2 M sodium acetate.
- The JCM preparation text in MediaDive says to add the base components to distilled water and bring the volume to 1.0 L, but the generated record uses MediaDive's `g_l` values calculated against a 21 ml solution volume. That inflates NaHCO3 from 2.5 g/L to 119.048 g/L, NH4Cl from 0.25 g/L to 11.9048 g/L, NaH2PO4 x H2O from 0.6 g/L to 28.5714 g/L, and KCl from 0.1 g/L to 4.7619 g/L.
- MediaDive represents vitamin and trace mineral stocks separately. The generated record flattens vitamin stock concentrations into top-level medium ingredients and leaves the trace-mineral stock only as prose.
- MediaDive rows for 1 ml or 0.1 ml sterile stock additions were imported as 1, 0.1, or 0.1 g/L ingredient concentrations for Na2SeO4, FeCl2, CaCl2 x 2 H2O, and sodium acetate, conflating stock-addition volumes with final mass concentrations.
- The generated preparation text preserves JCM's anaerobic dispensing, N2/CO2 sparging, autoclaving, Fe(III) suspension, supplemented trace-minerals, and JCM 12378 inoculum notes.

## Completeness

- The final-medium formula is materially wrong until stock additions are modeled as stocks and diluted correctly.
- Poorly crystalline iron(III) oxide is required at 100 mM in the J665 main solution and is absent as a structured ingredient or solution addition.
- Trace mineral solution is required as a stock addition and is not structurally represented.
- The direct JCM source URL is stale; MediaDive REST was the inspected recoverable source for the imported J665 payload.

## Findings

- Major: base-medium salts were divided by a 21 ml imported solution volume instead of the 1.0 L final base volume in the JCM preparation text; NaHCO3, NH4Cl, NaH2PO4 x H2O, and KCl are all overrepresented in both normalized and generated YAML.
- Major: vitamin, trace-mineral, Na2SeO4, FeCl2, CaCl2 x 2 H2O, and sodium acetate stock additions are flattened or mis-scaled as top-level g/L rows instead of being represented as post-autoclave sterile solution additions.
- Major: the 100 mM poorly crystalline iron(III) oxide addition exists only through preparation prose, not as a structured required stock addition.
- Minor: `Na2SeO4` still carries a legacy `mediaingredientmech_term` link after the June CHEBI migration history entry says legacy links were refreshed.
- Minor: the linked public JCM GRMD=665 page is stale and cannot recover the recipe without MediaDive.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/freshwater_iron_gel_medium.yaml` so the base salts use the 1 L amounts from JCM J665 rather than MediaDive's 21 ml normalization artifact.
- Model poorly crystalline iron(III) oxide, vitamin solution, and trace mineral solution as separate stock additions with source amounts and preparation boundaries intact.
- Replace the imported Na2SeO4, FeCl2, CaCl2 x 2 H2O, and sodium acetate `g/L` rows with correct sterile-stock addition records or correctly diluted final concentrations.
- Update the Na2SeO4 MediaIngredientMech link to the same CHEBI-keyed shape as the other ingredients when the record is repaired.
- Regenerate `data/merge_yaml/merged/freshwater_iron_gel_medium__d012b865.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated J665 YAML.
- Confirm NaHCO3 is 2.5 g/L, NH4Cl is 0.25 g/L, NaH2PO4 x H2O is 0.6 g/L, and KCl is 0.1 g/L in the base medium.
- Confirm 100 mM poorly crystalline iron(III) oxide, vitamin solution, trace mineral solution, 1 mM Na2SeO4, 130 mM FeCl2, 0.4 percent CaCl2 x 2 H2O, and pH 7.0 2 M sodium acetate remain scoped as stock additions.
- Confirm no vitamin-stock ingredient appears as an undiluted top-level final concentration.

## Additional Notes

- The generated file is derived data and is a one-source merge. All formula defects observed here are already present in the normalized JCM J665 record or the upstream MediaDive import shape.
