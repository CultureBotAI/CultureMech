# YAML Record Review: thermoplasma_kamchatkensis_medium__57d65c1c

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_kamchatkensis_medium__57d65c1c.yaml`
- Started UTC: 2026-09-25T10:30:00Z
- Finished UTC: 2026-09-25T10:34:00Z
- Verdict: needs curation

## Target

- Reviewed generated direct JCM 1239 record `CultureMech:002405`.
- Media term: `mediadive.medium:J1239`, `THERMOPLASMA KAMCHATKENSIS MEDIUM`.
- Source claims in the record point to JCM Medium 1239 through MediaDive.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoplasma_kamchatkensis_medium__57d65c1c.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- JCM Medium 1239 and MediaDive medium J1239 identify `THERMOPLASMA KAMCHATKENSIS MEDIUM`.
- TOGO M1333 also cites `JCM_M1239` and imports the same JCM page.
- An exact ignored-inclusive search found `data/normalized_yaml/archaea/TOGO_M1333_Thermoplasma_Kamchatkensis_Medium.yaml` and its generated `data/merge_yaml/merged/THERMOPLASMA_KAMCHATKENSIS_MEDIUM.yaml` counterpart as a duplicate JCM 1239 import.

## Evidence

- `/private/tmp/jcm_1239.html` lists KH2PO4 3 g/L, MgSO4 x 7 H2O 1 g/L, CaCl2 x 2 H2O 0.25 g/L, ammonium sulfate 0.2 g/L, yeast extract 0.1 g/L, sucrose 5 g/L, sulfur powder 4 g/L, and 1 L distilled water.
- `/private/tmp/mediadive_J1239.json` mirrors JCM 1239 and reports pH 2.5 plus the autoclave, sulfur steaming, N2-CO2 gas replacement, and sealing instructions.
- `/private/tmp/togo_M1333.json` independently exposes the same formula from TOGO and shows the gas phase imported as gas components.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact Thermoplasma source identifiers and filenames, so ignored generated indexes were included.

## Completeness

- The direct JCM generated record captures the seven non-water JCM ingredients, pH 2.5, and the full preparation step.
- The source 1 L distilled-water row is missing.
- The source sulfur powder ingredient is grounded to `CHEBI:26833`, sulfur atom, rather than the elemental sulfur grounding already present in the TOGO M1333 duplicate.
- The same JCM 1239 formulation exists as a separate TOGO M1333 generated record.

## Findings

- The direct JCM 1239 import omitted distilled water.
- Sulfur powder is grounded to sulfur atom rather than elemental sulfur.
- JCM 1239 is split across direct and TOGO generated outputs, with the direct record preserving preparation text but the TOGO duplicate adding variable gas ingredients and losing the preparation step.

## Recommended Edits

- Preserve distilled water in `data/normalized_yaml/archaea/thermoplasma_kamchatkensis_medium.yaml` or the MediaDive/JCM import path.
- Reground sulfur powder to elemental sulfur.
- Merge the direct JCM 1239 and TOGO M1333 sources into one canonical Thermoplasma Kamchatkensis Medium record after water and sulfur are repaired.
- Preserve the direct JCM preparation instruction and keep the N2-CO2 gas phase as preparation context rather than top-level variable ingredients.

## Follow-up Checks

- Rebuild the merged YAML and confirm that JCM 1239 has distilled water, pH 2.5, sulfur powder grounded to elemental sulfur, and a preparation step.
- Re-run schema, strict, reference, and term validation on the regenerated JCM 1239 target.
- Re-run an exact ignored-inclusive search for `TOGO_M1333_Thermoplasma_Kamchatkensis_Medium` and `mediadive.medium:J1239` to confirm JCM 1239 has one generated output.

## Additional Notes

- An initial local search for the Kamchatkensis duplicate used unrelated `JCM 945`, `mediadive.medium:945`, and `M2449` patterns and matched unrelated Methanobacterium, Marinitoga, and Trypticase records; I discarded that output and reran the search with exact Thermoplasma IDs.
