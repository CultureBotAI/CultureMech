# YAML Record Review: Anaerobacter Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerobacter_medium__c39de276.yaml
- Started UTC: 2026-09-21T11:53:15Z
- Finished UTC: 2026-09-21T11:54:45Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007678 |
| Source | TOGO:M1154 |
| Original source | JCM_M1085 |
| Generated path | data/merge_yaml/merged/anaerobacter_medium__c39de276.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1154_Anaerobacter_Medium.yaml |
| Merge fingerprint | c39de276b43d5ab0e7f1084ce288fee8005d0fc8d5459e538c117a5ef025df44 |
| Merge source | TOGO_M1154_Anaerobacter_Medium.yaml |

`data/merge_yaml/merged/anaerobacter_medium__c39de276.yaml` is a generated singleton merge from the TOGO/JCM M1154 normalized owner; any correction belongs in `data/normalized_yaml/bacterial/TOGO_M1154_Anaerobacter_Medium.yaml` or the TOGO importer.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobacter_medium__c39de276.yaml` under the cached Python 3.11 no-project environment. |
| Strict schema | Passed with `scripts/validate_strict.py data/merge_yaml/merged/anaerobacter_medium__c39de276.yaml --workers 1 --quiet`; the TSV contained 0 ERROR rows. |
| Reference validator | Passed with `linkml-reference-validator validate data ...`; no reference checks were emitted for this file. |
| Term validator | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no documented focused validator targets embedded `MediaRecipe.curation_history` inside one merge record. |

The project-level `just validate-schema`, `just validate-strict`, and `just validate-terms` routes were not usable for this target because project installation currently attempts to build `llvmlite==0.46.0` on Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The equivalent LinkML validators passed through an offline `uv run --no-project` invocation against `/usr/local/bin/python3.11`.

## Identity and Grounding

- The stable CultureMech ID, `TOGO:M1154` source term, JCM_M1085 provenance, and merge fingerprint identify a singleton TOGO import for JCM GRMD 1085, Anaerobacter Medium.
- A gitignore-independent search across `data`, `src`, `scripts`, `history`, `conf`, `reports`, `.claude`, `justfile`, and `CLAUDE.md` found exactly one current maintained owner for `CultureMech:007678`.
- The inspected TOGO M1154 JSON and JCM GRMD 1085 page agree on the source identity, the base mineral rows, the FeCl2 and trace-element Medium 187 stock references, the 8% bicarbonate, 20% sucrose, 5% sulfide, and 5% cysteine-HCl stock additions, and the two anaerobic preparation paragraphs.
- The simple-salt groundings for KH2PO4, NH4Cl, KCl, calcium chloride dihydrate, magnesium chloride hexahydrate, sodium bicarbonate solution, sodium sulfide nonahydrate solution, and dinitrogen/carbon dioxide gas are chemically plausible at the identifier level.

## Evidence

- The base gram-scale rows for yeast extract, CaCl2.2H2O, KH2PO4, NH4Cl, MgCl2.6H2O, and KCl match the JCM and TOGO sources numerically.
- JCM and TOGO both give `Resazurin` as `1.0 mg`, but the record stores `1 G_PER_L`; this is a 1000x unit error for a 1 L final volume.
- JCM and TOGO both give `Distilled water` as `1.0 L`, a final volume. The record converts that to `1 G_PER_L`, which makes water look like a one-gram-per-liter solute.
- JCM and TOGO give FeCl2 solution and trace element solution as `1.0 ml` additions from Medium 187, but the record stores both as empty `Unknown solution` entries with `1 G_PER_L`.
- JCM and TOGO give 8% NaHCO3, 20% sucrose, 5% Na2S.9H2O, and 5% L-cysteine.HCl.H2O solution amounts as milliliter additions, but the record stores their volumes as `18.3`, `10`, `6`, and `6 G_PER_L` on empty solution stubs.
- The JCM/TOGO comments provide pH 7.0, autoclaving under N2, post-cooling addition of sterile anaerobic stocks, an 80% N2/20% CO2 storage condition for filter-sterilized stocks, butyl-stopper vessel sealing, and final addition of reducing solutions. None of those procedural steps are present in the record.

## Completeness

- Consequentially incomplete: source preparation order, pH, gas atmosphere, stock sterilization, stock storage, and vessel sealing are absent.
- Consequentially incorrect: milligram, liter, and milliliter rows were all normalized into `G_PER_L`, even when they were final volumes or addition volumes.
- Consequentially incomplete: FeCl2 and trace-element stocks are cross-references to JCM Medium 187 but have no composition or resolvable structured reference.
- The absence of target organisms is acceptable here; the inspected TOGO and JCM medium records did not state strain-specific growth claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Resazurin is inflated from 1 mg per liter to `1 G_PER_L`. | JCM GRMD 1085 and TOGO M1154 both list Resazurin as `1.0 mg`; the normalized owner and generated merge store `value: '1'`, `unit: G_PER_L`. | Fix the TOGO unit conversion in `data/normalized_yaml/bacterial/TOGO_M1154_Anaerobacter_Medium.yaml` or, preferably, in the TOGO importer so mg per 1 L becomes `0.001 G_PER_L`. |
| Major | Distilled water is represented as a solute concentration. | JCM GRMD 1085 and TOGO M1154 list Distilled water as `1.0 L`; the record stores `1 G_PER_L`. | Remove final-volume water rows from TOGO normalized recipes or model them as final volume metadata if the schema supports that. |
| Major | Milliliter stock additions are flattened into gram-per-liter empty solutions. | The six source solution rows are 1.0 ml, 1.0 ml, 18.3 ml, 10.0 ml, 6.0 ml, and 6.0 ml additions; the record stores the same numerals with `G_PER_L` and no stock composition. | Parse TOGO/JCM solution rows as stock additions with volume units and resolve the Medium 187 stock references where possible. |
| Major | N2 and CO2 gas conditions are modeled as variable-concentration ingredients. | The source uses the gases in autoclaving, anaerobic stock storage, and culture-vessel dispensing instructions; it does not list gas masses as ingredients. | Move gas rows from `ingredients` into preparation atmosphere or stock storage context during TOGO normalization. |
| Major | The source pH and preparation instructions were not imported. | JCM and TOGO both state pH 7.0 and the anaerobic stock-addition sequence; the record has no `ph_value` and no `preparation_steps`. | Parse TOGO `comments` into `preparation_steps`, or curate the JCM GRMD 1085 instructions directly into the normalized owner. |

## Recommended Edits

1. Correct Resazurin to `0.001 G_PER_L` and stop converting the `Distilled water` final volume into an ingredient concentration.
2. Represent the FeCl2, trace-element, bicarbonate, sucrose, sulfide, and cysteine-HCl rows as milliliter stock additions rather than gram-per-liter empty solution stubs.
3. Resolve Medium 187 references for FeCl2 and trace-element solutions to structured stock records or leave explicit unresolved references with quality flags.
4. Add `ph_value: 7.0` and structured preparation steps for the JCM anaerobic workflow, including the N2 autoclave atmosphere, the 80% N2/20% CO2 filtered-stock storage condition, the butyl-rubber stopper sealing step, and the final anaerobic reducing-solution additions.
5. Regenerate `data/merge_yaml/merged` with `just merge-recipes` after the normalized owner or TOGO importer is corrected.

## Follow-up Checks

1. Run focused open-schema, strict, term, and reference validation on `data/normalized_yaml/bacterial/TOGO_M1154_Anaerobacter_Medium.yaml` and the regenerated `data/merge_yaml/merged/anaerobacter_medium__c39de276.yaml`.
2. Run `just verify-merges` and `just audit-merge-freshness --fail-on-drift` after regeneration.
3. Re-fetch TOGO M1154 via `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1154` and re-open JCM GRMD 1085 to verify the corrected units, stock volumes, gas contexts, and preparation steps.
4. Run the concentration plausibility report and confirm the existing `INDICATOR_UNIT_SLIP` finding for Resazurin no longer appears for `CultureMech:007678`.

## Additional Notes

- The bounded identity search used `rg --no-ignore --hidden`; ignored paths were included for the searched roots.
- The source page for TOGO public `/medium/M1154` is a SPA shell; the review used TOGO's `gmdb_medium_by_gmid` JSON API instead.
- The original JCM source page at GRMD 1085 was fetched directly during this review.
