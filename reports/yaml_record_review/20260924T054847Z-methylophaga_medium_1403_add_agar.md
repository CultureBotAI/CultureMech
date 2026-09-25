# YAML Record Review: Methylophaga Medium 1403 (add agar)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml
- Started UTC: 2026-09-24T05:46:15Z
- Finished UTC: 2026-09-24T05:48:47Z
- Verdict: needs curation

## Target

- **Class**: MediaRecipe
- **ID**: CultureMech:009041
- **Name**: methylophaga_medium_1403_add_agar
- **Original name**: Methylophaga Medium 1403 (add agar)
- **Generated status**: generated merge record under `data/merge_yaml/merged/`
- **Maintained owner**: `data/normalized_yaml/bacterial/methylophaga_medium_1403_add_agar.yaml`
- **Merge input**: `methylophaga_medium_1403_add_agar`
- **Merge fingerprint**: `04b2f9452211a81b575ad614ae6df3447931c0d39cb26f24fa9616694b0a9c5b`
- **Source identity**: TOGO Medium `M2462`
- **Linked upstream source**: DSMZ Medium 1337
- **Media term**: `TOGO:M2462`
- **Category**: bacterial
- **Composition and physical state**: `UNDEFINED`, `SOLID_AGAR`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml --out /private/tmp/methylophaga_medium_1403_add_agar.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file with 0 ERROR rows. The TSV contained the header only. |
| References, `linkml-reference-validator validate data data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Terms, `linkml-term-validator validate-data data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged recipe YAML. |

## Identity and Grounding

The local source identity is TOGO M2462. The `media_term`, label, and import
history all point to M2462, and the live TOGO API returns `Methylophaga Medium
1403 (add agar)` with DSMZ Medium 1337 as its `src_url`.

DSMZ Medium 1337 is the right linked source PDF for TOGO M2462; it is titled
`METHYLOPHAGA MEDIUM` and contains the Mineral Salts Solution, Solution T, and
Wolfe's Mineral Solution referenced by TOGO. DSMZ/MediaDive medium 1403 is a
near miss by number only: it is `METHYLOROSULA MEDIUM V-022`, so it should not
be used to repair this record.

An ignored-file-inclusive exact filename search under `data/` found only the
maintained normalized YAML and this generated merge YAML for the record. An
ignored-file-inclusive search for `M2462`, `Methylophaga Medium 1403`, and
`DSMZ_Medium1337` under `data/raw/togo`, `data/raw/mediadive`, and
`data/raw/mediadive_api` found no checked-in raw capture for this source.

## Evidence

The record preserves the TOGO M2462/DSMZ 1337 overall identity and the solid
agar modification, but the parsed subcomponent structure is badly collapsed.
TOGO M2462 represents these final additions: 10 ml Vitamin B12 solution, 3 ml
methanol, 20 ml Solution T, and 1 L Mineral Salts Solution. The Mineral Salts
Solution itself contains 10 ml Wolfe's Mineral Solution plus the salts and
20 g/L agar.

The YAML has four migrated `solutions`, but their amounts are stored as
`G_PER_L` masses and every migrated solution is named `Unknown solution`. The
main `ingredients` list also still contains stock members from Mineral Salts
Solution, Solution T, and Wolfe's Mineral Solution. Those flattened members
create nonsensical aggregate rows, including `1200.0 G_PER_L` distilled water,
`24.1 G_PER_L` NaCl from a 24 g Mineral Salts row plus a 0.1 g Wolfe row, and
`11.0 G_PER_L` CaCl2 from a 1 g Mineral Salts row plus a 10 mg Wolfe row.

Several Wolfe's Mineral Solution rows carry source unit slips in addition to the
stock/final scoping error. TOGO M2462 records `AlK(SO4)2`, `CuSO4`, and
`Na2MoO4` as 1 mg rows in the Wolfe stock, but the YAML stores each one as
`1 G_PER_L`. TOGO records `CoCl2`, `FeSO4`, and `ZnSO4` as 10 mg rows, but the
YAML stores each one as `10 G_PER_L`.

TOGO M2462 and the linked DSMZ/MediaDive 1337 source disagree on the Vitamin B12
addition volume: TOGO records 10 ml of a 0.1 mg/ml solution, while DSMZ and
MediaDive 1337 add 1 ml. The YAML value, `10 G_PER_L`, is wrong under either
source because the source value is a volume of a 0.1 mg/ml stock.

The DSMZ 1337 pH and preparation instructions are absent from the YAML. DSMZ
adjusts the Mineral Salts Solution to pH 8.0, autoclaves it, cools it, then
adds filter-sterilized methanol, separately autoclaved Solution T, Vitamin B12
solution, and Wolfe's Mineral Solution; Solution T and Wolfe's Mineral Solution
also have their own pH/autoclave preparation steps.

## Completeness

The record is complete enough to identify TOGO M2462 and to preserve that it is
a solid Methylophaga medium with 20 g/L agar, but it is not complete as a
usable structured recipe. It lacks the Mineral Salts/Solution T/Wolfe stock
boundaries, uses grams-per-liter units for volume additions, drops the pH 8.0
and sterilization workflow, and carries unresolved conflict between TOGO M2462
and DSMZ 1337 for the Vitamin B12 volume.

The empty `target_organisms`, `growth_metrics`, and `references` fields are not
defects for this generated import. The inspected TOGO and DSMZ records do not
include a primary growth study.

The maintained normalized YAML has the same flattened ingredients, invalid
solution units, and placeholder solution names as this merge record, so these
issues are present before merge generation.

## Findings

### Blocker

None found.

### Major

1. **Nested TOGO subcomponents were flattened and partially duplicated into the
   final ingredient list.** Solution T and Wolfe's Mineral Solution rows remain
   as top-level ingredients even though they are stocks, water from three
   scopes is merged into `1200.0 G_PER_L`, and same-named stock/final rows such
   as NaCl, CaCl2, and Bis-Tris were summed across source scopes. Future fixes
   belong in
   `data/normalized_yaml/bacterial/methylophaga_medium_1403_add_agar.yaml` or
   the TOGO import/solution-migration path that writes that normalized file; do
   not patch `data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml`
   directly.

2. **Migrated solution additions have mass units and placeholder names.** The
   four `solutions` entries all have `unit: G_PER_L` even though TOGO records
   the Vitamin B12, Solution T, Mineral Salts Solution, and Wolfe's Mineral
   Solution additions as `ml` or `L` volumes. Each migrated entry also has
   `name: Unknown solution`, which loses the source labels already present in
   `preferred_term`.

3. **Wolfe's Mineral Solution mg rows were imported as grams per liter.** The
   TOGO M2462 source has milligram units for CaCl2, `AlK(SO4)2`, CuSO4, CoCl2,
   FeSO4, Na2MoO4, and ZnSO4, while the YAML serializes the numeric values as
   `G_PER_L`. The concentration-plausibility report independently flags seven
   trace-salt rows plus the merged water row for this record.

4. **The pH and sterilization workflow from DSMZ 1337 are absent.** The YAML
   has no `ph_value` and no `preparation_steps`, so it omits pH 8.0, Mineral
   Salts autoclaving, filter sterilization of methanol and Vitamin B12, separate
   autoclaving of Solution T and Wolfe's Mineral Solution, and Wolfe's internal
   KOH pH adjustments.

5. **TOGO M2462 and DSMZ 1337 disagree on Vitamin B12 volume.** TOGO says
   10 ml of 0.1 mg/ml Vitamin B12 solution; DSMZ 1337 and MediaDive 1337 say
   1 ml. A future curator must preserve and resolve that discrepancy rather
   than silently selecting one amount.

### Minor

None found.

## Recommended Edits

1. Rebuild the normalized TOGO M2462 record so Mineral Salts Solution, Solution
   T, Wolfe's Mineral Solution, and Vitamin B12 solution are represented as
   volume-scoped solution additions with ml or L units rather than G/L units.

2. Move all Solution T and Wolfe's Mineral Solution ingredient rows out of
   final-medium `ingredients` and into their stock scopes; keep stock water rows
   inside those stock recipes.

3. Reparse milligram rows in Wolfe's Mineral Solution as milligrams, not grams,
   and remove duplicate-merge artifacts for Distilled water, NaCl, CaCl2, and
   Bis-Tris that were created by flattening independent scopes.

4. Add the DSMZ pH 8.0 and sterilization/post-autoclave addition workflow to
   appropriately scoped preparation fields.

5. Add a concrete discussion or quality flag for the Vitamin B12 volume conflict
   between TOGO M2462 and DSMZ/MediaDive 1337, or resolve it against an
   inspected primary source if one can be found.

6. Regenerate `data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml`
   from the normalized source and verify that the merge fingerprint changes
   only because of the reviewed corrections.

## Follow-up Checks

- Re-run focused open-schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/methylophaga_medium_1403_add_agar.yaml` and
  the regenerated `data/merge_yaml/merged/methylophaga_medium_1403_add_agar.yaml`.
- Manually compare the regenerated record against TOGO M2462 and DSMZ Medium
  1337, preserving the Vitamin B12 conflict if it remains unresolved.
- Re-run the concentration-plausibility report or its narrow equivalent and
  confirm this record no longer carries the water-volume or stock-strength
  trace-salt anomaly rows.
- Re-run the merge freshness/audit check that covers normalized inputs and
  `data/merge_yaml/merged/`.

## Additional Notes

The `1403` token in the TOGO label is not a DSMZ medium ID for this formula.
DSMZ/MediaDive medium 1403 was checked and is `METHYLOROSULA MEDIUM V-022`,
which does not match Methylophaga Medium M2462.

The schema, term, and reference validators all passed because the current YAML
is structurally valid even though the source subcomponent scopes, volume units,
and milligram units were not preserved.
