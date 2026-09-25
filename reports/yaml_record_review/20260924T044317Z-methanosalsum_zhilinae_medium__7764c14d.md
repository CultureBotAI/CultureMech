# YAML Record Review: Methanosalsum Zhilinae Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanosalsum_zhilinae_medium__7764c14d.yaml`
- Started UTC: 2026-09-24T04:41:51Z
- Finished UTC: 2026-09-24T04:43:17Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:001505`, the generated `methanosalsum_zhilinae_medium`
record for DSMZ/MediaDive medium 396, `METHANOSALSUM ZHILINAE MEDIUM`.

The generated record merged two duplicate normalized sources,
`methanosalsum_zhilinae_medium.yaml` from MediaDive/DSMZ 396 and
`methanohalophilus_zhilinae_medium.yaml` from KOMODO medium 396 after DSMZ
enrichment, on fingerprint
`7764c14dc4fabc25cde1c146e37c8efa2e4aef9fe5a99640a686473e8a4891a2`.

## Validation

- LinkML open validation: passed with `No issues found`.
- Strict schema validation: passed with 0 error rows; the TSV contained the
  header only.
- Reference validation: passed; 1 file validated, 0 total checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked. The available history validator
  targets standalone files under `history/`, not `MediaRecipe.curation_history`
  blocks embedded in generated YAML.

## Identity and Grounding

The DSMZ identity and pH range are correct. MediaDive medium 396 and the live
DSMZ PDF identify this recipe as `METHANOSALSUM ZHILINAE MEDIUM` with a final
pH range of 9.2 to 9.4.

The duplicate relationship points to a real KOMODO-derived duplicate,
`CultureMech:005183`, but the generated `variant_children.path` is stale:
`data/normalized_yaml/bacterial/methanohalophilus_zhilinae_medium.yaml` does
not exist when ignored files are included in the search; the duplicate source is
`data/normalized_yaml/archaea/methanohalophilus_zhilinae_medium.yaml`.

Most salts have exact or acceptable CHEBI grounding. `NiCl2 x 6 H2O` remains
grounded to anhydrous nickel dichloride and should be refreshed when the
stock-scope representation is repaired.

## Evidence

### Supported by inspected sources

- DSMZ 396 and MediaDive 396 support the main solution with yeast extract,
  Trypticase peptone, 40 g NaCl, 1 g NH4Cl, 3.5 g MgCl2 x 6 H2O,
  3 g MgSO4 x 7 H2O, 1 g KCl, 0.4 g K2HPO4, 5 ml Modified Wolin's mineral
  solution, 0.5 ml 0.1 percent sodium resazurin, 0.5 g
  L-Cysteine HCl x H2O, 3 g NaHCO3, 2 g Na2CO3, 2 g Trimethylamine-HCl,
  0.25 g Na2S x 9 H2O, and 1000 ml distilled water.
- DSMZ/MediaDive define `Modified Wolin's mineral solution` as a 1000 ml stock
  containing nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl,
  FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O,
  CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O,
  NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and distilled water.
- The generated record preserves the DSMZ anaerobic preparation paragraph and
  the Modified Wolin mineral-solution pH instruction.
- The `COMPLEX`/`UNDEFINED` typing is appropriate because the medium contains
  yeast extract and Trypticase peptone.

### Unsupported or over-scoped in the YAML

- The 5 ml `Modified Wolin's mineral solution` addition is missing as a stock
  addition; only its internal mineral rows remain.
- The main 1000 ml water row and the mineral-stock 1000 ml water row are both
  absent.
- `NaCl` sums the main 40 g/L sodium chloride with 1 g/L sodium chloride from
  the mineral stock, even though the latter should remain inside a stock that is
  added at only 5 ml/L.
- `MgSO4 x 7 H2O` is `6.0 G_PER_L`; DSMZ lists 3 g in the main solution and
  3 g/L inside the 1000 ml mineral stock, not 6 g/L in the final medium.
- All Modified Wolin mineral-solution children are represented as top-level
  ingredients at stock strength.

## Completeness

The record has the top-level DSMZ identity, pH range, direct main ingredients,
and source preparation text, but it is incomplete because the Modified Wolin
stock scope and both water rows are gone. The duplicate-source merge also
amplified the already-flattened MgSO4 row.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: the 5 ml Modified Wolin mineral-solution addition is
  flattened away.
- `needs curation`: both water rows are absent.
- `needs curation`: stock-local minerals are top-level final ingredients at
  stock strength.
- `needs curation`: NaCl is summed across main and stock scopes.
- `needs curation`: MgSO4 x 7 H2O is doubled to an unsupported
  `6.0 G_PER_L` during duplicate merging.
- `needs curation`: `variant_children.path` points to the wrong normalized
  directory.
- `needs curation`: `NiCl2 x 6 H2O` remains too broadly grounded.

## Recommended Edits

- Preserve the MediaDive `solution` row for `Modified Wolin's mineral solution`
  as a 5 ml/L stock addition.
- Keep the Modified Wolin stock formula nested under that addition or in a
  separately referenced local stock, including its 1000 ml water row.
- Restore the main 1000 ml distilled-water row.
- Remove cross-scope duplicate sums for NaCl and MgSO4 x 7 H2O.
- Rebuild duplicate detection so merging a DSMZ source with a KOMODO copy does
  not add numeric concentrations from identical source-derived rows.
- Fix the duplicate metadata path to
  `data/normalized_yaml/archaea/methanohalophilus_zhilinae_medium.yaml`.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators after
  regenerating both normalized duplicate sources and this merge.
- Diff the regenerated file against MediaDive 396 and DSMZ Medium 396, with
  explicit checks for the 5 ml mineral addition, 40 g/L main NaCl, 3 g/L main
  MgSO4 x 7 H2O, and 1000 ml water in both solution scopes.
- Search with ignored files included for stale
  `data/normalized_yaml/bacterial/methanohalophilus_zhilinae_medium.yaml`
  references after the path fix.

## Additional Notes

TOGO `M2648` also represents a Methanosalsum zhilinae recipe and is generated
separately as `data/merge_yaml/merged/METHANOSALSUM_ZHILINAE_MEDIUM.yaml`.
