# YAML Record Review: pyrodictium_ocultum_medium__440d69e3

- Repository: CultureMech
- Record: data/merge_yaml/merged/pyrodictium_ocultum_medium__440d69e3.yaml
- Started UTC: 2026-09-24T23:56:17Z
- Finished UTC: 2026-09-24T23:57:04Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:002566` for
`pyrodictium_ocultum_medium`.

- Generated record: `data/merge_yaml/merged/pyrodictium_ocultum_medium__440d69e3.yaml`
- Normalized owners: `data/normalized_yaml/archaea/pyrodictium_brockii_medium.yaml`,
  `data/normalized_yaml/archaea/pyrodictium_ocultum_medium.yaml`, and
  `data/normalized_yaml/archaea/pyrodictium_abysii_medium.yaml`
- Generated from: `pyrodictium_brockii_medium`, `pyrodictium_ocultum_medium`,
  `pyrodictium_abysii_medium`
- Source identities: `mediadive.medium:J203`, `mediadive.medium:J204`,
  `mediadive.medium:J205`
- Merge fingerprint: `440d69e3dec5445595b9094373d58ce7db78f3deeb65deba4496e9e3b113f97a`

`data/merge_yaml/merged` is generated output. The required repair is to split
and rebuild the three normalized JCM owners before regenerating this target.

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

The JCM source identities are real, but they are not source duplicates. Live JCM
203 defines PYRODICTIUM BROCKII MEDIUM. Live JCM 204 says to use medium 203
with 0.2 g/L final yeast extract. Live JCM 205 says to use medium 203 with
0.5 g/L final yeast extract and 0.1 mg/L Na2WO4 x 2H2O, and to omit citric
acid.

An ignored-file-inclusive exact search for `mediadive.medium:J203`,
`mediadive.medium:J204`, `mediadive.medium:J205`, and JCM `GRMD=203`,
`GRMD=204`, and `GRMD=205` found the three direct MediaDive/JCM owners, this
generated merged record, older TOGO projections for the same three JCM pages,
and generated pages for those projections. Those same-source TOGO projections
need reconciliation after the direct JCM owners are corrected.

The copied JCM 203 groundings also carry through earlier errors: sulfur powder
is grounded to `CHEBI:26833` sulfur atom instead of elemental sulfur, and `KI`
still has a deprecated numeric `mediaingredientmech_term` despite already being
grounded to `CHEBI:8346`.

## Evidence

JCM 203 is a Pyrodictium brockii medium built from 1 L Salt base solution from
JCM 151, 10 ml Trace minerals from JCM 151, 2 g yeast extract, 30 g sulfur
powder, 1 mg resazurin, and a 10 ml per-liter addition of sterile neutral 5%
Na2S x 9H2O after sterilization.

JCM 203 also carries the operative preparation: mix everything except sulfur,
adjust to pH 5.5 with H2SO4, autoclave under N2, steam sulfur for 3 hr on each
of 3 successive days, aseptically distribute medium and sulfur under an H2-CO2
80:20 stream, add the 5% Na2S solution before inoculation, readjust to pH 5.5 if
needed, and pressurize inoculated vessels to 200 kPa H2-CO2 80:20.

JCM 204 and JCM 205 are not identical recipes. JCM 204 only lowers the final
yeast extract to 0.2 g/L relative to JCM 203. JCM 205 lowers the final yeast
extract to 0.5 g/L, adds 0.1 mg/L Na2WO4 x 2H2O, and omits citric acid.

## Completeness

The generated record is incomplete and over-merged. It keeps JCM 204 as the
canonical `media_term`, copies JCM 203 bulk ingredients into all three owners,
lists JCM 203 and JCM 205 only as synonyms, and stores a one-line JCM 204
preparation note instead of the full JCM 203 protocol plus source-specific J204
and J205 deltas.

## Findings

- JCM 203, 204, and 205 were falsely merged as exact source duplicates. They are
  related recipes but not identical: JCM 204 changes yeast extract to 0.2 g/L
  final, while JCM 205 changes yeast extract to 0.5 g/L final, adds 0.1 mg/L
  Na2WO4 x 2H2O, and omits citric acid.
- `copy_referenced_compositions` copied JCM 203's ingredient rows into JCM 204
  and JCM 205 without applying those source deltas. The generated JCM 204 record
  still has yeast extract at `1.96078 G_PER_L`, and the merged JCM 205 synonym
  still implies citric acid is present and never adds tungstate.
- JCM 203's 5% Na2S x 9H2O solution was flattened incorrectly. The source adds
  10 ml/L of a 5% sulfide solution after sterilization, which contributes about
  0.5 g/L final Na2S x 9H2O; the normalized owners carry `Na2S x 9 H2O` at
  `10 G_PER_L` because the 10 ml stock dose became a gram-per-liter
  concentration.
- The inherited JCM 151 Salt base solution and Trace minerals stock were
  flattened into the main ingredient list. Their duplicate NaCl, MgSO4 x 7H2O,
  and H3BO3 rows were summed, while trace-only components such as NTA, FeSO4 x
  7H2O, CoSO4 x 7H2O, CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2, and
  Na2MoO4 x 2H2O appear as final-medium gram-per-liter components.
- The generated canonical record loses the full JCM 203 anaerobic procedure. It
  only retains `Use Medium No. 203 with 0.2 g/L (final) yeast extract`, so pH
  5.5 adjustment, N2 autoclaving, sulfur steaming, H2-CO2 anaerobic
  distribution, sulfide addition, and 200 kPa post-inoculation pressurization
  are absent from generated output.
- The source relationship metadata points at non-existent bacterial paths such
  as `data/normalized_yaml/bacterial/pyrodictium_abysii_medium.yaml`; the actual
  JCM 203, JCM 204, and JCM 205 owners all live under
  `data/normalized_yaml/archaea/`.

## Recommended Edits

- Split the JCM 203, JCM 204, and JCM 205 owners into three true variants
  rather than merging them as `SOURCE_DUPLICATE` records.
- Rebuild JCM 203 against live JCM 203, preserving JCM 151 Salt base solution,
  JCM 151 Trace minerals, and the 10 ml/L neutral 5% Na2S stock as stock
  additions instead of flattening all referenced stocks into final ingredients.
- Rebuild JCM 204 by referencing JCM 203 with only the final yeast extract
  changed to 0.2 g/L.
- Rebuild JCM 205 by referencing JCM 203 with final yeast extract changed to
  0.5 g/L, 0.1 mg/L Na2WO4 x 2H2O added, and citric acid omitted.
- Restore the full JCM 203 anaerobic preparation to the base record and keep the
  JCM 204 and JCM 205 pages' variant text as modifications, not as replacements
  for the base protocol.
- Correct the sulfur and `KI` legacy groundings, and repair stale
  `data/normalized_yaml/bacterial/...` relationship paths to the actual
  `data/normalized_yaml/archaea/...` owners.
- Reconcile the TOGO M196, M197, and M198 projections of the same JCM pages
  after the direct MediaDive/JCM owners have been repaired.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Run ignored-file-inclusive searches for `mediadive.medium:J203`,
  `mediadive.medium:J204`, `mediadive.medium:J205`, and `GRMD=203` through
  `GRMD=205` to verify the direct JCM and TOGO projections have intentional
  provenance links without an exact-signature false merge.
- Compare generated YAML against the three live JCM pages, specifically checking
  JCM 204's 0.2 g/L yeast extract and JCM 205's yeast, tungstate, and citric
  acid changes.

## Additional Notes

Empty optional fields were not treated as defects. No GitHub issues, PR
comments, or source YAML edits were made during this review pass.
