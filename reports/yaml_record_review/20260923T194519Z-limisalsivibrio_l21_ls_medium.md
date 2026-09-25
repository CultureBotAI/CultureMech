# YAML Record Review: LIMISALSIVIBRIO (L21 LS) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/limisalsivibrio_l21_ls_medium.yaml
- Started UTC: 2026-09-23T19:42:38Z
- Finished UTC: 2026-09-23T19:45:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001001 |
| Name | limisalsivibrio_l21_ls_medium |
| Original name | LIMISALSIVIBRIO (L21 LS) MEDIUM |
| Category | bacterial |
| Medium/composition type | DEFINED / DEFINED |
| Physical state | LIQUID |
| Structured pH | 6.8-7.0 |
| Media grounding | mediadive.medium:1526d |
| Source provenance | DSMZ Medium 1526d via MediaDive |
| Generated file | data/merge_yaml/merged/limisalsivibrio_l21_ls_medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml |
| Merge fingerprint | 52b95f7f4c1e50b40c973627361f76f4f5502bd08cb223203750633dd7163aec |

The reviewed target is a generated one-source DSMZ/MediaDive merge. Future fixes belong in `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml`, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/limisalsivibrio_l21_ls_medium.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/limisalsivibrio_l21_ls_medium.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The DSMZ PDF and the MediaDive REST record agree that DSMZ Medium 1526d is `LIMISALSIVIBRIO (L21 LS) MEDIUM`, a defined liquid medium from DSMZ with pH 6.8-7.0 and nested `Modified Wolin's mineral solution` and `Seven vitamins solution` stock recipes.

The generated record keeps the DSMZ/MediaDive source identity, stable `CultureMech:001001` ID, label, category, pH, and MediaDive source accession. It does not keep the DSMZ and MediaDive solution boundaries in the ingredient structure.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:001001`, `mediadive.medium:1526d`, `DSMZ_Medium1526d`, the maintained filename, the merge fingerprint, and the shared slug found this generated record, its maintained owner, and normalized source indexes.

## Evidence

Supported in the inspected DSMZ and MediaDive sources:

- The main medium has 60 g NaCl, 6 g MgCl2 x 6 H2O, 1.5 g KCl, 1 g Na2SO4, 1 g NH4Cl, 0.4 g CaCl2 x 2 H2O, 0.4 g K2HPO4, 0.5 ml sodium resazurin at 0.1 percent w/v, 1 g Na2CO3, 1.6 g Na-acetate, 6.4 g Na2-fumarate, 0.5 g Na2S x 9 H2O, and 1000 ml distilled water.
- The main medium adds `Modified Wolin's mineral solution` at 10 ml and `Seven vitamins solution` at 1 ml.
- The DSMZ and MediaDive Modified Wolin mineral stock has 15 non-water components in 1000 ml distilled water, including 1 g/L NaCl, 0.1 g/L CaCl2 x 2 H2O, 0.03 g/L NiCl2 x 6 H2O, 0.3 mg/L Na2SeO3 x 5 H2O, and 0.4 mg/L Na2WO4 x 2 H2O.
- The DSMZ and MediaDive Seven vitamins stock has seven vitamin components in 1000 ml distilled water: Vitamin B12, p-Aminobenzoic acid, D-(+)-biotin, Nicotinic acid, Calcium pantothenate, Pyridoxine hydrochloride, and Thiamine-HCl x 2 H2O.
- The main preparation, mineral solution pH-adjustment instruction, final pH range, anoxic gas mix, autoclave step, and filter-sterilized fumarate/vitamin stock note match the source text.

Unsupported or incomplete in the generated record:

- Stock recipes are flattened as if their stock concentrations were top-level medium concentrations; the generated rows list 1.5 g/L nitrilotriacetic acid and 3 g/L MgSO4 x 7 H2O, for example, rather than a 10 ml/L `Modified Wolin's mineral solution`.
- NaCl is stored as 60.3472 g/L with the note `[Merged 2 duplicates: 59.3472, 1.0]`, and CaCl2 x 2 H2O is stored as 0.495648 g/L with the note `[Merged 2 duplicates: 0.395648, 0.1]`. MediaDive places the 1.0 g/L NaCl and 0.1 g/L CaCl2 amounts inside the mineral stock, not at the same level as the converted main solution.
- All seven `Seven vitamins solution` rows are flattened in the generated record. The maintained owner has an unmerged 2026-08-07 `apply_cocktail_nesting.py` event that moved four rows into a `Seven vitamins solution`, but the generated target does not include that solution yet and the owner still leaves p-Aminobenzoic acid, D-(+)-biotin, and Calcium pantothenate top-level.
- NiCl2 x 6 H2O is grounded to CHEBI:34887 / nickel dichloride, which loses the hexahydrate form asserted by DSMZ.
- The generated record has no structured reference to DSMZ Medium 1526d or MediaDive medium 1526d.

## Completeness

The record is complete for the source identity, DSMZ label, high-level classification, pH range, all non-water source component names, and the two source preparation paragraphs.

It is incomplete for stock-solution nesting, water rows for the main and two stock recipes, exact hydrate grounding for NiCl2 x 6 H2O, and structured source references. Empty optional target-organism, incubation, storage, and growth-evidence fields are acceptable for this review because the inspected DSMZ Medium 1526d and MediaDive records do not list a strain, incubation recipe, storage condition, or primary growth result.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | `Modified Wolin's mineral solution` is flattened and stock concentrations are exposed as main-medium ingredient concentrations. | DSMZ and MediaDive add `Modified Wolin's mineral solution` at 10 ml; the generated YAML instead lists its 1 L stock rows, such as 1.5 g/L nitrilotriacetic acid and 3 g/L MgSO4 x 7 H2O, as top-level medium ingredients. | `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` |
| Major | NaCl and CaCl2 x 2 H2O were merged across different solution contexts. | MediaDive reports 59.3472 g/L NaCl and 0.395648 g/L CaCl2 x 2 H2O after normalizing the main solution, then lists separate 1 g/L NaCl and 0.1 g/L CaCl2 x 2 H2O rows inside the mineral stock; the generated record sums those pairs into 60.3472 and 0.495648 g/L. | `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` or the duplicate-merging logic |
| Major | `Seven vitamins solution` is absent from the generated target and incomplete in the maintained owner. | DSMZ and MediaDive add seven vitamins as a 1 ml stock solution. The generated target flattens all seven; the owner now nests only Vitamin B12, Nicotinic acid, Pyridoxine hydrochloride, and Thiamine-HCl x 2 H2O, leaving three stock ingredients at top level. | `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` |
| Major | NiCl2 x 6 H2O is over-broadly grounded. | DSMZ names nickel chloride hexahydrate in the Modified Wolin stock, while the YAML points that ingredient at CHEBI:34887 / nickel dichloride. | `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` |
| Minor | Distilled water rows are missing. | DSMZ and MediaDive list 1000 ml distilled water in the main recipe, the Modified Wolin stock, and the Seven vitamins stock; no water component or equivalent stock volume is represented in the generated target. | `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` |
| Minor | Structured references are missing. | The generated target carries only a free-text DSMZ URL in `notes`, and the reference validator performed zero checks. | `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` |

## Recommended Edits

1. Complete the `Seven vitamins solution` nesting in `data/normalized_yaml/bacterial/limisalsivibrio_l21_ls_medium.yaml` so all seven DSMZ/MediaDive vitamin rows live under that solution at 1 ml/L.
2. Add a nested `Modified Wolin's mineral solution` at 10 ml/L and move all 15 stock rows, including stock NaCl and stock CaCl2 x 2 H2O, under that solution.
3. Undo the cross-solution NaCl and CaCl2 x 2 H2O duplicate sums so the main-medium rows keep only the source main-solution quantities and the mineral-stock rows stay inside the mineral stock.
4. Replace the NiCl2 x 6 H2O CHEBI grounding with a hydrate-specific term if one is available in the ingredient index; otherwise leave the exact preferred term unresolved instead of grounding it to anhydrous nickel dichloride.
5. Preserve the main-recipe, mineral-stock, and vitamin-stock 1000 ml water context in the model, either as water components where supported or as stock preparation notes with 1 L final volumes.
6. Add structured references for MediaDive medium 1526d and the DSMZ Medium 1526d PDF.
7. Regenerate `data/merge_yaml/merged/` and downstream pages so the 2026-08-07 owner-side solution nesting and the new curation are reflected in this generated target.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against DSMZ Medium 1526d for the 10 ml Modified Wolin stock, the 1 ml Seven vitamins stock, the three 1000 ml water rows, and the two preparation paragraphs.
- Re-run an ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:001001`, `mediadive.medium:1526d`, `DSMZ_Medium1526d`, and `limisalsivibrio_l21_ls_medium` after regeneration to confirm the source owner, source indexes, and regenerated merge agree.

## Additional Notes

The DSMZ preparation paragraph says to add cysteine from a sterile anoxic stock solution even though the DSMZ 1526d PDF and MediaDive 1526d structured recipe do not list a cysteine amount. That source inconsistency should be kept visible as a quality flag if the maintained owner is curated.
