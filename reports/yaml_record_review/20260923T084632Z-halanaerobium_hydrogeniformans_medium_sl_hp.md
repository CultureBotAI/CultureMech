# YAML Record Review: HALANAEROBIUM HYDROGENIFORMANS MEDIUM (SL-HP)

- Repository: CultureMech
- Record: data/merge_yaml/merged/halanaerobium_hydrogeniformans_medium_sl_hp.yaml
- Started UTC: 2026-09-23T08:45:28Z
- Finished UTC: 2026-09-23T08:46:32Z
- Verdict: needs curation

## Target

- Reviewed generated YAML for `HALANAEROBIUM HYDROGENIFORMANS MEDIUM (SL-HP)`.
- Stable ID: `CultureMech:001138`.
- Primary source in generated record: DSMZ/MediaDive `mediadive.medium:1656`.
- Merge fingerprint: `ebe3ed85f26494a93542cfdcbf490153486d8b484c2840e484af2401c840ef52`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass; the validator exited 0 after its startup line, and `/private/tmp/halanaerobium_hydrogeniformans_medium_sl_hp.strict.tsv` has 1 line, the header only.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is the DSMZ/MediaDive import for medium 1656.
- An exact `rg --no-ignore --hidden` search for `DSMZ_Medium1656`, `DSMZ_Medium1656.pdf`, and `mediadive.medium:1656` found only this normalized source, this generated output, and its index entries under `data/merge_yaml` and `data/normalized_yaml`; no same-source duplicate record was found in those trees.

## Evidence

- The DSMZ Medium 1656 PDF lists 70 g NaCl, 40 g Na2CO3, 6.30 g K2HPO4, 1.00 g yeast extract, 0.75 g Na2S x 9 H2O, 0.60 g L-cysteine, 10 ml basal medium stock solution, 10 ml trace mineral solution, and final pH 11.0.
- The DSMZ PDF defines the basal medium and trace mineral solutions separately; they are 10 ml stock additions, not full-strength top-level medium components.
- The DSMZ PDF also instructs preparing the medium without cysteine, Na2S, or Na2CO3, boiling and cooling under N2:CO2, adding Na2CO3, autoclaving, then adding cysteine and Na2S from sterile stocks.
- The generated record has impossible top-level concentrations such as NaCl 3500.980392 g/L, Na2CO3 2000 g/L, K2HPO4 315 g/L, yeast extract 50 g/L, and Na2S x 9 H2O 42.5 g/L; these are artifacts of MediaDive's solution graph and the importer flattening 10 ml stock or per-10-ml additions as formula concentrations.

## Completeness

- All external stock members are present only after flattening and therefore at the wrong concentration scale.
- The duplicated Na2S and L-cysteine top-level rows were collapsed with the distinct post-sterilization stock additions.
- NaCl, CaCl2 x 2 H2O, FeSO4 x 7 H2O, and Na2MoO4 x 2 H2O are summed across top-level and stock contexts instead of preserving solution membership.
- `Yeast extract` and `Na3-NTA x H2O` are ungrounded.

## Findings

- Major: Core top-level ingredients are scaled as if the final volume were 20 ml, producing impossible per-liter concentrations.
- Major: Basal medium stock and trace mineral stock ingredients are flattened at stock concentration.
- Major: Reducer additions from sterile Na2S and L-cysteine stocks are collapsed into the same top-level ingredients as the bulk pre-sterilization masses.
- Major: Duplicate-ingredient cleanup sums salts across unrelated solution contexts.
- Minor: `Na3-NTA x H2O` is ungrounded, and `NiSO4 x 6 H2O` is grounded to `CHEBI:53001`, nickel sulfate, rather than a hexahydrate-specific term.

## Recommended Edits

- Recurate DSMZ 1656 with the published 70 g / 40 g / 6.3 g top-level masses and explicit 10 ml basal and trace stock additions.
- Preserve the two post-autoclave stock additions for Na2S and L-cysteine rather than summing them with the bulk formula rows.
- Keep stock-solution contents nested or convert them using the actual 10 ml aliquots before flattening.
- Add or repair local grounding for `Na3-NTA x H2O` and nickel sulfate hexahydrate.

## Follow-up Checks

- After repair, verify that NaCl is no longer near 3500 g/L, Na2CO3 is no longer 2000 g/L, K2HPO4 is no longer 315 g/L, and no ingredient row has a `Merged 2 duplicates` note.

## Additional Notes

- None found.
