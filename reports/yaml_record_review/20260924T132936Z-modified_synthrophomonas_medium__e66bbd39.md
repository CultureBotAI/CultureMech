# YAML Record Review: modified_synthrophomonas_medium__e66bbd39
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_synthrophomonas_medium__e66bbd39.yaml
- Started UTC: 2026-09-24T13:28:51Z
- Finished UTC: 2026-09-24T13:29:36Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_synthrophomonas_medium`, CultureMech ID `CultureMech:002887`.

- Reviewed generated record: `data/merge_yaml/merged/modified_synthrophomonas_medium__e66bbd39.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/modified_synthrophomonas_medium.yaml`
- Media term: `mediadive.medium:J539`, `MODIFIED SYNTHROPHOMONAS MEDIUM`
- Source note: `JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=539`
- Merge fingerprint: `e66bbd3919140e0e2e2b9d30994b444adf9e7a6614ce26749e42a34f24de6c35`
- `merged_from`: `modified_synthrophomonas_medium`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The medium identity is coherent for JCM/MediaDive `J539`, and the final pH of 7.2 matches the live MediaDive payload.

Most simple salts and vitamins that are present have plausible CHEBI grounding, but two issues remain:

- `NiCl2 x 6 H2O` is grounded to generic `CHEBI:34887` nickel dichloride, losing the source hexahydrate state.
- The final anaerobic completion ingredients named only in prose, including sodium pyruvate, NaHCO3, L-cysteine x HCl x H2O, and Na2S x 9H2O, have no structured term grounding or concentrations.

## Evidence
The direct JCM URL for `GRMD=539` currently returns `Nothing found`.

The live MediaDive `J539` payload still exposes the recipe as a stock-dependent Solution A:

- `Solution A` is 902 ml and contains 50 ml `Mineral solution`, 1 ml `FeCl2 solution`, 1 ml `Trace element solution`, 5 ml `Vitamin solution`, 20 mM glucose, 1 g yeast extract, 0.5 g peptone, 2.8 g Na2SO4, 1 mg resazurin, and 845 ml distilled water.
- `Mineral solution`, `FeCl2 solution`, `Trace element solution`, and `Vitamin solution` are separate 1 L stocks.
- Final completion is procedural: distribute Solution A anaerobically, autoclave it, then add 10 mM final sodium pyruvate, 0.1 volume of 3.5% NaHCO3, 0.3 g/L final L-cysteine x HCl x H2O, and 0.3 g/L final Na2S x 9H2O.

## Completeness
The generated record preserves pH 7.2 and the long preparation note, and it correctly carries the Solution A direct ingredients after MediaDive converted their 902 ml amounts to g/L.

It is incomplete for the stock-solution portion. The Mineral, FeCl2, Trace element, and Vitamin solution components are represented as final ingredients at stock strength. The correct dilution factors into Solution A are 50/902 for Mineral solution, 1/902 for FeCl2 solution, 1/902 for Trace element solution, and 5/902 for Vitamin solution before any later final-volume adjustment.

The record is also incomplete for the final post-autoclave additions because sodium pyruvate, NaHCO3, L-cysteine x HCl x H2O, and Na2S x 9H2O are present only inside `preparation_steps[0].description`.

## Findings
1. Needs curation - stock recipes were flattened without scaling. For example, `KH2PO4` is recorded as 10 g/L from the Mineral solution stock, `FeCl2 x 4 H2O` is recorded as 1.5 g/L from the FeCl2 stock, and trace/vitamin ingredients are recorded at their stock g/L values instead of their 50/902, 1/902, or 5/902 contributions to Solution A.

2. Needs curation - required final additions are unstructured. The live source instructs curators to add 10 mM final sodium pyruvate, 0.1 volume of 3.5% NaHCO3 solution, 0.3 g/L final L-cysteine x HCl x H2O, and 0.3 g/L final Na2S x 9H2O, but none of those appears in `ingredients` or `solutions`.

3. Needs curation - the generated recipe has no `solutions` array, so named Solution A and its four stock solutions are not recoverable as first-class structures.

4. Minor - `NiCl2 x 6 H2O` should be reviewed for a hydrate-specific CHEBI term; the current generic nickel dichloride grounding discards the source hexahydrate label.

5. Minor - the direct JCM provenance URL is stale. A live fetch of `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=539` returned `Nothing found`, so MediaDive `J539` is the resolvable formula source.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/modified_synthrophomonas_medium.yaml` from MediaDive `J539` with Solution A, Mineral solution, FeCl2 solution, Trace element solution, and Vitamin solution as named solutions.
- Scale stock contributions by their source volumes before emitting any flattened final ingredient list, or leave the stocks nested and make the volume relationships explicit.
- Add structured post-autoclave additions for sodium pyruvate, 3.5% NaHCO3 solution, L-cysteine x HCl x H2O, and Na2S x 9H2O.
- Preserve the anaerobic handling instructions, gas mixture, butyl rubber stopper instruction, separate autoclaving and filter sterilization notes, and N2 stock-storage note as ordered preparation steps.
- Revisit `NiCl2 x 6 H2O` grounding during the same repair.

## Follow-up Checks
- Re-fetch MediaDive `J539` and confirm that the repaired YAML contains the 902 ml Solution A and all four nested stocks with the same component order.
- Check that final structured additions include 10 mM sodium pyruvate and 0.3 g/L each cysteine reductant and sulfide reductant.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
