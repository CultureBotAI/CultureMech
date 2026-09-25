# YAML Record Review: pyrococcus_medium__acf8ae3a

- Repository: CultureMech
- Record: data/merge_yaml/merged/pyrococcus_medium__acf8ae3a.yaml
- Started UTC: 2026-09-24T23:51:12Z
- Finished UTC: 2026-09-24T23:52:21Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:009123` for `pyrococcus_medium`.

- Generated record: `data/merge_yaml/merged/pyrococcus_medium__acf8ae3a.yaml`
- Normalized owner: `data/normalized_yaml/archaea/TOGO_M2554_Pyrococcus_medium.yaml`
- Generated from: `TOGO_M2554_Pyrococcus_medium`
- Source identity: `TOGO:M2554`, original ATCC medium 1915 PDF
- Merge fingerprint: `acf8ae3a3b21247d8d682e7afc4f6e06117330128891c892e8097c8308fa4abd`

`data/merge_yaml/merged` is generated output. Fix the normalized owner and then
regenerate this target.

## Validation

- Open LinkML validation: Passed; `linkml-validate` reported `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` wrote a one-line TSV
  with only the header and reported 0 ERROR rows.
- LinkML reference validation: Passed; 1 file validated, 0 reference checks
  were applicable, and all validations passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` embedded in merged
  YAML.

## Identity and Grounding

The TOGO identity is unique and correctly recorded. An
ignored-file-inclusive numeric-boundary search for `TOGO:M2554` and
`togomedium.org/medium/M2554` found only this normalized owner, this generated
record, and normalized index entries. An ignored-file-inclusive search for the
ATCC PDF hash `4A37EA717D654CEB9FF4E233DA80040C` found only the owner and this
generated record.

The source label is imprecise but traceable: TOGO M2554 points to an ATCC PDF
for `ATCC medium: 1915 Pyrococcus medium (DSM medium 377)`. Because the PDF
self-identifies as a DSM 377 recipe, compare it against the other DSM 377 /
Pyrococcus Medium imports before deciding whether it should stay as a separate
variant, become a source duplicate, or be merged.

Several chemical groundings are missing or too broad. `Powdered sulfur` and
`Sulfur, powdered` have no `term` despite the same source compound being
elemental sulfur. `NiCl2 . 6H2O` is grounded to anhydrous nickel dichloride
instead of a hexahydrate-specific term, and `CoCl2 . 6H2O` is grounded to
cobalt dichloride rather than cobalt dichloride hexahydrate.

## Evidence

Live TOGO M2554 and the ATCC PDF agree on the source contents. The ATCC recipe
defines a 1 L seawater basal medium containing KH2PO4, 10 ml Wolfe's Mineral
Solution, yeast extract, Bacto peptone, resazurin, sulfur, sodium sulfide, and
seawater. NiCl2 x 6H2O and resazurin are milligram-scale additions. The same PDF
then instructs the curator to add about 0.18 g powdered sulfur to each tube,
dissolve the remaining ingredients except sodium sulfide in seawater, adjust to
pH 6.4 plus or minus 0.1, dispense 6.0 ml aliquots anaerobically under 100% N2
into tubes containing sulfur, autoclave at 100C for 30 minutes on 3 consecutive
days, reduce before inoculation with sterile neutral sodium sulfide to a final
0.5 g/L, and finish at pH 6.5.

The Wolfe's Mineral Solution in the same source is a 1 L distilled-water stock
with nitrilotriacetic acid, MgSO4 x 7H2O, MnSO4 x H2O, NaCl, FeSO4 x 7H2O,
CoCl2 x 6H2O, CaCl2, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2 x 12H2O, H3BO3, and
Na2MoO4 x 2H2O. Its preparation dissolves NTA in about 500 ml water, adjusts to
pH 6.5 with KOH, brings the stock to 1.0 L, and then adds the remaining
compounds one at a time.

## Completeness

The generated record is missing the pH, lacks every preparation step, and does
not distinguish the 1 L seawater basal recipe, a 6 ml anaerobic tube aliquot,
per-tube sulfur, pre-inoculation sulfide reduction, and the Wolfe mineral stock.
It also materializes N2 and KOH solution as variable components rather than as
preparation context.

## Findings

- The generated file is stale relative to the normalized owner. It still has
  `Na2S . 9H2O` at `1.0 G_PER_L` with `[Merged 2 duplicates: 0.5, 0.5]`, while
  the owner has the 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` repair that
  collapses that unambiguous duplicate back to `0.5`.
- The tube-scale source comments were parsed as final-medium ingredients.
  `Basal Medium 6.0 ml` became `Basal Medium` at `6 G_PER_L`, and the instruction
  to add about `0.18 g` powdered sulfur per 6 ml tube became a second
  `Powdered sulfur` final ingredient at `0.18 G_PER_L`. That 0.18 g per-tube
  sulfur corresponds to the `30 g/L` sulfur in the basal recipe and should not
  be a second independent concentration.
- The 10 ml Wolfe's Mineral Solution stock was not preserved cleanly. The
  `solutions` entry records it as a scalar `10 G_PER_L`, while every Wolfe stock
  component is also flattened into the final ingredient list at its stock
  concentration. Those Wolfe salts and NTA describe a 1 L stock that is dosed at
  10 ml into 1 L of basal medium.
- Milligram units are over-converted to grams per liter. The source's
  `Resazurin 1.0 mg` is curated as `1 G_PER_L`, and `NiCl2 . 6H2O 2.0 mg` is
  curated as `2 G_PER_L`.
- Procedural terms are modeled as recipe ingredients. The ATCC source uses 100%
  N2 gas for anaerobic boiling/cooling/dispensing and KOH only to dissolve NTA
  while preparing Wolfe's Mineral Solution, but this record keeps `N2` as a
  variable main ingredient and `KOH solution` as an empty variable solution.
- The source pH and preparation were dropped. The record has no `ph_value` and
  no `preparation_steps` for pH 6.4 plus or minus 0.1 before dispensing, final
  pH 6.5, anaerobic 6 ml aliquots, 100C autoclaving for 30 minutes on 3
  consecutive days, or pre-inoculation sodium-sulfide reduction.

## Recommended Edits

- Rebuild `data/normalized_yaml/archaea/TOGO_M2554_Pyrococcus_medium.yaml` from
  live TOGO M2554 and the ATCC 1915 PDF. Treat the basal recipe, 6 ml aliquot,
  0.18 g per-tube sulfur, and final 0.5 g/L sulfide reduction as one coherent
  procedure rather than independent material rows.
- Preserve `Wolfe's Mineral Solution` as a 10 ml stock addition, backed either by
  a verified reusable Wolfe stock record or by the explicit nested ATCC stock
  composition. Do not also flatten the stock-liter amounts into the final
  medium as grams per liter.
- Convert milligram rows before curation: `Resazurin 1.0 mg` and
  `NiCl2 . 6H2O 2.0 mg` are not gram-per-liter quantities.
- Add `ph_value: 6.5` and encode the ATCC pH adjustment, 100% N2 anaerobic
  handling, three-day 100C autoclaving, pre-inoculation sulfide reduction, and
  Wolfe stock preparation as preparation steps. Keep `N2` and `KOH solution` out
  of the final ingredient and solution material lists unless the schema can
  attach them specifically to those preparation steps.
- Ground both powdered-sulfur labels to elemental sulfur and replace the broad
  hydrate-insensitive chloride groundings for `NiCl2 . 6H2O` and `CoCl2 . 6H2O`
  with hydrate-aware terms or leave them ungrounded until exact terms are
  available.
- Regenerate `data/merge_yaml/merged/pyrococcus_medium__acf8ae3a.yaml` from the
  repaired owner so the `Na2S . 9H2O` duplicate-sum repair is reflected in the
  generated output.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Run ignored-file-inclusive numeric-boundary searches for `TOGO:M2554`,
  `togomedium.org/medium/M2554`, and `4A37EA717D654CEB9FF4E233DA80040C` to make
  sure the ATCC 1915 source remains unique.
- Compare the repaired owner against the ATCC PDF and the TOGO API response,
  including units, pH, 6 ml tube handling, and Wolfe stock preparation.
- Compare the ATCC 1915 record against the DSM 377 / Pyrococcus Medium imports
  and either record an intentional variant relationship or merge duplicate
  sources if the formulas are intended to represent the same medium.

## Additional Notes

Empty optional fields were not treated as defects. No GitHub issues, PR
comments, or source YAML edits were made during this review pass.
