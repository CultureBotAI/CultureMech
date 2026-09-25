# YAML Record Review: Bacillus Macyae Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_MACYAE_MEDIUM.yaml
- Started UTC: 2026-09-21T17:46:35Z
- Finished UTC: 2026-09-21T17:48:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010270 |
| Generated record | data/merge_yaml/merged/BACILLUS_MACYAE_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml |
| Label | Bacillus Macyae Medium |
| Source identity | TOGO M854, imported from JCM_M819 |
| Merge state | Single-source merge from `TOGO_M854_Bacillus_Macyae_Medium` |

The generated target is stale relative to its maintained normalized owner for
the water row: the owner was repaired to a single `1.0` row on 2026-09-02, but
this generated merge still has a summed `2.0` row. The remaining stock-solution
and preparation fixes belong in
`data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml` or the
TOGO import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_MACYAE_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_MACYAE_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, TOGO M854
  accession, original source note, and JCM GRMD=819 URL all point to the TOGO
  import of Bacillus Macyae Medium.
- **The main salts and direct nutrients mostly match M854.** TOGO M854 lists a
  1 L main solution with yeast extract 0.8 g, NaCl 1.2 g, CaCl2.2H2O 0.15 g,
  NH4Cl 0.3 g, K2HPO4 0.2 g, MgCl2.6H2O 0.4 g, KCl 0.3 g, NaHCO3 0.6 g,
  Na2SO4 0.3 g, KNO3 0.5 g, and sodium lactate 1.1 g; the generated record
  keeps those numeric values.
- **Stock identity is not preserved.** The three intended additions are
  Trace element solution SL-10 from M433 at 1 ml, Trace vitamins from M190 at
  10 ml, and a local M854 vitamin solution at 1 ml. The generated record stores
  all three as empty `solutions` with gram-per-liter concentrations.

## Evidence

- TOGO M854 resolves to Bacillus Macyae Medium, original media ID `JCM_M819`,
  and pH `7.4-7.8`. The live JCM GRMD=819 page currently returns `Nothing
  found`, so I used the cited TOGO payload and its referenced stock-media
  payloads as inspected source text.
- M854 defines one 1 L main solution, adds SL-10 from TOGO M433 at 1 ml, adds
  M190 trace vitamins at 10 ml, adds the local M854 vitamin stock at 1 ml, and
  calls for 100% N2 anaerobic preparation.
- The local M854 vitamin stock is 1 L water with biotin 20 mg,
  p--aminobenzoic acid 80 mg, calcium pantothenate 100 mg, pyridoxine HCl
  300 mg, vitamin B12 100 mg, nicotinic acid 200 mg, and thiamine HCl
  dihydrate 200 mg. The generated record promotes those stock components as
  top-level final-medium rows at `20`, `80`, `100`, `300`, `100`, `200`, and
  `200 G_PER_L`.
- M854 lists Resazurin at 0.5 mg in the main solution. The generated record
  stores `Resazurin 0.5 G_PER_L`.
- M854 carries the preparation note to add vitamins, sodium lactate, and nitrate
  from sterile anaerobic stocks and to adjust final pH to 7.4-7.8. The
  generated record has no `preparation_steps` or `ph_value`.

## Completeness

- The generated water row is stale at `2.0`; the maintained owner already
  collapsed that summed duplicate to `1.0`.
- M433 SL-10, M190 trace vitamins, and the local M854 vitamin solution are
  missing as populated solution records with milliliter additions.
- The local M854 vitamin solution's 1 L water row is collapsed into the single
  final-medium water row and no longer scoped to that stock.
- The 0.5 mg resazurin row is off by 1000x.
- pH 7.4-7.8 and anaerobic/filter-sterilization preparation are missing.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected TOGO M854 payload does not supply those claims, so I did
  not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_MACYAE_MEDIUM` and `BACILLUS MACYAE MEDIUM` found no prior report
  before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated water row is stale and sums main-medium and local vitamin-stock water. | TOGO M854 has 1 L water in the main solution and 1 L water in the local vitamin solution. The maintained owner was repaired on 2026-09-02 to collapse the former `2.0` value, but this generated record still has `Distilled water 2.0 G_PER_L`. | Regenerate `data/merge_yaml/merged/BACILLUS_MACYAE_MEDIUM.yaml` from `data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml`. |
| Major | The local M854 vitamin solution is flattened into the final medium at stock concentration. | M854 adds 1 ml of a 1 L vitamin stock; the generated record stores each stock vitamin as a top-level ingredient with the stock mg value converted to `G_PER_L`, and leaves `Vitamin solution (see below)` empty at `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml`; TOGO solution import. |
| Major | Referenced SL-10 and M190 stocks are represented as empty gram-per-liter solutions. | M854 adds 1 ml of M433 SL-10 and 10 ml of M190 trace vitamins; the generated `solutions` have empty `composition` arrays and concentrations `1 G_PER_L` and `10 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml`; TOGO cross-medium solution import. |
| Major | Resazurin is 1000x too high because a milligram source row was normalized as grams per liter. | TOGO M854 lists 0.5 mg Resazurin; the record stores `0.5 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml`; TOGO unit conversion. |
| Major | Final pH and anaerobic stock-addition preparation were dropped. | TOGO M854 reports pH 7.4-7.8 and instructs preparation under 100% N2 with vitamins, sodium lactate, and nitrate added from sterile anaerobic stock solutions. | `data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml`; TOGO pH/comment import. |
| Minor | Source evidence is encoded only as a note. | The TOGO and original JCM URLs appear in free text, but there is no structured reference or evidence tying the ingredient rows and stock links to TOGO M854/JCM GRMD=819. | `data/normalized_yaml/bacterial/TOGO_M854_Bacillus_Macyae_Medium.yaml` or the TOGO importer. |

## Recommended Edits

1. Regenerate the merged record so it picks up the owner-side 2026-09-02 water
   repair.
2. Move the seven local M854 vitamin rows into a local 1 L vitamin stock and
   add that stock to the main medium at 1 ml/L.
3. Preserve the M433 SL-10 and M190 trace-vitamin additions as 1 ml/L and
   10 ml/L solution links, not `G_PER_L` additions.
4. Convert `Resazurin 0.5 mg` to `0.0005 G_PER_L` or a semantically equivalent
   milligram representation.
5. Preserve pH 7.4-7.8 and the anaerobic, filter-sterilized stock preparation
   note from TOGO M854.
6. Add structured source provenance for TOGO M854, JCM GRMD=819, referenced
   TOGO M433, and referenced TOGO M190.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained TOGO
  owner after stock, unit, pH/preparation, and provenance edits.
- Regenerate merges and verify `BACILLUS_MACYAE_MEDIUM.yaml` water is no longer
  `2.0`, the three `solutions` are no longer empty, and local vitamin rows are
  absent from top-level final-medium ingredients.
- Compare the regenerated record manually against TOGO M854, M433, and M190,
  focusing on the three stock additions, resazurin's `mg` unit, pH, and 100% N2
  preparation note.

## Additional Notes

- The original JCM GRMD=819 page currently returns HTTP 200 with a `Nothing
  found` body, so TOGO M854 was the accessible inspected source for this
  review.
- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
