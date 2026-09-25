# YAML Record Review: M17 medium (Oxoid) supplemented with 1% (wt/vol) glucose

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml`
- Started UTC: 2026-09-23T20:57:24Z
- Finished UTC: 2026-09-23T20:59:07Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml`
- Canonical maintained owner: `data/normalized_yaml/bacterial/m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml`
- Merged sibling owner: `data/normalized_yaml/bacterial/m17_medium_oxoid_supplemented_with_0_5_wt_vol_glucose.yaml`
- CultureMech ID: `CultureMech:009428`
- Media term: `TOGO:M2892`
- Merge fingerprint: `953136c535842a25df3755ce3ed2e14dfb611f8670e82074c34255060b6abfd9`
- Merge sources: `m17_medium_oxoid_supplemented_with_0_5_wt_vol_glucose`, `m17_medium_oxoid_supplemented_with_1_wt_vol_glucose`
- Ignored-inclusive exact searches over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the two maintained TOGO owners, the generated merged record and indexes, and archived review or validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The generated record presents itself as TOGO Medium `M2892`, `M17 medium (Oxoid) supplemented with 1% (wt/vol) glucose`, but the generated YAML also merges TOGO Medium `M2883`, `M17 medium (Oxoid) supplemented with 0.5% (wt/vol) glucose`, and inherits a final `Glucose` value of `0.5 G_PER_L`. Those two source accessions are adjacent M17/Oxoid glucose recipes, not duplicates: the inspected TOGO API responses identify one as 1% glucose and the other as 0.5% glucose.

Ingredient ontology grounding for water and glucose is appropriate, but the `Lactose` term is attached to a stock-solution ingredient that was imported as a final ingredient. The generated record also leaves TOGO source identity only in `media_term`, `notes`, `synonyms`, and `merged_from`, not in structured `references`.

## Evidence

- TOGO `M2892` supports the source identity, the `M17 broth (Oxoid)` line at 37.25 g in 950 ml distilled water, and a 1% wt/vol glucose supplement, equivalent to 10 g/L for the final medium.
- TOGO `M2883` supports the sibling `0.5% (wt/vol) glucose` formula, equivalent to 5 g/L, not the generated canonical's 0.5 g/L and not a duplicate of the 1% formula.
- Both TOGO responses encode the 10% wt/vol lactose solution as a 50 ml addition. Flattening 50 ml of a 10% wt/vol lactose stock into a 1 L medium should contribute 5 g/L lactose, while preserving the stock-solution boundary.
- TOGO `M2892` carries source metadata for pH `6.9 +/- 0.2`, autoclaving at 121 C for 15 minutes, cooling to 50 C before adding sterile 10% lactose solution, and the source growth context of standing 30 C cultures for the Lactococcus lactis strains NZ9000 and MG1363.

## Completeness

The generated record is materially incomplete for source preparation semantics: it omits the source pH, the autoclave/cool/add workflow, and the stock-sterilization boundary. The empty `solutions[0].composition` is consequential here because the source did define the stock as 10 g lactose in 100 ml water, but the YAML stores that source detail as an empty `Unknown solution` added at `50 G_PER_L`.

No search miss was used as a finding. Ignored-inclusive exact searches over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` were used only to identify all owners and archived review context for `CultureMech:009428`, `TOGO:M2892`, `TOGO:M2883`, the merge fingerprint, and both sibling source names.

## Findings

1. **Blocker - the generated canonical conflates two distinct glucose variants.** TOGO `M2892` is the 1% glucose recipe and TOGO `M2883` is the 0.5% glucose recipe, but `data/merge_yaml/merged/m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml` merged both source records into one canonical record. This makes the generated record both claim 1% glucose in `original_name` and `media_term` and carry `0.5 G_PER_L` in its ingredient list.

2. **Major - percent weight/volume values were imported as if they were grams per liter.** The maintained 1% owner records `Glucose` as `1 G_PER_L` instead of 10 g/L, and the maintained 0.5% owner records `Glucose` as `0.5 G_PER_L` instead of 5 g/L.

3. **Major - the lactose stock was flattened at the wrong concentration and with the wrong boundary.** The source says to add 50 ml of sterile 10% wt/vol lactose solution, prepared from 10 g lactose per 100 ml water. The maintained owners instead store `Lactose` as `10 G_PER_L`, store `Lactose solution 10% (w/v)` as an empty solution at `50 G_PER_L`, and do not preserve that the final lactose contribution from 50 ml of stock is 5 g/L.

4. **Major - water from the main medium and lactose stock was merged into a false final value.** The source's 950 ml main-medium water and 100 ml stock-solution water were merged into `Distilled water` at `1050.0 G_PER_L`, hiding the fact that the 100 ml water belongs to the stock recipe and should be diluted through a 50 ml stock addition.

5. **Major - preparation and condition evidence was dropped.** TOGO `M2892` supplies pH `6.9 +/- 0.2`, 121 C autoclaving, 50 C cooling before sterile lactose addition, and the 30 C Lactococcus lactis standing-culture context, but the maintained owner and generated record keep none of those structured conditions or preparation steps.

## Recommended Edits

- In `data/normalized_yaml/bacterial/m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml`, correct the glucose supplement from `1 G_PER_L` to 10 g/L while preserving the source's 1% wt/vol expression.
- In `data/normalized_yaml/bacterial/m17_medium_oxoid_supplemented_with_0_5_wt_vol_glucose.yaml`, correct the sibling glucose supplement from `0.5 G_PER_L` to 5 g/L while preserving the source's 0.5% wt/vol expression.
- In both maintained owners, represent `Lactose solution 10% (w/v)` as a real stock solution made from 10 g lactose and 100 ml water, add it to the final medium as 50 ml, and avoid counting the stock water as direct final-medium water.
- Revisit the generated duplicate merge so TOGO `M2892` and TOGO `M2883` remain separate records after their source glucose concentrations are corrected.
- Add TOGO `M2892` pH and preparation details to the 1% maintained owner, and preserve 30 C standing-culture context only if explicit Lactococcus lactis growth claims are added.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- After regeneration, re-run an ignored-inclusive exact search for `CultureMech:009428`, `TOGO:M2892`, `TOGO:M2883`, and `953136c535842a25df3755ce3ed2e14dfb611f8670e82074c34255060b6abfd9` to confirm the two glucose variants no longer merge.
- Reinspect both TOGO API responses to verify that percent wt/vol concentrations, the lactose stock volume, and the final-volume arithmetic are represented without assuming stock water is a direct final-medium ingredient.
- Rerun open schema, strict, term, and reference validation on the regenerated `m17_medium_oxoid_supplemented_with_1_wt_vol_glucose.yaml`.

## Additional Notes

The source pages have no `src_url` field in the inspected TOGO API responses. The report therefore treats the TOGO medium APIs themselves as the inspected primary source for source quantities and preparation text.
