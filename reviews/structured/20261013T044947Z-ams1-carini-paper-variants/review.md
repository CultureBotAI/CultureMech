# AMS1 Carini 2013 paper, formulation variants and strain evidence

- Review: 20261013T044947Z-ams1-carini-paper-variants
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-13T04:49:42Z
- Finished UTC: 2026-10-13T04:49:47Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Added four paper-record citations (two papers), two study variants and two variant-scoped strain associations; preserved all parent data. The 2014 HMP/contamination evidence qualifies the historical 2013 formulation. KGX scope loss and repository merge failures prevent a publication-ready verdict.

## Scope And Provenance

Focused comparison of both MediaDB source-149 normalized recipes to the 2013 paper's Table 3 glycine/serine assay, including 40 direct ingredient instances and current strain identity.

Selection: Exact tracked owners of MEDIADB475 and MEDIADB477; no name-based cohort expansion.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007382 | data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml | maintained | AMS1 (Pyruvate+Glycine) |
| CultureMech:007384 | data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml | maintained | AMS1 (Pyruvate+Serine) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml | passed | True | CultureMech:007382 | Per-record schema/term/reference checks |
| just validate-strict data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml | passed | True | CultureMech:007382 | Per-record schema/term/reference checks |
| just validate data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml | passed | True | CultureMech:007384 | Per-record schema/term/reference checks |
| just validate-strict data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml | passed | True | CultureMech:007384 | Per-record schema/term/reference checks |
| just verify-merges | failed | True | CultureMech:007382, CultureMech:007384 | Repository-wide merge diagnostic; normalized inputs were not regenerated in place. |
| just audit-merge-freshness --json | failed | True | CultureMech:007382, CultureMech:007384 | Repository-wide merge diagnostic; normalized inputs were not regenerated in place. |
| Primary-source quote and table comparison | passed | True | CultureMech:007382, CultureMech:007384 | Re-read methods and tables, checked all added snippets and labeled row excerpts against normalized HTML text, and retained final-concentration context. |
| Current NCBI strain identity | passed | True | CultureMech:007382, CultureMech:007384 | Scientific name, strain, taxon ID and actual XML rank verified; no HTCC7211 inference from MediaDB. |
| Variant scope in KGX edge builder | failed | True | CultureMech:007382, CultureMech:007384 | Current edge builder drops the variant scope. Publication of these associations remains withheld. |

## Scientific And Domain Assessments

### Study-specific concentration and formulation scope

quantity: supported. Targets: CultureMech:007382.

Seven compound modification statements separate the 2013 assay from the imported parent. Source row excerpts support amounts, salt hydrates and the Table 1 vitamin mixture; arithmetic is not embedded in quotations.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "Pyruvate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:15361",
        "label": "pyruvate"
      },
      "old_amount": {
        "value": "1.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
          "locator": "Materials and methods, Glycine substitution experiments"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Biotin",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:15956",
        "label": "biotin"
      },
      "old_amount": {
        "value": "4e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "B 7 4 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "Sodium bicarbonate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate"
      },
      "old_amount": {
        "value": "6.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NaHCO 3 6 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "4-Amino-5-hydroxymethyl-2-methylpyrimidine",
      "ontology_term_as_recorded_not_reverified": null,
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": "HMP is not listed in the inspected complete 2013 Table 1 vitamin list; omission is not a quantified zero. The 2014 qualification addresses trace contamination.",
      "decision": "unsupported: absent from the complete 2013 Table 1 vitamin list; do not infer a 2013 HMP formulation",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Glycine",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:15428",
        "label": "glycine"
      },
      "old_amount": {
        "value": "0.05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "The positive control was amended with 25 μℳ glycine",
          "locator": "Materials and methods, Glycine substitution experiments; Table 3 identifies serine as a substitute"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:3312",
        "label": "calcium dichloride"
      },
      "old_amount": {
        "value": "10.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "CaCl 2 ·2H 2 O 10 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "Magnesium chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate"
      },
      "old_amount": {
        "value": "27.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "MgCl 2 ·6H 2 O 27 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Nickel chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:34887",
        "label": "nickel dichloride"
      },
      "old_amount": {
        "value": "1e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NiCl 2 ·6H 2 O 1 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "Sodium chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:26710",
        "label": "sodium chloride"
      },
      "old_amount": {
        "value": "481.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NaCl 481 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "Potassium chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:32588",
        "label": "potassium chloride"
      },
      "old_amount": {
        "value": "9.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "KCl 9 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "Iron(III) chloride",
      "ontology_term_as_recorded_not_reverified": null,
      "old_amount": {
        "value": "0.000117",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "FeCl 3 ·6H 2 O 117 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        },
        {
          "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
          "locator": "Materials and methods, Glycine substitution experiments"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "Sodium selenite",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:48843",
        "label": "disodium selenite"
      },
      "old_amount": {
        "value": "1e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "Na 2 SeO 3 1 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "Ammonium sulfate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:62946",
        "label": "ammonium sulfate"
      },
      "old_amount": {
        "value": "0.4",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "(NH 4 ) 2 SO 4 400 μℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "Manganese chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:63041",
        "label": "manganese(II) chloride"
      },
      "old_amount": {
        "value": "9e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "MnCl 2 ·4H 2 O 9 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Sodium molybdate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:75215",
        "label": "sodium molybdate (anhydrous)"
      },
      "old_amount": {
        "value": "3e-07",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "Na 2 MoO 4 ·2H 2 O 300 pM",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "DL-methionine",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:16811",
        "label": "methionine"
      },
      "old_amount": {
        "value": "0.05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
          "locator": "Materials and methods, Glycine substitution experiments"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "Zinc sulfate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:35176",
        "label": "zinc sulfate"
      },
      "old_amount": {
        "value": "8e-07",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "ZnSO 4 ·7H 2 O 800 pM",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Sodium dihydrogen phosphate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:37585",
        "label": "sodium dihydrogenphosphate"
      },
      "old_amount": {
        "value": "0.05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NaH 2 PO 4 (pH 7.5) 50 μℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "Magnesium sulfate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:32599",
        "label": "magnesium sulfate"
      },
      "old_amount": {
        "value": "28.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "MgSO 4 ·7H 2 O 2.8 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Cobalt chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:35696",
        "label": "cobalt dichloride"
      },
      "old_amount": {
        "value": "5e-07",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "CoCl 2 ·6H 2 O 500 pM",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    }
  ],
  "variant_field": "variants[0]",
  "variant_name": "Carini 2013 AMS1 glycine substitution assay",
  "variant_action": "add",
  "old_variant": null,
  "variant_modifications": [
    "Use 50 micromolar pyruvate instead of the parent's 1.0 mM, and 10 micromolar methionine instead of 0.05 mM DL-methionine; the paper does not specify methionine stereochemistry.",
    "Use 25 micromolar glycine instead of the parent's 0.05 mM Glycine; this is the Table 3 assay, not a titration maximum or a universal optimum.",
    "Use magnesium sulfate heptahydrate at 2.8 mM rather than the parent's magnesium sulfate at 28.0 mM. Other unchanged Table 1 base-salt and macronutrient molar amounts remain as reported there.",
    "Use calcium chloride dihydrate, manganese chloride tetrahydrate, zinc sulfate heptahydrate, cobalt chloride hexahydrate, sodium molybdate dihydrate and nickel chloride hexahydrate as specified in Table 1; retain their Table 1 molar amounts rather than infer mass equivalents from the local anhydrous or unspecified forms.",
    "Use iron(III) chloride at 1 micromolar in this assay instead of the parent's 117 nM; Table 1 specifies the hexahydrate and its basal 117 nM is overridden by the assay methods.",
    "Replace the imported biotin/HMP vitamin selection with the complete Table 1 vitamin mixture: B1 6 micromolar, B3 800 nM, B5 425 nM, B6 500 nM, B7 4 nM, B9 4 nM, B12 700 pM, myo-inositol 6 micromolar and 4-aminobenzoic acid 60 nM. Do not substitute HMP for B1 using this 2013 paper.",
    "Follow the paper's AMS1 preparation: autoclave the inorganic medium, establish the bicarbonate buffer by filtered CO2 then air sparging, and add vitamins and organics afterward; this differs from the imported all-ingredient filter-sterilization instruction. The reported resulting pH is 7.5-7.7, not an independently optimized value."
  ],
  "variant_source_evidence": [
    {
      "reference": "doi:10.1038/ismej.2012.122",
      "supports": "SUPPORT",
      "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
      "explanation": "Locator: Materials and methods, Glycine substitution experiments, with Table 1 (Compound / Final concentration) and Media preparation. Supports only this inline variant's modifications, never replacement of the parent's ingredients. The immediately preceding methods phrase is 'at a concentration of 25 μℳ'. Table 1 row: 'CaCl 2 ·2H 2 O 10 mℳ'; Table 1 row: 'MgSO 4 ·7H 2 O 2.8 mℳ'; Table 1 row: 'FeCl 3 ·6H 2 O 117 nℳ'; Table 1 row: 'MnCl 2 ·4H 2 O 9 nℳ'; Table 1 row: 'ZnSO 4 ·7H 2 O 800 pM'; Table 1 row: 'CoCl 2 ·6H 2 O 500 pM'; Table 1 row: 'Na 2 MoO 4 ·2H 2 O 300 pM'; Table 1 row: 'NiCl 2 ·6H 2 O 1 nℳ'; Table 1 row: 'B 1 6 μℳ'; Table 1 row: 'B 3 800 nℳ'; Table 1 row: 'B 5 425 nℳ'; Table 1 row: 'B 6 500 nℳ'; Table 1 row: 'B 7 4 nℳ'; Table 1 row: 'B 9 4 nℳ'; Table 1 row: 'B 12 700 pM'; Table 1 row: 'Myo-inositol 6 μℳ'; Table 1 row: '4-Aminobenzoic acid 60 nℳ'. The B-number names are retained as published; no molecular-weight conversion, unreported salt identity or stock dilution was inferred. Amounts are final assay concentrations. The paper's Table 1 excludes the reduced-sulfur, glycine and pyruvate additions, which the assay methods supply. Media preparation separately places vitamins/organics after autoclaving and sparging."
    }
  ],
  "historical_qualification": "Published AMS1 formulation used in the glycine substitution experiment, glycine positive-control condition. This is not an assertion that the imported MediaDB parent matches the paper. Composite concentration, vitamin, chemical-form and preparation changes; methionine and serine stereochemistry is not specified in the inspected methods. Historical 2013 assay formulation, not evidence that thiamin substitutes for HMP: Carini et al. 2014 (doi:10.1038/ismej.2014.61) found an HMP requirement and HMP contamination in their thiamin stock. Trace HMP in the 2013 batches was not quantified by the inspected 2013 paper; do not interpret nominal absence of added HMP as HMP-independent growth."
}

### Strain-specific, variant-only cultivation evidence

grounding: supported. Targets: CultureMech:007382.

Table 3 positive cell yield supports HTCC1062 only on the named study variant. Exact strain grounding is NCBITaxon335992; no HTCC7211 or parent-medium growth assertion is added.

### Study-specific concentration and formulation scope

quantity: supported. Targets: CultureMech:007384.

Seven compound modification statements separate the 2013 assay from the imported parent. Source row excerpts support amounts, salt hydrates and the Table 1 vitamin mixture; arithmetic is not embedded in quotations.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "4-Amino-5-hydroxymethyl-2-methylpyrimidine",
      "ontology_term_as_recorded_not_reverified": null,
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": "HMP is not listed in the inspected complete 2013 Table 1 vitamin list; omission is not a quantified zero. The 2014 qualification addresses trace contamination.",
      "decision": "unsupported: absent from the complete 2013 Table 1 vitamin list; do not infer a 2013 HMP formulation",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Pyruvate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:15361",
        "label": "pyruvate"
      },
      "old_amount": {
        "value": "1.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
          "locator": "Materials and methods, Glycine substitution experiments"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "Biotin",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:15956",
        "label": "biotin"
      },
      "old_amount": {
        "value": "4e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "B 7 4 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "Nickel chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:34887",
        "label": "nickel dichloride"
      },
      "old_amount": {
        "value": "1e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NiCl 2 ·6H 2 O 1 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Magnesium chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate"
      },
      "old_amount": {
        "value": "27.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "MgCl 2 ·6H 2 O 27 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "L-Serine",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:17115",
        "label": "L-serine"
      },
      "old_amount": {
        "value": "0.05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "Each substitute was tested at a concentration of 25 μℳ",
          "locator": "Materials and methods, Glycine substitution experiments; Table 3 identifies serine as a substitute"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "Sodium bicarbonate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate"
      },
      "old_amount": {
        "value": "6.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NaHCO 3 6 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:3312",
        "label": "calcium dichloride"
      },
      "old_amount": {
        "value": "10.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "CaCl 2 ·2H 2 O 10 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "Sodium molybdate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:75215",
        "label": "sodium molybdate (anhydrous)"
      },
      "old_amount": {
        "value": "3e-07",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "Na 2 MoO 4 ·2H 2 O 300 pM",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "Magnesium sulfate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:32599",
        "label": "magnesium sulfate"
      },
      "old_amount": {
        "value": "28.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "MgSO 4 ·7H 2 O 2.8 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "DL-methionine",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:16811",
        "label": "methionine"
      },
      "old_amount": {
        "value": "0.05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
          "locator": "Materials and methods, Glycine substitution experiments"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "Sodium selenite",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:48843",
        "label": "disodium selenite"
      },
      "old_amount": {
        "value": "1e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "Na 2 SeO 3 1 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "Potassium chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:32588",
        "label": "potassium chloride"
      },
      "old_amount": {
        "value": "9.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "KCl 9 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "Cobalt chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:35696",
        "label": "cobalt dichloride"
      },
      "old_amount": {
        "value": "5e-07",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "CoCl 2 ·6H 2 O 500 pM",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Sodium chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:26710",
        "label": "sodium chloride"
      },
      "old_amount": {
        "value": "481.0",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NaCl 481 mℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "Sodium dihydrogen phosphate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:37585",
        "label": "sodium dihydrogenphosphate"
      },
      "old_amount": {
        "value": "0.05",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "NaH 2 PO 4 (pH 7.5) 50 μℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "Ammonium sulfate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:62946",
        "label": "ammonium sulfate"
      },
      "old_amount": {
        "value": "0.4",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "(NH 4 ) 2 SO 4 400 μℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Manganese chloride",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:63041",
        "label": "manganese(II) chloride"
      },
      "old_amount": {
        "value": "9e-06",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "MnCl 2 ·4H 2 O 9 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "Zinc sulfate",
      "ontology_term_as_recorded_not_reverified": {
        "id": "CHEBI:35176",
        "label": "zinc sulfate"
      },
      "old_amount": {
        "value": "8e-07",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "ZnSO 4 ·7H 2 O 800 pM",
          "locator": "Table 1, Compound / Final concentration"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "evidence_only comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent recipe identity are not certified",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Iron(III) chloride",
      "ontology_term_as_recorded_not_reverified": null,
      "old_amount": {
        "value": "0.000117",
        "unit": "MILLIMOLAR"
      },
      "proposed_parent_amount": null,
      "source_reference": "doi:10.1038/ismej.2012.122",
      "source_excerpts": [
        {
          "snippet": "FeCl 3 ·6H 2 O 117 nℳ",
          "locator": "Table 1, Compound / Final concentration"
        },
        {
          "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
          "locator": "Materials and methods, Glycine substitution experiments"
        }
      ],
      "source_basis": "Table 1 final concentration; explicit Table 3 assay additions override basal FeCl3",
      "parent_basis": "Imported molar concentration; exact correspondence to this paper not established",
      "calculation": "Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.",
      "missing_source_detail": null,
      "decision": "conflict: local amount differs from the specifically reviewed Table 3 assay; retain parent and represent study variant",
      "action_taken": "Parent retained unchanged; differences represented only in the study variant."
    }
  ],
  "variant_field": "variants[0]",
  "variant_name": "Carini 2013 AMS1 serine substitution assay",
  "variant_action": "add",
  "old_variant": null,
  "variant_modifications": [
    "Use 50 micromolar pyruvate instead of the parent's 1.0 mM, and 10 micromolar methionine instead of 0.05 mM DL-methionine; the paper does not specify methionine stereochemistry.",
    "Use 25 micromolar serine instead of the parent's 0.05 mM L-Serine; this is the Table 3 assay, not a titration maximum or a universal optimum.",
    "Use magnesium sulfate heptahydrate at 2.8 mM rather than the parent's magnesium sulfate at 28.0 mM. Other unchanged Table 1 base-salt and macronutrient molar amounts remain as reported there.",
    "Use calcium chloride dihydrate, manganese chloride tetrahydrate, zinc sulfate heptahydrate, cobalt chloride hexahydrate, sodium molybdate dihydrate and nickel chloride hexahydrate as specified in Table 1; retain their Table 1 molar amounts rather than infer mass equivalents from the local anhydrous or unspecified forms.",
    "Use iron(III) chloride at 1 micromolar in this assay instead of the parent's 117 nM; Table 1 specifies the hexahydrate and its basal 117 nM is overridden by the assay methods.",
    "Replace the imported biotin/HMP vitamin selection with the complete Table 1 vitamin mixture: B1 6 micromolar, B3 800 nM, B5 425 nM, B6 500 nM, B7 4 nM, B9 4 nM, B12 700 pM, myo-inositol 6 micromolar and 4-aminobenzoic acid 60 nM. Do not substitute HMP for B1 using this 2013 paper.",
    "Follow the paper's AMS1 preparation: autoclave the inorganic medium, establish the bicarbonate buffer by filtered CO2 then air sparging, and add vitamins and organics afterward; this differs from the imported all-ingredient filter-sterilization instruction. The reported resulting pH is 7.5-7.7, not an independently optimized value."
  ],
  "variant_source_evidence": [
    {
      "reference": "doi:10.1038/ismej.2012.122",
      "supports": "SUPPORT",
      "snippet": "pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.",
      "explanation": "Locator: Materials and methods, Glycine substitution experiments, with Table 1 (Compound / Final concentration) and Media preparation. Supports only this inline variant's modifications, never replacement of the parent's ingredients. The immediately preceding methods phrase is 'at a concentration of 25 μℳ'. Table 1 row: 'CaCl 2 ·2H 2 O 10 mℳ'; Table 1 row: 'MgSO 4 ·7H 2 O 2.8 mℳ'; Table 1 row: 'FeCl 3 ·6H 2 O 117 nℳ'; Table 1 row: 'MnCl 2 ·4H 2 O 9 nℳ'; Table 1 row: 'ZnSO 4 ·7H 2 O 800 pM'; Table 1 row: 'CoCl 2 ·6H 2 O 500 pM'; Table 1 row: 'Na 2 MoO 4 ·2H 2 O 300 pM'; Table 1 row: 'NiCl 2 ·6H 2 O 1 nℳ'; Table 1 row: 'B 1 6 μℳ'; Table 1 row: 'B 3 800 nℳ'; Table 1 row: 'B 5 425 nℳ'; Table 1 row: 'B 6 500 nℳ'; Table 1 row: 'B 7 4 nℳ'; Table 1 row: 'B 9 4 nℳ'; Table 1 row: 'B 12 700 pM'; Table 1 row: 'Myo-inositol 6 μℳ'; Table 1 row: '4-Aminobenzoic acid 60 nℳ'. The B-number names are retained as published; no molecular-weight conversion, unreported salt identity or stock dilution was inferred. Amounts are final assay concentrations. The paper's Table 1 excludes the reduced-sulfur, glycine and pyruvate additions, which the assay methods supply. Media preparation separately places vitamins/organics after autoclaving and sparging."
    }
  ],
  "historical_qualification": "Published AMS1 formulation used in the glycine substitution experiment, serine test condition. This is not an assertion that the imported MediaDB parent matches the paper. Composite concentration, vitamin, chemical-form and preparation changes; methionine and serine stereochemistry is not specified in the inspected methods. Historical 2013 assay formulation, not evidence that thiamin substitutes for HMP: Carini et al. 2014 (doi:10.1038/ismej.2014.61) found an HMP requirement and HMP contamination in their thiamin stock. Trace HMP in the 2013 batches was not quantified by the inspected 2013 paper; do not interpret nominal absence of added HMP as HMP-independent growth."
}

### Strain-specific, variant-only cultivation evidence

grounding: supported. Targets: CultureMech:007384.

Table 3 positive cell yield supports HTCC1062 only on the named study variant. Exact strain grounding is NCBITaxon335992; no HTCC7211 or parent-medium growth assertion is added.

### Subsequent evidence limits interpretation of the 2013 recipe

evidence: supported. Targets: CultureMech:007382, CultureMech:007384.

Both variant descriptions and organism-evidence explanations preserve the HMP caveat; neither base recipe is changed. The 2014 citation is a qualification, not a new positive growth edge or a formal correction notice.

### KGX variant-scope preservation

graph: concern. Targets: CultureMech:007382, CultureMech:007384.

The current exporter cannot safely publish these two variant-only growth associations.

## Findings

### variant-export: KGX drops the new study-variant scope

major / open / confirmed; issue key: kgx-variant-growth-scope-loss-ams1-carini2013.

The YAML correctly scopes HTCC1062 growth to a named inline variant, but the exporter's parent-medium edge path ignores scoped_to_variant. Withholding this turn's export prevents publication but does not repair the exporter.

## Recommended Actions And Acceptance Checks

### guard-variant-export

Before publishing these associations, represent variant targets faithfully or fail closed for scoped_to_variant in the maintained KGX exporter.

- Regression test proves neither AMS1 parent receives the study-variant growth edge.
- Tests cover other variant-scoped organisms and ordinary unscoped growth without suppressing valid edges.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| paper | doi:10.1038/ismej.2012.122; PMC3578571, Materials and methods (Media preparation; Glycine substitution experiments; Organism source), Tables 1 and 3; references_cache/papers/primary_html/carini-2013-pmc.html | supports | Inspected full HTML and table-preserving Markdown. Supports the named study variants, not identity of the imported parent recipes. PMC issue date 2013 and PubMed PMID23096402/DOI/title/authors agree; PubMed has no correction/retraction notice. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=335992; Archived NCBI Taxonomy XML, TaxId 335992, ScientificName, Rank and LineageEx | supports | Exact strain match: Candidatus Pelagibacter ubique HTCC1062, rank strain in current XML. Species ancestor is Candidatus Pelagibacter communis, NCBITaxon198252. Browser legacy no-rank wording is not substituted for current XML rank. |
| records | CultureMech:007382; CultureMech:007384; Exact normalized paths and SHA-256 inputs in source; parent ingredients and additions compared with carini-2013-applied.json | context_only | Both parents retain all 20 direct ingredients, preparation and earlier history. Each adds two DOI bibliography entries, one inline study variant and one variant-scoped organism. The second citation qualifies historical vitamin interpretation. No nested or standalone stock is present in either target. |
| followup | doi:10.1038/ismej.2014.61; PMC4817611, Abstract; Organism source and cultivation details; Discussion thiamin-stock contamination paragraph | partial | The 2014 follow-up supports an HMP requirement and reports HMP contamination in thiamin stock. The 2013 nominal formulation is retained as historical experimental evidence, never as proof of HMP-independent growth or thiamin utilization. The 2014 assays used oxaloacetate and different vitamin/treatment conditions, so they are not asserted as parent-medium growth. |
| exporter | src/culturemech/export/kgx_export.py; transform (organism loop) and organism_grows_in_medium_edge; in-memory call on curated CultureMech007382 | refutes | The edge builder used the parent medium ID despite scoped_to_variant. In-memory reproduction emitted object CultureMech007382. No export file was written and no edges were published. |
| gate-0 | reports/paper_citation_curation/20261013-mediadb/carini-glycine-validate.log; Complete retained command output | context_only | Actual exit code 0; deterministic validation, not scientific approval. |
| gate-1 | reports/paper_citation_curation/20261013-mediadb/carini-glycine-validate-strict.log; Complete retained command output | context_only | Actual exit code 0; deterministic validation, not scientific approval. |
| gate-2 | reports/paper_citation_curation/20261013-mediadb/carini-serine-validate.log; Complete retained command output | context_only | Actual exit code 0; deterministic validation, not scientific approval. |
| gate-3 | reports/paper_citation_curation/20261013-mediadb/carini-serine-validate-strict.log; Complete retained command output | context_only | Actual exit code 0; deterministic validation, not scientific approval. |
| gate-4 | reports/paper_citation_curation/20261013-mediadb/verify-merges.log; Complete retained command output | context_only | Actual exit code 1; deterministic validation, not scientific approval. |
| gate-5 | reports/paper_citation_curation/20261013-mediadb/audit-merge-freshness.log; Complete retained command output | context_only | Actual exit code 1; deterministic validation, not scientific approval. |

## Limits And Additional Notes

- This is a focused paper/formulation assessment, not a full record or whole-corpus scientific review.
- All parent concentrations remain unchanged and are not certified as the 2013 formulation. Ingredient ontology grounding outside the reported hydrate comparison was not reassessed.
- Methionine and serine stereochemistry is not specified by the inspected methods; no stereochemical identity or molecular-weight conversion was invented.
- External supplements, unrelated organism mentions and other substitution assays were not exhaustively reviewed.
- No KGX output, rendered page or regenerated merged record was published. Current exporter scope loss requires separate repair before publication.
- Merge diagnostics cover the existing corpus; these checks do not establish an untouched baseline for every global drift difference.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T044947Z-ams1-carini-paper-variants
kind: batch
repository: culturebotai/CultureMech
title: AMS1 Carini 2013 paper, formulation variants and strain evidence
started_at: '2026-10-13T04:49:42Z'
finished_at: '2026-10-13T04:49:47Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same agent curated and checked these two records; no independent
    adversarial reviewer is claimed.
skill: culturemech-add-paper-citation; review-ingredient-concentrations evidence contract
completion: partial
verdict: needs_curation
scientific_review: true
summary: Added four paper-record citations (two papers), two study variants and two
  variant-scoped strain associations; preserved all parent data. The 2014 HMP/contamination
  evidence qualifies the historical 2013 formulation. KGX scope loss and repository
  merge failures prevent a publication-ready verdict.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
    sha256: 2f3755a57cf3a1daa6ff1adb12467300d5149beec89cc04f93f50bfc9d796fdb
    role: target
  - path: data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
    sha256: 1033a43ff2f5dc484bdc5f8592a6baffb401bb68e317e2d1b09da88e55834833
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Focused comparison of both MediaDB source-149 normalized recipes to
    the 2013 paper's Table 3 glycine/serine assay, including 40 direct ingredient
    instances and current strain identity.
  selection: Exact tracked owners of MEDIADB475 and MEDIADB477; no name-based cohort
    expansion.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - CultureMech:007382
  - CultureMech:007384
  exclusions:
  - target: Other CultureMech records and other study substitutions
    reason: Not part of this bounded scientific assessment.
targets:
- target_id: CultureMech:007382
  path: data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
  label: AMS1 (Pyruvate+Glycine)
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; generated merges and pages are
    not curation owners.
- target_id: CultureMech:007384
  path: data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
  label: AMS1 (Pyruvate+Serine)
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; generated merges and pages are
    not curation owners.
checks:
- check_id: gate-0
  name: just validate data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
  status: passed
  required: true
  summary: Per-record schema/term/reference checks
  command: just validate data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
  exit_code: 0
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - gate-0
- check_id: gate-1
  name: just validate-strict data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
  status: passed
  required: true
  summary: Per-record schema/term/reference checks
  command: just validate-strict data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml
  exit_code: 0
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - gate-1
- check_id: gate-2
  name: just validate data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
  status: passed
  required: true
  summary: Per-record schema/term/reference checks
  command: just validate data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
  exit_code: 0
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - gate-2
- check_id: gate-3
  name: just validate-strict data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
  status: passed
  required: true
  summary: Per-record schema/term/reference checks
  command: just validate-strict data/normalized_yaml/bacterial/ams1_pyruvate_serine.yaml
  exit_code: 0
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - gate-3
- check_id: gate-4
  name: just verify-merges
  status: failed
  required: true
  summary: Repository-wide merge diagnostic; normalized inputs were not regenerated
    in place.
  command: just verify-merges
  exit_code: 1
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - gate-4
- check_id: gate-5
  name: just audit-merge-freshness --json
  status: failed
  required: true
  summary: Repository-wide merge diagnostic; normalized inputs were not regenerated
    in place.
  command: just audit-merge-freshness --json
  exit_code: 1
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - gate-5
- check_id: quotes
  name: Primary-source quote and table comparison
  status: passed
  required: true
  summary: Re-read methods and tables, checked all added snippets and labeled row
    excerpts against normalized HTML text, and retained final-concentration context.
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - paper
- check_id: taxonomy-check
  name: Current NCBI strain identity
  status: passed
  required: true
  summary: Scientific name, strain, taxon ID and actual XML rank verified; no HTCC7211
    inference from MediaDB.
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - taxonomy
- check_id: export-scope
  name: Variant scope in KGX edge builder
  status: failed
  required: true
  summary: Current edge builder drops the variant scope. Publication of these associations
    remains withheld.
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - exporter
evidence:
- evidence_id: paper
  kind: primary_source
  reference: doi:10.1038/ismej.2012.122
  locator: PMC3578571, Materials and methods (Media preparation; Glycine substitution
    experiments; Organism source), Tables 1 and 3; references_cache/papers/primary_html/carini-2013-pmc.html
  accessed_at: '2026-10-13T04:49:46Z'
  support: supports
  snapshot_sha256: 9e0ca0cdc0fc0c3a6a3d5e38328903cda00d8a227711cf511b2fabeb6b12a9b9
  summary: Inspected full HTML and table-preserving Markdown. Supports the named study
    variants, not identity of the imported parent recipes. PMC issue date 2013 and
    PubMed PMID23096402/DOI/title/authors agree; PubMed has no correction/retraction
    notice.
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=335992
  locator: Archived NCBI Taxonomy XML, TaxId 335992, ScientificName, Rank and LineageEx
  accessed_at: '2026-10-13T04:49:46Z'
  support: supports
  snapshot_sha256: f9b6832625193d78c32e112d254e4e2389c4fab30f8aae38a4c57d96424d4491
  summary: 'Exact strain match: Candidatus Pelagibacter ubique HTCC1062, rank strain
    in current XML. Species ancestor is Candidatus Pelagibacter communis, NCBITaxon198252.
    Browser legacy no-rank wording is not substituted for current XML rank.'
- evidence_id: records
  kind: record_content
  reference: CultureMech:007382; CultureMech:007384
  locator: Exact normalized paths and SHA-256 inputs in source; parent ingredients
    and additions compared with carini-2013-applied.json
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  summary: Both parents retain all 20 direct ingredients, preparation and earlier
    history. Each adds two DOI bibliography entries, one inline study variant and
    one variant-scoped organism. The second citation qualifies historical vitamin
    interpretation. No nested or standalone stock is present in either target.
- evidence_id: followup
  kind: primary_source
  reference: doi:10.1038/ismej.2014.61
  locator: PMC4817611, Abstract; Organism source and cultivation details; Discussion
    thiamin-stock contamination paragraph
  accessed_at: '2026-10-13T04:49:46Z'
  support: partial
  snapshot_sha256: 5f4a13fba8d5682ffe44c5b21b237bb5fe98a552e522ef224eb52a5681691c16
  summary: The 2014 follow-up supports an HMP requirement and reports HMP contamination
    in thiamin stock. The 2013 nominal formulation is retained as historical experimental
    evidence, never as proof of HMP-independent growth or thiamin utilization. The
    2014 assays used oxaloacetate and different vitamin/treatment conditions, so they
    are not asserted as parent-medium growth.
- evidence_id: exporter
  kind: record_content
  reference: src/culturemech/export/kgx_export.py
  locator: transform (organism loop) and organism_grows_in_medium_edge; in-memory
    call on curated CultureMech007382
  accessed_at: '2026-10-13T04:49:46Z'
  support: refutes
  summary: The edge builder used the parent medium ID despite scoped_to_variant. In-memory
    reproduction emitted object CultureMech007382. No export file was written and
    no edges were published.
- evidence_id: gate-0
  kind: validation
  reference: reports/paper_citation_curation/20261013-mediadb/carini-glycine-validate.log
  locator: Complete retained command output
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  snapshot_sha256: 97210591a6bbc8db2524eff3b29c93c1400c4f52c99a24862ed2904238d9606d
  summary: Actual exit code 0; deterministic validation, not scientific approval.
- evidence_id: gate-1
  kind: validation
  reference: reports/paper_citation_curation/20261013-mediadb/carini-glycine-validate-strict.log
  locator: Complete retained command output
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; deterministic validation, not scientific approval.
- evidence_id: gate-2
  kind: validation
  reference: reports/paper_citation_curation/20261013-mediadb/carini-serine-validate.log
  locator: Complete retained command output
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  snapshot_sha256: 97210591a6bbc8db2524eff3b29c93c1400c4f52c99a24862ed2904238d9606d
  summary: Actual exit code 0; deterministic validation, not scientific approval.
- evidence_id: gate-3
  kind: validation
  reference: reports/paper_citation_curation/20261013-mediadb/carini-serine-validate-strict.log
  locator: Complete retained command output
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; deterministic validation, not scientific approval.
- evidence_id: gate-4
  kind: validation
  reference: reports/paper_citation_curation/20261013-mediadb/verify-merges.log
  locator: Complete retained command output
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
  summary: Actual exit code 1; deterministic validation, not scientific approval.
- evidence_id: gate-5
  kind: validation
  reference: reports/paper_citation_curation/20261013-mediadb/audit-merge-freshness.log
  locator: Complete retained command output
  accessed_at: '2026-10-13T04:49:46Z'
  support: context_only
  snapshot_sha256: 753b9951421bf2b31b2d98979971ecf0860c3570d39877cd541601c047bc3777
  summary: Actual exit code 1; deterministic validation, not scientific approval.
assessments:
- assessment_id: variant-007382
  area: quantity
  topic: Study-specific concentration and formulation scope
  outcome: supported
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - paper
  - records
  summary: Seven compound modification statements separate the 2013 assay from the
    imported parent. Source row excerpts support amounts, salt hydrates and the Table
    1 vitamin mixture; arithmetic is not embedded in quotations.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"Pyruvate\",\n   \
    \   \"ontology_term_as_recorded_not_reverified\": {\n        \"id\": \"CHEBI:15361\"\
    ,\n        \"label\": \"pyruvate\"\n      },\n      \"old_amount\": {\n      \
    \  \"value\": \"1.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\"\
    : null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"\
    source_excerpts\": [\n        {\n          \"snippet\": \"pyruvate (50 μℳ), methionine\
    \ (10 μℳ), FeCl 3 (1 μℳ) and vitamins.\",\n          \"locator\": \"Materials\
    \ and methods, Glycine substitution experiments\"\n        }\n      ],\n     \
    \ \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay additions\
    \ override basal FeCl3\",\n      \"parent_basis\": \"Imported molar concentration;\
    \ exact correspondence to this paper not established\",\n      \"calculation\"\
    : \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass\
    \ or stock conversion, and no parent amount rewritten.\",\n      \"missing_source_detail\"\
    : null,\n      \"decision\": \"conflict: local amount differs from the specifically\
    \ reviewed Table 3 assay; retain parent and represent study variant\",\n     \
    \ \"action_taken\": \"Parent retained unchanged; differences represented only\
    \ in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"Biotin\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:15956\",\n        \"label\": \"biotin\"\n      },\n\
    \      \"old_amount\": {\n        \"value\": \"4e-06\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"B 7 4 nℳ\",\n          \"locator\": \"Table 1, Compound\
    \ / Final concentration\"\n        }\n      ],\n      \"source_basis\": \"Table\
    \ 1 final concentration; explicit Table 3 assay additions override basal FeCl3\"\
    ,\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[2].concentration\"\
    ,\n      \"ingredient\": \"Sodium bicarbonate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:32139\",\n        \"label\": \"sodium hydrogencarbonate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"6.0\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NaHCO 3 6 mℳ\",\n          \"locator\"\
    : \"Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[3].concentration\"\
    ,\n      \"ingredient\": \"4-Amino-5-hydroxymethyl-2-methylpyrimidine\",\n   \
    \   \"ontology_term_as_recorded_not_reverified\": null,\n      \"old_amount\"\
    : {\n        \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n\
    \      \"proposed_parent_amount\": null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\"\
    ,\n      \"source_excerpts\": [],\n      \"source_basis\": \"Table 1 final concentration;\
    \ explicit Table 3 assay additions override basal FeCl3\",\n      \"parent_basis\"\
    : \"Imported molar concentration; exact correspondence to this paper not established\"\
    ,\n      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000\
    \ nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": \"HMP is not listed in the inspected complete\
    \ 2013 Table 1 vitamin list; omission is not a quantified zero. The 2014 qualification\
    \ addresses trace contamination.\",\n      \"decision\": \"unsupported: absent\
    \ from the complete 2013 Table 1 vitamin list; do not infer a 2013 HMP formulation\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[4].concentration\"\
    ,\n      \"ingredient\": \"Glycine\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:15428\",\n        \"label\": \"glycine\"\n      },\n\
    \      \"old_amount\": {\n        \"value\": \"0.05\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"The positive control was amended with 25 μℳ glycine\"\
    ,\n          \"locator\": \"Materials and methods, Glycine substitution experiments;\
    \ Table 3 identifies serine as a substitute\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"conflict: local amount differs from the specifically reviewed\
    \ Table 3 assay; retain parent and represent study variant\",\n      \"action_taken\"\
    : \"Parent retained unchanged; differences represented only in the study variant.\"\
    \n    },\n    {\n      \"field_path\": \"ingredients[5].concentration\",\n   \
    \   \"ingredient\": \"Calcium chloride anhydrous\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:3312\",\n        \"label\": \"calcium dichloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"10.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"CaCl 2 ·2H 2 O 10 mℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[6].concentration\",\n      \"ingredient\"\
    : \"Magnesium chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:86345\",\n        \"label\": \"magnesium dichloride\
    \ hexahydrate\"\n      },\n      \"old_amount\": {\n        \"value\": \"27.0\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\"\
    : null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"\
    source_excerpts\": [\n        {\n          \"snippet\": \"MgCl 2 ·6H 2 O 27 mℳ\"\
    ,\n          \"locator\": \"Table 1, Compound / Final concentration\"\n      \
    \  }\n      ],\n      \"source_basis\": \"Table 1 final concentration; explicit\
    \ Table 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"\
    Imported molar concentration; exact correspondence to this paper not established\"\
    ,\n      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000\
    \ nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[7].concentration\",\n      \"ingredient\"\
    : \"Nickel chloride\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:34887\",\n        \"label\": \"nickel dichloride\"\n\
    \      },\n      \"old_amount\": {\n        \"value\": \"1e-06\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NiCl 2 ·6H 2 O 1 nℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[8].concentration\",\n      \"ingredient\"\
    : \"Sodium chloride\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:26710\",\n        \"label\": \"sodium chloride\"\n  \
    \    },\n      \"old_amount\": {\n        \"value\": \"481.0\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NaCl 481 mℳ\",\n          \"locator\"\
    : \"Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[9].concentration\"\
    ,\n      \"ingredient\": \"Potassium chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:32588\",\n        \"label\": \"potassium chloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"9.0\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"KCl 9 mℳ\",\n          \"locator\": \"\
    Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[10].concentration\"\
    ,\n      \"ingredient\": \"Iron(III) chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : null,\n      \"old_amount\": {\n        \"value\": \"0.000117\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"FeCl 3 ·6H 2 O 117 nℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        },\n        {\n\
    \          \"snippet\": \"pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ)\
    \ and vitamins.\",\n          \"locator\": \"Materials and methods, Glycine substitution\
    \ experiments\"\n        }\n      ],\n      \"source_basis\": \"Table 1 final\
    \ concentration; explicit Table 3 assay additions override basal FeCl3\",\n  \
    \    \"parent_basis\": \"Imported molar concentration; exact correspondence to\
    \ this paper not established\",\n      \"calculation\": \"Comparison only; 1 mM\
    \ = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"conflict: local amount differs from the specifically reviewed\
    \ Table 3 assay; retain parent and represent study variant\",\n      \"action_taken\"\
    : \"Parent retained unchanged; differences represented only in the study variant.\"\
    \n    },\n    {\n      \"field_path\": \"ingredients[11].concentration\",\n  \
    \    \"ingredient\": \"Sodium selenite\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:48843\",\n        \"label\": \"disodium selenite\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"1e-06\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"Na 2 SeO 3 1 nℳ\",\n          \"locator\"\
    : \"Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"Ammonium sulfate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:62946\",\n        \"label\": \"ammonium sulfate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"0.4\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"(NH 4 ) 2 SO 4 400 μℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[13].concentration\",\n      \"ingredient\"\
    : \"Manganese chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:63041\",\n        \"label\": \"manganese(II) chloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"9e-06\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"MnCl 2 ·4H 2 O 9 nℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[14].concentration\",\n      \"ingredient\"\
    : \"Sodium molybdate\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:75215\",\n        \"label\": \"sodium molybdate (anhydrous)\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"3e-07\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"Na 2 MoO 4 ·2H 2 O 300 pM\",\n      \
    \    \"locator\": \"Table 1, Compound / Final concentration\"\n        }\n   \
    \   ],\n      \"source_basis\": \"Table 1 final concentration; explicit Table\
    \ 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"Imported\
    \ molar concentration; exact correspondence to this paper not established\",\n\
    \      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM\
    \ = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[15].concentration\",\n      \"ingredient\"\
    : \"DL-methionine\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:16811\",\n        \"label\": \"methionine\"\n      },\n\
    \      \"old_amount\": {\n        \"value\": \"0.05\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and\
    \ vitamins.\",\n          \"locator\": \"Materials and methods, Glycine substitution\
    \ experiments\"\n        }\n      ],\n      \"source_basis\": \"Table 1 final\
    \ concentration; explicit Table 3 assay additions override basal FeCl3\",\n  \
    \    \"parent_basis\": \"Imported molar concentration; exact correspondence to\
    \ this paper not established\",\n      \"calculation\": \"Comparison only; 1 mM\
    \ = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"conflict: local amount differs from the specifically reviewed\
    \ Table 3 assay; retain parent and represent study variant\",\n      \"action_taken\"\
    : \"Parent retained unchanged; differences represented only in the study variant.\"\
    \n    },\n    {\n      \"field_path\": \"ingredients[16].concentration\",\n  \
    \    \"ingredient\": \"Zinc sulfate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:35176\",\n        \"label\": \"zinc sulfate\"\n \
    \     },\n      \"old_amount\": {\n        \"value\": \"8e-07\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"ZnSO 4 ·7H 2 O 800 pM\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[17].concentration\",\n      \"ingredient\"\
    : \"Sodium dihydrogen phosphate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:37585\",\n        \"label\": \"sodium dihydrogenphosphate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"0.05\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NaH 2 PO 4 (pH 7.5) 50 μℳ\",\n      \
    \    \"locator\": \"Table 1, Compound / Final concentration\"\n        }\n   \
    \   ],\n      \"source_basis\": \"Table 1 final concentration; explicit Table\
    \ 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"Imported\
    \ molar concentration; exact correspondence to this paper not established\",\n\
    \      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM\
    \ = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[18].concentration\",\n      \"ingredient\"\
    : \"Magnesium sulfate\",\n      \"ontology_term_as_recorded_not_reverified\":\
    \ {\n        \"id\": \"CHEBI:32599\",\n        \"label\": \"magnesium sulfate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"28.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"MgSO 4 ·7H 2 O 2.8 mℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"conflict: local amount differs\
    \ from the specifically reviewed Table 3 assay; retain parent and represent study\
    \ variant\",\n      \"action_taken\": \"Parent retained unchanged; differences\
    \ represented only in the study variant.\"\n    },\n    {\n      \"field_path\"\
    : \"ingredients[19].concentration\",\n      \"ingredient\": \"Cobalt chloride\"\
    ,\n      \"ontology_term_as_recorded_not_reverified\": {\n        \"id\": \"CHEBI:35696\"\
    ,\n        \"label\": \"cobalt dichloride\"\n      },\n      \"old_amount\": {\n\
    \        \"value\": \"5e-07\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n \
    \     \"proposed_parent_amount\": null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\"\
    ,\n      \"source_excerpts\": [\n        {\n          \"snippet\": \"CoCl 2 ·6H\
    \ 2 O 500 pM\",\n          \"locator\": \"Table 1, Compound / Final concentration\"\
    \n        }\n      ],\n      \"source_basis\": \"Table 1 final concentration;\
    \ explicit Table 3 assay additions override basal FeCl3\",\n      \"parent_basis\"\
    : \"Imported molar concentration; exact correspondence to this paper not established\"\
    ,\n      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000\
    \ nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    }\n  ],\n\
    \  \"variant_field\": \"variants[0]\",\n  \"variant_name\": \"Carini 2013 AMS1\
    \ glycine substitution assay\",\n  \"variant_action\": \"add\",\n  \"old_variant\"\
    : null,\n  \"variant_modifications\": [\n    \"Use 50 micromolar pyruvate instead\
    \ of the parent's 1.0 mM, and 10 micromolar methionine instead of 0.05 mM DL-methionine;\
    \ the paper does not specify methionine stereochemistry.\",\n    \"Use 25 micromolar\
    \ glycine instead of the parent's 0.05 mM Glycine; this is the Table 3 assay,\
    \ not a titration maximum or a universal optimum.\",\n    \"Use magnesium sulfate\
    \ heptahydrate at 2.8 mM rather than the parent's magnesium sulfate at 28.0 mM.\
    \ Other unchanged Table 1 base-salt and macronutrient molar amounts remain as\
    \ reported there.\",\n    \"Use calcium chloride dihydrate, manganese chloride\
    \ tetrahydrate, zinc sulfate heptahydrate, cobalt chloride hexahydrate, sodium\
    \ molybdate dihydrate and nickel chloride hexahydrate as specified in Table 1;\
    \ retain their Table 1 molar amounts rather than infer mass equivalents from the\
    \ local anhydrous or unspecified forms.\",\n    \"Use iron(III) chloride at 1\
    \ micromolar in this assay instead of the parent's 117 nM; Table 1 specifies the\
    \ hexahydrate and its basal 117 nM is overridden by the assay methods.\",\n  \
    \  \"Replace the imported biotin/HMP vitamin selection with the complete Table\
    \ 1 vitamin mixture: B1 6 micromolar, B3 800 nM, B5 425 nM, B6 500 nM, B7 4 nM,\
    \ B9 4 nM, B12 700 pM, myo-inositol 6 micromolar and 4-aminobenzoic acid 60 nM.\
    \ Do not substitute HMP for B1 using this 2013 paper.\",\n    \"Follow the paper's\
    \ AMS1 preparation: autoclave the inorganic medium, establish the bicarbonate\
    \ buffer by filtered CO2 then air sparging, and add vitamins and organics afterward;\
    \ this differs from the imported all-ingredient filter-sterilization instruction.\
    \ The reported resulting pH is 7.5-7.7, not an independently optimized value.\"\
    \n  ],\n  \"variant_source_evidence\": [\n    {\n      \"reference\": \"doi:10.1038/ismej.2012.122\"\
    ,\n      \"supports\": \"SUPPORT\",\n      \"snippet\": \"pyruvate (50 μℳ), methionine\
    \ (10 μℳ), FeCl 3 (1 μℳ) and vitamins.\",\n      \"explanation\": \"Locator: Materials\
    \ and methods, Glycine substitution experiments, with Table 1 (Compound / Final\
    \ concentration) and Media preparation. Supports only this inline variant's modifications,\
    \ never replacement of the parent's ingredients. The immediately preceding methods\
    \ phrase is 'at a concentration of 25 μℳ'. Table 1 row: 'CaCl 2 ·2H 2 O 10 mℳ';\
    \ Table 1 row: 'MgSO 4 ·7H 2 O 2.8 mℳ'; Table 1 row: 'FeCl 3 ·6H 2 O 117 nℳ';\
    \ Table 1 row: 'MnCl 2 ·4H 2 O 9 nℳ'; Table 1 row: 'ZnSO 4 ·7H 2 O 800 pM'; Table\
    \ 1 row: 'CoCl 2 ·6H 2 O 500 pM'; Table 1 row: 'Na 2 MoO 4 ·2H 2 O 300 pM'; Table\
    \ 1 row: 'NiCl 2 ·6H 2 O 1 nℳ'; Table 1 row: 'B 1 6 μℳ'; Table 1 row: 'B 3 800\
    \ nℳ'; Table 1 row: 'B 5 425 nℳ'; Table 1 row: 'B 6 500 nℳ'; Table 1 row: 'B 7\
    \ 4 nℳ'; Table 1 row: 'B 9 4 nℳ'; Table 1 row: 'B 12 700 pM'; Table 1 row: 'Myo-inositol\
    \ 6 μℳ'; Table 1 row: '4-Aminobenzoic acid 60 nℳ'. The B-number names are retained\
    \ as published; no molecular-weight conversion, unreported salt identity or stock\
    \ dilution was inferred. Amounts are final assay concentrations. The paper's Table\
    \ 1 excludes the reduced-sulfur, glycine and pyruvate additions, which the assay\
    \ methods supply. Media preparation separately places vitamins/organics after\
    \ autoclaving and sparging.\"\n    }\n  ],\n  \"historical_qualification\": \"\
    Published AMS1 formulation used in the glycine substitution experiment, glycine\
    \ positive-control condition. This is not an assertion that the imported MediaDB\
    \ parent matches the paper. Composite concentration, vitamin, chemical-form and\
    \ preparation changes; methionine and serine stereochemistry is not specified\
    \ in the inspected methods. Historical 2013 assay formulation, not evidence that\
    \ thiamin substitutes for HMP: Carini et al. 2014 (doi:10.1038/ismej.2014.61)\
    \ found an HMP requirement and HMP contamination in their thiamin stock. Trace\
    \ HMP in the 2013 batches was not quantified by the inspected 2013 paper; do not\
    \ interpret nominal absence of added HMP as HMP-independent growth.\"\n}"
  dimensions:
  - name: reviewed_instances
    value: 20 direct parent ingredients; 0 stocks; 1 added inline study variant
    definition: Local recipe nodes inspected against this one paper, not a whole-corpus
      concentration score.
    evidence_ids:
    - records
    - paper
  - name: native_decisions
    value: conflict / unsupported / evidence_only comparison for parents; add supported
      study variant
    definition: Decisions are relative to the 2013 Table 3 assay, not a claim that
      the MediaDB parent is globally wrong.
    evidence_ids:
    - paper
    - records
  metrics:
  - name: parent ingredients compared
    value: 20
    unit: ingredient instances
    denominator: 20
    minimum: 0
    maximum: 20
    definition: Direct ingredients inspected for this source comparison; does not
      measure scientific correctness or evidence coverage of the canonical parent.
- assessment_id: organism-007382
  area: grounding
  topic: Strain-specific, variant-only cultivation evidence
  outcome: supported
  target_ids:
  - CultureMech:007382
  evidence_ids:
  - paper
  - taxonomy
  - records
  summary: Table 3 positive cell yield supports HTCC1062 only on the named study variant.
    Exact strain grounding is NCBITaxon335992; no HTCC7211 or parent-medium growth
    assertion is added.
- assessment_id: variant-007384
  area: quantity
  topic: Study-specific concentration and formulation scope
  outcome: supported
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - paper
  - records
  summary: Seven compound modification statements separate the 2013 assay from the
    imported parent. Source row excerpts support amounts, salt hydrates and the Table
    1 vitamin mixture; arithmetic is not embedded in quotations.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"4-Amino-5-hydroxymethyl-2-methylpyrimidine\"\
    ,\n      \"ontology_term_as_recorded_not_reverified\": null,\n      \"old_amount\"\
    : {\n        \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n\
    \      \"proposed_parent_amount\": null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\"\
    ,\n      \"source_excerpts\": [],\n      \"source_basis\": \"Table 1 final concentration;\
    \ explicit Table 3 assay additions override basal FeCl3\",\n      \"parent_basis\"\
    : \"Imported molar concentration; exact correspondence to this paper not established\"\
    ,\n      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000\
    \ nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": \"HMP is not listed in the inspected complete\
    \ 2013 Table 1 vitamin list; omission is not a quantified zero. The 2014 qualification\
    \ addresses trace contamination.\",\n      \"decision\": \"unsupported: absent\
    \ from the complete 2013 Table 1 vitamin list; do not infer a 2013 HMP formulation\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"Pyruvate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:15361\",\n        \"label\": \"pyruvate\"\n     \
    \ },\n      \"old_amount\": {\n        \"value\": \"1.0\",\n        \"unit\":\
    \ \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"pyruvate (50 μℳ), methionine (10 μℳ),\
    \ FeCl 3 (1 μℳ) and vitamins.\",\n          \"locator\": \"Materials and methods,\
    \ Glycine substitution experiments\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"conflict: local amount differs from the specifically reviewed\
    \ Table 3 assay; retain parent and represent study variant\",\n      \"action_taken\"\
    : \"Parent retained unchanged; differences represented only in the study variant.\"\
    \n    },\n    {\n      \"field_path\": \"ingredients[2].concentration\",\n   \
    \   \"ingredient\": \"Biotin\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:15956\",\n        \"label\": \"biotin\"\n      },\n\
    \      \"old_amount\": {\n        \"value\": \"4e-06\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"B 7 4 nℳ\",\n          \"locator\": \"Table 1, Compound\
    \ / Final concentration\"\n        }\n      ],\n      \"source_basis\": \"Table\
    \ 1 final concentration; explicit Table 3 assay additions override basal FeCl3\"\
    ,\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[3].concentration\"\
    ,\n      \"ingredient\": \"Nickel chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:34887\",\n        \"label\": \"nickel dichloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"1e-06\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NiCl 2 ·6H 2 O 1 nℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[4].concentration\",\n      \"ingredient\"\
    : \"Magnesium chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:86345\",\n        \"label\": \"magnesium dichloride\
    \ hexahydrate\"\n      },\n      \"old_amount\": {\n        \"value\": \"27.0\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\"\
    : null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"\
    source_excerpts\": [\n        {\n          \"snippet\": \"MgCl 2 ·6H 2 O 27 mℳ\"\
    ,\n          \"locator\": \"Table 1, Compound / Final concentration\"\n      \
    \  }\n      ],\n      \"source_basis\": \"Table 1 final concentration; explicit\
    \ Table 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"\
    Imported molar concentration; exact correspondence to this paper not established\"\
    ,\n      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000\
    \ nM = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[5].concentration\",\n      \"ingredient\"\
    : \"L-Serine\",\n      \"ontology_term_as_recorded_not_reverified\": {\n     \
    \   \"id\": \"CHEBI:17115\",\n        \"label\": \"L-serine\"\n      },\n    \
    \  \"old_amount\": {\n        \"value\": \"0.05\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"Each substitute was tested at a concentration of 25 μℳ\"\
    ,\n          \"locator\": \"Materials and methods, Glycine substitution experiments;\
    \ Table 3 identifies serine as a substitute\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"conflict: local amount differs from the specifically reviewed\
    \ Table 3 assay; retain parent and represent study variant\",\n      \"action_taken\"\
    : \"Parent retained unchanged; differences represented only in the study variant.\"\
    \n    },\n    {\n      \"field_path\": \"ingredients[6].concentration\",\n   \
    \   \"ingredient\": \"Sodium bicarbonate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:32139\",\n        \"label\": \"sodium hydrogencarbonate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"6.0\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NaHCO 3 6 mℳ\",\n          \"locator\"\
    : \"Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[7].concentration\"\
    ,\n      \"ingredient\": \"Calcium chloride anhydrous\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:3312\",\n        \"label\": \"calcium dichloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"10.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"CaCl 2 ·2H 2 O 10 mℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[8].concentration\",\n      \"ingredient\"\
    : \"Sodium molybdate\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:75215\",\n        \"label\": \"sodium molybdate (anhydrous)\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"3e-07\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"Na 2 MoO 4 ·2H 2 O 300 pM\",\n      \
    \    \"locator\": \"Table 1, Compound / Final concentration\"\n        }\n   \
    \   ],\n      \"source_basis\": \"Table 1 final concentration; explicit Table\
    \ 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"Imported\
    \ molar concentration; exact correspondence to this paper not established\",\n\
    \      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM\
    \ = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[9].concentration\",\n      \"ingredient\"\
    : \"Magnesium sulfate\",\n      \"ontology_term_as_recorded_not_reverified\":\
    \ {\n        \"id\": \"CHEBI:32599\",\n        \"label\": \"magnesium sulfate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"28.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"MgSO 4 ·7H 2 O 2.8 mℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"conflict: local amount differs\
    \ from the specifically reviewed Table 3 assay; retain parent and represent study\
    \ variant\",\n      \"action_taken\": \"Parent retained unchanged; differences\
    \ represented only in the study variant.\"\n    },\n    {\n      \"field_path\"\
    : \"ingredients[10].concentration\",\n      \"ingredient\": \"DL-methionine\"\
    ,\n      \"ontology_term_as_recorded_not_reverified\": {\n        \"id\": \"CHEBI:16811\"\
    ,\n        \"label\": \"methionine\"\n      },\n      \"old_amount\": {\n    \
    \    \"value\": \"0.05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    proposed_parent_amount\": null,\n      \"source_reference\": \"doi:10.1038/ismej.2012.122\"\
    ,\n      \"source_excerpts\": [\n        {\n          \"snippet\": \"pyruvate\
    \ (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ) and vitamins.\",\n          \"locator\"\
    : \"Materials and methods, Glycine substitution experiments\"\n        }\n   \
    \   ],\n      \"source_basis\": \"Table 1 final concentration; explicit Table\
    \ 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"Imported\
    \ molar concentration; exact correspondence to this paper not established\",\n\
    \      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM\
    \ = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"conflict: local\
    \ amount differs from the specifically reviewed Table 3 assay; retain parent and\
    \ represent study variant\",\n      \"action_taken\": \"Parent retained unchanged;\
    \ differences represented only in the study variant.\"\n    },\n    {\n      \"\
    field_path\": \"ingredients[11].concentration\",\n      \"ingredient\": \"Sodium\
    \ selenite\",\n      \"ontology_term_as_recorded_not_reverified\": {\n       \
    \ \"id\": \"CHEBI:48843\",\n        \"label\": \"disodium selenite\"\n      },\n\
    \      \"old_amount\": {\n        \"value\": \"1e-06\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"Na 2 SeO 3 1 nℳ\",\n          \"locator\": \"Table 1,\
    \ Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"Potassium chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:32588\",\n        \"label\": \"potassium chloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"9.0\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"KCl 9 mℳ\",\n          \"locator\": \"\
    Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[13].concentration\"\
    ,\n      \"ingredient\": \"Cobalt chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:35696\",\n        \"label\": \"cobalt dichloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"5e-07\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"CoCl 2 ·6H 2 O 500 pM\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[14].concentration\",\n      \"ingredient\"\
    : \"Sodium chloride\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:26710\",\n        \"label\": \"sodium chloride\"\n  \
    \    },\n      \"old_amount\": {\n        \"value\": \"481.0\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NaCl 481 mℳ\",\n          \"locator\"\
    : \"Table 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[15].concentration\"\
    ,\n      \"ingredient\": \"Sodium dihydrogen phosphate\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:37585\",\n        \"label\": \"sodium dihydrogenphosphate\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"0.05\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"NaH 2 PO 4 (pH 7.5) 50 μℳ\",\n      \
    \    \"locator\": \"Table 1, Compound / Final concentration\"\n        }\n   \
    \   ],\n      \"source_basis\": \"Table 1 final concentration; explicit Table\
    \ 3 assay additions override basal FeCl3\",\n      \"parent_basis\": \"Imported\
    \ molar concentration; exact correspondence to this paper not established\",\n\
    \      \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM\
    \ = 1000000000 pM. No mass or stock conversion, and no parent amount rewritten.\"\
    ,\n      \"missing_source_detail\": null,\n      \"decision\": \"evidence_only\
    \ comparison: numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[16].concentration\",\n      \"ingredient\"\
    : \"Ammonium sulfate\",\n      \"ontology_term_as_recorded_not_reverified\": {\n\
    \        \"id\": \"CHEBI:62946\",\n        \"label\": \"ammonium sulfate\"\n \
    \     },\n      \"old_amount\": {\n        \"value\": \"0.4\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"\
    source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"(NH 4 ) 2 SO 4 400 μℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[17].concentration\",\n      \"ingredient\"\
    : \"Manganese chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : {\n        \"id\": \"CHEBI:63041\",\n        \"label\": \"manganese(II) chloride\"\
    \n      },\n      \"old_amount\": {\n        \"value\": \"9e-06\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"MnCl 2 ·4H 2 O 9 nℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        }\n      ],\n\
    \      \"source_basis\": \"Table 1 final concentration; explicit Table 3 assay\
    \ additions override basal FeCl3\",\n      \"parent_basis\": \"Imported molar\
    \ concentration; exact correspondence to this paper not established\",\n     \
    \ \"calculation\": \"Comparison only; 1 mM = 1000 micromolar = 1000000 nM = 1000000000\
    \ pM. No mass or stock conversion, and no parent amount rewritten.\",\n      \"\
    missing_source_detail\": null,\n      \"decision\": \"evidence_only comparison:\
    \ numerical molar amount agrees with Table 1; chemical forms and whole-parent\
    \ recipe identity are not certified\",\n      \"action_taken\": \"Parent retained\
    \ unchanged; differences represented only in the study variant.\"\n    },\n  \
    \  {\n      \"field_path\": \"ingredients[18].concentration\",\n      \"ingredient\"\
    : \"Zinc sulfate\",\n      \"ontology_term_as_recorded_not_reverified\": {\n \
    \       \"id\": \"CHEBI:35176\",\n        \"label\": \"zinc sulfate\"\n      },\n\
    \      \"old_amount\": {\n        \"value\": \"8e-07\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n      \"source_reference\"\
    : \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\": [\n        {\n \
    \         \"snippet\": \"ZnSO 4 ·7H 2 O 800 pM\",\n          \"locator\": \"Table\
    \ 1, Compound / Final concentration\"\n        }\n      ],\n      \"source_basis\"\
    : \"Table 1 final concentration; explicit Table 3 assay additions override basal\
    \ FeCl3\",\n      \"parent_basis\": \"Imported molar concentration; exact correspondence\
    \ to this paper not established\",\n      \"calculation\": \"Comparison only;\
    \ 1 mM = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"evidence_only comparison: numerical molar amount agrees\
    \ with Table 1; chemical forms and whole-parent recipe identity are not certified\"\
    ,\n      \"action_taken\": \"Parent retained unchanged; differences represented\
    \ only in the study variant.\"\n    },\n    {\n      \"field_path\": \"ingredients[19].concentration\"\
    ,\n      \"ingredient\": \"Iron(III) chloride\",\n      \"ontology_term_as_recorded_not_reverified\"\
    : null,\n      \"old_amount\": {\n        \"value\": \"0.000117\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"proposed_parent_amount\": null,\n  \
    \    \"source_reference\": \"doi:10.1038/ismej.2012.122\",\n      \"source_excerpts\"\
    : [\n        {\n          \"snippet\": \"FeCl 3 ·6H 2 O 117 nℳ\",\n          \"\
    locator\": \"Table 1, Compound / Final concentration\"\n        },\n        {\n\
    \          \"snippet\": \"pyruvate (50 μℳ), methionine (10 μℳ), FeCl 3 (1 μℳ)\
    \ and vitamins.\",\n          \"locator\": \"Materials and methods, Glycine substitution\
    \ experiments\"\n        }\n      ],\n      \"source_basis\": \"Table 1 final\
    \ concentration; explicit Table 3 assay additions override basal FeCl3\",\n  \
    \    \"parent_basis\": \"Imported molar concentration; exact correspondence to\
    \ this paper not established\",\n      \"calculation\": \"Comparison only; 1 mM\
    \ = 1000 micromolar = 1000000 nM = 1000000000 pM. No mass or stock conversion,\
    \ and no parent amount rewritten.\",\n      \"missing_source_detail\": null,\n\
    \      \"decision\": \"conflict: local amount differs from the specifically reviewed\
    \ Table 3 assay; retain parent and represent study variant\",\n      \"action_taken\"\
    : \"Parent retained unchanged; differences represented only in the study variant.\"\
    \n    }\n  ],\n  \"variant_field\": \"variants[0]\",\n  \"variant_name\": \"Carini\
    \ 2013 AMS1 serine substitution assay\",\n  \"variant_action\": \"add\",\n  \"\
    old_variant\": null,\n  \"variant_modifications\": [\n    \"Use 50 micromolar\
    \ pyruvate instead of the parent's 1.0 mM, and 10 micromolar methionine instead\
    \ of 0.05 mM DL-methionine; the paper does not specify methionine stereochemistry.\"\
    ,\n    \"Use 25 micromolar serine instead of the parent's 0.05 mM L-Serine; this\
    \ is the Table 3 assay, not a titration maximum or a universal optimum.\",\n \
    \   \"Use magnesium sulfate heptahydrate at 2.8 mM rather than the parent's magnesium\
    \ sulfate at 28.0 mM. Other unchanged Table 1 base-salt and macronutrient molar\
    \ amounts remain as reported there.\",\n    \"Use calcium chloride dihydrate,\
    \ manganese chloride tetrahydrate, zinc sulfate heptahydrate, cobalt chloride\
    \ hexahydrate, sodium molybdate dihydrate and nickel chloride hexahydrate as specified\
    \ in Table 1; retain their Table 1 molar amounts rather than infer mass equivalents\
    \ from the local anhydrous or unspecified forms.\",\n    \"Use iron(III) chloride\
    \ at 1 micromolar in this assay instead of the parent's 117 nM; Table 1 specifies\
    \ the hexahydrate and its basal 117 nM is overridden by the assay methods.\",\n\
    \    \"Replace the imported biotin/HMP vitamin selection with the complete Table\
    \ 1 vitamin mixture: B1 6 micromolar, B3 800 nM, B5 425 nM, B6 500 nM, B7 4 nM,\
    \ B9 4 nM, B12 700 pM, myo-inositol 6 micromolar and 4-aminobenzoic acid 60 nM.\
    \ Do not substitute HMP for B1 using this 2013 paper.\",\n    \"Follow the paper's\
    \ AMS1 preparation: autoclave the inorganic medium, establish the bicarbonate\
    \ buffer by filtered CO2 then air sparging, and add vitamins and organics afterward;\
    \ this differs from the imported all-ingredient filter-sterilization instruction.\
    \ The reported resulting pH is 7.5-7.7, not an independently optimized value.\"\
    \n  ],\n  \"variant_source_evidence\": [\n    {\n      \"reference\": \"doi:10.1038/ismej.2012.122\"\
    ,\n      \"supports\": \"SUPPORT\",\n      \"snippet\": \"pyruvate (50 μℳ), methionine\
    \ (10 μℳ), FeCl 3 (1 μℳ) and vitamins.\",\n      \"explanation\": \"Locator: Materials\
    \ and methods, Glycine substitution experiments, with Table 1 (Compound / Final\
    \ concentration) and Media preparation. Supports only this inline variant's modifications,\
    \ never replacement of the parent's ingredients. The immediately preceding methods\
    \ phrase is 'at a concentration of 25 μℳ'. Table 1 row: 'CaCl 2 ·2H 2 O 10 mℳ';\
    \ Table 1 row: 'MgSO 4 ·7H 2 O 2.8 mℳ'; Table 1 row: 'FeCl 3 ·6H 2 O 117 nℳ';\
    \ Table 1 row: 'MnCl 2 ·4H 2 O 9 nℳ'; Table 1 row: 'ZnSO 4 ·7H 2 O 800 pM'; Table\
    \ 1 row: 'CoCl 2 ·6H 2 O 500 pM'; Table 1 row: 'Na 2 MoO 4 ·2H 2 O 300 pM'; Table\
    \ 1 row: 'NiCl 2 ·6H 2 O 1 nℳ'; Table 1 row: 'B 1 6 μℳ'; Table 1 row: 'B 3 800\
    \ nℳ'; Table 1 row: 'B 5 425 nℳ'; Table 1 row: 'B 6 500 nℳ'; Table 1 row: 'B 7\
    \ 4 nℳ'; Table 1 row: 'B 9 4 nℳ'; Table 1 row: 'B 12 700 pM'; Table 1 row: 'Myo-inositol\
    \ 6 μℳ'; Table 1 row: '4-Aminobenzoic acid 60 nℳ'. The B-number names are retained\
    \ as published; no molecular-weight conversion, unreported salt identity or stock\
    \ dilution was inferred. Amounts are final assay concentrations. The paper's Table\
    \ 1 excludes the reduced-sulfur, glycine and pyruvate additions, which the assay\
    \ methods supply. Media preparation separately places vitamins/organics after\
    \ autoclaving and sparging.\"\n    }\n  ],\n  \"historical_qualification\": \"\
    Published AMS1 formulation used in the glycine substitution experiment, serine\
    \ test condition. This is not an assertion that the imported MediaDB parent matches\
    \ the paper. Composite concentration, vitamin, chemical-form and preparation changes;\
    \ methionine and serine stereochemistry is not specified in the inspected methods.\
    \ Historical 2013 assay formulation, not evidence that thiamin substitutes for\
    \ HMP: Carini et al. 2014 (doi:10.1038/ismej.2014.61) found an HMP requirement\
    \ and HMP contamination in their thiamin stock. Trace HMP in the 2013 batches\
    \ was not quantified by the inspected 2013 paper; do not interpret nominal absence\
    \ of added HMP as HMP-independent growth.\"\n}"
  dimensions:
  - name: reviewed_instances
    value: 20 direct parent ingredients; 0 stocks; 1 added inline study variant
    definition: Local recipe nodes inspected against this one paper, not a whole-corpus
      concentration score.
    evidence_ids:
    - records
    - paper
  - name: native_decisions
    value: conflict / unsupported / evidence_only comparison for parents; add supported
      study variant
    definition: Decisions are relative to the 2013 Table 3 assay, not a claim that
      the MediaDB parent is globally wrong.
    evidence_ids:
    - paper
    - records
  metrics:
  - name: parent ingredients compared
    value: 20
    unit: ingredient instances
    denominator: 20
    minimum: 0
    maximum: 20
    definition: Direct ingredients inspected for this source comparison; does not
      measure scientific correctness or evidence coverage of the canonical parent.
- assessment_id: organism-007384
  area: grounding
  topic: Strain-specific, variant-only cultivation evidence
  outcome: supported
  target_ids:
  - CultureMech:007384
  evidence_ids:
  - paper
  - taxonomy
  - records
  summary: Table 3 positive cell yield supports HTCC1062 only on the named study variant.
    Exact strain grounding is NCBITaxon335992; no HTCC7211 or parent-medium growth
    assertion is added.
- assessment_id: historical-vitamin-qualification
  area: evidence
  topic: Subsequent evidence limits interpretation of the 2013 recipe
  outcome: supported
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - paper
  - followup
  - records
  summary: Both variant descriptions and organism-evidence explanations preserve the
    HMP caveat; neither base recipe is changed. The 2014 citation is a qualification,
    not a new positive growth edge or a formal correction notice.
- assessment_id: publication-scope
  area: graph
  topic: KGX variant-scope preservation
  outcome: concern
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  evidence_ids:
  - exporter
  summary: The current exporter cannot safely publish these two variant-only growth
    associations.
findings:
- finding_id: variant-export
  issue_key: kgx-variant-growth-scope-loss-ams1-carini2013
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: KGX drops the new study-variant scope
  description: The YAML correctly scopes HTCC1062 growth to a named inline variant,
    but the exporter's parent-medium edge path ignores scoped_to_variant. Withholding
    this turn's export prevents publication but does not repair the exporter.
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  field_paths:
  - target_organisms[0].scoped_to_variant
  evidence_ids:
  - exporter
  - records
  owner_paths:
  - repository: culturebotai/CultureMech
    path: src/culturemech/export/kgx_export.py
    role: scope-preserving edge construction
actions:
- action_id: guard-variant-export
  description: Before publishing these associations, represent variant targets faithfully
    or fail closed for scoped_to_variant in the maintained KGX exporter.
  finding_ids:
  - variant-export
  target_ids:
  - CultureMech:007382
  - CultureMech:007384
  owner_paths:
  - repository: culturebotai/CultureMech
    path: src/culturemech/export/kgx_export.py
    role: scope-preserving edge construction
  acceptance_checks:
  - Regression test proves neither AMS1 parent receives the study-variant growth edge.
  - Tests cover other variant-scoped organisms and ordinary unscoped growth without
    suppressing valid edges.
limitations:
- This is a focused paper/formulation assessment, not a full record or whole-corpus
  scientific review.
- All parent concentrations remain unchanged and are not certified as the 2013 formulation.
  Ingredient ontology grounding outside the reported hydrate comparison was not reassessed.
- Methionine and serine stereochemistry is not specified by the inspected methods;
  no stereochemical identity or molecular-weight conversion was invented.
- External supplements, unrelated organism mentions and other substitution assays
  were not exhaustively reviewed.
- No KGX output, rendered page or regenerated merged record was published. Current
  exporter scope loss requires separate repair before publication.
- Merge diagnostics cover the existing corpus; these checks do not establish an untouched
  baseline for every global drift difference.
```
