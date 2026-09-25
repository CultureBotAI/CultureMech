# YAML Record Review: sporulation_agar_sa
- Repository: CultureMech
- Record: data/merge_yaml/merged/sporulation_agar_sa.yaml
- Started UTC: 2026-09-25T07:04:00Z
- Finished UTC: 2026-09-25T07:05:49Z
- Verdict: pass with minor issues

## Target
Reviewed the generated merged record `data/merge_yaml/merged/sporulation_agar_sa.yaml`, which currently uses the KOMODO duplicate `CultureMech:006004` as the canonical merged identity and points back to the DSMZ normalized parent `data/normalized_yaml/bacterial/sporulation_agar_sa.yaml`, `CultureMech:001690`, through a `SOURCE_DUPLICATE` relationship.

The merged record carries `komodo.medium:555` and explicitly notes that the KOMODO source was copied from DSMZ Medium 555, `mediadive.medium:555`. Its ingredient signature is:

- Yeast extract: 1 g/L
- Beef extract: 1 g/L
- Tryptone peptone: 2 g/L
- FeSO4: variable
- Glucose: 10 g/L
- Agar: 15 g/L

## Validation
- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The source identity is internally consistent. The generated KOMODO child has `komodo.medium:555`, names DSMZ Medium 555 in its notes, and points to the DSMZ parent as a `SOURCE_DUPLICATE`; the parent has `mediadive.medium:555`, links the DSMZ PDF, and has the same normalized name and ingredient signature.

An exact source/id search for `mediadive.medium:555`, `komodo.medium:555`, `SPORULATION-AGAR (SA)`, `CultureMech:006004`, and `CultureMech:001690` included ignored files and found only the expected DSMZ parent, KOMODO child, merged record, and index references under `data/normalized_yaml` and `data/merge_yaml/merged`.

## Evidence
- MediaDive `/rest/medium/555` returned DSMZ Medium 555, `SPORULATION-AGAR (SA)`, with source `DSMZ`, pH 7.2, and the DSMZ Medium 555 PDF link.
- DSMZ Medium 555 PDF lists Yeast extract 1.0 g, Beef extract 1.0 g, Trypt. Peptone 2.0 g, FeSO4 trace, Glucose 10.0 g, Agar 15.0 g, Distilled water 1000.0 ml, and `pH 7.2`.
- The generated record preserves the source mass concentrations for the non-water ingredients and represents DSMZ's trace FeSO4 as a nonnumeric variable concentration rather than inventing a mass.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed DSMZ/MediaDive material names organism growth for this recipe, so that is not a defect.

The DSMZ parent includes a single preparation step, `pH 7.2`; the generated KOMODO-canonical merged record preserves the numeric pH in `ph_value` but does not carry that preparation step.

## Findings
- Low: The `SOURCE_DUPLICATE` merge chose the KOMODO child as the generated canonical record, so the generated record carries `komodo.medium:555` even though the formulation is resolved from DSMZ Medium 555. This also drops the normalized DSMZ parent's explicit preparation step, `pH 7.2`. The formula and `ph_value` are still preserved, so this is provenance/detail loss rather than a concentration error.

## Recommended Edits
- No ingredient corrections are required.
- If the duplicate merge canonical-selection logic is revisited, prefer the DSMZ/MediaDive source as the canonical parent for this pair or propagate the DSMZ preparation step into the generated KOMODO-canonical `SOURCE_DUPLICATE` output.

## Follow-up Checks
- After changing duplicate-merge heuristics, regenerate merged YAML and confirm `CultureMech:001690` and `CultureMech:006004` still collapse to one source-duplicate recipe with DSMZ Medium 555 provenance intact.

## Additional Notes
MediaDive's REST payload reported an internally inconsistent agar row with `amount: 20` and `g_l: 15`; the DSMZ PDF lists Agar 15.0 g, and the generated YAML uses 15 g/L, so no edit is needed for the agar concentration.
