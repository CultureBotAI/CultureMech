# YAML Record Review: fumarate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fumarate_medium.yaml
- Started UTC: 2026-09-23T04:55:44Z
- Finished UTC: 2026-09-23T04:57:36Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:004253` / `fumarate_medium`, the KOMODO 195a import backfilled from DSMZ composition.
- Compared it with maintained source `data/normalized_yaml/bacterial/fumarate_medium.yaml` and the direct DSMZ 195a owner `data/normalized_yaml/bacterial/desulfuromusa_medium.yaml`.
- Cross-checked the MediaDive REST payloads for DSMZ 195a and DSMZ 195 and the DSMZ Medium 195a PDF.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `komodo.medium:195a` identifies a KOMODO record named FUMARATE MEDIUM and notes a DSMZ 195a relationship, but the generated ingredients do not match DSMZ Medium 195a.
- Exact ignored-inclusive lookup for `komodo.medium:195a`, `CultureMech:004253`, `mediadive.medium:195a`, and `name: fumarate_medium` covered normalized and generated YAML; it found this maintained KOMODO owner, the direct MediaDive 195a `desulfuromusa_medium` owner, index entries, and the unsuffixed generated file.
- The maintained curation history says DSMZ enrichment copied ingredients from DSMZ Medium 195 even though this record is keyed to 195a.
- The record has no fumarate ingredient at all and instead carries `Na-propionate`, which is incompatible with both the KOMODO name and DSMZ 195a.
- NiCl2 x 6 H2O is grounded only to nickel dichloride, losing the source hexahydrate form.

## Evidence

- DSMZ Medium 195a defines DESULFUROMUSA MEDIUM from 952 ml Solution A, 30 ml Solution B, 10 ml Solution C, 1 ml Solution D, and 10 ml Solution E.
- In DSMZ 195a, Solution C contains 2.5 g Na2-fumarate in 10 ml Distilled water. The direct MediaDive 195a owner preserves `Na2-fumarate`, but this KOMODO 195a record has `Na-propionate` at 150 g/L and lacks Na2-fumarate entirely.
- Solution A contains 3 g Na2SO4, 0.2 g KH2PO4, 0.3 g NH4Cl, 21 g NaCl, 3 g MgCl2 x 6 H2O, 0.5 g KCl, 0.15 g CaCl2 x 2 H2O, 1 ml SL-10, 1 ml Selenite-tungstate solution, 0.5 ml 0.1% Sodium resazurin, and 950 ml Distilled water. The generated record uses the stock-normalized Solution A `g_l` values as top-level final rows.
- Solutions B, E, Selenite-tungstate solution, Trace element solution SL-10, and Wolin's vitamin solution are flattened into top-level stock-strength ingredients, including 50 g/L Na2CO3, 40 g/L Na2S x 9 H2O, trace metals, and vitamins.
- The generated `sodium` ingredient with `VARIABLE` concentration was extracted from a pH-buffer note even though the DSMZ 195a recipe already represents its sodium carbonate buffer explicitly as Solution B.
- DSMZ 195a says Solutions C and D are prepared under 100% N2 and filter-sterilized, Solution B is autoclaved under 80% N2 and 20% CO2, and Solution E is autoclaved separately under 100% N2; none of those solution-specific sterilization boundaries are present.

## Completeness

- Fumarate, the defining substrate for this record, is missing.
- Solution A, Solution B, Solution C, Solution D, Solution E, Selenite-tungstate solution, Trace element solution SL-10, and Wolin's vitamin solution are not structurally represented.
- Stock preparation, gassing, autoclaving, and filter-sterilization instructions are missing.
- The direct DSMZ 195a `desulfuromusa_medium` source duplicate is not linked from this KOMODO 195a record.

## Findings

- Major: the KOMODO 195a record has `Na-propionate` instead of DSMZ 195a `Na2-fumarate`, so the generated FUMARATE MEDIUM lacks fumarate.
- Major: DSMZ 195a Solutions A through E are flattened into top-level `G_PER_L` rows instead of represented as source stock additions.
- Major: Selenite-tungstate, SL-10, and Wolin's vitamin stock recipes are flattened at stock strength.
- Major: solution-specific DSMZ sterilization and gassing instructions are absent.
- Minor: the extracted variable `sodium` row is an unsupported artifact of note parsing.
- Minor: NiCl2 x 6 H2O is grounded to an anhydrous nickel dichloride term.

## Recommended Edits

- Correct the maintained KOMODO 195a source so Solution C contains DSMZ 195a Na2-fumarate, not Na-propionate.
- Link the KOMODO 195a record to the direct DSMZ 195a `desulfuromusa_medium` record as a source-equivalent duplicate if KOMODO is meant to mirror DSMZ 195a.
- Rebuild the recipe with explicit Solution A, Solution B, Solution C, Solution D, Solution E, Selenite-tungstate solution, Trace element solution SL-10, and Wolin's vitamin solution structures.
- Keep trace-element and vitamin components scoped to their stocks and encode the source 952 ml, 30 ml, 10 ml, 1 ml, and 10 ml solution assembly.
- Remove the unsupported variable `sodium` row.
- Regenerate `data/merge_yaml/merged/fumarate_medium.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated KOMODO 195a YAML.
- Confirm the generated record contains Na2-fumarate and no Na-propionate.
- Confirm stock-only trace-element, selenite-tungstate, and vitamin ingredients do not appear as top-level final-medium rows.
- Confirm Solution C and Solution D carry filter-sterilized handling while Solutions A, B, and E keep their source gas/autoclave handling.
- Confirm the variable `sodium` ingredient is gone.

## Additional Notes

- The generated file is derived data and is a one-source merge. The wrong propionate substrate and stock flattening are present in maintained normalized YAML.
