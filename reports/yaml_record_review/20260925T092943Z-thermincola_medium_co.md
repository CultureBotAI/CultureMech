# YAML Record Review: thermincola_medium_co

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermincola_medium_co.yaml
- Started UTC: 2026-09-25T09:29:43Z
- Finished UTC: 2026-09-25T09:30:02Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:000449`, `thermincola_medium_co`, grounded to DSMZ / MediaDive Medium 1028.

## Validation

- LinkML schema validation passed.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- DSMZ `DSMZ_Medium1028.pdf` is live and names medium 1028 `THERMINCOLA MEDIUM (CO)`.
- MediaDive `1028` currently resolves to status 200, count 1, source `DSMZ`, name `THERMINCOLA MEDIUM (CO)`, pH 8.0, and the DSMZ Medium 1028 PDF link.
- An exact `komodo.medium:1028` / `mediadive.medium:1028` / `DSMZ_Medium1028` / `DSMZ Medium 1028` / `thermincola_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this generated DSMZ/MediaDive record, the generated KOMODO duplicate `thermincola_medium.yaml`, and their normalized source files.

## Evidence

- DSMZ Medium 1028 and MediaDive `1028` agree on a 1003 ml final volume with direct NH4Cl, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, KCl, KH2PO4, Na-acetate, 0.5 ml of 0.1% sodium resazurin, NaHCO3, Na2CO3, `Na2S x 9 H2O`, yeast extract, 1000 ml distilled water, 1 ml Wolfe's mineral elixir, and 2 ml Wolin's vitamin solution (10x).
- DSMZ defines Wolfe's mineral elixir as a separate 1 L acidic stock with concentrated metal salts, including 30 g/L `MgSO4 x 7 H2O`, 10 g/L NaCl, and 1 g/L `CaCl2 x 2 H2O`.
- DSMZ defines Wolin's vitamin solution (10x) as a separate 1 L recipe; only 2 ml of that stock goes into the complete medium.
- The preparation says to sparge with 100% N2, dispense under 100% carbon monoxide, add yeast extract and vitamins before inoculation from sterile anoxic stocks, and adjust the complete medium to pH 8.0 with sterile anoxic 1 N HCl.

## Completeness

- The direct base compounds, final pH 8.0, and preparation notes are present.
- Wolfe's mineral elixir and Wolin's vitamin solution are flattened into final top-level ingredients at stock concentrations.
- The source-equivalent KOMODO import remains split out in `data/merge_yaml/merged/thermincola_medium.yaml`.

## Findings

- The 1 ml Wolfe's mineral elixir addition is expanded at full stock strength. Its 30 G_PER_L `MgSO4 x 7 H2O`, 5 G_PER_L `MnSO4 x H2O`, 10 G_PER_L NaCl, and other rows are stock-recipe values, not final-medium concentrations.
- Direct and stock `CaCl2 x 2 H2O` rows were merged as if both were final concentrations: the correct direct 0.0997009 G_PER_L row was summed with a 1.0 G_PER_L stock row, even though only 1 ml of Wolfe's mineral elixir is added.
- The 2 ml Wolin vitamin addition is expanded at full stock strength, so milligram-per-liter stock rows appear as 0.02, 0.1, or 0.05 G_PER_L final vitamin concentrations.
- The KOMODO `1028` record is source-equivalent to this DSMZ/MediaDive `1028` record but remains unmerged.
- `Na2SeO4` still carries a stale legacy `mediaingredientmech_term` despite having a CHEBI primary term.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/thermincola_medium_co.yaml`; repair the MediaDive import or stock-solution merge expansion, then regenerate this file.
- Preserve Wolfe's mineral elixir and Wolin's vitamin solution as nested stock additions, or dilute their contents by 1 ml / 1003 ml and 2 ml / 1003 ml if a future workflow intentionally materializes final concentrations.
- Merge this DSMZ/MediaDive branch with the KOMODO `thermincola_medium` branch using the shared DSMZ / MediaDive 1028 grounding.
- Migrate the remaining `Na2SeO4` legacy `mediaingredientmech_term` to the CHEBI-keyed slot.

## Follow-up Checks

- After importer or merge fixes, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `komodo.medium:1028`, `mediadive.medium:1028`, `DSMZ_Medium1028`, and `DSMZ Medium 1028` with ignored files included.
- Verify the regenerated record no longer has 30 G_PER_L magnesium sulfate from Wolfe's mineral elixir or 0.1 G_PER_L pyridoxine hydrochloride from Wolin's vitamin stock.
- Verify the KOMODO and DSMZ/MediaDive branches are gone or merged into the same `CultureMech` record.

## Additional Notes

None found
