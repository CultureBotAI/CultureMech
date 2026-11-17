# Continuous-cultivation CDM: variant integrity, hydrated reagents and fungal evidence

- Review: 20261028T081447Z-continuous-cultivation-cdm-batch060
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:42:29.524661Z
- Finished UTC: 2026-10-28T08:14:47.644484Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Five major findings concern stale variant collapse, supplied hydrate loss, trace-stock basis, preparation/culture context and fungal category; one minor finding concerns missing secondary links. Full primary publication and current ontology/taxonomy were inspected. Maintained paper citations and current merge safeguards are credited. Current MediaDB access and trace-stock final volume remain unresolved.

## Scope And Provenance

One complete generated target and its two maintained contributors;30 local concentration fields,38 quantity decisions,45 asserted ontology slots, five named and three scoped pooled historical reports, current owning writers and full six-page publication.

Selection: Batch060 item10 from Python-sorted paths uncovered by successful native validated lists;523 of6325 covered at selection.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007244 | data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml | generated | cdm_for_continuous_cultivation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007244 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007244 | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch060/record10/strict.tsv |
| validate-terms | passed | True | CultureMech:007244 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007244 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| check-mim-label-index | passed | True | CultureMech:007244 | MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9<br>Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350<br>uv run python scripts/check_mim_label_index.py |
| Current exact MediaDB accession and export access | unavailable | True | CultureMech:007244 | Both312/343 detail and text routes, source120 and versioned SQL export return502; full publication is available independently. |
| Manual embedded history and registry assessment | passed | False | CultureMech:007244 | All embedded events and exact registry/reciprocal links read. Existing October13 bibliography additions credited; no historical event was rewritten. |
| Full-corpus ID/product/merge gates | skipped | False | CultureMech:007244 | No scientific input/schema/generator changed. Corpus assign-ids-check, validate-products, verify-merges and audit-merge-freshness were not run; no focused substitute is claimed. |

## Scientific And Domain Assessments

### Continuous/batch accession, variant and fungal category

identity: concern. Targets: CultureMech:007244.

The selected generated record is unambiguously resolved, but its continuous MEDIADB343 identity carries batch glucose/ammonium values and a contradictory continuous-variant note. Both owners resolve; the primary is a fungal study.

The maintained child preserves the lower two concentrations; parent/child references resolve and the October13 citation is already present in both. Defined/liquid composition is consistent with the reported glucose medium. The subsequent maltose-feed phase is a separate condition, not the default glucose recipe. iModulonDB is not applicable: no gene, expression module or transcriptomic dataset is asserted.

### Every local amount and source stock/control quantity

quantity: concern. Targets: CultureMech:007244.

Six main-component molarities per owner agree with source mass-per-litre values at the supplied-form molecular masses. Two generated child fields retain parent values. Twelve local trace-component fields remain unsupported as final molarities because the primary stock denominator is unspecified.

[
  {
    "decision_id": "q01",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[0].concentration",
    "ingredient": "Ferrous sulfate",
    "existing": {
      "value": "0.02482",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5192,343,16397,0.02482)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "iron(2+) sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:75836",
    "source_stock_mass_g": "13.8",
    "source_snippet": "13.8 g FeSO,. 7H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q02",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[1].concentration",
    "ingredient": "Nickel chloride",
    "existing": {
      "value": "0.001052",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5188,343,13121,0.001052)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "nickel chloride hexahydrate",
    "verified_form_candidate": "CHEBI:53542",
    "source_stock_mass_g": "0.5",
    "source_snippet": "0.5 g",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q03",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[2].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "126.2",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5187,343,280,40.37)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "correct",
    "source_form": "glucose monohydrate",
    "verified_form_candidate": null,
    "source_mass_g_per_L": "8.0",
    "source_snippet": "8*0g glucose monohydrate",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "198.17",
    "calculation": "8.0 g/L *1000 /198.17 g/mol = 40.36937982540243225513448050 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "40.37",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q04",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[3].concentration",
    "ingredient": "Calcium chloride anhydrous",
    "existing": {
      "value": "0.6802",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5191,343,6656,0.6802)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "calcium chloride dihydrate",
    "verified_form_candidate": "CHEBI:86158",
    "source_mass_g_per_L": "0.1",
    "source_snippet": "0.1 g CaC1,.2H20",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "147.014",
    "calculation": "0.1 g/L *1000 /147.014 g/mol = 0.6802073271933285265348878338 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "0.6802",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q05",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[4].concentration",
    "ingredient": "Sodium chloride",
    "existing": {
      "value": "17.11",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5186,343,16384,17.11)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "sodium chloride",
    "verified_form_candidate": "CHEBI:26710",
    "source_mass_g_per_L": "1.0",
    "source_snippet": "1.0 g NaC1",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "58.443",
    "calculation": "1.0 g/L *1000 /58.443 g/mol = 17.11068904744794072857313964 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "17.11",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q06",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[5].concentration",
    "ingredient": "Cupric sulfate",
    "existing": {
      "value": "0.005006",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5195,343,16405,0.005006)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "copper(II) sulfate pentahydrate",
    "verified_form_candidate": "CHEBI:31440",
    "source_stock_mass_g": "2.5",
    "source_snippet": "2 5 g CuSO,. 5H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q07",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[6].concentration",
    "ingredient": "Zinc sulfate",
    "existing": {
      "value": "0.02487",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5189,343,16399,0.02487)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "zinc sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:32312",
    "source_stock_mass_g": "14.3",
    "source_snippet": "14.3 g ZnSO,. 7H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q08",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[7].concentration",
    "ingredient": "Magnesium sulfate",
    "existing": {
      "value": "4.057",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5193,343,16394,4.057)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "magnesium sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:31795",
    "source_mass_g_per_L": "1.0",
    "source_snippet": "MgSO,. 7H20",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "246.473",
    "calculation": "1.0 g/L *1000 /246.473 g/mol = 4.057239535364928410008398486 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "4.057",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q09",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[8].concentration",
    "ingredient": "Potassium dihydrogen phosphate",
    "existing": {
      "value": "11.02",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5190,343,16391,11.02)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "potassium dihydrogen phosphate",
    "verified_form_candidate": "CHEBI:63036",
    "source_mass_g_per_L": "1.5",
    "source_snippet": "1.5 g KH,PO,",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "136.084",
    "calculation": "1.5 g/L *1000 /136.084 g/mol = 11.02260368595867258458011228 mM; existing value is compared as a rounded nominal solute concentration. At the existing displayed precision, the source-derived value rounds to 11.02 mM; retain that nominal amount with the supplied-form caveat.",
    "proposed_value": "11.02",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q10",
    "path": "data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml",
    "field": "ingredients[9].concentration",
    "ingredient": "Ammonium sulfate",
    "existing": {
      "value": "55.24",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5194,343,16401,37.84)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "correct",
    "source_form": "ammonium sulfate",
    "verified_form_candidate": "CHEBI:62946",
    "source_mass_g_per_L": "5.0",
    "source_snippet": "5.0 g (NH,),SO,",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "132.141",
    "calculation": "5.0 g/L *1000 /132.141 g/mol = 37.83836962032979922961079453 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "37.84",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q11",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[0].concentration",
    "ingredient": "Ferrous sulfate",
    "existing": {
      "value": "0.02482",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(4437,312,16397,0.02482)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "iron(2+) sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:75836",
    "source_stock_mass_g": "13.8",
    "source_snippet": "13.8 g FeSO,. 7H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q12",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[1].concentration",
    "ingredient": "Nickel chloride",
    "existing": {
      "value": "0.001052",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(4438,312,13121,0.001052)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "nickel chloride hexahydrate",
    "verified_form_candidate": "CHEBI:53542",
    "source_stock_mass_g": "0.5",
    "source_snippet": "0.5 g",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q13",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[2].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "126.2",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(4439,312,280,126.2)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "glucose monohydrate",
    "verified_form_candidate": null,
    "source_mass_g_per_L": "25.0",
    "source_snippet": "25.0 g glucose",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "198.17",
    "calculation": "25.0 g/L *1000 /198.17 g/mol = 126.1543119543826007972952516 mM; existing value is compared as a rounded nominal solute concentration. At the existing displayed precision, the source-derived value rounds to 126.2 mM; retain that nominal amount with the supplied-form caveat.",
    "proposed_value": "126.2",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q14",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[3].concentration",
    "ingredient": "Calcium chloride anhydrous",
    "existing": {
      "value": "0.6802",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(4440,312,6656,0.6802)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "calcium chloride dihydrate",
    "verified_form_candidate": "CHEBI:86158",
    "source_mass_g_per_L": "0.1",
    "source_snippet": "0.1 g CaC1,.2H20",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "147.014",
    "calculation": "0.1 g/L *1000 /147.014 g/mol = 0.6802073271933285265348878338 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "0.6802",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q15",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[4].concentration",
    "ingredient": "Sodium chloride",
    "existing": {
      "value": "17.11",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(4441,312,16384,17.11)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "sodium chloride",
    "verified_form_candidate": "CHEBI:26710",
    "source_mass_g_per_L": "1.0",
    "source_snippet": "1.0 g NaC1",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "58.443",
    "calculation": "1.0 g/L *1000 /58.443 g/mol = 17.11068904744794072857313964 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "17.11",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q16",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[5].concentration",
    "ingredient": "Cupric sulfate",
    "existing": {
      "value": "0.005006",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(4442,312,16405,0.005006)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "copper(II) sulfate pentahydrate",
    "verified_form_candidate": "CHEBI:31440",
    "source_stock_mass_g": "2.5",
    "source_snippet": "2 5 g CuSO,. 5H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q17",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[6].concentration",
    "ingredient": "Zinc sulfate",
    "existing": {
      "value": "0.02487",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(4443,312,16399,0.02487)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "zinc sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:32312",
    "source_stock_mass_g": "14.3",
    "source_snippet": "14.3 g ZnSO,. 7H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q18",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[7].concentration",
    "ingredient": "Magnesium sulfate",
    "existing": {
      "value": "4.057",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(4444,312,16394,4.057)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "magnesium sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:31795",
    "source_mass_g_per_L": "1.0",
    "source_snippet": "MgSO,. 7H20",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "246.473",
    "calculation": "1.0 g/L *1000 /246.473 g/mol = 4.057239535364928410008398486 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "4.057",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q19",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[8].concentration",
    "ingredient": "Potassium dihydrogen phosphate",
    "existing": {
      "value": "11.02",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(4445,312,16391,11.02)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "potassium dihydrogen phosphate",
    "verified_form_candidate": "CHEBI:63036",
    "source_mass_g_per_L": "1.5",
    "source_snippet": "1.5 g KH,PO,",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "136.084",
    "calculation": "1.5 g/L *1000 /136.084 g/mol = 11.02260368595867258458011228 mM; existing value is compared as a rounded nominal solute concentration. At the existing displayed precision, the source-derived value rounds to 11.02 mM; retain that nominal amount with the supplied-form caveat.",
    "proposed_value": "11.02",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q20",
    "path": "data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml",
    "field": "ingredients[9].concentration",
    "ingredient": "Ammonium sulfate",
    "existing": {
      "value": "55.24",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(4446,312,16401,55.24)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "ammonium sulfate",
    "verified_form_candidate": "CHEBI:62946",
    "source_mass_g_per_L": "7.3",
    "source_snippet": "7-3 g (NH,),SO,",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "132.141",
    "calculation": "7.3 g/L *1000 /132.141 g/mol = 55.24401964568150687523176001 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "55.24",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q21",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[0].concentration",
    "ingredient": "Sodium chloride",
    "existing": {
      "value": "17.11",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5186,343,16384,17.11)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "sodium chloride",
    "verified_form_candidate": "CHEBI:26710",
    "source_mass_g_per_L": "1.0",
    "source_snippet": "1.0 g NaC1",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "58.443",
    "calculation": "1.0 g/L *1000 /58.443 g/mol = 17.11068904744794072857313964 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "17.11",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q22",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[1].concentration",
    "ingredient": "Glucose",
    "existing": {
      "value": "40.37",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5187,343,280,40.37)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "glucose monohydrate",
    "verified_form_candidate": null,
    "source_mass_g_per_L": "8.0",
    "source_snippet": "8*0g glucose monohydrate",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "198.17",
    "calculation": "8.0 g/L *1000 /198.17 g/mol = 40.36937982540243225513448050 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "40.37",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q23",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[2].concentration",
    "ingredient": "Nickel chloride",
    "existing": {
      "value": "0.001052",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5188,343,13121,0.001052)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "nickel chloride hexahydrate",
    "verified_form_candidate": "CHEBI:53542",
    "source_stock_mass_g": "0.5",
    "source_snippet": "0.5 g",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q24",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[3].concentration",
    "ingredient": "Zinc sulfate",
    "existing": {
      "value": "0.02487",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5189,343,16399,0.02487)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "zinc sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:32312",
    "source_stock_mass_g": "14.3",
    "source_snippet": "14.3 g ZnSO,. 7H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q25",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[4].concentration",
    "ingredient": "Potassium dihydrogen phosphate",
    "existing": {
      "value": "11.02",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5190,343,16391,11.02)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "potassium dihydrogen phosphate",
    "verified_form_candidate": "CHEBI:63036",
    "source_mass_g_per_L": "1.5",
    "source_snippet": "1.5 g KH,PO,",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "136.084",
    "calculation": "1.5 g/L *1000 /136.084 g/mol = 11.02260368595867258458011228 mM; existing value is compared as a rounded nominal solute concentration. At the existing displayed precision, the source-derived value rounds to 11.02 mM; retain that nominal amount with the supplied-form caveat.",
    "proposed_value": "11.02",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q26",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[5].concentration",
    "ingredient": "Calcium chloride anhydrous",
    "existing": {
      "value": "0.6802",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5191,343,6656,0.6802)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "calcium chloride dihydrate",
    "verified_form_candidate": "CHEBI:86158",
    "source_mass_g_per_L": "0.1",
    "source_snippet": "0.1 g CaC1,.2H20",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "147.014",
    "calculation": "0.1 g/L *1000 /147.014 g/mol = 0.6802073271933285265348878338 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "0.6802",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q27",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[6].concentration",
    "ingredient": "Ferrous sulfate",
    "existing": {
      "value": "0.02482",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5192,343,16397,0.02482)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "iron(2+) sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:75836",
    "source_stock_mass_g": "13.8",
    "source_snippet": "13.8 g FeSO,. 7H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q28",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[7].concentration",
    "ingredient": "Magnesium sulfate",
    "existing": {
      "value": "4.057",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5193,343,16394,4.057)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "magnesium sulfate heptahydrate",
    "verified_form_candidate": "CHEBI:31795",
    "source_mass_g_per_L": "1.0",
    "source_snippet": "MgSO,. 7H20",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "246.473",
    "calculation": "1.0 g/L *1000 /246.473 g/mol = 4.057239535364928410008398486 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "4.057",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q29",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[8].concentration",
    "ingredient": "Ammonium sulfate",
    "existing": {
      "value": "37.84",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "main medium",
    "historical_database_snippet": "(5194,343,16401,37.84)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "verified",
    "source_form": "ammonium sulfate",
    "verified_form_candidate": "CHEBI:62946",
    "source_mass_g_per_L": "5.0",
    "source_snippet": "5.0 g (NH,),SO,",
    "basis": "Primary explicitly uses per-litre medium composition; continuous recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula span adjacent lines in the paragraph, checked visually.",
    "molecular_mass_g_per_mol": "132.141",
    "calculation": "5.0 g/L *1000 /132.141 g/mol = 37.83836962032979922961079453 mM; existing value is compared as a rounded nominal solute concentration.",
    "proposed_value": "37.84",
    "proposed_unit": "MILLIMOLAR",
    "identity_caveat": "A matching molarity does not establish that the encoded supplied chemical form is correct. Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer remains unspecified."
  },
  {
    "decision_id": "q30",
    "path": "data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml",
    "field": "ingredients[9].concentration",
    "ingredient": "Cupric sulfate",
    "existing": {
      "value": "0.005006",
      "unit": "MILLIMOLAR"
    },
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, Organism and culture conditions, formulation paragraph",
    "source_stage": "trace-stock addition, final working contribution unresolved",
    "historical_database_snippet": "(5195,343,16405,0.005006)",
    "historical_evidence_status": "Derivative report only; original2015 SQL and October2026 HTML captures not recovered.",
    "action_taken": "none",
    "decision": "unsupported",
    "source_form": "copper(II) sulfate pentahydrate",
    "verified_form_candidate": "CHEBI:31440",
    "source_stock_mass_g": "2.5",
    "source_snippet": "2 5 g CuSO,. 5H,O",
    "basis": "Four hydrate masses are listed inside the trace-solution parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.",
    "calculation": "Not performed: unknown stock-volume denominator prevents independent confirmation of this final-medium mM. Historical database agrees with the local value but does not repair missing primary basis.",
    "proposed_value": null
  },
  {
    "decision_id": "q31",
    "path": null,
    "field": "source-only trace-stock composition",
    "ingredient": "iron(2+) sulfate heptahydrate",
    "decision": "evidence_only",
    "source_amount_g": "13.8",
    "source_snippet": "13.8 g FeSO,. 7H,O",
    "source_stage": "trace stock",
    "basis": "Stock final volume unspecified, so grams are not silently relabelled g/L.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 formulation paragraph, trace-stock parenthesis",
    "verified_form_candidate": "CHEBI:75836",
    "action_taken": "none"
  },
  {
    "decision_id": "q32",
    "path": null,
    "field": "source-only trace-stock composition",
    "ingredient": "nickel chloride hexahydrate",
    "decision": "evidence_only",
    "source_amount_g": "0.5",
    "source_snippet": "0.5 g",
    "source_stage": "trace stock",
    "basis": "Stock final volume unspecified, so grams are not silently relabelled g/L.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 formulation paragraph, trace-stock parenthesis",
    "verified_form_candidate": "CHEBI:53542",
    "action_taken": "none"
  },
  {
    "decision_id": "q33",
    "path": null,
    "field": "source-only trace-stock composition",
    "ingredient": "copper(II) sulfate pentahydrate",
    "decision": "evidence_only",
    "source_amount_g": "2.5",
    "source_snippet": "2 5 g CuSO,. 5H,O",
    "source_stage": "trace stock",
    "basis": "Stock final volume unspecified, so grams are not silently relabelled g/L.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 formulation paragraph, trace-stock parenthesis",
    "verified_form_candidate": "CHEBI:31440",
    "action_taken": "none"
  },
  {
    "decision_id": "q34",
    "path": null,
    "field": "source-only trace-stock composition",
    "ingredient": "zinc sulfate heptahydrate",
    "decision": "evidence_only",
    "source_amount_g": "14.3",
    "source_snippet": "14.3 g ZnSO,. 7H,O",
    "source_stage": "trace stock",
    "basis": "Stock final volume unspecified, so grams are not silently relabelled g/L.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 formulation paragraph, trace-stock parenthesis",
    "verified_form_candidate": "CHEBI:32312",
    "action_taken": "none"
  },
  {
    "decision_id": "q35",
    "path": null,
    "field": "source-only preparation/stock boundary",
    "ingredient": "Trace-stock receiving dose",
    "decision": "add",
    "source_value": "0.5",
    "source_unit": "ML_PER_L",
    "source_snippet": "0.5 ml trace",
    "source_stage": "preparation or culture pH control",
    "basis": "Main medium per-litre header supplies receiving basis, not the trace-stock formulation denominator.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, formulation and culture conditions",
    "action_taken": "none"
  },
  {
    "decision_id": "q36",
    "path": null,
    "field": "source-only preparation/stock boundary",
    "ingredient": "Sulfuric-acid titrant",
    "decision": "evidence_only",
    "source_value": "2",
    "source_unit": "MOLAR",
    "source_snippet": "2 M H,SO,",
    "source_stage": "preparation or culture pH control",
    "basis": "pH-control stock strength; no fixed added volume or final-medium sulfate contribution reported.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, formulation and culture conditions",
    "action_taken": "none"
  },
  {
    "decision_id": "q37",
    "path": null,
    "field": "source-only preparation/stock boundary",
    "ingredient": "Sodium-hydroxide titrant",
    "decision": "evidence_only",
    "source_value": "4",
    "source_unit": "MOLAR",
    "source_snippet": "4 M NaOH",
    "source_stage": "preparation or culture pH control",
    "basis": "pH-control stock strength; no fixed added volume or final-medium sodium contribution reported.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, formulation and culture conditions",
    "action_taken": "none"
  },
  {
    "decision_id": "q38",
    "path": null,
    "field": "source-only preparation/stock boundary",
    "ingredient": "Trace-stock final volume",
    "decision": "not_quantified",
    "source_value": null,
    "source_unit": null,
    "source_snippet": "metal solution (",
    "source_stage": "preparation or culture pH control",
    "basis": "No explicit stock final volume is printed in the full Methods. Do not infer1L from agreement with the historical molar values.",
    "reference": "https://doi.org/10.1099/13500872-141-10-2449",
    "locator": "p2450 left column, formulation and culture conditions",
    "action_taken": "none"
  }
]

### Chemical IDs, exact supplied hydrates and MIM coverage

grounding: concern. Targets: CultureMech:007244.

All10 asserted ChEBI IDs are current and labels match; current MIM answers agree with all supplied labels. Nevertheless six salt identities omit the paper’s hydrates, and generic glucose omits monohydrate context.

Verified hydrate candidates:Mg31795,Ca86158,Zn32312,Cu31440,Ni53542,Fe75836. These are source-form candidates, not applied edits or proof every historical imported database node used that supplied reagent. Generic glucose17234 remains a valid broad identity; record the monohydrate material without inventing a stereochemical/anomeric term. The historical database Mg compound row itself combines formulaMgSO4 with ChEBI31795; this inconsistency is preserved, not treated as proof the generic local32599 term is invalid. Existing secondary links cover glucose,NaCl,ZnSO4,MgSO4,ammonium sulfate only.

### Trace-stock stage, culture controls and unsupported filtration

completeness: concern. Targets: CultureMech:007244.

The primary separates trace-stock addition from its composition and reports culture controls absent from the YAML. Generic0.22µm filtration is not a source-supported sterilization method.

Source controls are pH6.0,30°C,1volume air per volume medium per minute and dissolved oxygen above60%; acid/base strengths are titrants, not fixed medium ingredients. Bioreactor nominal sizes15L batch and7L continuous do not specify working batch volumes. Fig5 gives a0.075h−1 dilution rate for the A1560 experiment; do not turn it into maximum growth rate or universal cultivation condition. Analysis buffers, protein-extraction reagents, sample storage/freezing, gels and assay temperatures are outside the growth formulation. No sterilization cycle, storage life or maltose feed concentration is invented.

### Existing paper citation and strain-specific scope

evidence: supported. Targets: CultureMech:007244.

Both maintained citations correctly distinguish bibliographic/taxonomic evidence from unverified concentration or native growth assertions; the generated target omits them. Full text now identifies batch studies of A1560,CF1.1,CF2.1 and the continuous experiment specifically with A1560.

A1560 originated from IFO4177; this is ancestry, not a demonstrated interchangeable strain or exact taxonomy node. CF1.1 andCF2.1 are distinct experimental strains. NCBITaxon5062 verifies the species parent, as the existing references explicitly say. Historical database growth links for all three strains on343 cannot be promoted to full-text support for all three continuous experiments. Table1 measures alpha-amylase quantities/productivity/residence, not organism growth rates. No new native organism or growth assertion is made.

### Current merger/importer, historical evidence and append-only history

provenance: concern. Targets: CultureMech:007244.

Current exact-formulation code rejects this parent/child pair; the old generated collapse is stale. The importer still supplies generic preparation and a bacterial name-based default. Existing paper citations and their scoped limits are credited.

All five named historical reports and complete relevant objects from three pooled reports were read. October9 derivative SQL/live comparisons agree with each owner’s numbers; their raw hashes/times are not newly authenticated. The September review predates October13 bibliography and current merge safeguards. Mazumdar2014 is the MediaDB database-paper attribution, not evidence for this formulation; preserve the original import event and distinguish the already-added Mørkeberg1995 primary citation. Current source notes point at references_cache files absent in the owned checkout after ignored-inclusive filename/exact-path checks; freshly retrieved PubMed/PDF evidence can support a future append-only access update. Missing local cache is not a broken PMID or proof the old capture never existed.

## Findings

### F1: Generated continuous identity retains the batch formulation

major / open / confirmed; issue key: cm007244-generated-concentration-variant-collapse.

Target glucose126.2 and ammonium55.24mM are the parent values, while the child and source continuous formulation support40.37 and37.84mM. Generated output also drops both maintained primary-paper references. Current exact-formulation merger rejects this pair; regenerate separate variants after maintained source-form review.

### F2: Imported identities omit supplied hydrate forms

major / open / confirmed; issue key: cm007244-supplied-hydrate-provenance-loss.

The primary specifies Mg/Ca/Fe/Zn/Cu/Ni hydrates and glucose monohydrate, while local descriptors use anhydrous/generic identities. Matching source-derived nominal molarity does not preserve the supplied reagent identity. Reconcile exact source forms without swapping arbitrary broader/specific identifiers or recalculating molarity using anhydrous mass.

### F3: Trace-stock boundary and dilution basis are missing

major / open / confirmed; issue key: cm007244-trace-stock-stage-basis.

Four local final trace molarities correspond to source stock ingredients, but no stock descriptor or0.5mL/L receiving dose is represented. The paper supplies stock masses without explicit stock final volume; historical database numbers cannot independently authenticate that missing denominator.

### F4: Culture context is missing and filtration is unsupported

major / open / confirmed; issue key: cm007244-culture-context-and-template-preparation.

Primary pH/temperature/aeration context is omitted, while all three records assert a generic0.22µm filtration protocol not supported by the inspected full paper. Current importer hard-codes that step. Preserve culture-specific controls and distinguish titration from initial formulation.

### F5: Fungal study records are filed as bacterial

major / open / confirmed; issue key: cm007244-fungal-category-mismatch.

Both owners and generated target carry bacterial classification despite the primary Aspergillus oryzae study and verified fungal taxonomy. Current importer relies on name keywords and defaults this medium name to bacterial.

### F6: Five current secondary ingredient links are missing

minor / open / confirmed; issue key: cm007244-secondary-linkage-gaps.

Ferrous sulfate,nickel chloride,calcium chloride,cupric sulfate and potassium dihydrogen phosphate lack secondary links despite primary IDs and current index answers. Resolve supplied-form scope first, then populate through the maintained resolver.

## Recommended Actions And Acceptance Checks

### A1

Reconcile the maintained batch/continuous source formulations and supplied hydrates with the primary, preserving exact source amount, stock stage and claim-level evidence. Recover the trace-stock final-volume basis before certifying its final molarities.

- Join all30 existing concentration fields to the38 scoped decisions; preserve the two variant-specific carbon/nitrogen quantities.
- Check six hydrate identifiers through current ontology/MIM tools; leave glucose stereochemistry unresolved unless independently supported.
- Preserve the stock mass parenthesis and receiving dose separately; no1L stock denominator inferred from rounded database numbers.
- Run the four native per-owner checks and just check-mim-label-index; append actual curation history without rewriting earlier events.

### A2

Source the culture context and replace unsupported generic preparation with bounded evidence-bearing text; maintain the distinction between formulation, titrant strength, continuous dilution rate and assay methods.

- Every culture condition cites p2450/Fig5 with strain and experiment scope.
- No assay/extraction reagent, sample-storage temperature, inferred sterilization cycle or unreported maltose strength enters the medium.
- Review the importer template path so a later import cannot silently reinstate unsupported filtration.

### A3

Correct the maintained fungal category and distinguish existing primary citation from database-import attribution; preserve study strain boundaries and update access notes append-only.

- Preserve permanent IDs and repair all path references if category relocation is used.
- NCBITaxon5062 remains explicitly a species parent; continuous A1560 evidence is not copied to CF1.1/CF2.1.
- Do not recast alpha-amylase productivity or residence time as organism growth metrics.

### A4

Add missing secondary links only after supplied reagent scope is reconciled.

- Resolve exact chosen labels with the packaged MIM index; compare primary/secondary terms and source form.
- Recompute linkage denominators without treating coverage as scientific accuracy.

### A5

Regenerate distinct batch and continuous outputs through the current conservative pipeline and retain both existing primary-paper references.

- Current exact-formulation guard continues to reject collapsing these variants.
- Generated continuous output preserves its own glucose/ammonium values, fungal category, paper evidence and preparation context.
- Run just verify-merges and just audit-merge-freshness after separately authorized regeneration; inspect the exact target and owners again.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml; entire record | supports | Complete record read: all ingredients, concentration fields, identifiers, preparation, history, relationship and references. |
| batch-owner | data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml; entire record | supports | Complete record read: all ingredients, concentration fields, identifiers, preparation, history, relationship and references. |
| continuous-owner | data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml; entire record | supports | Complete record read: all ingredients, concentration fields, identifiers, preparation, history, relationship and references. |
| diagnostics | REVIEW_WORK/batch060/record10/diagnostics.json; entire declared file or explicitly scoped section | supports | Three complete records:365 scalar leaves,30 concentration fields,45 asserted ontology slots, all current MIM responses, exact registry routes, in-memory writer/merge probes and bounded ignored-inclusive path search. |
| scalar-census | REVIEW_WORK/batch060/record10/scalar-census.json; entire declared file or explicitly scoped section | supports | Lossless scalar census of the three complete records; a navigation aid, not source verification. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; entire declared file or explicitly scoped section | supports | Pinned MIM index: all24 exact query-label rows, including rejected duplicates, were read alongside maintained resolution decisions. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; entire declared file or explicitly scoped section | supports | Pinned source commit/hash/row contract verified through maintained runtime and once-only integrity recipe. |
| importer | src/culturemech/import/mediadb_importer.py; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| merge-formulation | src/culturemech/merge/formulation.py; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| merge-writer | src/culturemech/merge/merger.py; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| profile | docs/record-review-profile.md; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| rules | .claude/skills/review-recipes/reference/validation-rules.md; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| concentration-contract | .claude/skills/review-ingredient-concentrations/references/evidence-contract.md; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| project-recipes | project.justfile; entire declared file or explicitly scoped section | supports | Current owning implementation or native contract; relevant complete functions/rubric read. No historic execution is inferred from current code. |
| historical-report-1 | reports/archive/media_variant_defined_strength_concentration_review.md; entire declared file or explicitly scoped section | supports | Complete historical report read; prior observations do not authenticate new source access or close structured findings. |
| historical-report-2 | reports/yaml_record_review/20260922T063301Z-CDM_for_Continuous_Cultivation.md; entire declared file or explicitly scoped section | supports | Complete historical report read; prior observations do not authenticate new source access or close structured findings. |
| historical-report-3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cdm_for_continuous_cultivation.md; entire declared file or explicitly scoped section | supports | Complete historical report read; prior observations do not authenticate new source access or close structured findings. |
| historical-report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cdm_for_batch_cultivation.md; entire declared file or explicitly scoped section | supports | Complete historical report read; prior observations do not authenticate new source access or close structured findings. |
| historical-report-5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CDM_for_Continuous_Cultivation.md; entire declared file or explicitly scoped section | supports | Complete historical report read; prior observations do not authenticate new source access or close structured findings. |
| historical-pooled-1 | reports/ingredient_concentration_curation/20261009-mediadb-exceptions/cohort-assessment.json; $.records where source_term in MEDIADB:312,MEDIADB:343; enclosing source and limits | supports | Only complete MEDIADB312 and343 objects plus enclosing source/scope/limits assessed; unrelated cohort claims excluded. Raw historical SQL/HTML captures are not available in this checkout. |
| historical-pooled-2 | reports/ingredient_concentration_curation/20261009-mediadb-exceptions/remaining-live-comparison.json; $.records where source_term in MEDIADB:312,MEDIADB:343; enclosing source and limits | supports | Only complete MEDIADB312 and343 objects plus enclosing source/scope/limits assessed; unrelated cohort claims excluded. Raw historical SQL/HTML captures are not available in this checkout. |
| historical-pooled-3 | reports/ingredient_concentration_curation/20261009-mediadb-exceptions/remaining-source-dispositions.json; $.records where source_term in MEDIADB:312,MEDIADB:343; enclosing source and limits | supports | Only complete MEDIADB312 and343 objects plus enclosing source/scope/limits assessed; unrelated cohort claims excluded. Raw historical SQL/HTML captures are not available in this checkout. |
| historical-selection | REVIEW_WORK/batch060/record10/historical-selection.json; entire declared file or explicitly scoped section | supports | Lossless selected historical objects with source hashes and exact snippets; derivative context, not newly recovered original source bytes. |
| inspection | REVIEW_WORK/batch060/record10/inspection-addendum-historical/inspect.json; entire declared file or explicitly scoped section | supports | Native additive context inspection retains all41 original inputs and adds three pooled historical reports,44 total. |
| inspection-delta | REVIEW_WORK/batch060/record10/inspection-addendum-historical/delta.json; entire declared file or explicitly scoped section | supports | Original41 input bytes unchanged; only three context inputs added. |
| paper | https://doi.org/10.1099/13500872-141-10-2449; pp2449–2454; especially p2450 left column Organism and culture conditions, p2452 Continuous culture and p2453 Fig5 | supports | Mørkeberg R, Carlsen M, Nielsen J (1995), Microbiology141:2449–2454. All six PDF pages read visually and textually. Methods distinguish batch/continuous formulations, supplied hydrates and trace-stock addition; results scope continuous experiment to A1560. |
| paper-text | REVIEW_WORK/batch060/record10/sources/paper-visible.txt; entire declared file or explicitly scoped section | supports | Text extraction checked against all six rendered pages. OCR punctuation/formula errors are retained in quoted text; chemically normalized transcriptions are separately identified. |
| paper-extraction | REVIEW_WORK/batch060/record10/sources/paper-extraction.json; entire declared file or explicitly scoped section | supports | Actual extraction/render commands and all six page-image hashes. Publisher response is a PDF; the CiteSeer lead returned HTML rather than the article. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=7582005&amp;retmode=xml; PubmedArticleSet/PubmedArticle | supports | Complete PubMed record confirms PMID7582005, DOI, authors, title/year/pages and exact existing abstract excerpts. No correction/retraction item appears in this inspected metadata; this is a bounded metadata check. |
| crossref | https://api.crossref.org/works/10.1099%2F13500872-141-10-2449; $.message | supports | Publisher/DOI/title/authors/year/pages match; empty relation metadata is not a comprehensive retraction audit. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5062&amp;retmode=xml; TaxaSet/Taxon[TaxId=5062] | supports | NCBITaxon5062 is Aspergillus oryzae at species rank in Fungi. This verifies the existing species parent; no exact A1560/CF1.1/CF2.1 strain node is asserted. |
| glucose-mass | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/glucose%20monohydrate/property/MolecularFormula,MolecularWeight/JSON; $.PropertyTable.Properties[0] | supports | NIH PubChem name-query property response gives formula C6H14O7 and molecular mass198.17. Used only for the mass conversion; no stereochemical/anomeric grounding is inferred from the query. |
| glucose-id-search | https://www.ebi.ac.uk/ols4/api/search?q=glucose%20monohydrate&amp;ontology=chebi&amp;exact=true; $.response | unknown | Exact glucose-monohydrate ChEBI query returned no documents. This bounded query and MIM miss do not establish ontology-wide absence; exact hydrate identity remains unresolved. |
| chebi-17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0] | supports | Exact current term CHEBI:17234 = glucose; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-23414 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23414; $._embedded.terms[0] | supports | Exact current term CHEBI:23414 = copper(II) sulfate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0] | supports | Exact current term CHEBI:26710 = sodium chloride; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; $._embedded.terms[0] | supports | Exact current term CHEBI:31440 = copper(II) sulfate pentahydrate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0] | supports | Exact current term CHEBI:31795 = magnesium sulfate heptahydrate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; $._embedded.terms[0] | supports | Exact current term CHEBI:32312 = zinc sulfate heptahydrate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0] | supports | Exact current term CHEBI:32599 = magnesium sulfate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-3312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312; $._embedded.terms[0] | supports | Exact current term CHEBI:3312 = calcium dichloride; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0] | supports | Exact current term CHEBI:34887 = nickel dichloride; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-35176 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35176; $._embedded.terms[0] | supports | Exact current term CHEBI:35176 = zinc sulfate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; $._embedded.terms[0] | supports | Exact current term CHEBI:53542 = nickel chloride hexahydrate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; $._embedded.terms[0] | supports | Exact current term CHEBI:62946 = ammonium sulfate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0] | supports | Exact current term CHEBI:63036 = potassium dihydrogen phosphate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-75832 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832; $._embedded.terms[0] | supports | Exact current term CHEBI:75832 = iron(2+) sulfate (anhydrous); definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0] | supports | Exact current term CHEBI:75836 = iron(2+) sulfate heptahydrate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| chebi-86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0] | supports | Exact current term CHEBI:86158 = calcium chloride dihydrate; definition, synonyms, charge, empirical formula and mass read. This supports chemical identity/mass only. |
| mediadb-media-312-html | https://mediadb.systemsbiology.net/defined_media/media/312/; HTTP502 retained response | unknown | Exact named current source/export request returned502. Historical accession/formulation/version metadata are contextual; this response does not authenticate the old raw capture. |
| mediadb-media_text-312-html | https://mediadb.systemsbiology.net/defined_media/media_text/312/; HTTP502 retained response | unknown | Exact named current source/export request returned502. Historical accession/formulation/version metadata are contextual; this response does not authenticate the old raw capture. |
| mediadb-media-343-html | https://mediadb.systemsbiology.net/defined_media/media/343/; HTTP502 retained response | unknown | Exact named current source/export request returned502. Historical accession/formulation/version metadata are contextual; this response does not authenticate the old raw capture. |
| mediadb-media_text-343-html | https://mediadb.systemsbiology.net/defined_media/media_text/343/; HTTP502 retained response | unknown | Exact named current source/export request returned502. Historical accession/formulation/version metadata are contextual; this response does not authenticate the old raw capture. |
| mediadb-source120-html | https://mediadb.systemsbiology.net/defined_media/sources/120/; HTTP502 retained response | unknown | Exact named current source/export request returned502. Historical accession/formulation/version metadata are contextual; this response does not authenticate the old raw capture. |
| mediadb-export-sql-gz | https://mediadb.systemsbiology.net/static/defined_media/downloads/media_database.07Oct2015.sql.gz; HTTP502 retained response | unknown | Exact named current source/export request returned502. Historical accession/formulation/version metadata are contextual; this response does not authenticate the old raw capture. |
| publisher-html | https://www.microbiologyresearch.org/content/journal/micro/10.1099/13500872-141-10-2449; response status/content type/redirect preserved | unknown | Preserved access lead: publisher HTML403; CiteSeer redirected to an archived HTML response. The separately retrieved publisher PDF supplies full text. |
| publisher-full-html | https://www.microbiologyresearch.org/deliver/fulltext/micro/141/10/mic-141-10-2449.html?itemId=/content/journal/micro/10.1099/13500872-141-10-2449&amp;mimeType=html&amp;fmt=ahah; response status/content type/redirect preserved | unknown | Preserved access lead: publisher HTML403; CiteSeer redirected to an archived HTML response. The separately retrieved publisher PDF supplies full text. |
| paper-citeseer-pdf | https://citeseerx.ist.psu.edu/document?doi=7e5826102180b2b72bb9323a3783cd1fc08a273d&amp;repid=rep1&amp;type=pdf; response status/content type/redirect preserved | unknown | Preserved access lead: publisher HTML403; CiteSeer redirected to an archived HTML response. The separately retrieved publisher PDF supplies full text. |
| validate-schema | REVIEW_WORK/batch060/record10/validate-schema-result.json; entire declared file or explicitly scoped section | supports | Original once-only command, real UTC times and complete streams read. Structural/label checks do not certify source support. |
| validate-strict | REVIEW_WORK/batch060/record10/validate-strict-result.json; entire declared file or explicitly scoped section | supports | Original once-only command, real UTC times and complete streams read. Structural/label checks do not certify source support. |
| validate-terms | REVIEW_WORK/batch060/record10/validate-terms-result.json; entire declared file or explicitly scoped section | supports | Original once-only command, real UTC times and complete streams read. Structural/label checks do not certify source support. |
| validate-references | REVIEW_WORK/batch060/record10/validate-references-result.json; entire declared file or explicitly scoped section | supports | Original once-only command, real UTC times and complete streams read. Structural/label checks do not certify source support. |
| check-mim-label-index | REVIEW_WORK/batch060/record10/check-mim-label-index-result.json; entire declared file or explicitly scoped section | supports | Original once-only command, real UTC times and complete streams read. Structural/label checks do not certify source support. |
| quantity-inventory | REVIEW_WORK/batch060/record10/quantity-inventory.json; entire declared file or explicitly scoped section | supports | 38 decisions account for all30 local concentration fields, four source stock masses, receiving dose, two titrant strengths and unknown stock final volume. Actual inspected primary snippets and separate arithmetic retained. |

## Limits And Additional Notes

- All current exact MediaDB endpoints and versioned export return502. Historical SQL/HTML snippets were read as derivative reports; old raw digests, retrieval times and accession contents are not newly authenticated.
- The primary full text gives the trace-stock dose and four hydrate masses, but not an explicit stock final-volume denominator. Their final trace molarities remain unresolved; no density or final-volume assumption is introduced.
- Exact glucose-monohydrate ontology identity and strain-level taxonomy nodes remain unresolved. Molecular formula/mass supports arithmetic only; species5062 does not certify exact strain identity or interchangeable ancestry.
- Four canonical checks apply to the target; owners/context were read and the extra MIM integrity check passed. Full-corpus gates, experiments and scientific record changes were not performed.
- Existing references correctly marked their earlier abstract-only scope. New full-text access can support a future appended clarification; old history/cache existence is not rewritten or inferred.
- No previous structured finding is closed. Historical recommendations are reassessed against current owners and merge safeguards.
- Current primary and secondary labels resolve, but valid identifiers and rounded molarity do not establish the correct supplied hydrate or experimental scope.
- Original native inspection and diagnostics are preserved; the additive context inspection retained every original input hash.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T081447Z-continuous-cultivation-cdm-batch060
kind: record
repository: CultureBotAI/CultureMech
title: 'Continuous-cultivation CDM: variant integrity, hydrated reagents and fungal
  evidence'
started_at: '2026-10-28T07:42:29.524661Z'
finished_at: '2026-10-28T08:14:47.644484Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the scientific inputs; independent
    source-grounded review without experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Five major findings concern stale variant collapse, supplied hydrate loss,
  trace-stock basis, preparation/culture context and fungal category; one minor finding
  concerns missing secondary links. Full primary publication and current ontology/taxonomy
  were inspected. Maintained paper citations and current merge safeguards are credited.
  Current MediaDB access and trace-stock final volume remain unresolved.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
    sha256: b2e1fa518763083352439096cbf6589f36b4fee6d6e2a936080adbbdcfaf3adf
    role: target
  - path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    sha256: 0ae6d50bad2f839cb29f09828138f1316a9693e39a0768455ba2368268d12666
    role: context
  - path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    sha256: f4fa2c28574d0d290629acd7ce19cd2be36eaaf4173a1ae5af8b16a093f3a5e3
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/archive/media_variant_defined_strength_concentration_review.md
    sha256: 510c137872b3e747657ca4130c5be801084a644f165a7ac0ec43573f703377aa
    role: context
  - path: reports/ingredient_concentration_curation/20261009-mediadb-exceptions/cohort-assessment.json
    sha256: bfd6b6a15fe29cd8c3024c568952407ba92ccd27576a1603cb80c3ef4284b78d
    role: context
  - path: reports/ingredient_concentration_curation/20261009-mediadb-exceptions/remaining-live-comparison.json
    sha256: 378f054ab156db20b86074131b3a0254061726461814c8de23d035a3934907aa
    role: context
  - path: reports/ingredient_concentration_curation/20261009-mediadb-exceptions/remaining-source-dispositions.json
    sha256: 329c67710bbd12e6ac94d404dff1e01b1c3e653e757f4ba006359e2bf81417b1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CDM_for_Continuous_Cultivation.md
    sha256: 9bdce301d1a625e5dacf7a170fa828040d9b8b32ff956dcc47f80e37432a6017
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cdm_for_batch_cultivation.md
    sha256: 9e473462d6683b5b3ed1b6423430999c8d49df316836846b0434d8c512a3beef
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cdm_for_continuous_cultivation.md
    sha256: 6eb2d8fa651a203872ef90324bf5e0c1ce0e406e0f165c056e0597c474817422
    role: context
  - path: reports/yaml_record_review/20260922T063301Z-CDM_for_Continuous_Cultivation.md
    sha256: 5411423ed246fef14e20860ceef1d9e76fa663e7cf6319822fdcff072ee0c664
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
    role: context
  - path: src/culturemech/convert/mediadb_raw_yaml.py
    sha256: 2c8a64083ec095130cbf1cc87e2ba18a63a9437ca9772784d0932d12d42cab81
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/mediadb_fetcher.py
    sha256: 25e7d4bdb93551a01b7f54536de8884e7a5342453ffedc69bf45f91dbada1b11
    role: context
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One complete generated target and its two maintained contributors;30
    local concentration fields,38 quantity decisions,45 asserted ontology slots, five
    named and three scoped pooled historical reports, current owning writers and full
    six-page publication.
  selection: Batch060 item10 from Python-sorted paths uncovered by successful native
    validated lists;523 of6325 covered at selection.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007244
  exclusions:
  - target: Other recipes and unrelated pooled-report records
    reason: Only the exact selected target and required contributor context are assessed.
  - target: Assay/extraction protocols and new native growth assertions
    reason: Culture-medium review does not transfer analytical reagents or certify
      growth on unreviewed variants.
targets:
- target_id: CultureMech:007244
  path: data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
  label: cdm_for_continuous_cultivation
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:007244
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
    --workers 1 --out REVIEW_WORK/batch060/record10/strict.tsv
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:007244
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch060/record10/strict.tsv"
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:007244
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:007244
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  evidence_ids:
  - validate-references
- check_id: check-mim-label-index
  name: check-mim-label-index
  command: just check-mim-label-index
  exit_code: 0
  status: passed
  required: true
  target_ids:
  - CultureMech:007244
  summary: 'MIM label index OK: 9,077 rows, 8,733 labels, commit 6643131b0f12ab40b66f98135245fca04027e0e9

    Decisions: ambiguous=23, hydrate_conflict=12, mapped=8,347, undecided=1, unmapped=350

    uv run python scripts/check_mim_label_index.py'
  evidence_ids:
  - check-mim-label-index
- check_id: current-mediadb
  name: Current exact MediaDB accession and export access
  required: true
  status: unavailable
  target_ids:
  - CultureMech:007244
  summary: Both312/343 detail and text routes, source120 and versioned SQL export
    return502; full publication is available independently.
  evidence_ids:
  - mediadb-media-343-html
  - mediadb-media_text-343-html
  - mediadb-export-sql-gz
- check_id: embedded-history
  name: Manual embedded history and registry assessment
  required: false
  status: passed
  target_ids:
  - CultureMech:007244
  summary: All embedded events and exact registry/reciprocal links read. Existing
    October13 bibliography additions credited; no historical event was rewritten.
  evidence_ids:
  - target
  - batch-owner
  - continuous-owner
  - diagnostics
- check_id: corpus-gates
  name: Full-corpus ID/product/merge gates
  required: false
  status: skipped
  target_ids:
  - CultureMech:007244
  summary: No scientific input/schema/generator changed. Corpus assign-ids-check,
    validate-products, verify-merges and audit-merge-freshness were not run; no focused
    substitute is claimed.
  evidence_ids:
  - project-recipes
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
  locator: entire record
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: 'Complete record read: all ingredients, concentration fields, identifiers,
    preparation, history, relationship and references.'
  snapshot_sha256: b2e1fa518763083352439096cbf6589f36b4fee6d6e2a936080adbbdcfaf3adf
- evidence_id: batch-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
  locator: entire record
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: 'Complete record read: all ingredients, concentration fields, identifiers,
    preparation, history, relationship and references.'
  snapshot_sha256: 0ae6d50bad2f839cb29f09828138f1316a9693e39a0768455ba2368268d12666
- evidence_id: continuous-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
  locator: entire record
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: 'Complete record read: all ingredients, concentration fields, identifiers,
    preparation, history, relationship and references.'
  snapshot_sha256: f4fa2c28574d0d290629acd7ce19cd2be36eaaf4173a1ae5af8b16a093f3a5e3
- evidence_id: diagnostics
  kind: validation
  reference: REVIEW_WORK/batch060/record10/diagnostics.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Three complete records:365 scalar leaves,30 concentration fields,45 asserted
    ontology slots, all current MIM responses, exact registry routes, in-memory writer/merge
    probes and bounded ignored-inclusive path search.
  snapshot_sha256: 66586f28d24410d242ec29302ef567216d7b9659bbabd37839c0d22ea55bbfbb
- evidence_id: scalar-census
  kind: validation
  reference: REVIEW_WORK/batch060/record10/scalar-census.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Lossless scalar census of the three complete records; a navigation aid,
    not source verification.
  snapshot_sha256: af518834848695677bf541aab9e0380df22af41aafd70e6467cc936029a92cc6
- evidence_id: mim-index
  kind: authority
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: 'Pinned MIM index: all24 exact query-label rows, including rejected duplicates,
    were read alongside maintained resolution decisions.'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-metadata
  kind: authority
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Pinned source commit/hash/row contract verified through maintained runtime
    and once-only integrity recipe.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: importer
  kind: authority
  reference: src/culturemech/import/mediadb_importer.py
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
- evidence_id: merge-formulation
  kind: authority
  reference: src/culturemech/merge/formulation.py
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: merge-writer
  kind: authority
  reference: src/culturemech/merge/merger.py
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
- evidence_id: rules
  kind: authority
  reference: .claude/skills/review-recipes/reference/validation-rules.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
- evidence_id: concentration-contract
  kind: authority
  reference: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
- evidence_id: project-recipes
  kind: authority
  reference: project.justfile
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Current owning implementation or native contract; relevant complete functions/rubric
    read. No historic execution is inferred from current code.
  snapshot_sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
- evidence_id: historical-report-1
  kind: prior_review
  reference: reports/archive/media_variant_defined_strength_concentration_review.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Complete historical report read; prior observations do not authenticate
    new source access or close structured findings.
  snapshot_sha256: 510c137872b3e747657ca4130c5be801084a644f165a7ac0ec43573f703377aa
- evidence_id: historical-report-2
  kind: prior_review
  reference: reports/yaml_record_review/20260922T063301Z-CDM_for_Continuous_Cultivation.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Complete historical report read; prior observations do not authenticate
    new source access or close structured findings.
  snapshot_sha256: 5411423ed246fef14e20860ceef1d9e76fa663e7cf6319822fdcff072ee0c664
- evidence_id: historical-report-3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cdm_for_continuous_cultivation.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Complete historical report read; prior observations do not authenticate
    new source access or close structured findings.
  snapshot_sha256: 6eb2d8fa651a203872ef90324bf5e0c1ce0e406e0f165c056e0597c474817422
- evidence_id: historical-report-4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cdm_for_batch_cultivation.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Complete historical report read; prior observations do not authenticate
    new source access or close structured findings.
  snapshot_sha256: 9e473462d6683b5b3ed1b6423430999c8d49df316836846b0434d8c512a3beef
- evidence_id: historical-report-5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CDM_for_Continuous_Cultivation.md
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Complete historical report read; prior observations do not authenticate
    new source access or close structured findings.
  snapshot_sha256: 9bdce301d1a625e5dacf7a170fa828040d9b8b32ff956dcc47f80e37432a6017
- evidence_id: historical-pooled-1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261009-mediadb-exceptions/cohort-assessment.json
  locator: $.records where source_term in MEDIADB:312,MEDIADB:343; enclosing source
    and limits
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Only complete MEDIADB312 and343 objects plus enclosing source/scope/limits
    assessed; unrelated cohort claims excluded. Raw historical SQL/HTML captures are
    not available in this checkout.
  snapshot_sha256: bfd6b6a15fe29cd8c3024c568952407ba92ccd27576a1603cb80c3ef4284b78d
- evidence_id: historical-pooled-2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261009-mediadb-exceptions/remaining-live-comparison.json
  locator: $.records where source_term in MEDIADB:312,MEDIADB:343; enclosing source
    and limits
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Only complete MEDIADB312 and343 objects plus enclosing source/scope/limits
    assessed; unrelated cohort claims excluded. Raw historical SQL/HTML captures are
    not available in this checkout.
  snapshot_sha256: 378f054ab156db20b86074131b3a0254061726461814c8de23d035a3934907aa
- evidence_id: historical-pooled-3
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261009-mediadb-exceptions/remaining-source-dispositions.json
  locator: $.records where source_term in MEDIADB:312,MEDIADB:343; enclosing source
    and limits
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Only complete MEDIADB312 and343 objects plus enclosing source/scope/limits
    assessed; unrelated cohort claims excluded. Raw historical SQL/HTML captures are
    not available in this checkout.
  snapshot_sha256: 329c67710bbd12e6ac94d404dff1e01b1c3e653e757f4ba006359e2bf81417b1
- evidence_id: historical-selection
  kind: prior_review
  reference: REVIEW_WORK/batch060/record10/historical-selection.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Lossless selected historical objects with source hashes and exact snippets;
    derivative context, not newly recovered original source bytes.
  snapshot_sha256: 1ebd9289160bf30dc3a7542ea7768dbc70e451a66f161c5823393315951e907e
- evidence_id: inspection
  kind: validation
  reference: REVIEW_WORK/batch060/record10/inspection-addendum-historical/inspect.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Native additive context inspection retains all41 original inputs and adds
    three pooled historical reports,44 total.
  snapshot_sha256: 40371c5b36cb2b20fad6eabb2198dc3ab4e63b598c0c4bcf572b93f0f874adc7
- evidence_id: inspection-delta
  kind: validation
  reference: REVIEW_WORK/batch060/record10/inspection-addendum-historical/delta.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Original41 input bytes unchanged; only three context inputs added.
  snapshot_sha256: 329144b0466efca754e318e6305249b5607829de60f762222da2ea077c100936
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.1099/13500872-141-10-2449
  locator: pp2449–2454; especially p2450 left column Organism and culture conditions,
    p2452 Continuous culture and p2453 Fig5
  accessed_at: '2026-10-28T07:45:52.143718Z'
  support: supports
  summary: Mørkeberg R, Carlsen M, Nielsen J (1995), Microbiology141:2449–2454. All
    six PDF pages read visually and textually. Methods distinguish batch/continuous
    formulations, supplied hydrates and trace-stock addition; results scope continuous
    experiment to A1560.
  snapshot_sha256: 0fa1e59358cdc5803db7c4c20953594c8e6b23c8769f7349b8be184da574d314
- evidence_id: paper-text
  kind: primary_source
  reference: REVIEW_WORK/batch060/record10/sources/paper-visible.txt
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Text extraction checked against all six rendered pages. OCR punctuation/formula
    errors are retained in quoted text; chemically normalized transcriptions are separately
    identified.
  snapshot_sha256: 2d9d952a62585dd948f7fce395ae861e394b0e3e52a2d55771f645b45d540cbb
- evidence_id: paper-extraction
  kind: validation
  reference: REVIEW_WORK/batch060/record10/sources/paper-extraction.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Actual extraction/render commands and all six page-image hashes. Publisher
    response is a PDF; the CiteSeer lead returned HTML rather than the article.
  snapshot_sha256: bc137b32c338e92be2d340697ec76952fef12c78a4faf084f6e1eb6289c22857
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=7582005&retmode=xml
  locator: PubmedArticleSet/PubmedArticle
  accessed_at: '2026-10-28T07:43:54.982782Z'
  support: supports
  summary: Complete PubMed record confirms PMID7582005, DOI, authors, title/year/pages
    and exact existing abstract excerpts. No correction/retraction item appears in
    this inspected metadata; this is a bounded metadata check.
  snapshot_sha256: c6e06935a70296af7660bb73890f4b1edbcfdf20a9b223f124c9736418a42502
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1099%2F13500872-141-10-2449
  locator: $.message
  accessed_at: '2026-10-28T07:43:55.046359Z'
  support: supports
  summary: Publisher/DOI/title/authors/year/pages match; empty relation metadata is
    not a comprehensive retraction audit.
  snapshot_sha256: a9d71da11b065c3f70fdd3ae2a5f73f60ac4623154fdc896cecbcec39487650f
- evidence_id: taxonomy
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5062&retmode=xml
  locator: TaxaSet/Taxon[TaxId=5062]
  accessed_at: '2026-10-28T07:43:54.952259Z'
  support: supports
  summary: NCBITaxon5062 is Aspergillus oryzae at species rank in Fungi. This verifies
    the existing species parent; no exact A1560/CF1.1/CF2.1 strain node is asserted.
  snapshot_sha256: b28ef471324753819e59fbd697e6c4f2417d9d21618b270667e34bb9178f7fbd
- evidence_id: glucose-mass
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/glucose%20monohydrate/property/MolecularFormula,MolecularWeight/JSON
  locator: $.PropertyTable.Properties[0]
  accessed_at: '2026-10-28T07:54:31.308777Z'
  support: supports
  summary: NIH PubChem name-query property response gives formula C6H14O7 and molecular
    mass198.17. Used only for the mass conversion; no stereochemical/anomeric grounding
    is inferred from the query.
  snapshot_sha256: e0d903ee581071902329c49122e5d6511eb2a33e86cc32a8ae617cb1953e05ab
- evidence_id: glucose-id-search
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?q=glucose%20monohydrate&ontology=chebi&exact=true
  locator: $.response
  accessed_at: '2026-10-28T07:50:17.831194Z'
  support: unknown
  summary: Exact glucose-monohydrate ChEBI query returned no documents. This bounded
    query and MIM miss do not establish ontology-wide absence; exact hydrate identity
    remains unresolved.
  snapshot_sha256: b961a3766d15debbafc36efb2b85930a3814a1c322cdb88487b3ca19de4bf396
  search_scope: One exact OLS ChEBI query for glucose monohydrate at the recorded
    URL; only the returned response was inspected. No exhaustive ontology absence
    claim and no filesystem search.
- evidence_id: chebi-17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:55.384304Z'
  support: supports
  summary: Exact current term CHEBI:17234 = glucose; definition, synonyms, charge,
    empirical formula and mass read. This supports chemical identity/mass only.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi-23414
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23414
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:55.444434Z'
  support: supports
  summary: Exact current term CHEBI:23414 = copper(II) sulfate; definition, synonyms,
    charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 7f9d81f59ca2cbe7614d7e0dd3f85cb578000bf273b1b93968e74054e475fee1
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:55.585655Z'
  support: supports
  summary: Exact current term CHEBI:26710 = sodium chloride; definition, synonyms,
    charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi-31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:50:17.170607Z'
  support: supports
  summary: Exact current term CHEBI:31440 = copper(II) sulfate pentahydrate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi-31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:50:17.170653Z'
  support: supports
  summary: Exact current term CHEBI:31795 = magnesium sulfate heptahydrate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi-32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:50:17.163530Z'
  support: supports
  summary: Exact current term CHEBI:32312 = zinc sulfate heptahydrate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi-32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:55.587787Z'
  support: supports
  summary: Exact current term CHEBI:32599 = magnesium sulfate; definition, synonyms,
    charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi-3312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_3312
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:55.654675Z'
  support: supports
  summary: Exact current term CHEBI:3312 = calcium dichloride; definition, synonyms,
    charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 34ed49d95375c80dcb07576c67d04fa77337bfecf406accb283e8c32253b754b
- evidence_id: chebi-34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:56.060070Z'
  support: supports
  summary: Exact current term CHEBI:34887 = nickel dichloride; definition, synonyms,
    charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi-35176
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35176
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:56.053354Z'
  support: supports
  summary: Exact current term CHEBI:35176 = zinc sulfate; definition, synonyms, charge,
    empirical formula and mass read. This supports chemical identity/mass only.
  snapshot_sha256: 81ec7a8870c22cb4add111b8bd75e37886d7c96c9fc402a01f384c4cd4b6b746
- evidence_id: chebi-53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:50:17.158287Z'
  support: supports
  summary: Exact current term CHEBI:53542 = nickel chloride hexahydrate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: chebi-62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:56.184553Z'
  support: supports
  summary: Exact current term CHEBI:62946 = ammonium sulfate; definition, synonyms,
    charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi-63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:56.202496Z'
  support: supports
  summary: Exact current term CHEBI:63036 = potassium dihydrogen phosphate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi-75832
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75832
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:43:56.342986Z'
  support: supports
  summary: Exact current term CHEBI:75832 = iron(2+) sulfate (anhydrous); definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: b9119cb3893b1a8171f719ef3e8fe6e5775a4fd59575baec8cd6da953801d089
- evidence_id: chebi-75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:50:17.778309Z'
  support: supports
  summary: Exact current term CHEBI:75836 = iron(2+) sulfate heptahydrate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi-86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: $._embedded.terms[0]
  accessed_at: '2026-10-28T07:50:17.767161Z'
  support: supports
  summary: Exact current term CHEBI:86158 = calcium chloride dihydrate; definition,
    synonyms, charge, empirical formula and mass read. This supports chemical identity/mass
    only.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: mediadb-media-312-html
  kind: database
  reference: https://mediadb.systemsbiology.net/defined_media/media/312/
  locator: HTTP502 retained response
  accessed_at: '2026-10-28T07:43:54.729101Z'
  support: unknown
  summary: Exact named current source/export request returned502. Historical accession/formulation/version
    metadata are contextual; this response does not authenticate the old raw capture.
  snapshot_sha256: 76440d13ed742192bf6577638dbc565059fb80edab73982971686169bf58c273
- evidence_id: mediadb-media_text-312-html
  kind: database
  reference: https://mediadb.systemsbiology.net/defined_media/media_text/312/
  locator: HTTP502 retained response
  accessed_at: '2026-10-28T07:43:54.756558Z'
  support: unknown
  summary: Exact named current source/export request returned502. Historical accession/formulation/version
    metadata are contextual; this response does not authenticate the old raw capture.
  snapshot_sha256: 76440d13ed742192bf6577638dbc565059fb80edab73982971686169bf58c273
- evidence_id: mediadb-media-343-html
  kind: database
  reference: https://mediadb.systemsbiology.net/defined_media/media/343/
  locator: HTTP502 retained response
  accessed_at: '2026-10-28T07:43:54.744642Z'
  support: unknown
  summary: Exact named current source/export request returned502. Historical accession/formulation/version
    metadata are contextual; this response does not authenticate the old raw capture.
  snapshot_sha256: 76440d13ed742192bf6577638dbc565059fb80edab73982971686169bf58c273
- evidence_id: mediadb-media_text-343-html
  kind: database
  reference: https://mediadb.systemsbiology.net/defined_media/media_text/343/
  locator: HTTP502 retained response
  accessed_at: '2026-10-28T07:43:54.749448Z'
  support: unknown
  summary: Exact named current source/export request returned502. Historical accession/formulation/version
    metadata are contextual; this response does not authenticate the old raw capture.
  snapshot_sha256: 76440d13ed742192bf6577638dbc565059fb80edab73982971686169bf58c273
- evidence_id: mediadb-source120-html
  kind: database
  reference: https://mediadb.systemsbiology.net/defined_media/sources/120/
  locator: HTTP502 retained response
  accessed_at: '2026-10-28T07:43:54.736071Z'
  support: unknown
  summary: Exact named current source/export request returned502. Historical accession/formulation/version
    metadata are contextual; this response does not authenticate the old raw capture.
  snapshot_sha256: 76440d13ed742192bf6577638dbc565059fb80edab73982971686169bf58c273
- evidence_id: mediadb-export-sql-gz
  kind: database
  reference: https://mediadb.systemsbiology.net/static/defined_media/downloads/media_database.07Oct2015.sql.gz
  locator: HTTP502 retained response
  accessed_at: '2026-10-28T07:50:17.308047Z'
  support: unknown
  summary: Exact named current source/export request returned502. Historical accession/formulation/version
    metadata are contextual; this response does not authenticate the old raw capture.
  snapshot_sha256: 76440d13ed742192bf6577638dbc565059fb80edab73982971686169bf58c273
- evidence_id: publisher-html
  kind: search
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/13500872-141-10-2449
  locator: response status/content type/redirect preserved
  accessed_at: '2026-10-28T07:43:54.790916Z'
  support: unknown
  summary: 'Preserved access lead: publisher HTML403; CiteSeer redirected to an archived
    HTML response. The separately retrieved publisher PDF supplies full text.'
  snapshot_sha256: 6fff41a047e8faadbd7fc279ae87c6749113636b085bcc3ec96353883e3673ae
  search_scope: One HTTP GET to the exact recorded URL, following its observed redirect
    chain; status, content type and response bytes were retained. This access attempt
    does not establish source absence, and it is not a filesystem search.
- evidence_id: publisher-full-html
  kind: search
  reference: https://www.microbiologyresearch.org/deliver/fulltext/micro/141/10/mic-141-10-2449.html?itemId=/content/journal/micro/10.1099/13500872-141-10-2449&mimeType=html&fmt=ahah
  locator: response status/content type/redirect preserved
  accessed_at: '2026-10-28T07:43:54.829486Z'
  support: unknown
  summary: 'Preserved access lead: publisher HTML403; CiteSeer redirected to an archived
    HTML response. The separately retrieved publisher PDF supplies full text.'
  snapshot_sha256: b1e89ca24c9e9797d1780e67109d97f7dfe33e5aeac78edccacb78d798e58c09
  search_scope: One HTTP GET to the exact recorded URL, following its observed redirect
    chain; status, content type and response bytes were retained. This access attempt
    does not establish source absence, and it is not a filesystem search.
- evidence_id: paper-citeseer-pdf
  kind: search
  reference: https://citeseerx.ist.psu.edu/document?doi=7e5826102180b2b72bb9323a3783cd1fc08a273d&repid=rep1&type=pdf
  locator: response status/content type/redirect preserved
  accessed_at: '2026-10-28T07:45:51.060781Z'
  support: unknown
  summary: 'Preserved access lead: publisher HTML403; CiteSeer redirected to an archived
    HTML response. The separately retrieved publisher PDF supplies full text.'
  snapshot_sha256: 5d2134aee0d43f84c85e35f8e1a4e566a92dd129366a493e4eee9464a50a6858
  search_scope: One HTTP GET to the exact recorded URL, following its observed redirect
    chain; status, content type and response bytes were retained. This access attempt
    does not establish source absence, and it is not a filesystem search.
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record10/validate-schema-result.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Original once-only command, real UTC times and complete streams read. Structural/label
    checks do not certify source support.
  snapshot_sha256: 587d3b3a0086271b0f858245bc04384430e336a4ddd7f5e5bd05991fbf29dedb
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record10/validate-strict-result.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Original once-only command, real UTC times and complete streams read. Structural/label
    checks do not certify source support.
  snapshot_sha256: 28042da85864990e8f7ae14794abdcea6d81e0682fd9dac138f6634fcf2f2459
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record10/validate-terms-result.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Original once-only command, real UTC times and complete streams read. Structural/label
    checks do not certify source support.
  snapshot_sha256: cc931aa2928947f8a67285f87302f7fedd59cbb85a6107f56b42749361e9e97b
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch060/record10/validate-references-result.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Original once-only command, real UTC times and complete streams read. Structural/label
    checks do not certify source support.
  snapshot_sha256: 756994115d1a82650c0f2f79de8d46a73601e2ad13f5b8c2e8f0a355ad7bbe22
- evidence_id: check-mim-label-index
  kind: validation
  reference: REVIEW_WORK/batch060/record10/check-mim-label-index-result.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:01:14.201003Z'
  support: supports
  summary: Original once-only command, real UTC times and complete streams read. Structural/label
    checks do not certify source support.
  snapshot_sha256: b4baf0dae0f28675b9030191d4d0838e257bf32652640b6ec701a09aba83ef1b
- evidence_id: quantity-inventory
  kind: validation
  reference: REVIEW_WORK/batch060/record10/quantity-inventory.json
  locator: entire declared file or explicitly scoped section
  accessed_at: '2026-10-28T08:07:35.945267Z'
  support: supports
  summary: 38 decisions account for all30 local concentration fields, four source
    stock masses, receiving dose, two titrant strengths and unknown stock final volume.
    Actual inspected primary snippets and separate arithmetic retained.
  snapshot_sha256: 94f73e16d610dfd7e74a70d786416a966e48c8b5031acea1972627038b80cd5d
assessments:
- assessment_id: identity
  area: identity
  topic: Continuous/batch accession, variant and fungal category
  outcome: concern
  summary: The selected generated record is unambiguously resolved, but its continuous
    MEDIADB343 identity carries batch glucose/ammonium values and a contradictory
    continuous-variant note. Both owners resolve; the primary is a fungal study.
  target_ids:
  - CultureMech:007244
  evidence_ids:
  - target
  - batch-owner
  - continuous-owner
  - paper
  - taxonomy
  - diagnostics
  details: 'The maintained child preserves the lower two concentrations; parent/child
    references resolve and the October13 citation is already present in both. Defined/liquid
    composition is consistent with the reported glucose medium. The subsequent maltose-feed
    phase is a separate condition, not the default glucose recipe. iModulonDB is not
    applicable: no gene, expression module or transcriptomic dataset is asserted.'
- assessment_id: quantities
  area: quantity
  topic: Every local amount and source stock/control quantity
  outcome: concern
  summary: Six main-component molarities per owner agree with source mass-per-litre
    values at the supplied-form molecular masses. Two generated child fields retain
    parent values. Twelve local trace-component fields remain unsupported as final
    molarities because the primary stock denominator is unspecified.
  target_ids:
  - CultureMech:007244
  evidence_ids:
  - paper
  - paper-text
  - glucose-mass
  - quantity-inventory
  - historical-selection
  details: "[\n  {\n    \"decision_id\": \"q01\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[0].concentration\",\n    \"ingredient\": \"Ferrous\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.02482\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5192,343,16397,0.02482)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"iron(2+) sulfate\
    \ heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:75836\",\n    \"source_stock_mass_g\"\
    : \"13.8\",\n    \"source_snippet\": \"13.8 g FeSO,. 7H,O\",\n    \"basis\": \"\
    Four hydrate masses are listed inside the trace-solution parenthesis, with no\
    \ explicit stock final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\"\
    : \"Not performed: unknown stock-volume denominator prevents independent confirmation\
    \ of this final-medium mM. Historical database agrees with the local value but\
    \ does not repair missing primary basis.\",\n    \"proposed_value\": null\n  },\n\
    \  {\n    \"decision_id\": \"q02\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[1].concentration\",\n    \"ingredient\": \"Nickel\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"0.001052\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5188,343,13121,0.001052)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"nickel chloride\
    \ hexahydrate\",\n    \"verified_form_candidate\": \"CHEBI:53542\",\n    \"source_stock_mass_g\"\
    : \"0.5\",\n    \"source_snippet\": \"0.5 g\",\n    \"basis\": \"Four hydrate\
    \ masses are listed inside the trace-solution parenthesis, with no explicit stock\
    \ final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\": \"Not performed:\
    \ unknown stock-volume denominator prevents independent confirmation of this final-medium\
    \ mM. Historical database agrees with the local value but does not repair missing\
    \ primary basis.\",\n    \"proposed_value\": null\n  },\n  {\n    \"decision_id\"\
    : \"q03\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[2].concentration\",\n    \"ingredient\": \"Glucose\"\
    ,\n    \"existing\": {\n      \"value\": \"126.2\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5187,343,280,40.37)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"correct\",\n    \"source_form\"\
    : \"glucose monohydrate\",\n    \"verified_form_candidate\": null,\n    \"source_mass_g_per_L\"\
    : \"8.0\",\n    \"source_snippet\": \"8*0g glucose monohydrate\",\n    \"basis\"\
    : \"Primary explicitly uses per-litre medium composition; continuous recipe changes\
    \ only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate\
    \ formula span adjacent lines in the paragraph, checked visually.\",\n    \"molecular_mass_g_per_mol\"\
    : \"198.17\",\n    \"calculation\": \"8.0 g/L *1000 /198.17 g/mol = 40.36937982540243225513448050\
    \ mM; existing value is compared as a rounded nominal solute concentration.\"\
    ,\n    \"proposed_value\": \"40.37\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n\
    \    \"identity_caveat\": \"A matching molarity does not establish that the encoded\
    \ supplied chemical form is correct. Preserve source hydrate and independently\
    \ reviewed identifier; glucose stereo/anomer remains unspecified.\"\n  },\n  {\n\
    \    \"decision_id\": \"q04\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[3].concentration\",\n    \"ingredient\": \"Calcium\
    \ chloride anhydrous\",\n    \"existing\": {\n      \"value\": \"0.6802\",\n \
    \     \"unit\": \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5191,343,6656,0.6802)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"calcium chloride dihydrate\",\n    \"verified_form_candidate\": \"CHEBI:86158\"\
    ,\n    \"source_mass_g_per_L\": \"0.1\",\n    \"source_snippet\": \"0.1 g CaC1,.2H20\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"147.014\",\n    \"calculation\": \"0.1\
    \ g/L *1000 /147.014 g/mol = 0.6802073271933285265348878338 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"0.6802\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q05\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[4].concentration\",\n    \"ingredient\": \"Sodium\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"17.11\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5186,343,16384,17.11)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"sodium chloride\",\n    \"verified_form_candidate\": \"CHEBI:26710\",\n  \
    \  \"source_mass_g_per_L\": \"1.0\",\n    \"source_snippet\": \"1.0 g NaC1\",\n\
    \    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"58.443\",\n    \"calculation\": \"1.0 g/L\
    \ *1000 /58.443 g/mol = 17.11068904744794072857313964 mM; existing value is compared\
    \ as a rounded nominal solute concentration.\",\n    \"proposed_value\": \"17.11\"\
    ,\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\": \"A matching\
    \ molarity does not establish that the encoded supplied chemical form is correct.\
    \ Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer\
    \ remains unspecified.\"\n  },\n  {\n    \"decision_id\": \"q06\",\n    \"path\"\
    : \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\",\n    \"field\"\
    : \"ingredients[5].concentration\",\n    \"ingredient\": \"Cupric sulfate\",\n\
    \    \"existing\": {\n      \"value\": \"0.005006\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5195,343,16405,0.005006)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"copper(II)\
    \ sulfate pentahydrate\",\n    \"verified_form_candidate\": \"CHEBI:31440\",\n\
    \    \"source_stock_mass_g\": \"2.5\",\n    \"source_snippet\": \"2 5 g CuSO,.\
    \ 5H,O\",\n    \"basis\": \"Four hydrate masses are listed inside the trace-solution\
    \ parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.\"\
    ,\n    \"calculation\": \"Not performed: unknown stock-volume denominator prevents\
    \ independent confirmation of this final-medium mM. Historical database agrees\
    \ with the local value but does not repair missing primary basis.\",\n    \"proposed_value\"\
    : null\n  },\n  {\n    \"decision_id\": \"q07\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[6].concentration\",\n    \"ingredient\": \"Zinc\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.02487\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5189,343,16399,0.02487)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"zinc sulfate\
    \ heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:32312\",\n    \"source_stock_mass_g\"\
    : \"14.3\",\n    \"source_snippet\": \"14.3 g ZnSO,. 7H,O\",\n    \"basis\": \"\
    Four hydrate masses are listed inside the trace-solution parenthesis, with no\
    \ explicit stock final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\"\
    : \"Not performed: unknown stock-volume denominator prevents independent confirmation\
    \ of this final-medium mM. Historical database agrees with the local value but\
    \ does not repair missing primary basis.\",\n    \"proposed_value\": null\n  },\n\
    \  {\n    \"decision_id\": \"q08\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[7].concentration\",\n    \"ingredient\": \"Magnesium\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"4.057\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5193,343,16394,4.057)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"magnesium sulfate heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:31795\"\
    ,\n    \"source_mass_g_per_L\": \"1.0\",\n    \"source_snippet\": \"MgSO,. 7H20\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"246.473\",\n    \"calculation\": \"1.0\
    \ g/L *1000 /246.473 g/mol = 4.057239535364928410008398486 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"4.057\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q09\",\n    \"path\": \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[8].concentration\",\n    \"ingredient\": \"Potassium\
    \ dihydrogen phosphate\",\n    \"existing\": {\n      \"value\": \"11.02\",\n\
    \      \"unit\": \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5190,343,16391,11.02)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"potassium dihydrogen phosphate\",\n    \"verified_form_candidate\": \"CHEBI:63036\"\
    ,\n    \"source_mass_g_per_L\": \"1.5\",\n    \"source_snippet\": \"1.5 g KH,PO,\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"136.084\",\n    \"calculation\": \"1.5\
    \ g/L *1000 /136.084 g/mol = 11.02260368595867258458011228 mM; existing value\
    \ is compared as a rounded nominal solute concentration. At the existing displayed\
    \ precision, the source-derived value rounds to 11.02 mM; retain that nominal\
    \ amount with the supplied-form caveat.\",\n    \"proposed_value\": \"11.02\"\
    ,\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\": \"A matching\
    \ molarity does not establish that the encoded supplied chemical form is correct.\
    \ Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer\
    \ remains unspecified.\"\n  },\n  {\n    \"decision_id\": \"q10\",\n    \"path\"\
    : \"data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml\",\n    \"field\"\
    : \"ingredients[9].concentration\",\n    \"ingredient\": \"Ammonium sulfate\"\
    ,\n    \"existing\": {\n      \"value\": \"55.24\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5194,343,16401,37.84)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"correct\",\n    \"source_form\"\
    : \"ammonium sulfate\",\n    \"verified_form_candidate\": \"CHEBI:62946\",\n \
    \   \"source_mass_g_per_L\": \"5.0\",\n    \"source_snippet\": \"5.0 g (NH,),SO,\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"132.141\",\n    \"calculation\": \"5.0\
    \ g/L *1000 /132.141 g/mol = 37.83836962032979922961079453 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"37.84\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q11\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[0].concentration\",\n    \"ingredient\": \"Ferrous\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.02482\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(4437,312,16397,0.02482)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"iron(2+) sulfate\
    \ heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:75836\",\n    \"source_stock_mass_g\"\
    : \"13.8\",\n    \"source_snippet\": \"13.8 g FeSO,. 7H,O\",\n    \"basis\": \"\
    Four hydrate masses are listed inside the trace-solution parenthesis, with no\
    \ explicit stock final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\"\
    : \"Not performed: unknown stock-volume denominator prevents independent confirmation\
    \ of this final-medium mM. Historical database agrees with the local value but\
    \ does not repair missing primary basis.\",\n    \"proposed_value\": null\n  },\n\
    \  {\n    \"decision_id\": \"q12\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[1].concentration\",\n    \"ingredient\": \"Nickel\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"0.001052\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(4438,312,13121,0.001052)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"nickel chloride\
    \ hexahydrate\",\n    \"verified_form_candidate\": \"CHEBI:53542\",\n    \"source_stock_mass_g\"\
    : \"0.5\",\n    \"source_snippet\": \"0.5 g\",\n    \"basis\": \"Four hydrate\
    \ masses are listed inside the trace-solution parenthesis, with no explicit stock\
    \ final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\": \"Not performed:\
    \ unknown stock-volume denominator prevents independent confirmation of this final-medium\
    \ mM. Historical database agrees with the local value but does not repair missing\
    \ primary basis.\",\n    \"proposed_value\": null\n  },\n  {\n    \"decision_id\"\
    : \"q13\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[2].concentration\",\n    \"ingredient\": \"Glucose\"\
    ,\n    \"existing\": {\n      \"value\": \"126.2\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(4439,312,280,126.2)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"glucose monohydrate\",\n    \"verified_form_candidate\": null,\n    \"source_mass_g_per_L\"\
    : \"25.0\",\n    \"source_snippet\": \"25.0 g glucose\",\n    \"basis\": \"Primary\
    \ explicitly uses per-litre medium composition; continuous recipe changes only\
    \ glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate formula\
    \ span adjacent lines in the paragraph, checked visually.\",\n    \"molecular_mass_g_per_mol\"\
    : \"198.17\",\n    \"calculation\": \"25.0 g/L *1000 /198.17 g/mol = 126.1543119543826007972952516\
    \ mM; existing value is compared as a rounded nominal solute concentration. At\
    \ the existing displayed precision, the source-derived value rounds to 126.2 mM;\
    \ retain that nominal amount with the supplied-form caveat.\",\n    \"proposed_value\"\
    : \"126.2\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q14\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[3].concentration\",\n    \"ingredient\": \"Calcium\
    \ chloride anhydrous\",\n    \"existing\": {\n      \"value\": \"0.6802\",\n \
    \     \"unit\": \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(4440,312,6656,0.6802)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"calcium chloride dihydrate\",\n    \"verified_form_candidate\": \"CHEBI:86158\"\
    ,\n    \"source_mass_g_per_L\": \"0.1\",\n    \"source_snippet\": \"0.1 g CaC1,.2H20\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"147.014\",\n    \"calculation\": \"0.1\
    \ g/L *1000 /147.014 g/mol = 0.6802073271933285265348878338 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"0.6802\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q15\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[4].concentration\",\n    \"ingredient\": \"Sodium\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"17.11\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(4441,312,16384,17.11)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"sodium chloride\",\n    \"verified_form_candidate\": \"CHEBI:26710\",\n  \
    \  \"source_mass_g_per_L\": \"1.0\",\n    \"source_snippet\": \"1.0 g NaC1\",\n\
    \    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"58.443\",\n    \"calculation\": \"1.0 g/L\
    \ *1000 /58.443 g/mol = 17.11068904744794072857313964 mM; existing value is compared\
    \ as a rounded nominal solute concentration.\",\n    \"proposed_value\": \"17.11\"\
    ,\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\": \"A matching\
    \ molarity does not establish that the encoded supplied chemical form is correct.\
    \ Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer\
    \ remains unspecified.\"\n  },\n  {\n    \"decision_id\": \"q16\",\n    \"path\"\
    : \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\",\n    \"field\"\
    : \"ingredients[5].concentration\",\n    \"ingredient\": \"Cupric sulfate\",\n\
    \    \"existing\": {\n      \"value\": \"0.005006\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(4442,312,16405,0.005006)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"copper(II)\
    \ sulfate pentahydrate\",\n    \"verified_form_candidate\": \"CHEBI:31440\",\n\
    \    \"source_stock_mass_g\": \"2.5\",\n    \"source_snippet\": \"2 5 g CuSO,.\
    \ 5H,O\",\n    \"basis\": \"Four hydrate masses are listed inside the trace-solution\
    \ parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.\"\
    ,\n    \"calculation\": \"Not performed: unknown stock-volume denominator prevents\
    \ independent confirmation of this final-medium mM. Historical database agrees\
    \ with the local value but does not repair missing primary basis.\",\n    \"proposed_value\"\
    : null\n  },\n  {\n    \"decision_id\": \"q17\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[6].concentration\",\n    \"ingredient\": \"Zinc\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.02487\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(4443,312,16399,0.02487)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"zinc sulfate\
    \ heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:32312\",\n    \"source_stock_mass_g\"\
    : \"14.3\",\n    \"source_snippet\": \"14.3 g ZnSO,. 7H,O\",\n    \"basis\": \"\
    Four hydrate masses are listed inside the trace-solution parenthesis, with no\
    \ explicit stock final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\"\
    : \"Not performed: unknown stock-volume denominator prevents independent confirmation\
    \ of this final-medium mM. Historical database agrees with the local value but\
    \ does not repair missing primary basis.\",\n    \"proposed_value\": null\n  },\n\
    \  {\n    \"decision_id\": \"q18\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[7].concentration\",\n    \"ingredient\": \"Magnesium\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"4.057\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(4444,312,16394,4.057)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"magnesium sulfate heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:31795\"\
    ,\n    \"source_mass_g_per_L\": \"1.0\",\n    \"source_snippet\": \"MgSO,. 7H20\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"246.473\",\n    \"calculation\": \"1.0\
    \ g/L *1000 /246.473 g/mol = 4.057239535364928410008398486 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"4.057\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q19\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[8].concentration\",\n    \"ingredient\": \"Potassium\
    \ dihydrogen phosphate\",\n    \"existing\": {\n      \"value\": \"11.02\",\n\
    \      \"unit\": \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(4445,312,16391,11.02)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"potassium dihydrogen phosphate\",\n    \"verified_form_candidate\": \"CHEBI:63036\"\
    ,\n    \"source_mass_g_per_L\": \"1.5\",\n    \"source_snippet\": \"1.5 g KH,PO,\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"136.084\",\n    \"calculation\": \"1.5\
    \ g/L *1000 /136.084 g/mol = 11.02260368595867258458011228 mM; existing value\
    \ is compared as a rounded nominal solute concentration. At the existing displayed\
    \ precision, the source-derived value rounds to 11.02 mM; retain that nominal\
    \ amount with the supplied-form caveat.\",\n    \"proposed_value\": \"11.02\"\
    ,\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\": \"A matching\
    \ molarity does not establish that the encoded supplied chemical form is correct.\
    \ Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer\
    \ remains unspecified.\"\n  },\n  {\n    \"decision_id\": \"q20\",\n    \"path\"\
    : \"data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml\",\n    \"field\"\
    : \"ingredients[9].concentration\",\n    \"ingredient\": \"Ammonium sulfate\"\
    ,\n    \"existing\": {\n      \"value\": \"55.24\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(4446,312,16401,55.24)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"ammonium sulfate\",\n    \"verified_form_candidate\": \"CHEBI:62946\",\n \
    \   \"source_mass_g_per_L\": \"7.3\",\n    \"source_snippet\": \"7-3 g (NH,),SO,\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"132.141\",\n    \"calculation\": \"7.3\
    \ g/L *1000 /132.141 g/mol = 55.24401964568150687523176001 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"55.24\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q21\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[0].concentration\",\n    \"ingredient\": \"Sodium\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"17.11\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5186,343,16384,17.11)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"sodium chloride\",\n    \"verified_form_candidate\": \"CHEBI:26710\",\n  \
    \  \"source_mass_g_per_L\": \"1.0\",\n    \"source_snippet\": \"1.0 g NaC1\",\n\
    \    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"58.443\",\n    \"calculation\": \"1.0 g/L\
    \ *1000 /58.443 g/mol = 17.11068904744794072857313964 mM; existing value is compared\
    \ as a rounded nominal solute concentration.\",\n    \"proposed_value\": \"17.11\"\
    ,\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\": \"A matching\
    \ molarity does not establish that the encoded supplied chemical form is correct.\
    \ Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer\
    \ remains unspecified.\"\n  },\n  {\n    \"decision_id\": \"q22\",\n    \"path\"\
    : \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\",\n  \
    \  \"field\": \"ingredients[1].concentration\",\n    \"ingredient\": \"Glucose\"\
    ,\n    \"existing\": {\n      \"value\": \"40.37\",\n      \"unit\": \"MILLIMOLAR\"\
    \n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5187,343,280,40.37)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"glucose monohydrate\",\n    \"verified_form_candidate\": null,\n    \"source_mass_g_per_L\"\
    : \"8.0\",\n    \"source_snippet\": \"8*0g glucose monohydrate\",\n    \"basis\"\
    : \"Primary explicitly uses per-litre medium composition; continuous recipe changes\
    \ only glucose and ammonium sulfate. For magnesium, the1.0g amount and hydrate\
    \ formula span adjacent lines in the paragraph, checked visually.\",\n    \"molecular_mass_g_per_mol\"\
    : \"198.17\",\n    \"calculation\": \"8.0 g/L *1000 /198.17 g/mol = 40.36937982540243225513448050\
    \ mM; existing value is compared as a rounded nominal solute concentration.\"\
    ,\n    \"proposed_value\": \"40.37\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n\
    \    \"identity_caveat\": \"A matching molarity does not establish that the encoded\
    \ supplied chemical form is correct. Preserve source hydrate and independently\
    \ reviewed identifier; glucose stereo/anomer remains unspecified.\"\n  },\n  {\n\
    \    \"decision_id\": \"q23\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[2].concentration\",\n    \"ingredient\": \"Nickel\
    \ chloride\",\n    \"existing\": {\n      \"value\": \"0.001052\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5188,343,13121,0.001052)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"nickel chloride\
    \ hexahydrate\",\n    \"verified_form_candidate\": \"CHEBI:53542\",\n    \"source_stock_mass_g\"\
    : \"0.5\",\n    \"source_snippet\": \"0.5 g\",\n    \"basis\": \"Four hydrate\
    \ masses are listed inside the trace-solution parenthesis, with no explicit stock\
    \ final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\": \"Not performed:\
    \ unknown stock-volume denominator prevents independent confirmation of this final-medium\
    \ mM. Historical database agrees with the local value but does not repair missing\
    \ primary basis.\",\n    \"proposed_value\": null\n  },\n  {\n    \"decision_id\"\
    : \"q24\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[3].concentration\",\n    \"ingredient\": \"Zinc\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.02487\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5189,343,16399,0.02487)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"zinc sulfate\
    \ heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:32312\",\n    \"source_stock_mass_g\"\
    : \"14.3\",\n    \"source_snippet\": \"14.3 g ZnSO,. 7H,O\",\n    \"basis\": \"\
    Four hydrate masses are listed inside the trace-solution parenthesis, with no\
    \ explicit stock final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\"\
    : \"Not performed: unknown stock-volume denominator prevents independent confirmation\
    \ of this final-medium mM. Historical database agrees with the local value but\
    \ does not repair missing primary basis.\",\n    \"proposed_value\": null\n  },\n\
    \  {\n    \"decision_id\": \"q25\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[4].concentration\",\n    \"ingredient\": \"Potassium\
    \ dihydrogen phosphate\",\n    \"existing\": {\n      \"value\": \"11.02\",\n\
    \      \"unit\": \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5190,343,16391,11.02)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"potassium dihydrogen phosphate\",\n    \"verified_form_candidate\": \"CHEBI:63036\"\
    ,\n    \"source_mass_g_per_L\": \"1.5\",\n    \"source_snippet\": \"1.5 g KH,PO,\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"136.084\",\n    \"calculation\": \"1.5\
    \ g/L *1000 /136.084 g/mol = 11.02260368595867258458011228 mM; existing value\
    \ is compared as a rounded nominal solute concentration. At the existing displayed\
    \ precision, the source-derived value rounds to 11.02 mM; retain that nominal\
    \ amount with the supplied-form caveat.\",\n    \"proposed_value\": \"11.02\"\
    ,\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\": \"A matching\
    \ molarity does not establish that the encoded supplied chemical form is correct.\
    \ Preserve source hydrate and independently reviewed identifier; glucose stereo/anomer\
    \ remains unspecified.\"\n  },\n  {\n    \"decision_id\": \"q26\",\n    \"path\"\
    : \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\",\n  \
    \  \"field\": \"ingredients[5].concentration\",\n    \"ingredient\": \"Calcium\
    \ chloride anhydrous\",\n    \"existing\": {\n      \"value\": \"0.6802\",\n \
    \     \"unit\": \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5191,343,6656,0.6802)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"calcium chloride dihydrate\",\n    \"verified_form_candidate\": \"CHEBI:86158\"\
    ,\n    \"source_mass_g_per_L\": \"0.1\",\n    \"source_snippet\": \"0.1 g CaC1,.2H20\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"147.014\",\n    \"calculation\": \"0.1\
    \ g/L *1000 /147.014 g/mol = 0.6802073271933285265348878338 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"0.6802\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q27\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[6].concentration\",\n    \"ingredient\": \"Ferrous\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.02482\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5192,343,16397,0.02482)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"iron(2+) sulfate\
    \ heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:75836\",\n    \"source_stock_mass_g\"\
    : \"13.8\",\n    \"source_snippet\": \"13.8 g FeSO,. 7H,O\",\n    \"basis\": \"\
    Four hydrate masses are listed inside the trace-solution parenthesis, with no\
    \ explicit stock final volume. The receiving dose is0.5mL/L.\",\n    \"calculation\"\
    : \"Not performed: unknown stock-volume denominator prevents independent confirmation\
    \ of this final-medium mM. Historical database agrees with the local value but\
    \ does not repair missing primary basis.\",\n    \"proposed_value\": null\n  },\n\
    \  {\n    \"decision_id\": \"q28\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[7].concentration\",\n    \"ingredient\": \"Magnesium\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"4.057\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5193,343,16394,4.057)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"magnesium sulfate heptahydrate\",\n    \"verified_form_candidate\": \"CHEBI:31795\"\
    ,\n    \"source_mass_g_per_L\": \"1.0\",\n    \"source_snippet\": \"MgSO,. 7H20\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"246.473\",\n    \"calculation\": \"1.0\
    \ g/L *1000 /246.473 g/mol = 4.057239535364928410008398486 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"4.057\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q29\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[8].concentration\",\n    \"ingredient\": \"Ammonium\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"37.84\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"main medium\",\n    \"historical_database_snippet\"\
    : \"(5194,343,16401,37.84)\",\n    \"historical_evidence_status\": \"Derivative\
    \ report only; original2015 SQL and October2026 HTML captures not recovered.\"\
    ,\n    \"action_taken\": \"none\",\n    \"decision\": \"verified\",\n    \"source_form\"\
    : \"ammonium sulfate\",\n    \"verified_form_candidate\": \"CHEBI:62946\",\n \
    \   \"source_mass_g_per_L\": \"5.0\",\n    \"source_snippet\": \"5.0 g (NH,),SO,\"\
    ,\n    \"basis\": \"Primary explicitly uses per-litre medium composition; continuous\
    \ recipe changes only glucose and ammonium sulfate. For magnesium, the1.0g amount\
    \ and hydrate formula span adjacent lines in the paragraph, checked visually.\"\
    ,\n    \"molecular_mass_g_per_mol\": \"132.141\",\n    \"calculation\": \"5.0\
    \ g/L *1000 /132.141 g/mol = 37.83836962032979922961079453 mM; existing value\
    \ is compared as a rounded nominal solute concentration.\",\n    \"proposed_value\"\
    : \"37.84\",\n    \"proposed_unit\": \"MILLIMOLAR\",\n    \"identity_caveat\"\
    : \"A matching molarity does not establish that the encoded supplied chemical\
    \ form is correct. Preserve source hydrate and independently reviewed identifier;\
    \ glucose stereo/anomer remains unspecified.\"\n  },\n  {\n    \"decision_id\"\
    : \"q30\",\n    \"path\": \"data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml\"\
    ,\n    \"field\": \"ingredients[9].concentration\",\n    \"ingredient\": \"Cupric\
    \ sulfate\",\n    \"existing\": {\n      \"value\": \"0.005006\",\n      \"unit\"\
    : \"MILLIMOLAR\"\n    },\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, Organism and culture conditions, formulation\
    \ paragraph\",\n    \"source_stage\": \"trace-stock addition, final working contribution\
    \ unresolved\",\n    \"historical_database_snippet\": \"(5195,343,16405,0.005006)\"\
    ,\n    \"historical_evidence_status\": \"Derivative report only; original2015\
    \ SQL and October2026 HTML captures not recovered.\",\n    \"action_taken\": \"\
    none\",\n    \"decision\": \"unsupported\",\n    \"source_form\": \"copper(II)\
    \ sulfate pentahydrate\",\n    \"verified_form_candidate\": \"CHEBI:31440\",\n\
    \    \"source_stock_mass_g\": \"2.5\",\n    \"source_snippet\": \"2 5 g CuSO,.\
    \ 5H,O\",\n    \"basis\": \"Four hydrate masses are listed inside the trace-solution\
    \ parenthesis, with no explicit stock final volume. The receiving dose is0.5mL/L.\"\
    ,\n    \"calculation\": \"Not performed: unknown stock-volume denominator prevents\
    \ independent confirmation of this final-medium mM. Historical database agrees\
    \ with the local value but does not repair missing primary basis.\",\n    \"proposed_value\"\
    : null\n  },\n  {\n    \"decision_id\": \"q31\",\n    \"path\": null,\n    \"\
    field\": \"source-only trace-stock composition\",\n    \"ingredient\": \"iron(2+)\
    \ sulfate heptahydrate\",\n    \"decision\": \"evidence_only\",\n    \"source_amount_g\"\
    : \"13.8\",\n    \"source_snippet\": \"13.8 g FeSO,. 7H,O\",\n    \"source_stage\"\
    : \"trace stock\",\n    \"basis\": \"Stock final volume unspecified, so grams\
    \ are not silently relabelled g/L.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 formulation paragraph, trace-stock parenthesis\",\n\
    \    \"verified_form_candidate\": \"CHEBI:75836\",\n    \"action_taken\": \"none\"\
    \n  },\n  {\n    \"decision_id\": \"q32\",\n    \"path\": null,\n    \"field\"\
    : \"source-only trace-stock composition\",\n    \"ingredient\": \"nickel chloride\
    \ hexahydrate\",\n    \"decision\": \"evidence_only\",\n    \"source_amount_g\"\
    : \"0.5\",\n    \"source_snippet\": \"0.5 g\",\n    \"source_stage\": \"trace\
    \ stock\",\n    \"basis\": \"Stock final volume unspecified, so grams are not\
    \ silently relabelled g/L.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 formulation paragraph, trace-stock parenthesis\",\n\
    \    \"verified_form_candidate\": \"CHEBI:53542\",\n    \"action_taken\": \"none\"\
    \n  },\n  {\n    \"decision_id\": \"q33\",\n    \"path\": null,\n    \"field\"\
    : \"source-only trace-stock composition\",\n    \"ingredient\": \"copper(II) sulfate\
    \ pentahydrate\",\n    \"decision\": \"evidence_only\",\n    \"source_amount_g\"\
    : \"2.5\",\n    \"source_snippet\": \"2 5 g CuSO,. 5H,O\",\n    \"source_stage\"\
    : \"trace stock\",\n    \"basis\": \"Stock final volume unspecified, so grams\
    \ are not silently relabelled g/L.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 formulation paragraph, trace-stock parenthesis\",\n\
    \    \"verified_form_candidate\": \"CHEBI:31440\",\n    \"action_taken\": \"none\"\
    \n  },\n  {\n    \"decision_id\": \"q34\",\n    \"path\": null,\n    \"field\"\
    : \"source-only trace-stock composition\",\n    \"ingredient\": \"zinc sulfate\
    \ heptahydrate\",\n    \"decision\": \"evidence_only\",\n    \"source_amount_g\"\
    : \"14.3\",\n    \"source_snippet\": \"14.3 g ZnSO,. 7H,O\",\n    \"source_stage\"\
    : \"trace stock\",\n    \"basis\": \"Stock final volume unspecified, so grams\
    \ are not silently relabelled g/L.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 formulation paragraph, trace-stock parenthesis\",\n\
    \    \"verified_form_candidate\": \"CHEBI:32312\",\n    \"action_taken\": \"none\"\
    \n  },\n  {\n    \"decision_id\": \"q35\",\n    \"path\": null,\n    \"field\"\
    : \"source-only preparation/stock boundary\",\n    \"ingredient\": \"Trace-stock\
    \ receiving dose\",\n    \"decision\": \"add\",\n    \"source_value\": \"0.5\"\
    ,\n    \"source_unit\": \"ML_PER_L\",\n    \"source_snippet\": \"0.5 ml trace\"\
    ,\n    \"source_stage\": \"preparation or culture pH control\",\n    \"basis\"\
    : \"Main medium per-litre header supplies receiving basis, not the trace-stock\
    \ formulation denominator.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, formulation and culture conditions\"\
    ,\n    \"action_taken\": \"none\"\n  },\n  {\n    \"decision_id\": \"q36\",\n\
    \    \"path\": null,\n    \"field\": \"source-only preparation/stock boundary\"\
    ,\n    \"ingredient\": \"Sulfuric-acid titrant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_value\": \"2\",\n    \"source_unit\": \"MOLAR\",\n    \"source_snippet\"\
    : \"2 M H,SO,\",\n    \"source_stage\": \"preparation or culture pH control\"\
    ,\n    \"basis\": \"pH-control stock strength; no fixed added volume or final-medium\
    \ sulfate contribution reported.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, formulation and culture conditions\"\
    ,\n    \"action_taken\": \"none\"\n  },\n  {\n    \"decision_id\": \"q37\",\n\
    \    \"path\": null,\n    \"field\": \"source-only preparation/stock boundary\"\
    ,\n    \"ingredient\": \"Sodium-hydroxide titrant\",\n    \"decision\": \"evidence_only\"\
    ,\n    \"source_value\": \"4\",\n    \"source_unit\": \"MOLAR\",\n    \"source_snippet\"\
    : \"4 M NaOH\",\n    \"source_stage\": \"preparation or culture pH control\",\n\
    \    \"basis\": \"pH-control stock strength; no fixed added volume or final-medium\
    \ sodium contribution reported.\",\n    \"reference\": \"https://doi.org/10.1099/13500872-141-10-2449\"\
    ,\n    \"locator\": \"p2450 left column, formulation and culture conditions\"\
    ,\n    \"action_taken\": \"none\"\n  },\n  {\n    \"decision_id\": \"q38\",\n\
    \    \"path\": null,\n    \"field\": \"source-only preparation/stock boundary\"\
    ,\n    \"ingredient\": \"Trace-stock final volume\",\n    \"decision\": \"not_quantified\"\
    ,\n    \"source_value\": null,\n    \"source_unit\": null,\n    \"source_snippet\"\
    : \"metal solution (\",\n    \"source_stage\": \"preparation or culture pH control\"\
    ,\n    \"basis\": \"No explicit stock final volume is printed in the full Methods.\
    \ Do not infer1L from agreement with the historical molar values.\",\n    \"reference\"\
    : \"https://doi.org/10.1099/13500872-141-10-2449\",\n    \"locator\": \"p2450\
    \ left column, formulation and culture conditions\",\n    \"action_taken\": \"\
    none\"\n  }\n]"
- assessment_id: grounding
  area: grounding
  topic: Chemical IDs, exact supplied hydrates and MIM coverage
  outcome: concern
  summary: All10 asserted ChEBI IDs are current and labels match; current MIM answers
    agree with all supplied labels. Nevertheless six salt identities omit the paper’s
    hydrates, and generic glucose omits monohydrate context.
  target_ids:
  - CultureMech:007244
  evidence_ids:
  - paper
  - diagnostics
  - mim-index
  - mim-metadata
  - glucose-id-search
  - chebi-17234
  - chebi-23414
  - chebi-26710
  - chebi-31440
  - chebi-31795
  - chebi-32312
  - chebi-32599
  - chebi-3312
  - chebi-34887
  - chebi-35176
  - chebi-53542
  - chebi-62946
  - chebi-63036
  - chebi-75832
  - chebi-75836
  - chebi-86158
  details: Verified hydrate candidates:Mg31795,Ca86158,Zn32312,Cu31440,Ni53542,Fe75836.
    These are source-form candidates, not applied edits or proof every historical
    imported database node used that supplied reagent. Generic glucose17234 remains
    a valid broad identity; record the monohydrate material without inventing a stereochemical/anomeric
    term. The historical database Mg compound row itself combines formulaMgSO4 with
    ChEBI31795; this inconsistency is preserved, not treated as proof the generic
    local32599 term is invalid. Existing secondary links cover glucose,NaCl,ZnSO4,MgSO4,ammonium
    sulfate only.
  metrics:
  - name: primary_coverage
    value: 100
    unit: percent
    denominator: 10
    minimum: 0
    maximum: 100
    definition: 10 of10 target ingredients carry primary ChEBI identifiers; field
      coverage only.
  - name: secondary_coverage
    value: 50
    unit: percent
    denominator: 10
    minimum: 0
    maximum: 100
    definition: 5 of10 target ingredients carry secondary CHEBI-keyed MIM links; field
      coverage only.
  - name: secondary_resolver_agreement
    value: 100
    unit: percent
    denominator: 5
    minimum: 0
    maximum: 100
    definition: 5 of5 existing secondary IDs agree with the current maintained MIM
      answer for their supplied label; not source-form accuracy.
- assessment_id: preparation
  area: completeness
  topic: Trace-stock stage, culture controls and unsupported filtration
  outcome: concern
  summary: The primary separates trace-stock addition from its composition and reports
    culture controls absent from the YAML. Generic0.22µm filtration is not a source-supported
    sterilization method.
  target_ids:
  - CultureMech:007244
  evidence_ids:
  - paper
  - paper-text
  - target
  - batch-owner
  - continuous-owner
  - importer
  - quantity-inventory
  details: Source controls are pH6.0,30°C,1volume air per volume medium per minute
    and dissolved oxygen above60%; acid/base strengths are titrants, not fixed medium
    ingredients. Bioreactor nominal sizes15L batch and7L continuous do not specify
    working batch volumes. Fig5 gives a0.075h−1 dilution rate for the A1560 experiment;
    do not turn it into maximum growth rate or universal cultivation condition. Analysis
    buffers, protein-extraction reagents, sample storage/freezing, gels and assay
    temperatures are outside the growth formulation. No sterilization cycle, storage
    life or maltose feed concentration is invented.
- assessment_id: organisms
  area: evidence
  topic: Existing paper citation and strain-specific scope
  outcome: supported
  summary: Both maintained citations correctly distinguish bibliographic/taxonomic
    evidence from unverified concentration or native growth assertions; the generated
    target omits them. Full text now identifies batch studies of A1560,CF1.1,CF2.1
    and the continuous experiment specifically with A1560.
  target_ids:
  - CultureMech:007244
  evidence_ids:
  - batch-owner
  - continuous-owner
  - paper
  - pubmed
  - taxonomy
  details: A1560 originated from IFO4177; this is ancestry, not a demonstrated interchangeable
    strain or exact taxonomy node. CF1.1 andCF2.1 are distinct experimental strains.
    NCBITaxon5062 verifies the species parent, as the existing references explicitly
    say. Historical database growth links for all three strains on343 cannot be promoted
    to full-text support for all three continuous experiments. Table1 measures alpha-amylase
    quantities/productivity/residence, not organism growth rates. No new native organism
    or growth assertion is made.
- assessment_id: provenance
  area: provenance
  topic: Current merger/importer, historical evidence and append-only history
  outcome: concern
  summary: Current exact-formulation code rejects this parent/child pair; the old
    generated collapse is stale. The importer still supplies generic preparation and
    a bacterial name-based default. Existing paper citations and their scoped limits
    are credited.
  target_ids:
  - CultureMech:007244
  evidence_ids:
  - target
  - batch-owner
  - continuous-owner
  - diagnostics
  - merge-formulation
  - merge-writer
  - importer
  - historical-selection
  - historical-report-1
  - historical-report-2
  - historical-report-3
  - historical-report-4
  - historical-report-5
  - historical-pooled-1
  - historical-pooled-2
  - historical-pooled-3
  details: All five named historical reports and complete relevant objects from three
    pooled reports were read. October9 derivative SQL/live comparisons agree with
    each owner’s numbers; their raw hashes/times are not newly authenticated. The
    September review predates October13 bibliography and current merge safeguards.
    Mazumdar2014 is the MediaDB database-paper attribution, not evidence for this
    formulation; preserve the original import event and distinguish the already-added
    Mørkeberg1995 primary citation. Current source notes point at references_cache
    files absent in the owned checkout after ignored-inclusive filename/exact-path
    checks; freshly retrieved PubMed/PDF evidence can support a future append-only
    access update. Missing local cache is not a broken PMID or proof the old capture
    never existed.
findings:
- finding_id: F1
  issue_key: cm007244-generated-concentration-variant-collapse
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generated continuous identity retains the batch formulation
  description: Target glucose126.2 and ammonium55.24mM are the parent values, while
    the child and source continuous formulation support40.37 and37.84mM. Generated
    output also drops both maintained primary-paper references. Current exact-formulation
    merger rejects this pair; regenerate separate variants after maintained source-form
    review.
  target_ids:
  - CultureMech:007244
  field_paths:
  - ingredients[2].concentration
  - ingredients[9].concentration
  - merged_from
  - variant_modifications
  - references
  evidence_ids:
  - target
  - batch-owner
  - continuous-owner
  - paper
  - quantity-inventory
  - merge-formulation
  - diagnostics
  rule_id: P2.5
  native_severity: P2
  normalization_reason: Material variant-scope and evidence loss; target remains exactly
    resolved, so this is major curation impact rather than an unresolved selector.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: generated merge pipeline
- finding_id: F2
  issue_key: cm007244-supplied-hydrate-provenance-loss
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported identities omit supplied hydrate forms
  description: The primary specifies Mg/Ca/Fe/Zn/Cu/Ni hydrates and glucose monohydrate,
    while local descriptors use anhydrous/generic identities. Matching source-derived
    nominal molarity does not preserve the supplied reagent identity. Reconcile exact
    source forms without swapping arbitrary broader/specific identifiers or recalculating
    molarity using anhydrous mass.
  target_ids:
  - CultureMech:007244
  field_paths:
  - ingredients[*].preferred_term
  - ingredients[*].term
  - ingredients[*].mediaingredientmech_chebi_term
  evidence_ids:
  - paper
  - quantity-inventory
  - diagnostics
  - mim-index
  - chebi-17234
  - chebi-23414
  - chebi-26710
  - chebi-31440
  - chebi-31795
  - chebi-32312
  - chebi-32599
  - chebi-3312
  - chebi-34887
  - chebi-35176
  - chebi-53542
  - chebi-62946
  - chebi-63036
  - chebi-75832
  - chebi-75836
  - chebi-86158
  rule_id: P2.2
  native_severity: P2
  normalization_reason: IDs exist and their labels are correct; normalization is major
    because the recipe-to-supplied-form correspondence is materially wrong or incomplete.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
- finding_id: F3
  issue_key: cm007244-trace-stock-stage-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Trace-stock boundary and dilution basis are missing
  description: Four local final trace molarities correspond to source stock ingredients,
    but no stock descriptor or0.5mL/L receiving dose is represented. The paper supplies
    stock masses without explicit stock final volume; historical database numbers
    cannot independently authenticate that missing denominator.
  target_ids:
  - CultureMech:007244
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - solutions
  evidence_ids:
  - paper
  - quantity-inventory
  - historical-selection
  rule_id: 'concentration evidence contract: stock stages and denominator'
  native_severity: P2
  normalization_reason: Material source-stage and dilution uncertainty; unknown stock
    volume blocks new final-concentration assertions.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
- finding_id: F4
  issue_key: cm007244-culture-context-and-template-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Culture context is missing and filtration is unsupported
  description: Primary pH/temperature/aeration context is omitted, while all three
    records assert a generic0.22µm filtration protocol not supported by the inspected
    full paper. Current importer hard-codes that step. Preserve culture-specific controls
    and distinguish titration from initial formulation.
  target_ids:
  - CultureMech:007244
  field_paths:
  - preparation_steps
  - ph_value
  - temperature_value
  - atmosphere
  evidence_ids:
  - paper
  - target
  - batch-owner
  - continuous-owner
  - importer
  - quantity-inventory
  rule_id: P3.4 / P3.5 / P3.6
  native_severity: P3
  normalization_reason: Elevated to major because unsupported preparation plus missing
    source controls materially changes reproducibility; no generic protocol is supplied.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadb_importer.py
    role: maintained source transform
- finding_id: F5
  issue_key: cm007244-fungal-category-mismatch
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Fungal study records are filed as bacterial
  description: Both owners and generated target carry bacterial classification despite
    the primary Aspergillus oryzae study and verified fungal taxonomy. Current importer
    relies on name keywords and defaults this medium name to bacterial.
  target_ids:
  - CultureMech:007244
  field_paths:
  - category
  - categories
  evidence_ids:
  - paper
  - taxonomy
  - diagnostics
  - importer
  rule_id: P2.4
  native_severity: P2
  normalization_reason: Material organism-category mismatch supported by primary study
    and current taxonomy.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadb_importer.py
    role: maintained source transform
- finding_id: F6
  issue_key: cm007244-secondary-linkage-gaps
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Five current secondary ingredient links are missing
  description: Ferrous sulfate,nickel chloride,calcium chloride,cupric sulfate and
    potassium dihydrogen phosphate lack secondary links despite primary IDs and current
    index answers. Resolve supplied-form scope first, then populate through the maintained
    resolver.
  target_ids:
  - CultureMech:007244
  field_paths:
  - ingredients[*].mediaingredientmech_chebi_term
  evidence_ids:
  - target
  - batch-owner
  - continuous-owner
  - diagnostics
  - mim-index
  rule_id: P3.2
  native_severity: P3
  normalization_reason: Reduced traceability only;50percent secondary linkage does
    not imply50percent scientific accuracy.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
actions:
- action_id: A1
  description: Reconcile the maintained batch/continuous source formulations and supplied
    hydrates with the primary, preserving exact source amount, stock stage and claim-level
    evidence. Recover the trace-stock final-volume basis before certifying its final
    molarities.
  finding_ids:
  - F2
  - F3
  target_ids:
  - CultureMech:007244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Join all30 existing concentration fields to the38 scoped decisions; preserve the
    two variant-specific carbon/nitrogen quantities.
  - Check six hydrate identifiers through current ontology/MIM tools; leave glucose
    stereochemistry unresolved unless independently supported.
  - Preserve the stock mass parenthesis and receiving dose separately; no1L stock
    denominator inferred from rounded database numbers.
  - Run the four native per-owner checks and just check-mim-label-index; append actual
    curation history without rewriting earlier events.
- action_id: A2
  description: Source the culture context and replace unsupported generic preparation
    with bounded evidence-bearing text; maintain the distinction between formulation,
    titrant strength, continuous dilution rate and assay methods.
  finding_ids:
  - F4
  target_ids:
  - CultureMech:007244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadb_importer.py
    role: maintained source transform
  acceptance_checks:
  - Every culture condition cites p2450/Fig5 with strain and experiment scope.
  - No assay/extraction reagent, sample-storage temperature, inferred sterilization
    cycle or unreported maltose strength enters the medium.
  - Review the importer template path so a later import cannot silently reinstate
    unsupported filtration.
- action_id: A3
  description: Correct the maintained fungal category and distinguish existing primary
    citation from database-import attribution; preserve study strain boundaries and
    update access notes append-only.
  finding_ids:
  - F5
  target_ids:
  - CultureMech:007244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadb_importer.py
    role: maintained source transform
  acceptance_checks:
  - Preserve permanent IDs and repair all path references if category relocation is
    used.
  - NCBITaxon5062 remains explicitly a species parent; continuous A1560 evidence is
    not copied to CF1.1/CF2.1.
  - Do not recast alpha-amylase productivity or residence time as organism growth
    metrics.
- action_id: A4
  description: Add missing secondary links only after supplied reagent scope is reconciled.
  finding_ids:
  - F6
  target_ids:
  - CultureMech:007244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Resolve exact chosen labels with the packaged MIM index; compare primary/secondary
    terms and source form.
  - Recompute linkage denominators without treating coverage as scientific accuracy.
  depends_on:
  - A1
- action_id: A5
  description: Regenerate distinct batch and continuous outputs through the current
    conservative pipeline and retain both existing primary-paper references.
  finding_ids:
  - F1
  target_ids:
  - CultureMech:007244
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: generated merge pipeline
  acceptance_checks:
  - Current exact-formulation guard continues to reject collapsing these variants.
  - Generated continuous output preserves its own glucose/ammonium values, fungal
    category, paper evidence and preparation context.
  - Run just verify-merges and just audit-merge-freshness after separately authorized
    regeneration; inspect the exact target and owners again.
  depends_on:
  - A1
  - A2
  - A3
  - A4
  generator: src/culturemech/merge/merge_recipes.py via just merge-recipes
limitations:
- All current exact MediaDB endpoints and versioned export return502. Historical SQL/HTML
  snippets were read as derivative reports; old raw digests, retrieval times and accession
  contents are not newly authenticated.
- The primary full text gives the trace-stock dose and four hydrate masses, but not
  an explicit stock final-volume denominator. Their final trace molarities remain
  unresolved; no density or final-volume assumption is introduced.
- Exact glucose-monohydrate ontology identity and strain-level taxonomy nodes remain
  unresolved. Molecular formula/mass supports arithmetic only; species5062 does not
  certify exact strain identity or interchangeable ancestry.
- Four canonical checks apply to the target; owners/context were read and the extra
  MIM integrity check passed. Full-corpus gates, experiments and scientific record
  changes were not performed.
- Existing references correctly marked their earlier abstract-only scope. New full-text
  access can support a future appended clarification; old history/cache existence
  is not rewritten or inferred.
notes:
- No previous structured finding is closed. Historical recommendations are reassessed
  against current owners and merge safeguards.
- Current primary and secondary labels resolve, but valid identifiers and rounded
  molarity do not establish the correct supplied hydrate or experimental scope.
- Original native inspection and diagnostics are preserved; the additive context inspection
  retained every original input hash.
tags:
- review-only
- batch060
- primary-publication
- quantity-inventory
```
