# YAML Record Review: bacillus_macyae_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_macyae_medium__8da9c7f8.yaml
- Started UTC: 2026-09-21T17:48:35Z
- Finished UTC: 2026-09-21T17:49:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003163 |
| Generated record | data/merge_yaml/merged/bacillus_macyae_medium__8da9c7f8.yaml |
| Maintained owner | data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml |
| Label | BACILLUS MACYAE MEDIUM |
| Source identity | MediaDive import of JCM J819 |
| Merge state | Single-source merge from `bacillus_macyae_medium` |

The generated target is stale relative to the maintained owner because
`apply_cocktail_nesting.py` added partial `ML_PER_L` solution structures on
2026-08-13, after this merge was generated. The maintained owner still leaves
most referenced-stock ingredients flattened at top level, so a full future fix
belongs in `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml` or the
MediaDive/JCM import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_macyae_medium__8da9c7f8.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/bacillus_macyae_medium__8da9c7f8.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, import
  history, and JCM GRMD=819 URL all point to the JCM import of BACILLUS MACYAE
  MEDIUM.
- **Direct main-medium arithmetic is plausible.** Compared with TOGO M854, the
  JCM/MediaDive rows are divided by the 1.012 L final volume implied by a 1 L
  main solution plus 1 ml SL-10, 10 ml trace vitamins, and 1 ml local vitamin
  solution.
- **Referenced stock identity is not preserved.** Components from M433 SL-10,
  M190 Trace vitamins, and the local M854 vitamin stock are top-level
  final-medium ingredients, and overlapping vitamin rows were summed across
  distinct stocks.

## Evidence

- TOGO M854 resolves to Bacillus Macyae Medium and original media ID `JCM_M819`;
  the live JCM GRMD=819 page currently returns `Nothing found`, so I used the
  corresponding TOGO M854 payload and its referenced M433/M190 payloads as
  inspected source text.
- M854 adds three stocks to the main solution: 1 ml Trace element solution
  SL-10 from M433, 10 ml Trace vitamins from M190, and 1 ml of the local M854
  vitamin solution.
- The generated record has no `solutions` block. It flattens M433 components
  such as HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CuCl2 x
  2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O into the final medium at stock
  strength.
- It flattens M190-only vitamins, such as folic acid, thiamine HCl, riboflavin,
  and lipoic acid, as top-level final-medium ingredients at their M190 stock
  concentrations.
- It also sums vitamins shared by M190 and the local M854 vitamin stock:
  for example, vitamin B12 is `0.10010000000000001 G_PER_L` from `0.1` plus
  `0.0001`, and p-aminobenzoic acid is `0.085 G_PER_L` from `0.08` plus
  `0.005`.
- M854 reports final pH as `7.4-7.8`; the generated record uses scalar
  `ph_value: 7.6`.

## Completeness

- The M433 SL-10, M190 Trace vitamins, and local M854 vitamin solution
  boundaries are absent from the generated merge.
- Water rows are absent for the main medium and every referenced stock.
- The 7.4-7.8 pH range is collapsed to a midpoint scalar.
- The maintained owner has already restored five flattened stock ingredients
  into three partial solution entries, but still leaves p-aminobenzoic acid,
  biotin, calcium pantothenate, M190-only vitamins, and most SL-10 components at
  top level.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected M854 payload does not supply those claims, so I did not
  count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for the exact
  stem `bacillus_macyae_medium__8da9c7f8` found no prior report before this file
  was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale and lacks the owner-side partial solution repair. | `apply_cocktail_nesting.py` added three `ML_PER_L` solution entries to `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml` on 2026-08-13; this generated 2026-08-06 merge has no `solutions` block. | Regenerate `data/merge_yaml/merged/bacillus_macyae_medium__8da9c7f8.yaml` after repairing the owner. |
| Major | M433 SL-10 stock components are flattened into the final medium at stock concentration. | M854 adds 1 ml SL-10 from M433; generated rows such as `FeCl2 x 4 H2O 1.5 G_PER_L` and `ZnCl2 0.07 G_PER_L` are M433 stock rows, not final-medium concentrations. | `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml`; JCM/MediaDive stock import. |
| Major | M190 Trace vitamins and the local M854 vitamin stock are flattened and partially summed together. | M854 adds M190 Trace vitamins at 10 ml and a local vitamin stock at 1 ml. The generated record sums overlapping stocks, including B12 `0.1 + 0.0001` and p-aminobenzoic acid `0.08 + 0.005`. | `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml`; JCM/MediaDive stock import. |
| Major | Source water rows are absent. | M854, M433, and M190 all scope water to main or stock solutions, but the generated record has no water row and no stock solutions to own their water rows. | `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml`. |
| Major | The final pH range is collapsed to an unsupported scalar midpoint. | M854 reports final pH 7.4-7.8; the generated record stores only `ph_value: 7.6`. | `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml`; MediaDive/JCM import. |
| Major | NiCl2 x 6 H2O is grounded too broadly. | M433 SL-10 specifies nickel chloride hexahydrate, while the flattened row uses `CHEBI:34887` / nickel dichloride. | `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml`; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as a note. | The JCM URL appears in free text, but there is no structured reference or evidence tying ingredients and referenced stocks to JCM GRMD=819, M433, or M190. | `data/normalized_yaml/bacterial/bacillus_macyae_medium.yaml` or the MediaDive/JCM importer. |

## Recommended Edits

1. Complete the owner-side nesting of all M433 SL-10, M190 Trace vitamins, and
   local M854 vitamin-stock rows under their respective `solutions` entries.
2. Restore water rows for the main solution and the three referenced stocks, or
   link the referenced stock solutions in a way that preserves their own water
   composition.
3. Reverse the cross-stock sums for biotin, p-aminobenzoic acid, calcium
   pantothenate, nicotinic acid, pyridoxine hydrochloride, and vitamin B12.
4. Represent the final pH range as 7.4-7.8 instead of the scalar 7.6.
5. Re-ground `NiCl2 x 6 H2O` to an exact nickel chloride hexahydrate term, or
   remove the broad anhydrous term until an exact hydrate is verified.
6. Add structured source provenance for JCM GRMD=819, M433, and M190, then
   regenerate merged products.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained JCM
  owner after stock, water, pH, grounding, and provenance edits.
- Regenerate merges and verify `bacillus_macyae_medium__8da9c7f8.yaml` contains
  exactly three non-empty solution additions rather than stock-strength
  top-level components.
- Compare the regenerated record manually against TOGO M854, M433, and M190,
  focusing on the 1 ml/10 ml stock additions and on vitamins shared by two
  different stocks.

## Additional Notes

- The original JCM GRMD=819 page currently returns HTTP 200 with a `Nothing
  found` body, so TOGO M854 was the accessible inspected source for this
  review.
- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
