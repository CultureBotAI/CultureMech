# YAML Record Review: pyrolobus_fumarii_medium__0aa02c21

- Repository: CultureMech
- Record: data/merge_yaml/merged/pyrolobus_fumarii_medium__0aa02c21.yaml
- Started UTC: 2026-09-24T23:58:13Z
- Finished UTC: 2026-09-24T23:58:45Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:001932` for
`pyrolobus_fumarii_medium`.

- Generated record: `data/merge_yaml/merged/pyrolobus_fumarii_medium__0aa02c21.yaml`
- Normalized owner: `data/normalized_yaml/archaea/pyrolobus_fumarii_medium.yaml`
- Generated from: `pyrolobus_fumarii_medium`
- Source identity: `mediadive.medium:792`
- Merge fingerprint: `0aa02c21be087785ade5bc5c004f766a9494486cb19d852fe0b902ccf8e687a9`

`data/merge_yaml/merged` is generated output. Fix the normalized owner and then
regenerate this target.

## Validation

- Open LinkML validation: Passed; `linkml-validate` exited 0 with no
  diagnostics.
- Strict validation: Passed; `scripts/validate_strict.py` wrote a one-line TSV
  with only the header and reported 0 ERROR rows.
- LinkML reference validation: Passed; 1 file validated, 0 reference checks
  were applicable, and all validations passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` embedded in merged
  YAML.

## Identity and Grounding

The direct DSMZ/MediaDive identity is valid: live MediaDive medium 792 and the
DSMZ PDF both serve `PYROLOBUS FUMARII MEDIUM`, and `mediadive.medium:792` is
the right identifier for this direct import.

An ignored-file-inclusive alphanumeric-boundary search for
`mediadive.medium:792`, `DSMZ, ID: 792`, and `DSMZ_Medium792.pdf` found this
direct MediaDive owner, this generated record, the TOGO M2683 projection, a
KOMODO projection of the same DSMZ medium, and a curated Wolfe mineral-elixir
helper that cites DSMZ 792. The search intentionally excluded lettered
MediaDive variants such as `792a`, `792b`, and `792c`.

Two rows still carry deprecated numeric MediaIngredientMech identifiers:
`KNO3` and `Na2SeO4`. They should be moved to CHEBI-keyed slots or left without
legacy MIM ids when exact CHEBI-keying is not already present.

## Evidence

DSMZ 792 is a top-level 1010 ml medium assembled from 989 ml Solution A, 10 ml
Solution B, 1 ml Solution C, and 10 ml Solution D. Solution A is a freshly
prepared 989 ml salts solution that itself contains 1 ml Wolfe's mineral elixir.
Solution B is a 10 ml KNO3 / KH2PO4 stock, Solution C is 1 ml Seven vitamins
solution, and Solution D is a 10 ml Na2S x 9H2O stock.

The source keeps two further 1 L reusable stocks nested below those solutions:
Wolfe's mineral elixir has fourteen salts in 1 L distilled water, and Seven
vitamins solution has seven vitamins in 1 L distilled water. The DSMZ/MediaDive
preparation steps sparge Solution A under 80% H2 and 20% CO2, autoclave
solutions B and D separately under 100% N2, prepare and filter-sterilize
Solution C under 100% N2, complete the medium from the four solutions, adjust
the complete pH to 5.8 with sterile anoxic 5% Na2CO3 if needed, and pressurize
vials after inoculation to 1 bar overpressure with sterile 80% H2 and 20% CO2.

## Completeness

The generated record has pH and preparation prose but no solution hierarchy at
all. The normalized owner is only partly repaired: its 2026-08-07 cocktail pass
nested four Wolfe rows and four Seven vitamins rows, but it still does not
represent Solution A, Solution B, Solution C, or Solution D, and it still leaves
several stock-only rows in the final `ingredients` list.

## Findings

- The generated file is stale relative to the normalized owner. It predates the
  2026-08-07 `NESTED_FLATTENED_COCKTAIL` repair that moved eight stock-strength
  rows under `Wolfe's mineral elixir` and `Seven vitamins solution`.
- The top-level four-solution DSMZ structure is absent. Source additions of
  `989 ml Solution A`, `10 ml Solution B`, `1 ml Solution C`, and
  `10 ml Solution D` are not represented, so the record cannot tell which
  compounds are pre-autoclaved, filter-sterilized, or combined late.
- Solution B and Solution D are flattened as if their 10 ml stock concentrations
  were final medium concentrations. `KNO3` is stored at `100 G_PER_L`, `KH2PO4`
  at `50 G_PER_L`, and `Na2S x 9 H2O` at `15 G_PER_L`, instead of being nested
  in 10 ml stocks added to the 1010 ml final medium.
- Wolfe's mineral elixir is only partly nested. The generated file leaves the
  whole stock in final ingredients; the normalized owner still leaves CuSO4 x
  5H2O, AlK(SO4)2 x 12H2O, Na2MoO4 x 2H2O, `(NH4)2Ni(SO4)2 x 6H2O`,
  Na2WO4 x 2H2O, and Na2SeO4 as final-medium gram-per-liter rows instead of
  stock rows under Wolfe's mineral elixir.
- Duplicate cleanup summed Wolfe stock rows into Solution A rows. `NaCl` is
  `24.003999999999998 G_PER_L` from `14.004 + 10.0`, `MgSO4 x 7 H2O` is
  `33.53893 G_PER_L` from `3.53893 + 30.0`, `CaCl2 x 2 H2O` is
  `1.384227 G_PER_L` from `0.384227 + 1.0`, and `H3BO3` is
  `0.1151668 G_PER_L` from `0.0151668 + 0.1`.
- Seven vitamins solution is also only partly nested in the owner and fully
  flattened in the generated target. The owner still leaves p-aminobenzoic acid,
  biotin, and calcium pantothenate in final ingredients, while the source adds a
  1 ml Solution C aliquot that contains the complete seven-vitamin stock.

## Recommended Edits

- Rebuild `data/normalized_yaml/archaea/pyrolobus_fumarii_medium.yaml` from live
  MediaDive 792 and the DSMZ PDF, preserving the source hierarchy:
  989 ml Solution A, 10 ml Solution B, 1 ml Solution C, and 10 ml Solution D.
- Nest Wolfe's mineral elixir under Solution A at 1 ml and include all fourteen
  Wolfe components under that stock, not only the four rows already moved by
  `apply_cocktail_nesting.py`.
- Nest Seven vitamins solution under Solution C at 1 ml and include all seven
  vitamin rows under that stock.
- Move `KNO3`, `KH2PO4`, and `Na2S x 9 H2O` into Solution B and Solution D at
  the stock concentrations given by MediaDive, and keep those stocks as 10 ml
  additions to the final medium.
- Recompute Solution A rows without adding Wolfe stock concentrations into NaCl,
  MgSO4 x 7H2O, CaCl2 x 2H2O, and H3BO3.
- Remove deprecated numeric MIM fields from `KNO3` and `Na2SeO4` after
  assigning exact CHEBI-keyed links where possible.
- Regenerate `data/merge_yaml/merged/pyrolobus_fumarii_medium__0aa02c21.yaml`
  from the repaired owner and reconcile the TOGO M2683 and KOMODO DSMZ 792
  projections against it.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Run ignored-file-inclusive alphanumeric-boundary searches for
  `mediadive.medium:792`, `DSMZ, ID: 792`, and `DSMZ_Medium792.pdf` to verify
  direct DSMZ 792, TOGO M2683, KOMODO 792, and Wolfe helper provenance are
  intentional and not stranded duplicates.
- Compare the repaired record to live MediaDive 792 and the DSMZ PDF, checking
  the four top-level solution volumes and both nested reusable stock recipes.

## Additional Notes

Empty optional fields were not treated as defects. No GitHub issues, PR
comments, or source YAML edits were made during this review pass.
