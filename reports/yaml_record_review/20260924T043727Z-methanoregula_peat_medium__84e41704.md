# YAML Record Review: Methanoregula Peat Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanoregula_peat_medium__84e41704.yaml`
- Started UTC: 2026-09-24T04:35:24Z
- Finished UTC: 2026-09-24T04:37:27Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:000744`, the generated `methanoregula_peat_medium`
record for DSMZ/MediaDive medium 1280, `METHANOREGULA (PEAT) MEDIUM`.

The generated record merged two duplicate normalized sources,
`methanoregula_peat_medium.yaml` from MediaDive/DSMZ 1280 and
`methanoregula_medium.yaml` from KOMODO medium 1280 after DSMZ enrichment, on
fingerprint `84e41704d2f29958d05870d2dfb2c68b2b3cfe591f6b45836792361ed0881121`.

## Validation

- LinkML open validation: passed; the validator exited 0 with no diagnostics.
- Strict schema validation: passed with 0 error rows; the TSV contained the
  header only.
- Reference validation: passed; 1 file validated, 0 total checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked. The available history validator
  targets standalone files under `history/`, not `MediaRecipe.curation_history`
  blocks embedded in generated YAML.

## Identity and Grounding

The primary identity is appropriate for the direct DSMZ import. MediaDive medium
1280 and the current DSMZ PDF both identify the source as `METHANOREGULA
(PEAT) MEDIUM` with final pH 5.1 and final volume 1007 ml.

The duplicate merge metadata points to a real KOMODO/DSMZ duplicate,
`CultureMech:004033`, but the generated `parent_media.path` is stale:
`data/normalized_yaml/bacterial/methanoregula_medium.yaml` does not exist when
ignored files are included in the search; the file is currently
`data/normalized_yaml/archaea/methanoregula_medium.yaml`.

Ingredient grounding is mixed. Many salts and vitamins are exact, but
`NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride, `TiCl3` and
`Homo-PIPES` have no primary term, and `Calcium D-(+)-pantothenate` lacks the
CHEBI-keyed `mediaingredientmech_chebi_term` carried by most enriched rows.

## Evidence

### Supported by inspected sources

- MediaDive 1280 and the DSMZ 1280 PDF support a main recipe that combines
  954 ml Solution A, 10 ml Solution B, 13 ml Solution C, 10 ml Solution D,
  10 ml Solution E, and 10 ml Solution F.
- Solution A contains 27 mg NH4Cl, 14 mg KH2PO4, 2 ml 0.1 percent KCl,
  17 mg Na-acetate, 1 ml Trace elements solution, 0.5 ml 0.1 percent sodium
  resazurin, and 950 ml distilled water.
- Solution B contains 1.58 g Homo-PIPES, 0.18 g NaOH pellets, and 10 ml
  distilled water.
- Solution C contains 7.2 ml 0.38 M NaOH, 4.8 ml 0.5 M nitrilotriacetate, and
  0.55 ml 15 percent TiCl3.
- Solution D contains 0.2 g yeast extract and 10 ml distilled water. Solution E
  contains 0.07 g 2-mercaptoethanesulfonate and 10 ml distilled water.
- Solution F is 10 ml `Wolin's vitamin solution (10x)`, which current
  MediaDive and DSMZ define as a 1000 ml stock containing biotin, folic acid,
  pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid,
  Calcium D-(+)-pantothenate, Vitamin B12, p-Aminobenzoic acid,
  (DL)-alpha-Lipoic acid, and distilled water.
- The YAML preserves the main DSMZ/MediaDive anoxic preparation paragraphs, the
  Solution B pH adjustment, and the trace-elements preparation instruction.

### Unsupported or over-scoped in the YAML

- No source supports losing all explicit Solution A through F addition rows.
  The source first assembles the final medium from named stocks; the YAML only
  keeps the chemicals inside those stocks.
- All water rows are absent: 950 ml from Solution A, 10 ml from Solution B,
  10 ml from Solution D, 10 ml from Solution E, 1000 ml from Trace elements
  solution, and 1000 ml from `Wolin's vitamin solution (10x)`.
- The stock ingredients are stored at stock concentration rather than final
  medium concentration and without their local scope. For example, Solution B
  has `1.58 g` Homo-PIPES in 10 ml, so the YAML reports `158 G_PER_L`, and the
  trace-elements salts are the concentrations of the 1010 ml trace stock rather
  than the final medium after adding 1 ml of that stock to Solution A.
- `NaOH` merges two chemically and operationally distinct rows: 0.18 g NaOH
  pellets in Solution B and 7.2 ml 0.38 M NaOH in Solution C. The resulting
  `18.109432 G_PER_L` concentration is a cross-scope artifact.
- Solution F's 10 ml `Wolin's vitamin solution (10x)` addition is flattened to
  the 1000 ml vitamin stock formula, so vitamin rows are present at stock
  strength and the final Solution F addition is no longer represented.
- The trace-elements preparation step is detached from the trace-elements
  solution and placed after the complete-medium preparation steps.
- `parent_media.path` is stale after moving the KOMODO duplicate into the
  `archaea` normalized directory.

## Completeness

The generated record has the right DSMZ identity and most of the preparation
text, but it is not complete as an executable recipe. It cannot reconstruct the
six final additions, the water in each stock, the stock-vs-final dilution
relationships, or the separate Solution B and Solution C uses of NaOH.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: Solution A through F are flattened away; the record lacks
  the six final milliliter addition rows from DSMZ 1280.
- `needs curation`: every distilled-water row was dropped.
- `needs curation`: nested trace-element and vitamin-stock components are
  listed at stock strength in the top-level ingredient list.
- `needs curation`: the NaOH duplicate merge sums NaOH pellets from Solution B
  with a 0.38 M NaOH addition from Solution C.
- `pass with minor issues`: several valid DSMZ preparation paragraphs are
  present, but the trace-elements preparation step is not scoped to the trace
  stock it prepares.
- `needs curation`: `parent_media.path` points to the wrong normalized
  directory.
- `needs curation`: `NiCl2 x 6 H2O`, `TiCl3`, `Homo-PIPES`, and
  `Calcium D-(+)-pantothenate` need grounding cleanup.

## Recommended Edits

- Preserve the MediaDive `solution` rows in the normalized DSMZ import so
  Solution A through F remain explicit final-medium additions.
- Model Solution A through F, Trace elements solution, and `Wolin's vitamin
  solution (10x)` as nested stocks with their own water rows and local
  ingredient amounts.
- Remove the cross-scope NaOH merge and keep Solution B NaOH pellets distinct
  from the 0.38 M NaOH addition in Solution C.
- Keep the Solution B pH adjustment attached to Solution B and the ferrous
  chloride/HCl instruction attached to the trace-elements solution.
- Fix duplicate metadata paths so `CultureMech:000744` and `CultureMech:004033`
  point at `data/normalized_yaml/archaea/...`.
- Refresh ingredient grounding after the structural repair.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators after
  regenerating the two normalized duplicates and this merge.
- Diff the regenerated record against MediaDive 1280 and the current DSMZ 1280
  PDF, confirming the 1007 ml main volume and all nested solution IDs
  2561 through 2568 and 5980.
- Search with ignored files included for stale
  `data/normalized_yaml/bacterial/methanoregula` paths after the metadata fix.
- Confirm that no `Merged 2 duplicates` note remains on `NaOH`.

## Additional Notes

The TOGO `M2654` snapshot of DSMZ 1280 is reviewed separately in
`data/merge_yaml/merged/methanoregula_peat_medium.yaml`.
