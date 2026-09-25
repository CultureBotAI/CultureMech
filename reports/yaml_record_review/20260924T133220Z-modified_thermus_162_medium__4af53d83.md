# YAML Record Review: modified_thermus_162_medium__4af53d83
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_thermus_162_medium__4af53d83.yaml
- Started UTC: 2026-09-24T13:31:35Z
- Finished UTC: 2026-09-24T13:32:20Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_thermus_162_medium`, CultureMech ID `CultureMech:001761`.

- Reviewed generated record: `data/merge_yaml/merged/modified_thermus_162_medium__4af53d83.yaml`
- Reviewed canonical normalized source: `data/normalized_yaml/bacterial/modified_thermus_162_medium.yaml`
- Reviewed duplicate source set: `medium_630_modified_for_dsm_12048`, `medium_630_modified_for_dsm_12049`, `medium_630_modified_for_dsm_22673`, `medium_630_modified_for_dsm_4252`, and `medium_630_modified_for_dsm_4253`
- Media term: `mediadive.medium:630`, `DSMZ Medium 630`
- Merge fingerprint: `4af53d83b7103baff61d460153c1b8a868945490dea98f8225eca5a49af43529`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The merged identity is coherent: six DSMZ 630 source records collapsed into one `MODIFIED THERMUS 162 MEDIUM` record and the KOMODO strain-specific names were retained as synonyms/variant children.

Several grounded hydrate labels are correct, including `CaSO4 x 2 H2O`, `MgCl2 x 6 H2O`, `FeCl2 x 4 H2O`, `MnCl2 x 4 H2O`, `CuCl2 x 2 H2O`, and `Na2MoO4 x 2 H2O`.

Grounding defects remain for:

- `Na2HPO4 x 12 H2O`, which is grounded to generic `CHEBI:34683` disodium hydrogenphosphate.
- `CoCl2 x 4 H2O`, which is grounded to generic `CHEBI:35696` cobalt dichloride.
- `NiCl2 x 6 H2O`, which is grounded to generic `CHEBI:34887` nickel dichloride.

## Evidence
The live MediaDive `630` payload defines one 1 L main solution with direct 2.5 g yeast extract, 2.5 g tryptone, 28 g agar, 100 mg nitrilotriacetic acid, 40 mg CaSO4 x 2 H2O, 200 mg MgCl2 x 6 H2O, 0.5 ml of 0.01 M Fe(III) citrate, 0.5 ml Trace element solution, 100 ml Phosphate buffer, and 900 ml distilled water.

The same source defines:

- 1 L `Phosphate buffer`: 5.44 g KH2PO4 and 43 g Na2HPO4 x 12 H2O, adjusted to pH 7.2.
- 1 L `Trace element solution`: 12.8 g nitrilotriacetic acid, 1 g FeCl2 x 4 H2O, 0.5 g MnCl2 x 4 H2O, 0.3 g CoCl2 x 4 H2O, 50 mg CuCl2 x 2 H2O, 50 mg Na2MoO4 x 2 H2O, 20 mg H3BO3, and 20 mg NiCl2 x 6 H2O.
- Main-solution handling: adjust to pH 7.2 with NaOH, autoclave at 121C for 15 min, autoclave the phosphate buffer separately, then add it to the medium.

## Completeness
The generated record keeps the direct main ingredients and the pH/preparation notes, but it has no `solutions` array and cannot represent the separately autoclaved phosphate buffer or the 0.5 ml/L trace addition.

The flattened concentrations are wrong for both stocks. The phosphate rows should be diluted 100 ml per 1000 ml into the main solution, while every trace element stock row should be diluted 0.5 ml per 1000 ml. `Nitrilotriacetic acid` is especially distorted because the 0.1 g/L main ingredient and the 12.8 g/L trace-stock ingredient were summed into one 12.9 g/L ingredient.

## Findings
1. Needs curation - final and stock nitrilotriacetic acid were summed across scopes. The source has 0.1 g/L in the main solution plus 12.8 g/L in a trace stock dosed at 0.5 ml/L, not 12.9 g/L final nitrilotriacetic acid.

2. Needs curation - `KH2PO4` and `Na2HPO4 x 12 H2O` were flattened at 1 L phosphate-buffer stock strength. The DSMZ/MediaDive main formula uses only 100 ml of that buffer per liter.

3. Needs curation - all trace element solution rows were flattened at 1 L stock strength even though the main formula uses only 0.5 ml Trace element solution per liter.

4. Needs curation - the generated record omits named `Phosphate buffer` and `Trace element solution` structures, so the separate phosphate autoclaving instruction has no structured target.

5. Minor - `Na2HPO4 x 12 H2O`, `CoCl2 x 4 H2O`, and `NiCl2 x 6 H2O` should be reviewed for hydrate-specific CHEBI terms.

## Recommended Edits
- Recurate DSMZ Medium 630 with a main solution, a named phosphate buffer dosed at 100 ml/L, and a named trace element solution dosed at 0.5 ml/L.
- Keep 0.1 g/L main nitrilotriacetic acid separate from the 12.8 g/L trace-stock chelator, or calculate only the trace stock's 0.5 ml/L final contribution before any flattening.
- Preserve the source instruction that the phosphate buffer is autoclaved separately before addition to the medium.
- Apply the same repair to the five KOMODO DSMZ 630 source-duplicate normalized files, or regenerate them from the repaired canonical record if the duplicate relationship remains valid.
- Revisit dodecahydrate, cobalt tetrahydrate, and nickel hexahydrate CHEBI grounding during the repair.

## Follow-up Checks
- Re-fetch MediaDive `630` and confirm that the repaired YAML has exactly 100 ml/L phosphate buffer and 0.5 ml/L trace element solution in the main formula.
- Confirm that no merged duplicate row still reports `Nitrilotriacetic acid` at 12.9 g/L.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
