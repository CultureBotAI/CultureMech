# YAML Record Review: thermoplasma_acidophilum_medium__bb19d61f

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_acidophilum_medium__bb19d61f.yaml`
- Started UTC: 2026-09-25T10:30:00Z
- Finished UTC: 2026-09-25T10:33:58Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M963 record `CultureMech:010388`.
- Media term: `TOGO:M963`, `Thermoplasma Acidophilum Medium`.
- Source claims in the record point to `https://togomedium.org/medium/M963` and JCM Medium 917.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoplasma_acidophilum_medium__bb19d61f.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- JCM Medium 917 and MediaDive medium J917 identify `THERMOPLASMA ACIDOPHILUM MEDIUM`.
- TOGO M963 cites `JCM_M917` and the JCM 917 URL, and its component list matches the JCM page.
- An exact ignored-inclusive search for `TOGO_M963_Thermoplasma_Acidophilum_Medium` found this as a single generated source, distinct from the DSMZ 158 Thermoplasma Acidophilum formulations.

## Evidence

- `/private/tmp/jcm_917.html` lists yeast extract 1 g/L, Casamino acids 1 g/L, ammonium sulfate 1.3 g/L, KH2PO4 0.3 g/L, MgSO4 x 7 H2O 0.25 g/L, NaCl 0.2 g/L, CaCl2 x 2 H2O 0.05 g/L, and 1 L distilled water.
- `/private/tmp/mediadive_J917.json` mirrors those ingredient amounts and records the pH 2.0 adjustment with 10 N H2SO4.
- `/private/tmp/togo_M963.json` independently exposes the same JCM 917 ingredient set from TOGO.
- Local identity detection used `rg --no-ignore --hidden`, so ignored generated indexes were included in the source search.

## Completeness

- The generated TOGO record captures every source ingredient.
- The generated record has no `ph_value` even though JCM 917 and TOGO M963 report pH 2.0.
- The source distilled water row is normalized as `1 G_PER_L`, which does not preserve the original 1 L water basis.
- The pH-adjustment instruction is reduced to a variable H2SO4 ingredient.

## Findings

- JCM 917's 1 L distilled-water row is represented as 1 g/L.
- pH 2.0 was not captured as `ph_value`.
- The source preparation instruction to adjust with 10 N H2SO4 is absent from `preparation_steps`.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M963_Thermoplasma_Acidophilum_Medium.yaml` so the source water basis is represented as 1 L or 1000 ml, not 1 g/L.
- Add pH 2.0 and keep the H2SO4 adjustment as preparation context.
- Regenerate the merged YAML after correcting the normalized TOGO source.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated TOGO M963 target.
- Confirm the rebuilt record includes pH 2.0 and no longer has distilled water at 1 g/L.
- Re-run an exact ignored-inclusive search for `TOGO_M963_Thermoplasma_Acidophilum_Medium` to confirm the source remains single and distinct from DSMZ 158.

## Additional Notes

None found.
