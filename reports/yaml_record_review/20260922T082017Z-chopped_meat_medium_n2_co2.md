# YAML Record Review: CHOPPED MEAT MEDIUM (N2/CO2)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_n2_co2.yaml
- Started UTC: 2026-09-22T08:19:23Z
- Finished UTC: 2026-09-22T08:20:30Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001928 |
| Label | CHOPPED MEAT MEDIUM (N2/CO2) |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_n2_co2.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_medium_n2_co2.yaml |
| Source | DSMZ Medium 78b via MediaDive |

The reviewed file is a generated one-source merge of the MediaDive DSMZ 78b
normalized owner. Future source corrections belong in
`data/normalized_yaml/bacterial/chopped_meat_medium_n2_co2.yaml` or the
MediaDive importer; this generated merge needs regeneration after the
September 2026 normalized repair.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed; reported `No issues found` |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_n2_co2.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is coherent: `CultureMech:001928`, `mediadive.medium:78b`,
the DSMZ Medium 78b PDF token, the maintained owner stem, and the generated
merge fingerprint all denote liquid DSMZ Chopped Meat Medium under N2/CO2.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml`, `data/merge_yaml/merged`, the registry and catalog
TSVs, and `data/import_tracking/reports` for the CultureMech ID, MediaDive
source CURIE, DSMZ PDF token, maintained owner stem, and merge fingerprint
found this generated record, its maintained owner, normalized indexes, the
related KOMODO 78b normalized records, and diagnostic registry or
import-tracking rows for this source family.

The generated record no longer agrees with its maintained owner. The owner was
repaired on 2026-09-12, removes optional Haemin and Vitamin K stock internals
from the final ingredient list, keeps this recipe as liquid DSMZ 78b, adds
references, and names KOMODO 78b as a strain-specific variant child. The
generated record still reflects an older pre-repair state.

## Evidence

The inspected DSMZ Medium 78b PDF supports a liquid chopped-meat medium made
from 500 g fat-free ground beef, 25 mL 1 N NaOH, 30 g Casitone, 5 g yeast
extract, 5 g `K2HPO4`, 0.5 mL 0.1% sodium resazurin, 0.5 g L-Cysteine HCl x
H2O, and 1000 mL distilled water. The preparation uses lean beef or horse meat,
brings meat, water, and NaOH to a boil for 15 minutes, filters while retaining
meat particles and filtrate, adds nutrients and water to 700 mL, sparges with
80% N2 / 20% CO2 for 30 to 45 minutes, adjusts to pH 7.0 after cysteine,
dispenses under the same gas phase into Hungate tubes with meat particles, and
autoclaves at 121 C for 20 minutes.

DSMZ lists Haemin, Vitamin K1, and Vitamin K3 as optional post-autoclave stocks
for cases indicated in the catalogue. The source represents them as separate
filter-sterilized stocks with explicit 10 mL, 10 mL, and 1 mL optional
post-autoclave additions; their haemin, Vitamin K1, Vitamin K3, NaOH, ethanol,
and water internals are not unconditional DSMZ 78b final-medium ingredients.

The generated record still flattens all three optional stocks into the parent
ingredient list. It merges the base-medium 25 mL 1 N NaOH with Haemin-stock
1 mL 1 N NaOH into a 26 g/L solid-sodium-hydroxide ingredient, merges 95%
ethanol from Vitamin K1 and Vitamin K3 into one 959.5 g/L parent ingredient,
and asserts stock-internal haemin, Vitamin K1, and Vitamin K3 as direct parent
ingredients.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this DSMZ source record.

The generated record is stale relative to the maintained owner: it is missing
the owner record's `references`, `data_quality_flags`, 2026-09-12 repair
history, and KOMODO 78b `variant_children` link, while containing optional
stock internals that the owner already removed.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The generated record is stale relative to the maintained owner repaired on 2026-09-12: it still includes optional Haemin, Vitamin K1, Vitamin K3, NaOH, and ethanol stock internals as direct final-medium ingredients. **Owner:** regenerate `data/merge_yaml/merged/chopped_meat_medium_n2_co2.yaml` from `data/normalized_yaml/bacterial/chopped_meat_medium_n2_co2.yaml`. |
| Major | The generated record omits owner-only curation added in the 2026-09-12 repair, including source references, data-quality flags, and the KOMODO 78b strain-specific variant child. **Owner:** regenerated merge output. |
| Major | The stale generated recipe merges source quantities across scopes: 25 mL base 1 N NaOH plus 1 mL Haemin-stock 1 N NaOH become one 26 g/L solid-sodium-hydroxide entry, and separate optional Vitamin K ethanol stocks become one 959.5 g/L parent entry. **Owner:** already fixed in the maintained owner; rerun the merge. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/chopped_meat_medium_n2_co2.yaml` from the
   current maintained owner.
2. Keep Haemin, Vitamin K1, and Vitamin K3 internals out of the DSMZ 78b
   final-medium ingredient list unless a specific catalogue case needs one of
   those optional stock additions.
3. Preserve the KOMODO 78b Treponema parvum record as a strain-specific child
   of DSMZ 78b rather than mixing its variant metadata into this parent.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then diff the regenerated record against the repaired maintained owner to
confirm that the generated ingredients, references, data-quality flags,
variant child, and curation history reflect the 2026-09-12 repair without
reintroducing optional Haemin or Vitamin K stock internals.

## Additional Notes

None found.
