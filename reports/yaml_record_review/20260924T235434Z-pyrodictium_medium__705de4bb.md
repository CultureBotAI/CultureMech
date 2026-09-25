# YAML Record Review: pyrodictium_medium__705de4bb

- Repository: CultureMech
- Record: data/merge_yaml/merged/pyrodictium_medium__705de4bb.yaml
- Started UTC: 2026-09-24T23:54:34Z
- Finished UTC: 2026-09-24T23:55:20Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:001381` for
`pyrodictium_medium`.

- Generated record: `data/merge_yaml/merged/pyrodictium_medium__705de4bb.yaml`
- Normalized owner: `data/normalized_yaml/archaea/pyrodictium_medium.yaml`
- Generated from: `pyrodictium_medium`
- Source identity: `mediadive.medium:283`
- Merge fingerprint: `705de4bb54d20ba5523f882e3f1b7b35f4ccaa6cf738a942f456befb98b5876e`

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

The direct DSMZ/MediaDive identity is valid: live MediaDive medium 283 and the
DSMZ PDF both serve `PYRODICTIUM MEDIUM`, and `mediadive.medium:283` is the
right identifier for this direct import.

An ignored-file-inclusive exact search for `mediadive.medium:283`, the DSMZ
Medium 283 PDF name, and `DSMZ, ID: 283` found this owner and generated record.
It also found `data/normalized_yaml/archaea/KOMODO_283_PYRODICTIUM_medium.yaml`
and generated `data/merge_yaml/merged/PYRODICTIUM_MEDIUM.yaml`, which carry the
same DSMZ 283 provenance through `komodo.medium:283`. That KOMODO source is a
same-DSMZ projection and should be reconciled with the direct MediaDive owner;
its `Aerobic: Yes` note also contradicts the anoxic H2/CO2 DSMZ protocol.

The most important grounding issue is sulfur: DSMZ says `Sulfur (powdered)`,
but the record grounds it to `CHEBI:26833` sulfur atom instead of elemental
sulfur. `NiCl2 x 6 H2O` is also over-broadly grounded to anhydrous nickel
dichloride, and `KI` still carries a deprecated numeric
`mediaingredientmech_term` despite having a CHEBI grounding.

## Evidence

MediaDive and the DSMZ PDF describe a 1025 ml main solution. Many main rows are
already normalized by MediaDive from source amounts into final grams per liter:
for example 13.85 g NaCl becomes 13.5122 g/L and 3.50 g MgSO4 x 7H2O becomes
3.41463 g/L. The source also adds 10 ml Modified Wolin's mineral solution.

Modified Wolin's mineral solution is a separate 1 L stock from DSMZ medium 141.
It contains nitrilotriacetic acid, MgSO4 x 7H2O, MnSO4 x H2O, NaCl, FeSO4 x
7H2O, CoSO4 x 7H2O, CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2 x
12H2O, H3BO3, Na2MoO4 x 2H2O, NiCl2 x 6H2O, Na2SeO3 x 5H2O, Na2WO4 x 2H2O, and
1 L distilled water. The stock directions dissolve NTA, adjust to pH 6.5 with
KOH, add minerals, and adjust final pH to 7.0 with KOH.

The source preparation text is largely present: pH 5.0 to 5.5 adjustment with
10 N sulfuric acid, 80% H2 / 20% CO2 sparging for 30 to 45 minutes, dispensing
into anoxic vessels containing sulfur, 90-100C sterilization on 3 successive
days with no autoclave, yeast extract and sulfide addition from sterile anoxic
stocks made under 100% N2, final pH 5.5 readjustment if needed, and
post-inoculation pressurization to 2 bar overpressure with sterile 80% H2 / 20%
CO2.

## Completeness

The owner has pH and preparation steps, but it does not preserve the 10 ml
Modified Wolin stock addition as a solution. Its components are instead flattened
into the final ingredient list at stock-liter concentrations.

## Findings

- Modified Wolin's mineral solution was flattened and its 10 ml dose was lost.
  Stock-only components such as NTA, MnSO4 x H2O, FeSO4 x 7H2O, CoSO4 x 7H2O,
  ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2 x 12H2O, Na2MoO4 x 2H2O,
  Na2SeO3 x 5H2O, and Na2WO4 x 2H2O now appear as if their stock-liter amounts
  were final-medium grams per liter.
- Duplicate cleanup summed stock-liter concentrations into MediaDive's
  1025 ml-scaled main-solution concentrations. `NaCl` is `14.5122 G_PER_L`
  instead of the MediaDive main-solution value `13.5122`, `MgSO4 x 7 H2O` is
  `6.41463 G_PER_L` instead of `3.41463`, `H3BO3` is `0.0246341 G_PER_L`
  instead of `0.0146341`, `CaCl2 x 2 H2O` is `0.831707 G_PER_L` instead of
  `0.731707`, and `NiCl2 x 6 H2O` is `0.03195122 G_PER_L` instead of
  `0.00195122`.
- The same DSMZ 283 source is represented by a second KOMODO owner at
  `data/normalized_yaml/archaea/KOMODO_283_PYRODICTIUM_medium.yaml`; the KOMODO
  projection repeats the flattened/summed ingredient rows and carries an
  `Aerobic: Yes` note even though DSMZ 283 is explicitly sparged and dispensed
  under H2/CO2.
- Sulfur powder is over-generalized to `CHEBI:26833` sulfur atom, and the
  nickel chloride hexahydrate source row is grounded to anhydrous nickel
  dichloride.
- The `KI` row still has `mediaingredientmech_term: MediaIngredientMech:000232`
  even though the row is already keyed to `CHEBI:8346`; it should not retain a
  deprecated numeric MediaIngredientMech identifier.

## Recommended Edits

- Restore `Modified Wolin's mineral solution` as the 10 ml solution addition
  from DSMZ medium 141, either by linking a verified reusable solution record or
  by nesting the live DSMZ stock composition.
- Recompute final ingredients from the 1025 ml main solution without adding
  Modified Wolin stock-liter values into the main NaCl, MgSO4 x 7H2O, H3BO3,
  CaCl2 x 2H2O, and NiCl2 x 6H2O rows.
- Reconcile `KOMODO_283_PYRODICTIUM_medium.yaml` with
  `pyrodictium_medium.yaml` so DSMZ medium 283 no longer has a stranded KOMODO
  projection, and drop the erroneous KOMODO aerobic label when that source is
  kept only as a duplicate provenance note.
- Re-ground `Sulfur (powdered)` to elemental sulfur, replace the broad NiCl2
  grounding with a hexahydrate-specific term or leave it ungrounded, and remove
  the legacy numeric MIM field from `KI`.
- Regenerate `data/merge_yaml/merged/pyrodictium_medium__705de4bb.yaml` from the
  repaired owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Run ignored-file-inclusive searches for `mediadive.medium:283`,
  `DSMZ_Medium283.pdf`, and `komodo.medium:283` to verify DSMZ 283 provenance is
  reconciled across direct MediaDive and KOMODO sources.
- Compare the repaired record against live MediaDive medium 283 and the rendered
  DSMZ PDF, checking that only source main-solution rows stay in the final
  ingredient list and that Modified Wolin stock remains separate.

## Additional Notes

Empty optional fields were not treated as defects. No GitHub issues, PR
comments, or source YAML edits were made during this review pass.
