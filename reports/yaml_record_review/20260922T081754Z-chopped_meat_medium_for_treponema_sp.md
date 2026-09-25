# YAML Record Review: CHOPPED MEAT medium FOR TREPONEMA SP

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_for_treponema_sp.yaml
- Started UTC: 2026-09-22T08:16:23Z
- Finished UTC: 2026-09-22T08:18:21Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:006493 |
| Label | CHOPPED MEAT medium FOR TREPONEMA SP |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_for_treponema_sp.yaml |
| Canonical maintained owner | data/normalized_yaml/bacterial/KOMODO_78a_CHOPPED_MEAT_medium_FOR_TREPONEMA_SP.yaml |
| DSMZ duplicate source | data/normalized_yaml/bacterial/chopped_meat_medium_for_treponema_sp.yaml |
| Sources | KOMODO Medium 78a; DSMZ Medium 78a and Medium 78 |

The reviewed file is a generated 44-source merge whose canonical source is the
KOMODO 78a normalized record. The generated filename matches the separate
MediaDive DSMZ 78a duplicate stem, but not its `CultureMech:001927` ID. Future
formula fixes belong in the KOMODO/MediaDive normalized source records, the
DSMZ resolver, or the duplicate-merge logic rather than in this generated
merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_for_treponema_sp.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source IDs line up with one DSMZ 78a / KOMODO 78a Treponema medium, but
the merge obscures two identity boundaries:

| Scope | Current state |
| --- | --- |
| Generated record | `CultureMech:006493`, `komodo.medium:78a`, generated at `data/merge_yaml/merged/chopped_meat_medium_for_treponema_sp.yaml` |
| Canonical normalized owner | `data/normalized_yaml/bacterial/KOMODO_78a_CHOPPED_MEAT_medium_FOR_TREPONEMA_SP.yaml` |
| MediaDive duplicate | `CultureMech:001927`, `mediadive.medium:78a`, `data/normalized_yaml/bacterial/chopped_meat_medium_for_treponema_sp.yaml` |
| Parent | `CultureMech:006491`, KOMODO Chopped Meat Medium, recorded as a `SOURCE_DUPLICATE` parent |

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml`, `data/merge_yaml/merged`, the registry and catalog
TSVs, and `data/import_tracking/reports` for `CultureMech:006493`,
`komodo.medium:78a`, the canonical owner stem, the generated merge
fingerprint, and the generated record stem found the generated record, the
KOMODO canonical owner, the separate MediaDive 78a duplicate, the parent
KOMODO 78 record, normalized indexes, and diagnostic registry or
import-tracking rows for this merge set.

The synonym set is overbroad for a record labelled "for Treponema sp.": the
merge now lists 44 KOMODO source IDs, including DSMZ 78 base, DSMZ 78b for
Treponema parvum, an anoxic version, and many strain-specific `78_*` variants.
Those sources need to be reviewed as parent/variant relationships or
strain-specific variants, not collapsed into exact synonyms merely because
the imported ingredient fingerprints matched after information loss.

## Evidence

The inspected DSMZ Medium 78a PDF supports this record as a supplement to
ready DSMZ Medium 78: to 1 L of ready medium 78, add 50 mL/L amino acid
solution and 5 mL/L vitamin solution, and do not prepare those two solutions
under anaerobic conditions.

The 78a amino acid solution is a filtered stock containing 0.6 g L-Histidine,
0.5 g L-Serine, 0.7 g L-Glutamine, and 50 mL distilled water. The vitamin
solution contains 50 mg Vitamin B12, 50 mg pantothenic acid, 50 mg riboflavin,
10 mg pyridoxamine HCl, 20 mg biotin, 20 mg folic acid, 25 mg nicotinic acid,
25 mg nicotinamide, 50 mg alpha-lipoic acid, 50 mg p-aminobenzoic acid,
50 mg thiamine-HCl x 2 H2O, and distilled water to 1000 mL; it is stirred for
some hours and filter sterilized.

The inspected DSMZ Medium 78 PDF supports a separate chopped-meat base medium,
not direct Treponema-supplement ingredients. Its meat-filtrate stage begins
with 500 g fat-free ground beef, 1000 mL distilled water, and 25 mL 1 N NaOH;
it adds Casitone, yeast extract, `K2HPO4`, 1 mg resazurin, and 0.5 g/L
L-cysteine HCl; it uses pH 7.0, 100% N2 dispensing, 121 C autoclaving for 30
minutes, and optional 15 g/L agar for slants. Haemin, Vitamin K1, and Vitamin
K3 are optional post-autoclave stocks, added only in cases indicated by the
catalogue.

The reviewed record flattens the 78a amino-acid and vitamin stock
concentrations into the parent medium. For example, 0.6 g L-Histidine in
50 mL amino-acid stock becomes 12 g/L in the final medium, and 50 mg Vitamin
B12 in a 1000 mL vitamin stock becomes 0.05 g/L in the final medium instead
of a 5 mL/L stock addition. Both stock water quantities are absent.

The record also flattens optional DSMZ 78 Haemin, Vitamin K1, and Vitamin K3
stocks into final-medium ingredients, merges their ethanol into one
959.5 g/L parent ingredient, rescales the base-medium gram amounts against an
unsupported denominator, omits all DSMZ 78 preparation steps, and retains no
source representation of the 50 mL/L and 5 mL/L DSMZ 78a stock additions.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this KOMODO/DSMZ source record.

The record is incomplete until DSMZ Medium 78, amino acid solution, vitamin
solution, and any optional Haemin or Vitamin K stock are represented as
separate recipe scopes with source-faithful stock additions. It is also
incomplete until the generated merge preserves DSMZ 78a preparation steps from
the MediaDive duplicate or regenerates them from source.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The duplicate merge dropped `preparation_steps` that exist in the MediaDive DSMZ 78a normalized source, leaving the generated record with no instructions for the amino acid stock, vitamin stock, anoxic DSMZ 78 base, Haemin stock, or Vitamin K stocks. **Owner:** merge logic plus `data/normalized_yaml/bacterial/KOMODO_78a_CHOPPED_MEAT_medium_FOR_TREPONEMA_SP.yaml`. |
| Major | The DSMZ 78a amino acid solution and vitamin solution are flattened into direct parent-medium ingredients and stock concentrations are asserted as final `G_PER_L` concentrations. **Owner:** the KOMODO DSMZ resolver and MediaDive stock importer. |
| Major | The DSMZ 78 base recipe is flattened into the Treponema record with rescaled gram amounts and no 1000 mL base water, while optional Haemin, Vitamin K1, and Vitamin K3 stock internals are also flattened into the parent and their ethanol quantities are merged. **Owner:** the DSMZ resolver, unit converter, and duplicate merger. |
| Major | The generated synonym set treats DSMZ 78, DSMZ 78a, DSMZ 78b, anoxic 78, and dozens of strain-specific `78_*` records as exact duplicate source names. **Owner:** the recipe-merger fingerprinting or the upstream source records whose missing details caused false duplicate fingerprints. |
| Major | The 25 mL base 1 N NaOH and the 1 mL Haemin-stock 1 N NaOH are merged into 26 g/L direct sodium hydroxide, losing stock scope and changing the supplied form from 1 N NaOH solution to solid sodium hydroxide. **Owner:** duplicate merging plus solution migration. |

## Recommended Edits

1. Restore DSMZ 78a preparation and stock-addition semantics in the canonical
   KOMODO 78a owner: 50 mL/L amino acid stock and 5 mL/L vitamin stock added
   to ready DSMZ Medium 78.
2. Preserve the amino acid and vitamin stocks as separate solution recipes,
   including the 50 mL and 1000 mL water quantities, and filter sterilization.
3. Represent DSMZ Medium 78 as the ready base medium instead of mixing base
   ingredients, optional Haemin/Vitamin K stock internals, and 78a supplements
   into one flat parent list.
4. Unmerge falsely equivalent KOMODO 78, 78a, 78b, anoxic, and strain-specific
   source records into parent, variant, or exact-duplicate relationships that
   are source-supported.
5. Keep 1 N NaOH additions scoped to the base medium and Haemin stock rather
   than merging them or grounding them as solid sodium hydroxide.
6. Regenerate merged YAML after repairing the source records or merge logic.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against DSMZ Medium 78a and DSMZ
Medium 78 to confirm that stock additions, preparation steps, optional agar,
optional Haemin and Vitamin K stocks, source units, source water quantities,
and the duplicate/variant boundaries are source-faithful.

## Additional Notes

The exact source search intentionally covered the generated merge, normalized
owners and indexes, registry/catalog TSVs, and import-tracking reports; it did
not include generated `pages` or `output` bundles because an earlier
repository-wide exact search found the same record but produced unusably large
single-line generated-artifact matches.
