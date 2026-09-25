# YAML Record Review: CHOPPED MEAT MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium__04a0e620.yaml
- Started UTC: 2026-09-22T07:56:28Z
- Finished UTC: 2026-09-22T07:56:56Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001926 |
| Label | CHOPPED MEAT MEDIUM |
| Generated record | data/merge_yaml/merged/chopped_meat_medium__04a0e620.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_medium.yaml |
| Source | DSMZ Medium 78 through MediaDive |

The reviewed file is a generated one-source merge of DSMZ Medium 78 from the
MediaDive/DSMZ import. Future fixes belong in the maintained normalized owner
or in the MediaDive importer and solution-normalization logic rather than in the
generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium__04a0e620.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:001926`, `mediadive.medium:78`,
the maintained owner stem, and the generated merge fingerprint all denote DSMZ
78 Chopped Meat Medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID and
merge fingerprint found this generated record, its maintained owner, and
normalized index entries. A source-ID search for `mediadive.medium:78` also
finds intentional DSMZ 78 variants and numeric siblings such as `78a`, `78b`,
and `780`, so exact identity for this review was resolved by the CultureMech ID
and merge fingerprint.

## Evidence

DSMZ Medium 78 supports a base chopped-meat medium with 500.0 g fat-free ground
beef or horse meat, 1000.0 mL distilled water, and 25.0 mL 1 N NaOH in the
initial meat stage. The filtrate is restored to a final volume of 1000 mL and
receives 30.0 g Casitone, 5.0 g yeast extract, 5.0 g `K2HPO4`, and 1.0 mg
resazurin. The medium is then boiled, cooled under 100% N2, supplemented with
0.5 g/L L-cysteine hydrochloride, adjusted to pH 7.0, dispensed as 7 mL into
anoxic Hungate-type tubes under 100% N2, and autoclaved at 121 C for
30 minutes. Agar is used only for agar slants.

The source separately says that, only in some indicated cases, Haemin and
Vitamin K1 or Vitamin K3 are added after autoclaving. Their stock recipes are
separate solution preparations: 50 mg haemin in 1 mL 1 N NaOH made to 100 mL
with water, 0.1 mL Vitamin K1 in 20 mL 95% ethanol, and Vitamin K3 diluted to
0.05 mg/mL.

The record imports the base medium as if it had a 1.025 L denominator and stores
500 g ground beef as 487.805 g/L, 30 g Casitone as 29.2683 g/L, 5 g yeast
extract and 5 g `K2HPO4` as 4.87805 g/L, 1 mg resazurin as 0.00097561 g/L,
0.5 g/L L-cysteine as 0.487805 g/L, and optional 15 g agar as 14.6341 g/L. DSMZ
instead restores the filtrate to a final 1000 mL before the main additions and
states L-cysteine as 0.5 g/L.

The record flattens optional Haemin, Vitamin K1, and Vitamin K3 stock recipes
into unconditional base-medium ingredients. It also merges the base 25 mL NaOH
with the 1 mL NaOH from Haemin solution and merges ethanol amounts from vitamin
stocks into a 959.5 g/L parent ingredient.

The preparation text contains real DSMZ prose, but the steps are out of order
and misclassified: anoxia/autoclaving precedes beef grinding, the beef-filtrate
preparation is marked `FILTER_STERILIZE`, and post-autoclave optional stock
instructions are mixed into the base workflow.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this DSMZ source record.

The recipe is incomplete until the base chopped-meat medium is separated from
optional vitamin and haemin stocks, the formula uses the source's 1000 mL final
volume, optional agar is kept optional, the 100% N2 gas phase is represented,
and preparation steps are ordered and typed according to the source.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The base DSMZ Medium 78 ingredient amounts are rescaled against an unsupported 1.025 L denominator instead of DSMZ's 1000 mL final volume. **Owner:** `data/normalized_yaml/bacterial/chopped_meat_medium.yaml` or the MediaDive/DSMZ importer. |
| Major | Optional Haemin, Vitamin K1, and Vitamin K3 stock recipes are flattened into unconditional parent ingredients and duplicate stock components are merged with base components. **Owner:** the maintained normalized owner or solution-normalization logic. |
| Major | The record is unconditionally `SOLID_AGAR` and includes agar, but the source reserves agar for optional agar slants. **Owner:** the maintained normalized owner or the MediaDive/DSMZ importer. |
| Major | Preparation steps are source-derived but ordered and classified incorrectly, with the beef-filtrate stage placed after autoclaving and marked as filter sterilization. **Owner:** the preparation-step importer. |

## Recommended Edits

1. Recalculate the base chopped-meat formula against DSMZ's restored 1000 mL
   final volume and preserve the 0.5 g/L L-cysteine value.
2. Move Haemin, Vitamin K1, and Vitamin K3 internals into optional post-
   autoclave stock-solution records instead of unconditional parent
   ingredients.
3. Remove agar from the base formula or mark it as an optional agar-slant
   addition.
4. Reorder and reclassify the preparation steps so beef grinding and filtrate
   preparation precede boiling, anoxic cooling, cysteine addition, pH
   adjustment, Hungate-tube dispensing, and autoclaving.
5. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against DSMZ Medium 78 to confirm
the base formula, optional post-autoclave stocks, agar handling, 100% N2 gas
phase, and preparation order are source-faithful.

## Additional Notes

The generated record still carries a legacy `mediaingredientmech_term` for
L-Cysteine HCl without a current `mediaingredientmech_chebi_term`, despite the
`mim-legacy-to-chebi-migration-v1.0` curation event.
