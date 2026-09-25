# YAML Record Review: THERMOANAEROBACTER (KoKo) MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_koko_medium.yaml`
- Started UTC: `2026-09-25T09:38:19Z`
- Finished UTC: `2026-09-25T09:39:31Z`
- Verdict: needs curation

## Target
Generated bacterial recipe `CultureMech:001848`, `thermoanaerobacter_koko_medium`, with medium term `mediadive.medium:710` and label `THERMOANAEROBACTER (KoKo) MEDIUM`.

It merges the MediaDive DSMZ 710 source `thermoanaerobacter_koko_medium` with KOMODO aliases `komodo.medium:710` and `komodo.medium:710_12299`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The branch is correctly grounded to DSMZ Medium 710, `THERMOANAEROBACTER (KoKo) MEDIUM`, and the two KOMODO aliases are legitimate DSMZ 710 source-equivalent records.

The TOGO import `TOGO:M2715` for the same DSMZ 710 PDF remains split into `data/merge_yaml/merged/thermoanaerobacter_koko_medium__f3bb6f3e.yaml`.

Most ingredient groundings match their strings. `MgSO4 x 6 H2O` is grounded only to generic `CHEBI:32599`; because DSMZ names the unusual hexahydrate explicitly, that row needs a manual grounding check during source normalization.

## Evidence
DSMZ Medium 710 and MediaDive medium 710 specify a main solution with tryptone, peptone, yeast extract, K2HPO4, NaH2PO4 x 2 H2O, NH4Cl, MgSO4 x 6 H2O, 1 ml Trace element solution SL-11, resazurin, CaCl2 x 2 H2O, NaHCO3, D-glucose, 1 ml Wolin's vitamin solution 10x, cysteine, sulfide, and water.

The generated record flattens SL-11 into top-level final ingredients at stock concentration: `Na2-EDTA x 2 H2O` at `5.2 G_PER_L`, `FeCl2 x 4 H2O` at `1.5 G_PER_L`, and the milligram-level trace salts as gram-per-liter rows.

The generated record also flattens Wolin's vitamin solution 10x into top-level rows, with stock recipe concentrations such as `0.02 G_PER_L` for `Biotin`, `0.1 G_PER_L` for `Pyridoxine hydrochloride`, and `0.001 G_PER_L` for `Vitamin B12`.

The MediaDive/KOMODO branch preserves the DSMZ preparation text, including late addition of calcium chloride, bicarbonate, glucose, vitamins, cysteine, and sulfide from sterile anoxic stocks.

## Completeness
The DSMZ MOPS supplementation note is preserved, and the KOMODO `komodo.medium:710_12299` source records the DSM 12299 D-glucose omission variant.

The generated hierarchy is still incomplete because the SL-11 and vitamin-stock preparation semantics have been collapsed into the final ingredient list.

## Findings
1. Needs curation: Trace element solution SL-11 was flattened into top-level final ingredients even though the base recipe adds only 1 ml/L of that stock.
2. Needs curation: Wolin's vitamin solution 10x was flattened into top-level final ingredients even though the base recipe adds only 1 ml/L of that stock.
3. Needs curation: TOGO M2715 remains an unmerged DSMZ 710 duplicate branch.
4. Minor issue: `MgSO4 x 6 H2O` is currently grounded to generic magnesium sulfate and should be checked against CHEBI's hexahydrate coverage.

## Recommended Edits
1. Normalize the MediaDive, KOMODO, and TOGO DSMZ 710 source records, not the generated merge YAML, so the main recipe retains explicit 1 ml/L additions of Trace element solution SL-11 and Wolin's vitamin solution 10x.
2. Preserve the calcium chloride, bicarbonate, glucose, vitamin, cysteine, and sulfide late-addition preparation semantics when regenerating from source YAML.
3. Model the DSM 12299 D-glucose omission as a strain-specific note or variant rather than as a source-equivalent duplicate only.
4. Merge `mediadive.medium:710`, `komodo.medium:710`, `komodo.medium:710_12299`, and `TOGO:M2715` by exact DSMZ 710 source identity after normalization.

## Follow-up Checks
After source edits and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:710`, `komodo.medium:710`, `komodo.medium:710_12299`, `TOGO:M2715`, and `DSMZ_Medium710.pdf` and confirm that DSMZ 710 regenerates as one canonical record.

## Additional Notes
Exact duplicate-source searches included ignored files. A first pass that searched exact `name: koko_medium` values was discarded for duplicate-source purposes because it also matched a separate TOGO M860 KoKo name family outside DSMZ 710.
