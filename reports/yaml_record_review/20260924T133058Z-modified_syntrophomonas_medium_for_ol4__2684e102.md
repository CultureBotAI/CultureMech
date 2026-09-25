# YAML Record Review: modified_syntrophomonas_medium_for_ol4__2684e102
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_syntrophomonas_medium_for_ol4__2684e102.yaml
- Started UTC: 2026-09-24T13:30:21Z
- Finished UTC: 2026-09-24T13:30:58Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_syntrophomonas_medium_for_ol4`, CultureMech ID `CultureMech:002889`.

- Reviewed generated record: `data/merge_yaml/merged/modified_syntrophomonas_medium_for_ol4__2684e102.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/modified_syntrophomonas_medium_for_ol4.yaml`
- Media term: `mediadive.medium:J540`, `MODIFIED SYNTROPHOMONAS MEDIUM FOR OL4`
- Source note: `JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=540`
- Merge fingerprint: `2684e1020ab5f993228d95a9bf80a96a989b5218888ef7c84bc19f6e6e3f5079`
- `merged_from`: `modified_syntrophomonas_medium_for_ol4`

## Validation
- Open LinkML validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The medium identity and defined-medium classification match JCM/MediaDive `J540`. The final pH of 7.2 also matches the live MediaDive payload.

The salt and vitamin terms that are present are mostly plausible, but the structured list is not final-medium chemistry:

- `NiCl2 x 6 H2O` is grounded to generic `CHEBI:34887` nickel dichloride, losing the hexahydrate state.
- Sodium oleate is present at the 1.5 g/L Solution B stock concentration, not the final concentration after Solution B contributes 0.1 volume.
- NaHCO3, L-cysteine x HCl x H2O, and Na2S x 9H2O are final additions in the source procedure but are not structured ingredients.

## Evidence
The direct JCM URL for `GRMD=540` currently returns `Nothing found`.

The live MediaDive `J540` payload defines:

- `Solution A`, 802 ml, containing 50 ml Mineral solution, 1 ml FeCl2 solution, 1 ml Trace element solution, 5 ml Vitamin solution, 2.8 g Na2SO4, 1 mg resazurin, and 745 ml distilled water.
- `Solution B`, 100 ml, containing 0.15 g sodium oleate and 100 ml distilled water.
- The same 1 L Mineral, FeCl2, Trace element, and Vitamin stocks used by the adjacent JCM `J539` Synthrophomonas medium.
- Final completion by combining 0.8 volume Solution A, 0.1 volume Solution B, and 0.1 volume 3.5% NaHCO3 solution, then reducing with 0.3 g/L final L-cysteine x HCl x H2O and 0.3 g/L final Na2S x 9H2O.

## Completeness
The generated YAML retains pH 7.2, both direct Solution A ingredients, and the Sodium oleate in Solution B, but it drops the actual solution hierarchy.

The flattened ingredients are not final-medium concentrations. Mineral stock rows need the 50/802 Solution A dilution and then the 0.8 final dilution; FeCl2 and trace stock rows need 1/802 and then 0.8; vitamin rows need 5/802 and then 0.8; sodium oleate needs the 0.1 final Solution B dilution. The 3.5% NaHCO3 solution and reductants remain unstructured.

## Findings
1. Needs curation - multiple stock solutions were flattened at stock strength. `KH2PO4`, `FeCl2 x 4 H2O`, the trace salts, the vitamins, and `Sodium oleate` all appear at source stock g/L values even though MediaDive `J540` dilutes them through Solution A or Solution B before final combination.

2. Needs curation - final completion additions are missing from the structured recipe. The live source requires 0.1 volume 3.5% NaHCO3 solution plus final 0.3 g/L L-cysteine x HCl x H2O and 0.3 g/L Na2S x 9H2O, but those are prose only in the generated YAML.

3. Needs curation - `Solution A`, `Solution B`, Mineral solution, FeCl2 solution, Trace element solution, and Vitamin solution are absent as named solutions, which makes the generated recipe impossible to execute from structured fields alone.

4. Minor - `NiCl2 x 6 H2O` should be reviewed for a hydrate-specific CHEBI term; the current generic nickel dichloride grounding discards the source hexahydrate label.

5. Minor - the strain note still contains source HTML tags: `<I>Methanobacterium formicicum</I>`. The note should be plain text in curated YAML.

6. Minor - the direct JCM provenance URL is stale. A live fetch of `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=540` returned `Nothing found`, so MediaDive `J540` is the resolvable formula source.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/modified_syntrophomonas_medium_for_ol4.yaml` from MediaDive `J540` with Solution A, Solution B, Mineral solution, FeCl2 solution, Trace element solution, and Vitamin solution as named solutions.
- Represent the final 0.8/0.1/0.1 Solution A, Solution B, and bicarbonate mixture explicitly before flattening concentrations.
- Add structured final reductants for L-cysteine x HCl x H2O and Na2S x 9H2O at 0.3 g/L final each.
- Strip HTML from the strain-specific co-culture note.
- Revisit `NiCl2 x 6 H2O` grounding during the same repair.

## Follow-up Checks
- Re-fetch MediaDive `J540` and confirm that the repaired YAML contains both 802 ml Solution A and 100 ml Solution B.
- Confirm that any flattened final concentrations have both the stock dilution and the 0.8 or 0.1 final-volume factors applied.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
