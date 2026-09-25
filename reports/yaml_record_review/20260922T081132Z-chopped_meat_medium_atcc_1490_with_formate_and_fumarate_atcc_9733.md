# YAML Record Review: chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.yaml
- Started UTC: 2026-09-22T08:08:24Z
- Finished UTC: 2026-09-22T08:11:32Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009185 |
| Label | Chopped Meat Medium (ATCC 1490) with Formate and Fumarate (ATCC 9733) |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.yaml |
| Source | TOGO Medium M2618, ATCC Medium 1539 |

The reviewed file is a generated one-source merge of an ATCC Medium 1539 record
imported through TOGO M2618. The generated merge differs from the maintained
normalized owner only by the merge-history event and the `merge_fingerprint` /
`merged_from` footer, so future fixes belong in the normalized owner or in the
TOGO import, unit-conversion, and solution-migration logic rather than in the
generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Failed with 8 exact-snippet errors |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The reference validator rejected every `target_organisms[*].evidence[*].snippet`
and the `variants[1]` evidence snippet as not present verbatim in their cited
sources. The two `doi:10.1002/ptr.765` failures were against the cached
abstract, with a note that the full text might contain the excerpts.

## Identity and Grounding

The source identity is coherent: `CultureMech:009185`, `TOGO:M2618`, the
original ATCC URL fingerprint `78329ED2D2314D3BB1BC2F3BEAA2ECFB`, the
maintained owner stem, and the generated merge fingerprint all denote Chopped
Meat Medium (ATCC 1490) with Formate and Fumarate (ATCC 9733).

An ignored-independent `rg --no-ignore --hidden` search for the CultureMech ID,
TOGO M2618 ID, ATCC URL fingerprint, maintained owner stem, and merge
fingerprint found this generated record, its maintained owner, and normalized
index entries.

The medium term also points at the right TOGO source, but the imported formula
does not preserve the nested recipe identity of ATCC Medium 1490, Formate and
Fumarate Solution, Hemin Solution, or Vitamin K1 Solution.

## Evidence

The inspected ATCC Medium 1539 PDF supports the source formulation as
952.4 mL Chopped Meat Medium plus 47.6 mL Formate and Fumarate Solution,
anaerobically dispensed under N2:H2:CO2 at 80:10:10. Its Formate and Fumarate
Solution is a separate 6% / 6% stock made with 6.0 g sodium formate, 6.0 g
fumaric acid, and 100.0 mL DI water, adjusted to pH 7.0, filter sterilized,
and aseptically added to the chopped meat medium.

TOGO M2618 supports an ATCC Medium 1490 subrecipe made by boiling 1 L
distilled water, 25 mL 1 N NaOH, and 500 g fat-free ground beef; skimming and
filtering while retaining both meat particles and filtrate; restoring the
filtrate to 1.0 L; adding 4 mL 0.025% resazurin, 5 g yeast extract, 5 g
`K2HPO4`, 20 g agar, and 30 g Trypticase Peptone; boiling and cooling under
80% N2, 10% H2, and 10% CO2; adding 0.5 g L-cysteine HCl, 10 mL Hemin
Solution, and 0.2 mL Vitamin K1 Solution; adjusting the final pH to 7.0; and
anaerobically dispensing 7 mL into tubes containing one part meat particles to
five parts fluid under the same gas phase.

TOGO M2618 also supports separate stock boundaries for Hemin Solution, Vitamin
K1 Solution, and Formate and Fumarate Solution. The record flattens all of
those stock internals into final-medium ingredients while retaining the added
stock volumes only as empty `G_PER_L` solution shells. The 952.4 mL ATCC
Medium 1490 and 47.6 mL Formate and Fumarate Solution additions likewise become
`G_PER_L` entries; 1 L ATCC 1490 water becomes 1 g/L; the 25 mL ATCC 1490
NaOH and 1 mL Hemin-stock NaOH are merged into 26 g/L; 4 mL resazurin becomes
4 g/L; 30 mL 95% ethanol, 0.15 mL Vitamin K1, 100 mL Hemin-stock water,
50 mg hemin, and 100 mL DI water for Formate and Fumarate Solution are all
modeled as direct `G_PER_L` parent-medium ingredients.

O'Hanlon et al. 2011 supports Bacteroides ureolyticus ATCC 33387 on ATCC
medium 1490 with formate and fumarate, and it supports Lactobacillus crispatus
ATCC 33820, Fusobacterium nucleatum ATCC 25586, Porphyromonas levii ATCC
29147, and Prevotella bivia ATCC 29303 on the plain ATCC medium 1490 variant.
Kleniewska et al. 2023 supports Parabacteroides distasonis ATCC 8503 on ATCC
1490 Modified Chopped Meat medium. The current snippets for those assertions
are source-aligned in meaning, but are not exact source substrings and fail
reference validation.

The two Fusobacterium necrophorum ATCC 27852 assertions cite Johnston et al.
2001. The reference cache exposes only the abstract, the DOI URL resolves to a
Wiley Cloudflare JavaScript challenge even with a browser user agent, and the
carbonate/CO2-buffered ATCC 1490 method could not be verified from inspected
full text during this review.

## Completeness

The record is incomplete until ATCC Medium 1490, Formate and Fumarate
Solution, Hemin Solution, and Vitamin K1 Solution are represented as bounded
subrecipes or solution references with source-faithful units, dilution
arithmetic, pH values, gas phase, and preparation steps.

The empty growth-observation fields are not defects here. The record already
names the medium variants that own the plain ATCC 1490 and carbonate/CO2
growth evidence.

## Findings

| Severity | Finding |
| --- | --- |
| Blocker | The generated record fails reference validation with 8 non-verbatim evidence snippets across all seven `target_organisms` entries and one medium-variant entry. **Owner:** `data/normalized_yaml/bacterial/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.yaml`. |
| Major | The Fusobacterium necrophorum ATCC 27852 growth claim and the `atcc_1490_carbonate_co2_buffered` variant cite `doi:10.1002/ptr.765`, but only the abstract was available to the validator and a direct Wiley fetch was blocked by a Cloudflare JavaScript challenge; the carbonate/CO2 medium claim is therefore unverified. **Owner:** the same maintained normalized owner. |
| Major | The parent medium incorrectly contains both the 952.4 mL ATCC Medium 1490 addition and the internals of ATCC Medium 1490 as direct ingredients. **Owner:** the maintained normalized owner or the TOGO nested-medium importer. |
| Major | Formate and Fumarate Solution, Hemin Solution, and Vitamin K1 Solution are flattened into parent ingredients while their final-medium addition volumes are kept as empty `G_PER_L` solution shells. **Owner:** the maintained normalized owner or solution migration. |
| Major | Multiple source volumes and milligram amounts are converted to `G_PER_L`, and the 25 mL ATCC 1490 NaOH addition is merged with the 1 mL Hemin-stock NaOH addition into a single 26 g/L parent ingredient. **Owner:** the TOGO import and unit-conversion logic. |
| Major | pH and preparation evidence is mostly absent: ATCC 1539 gas dispensing, Formate and Fumarate Solution pH 7.0 and filter sterilization, the ATCC 1490 meat-filtrate workflow, 80:10:10 gas handling, final pH 7.0, tube dispensing with meat particles, and Vitamin K1/Hemin stock handling are not represented. **Owner:** the maintained normalized owner or the TOGO importer. |

## Recommended Edits

1. Replace all seven target-organism snippets and both variant snippets with
   exact, source-verbatim text. For Johnston et al. 2001, first inspect the
   full text; if the full text is unavailable, mark the carbonate/CO2 variant
   evidence unresolved rather than keeping the current unverified snippets.
2. Model 952.4 mL ATCC Medium 1490 and 47.6 mL Formate and Fumarate Solution
   as component or stock additions, not as gram-per-litre direct ingredients.
3. Preserve Formate and Fumarate Solution, Hemin Solution, and Vitamin K1
   Solution as separate stock recipes or solution references and keep their
   internal ingredients scoped to those stocks.
4. Preserve source units for millilitre and milligram quantities and prevent
   duplicate merging of NaOH entries from different recipe scopes.
5. Add supported pH, gas-phase, sterilization, stock-storage, aseptic-addition,
   meat-filtrate, and 7 mL dispensing steps from TOGO M2618 and ATCC Medium
   1539.
6. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against ATCC Medium 1539, TOGO
M2618, O'Hanlon et al. 2011, Kleniewska et al. 2023, and the inspected
Johnston et al. 2001 full text to confirm the solution boundaries, source
units, pH values, gas phase, preparation sequence, growth-evidence snippets,
and variant-scoped growth assertions are source-faithful.

## Additional Notes

The bounded Wiley retry covered `https://doi.org/10.1002/ptr.765` with a
browser user agent and landed on a Cloudflare JavaScript challenge rather than
the Johnston et al. 2001 full text.
