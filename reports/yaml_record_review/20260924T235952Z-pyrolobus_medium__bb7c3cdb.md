# YAML Record Review: pyrolobus_medium__bb7c3cdb

- Repository: CultureMech
- Record: data/merge_yaml/merged/pyrolobus_medium__bb7c3cdb.yaml
- Started UTC: 2026-09-24T23:59:52Z
- Finished UTC: 2026-09-25T00:00:28Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:003204` for `pyrolobus_medium`.

- Generated record: `data/merge_yaml/merged/pyrolobus_medium__bb7c3cdb.yaml`
- Normalized owner: `data/normalized_yaml/archaea/pyrolobus_medium.yaml`
- Generated from: `pyrolobus_medium`
- Source identity: `mediadive.medium:J859`, JCM GRMD 859
- Merge fingerprint: `bb7c3cdba9a729f9acbfccc61665658d435e7f65ef2ffcb04ca00f41a22c4f72`

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

The JCM identity is valid. Live JCM GRMD 859 serves PYROLOBUS MEDIUM with the
same Solution A/B/C high-level structure, and `mediadive.medium:J859` is the
right identifier for the direct MediaDive/JCM import.

An ignored-file-inclusive numeric-boundary search for `mediadive.medium:J859`
and JCM `GRMD=859` found this direct JCM owner, this generated record, the TOGO
M895 projection of the same JCM page, and a generated page for that projection.
The TOGO M895 projection should be reconciled after this direct owner is
repaired.

`KNO3`, `KI`, and `Na2SeO4` still carry deprecated numeric MediaIngredientMech
identifiers despite having primary CHEBI groundings. `MnSO4 x n H2O` is also
grounded only to generic manganese sulfate, which is acceptable for a
variable-hydrate label but should not receive a hydrate-specific synonym.

## Evidence

Live JCM 859 defines Solution A from 250 ml 2x synthetic seawater from JCM 244,
1 ml Wolfe's mineral elixir from JCM 470, 1.95 g MES, 0.5 mg resazurin, and
750 ml distilled water. Solution B is a 10 ml stock with 1 g KNO3 and 0.5 g
KH2PO4. Solution C is a 10 ml stock with 0.15 g Na2S x 9H2O. JCM then directs
the curator to add Solutions B and C at 10 ml each per liter of Solution A
before inoculation.

The JCM 244 2x synthetic seawater stock has its own 1 L composition; JCM 859
uses only 250 ml of that stock. JCM 470 Wolfe's mineral elixir is also a 1 L
stock, and JCM 859 uses only 1 ml of it. The preparation text mixes Solution A,
adjusts to pH 5.7, boils for 1 minute, cools under H2-CO2 4:1, dispenses under
the same gas, separately autoclaves Solutions B and C under N2, adds B and C
before inoculation, readjusts to pH 5.7 if necessary, and pressurizes inoculated
bottles to 200 kPa H2-CO2 4:1.

## Completeness

The generated record has pH and preparation prose, but it has no Solution A,
Solution B, or Solution C structure and no nested JCM 244 or JCM 470 stock
records. The normalized owner has a partial 2026-08-13 repair that moves four
Wolfe rows under `Wolfe's mineral elixir`, but that owner still leaves most
JCM 470 stock contents and all Solution B/C stock contents as final ingredients.

## Findings

- The generated file is stale relative to the normalized owner. It predates the
  2026-08-13 `NESTED_FLATTENED_COCKTAIL` repair that moved four Wolfe
  stock-strength rows under `Wolfe's mineral elixir`.
- The top-level JCM solution structure is absent. Source Solution A, Solution B,
  and Solution C are all flattened, and the record cannot distinguish the basal
  Solution A material from the separately autoclaved KNO3/KH2PO4 and Na2S
  stocks added before inoculation.
- Solution B and Solution C stock concentrations are stored as if they were
  final concentrations. `KNO3` is `100 G_PER_L`, `KH2PO4` is `50 G_PER_L`, and
  `Na2S x 9 H2O` is `15 G_PER_L`, but the source adds each concentrated 10 ml
  stock at 10 ml per liter of Solution A.
- The JCM 244 2x synthetic-seawater stock is imported at stock strength even
  though JCM 859 adds only 250 ml of it to Solution A. This leaves rows such as
  NaCl `55.4 G_PER_L`, MgSO4 x 7H2O `14 G_PER_L`, MgCl2 x 6H2O `11 G_PER_L`,
  and CaCl2 x 2H2O `1.5 G_PER_L` as if they were direct final concentrations.
- Wolfe's mineral elixir from JCM 470 is only partly nested. The owner still
  leaves CuSO4 x 5H2O, AlK(SO4)2 x 12H2O, Na2MoO4 x 2H2O,
  `(NH4)2Ni(SO4)2 x 6H2O`, Na2WO4 x 2H2O, and Na2SeO4 in final ingredients,
  while the generated file leaves the whole Wolfe stock flattened.
- Duplicate cleanup summed JCM 470 Wolfe concentrations into JCM 244 seawater
  rows. `NaCl` is `65.4 G_PER_L` from `55.4 + 10.0`, `MgSO4 x 7H2O` is
  `44.0 G_PER_L` from `14.0 + 30.0`, `H3BO3` is `0.16 G_PER_L` from
  `0.06 + 0.1`, and `CaCl2 x 2H2O` is `2.5 G_PER_L` from `1.5 + 1.0`.

## Recommended Edits

- Rebuild `data/normalized_yaml/archaea/pyrolobus_medium.yaml` from live JCM
  GRMD 859, preserving Solution A, Solution B, and Solution C as separate
  solutions.
- Represent 250 ml of JCM 244 2x synthetic seawater and 1 ml of JCM 470 Wolfe's
  mineral elixir as additions to Solution A. Do not flatten either referenced
  1 L stock into final-medium ingredients.
- Move KNO3 and KH2PO4 into Solution B and Na2S x 9H2O into Solution C at their
  source stock concentrations, and record those stocks as 10 ml additions per
  liter of Solution A.
- Nest the complete JCM 470 Wolfe composition under Wolfe's mineral elixir,
  including the six rows the partial cocktail repair left in main ingredients.
- Remove deprecated numeric MIM fields from `KNO3`, `KI`, and `Na2SeO4` after
  assigning exact CHEBI-keyed links where possible.
- Regenerate `data/merge_yaml/merged/pyrolobus_medium__bb7c3cdb.yaml` from the
  repaired owner and reconcile the TOGO M895 projection against it.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Run ignored-file-inclusive numeric-boundary searches for `mediadive.medium:J859`
  and `GRMD=859` to verify direct JCM and TOGO provenance are intentional and no
  exact-signature false merge remains.
- Compare the repaired record to JCM 859, JCM 244, and JCM 470, checking the
  250 ml synthetic-seawater dose, 1 ml Wolfe dose, and two 10 ml late stocks.

## Additional Notes

Empty optional fields were not treated as defects. No GitHub issues, PR
comments, or source YAML edits were made during this review pass.
