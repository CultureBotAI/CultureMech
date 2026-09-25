# YAML Record Review: BACILLUS ACIDOCALDARIUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:27:06Z
- Finished UTC: 2026-09-21T17:28:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002203 |
| Generated record | data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml |
| Canonical normalized owner | data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml |
| Other merged inputs | KOMODO Medium 13, DSMZ Medium 13, DSMZ Medium 1286, and seven KOMODO 13 DSM-strain records |
| Label | BACILLUS ACIDOCALDARIUS MEDIUM |
| Source identity | JCM GRMD=101 / DSMZ Medium 13 |

The reviewed YAML is a generated 11-source merge. Direct fixes belong in the
normalized owners and the merge rules that grouped them, followed by
regeneration of `data/merge_yaml/merged/` and pages.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

I used the offline `uv --no-project` Python 3.11 workaround for the focused
validators because direct project `just` validation currently reaches a Python
3.13 build failure for `llvmlite==0.46.0` before target validation starts.

## Identity and Grounding

- **The primary label points to the intended JCM/DSMZ medium.** JCM GRMD=101
  and DSMZ Medium 13 both identify BACILLUS ACIDOCALDARIUS MEDIUM.
- **The merge identity is wrong.** `bryocella_elongata_medium.yaml` is DSMZ
  Medium 1286, BRYOCELLA ELONGATA MEDIUM, with pH 5.0-5.8, 0.5 g/L glucose,
  optional fructose, 0.05 g/L yeast extract, 15 g/L optional agar, and no two
  500 ml Solution A/B assembly. It should not appear in `merged_from` or as a
  synonym of BACILLUS ACIDOCALDARIUS MEDIUM.
- **The KOMODO 13 DSM-strain children are exact formula copies, not distinct
  concentration or supplement variants.** The inspected `medium_13_modified_*`
  normalized records all state `DSMZ Medium: 13` and contain the same seven
  doubled stock-strength ingredient rows as KOMODO Medium 13.
- **Ingredient groundings are plausible for the named salts.** The CHEBI terms
  preserve ammonium sulfate, magnesium sulfate heptahydrate, calcium chloride
  dihydrate, potassium dihydrogen phosphate, glucose, and agar identities.

## Evidence

- JCM GRMD=101 and DSMZ Medium 13 agree on the recipe structure: Solution A is
  500 ml with yeast extract 1 g, (NH4)2SO4 0.2 g, MgSO4 x 7 H2O 0.5 g,
  CaCl2 x 2 H2O 0.25 g, and KH2PO4 0.6 g; Solution B is 500 ml with glucose
  1 g and agar 20 g.
- Both JCM 101 and DSMZ 13 say to adjust pH to 3.0-4.0 and to sterilize
  Solutions A and B separately before aseptically combining them.
- The generated record has no Solution A/B boundary or 500 ml water rows. It
  keeps the stock strengths as final `G_PER_L` rows: yeast extract 2,
  ammonium sulfate 0.4, MgSO4 x 7 H2O 1, CaCl2 x 2 H2O 0.5, KH2PO4 1.2,
  glucose 2, and agar 40. Every one of those values is double the final
  combined-liter amount.
- The generated `ph_value: 3.5` is an inferred midpoint, not a source value.
  DSMZ 13 and JCM 101 both provide only the pH range 3.0-4.0.
- DSMZ Medium 1286 for BRYOCELLA ELONGATA MEDIUM uses the same ingredient
  names but at substantially lower concentrations, permits glucose or fructose,
  makes agar optional at 15 g/L, and targets pH 5.0-5.8.

## Completeness

- The canonical generated recipe cannot be reconstructed faithfully because the
  two 500 ml solution boundaries and water amounts are gone.
- The exact pH range is not structured; a scalar midpoint is structured instead.
- The false Bryocella synonym and `merged_from` row overstate source agreement.
- `target_organisms`, growth metrics, incubation temperature, light, salinity,
  and storage are empty. The inspected medium sources do not provide those
  claims, so I did not treat these empty optional fields as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_ACIDOCALDARIUS_MEDIUM`, `Bacillus Acidocaldarius Medium`, and
  `BACILLUS ACIDOCALDARIUS MEDIUM` found no prior report for this target before
  this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Blocker | The merge conflates BRYOCELLA ELONGATA MEDIUM with BACILLUS ACIDOCALDARIUS MEDIUM. | The generated record lists `bryocella_elongata_medium` as a MediaDive synonym and merged source. The maintained Bryocella source is DSMZ Medium 1286, while inspected DSMZ Medium 1286 has pH 5.0-5.8, optional 15 g/L agar, and lower glucose/yeast/salt concentrations than DSMZ Medium 13 / JCM 101. | Merge grouping for `data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml`; `data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml` should remain a separate medium. |
| Major | JCM/DSMZ Solution A and Solution B were flattened at stock strength. | DSMZ Medium 13 and JCM 101 split the recipe into two 500 ml solutions and then combine them. The generated record lacks both `Distilled water` rows and stores each stock component at its 500 ml concentration rather than its final 1000 ml concentration. | `data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml`, `data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml`, and KOMODO 13 derivative owners; if import-owned, the MediaDive/JCM and DSMZ-to-KOMODO importers. |
| Major | All ingredient quantities are doubled relative to the final combined medium. | The source recipe's final combined liter contains 1 g/L yeast extract, 0.2 g/L (NH4)2SO4, 0.5 g/L MgSO4 x 7 H2O, 0.25 g/L CaCl2 x 2 H2O, 0.6 g/L KH2PO4, 1 g/L glucose, and 20 g/L agar. The generated record stores 2, 0.4, 1, 0.5, 1.2, 2, and 40 `G_PER_L`. | Same normalized owners as above, or a stock/final concentration migration rule. |
| Major | The source pH range was collapsed to an unsupported scalar. | JCM 101 and DSMZ Medium 13 both say pH 3.0-4.0. The generated canonical record has `ph_value: 3.5`; the KOMODO 13 owner already preserves `ph_range: {min: 3.0, max: 4.0}`. | `data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml` and merge rules for pH conflicts. |
| Minor | Source provenance and duplicate-source rationale are too thin. | The generated record retains source IDs only in notes, lists seven KOMODO `medium_13_modified_for_dsm_*` records as `SOURCE_DUPLICATE`, and does not cite inspected DSMZ/JCM text explaining which rows and preparation steps came from which source. | The normalized JCM, DSMZ, and KOMODO 13 records plus media-variant-link review data. |

## Recommended Edits

1. Remove `bryocella_elongata_medium.yaml` from this merge group and ensure
   `data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml` remains a
   separate DSMZ Medium 1286 record with its own pH 5.0-5.8 and optional
   glucose/fructose and agar semantics.
2. Rework the BACILLUS ACIDOCALDARIUS owners so Solution A and Solution B are
   represented as separate 500 ml stocks that are sterilized separately and
   combined after cooling.
3. Correct final-medium concentrations to half of the current stock-strength
   rows: yeast extract 1 g/L, (NH4)2SO4 0.2 g/L, MgSO4 x 7 H2O 0.5 g/L,
   CaCl2 x 2 H2O 0.25 g/L, KH2PO4 0.6 g/L, glucose 1 g/L, and agar 20 g/L.
4. Replace `ph_value: 3.5` with a pH range of 3.0-4.0.
5. Re-evaluate the seven `medium_13_modified_for_dsm_*` KOMODO records after
   the concentration fix. If they are only DSMZ Medium 13 source duplicates,
   keep them linked as duplicates; if source evidence shows real strain-specific
   changes, curate those changes instead of merging them as exact duplicates.
6. Regenerate merged records and page outputs after the normalized owner and
   merge grouping are corrected.

## Follow-up Checks

- Run schema, strict, term, and reference validators on the edited JCM, DSMZ,
  KOMODO, and Bryocella normalized owners.
- Rebuild merges and verify `BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml` no longer
  lists `bryocella_elongata_medium` in `merged_from` or `synonyms`.
- Compare the regenerated Bacillus record manually against JCM GRMD=101 and
  DSMZ Medium 13, checking two 500 ml solutions, the pH range, final
  concentrations, separate sterilization, cooling, and aseptic combining.
- Compare `bryocella_elongata_medium.yaml` manually against DSMZ Medium 1286 to
  confirm it stayed separate and did not inherit Bacillus Medium 13 quantities.

## Additional Notes

- The current canonical stable ID belongs to the JCM J101 owner. The record
  should keep that stable ID for BACILLUS ACIDOCALDARIUS MEDIUM and drop the
  unrelated Bryocella source rather than choosing a new ID.
- The exact prior-report search was run with `--no-ignore --hidden`, so ignored
  review reports were included.
