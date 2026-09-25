# YAML Record Review: CHOPPED MEAT MEDIUM FOR FRETIBACTERIUM SP.

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_for_fretibacterium_sp.yaml
- Started UTC: 2026-09-22T08:13:08Z
- Finished UTC: 2026-09-22T08:15:08Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001929 |
| Label | CHOPPED MEAT MEDIUM FOR FRETIBACTERIUM SP. |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_for_fretibacterium_sp.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_medium_for_fretibacterium_sp.yaml |
| Source | DSMZ Medium 78c via MediaDive |

The reviewed file is a generated one-source merge of a MediaDive import. The
generated merge differs from the maintained normalized owner only by the
merge-history event and the `merge_fingerprint` / `merged_from` footer, so
future fixes belong in the normalized owner or in the MediaDive importer and
post-import enrichment steps rather than in the generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_for_fretibacterium_sp.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The stable source identity is coherent: `CultureMech:001929`, the
`mediadive.medium:78c` source CURIE, the normalized owner stem, and the
generated merge fingerprint all denote DSMZ Medium 78c. DSMZ's PDF title
misspells Fretibacterium as `FERTIBACTERIUM`; the record's corrected
Fretibacterium spelling is appropriate.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml`, `data/merge_yaml/merged`, the registry and catalog
TSVs, and `data/import_tracking/reports` for the CultureMech ID, MediaDive
source CURIE, DSMZ PDF token, maintained owner stem, and merge fingerprint
found this generated record, its maintained owner, normalized indexes, and
diagnostic registry or import-tracking rows for this same record.

The imported DSMZ source identity is undermined by unrelated Luria-Bertani
product provenance in `notes` and by LB-derived ingredients inserted into the
DSMZ 78c formula.

## Evidence

The inspected DSMZ Medium 78c PDF supports a base medium containing 500 g
fat-free ground beef, 25 mL 1 N NaOH, 30 g Casein peptone, 5 g yeast extract,
5 g `K2HPO4`, 0.5 mL 0.1% sodium resazurin, 0.5 g L-cysteine HCl x H2O,
6 g Na-fumarate, 6 g Na-formate, 50 mL clarified rumen fluid, 50 mL horse
serum, 20 mL fatty acid mixture, 1 mL Wolin's vitamin solution (10x), 5 mL
0.05% Haemin solution, 2 mL 0.05% Vitamin K1 solution, 0.3 g
DL-Dithiothreitol, and distilled water to 700 mL before later stock additions.
It supports pH 7.0 after 80% N2 / 20% CO2 sparging, Hungate tubes with about
7 mL liquid medium per 1 to 2 g meat particles, autoclaving at 121 C for 20
minutes, and post-autoclave addition of fumarate, formate, rumen fluid, horse
serum, fatty acids, vitamins, haemin, vitamin K1, and DTT from sterile anoxic
stocks prepared under 100% N2 and sterilized by filtration.

The PDF also supports four separate stock recipes:

| Stock | Supported composition |
| --- | --- |
| Clarified rumen fluid | Rumen fluid filtered through muslin, autoclaved at 121 C for 15 minutes, centrifuged at 27,000 g for 20 minutes, sparged with 100% N2, and stored frozen at -20 C |
| Fatty acid mixture | 23 mL isobutyric acid, 27 mL DL-2-methylbutyric acid, 27 mL valeric acid, 27 mL isovaleric acid, and 896 mL distilled water, adjusted to pH 7.5 with concentrated NaOH |
| Haemin solution | 50 mg haemin, 1 mL 1 N NaOH, and distilled water to 100 mL, filter sterilized and stored refrigerated |
| Vitamin K1 solution | 0.1 mL Vitamin K1 and 20 mL 95% ethanol, filter sterilized and stored refrigerated in a brown bottle |
| Wolin's vitamin solution (10x) | Biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-(+)-pantothenate, Vitamin B12, p-aminobenzoic acid, and (DL)-alpha-lipoic acid in 1000 mL distilled water |

The record flattens the fatty acid, Haemin, Vitamin K1, and Wolin vitamin
stock internals into parent-medium ingredients instead of representing the
20 mL, 5 mL, 2 mL, and 1 mL stock additions. It also drops DL-2-methylbutyric
acid, all source water quantities, and the clarified rumen fluid addition.

The note block beginning `Commercial Product: LB Medium (Luria-Bertani, Miller
formulation)` has no support in the DSMZ Medium 78c source. Its three derived
ingredients, Tryptone at 10 g/L, duplicate Yeast extract at 5 g/L, and Sodium
chloride at 10 g/L, are likewise unrelated to this medium.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this DSMZ recipe.

The formula is incomplete until the parent medium and five source stock
recipes are separated. In the parent medium, the record needs explicit
post-autoclave additions for clarified rumen fluid, horse serum, fatty acid
mixture, Wolin's vitamin solution, Haemin solution, Vitamin K1 solution,
Na-formate, Na-fumarate, and DTT. In stock scope, it needs DL-2-methylbutyric
acid and the source water quantities for the fatty acid, Haemin, and Wolin
solutions.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The DSMZ 78c record contains unsupported LB Medium provenance and three LB-derived direct ingredients: Tryptone 10 g/L, a duplicate Yeast extract 5 g/L, and Sodium chloride 10 g/L. **Owner:** `data/normalized_yaml/bacterial/chopped_meat_medium_for_fretibacterium_sp.yaml` or the commercial-product enrichment that inserted the LB block. |
| Major | Fatty acid mixture, Wolin's vitamin solution, Haemin solution, and Vitamin K1 solution are flattened into direct parent ingredients, so stock concentrations are being asserted as final-medium `G_PER_L` concentrations. **Owner:** the maintained normalized owner or the MediaDive stock importer. |
| Major | Required source ingredients are missing or scoped away: clarified rumen fluid, DL-2-methylbutyric acid, distilled water for the base medium, and water for the fatty acid, Haemin, and Wolin stocks are absent. **Owner:** the maintained normalized owner or the MediaDive importer. |
| Major | Millilitre quantities and stock concentrations are modeled as parent `G_PER_L` masses, including NaOH, horse serum, the fatty-acid stock members, haemin, Vitamin K1, ethanol, and all Wolin vitamin members. **Owner:** the MediaDive unit-conversion and solution-migration logic. |
| Major | The 25 mL base 1 N NaOH and the 1 mL Haemin-stock 1 N NaOH were merged into 26 g/L direct sodium hydroxide, losing stock scope and changing the supplied form from 1 N NaOH solution to solid sodium hydroxide. **Owner:** duplicate merging plus solution migration. |

## Recommended Edits

1. Remove the unsupported LB Medium note block and its LB-only Tryptone,
   duplicate Yeast extract, and Sodium chloride ingredients.
2. Keep fatty acid mixture, Wolin's vitamin solution, Haemin solution, Vitamin
   K1 solution, and clarified rumen fluid as separate stock recipes or
   bounded solution additions.
3. Restore source units and addition amounts: 50 mL clarified rumen fluid,
   50 mL horse serum, 20 mL fatty acid mixture, 1 mL Wolin's vitamin solution,
   5 mL Haemin solution, 2 mL Vitamin K1 solution, 6 g Na-fumarate, 6 g
   Na-formate, and 0.3 g DTT.
4. Add the missing DL-2-methylbutyric acid and stock-water quantities.
5. Keep 1 N NaOH additions scoped to the base medium and Haemin stock rather
   than merging them or grounding them as solid sodium hydroxide.
6. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against the DSMZ Medium 78c PDF to
confirm that the parent medium, clarified rumen fluid, fatty acid mixture,
Haemin solution, Vitamin K1 solution, and Wolin's vitamin solution retain their
source quantities, units, preparation boundaries, pH values, and gas handling.

## Additional Notes

MuPDF text extraction succeeded on the DSMZ PDF after `pypdf` returned no
extractable page text.
