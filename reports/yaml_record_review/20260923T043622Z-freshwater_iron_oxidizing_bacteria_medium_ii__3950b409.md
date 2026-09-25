# YAML Record Review: freshwater_iron_oxidizing_bacteria_medium_ii

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium_ii__3950b409.yaml
- Started UTC: 2026-09-23T04:35:30Z
- Finished UTC: 2026-09-23T04:36:22Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:002247` / `freshwater_iron_oxidizing_bacteria_medium_ii`, the direct MediaDive/JCM Medium J1067 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/freshwater_iron_oxidizing_bacteria_medium_ii.yaml`.
- Cross-checked the MediaDive REST payload for J1067, the live JCM GRMD=1067 page, and the TOGO M1136 duplicate generated as `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium_ii.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J1067` correctly identifies JCM Medium 1067, FRESHWATER IRON-OXIDIZING BACTERIA MEDIUM-II.
- Exact ignored-inclusive lookup for `mediadive.medium:J1067`, `CultureMech:002247`, and `freshwater_iron_oxidizing_bacteria_medium_ii__3950b409` covered normalized and generated bacterial YAML; it found this single maintained JCM J1067 owner and the suffixed generated file.
- The direct JCM record lacks an explicit duplicate relationship to TOGO M1136 even though TOGO M1136 names JCM 1067 as its original source.
- The generated record is also stale relative to a September CaCl2 duplicate repair in normalized YAML.

## Evidence

- MediaDive represents J1067 with a main solution that contains FeS solution, Modified Wolfe's mineral solution, Noble agar, a second Modified Wolfe's mineral solution addition, Trace minerals, Trace vitamins, and 5.25 ml of 8% NaHCO3 solution.
- JCM 1067 preserves the intended layer boundaries: a bottom layer with 50 ml FeS, 50 ml Modified Wolfe's solution, and 1.5 g Agar, Noble, and a top layer with 1 L Modified Wolfe's solution plus 10 ml Trace minerals from JCM 151.
- The generated record flattens FeS, Modified Wolfe's, JCM 151 Trace minerals, and JCM 197 Trace vitamins into top-level ingredients; FeSO4, MgSO4, and CaCl2 were further summed across unrelated stocks.
- The generated NaHCO3 row is 5.25 g/L, but the source row is 5.25 ml of 8% NaHCO3 added per liter as a filter-sterilized stock.
- The generated preparation text preserves JCM 1067's autoclave, cooled top-layer addition, overlay, gas-phase, and storage comments, but its first two steps are only layer headings and no structured layer recipes remain.
- The generated file still has `CaCl2 x 2 H2O` summed to 0.2 g/L; the maintained source has a September repair that collapsed one identical duplicate-sum artifact back to 0.1 g/L.

## Completeness

- Bottom-layer and top-layer recipes are missing.
- FeS solution, Modified Wolfe's mineral solution, Trace minerals, Trace vitamins, and 8% NaHCO3 solution are missing as structured stocks.
- Trace mineral and vitamin components are present as unsupported top-level final-medium rows instead of as JCM 151/JCM 197 stock members.
- The cross-source TOGO M1136 duplicate remains generated as a separate record.

## Findings

- Major: direct JCM J1067 layer and stock topology was flattened into one top-level ingredient list; the fix belongs in `data/normalized_yaml/bacterial/freshwater_iron_oxidizing_bacteria_medium_ii.yaml` or the MediaDive/JCM importer.
- Major: FeS, Modified Wolfe's, Trace minerals, and Trace vitamins stock contents are represented as final-medium g/L ingredients and were summed where compounds recur across distinct stocks.
- Major: 5.25 ml/L of 8% NaHCO3 solution was imported as 5.25 g/L sodium bicarbonate.
- Major: the generated file missed the normalized September CaCl2 duplicate-sum repair.
- Major: direct JCM J1067 and TOGO M1136 remain generated as separate records without a duplicate relationship.
- Minor: the source-specific Agar, Noble (BD-Difco) supplied form is reduced to generic agar plus a partial `Noble` note.

## Recommended Edits

- Rebuild the maintained JCM J1067 record with explicit bottom-layer, top-layer, FeS, Modified Wolfe's, Trace minerals, Trace vitamins, and 8% NaHCO3 solution structure.
- Keep FeS and Modified Wolfe's stock components scoped under their JCM 628 stocks; keep Trace minerals under JCM 151 and Trace vitamins under JCM 197.
- Represent 8% NaHCO3 as a 5.25 ml/L filter-sterilized stock addition to the cooled top layer.
- Add a `SOURCE_DUPLICATE` relationship to TOGO M1136 or converge the JCM and TOGO imports into one generated record after both share equivalent layer topology.
- Regenerate `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium_ii__3950b409.yaml` after normalized/import curation so the existing CaCl2 duplicate repair is included.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J1067 YAML.
- Confirm stock components from FeS, Modified Wolfe's, Trace minerals, and Trace vitamins do not appear as top-level final-medium ingredients.
- Confirm 8% NaHCO3 is a volume stock addition, not a 5.25 g/L final ingredient.
- Confirm the direct JCM J1067 and TOGO M1136 records have an explicit duplicate relationship or generate as one reviewed record.

## Additional Notes

- TOGO M1136 already has a richer September repair for the same source recipe. The direct JCM/MediaDive owner can likely be reconciled against that repaired topology instead of recapturing JCM 1067 from scratch.
