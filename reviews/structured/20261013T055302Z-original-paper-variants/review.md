# Mattanovich and Jensen paper citations, recipe variants and strain evidence

- Review: 20261013T055302Z-original-paper-variants
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-13T05:30:34Z
- Finished UTC: 2026-10-13T05:53:02Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Six paper-record citations for two papers, six inline variants and six variant-only strain growth assertions; all parent ingredients preserved. Focused record gates pass, but export scope loss, retained category mismatch, chemical uncertainties and global merge diagnostics prevent publication-ready approval.

## Scope And Provenance

Six exact MediaDB source11/128 normalized owners and 181 direct ingredient instances, with source recipe and strain comparison.

Selection: Frozen targets.yaml exact paths/IDs; no source128 SA record invented and no other cohort expansion.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007250 | data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml | maintained | Batch medium; mattanovich et al |
| CultureMech:007302 | data/normalized_yaml/bacterial/bl_medium.yaml | maintained | BL Medium |
| CultureMech:007303 | data/normalized_yaml/bacterial/bl_medium_arg.yaml | maintained | BL Medium + Arg |
| CultureMech:007304 | data/normalized_yaml/bacterial/bl_medium_asp.yaml | maintained | BL Medium + Asp |
| CultureMech:007305 | data/normalized_yaml/bacterial/bl_medium_low_mops.yaml | maintained | BL Medium, Low MOPS |
| CultureMech:007306 | data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml | maintained | BL Medium + Arg + Ser + Trp |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-schema data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml | passed | True | CultureMech:007250 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml | passed | True | CultureMech:007250 | Maintained baseline/post-edit or repository merge gate. |
| just validate-schema data/normalized_yaml/bacterial/bl_medium.yaml | passed | True | CultureMech:007302 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium.yaml | passed | True | CultureMech:007302 | Maintained baseline/post-edit or repository merge gate. |
| just validate-schema data/normalized_yaml/bacterial/bl_medium_arg.yaml | passed | True | CultureMech:007303 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_arg.yaml | passed | True | CultureMech:007303 | Maintained baseline/post-edit or repository merge gate. |
| just validate-schema data/normalized_yaml/bacterial/bl_medium_asp.yaml | passed | True | CultureMech:007304 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_asp.yaml | passed | True | CultureMech:007304 | Maintained baseline/post-edit or repository merge gate. |
| just validate-schema data/normalized_yaml/bacterial/bl_medium_low_mops.yaml | passed | True | CultureMech:007305 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_low_mops.yaml | passed | True | CultureMech:007305 | Maintained baseline/post-edit or repository merge gate. |
| just validate-schema data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml | passed | True | CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml | passed | True | CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| just validate data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml | passed | True | CultureMech:007250 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml | passed | True | CultureMech:007250 | Maintained baseline/post-edit or repository merge gate. |
| just validate data/normalized_yaml/bacterial/bl_medium.yaml | passed | True | CultureMech:007302 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium.yaml | passed | True | CultureMech:007302 | Maintained baseline/post-edit or repository merge gate. |
| just validate data/normalized_yaml/bacterial/bl_medium_arg.yaml | passed | True | CultureMech:007303 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_arg.yaml | passed | True | CultureMech:007303 | Maintained baseline/post-edit or repository merge gate. |
| just validate data/normalized_yaml/bacterial/bl_medium_asp.yaml | passed | True | CultureMech:007304 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_asp.yaml | passed | True | CultureMech:007304 | Maintained baseline/post-edit or repository merge gate. |
| just validate data/normalized_yaml/bacterial/bl_medium_low_mops.yaml | passed | True | CultureMech:007305 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_low_mops.yaml | passed | True | CultureMech:007305 | Maintained baseline/post-edit or repository merge gate. |
| just validate data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml | passed | True | CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| just validate-strict data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml | passed | True | CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| just verify-merges | failed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Interrupted after the YAML-parse stage and1247 canonical-name conflicts; remaining completeness/fingerprint/synonym diagnostics did not finish. Not a completed full merge audit. See merge-interruption.json. |
| just audit-merge-freshness --json | failed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Completed freshness audit failed: 6320 existing on-disk merged files versus10781 regenerated,4275 only existing,8736 only fresh,2045 changed,0 unchanged. The tracked_total label is the audit tool terminology, not an exact git ls-files inventory. Regeneration was temporary; no merged outputs replaced. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/.codex/skills/.system/skill-creator/scripts/quick_validate.py .claude/skills/culturemech-add-paper-citation | passed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| /tmp/culturemech-parallel-env-20261012/bin/python -m pytest tests/test_fetch_pubmed_abstracts.py tests/test_claude_skills.py tests/test_skill_frontmatter.py tests/test_record_review_contract.py tests/test_record_review_routes.py tests/test_mediadb_sql_parsing.py --no-cov -q | passed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| /tmp/culturemech-parallel-env-20261012/bin/python /tmp/curate-original-papers-20261013.py --apply | passed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| git diff --check | passed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Maintained baseline/post-edit or repository merge gate. |
| Primary-source excerpts and recipe comparison | passed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | Read main methods, XLS source cells, original scans, table headings and footnotes; retain explicit limits on chemical forms and parent amounts. |
| KGX variant scope | failed | True | CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306 | In-memory edge construction drops variant scope for all six targets. No edges or generated pages published. |

## Scientific And Domain Assessments

### Source-specific formulation and parent preservation

quantity: supported. Targets: CultureMech:007250.

Supported source-defined chemostat variant preserves stock/final boundaries; parent molar conversions remain unverified.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "Sulfate",
      "old_amount": {
        "value": "0.41587",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "5 mL H2SO4 (95-98% w/w)",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A33",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Glycerol",
      "old_amount": {
        "value": "433.27",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "39.9 g glycerol, 1.8 g ",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A3",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "Biotin",
      "old_amount": {
        "value": "0.001637",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "2 mL of Biotin (0.2 g L-1)",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A9",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "Citrate",
      "old_amount": {
        "value": "9.369",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "1.8 g citric acid",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A4",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "old_amount": {
        "value": "0.1496",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.022 g CaCl2 · 2H2O",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A7",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "Boric acid",
      "old_amount": {
        "value": "0.001488",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.02 g H3BO3",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A29",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "Sodium molybdate",
      "old_amount": {
        "value": "0.003802",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.2g Na2MoO4 · 2H2O",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A28",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Potassium chloride",
      "old_amount": {
        "value": "12.072",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.9 g KCl",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A5",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "Magnesium sulfate",
      "old_amount": {
        "value": "2.0286",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.5 g MgSO4 · 7H2O",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A8",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "Manganese sulfate",
      "old_amount": {
        "value": "0.08165",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "3.0 g MnSO4 ·H2O",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A27",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "Ferrous sulfate",
      "old_amount": {
        "value": "0.08273",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "5.0 g FeSO4 · 7H2O",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A32",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "Cobalt chloride",
      "old_amount": {
        "value": "0.017714",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.5 g CoCl2",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A30",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "Cupric sulfate",
      "old_amount": {
        "value": "0.11054",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "6.0 g CuSO4 · 5H2O",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A25",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "Zinc Chloride",
      "old_amount": {
        "value": "0.6749",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "20.0 g ZnCl2",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A31",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Ammonium phosphate",
      "old_amount": {
        "value": "95.414",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "12.6 g (NH4)2HPO4",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A6",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "Sodium iodide",
      "old_amount": {
        "value": "0.002455",
        "unit": "MILLIMOLAR"
      },
      "status": "unsupported",
      "source_excerpt": "0.08 g NaI",
      "source_locator": "additional file 3, 'Fermentation data and Analysis'!A26",
      "source_reference": "doi:10.1186/1475-2859-8-29",
      "reason": "Parent molar amount not recertified from mass/stock/acid source units; no molecular-weight or density conversion undertaken.",
      "action": "parent unchanged; separately source-defined chemostat variant added",
      "proposed_parent_amount": null
    }
  ],
  "variant_field": "variants[0]",
  "old_variant": null,
  "action": "add",
  "variant": {
    "name": "Mattanovich 2009 glucose chemostat formulation",
    "description": "Source-defined glucose chemostat formulation, distinct from the imported glycerol batch medium. All recipe quantities retain supplement source units and stock/final boundaries; not a certification of the parent's concentrations, ingredient grounding or preparation.",
    "modifications": [
      "Replace the batch parent's glycerol (433.27 mM) with glucose monohydrate at the source's 50.0 g per liter of chemostat medium.",
      "Use 0.9 g/L citric acid, 1.7 g/L KCl and 4.35 g/L (NH4)2HPO4, replacing the parent's molar citrate, KCl and ammonium-phosphate entries; preserve the source's chemical forms and mass basis.",
      "Use 0.01 g/L CaCl2 dihydrate and 0.65 g/L MgSO4 heptahydrate rather than inheriting the parent's batch amounts and anhydrous/unspecified forms.",
      "Add 1 mL of 0.2 g/L biotin stock per liter of chemostat medium instead of inheriting the parent's direct biotin molarity.",
      "Replace the parent's nine flattened trace/acid entries (sulfate, boric acid, sodium molybdate, manganese sulfate, ferrous sulfate, cobalt chloride, cupric sulfate, zinc chloride and sodium iodide) with 1.6 mL of trace-salts stock per liter of chemostat medium. Do not retain both the flattened ingredients and this stock dose.",
      "Trace-salts stock, per liter of stock: 6.0 g CuSO4 pentahydrate, 0.08 g NaI, 3.0 g MnSO4 monohydrate, 0.2 g Na2MoO4 dihydrate, 0.02 g H3BO3, 0.5 g CoCl2, 20.0 g ZnCl2, 5.0 g FeSO4 heptahydrate and 5 mL H2SO4 (95-98% w/w). These are stock amounts, not final-medium amounts; no acid density or molar conversion is inferred.",
      "Set initial medium pH to 5.0 using 25% HCl as stated in the supplement; its percentage basis and a fixed titrant volume are not specified. The chemostat pH was controlled at 5.0 with 25% ammonium hydroxide. The inspected source does not establish the parent's generic final-medium filter-sterilization procedure, so that procedure is not inherited as verified study preparation."
    ],
    "purpose": "Glucose-limited chemostat cultivation for experimental secretome analysis.",
    "evidence": [
      {
        "reference": "doi:10.1186/1475-2859-8-29",
        "supports": "SUPPORT",
        "snippet": "50.0g glucose · H2O",
        "explanation": "Locator: additional file 3, sheet 'Fermentation data and Analysis', A13:A33; source=https://media.springernature.com/original/springer-static/esm/art%3A10.1186%2F1475-2859-8-29/MediaObjects/12934_2009_349_MOESM3_ESM.xls. A13: 'Chemostat medium contained per Liter'; A14: '50.0g glucose · H2O'; A15: '0.9g citric acid'; A16: '1.7 g KCl'; A17: '4.35 g (NH4)2HPO4'; A18: '0.01 g CaCl2 · 2H2O'; A19: '0.65 g MgSO4 · 7H2O'; A20: '1 mL of Biotin (0.2 g L-1)'; A21: '1.6 mL of trace salts stock solution. '; A22: 'pH set to 5.0 using 25% HCl'; A24: 'Trace salts stock solution contained per Liter'; A25: '6.0 g CuSO4 · 5H2O'; A26: '0.08 g NaI'; A27: '3.0 g MnSO4 ·H2O'; A28: '0.2g Na2MoO4 · 2H2O'; A29: '0.02 g H3BO3'; A30: '0.5 g CoCl2'; A31: '20.0 g ZnCl2'; A32: '5.0 g FeSO4 · 7H2O'; A33: '5 mL H2SO4 (95-98% w/w)'. The heading in A13 establishes the per-liter chemostat-medium basis, A24 establishes the separate per-liter stock basis. Quotes are individual literal cell values, not a spliced sentence. No molecular weights, acid density, stock dilution results or unreported preparation steps are inferred."
      }
    ]
  },
  "parent_amounts_changed": false,
  "conversion": "No mass, density, hydrate or stock dilution conversion. Jensen micromolar-to-mM comparison divides by1000; original facts and basis remain explicit.",
  "scope": "All direct ingredients; none of these parents contains nested solutions. The Mattanovich added variant retains an explicit trace stock in modification prose."
}

### Scientific name, current taxonomy and growth scope

grounding: supported. Targets: CultureMech:007250.

Exact strain DSMZ70382 maps to Komagataella pastoris DSMZ70382, NCBITaxon638632, rank strain; growth is on the glucose chemostat variant.

{
  "preferred_term": "Pichia pastoris",
  "term": {
    "id": "NCBITaxon:638632",
    "label": "Komagataella pastoris DSMZ 70382"
  },
  "strain": "DSMZ 70382",
  "scoped_to_variant": "Mattanovich 2009 glucose chemostat formulation",
  "evidence": [
    {
      "reference": "doi:10.1186/1475-2859-8-29",
      "supports": "SUPPORT",
      "snippet": "P. pastoris DSMZ 70382 was grown in fully aerobic chemostat cultures on minimal medium with glucose as carbon source",
      "explanation": "Locator: Material and methods, Strain and Experimental secretome analysis, together with additional file 3 A13:A40. Growth belongs to the glucose chemostat variant, not the glycerol batch parent. Supplement A38 reports 25 C, A39 pH 5.0 and A36 oxygen control above 20%; these are study conditions, not optima. The database's 0.2/h growth value is not imported. A40's dilution-rate/flow wording is not converted into a growth metric. Reported scientific name=Pichia pastoris; strain=DSMZ 70382 (=CBS704 in the paper). taxonomy_match=exact_strain; NCBITaxon:638632; canonical_label=Komagataella pastoris DSMZ 70382; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=638632. NCBI lists Pichia pastoris DSMZ 70382 as a synonym; species ancestor=Komagataella pastoris, NCBITaxon:4922."
    }
  ]
}

### Source-specific formulation and parent preservation

quantity: supported. Targets: CultureMech:007302.

Selected BL liquid treatment is represented as preparation-qualified variant; numerical agreement is not exact chemical-form equivalence.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "Ammonium chloride",
      "old_amount": {
        "value": "9.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ammonium chloride",
        "source_label": "NH4Cl",
        "source_value": "9.5",
        "source_unit": "mM",
        "value_mM": "9.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "L-Valine",
      "old_amount": {
        "value": "2.6",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Valine",
        "source_label": "L-Valine",
        "source_value": "2.6",
        "source_unit": "mM",
        "value_mM": "2.6",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "L-Methionine",
      "old_amount": {
        "value": "0.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Methionine",
        "source_label": "L-Methionine",
        "source_value": "0.5",
        "source_unit": "mM",
        "value_mM": "0.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "L-Leucine",
      "old_amount": {
        "value": "1.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Leucine",
        "source_label": "L-Leucine",
        "source_value": "1.5",
        "source_unit": "mM",
        "value_mM": "1.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "L-Histidine",
      "old_amount": {
        "value": "0.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Histidine",
        "source_label": "L-Histidine",
        "source_value": "0.3",
        "source_unit": "mM",
        "value_mM": "0.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "L-Glutamine",
      "old_amount": {
        "value": "0.7",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamine",
        "source_label": "L-Glutamine",
        "source_value": "0.7",
        "source_unit": "mM",
        "value_mM": "0.7",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "L-Glutamate",
      "old_amount": {
        "value": "21.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamate",
        "source_label": "L-Glutamate",
        "source_value": "21",
        "source_unit": "mM",
        "value_mM": "21",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Pantothenate",
      "old_amount": {
        "value": "0.002",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pantothenate",
        "source_label": "pantothenate",
        "source_value": "2",
        "source_unit": "micromolar",
        "value_mM": "0.002",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "Boric acid",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Boric acid",
        "source_label": "H3BO3",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "Riboflavin",
      "old_amount": {
        "value": "0.0026",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Riboflavin",
        "source_label": "riboflavin",
        "source_value": "2.6",
        "source_unit": "micromolar",
        "value_mM": "0.0026",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "Thiamine HCl",
      "old_amount": {
        "value": "0.003",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Thiamine HCl",
        "source_label": "thiamine-HCl",
        "source_value": "3",
        "source_unit": "micromolar",
        "value_mM": "0.003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "Nicotinamide",
      "old_amount": {
        "value": "0.008",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Nicotinamide",
        "source_label": "niacinamide",
        "source_value": "8",
        "source_unit": "micromolar",
        "value_mM": "0.008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "L-Asparagine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Asparagine",
        "source_label": "L-Asparagine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "L-Isoleucine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Isoleucine",
        "source_label": "L-Isoleucine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Potassium sulfate",
      "old_amount": {
        "value": "0.28",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium sulfate",
        "source_label": "K2SO4",
        "source_value": "0.28",
        "source_unit": "mM",
        "value_mM": "0.28",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "Potassium dihydrogen phosphate",
      "old_amount": {
        "value": "1.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium dihydrogen phosphate",
        "source_label": "KH2PO4",
        "source_value": "1.3",
        "source_unit": "mM",
        "value_mM": "1.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "Molybdic acid ammonium salt tetrahydrate",
      "old_amount": {
        "value": "3e-06",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Molybdic acid ammonium salt tetrahydrate",
        "source_label": "molybdate trace, printed formula unresolved",
        "source_value": "0.003",
        "source_unit": "micromolar",
        "value_mM": "0.000003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Cobalt chloride",
      "old_amount": {
        "value": "3e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cobalt chloride",
        "source_label": "CoCl2",
        "source_value": "0.03",
        "source_unit": "micromolar",
        "value_mM": "0.00003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "Sodium acetate",
      "old_amount": {
        "value": "15.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium acetate",
        "source_label": "Na-acetate",
        "source_value": "15",
        "source_unit": "mM",
        "value_mM": "15",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Glucose",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Glucose",
        "source_label": "Glucose",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[20].concentration",
      "ingredient": "MOPS",
      "old_amount": {
        "value": "190.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "MOPS",
        "source_label": "MOPS",
        "source_value": "190",
        "source_unit": "mM",
        "value_mM": "190",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[21].concentration",
      "ingredient": "Tricine",
      "old_amount": {
        "value": "4.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Tricine",
        "source_label": "Tricine",
        "source_value": "4",
        "source_unit": "mM",
        "value_mM": "4",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[22].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "old_amount": {
        "value": "0.0005",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Calcium chloride anhydrous",
        "source_label": "CaCl2",
        "source_value": "0.0005",
        "source_unit": "mM",
        "value_mM": "0.0005",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[23].concentration",
      "ingredient": "Magnesium chloride",
      "old_amount": {
        "value": "0.52",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Magnesium chloride",
        "source_label": "MgCl2",
        "source_value": "0.52",
        "source_unit": "mM",
        "value_mM": "0.52",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[24].concentration",
      "ingredient": "Ferrous sulfate",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ferrous sulfate",
        "source_label": "FeSO4",
        "source_value": "0.01",
        "source_unit": "mM",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[25].concentration",
      "ingredient": "Sodium chloride",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium chloride",
        "source_label": "NaCl",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[26].concentration",
      "ingredient": "Cupric sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cupric sulfate",
        "source_label": "CuSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[27].concentration",
      "ingredient": "Zinc sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Zinc sulfate",
        "source_label": "ZnSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[28].concentration",
      "ingredient": "Folate",
      "old_amount": {
        "value": "0.0023",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Folate",
        "source_label": "folic acid",
        "source_value": "2.3",
        "source_unit": "micromolar",
        "value_mM": "0.0023",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[29].concentration",
      "ingredient": "Biotin",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Biotin",
        "source_label": "biotin",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[30].concentration",
      "ingredient": "Manganese chloride",
      "old_amount": {
        "value": "8e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Manganese chloride",
        "source_label": "MnCl2",
        "source_value": "0.08",
        "source_unit": "micromolar",
        "value_mM": "0.00008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[31].concentration",
      "ingredient": "Pyridoxal HCl",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pyridoxal HCl",
        "source_label": "pyridoxal-HCl",
        "source_value": "10",
        "source_unit": "micromolar",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    }
  ],
  "variant_field": "variants[0]",
  "old_variant": null,
  "action": "add",
  "variant": {
    "name": "Jensen 1993 BL Medium reported preparation",
    "description": "Historical Table 3 liquid-culture treatment with the source's preparation and pantothenate form. Numerical parent amounts match the selected Table 1/3 treatment, but unresolved hydrate details are not asserted as exact parent equivalence. This preparation-qualified inline variant does not duplicate or replace the existing BL/low-MOPS full-record relationship.",
    "modifications": [
      "Use the paper's stock-solution filtration through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer filtration of the complete mixture; no additional final-medium sterilization step is inferred.",
      "Use calcium pantothenate as specified in the text; Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar calcium salt or add an inferred calcium concentration.",
      "Keep the published nominal molar formulation from Table 1 and this Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate labels are not promoted to verified study identities. No mass or hydrate conversion is performed.",
      "Retain the Table 3 unmodified BL treatment, including 190 mM MOPS and the Table 1 BL-column amino-acid doses; this is not the 19-amino-acid SA medium."
    ],
    "purpose": "Reported liquid batch-culture treatment for MG1363.",
    "evidence": [
      {
        "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
        "supports": "SUPPORT",
        "snippet": "All stock solutions were passed through Millipore filters (0.2-μm pore size).",
        "explanation": "Locator: page 4363, Growth on plates containing eight amino acids, preparation paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid treatment None (=BL). All numeric ingredient amounts were compared with the original scans; micromolar footnote values were divided by 1000 solely for comparison to existing mM fields. No parent amount was rewritten. The printed molybdate formula/hydration remains unresolved; no unsupported exact chemical identity is claimed."
      }
    ]
  },
  "parent_amounts_changed": false,
  "conversion": "No mass, density, hydrate or stock dilution conversion. Jensen micromolar-to-mM comparison divides by1000; original facts and basis remain explicit.",
  "scope": "All direct ingredients; none of these parents contains nested solutions. The Mattanovich added variant retains an explicit trace stock in modification prose."
}

### Scientific name, current taxonomy and growth scope

grounding: supported. Targets: CultureMech:007302.

Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain; Table3 growth is variant-only.

{
  "preferred_term": "Lactococcus lactis subsp. lactis",
  "term": {
    "id": "NCBITaxon:416870",
    "label": "Lactococcus cremoris subsp. cremoris MG1363"
  },
  "strain": "MG1363",
  "scoped_to_variant": "Jensen 1993 BL Medium reported preparation",
  "evidence": [
    {
      "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "supports": "SUPPORT",
      "snippet": "MG1363 in unaerated batch cultures of BL medium or modified BL medium",
      "explanation": "Locator: original page 4364, Table 3 caption and treatment row None (=BL); that row reports positive growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis. No growth-rate value, OD conversion, pH optimum or broad species growth assertion is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870. The historical subspecies wording differs from current taxonomy; retain it as the reported name, not a current classification. No equivalence between all historical L. lactis strains and L. cremoris is inferred."
    }
  ]
}

### Source-specific formulation and parent preservation

quantity: supported. Targets: CultureMech:007303.

Selected BL liquid treatment is represented as preparation-qualified variant; numerical agreement is not exact chemical-form equivalence.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "L-Valine",
      "old_amount": {
        "value": "2.6",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Valine",
        "source_label": "L-Valine",
        "source_value": "2.6",
        "source_unit": "mM",
        "value_mM": "2.6",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Thiamine HCl",
      "old_amount": {
        "value": "0.003",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Thiamine HCl",
        "source_label": "thiamine-HCl",
        "source_value": "3",
        "source_unit": "micromolar",
        "value_mM": "0.003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "L-Arginine",
      "old_amount": {
        "value": "1.1",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "source_value_mM": "1.1",
        "locator": "pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "Pantothenate",
      "old_amount": {
        "value": "0.002",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pantothenate",
        "source_label": "pantothenate",
        "source_value": "2",
        "source_unit": "micromolar",
        "value_mM": "0.002",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Sodium chloride",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium chloride",
        "source_label": "NaCl",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "L-Methionine",
      "old_amount": {
        "value": "0.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Methionine",
        "source_label": "L-Methionine",
        "source_value": "0.5",
        "source_unit": "mM",
        "value_mM": "0.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "Biotin",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Biotin",
        "source_label": "biotin",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "MOPS",
      "old_amount": {
        "value": "190.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "MOPS",
        "source_label": "MOPS",
        "source_value": "190",
        "source_unit": "mM",
        "value_mM": "190",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "L-Asparagine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Asparagine",
        "source_label": "L-Asparagine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "Nicotinamide",
      "old_amount": {
        "value": "0.008",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Nicotinamide",
        "source_label": "niacinamide",
        "source_value": "8",
        "source_unit": "micromolar",
        "value_mM": "0.008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "L-Glutamate",
      "old_amount": {
        "value": "21.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamate",
        "source_label": "L-Glutamate",
        "source_value": "21",
        "source_unit": "mM",
        "value_mM": "21",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "L-Glutamine",
      "old_amount": {
        "value": "0.7",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamine",
        "source_label": "L-Glutamine",
        "source_value": "0.7",
        "source_unit": "mM",
        "value_mM": "0.7",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "L-Leucine",
      "old_amount": {
        "value": "1.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Leucine",
        "source_label": "L-Leucine",
        "source_value": "1.5",
        "source_unit": "mM",
        "value_mM": "1.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "L-Histidine",
      "old_amount": {
        "value": "0.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Histidine",
        "source_label": "L-Histidine",
        "source_value": "0.3",
        "source_unit": "mM",
        "value_mM": "0.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Riboflavin",
      "old_amount": {
        "value": "0.0026",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Riboflavin",
        "source_label": "riboflavin",
        "source_value": "2.6",
        "source_unit": "micromolar",
        "value_mM": "0.0026",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "Tricine",
      "old_amount": {
        "value": "4.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Tricine",
        "source_label": "Tricine",
        "source_value": "4",
        "source_unit": "mM",
        "value_mM": "4",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "Sodium acetate",
      "old_amount": {
        "value": "15.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium acetate",
        "source_label": "Na-acetate",
        "source_value": "15",
        "source_unit": "mM",
        "value_mM": "15",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Potassium dihydrogen phosphate",
      "old_amount": {
        "value": "1.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium dihydrogen phosphate",
        "source_label": "KH2PO4",
        "source_value": "1.3",
        "source_unit": "mM",
        "value_mM": "1.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "Ferrous sulfate",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ferrous sulfate",
        "source_label": "FeSO4",
        "source_value": "0.01",
        "source_unit": "mM",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Folate",
      "old_amount": {
        "value": "0.0023",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Folate",
        "source_label": "folic acid",
        "source_value": "2.3",
        "source_unit": "micromolar",
        "value_mM": "0.0023",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[20].concentration",
      "ingredient": "L-Isoleucine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Isoleucine",
        "source_label": "L-Isoleucine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[21].concentration",
      "ingredient": "Pyridoxal HCl",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pyridoxal HCl",
        "source_label": "pyridoxal-HCl",
        "source_value": "10",
        "source_unit": "micromolar",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[22].concentration",
      "ingredient": "Cupric sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cupric sulfate",
        "source_label": "CuSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[23].concentration",
      "ingredient": "Cobalt chloride",
      "old_amount": {
        "value": "3e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cobalt chloride",
        "source_label": "CoCl2",
        "source_value": "0.03",
        "source_unit": "micromolar",
        "value_mM": "0.00003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[24].concentration",
      "ingredient": "Magnesium chloride",
      "old_amount": {
        "value": "0.52",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Magnesium chloride",
        "source_label": "MgCl2",
        "source_value": "0.52",
        "source_unit": "mM",
        "value_mM": "0.52",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[25].concentration",
      "ingredient": "Manganese chloride",
      "old_amount": {
        "value": "8e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Manganese chloride",
        "source_label": "MnCl2",
        "source_value": "0.08",
        "source_unit": "micromolar",
        "value_mM": "0.00008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[26].concentration",
      "ingredient": "Boric acid",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Boric acid",
        "source_label": "H3BO3",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[27].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "old_amount": {
        "value": "0.0005",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Calcium chloride anhydrous",
        "source_label": "CaCl2",
        "source_value": "0.0005",
        "source_unit": "mM",
        "value_mM": "0.0005",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[28].concentration",
      "ingredient": "Glucose",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Glucose",
        "source_label": "Glucose",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[29].concentration",
      "ingredient": "Potassium sulfate",
      "old_amount": {
        "value": "0.28",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium sulfate",
        "source_label": "K2SO4",
        "source_value": "0.28",
        "source_unit": "mM",
        "value_mM": "0.28",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[30].concentration",
      "ingredient": "Molybdic acid ammonium salt tetrahydrate",
      "old_amount": {
        "value": "3e-06",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Molybdic acid ammonium salt tetrahydrate",
        "source_label": "molybdate trace, printed formula unresolved",
        "source_value": "0.003",
        "source_unit": "micromolar",
        "value_mM": "0.000003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[31].concentration",
      "ingredient": "Ammonium chloride",
      "old_amount": {
        "value": "9.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ammonium chloride",
        "source_label": "NH4Cl",
        "source_value": "9.5",
        "source_unit": "mM",
        "value_mM": "9.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[32].concentration",
      "ingredient": "Zinc sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Zinc sulfate",
        "source_label": "ZnSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    }
  ],
  "variant_field": "variants[0]",
  "old_variant": null,
  "action": "add",
  "variant": {
    "name": "Jensen 1993 BL Medium + Arg reported preparation",
    "description": "Historical Table 3 liquid-culture treatment with the source's preparation and pantothenate form. Numerical parent amounts match the selected Table 1/3 treatment, but unresolved hydrate details are not asserted as exact parent equivalence. This preparation-qualified inline variant does not duplicate or replace the existing BL/low-MOPS full-record relationship.",
    "modifications": [
      "Use the paper's stock-solution filtration through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer filtration of the complete mixture; no additional final-medium sterilization step is inferred.",
      "Use calcium pantothenate as specified in the text; Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar calcium salt or add an inferred calcium concentration.",
      "Keep the published nominal molar formulation from Table 1 and this Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate labels are not promoted to verified study identities. No mass or hydrate conversion is performed.",
      "Retain this existing treatment dose: L-Arginine 1.1 mM. Table 3 footnote b points to the Table 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows state their own doses. No new base-versus-child link is created."
    ],
    "purpose": "Reported liquid batch-culture treatment for MG1363.",
    "evidence": [
      {
        "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
        "supports": "SUPPORT",
        "snippet": "All stock solutions were passed through Millipore filters (0.2-μm pore size).",
        "explanation": "Locator: page 4363, Growth on plates containing eight amino acids, preparation paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid treatment +Arg. All numeric ingredient amounts were compared with the original scans; micromolar footnote values were divided by 1000 solely for comparison to existing mM fields. No parent amount was rewritten. The printed molybdate formula/hydration remains unresolved; no unsupported exact chemical identity is claimed."
      }
    ]
  },
  "parent_amounts_changed": false,
  "conversion": "No mass, density, hydrate or stock dilution conversion. Jensen micromolar-to-mM comparison divides by1000; original facts and basis remain explicit.",
  "scope": "All direct ingredients; none of these parents contains nested solutions. The Mattanovich added variant retains an explicit trace stock in modification prose."
}

### Scientific name, current taxonomy and growth scope

grounding: supported. Targets: CultureMech:007303.

Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain; Table3 growth is variant-only.

{
  "preferred_term": "Lactococcus lactis subsp. lactis",
  "term": {
    "id": "NCBITaxon:416870",
    "label": "Lactococcus cremoris subsp. cremoris MG1363"
  },
  "strain": "MG1363",
  "scoped_to_variant": "Jensen 1993 BL Medium + Arg reported preparation",
  "evidence": [
    {
      "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "supports": "SUPPORT",
      "snippet": "MG1363 in unaerated batch cultures of BL medium or modified BL medium",
      "explanation": "Locator: original page 4364, Table 3 caption and treatment row +Arg; that row reports positive growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis. No growth-rate value, OD conversion, pH optimum or broad species growth assertion is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870. The historical subspecies wording differs from current taxonomy; retain it as the reported name, not a current classification. No equivalence between all historical L. lactis strains and L. cremoris is inferred."
    }
  ]
}

### Source-specific formulation and parent preservation

quantity: supported. Targets: CultureMech:007304.

Selected BL liquid treatment is represented as preparation-qualified variant; numerical agreement is not exact chemical-form equivalence.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "L-Leucine",
      "old_amount": {
        "value": "1.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Leucine",
        "source_label": "L-Leucine",
        "source_value": "1.5",
        "source_unit": "mM",
        "value_mM": "1.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Potassium sulfate",
      "old_amount": {
        "value": "0.28",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium sulfate",
        "source_label": "K2SO4",
        "source_value": "0.28",
        "source_unit": "mM",
        "value_mM": "0.28",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "Sodium chloride",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium chloride",
        "source_label": "NaCl",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "L-Isoleucine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Isoleucine",
        "source_label": "L-Isoleucine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Folate",
      "old_amount": {
        "value": "0.0023",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Folate",
        "source_label": "folic acid",
        "source_value": "2.3",
        "source_unit": "micromolar",
        "value_mM": "0.0023",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "Pyridoxal HCl",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pyridoxal HCl",
        "source_label": "pyridoxal-HCl",
        "source_value": "10",
        "source_unit": "micromolar",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "L-Glutamine",
      "old_amount": {
        "value": "0.7",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamine",
        "source_label": "L-Glutamine",
        "source_value": "0.7",
        "source_unit": "mM",
        "value_mM": "0.7",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Tricine",
      "old_amount": {
        "value": "4.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Tricine",
        "source_label": "Tricine",
        "source_value": "4",
        "source_unit": "mM",
        "value_mM": "4",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "L-Aspartate",
      "old_amount": {
        "value": "1.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "source_value_mM": "1.0",
        "locator": "pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "L-Histidine",
      "old_amount": {
        "value": "0.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Histidine",
        "source_label": "L-Histidine",
        "source_value": "0.3",
        "source_unit": "mM",
        "value_mM": "0.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "L-Methionine",
      "old_amount": {
        "value": "0.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Methionine",
        "source_label": "L-Methionine",
        "source_value": "0.5",
        "source_unit": "mM",
        "value_mM": "0.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "L-Glutamate",
      "old_amount": {
        "value": "21.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamate",
        "source_label": "L-Glutamate",
        "source_value": "21",
        "source_unit": "mM",
        "value_mM": "21",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "L-Asparagine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Asparagine",
        "source_label": "L-Asparagine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "Biotin",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Biotin",
        "source_label": "biotin",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Nicotinamide",
      "old_amount": {
        "value": "0.008",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Nicotinamide",
        "source_label": "niacinamide",
        "source_value": "8",
        "source_unit": "micromolar",
        "value_mM": "0.008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "Cupric sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cupric sulfate",
        "source_label": "CuSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "MOPS",
      "old_amount": {
        "value": "190.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "MOPS",
        "source_label": "MOPS",
        "source_value": "190",
        "source_unit": "mM",
        "value_mM": "190",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Potassium dihydrogen phosphate",
      "old_amount": {
        "value": "1.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium dihydrogen phosphate",
        "source_label": "KH2PO4",
        "source_value": "1.3",
        "source_unit": "mM",
        "value_mM": "1.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "Thiamine HCl",
      "old_amount": {
        "value": "0.003",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Thiamine HCl",
        "source_label": "thiamine-HCl",
        "source_value": "3",
        "source_unit": "micromolar",
        "value_mM": "0.003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Glucose",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Glucose",
        "source_label": "Glucose",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[20].concentration",
      "ingredient": "Riboflavin",
      "old_amount": {
        "value": "0.0026",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Riboflavin",
        "source_label": "riboflavin",
        "source_value": "2.6",
        "source_unit": "micromolar",
        "value_mM": "0.0026",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[21].concentration",
      "ingredient": "L-Valine",
      "old_amount": {
        "value": "2.6",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Valine",
        "source_label": "L-Valine",
        "source_value": "2.6",
        "source_unit": "mM",
        "value_mM": "2.6",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[22].concentration",
      "ingredient": "Ferrous sulfate",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ferrous sulfate",
        "source_label": "FeSO4",
        "source_value": "0.01",
        "source_unit": "mM",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[23].concentration",
      "ingredient": "Cobalt chloride",
      "old_amount": {
        "value": "3e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cobalt chloride",
        "source_label": "CoCl2",
        "source_value": "0.03",
        "source_unit": "micromolar",
        "value_mM": "0.00003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[24].concentration",
      "ingredient": "Zinc sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Zinc sulfate",
        "source_label": "ZnSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[25].concentration",
      "ingredient": "Manganese chloride",
      "old_amount": {
        "value": "8e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Manganese chloride",
        "source_label": "MnCl2",
        "source_value": "0.08",
        "source_unit": "micromolar",
        "value_mM": "0.00008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[26].concentration",
      "ingredient": "Magnesium chloride",
      "old_amount": {
        "value": "0.52",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Magnesium chloride",
        "source_label": "MgCl2",
        "source_value": "0.52",
        "source_unit": "mM",
        "value_mM": "0.52",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[27].concentration",
      "ingredient": "Pantothenate",
      "old_amount": {
        "value": "0.002",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pantothenate",
        "source_label": "pantothenate",
        "source_value": "2",
        "source_unit": "micromolar",
        "value_mM": "0.002",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[28].concentration",
      "ingredient": "Boric acid",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Boric acid",
        "source_label": "H3BO3",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[29].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "old_amount": {
        "value": "0.0005",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Calcium chloride anhydrous",
        "source_label": "CaCl2",
        "source_value": "0.0005",
        "source_unit": "mM",
        "value_mM": "0.0005",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[30].concentration",
      "ingredient": "Molybdic acid ammonium salt tetrahydrate",
      "old_amount": {
        "value": "3e-06",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Molybdic acid ammonium salt tetrahydrate",
        "source_label": "molybdate trace, printed formula unresolved",
        "source_value": "0.003",
        "source_unit": "micromolar",
        "value_mM": "0.000003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[31].concentration",
      "ingredient": "Ammonium chloride",
      "old_amount": {
        "value": "9.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ammonium chloride",
        "source_label": "NH4Cl",
        "source_value": "9.5",
        "source_unit": "mM",
        "value_mM": "9.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[32].concentration",
      "ingredient": "Sodium acetate",
      "old_amount": {
        "value": "15.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium acetate",
        "source_label": "Na-acetate",
        "source_value": "15",
        "source_unit": "mM",
        "value_mM": "15",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    }
  ],
  "variant_field": "variants[0]",
  "old_variant": null,
  "action": "add",
  "variant": {
    "name": "Jensen 1993 BL Medium + Asp reported preparation",
    "description": "Historical Table 3 liquid-culture treatment with the source's preparation and pantothenate form. Numerical parent amounts match the selected Table 1/3 treatment, but unresolved hydrate details are not asserted as exact parent equivalence. This preparation-qualified inline variant does not duplicate or replace the existing BL/low-MOPS full-record relationship.",
    "modifications": [
      "Use the paper's stock-solution filtration through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer filtration of the complete mixture; no additional final-medium sterilization step is inferred.",
      "Use calcium pantothenate as specified in the text; Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar calcium salt or add an inferred calcium concentration.",
      "Keep the published nominal molar formulation from Table 1 and this Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate labels are not promoted to verified study identities. No mass or hydrate conversion is performed.",
      "Retain this existing treatment dose: L-Aspartate 1.0 mM. Table 3 footnote b points to the Table 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows state their own doses. No new base-versus-child link is created."
    ],
    "purpose": "Reported liquid batch-culture treatment for MG1363.",
    "evidence": [
      {
        "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
        "supports": "SUPPORT",
        "snippet": "All stock solutions were passed through Millipore filters (0.2-μm pore size).",
        "explanation": "Locator: page 4363, Growth on plates containing eight amino acids, preparation paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid treatment +Asp (1 mM). All numeric ingredient amounts were compared with the original scans; micromolar footnote values were divided by 1000 solely for comparison to existing mM fields. No parent amount was rewritten. The printed molybdate formula/hydration remains unresolved; no unsupported exact chemical identity is claimed."
      }
    ]
  },
  "parent_amounts_changed": false,
  "conversion": "No mass, density, hydrate or stock dilution conversion. Jensen micromolar-to-mM comparison divides by1000; original facts and basis remain explicit.",
  "scope": "All direct ingredients; none of these parents contains nested solutions. The Mattanovich added variant retains an explicit trace stock in modification prose."
}

### Scientific name, current taxonomy and growth scope

grounding: supported. Targets: CultureMech:007304.

Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain; Table3 growth is variant-only.

{
  "preferred_term": "Lactococcus lactis subsp. lactis",
  "term": {
    "id": "NCBITaxon:416870",
    "label": "Lactococcus cremoris subsp. cremoris MG1363"
  },
  "strain": "MG1363",
  "scoped_to_variant": "Jensen 1993 BL Medium + Asp reported preparation",
  "evidence": [
    {
      "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "supports": "SUPPORT",
      "snippet": "MG1363 in unaerated batch cultures of BL medium or modified BL medium",
      "explanation": "Locator: original page 4364, Table 3 caption and treatment row +Asp (1 mM); that row reports positive growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis. No growth-rate value, OD conversion, pH optimum or broad species growth assertion is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870. The historical subspecies wording differs from current taxonomy; retain it as the reported name, not a current classification. No equivalence between all historical L. lactis strains and L. cremoris is inferred."
    }
  ]
}

### Source-specific formulation and parent preservation

quantity: supported. Targets: CultureMech:007305.

Selected BL liquid treatment is represented as preparation-qualified variant; numerical agreement is not exact chemical-form equivalence.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "L-Leucine",
      "old_amount": {
        "value": "1.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Leucine",
        "source_label": "L-Leucine",
        "source_value": "1.5",
        "source_unit": "mM",
        "value_mM": "1.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Potassium sulfate",
      "old_amount": {
        "value": "0.28",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium sulfate",
        "source_label": "K2SO4",
        "source_value": "0.28",
        "source_unit": "mM",
        "value_mM": "0.28",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "Sodium chloride",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium chloride",
        "source_label": "NaCl",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "L-Isoleucine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Isoleucine",
        "source_label": "L-Isoleucine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Folate",
      "old_amount": {
        "value": "0.0023",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Folate",
        "source_label": "folic acid",
        "source_value": "2.3",
        "source_unit": "micromolar",
        "value_mM": "0.0023",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "Pyridoxal HCl",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pyridoxal HCl",
        "source_label": "pyridoxal-HCl",
        "source_value": "10",
        "source_unit": "micromolar",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "L-Glutamine",
      "old_amount": {
        "value": "0.7",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamine",
        "source_label": "L-Glutamine",
        "source_value": "0.7",
        "source_unit": "mM",
        "value_mM": "0.7",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Tricine",
      "old_amount": {
        "value": "4.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Tricine",
        "source_label": "Tricine",
        "source_value": "4",
        "source_unit": "mM",
        "value_mM": "4",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "L-Histidine",
      "old_amount": {
        "value": "0.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Histidine",
        "source_label": "L-Histidine",
        "source_value": "0.3",
        "source_unit": "mM",
        "value_mM": "0.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "L-Methionine",
      "old_amount": {
        "value": "0.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Methionine",
        "source_label": "L-Methionine",
        "source_value": "0.5",
        "source_unit": "mM",
        "value_mM": "0.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "L-Glutamate",
      "old_amount": {
        "value": "21.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamate",
        "source_label": "L-Glutamate",
        "source_value": "21",
        "source_unit": "mM",
        "value_mM": "21",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "L-Asparagine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Asparagine",
        "source_label": "L-Asparagine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "Biotin",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Biotin",
        "source_label": "biotin",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "Nicotinamide",
      "old_amount": {
        "value": "0.008",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Nicotinamide",
        "source_label": "niacinamide",
        "source_value": "8",
        "source_unit": "micromolar",
        "value_mM": "0.008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "Cupric sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cupric sulfate",
        "source_label": "CuSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "MOPS",
      "old_amount": {
        "value": "40.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "source_value_mM": "40",
        "locator": "pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "Potassium dihydrogen phosphate",
      "old_amount": {
        "value": "1.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium dihydrogen phosphate",
        "source_label": "KH2PO4",
        "source_value": "1.3",
        "source_unit": "mM",
        "value_mM": "1.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Thiamine HCl",
      "old_amount": {
        "value": "0.003",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Thiamine HCl",
        "source_label": "thiamine-HCl",
        "source_value": "3",
        "source_unit": "micromolar",
        "value_mM": "0.003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "Glucose",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Glucose",
        "source_label": "Glucose",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Riboflavin",
      "old_amount": {
        "value": "0.0026",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Riboflavin",
        "source_label": "riboflavin",
        "source_value": "2.6",
        "source_unit": "micromolar",
        "value_mM": "0.0026",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[20].concentration",
      "ingredient": "L-Valine",
      "old_amount": {
        "value": "2.6",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Valine",
        "source_label": "L-Valine",
        "source_value": "2.6",
        "source_unit": "mM",
        "value_mM": "2.6",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[21].concentration",
      "ingredient": "Ferrous sulfate",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ferrous sulfate",
        "source_label": "FeSO4",
        "source_value": "0.01",
        "source_unit": "mM",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[22].concentration",
      "ingredient": "Cobalt chloride",
      "old_amount": {
        "value": "3e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cobalt chloride",
        "source_label": "CoCl2",
        "source_value": "0.03",
        "source_unit": "micromolar",
        "value_mM": "0.00003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[23].concentration",
      "ingredient": "Zinc sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Zinc sulfate",
        "source_label": "ZnSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[24].concentration",
      "ingredient": "Manganese chloride",
      "old_amount": {
        "value": "8e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Manganese chloride",
        "source_label": "MnCl2",
        "source_value": "0.08",
        "source_unit": "micromolar",
        "value_mM": "0.00008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[25].concentration",
      "ingredient": "Magnesium chloride",
      "old_amount": {
        "value": "0.52",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Magnesium chloride",
        "source_label": "MgCl2",
        "source_value": "0.52",
        "source_unit": "mM",
        "value_mM": "0.52",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[26].concentration",
      "ingredient": "Pantothenate",
      "old_amount": {
        "value": "0.002",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pantothenate",
        "source_label": "pantothenate",
        "source_value": "2",
        "source_unit": "micromolar",
        "value_mM": "0.002",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[27].concentration",
      "ingredient": "Boric acid",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Boric acid",
        "source_label": "H3BO3",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[28].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "old_amount": {
        "value": "0.0005",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Calcium chloride anhydrous",
        "source_label": "CaCl2",
        "source_value": "0.0005",
        "source_unit": "mM",
        "value_mM": "0.0005",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[29].concentration",
      "ingredient": "Molybdic acid ammonium salt tetrahydrate",
      "old_amount": {
        "value": "3e-06",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Molybdic acid ammonium salt tetrahydrate",
        "source_label": "molybdate trace, printed formula unresolved",
        "source_value": "0.003",
        "source_unit": "micromolar",
        "value_mM": "0.000003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[30].concentration",
      "ingredient": "Ammonium chloride",
      "old_amount": {
        "value": "9.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ammonium chloride",
        "source_label": "NH4Cl",
        "source_value": "9.5",
        "source_unit": "mM",
        "value_mM": "9.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[31].concentration",
      "ingredient": "Sodium acetate",
      "old_amount": {
        "value": "15.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium acetate",
        "source_label": "Na-acetate",
        "source_value": "15",
        "source_unit": "mM",
        "value_mM": "15",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    }
  ],
  "variant_field": "variants[0]",
  "old_variant": null,
  "action": "add",
  "variant": {
    "name": "Jensen 1993 BL Medium, Low MOPS reported preparation",
    "description": "Historical Table 3 liquid-culture treatment with the source's preparation and pantothenate form. Numerical parent amounts match the selected Table 1/3 treatment, but unresolved hydrate details are not asserted as exact parent equivalence. This preparation-qualified inline variant does not duplicate or replace the existing BL/low-MOPS full-record relationship.",
    "modifications": [
      "Use the paper's stock-solution filtration through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer filtration of the complete mixture; no additional final-medium sterilization step is inferred.",
      "Use calcium pantothenate as specified in the text; Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar calcium salt or add an inferred calcium concentration.",
      "Keep the published nominal molar formulation from Table 1 and this Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate labels are not promoted to verified study identities. No mass or hydrate conversion is performed.",
      "Retain this existing treatment dose: MOPS 40 mM. Table 3 footnote b points to the Table 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows state their own doses. No new base-versus-child link is created."
    ],
    "purpose": "Reported liquid batch-culture treatment for MG1363.",
    "evidence": [
      {
        "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
        "supports": "SUPPORT",
        "snippet": "All stock solutions were passed through Millipore filters (0.2-μm pore size).",
        "explanation": "Locator: page 4363, Growth on plates containing eight amino acids, preparation paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid treatment Low MOPS (0.04 M). All numeric ingredient amounts were compared with the original scans; micromolar footnote values were divided by 1000 solely for comparison to existing mM fields. No parent amount was rewritten. The printed molybdate formula/hydration remains unresolved; no unsupported exact chemical identity is claimed."
      }
    ]
  },
  "parent_amounts_changed": false,
  "conversion": "No mass, density, hydrate or stock dilution conversion. Jensen micromolar-to-mM comparison divides by1000; original facts and basis remain explicit.",
  "scope": "All direct ingredients; none of these parents contains nested solutions. The Mattanovich added variant retains an explicit trace stock in modification prose."
}

### Scientific name, current taxonomy and growth scope

grounding: supported. Targets: CultureMech:007305.

Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain; Table3 growth is variant-only.

{
  "preferred_term": "Lactococcus lactis subsp. lactis",
  "term": {
    "id": "NCBITaxon:416870",
    "label": "Lactococcus cremoris subsp. cremoris MG1363"
  },
  "strain": "MG1363",
  "scoped_to_variant": "Jensen 1993 BL Medium, Low MOPS reported preparation",
  "evidence": [
    {
      "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "supports": "SUPPORT",
      "snippet": "MG1363 in unaerated batch cultures of BL medium or modified BL medium",
      "explanation": "Locator: original page 4364, Table 3 caption and treatment row Low MOPS (0.04 M); that row reports positive growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis. No growth-rate value, OD conversion, pH optimum or broad species growth assertion is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870. The historical subspecies wording differs from current taxonomy; retain it as the reported name, not a current classification. No equivalence between all historical L. lactis strains and L. cremoris is inferred."
    }
  ]
}

### Source-specific formulation and parent preservation

quantity: supported. Targets: CultureMech:007306.

Selected BL liquid treatment is represented as preparation-qualified variant; numerical agreement is not exact chemical-form equivalence.

{
  "parent_ingredient_comparisons": [
    {
      "field_path": "ingredients[0].concentration",
      "ingredient": "L-Leucine",
      "old_amount": {
        "value": "1.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Leucine",
        "source_label": "L-Leucine",
        "source_value": "1.5",
        "source_unit": "mM",
        "value_mM": "1.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[1].concentration",
      "ingredient": "Potassium sulfate",
      "old_amount": {
        "value": "0.28",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium sulfate",
        "source_label": "K2SO4",
        "source_value": "0.28",
        "source_unit": "mM",
        "value_mM": "0.28",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[2].concentration",
      "ingredient": "Sodium chloride",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium chloride",
        "source_label": "NaCl",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[3].concentration",
      "ingredient": "L-Isoleucine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Isoleucine",
        "source_label": "L-Isoleucine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[4].concentration",
      "ingredient": "Folate",
      "old_amount": {
        "value": "0.0023",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Folate",
        "source_label": "folic acid",
        "source_value": "2.3",
        "source_unit": "micromolar",
        "value_mM": "0.0023",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[5].concentration",
      "ingredient": "L-Tryptophan",
      "old_amount": {
        "value": "0.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "source_value_mM": "0.5",
        "locator": "pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[6].concentration",
      "ingredient": "L-Serine",
      "old_amount": {
        "value": "2.9",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "source_value_mM": "2.9",
        "locator": "pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[7].concentration",
      "ingredient": "Pyridoxal HCl",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pyridoxal HCl",
        "source_label": "pyridoxal-HCl",
        "source_value": "10",
        "source_unit": "micromolar",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[8].concentration",
      "ingredient": "L-Glutamine",
      "old_amount": {
        "value": "0.7",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamine",
        "source_label": "L-Glutamine",
        "source_value": "0.7",
        "source_unit": "mM",
        "value_mM": "0.7",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[9].concentration",
      "ingredient": "Tricine",
      "old_amount": {
        "value": "4.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Tricine",
        "source_label": "Tricine",
        "source_value": "4",
        "source_unit": "mM",
        "value_mM": "4",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[10].concentration",
      "ingredient": "L-Arginine",
      "old_amount": {
        "value": "1.1",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "source_value_mM": "1.1",
        "locator": "pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[11].concentration",
      "ingredient": "L-Histidine",
      "old_amount": {
        "value": "0.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Histidine",
        "source_label": "L-Histidine",
        "source_value": "0.3",
        "source_unit": "mM",
        "value_mM": "0.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[12].concentration",
      "ingredient": "L-Methionine",
      "old_amount": {
        "value": "0.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Methionine",
        "source_label": "L-Methionine",
        "source_value": "0.5",
        "source_unit": "mM",
        "value_mM": "0.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[13].concentration",
      "ingredient": "L-Glutamate",
      "old_amount": {
        "value": "21.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Glutamate",
        "source_label": "L-Glutamate",
        "source_value": "21",
        "source_unit": "mM",
        "value_mM": "21",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[14].concentration",
      "ingredient": "L-Asparagine",
      "old_amount": {
        "value": "0.8",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Asparagine",
        "source_label": "L-Asparagine",
        "source_value": "0.8",
        "source_unit": "mM",
        "value_mM": "0.8",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[15].concentration",
      "ingredient": "Biotin",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Biotin",
        "source_label": "biotin",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[16].concentration",
      "ingredient": "Nicotinamide",
      "old_amount": {
        "value": "0.008",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Nicotinamide",
        "source_label": "niacinamide",
        "source_value": "8",
        "source_unit": "micromolar",
        "value_mM": "0.008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[17].concentration",
      "ingredient": "Cupric sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cupric sulfate",
        "source_label": "CuSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[18].concentration",
      "ingredient": "MOPS",
      "old_amount": {
        "value": "190.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "MOPS",
        "source_label": "MOPS",
        "source_value": "190",
        "source_unit": "mM",
        "value_mM": "190",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[19].concentration",
      "ingredient": "Potassium dihydrogen phosphate",
      "old_amount": {
        "value": "1.3",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Potassium dihydrogen phosphate",
        "source_label": "KH2PO4",
        "source_value": "1.3",
        "source_unit": "mM",
        "value_mM": "1.3",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[20].concentration",
      "ingredient": "Thiamine HCl",
      "old_amount": {
        "value": "0.003",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Thiamine HCl",
        "source_label": "thiamine-HCl",
        "source_value": "3",
        "source_unit": "micromolar",
        "value_mM": "0.003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[21].concentration",
      "ingredient": "Glucose",
      "old_amount": {
        "value": "50.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Glucose",
        "source_label": "Glucose",
        "source_value": "50",
        "source_unit": "mM",
        "value_mM": "50",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[22].concentration",
      "ingredient": "Riboflavin",
      "old_amount": {
        "value": "0.0026",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Riboflavin",
        "source_label": "riboflavin",
        "source_value": "2.6",
        "source_unit": "micromolar",
        "value_mM": "0.0026",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[23].concentration",
      "ingredient": "L-Valine",
      "old_amount": {
        "value": "2.6",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "L-Valine",
        "source_label": "L-Valine",
        "source_value": "2.6",
        "source_unit": "mM",
        "value_mM": "2.6",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[24].concentration",
      "ingredient": "Ferrous sulfate",
      "old_amount": {
        "value": "0.01",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ferrous sulfate",
        "source_label": "FeSO4",
        "source_value": "0.01",
        "source_unit": "mM",
        "value_mM": "0.01",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[25].concentration",
      "ingredient": "Cobalt chloride",
      "old_amount": {
        "value": "3e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Cobalt chloride",
        "source_label": "CoCl2",
        "source_value": "0.03",
        "source_unit": "micromolar",
        "value_mM": "0.00003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[26].concentration",
      "ingredient": "Zinc sulfate",
      "old_amount": {
        "value": "1e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Zinc sulfate",
        "source_label": "ZnSO4",
        "source_value": "0.01",
        "source_unit": "micromolar",
        "value_mM": "0.00001",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[27].concentration",
      "ingredient": "Manganese chloride",
      "old_amount": {
        "value": "8e-05",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Manganese chloride",
        "source_label": "MnCl2",
        "source_value": "0.08",
        "source_unit": "micromolar",
        "value_mM": "0.00008",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[28].concentration",
      "ingredient": "Magnesium chloride",
      "old_amount": {
        "value": "0.52",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Magnesium chloride",
        "source_label": "MgCl2",
        "source_value": "0.52",
        "source_unit": "mM",
        "value_mM": "0.52",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[29].concentration",
      "ingredient": "Pantothenate",
      "old_amount": {
        "value": "0.002",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Pantothenate",
        "source_label": "pantothenate",
        "source_value": "2",
        "source_unit": "micromolar",
        "value_mM": "0.002",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[30].concentration",
      "ingredient": "Boric acid",
      "old_amount": {
        "value": "0.0004",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Boric acid",
        "source_label": "H3BO3",
        "source_value": "0.4",
        "source_unit": "micromolar",
        "value_mM": "0.0004",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[31].concentration",
      "ingredient": "Calcium chloride anhydrous",
      "old_amount": {
        "value": "0.0005",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Calcium chloride anhydrous",
        "source_label": "CaCl2",
        "source_value": "0.0005",
        "source_unit": "mM",
        "value_mM": "0.0005",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[32].concentration",
      "ingredient": "Molybdic acid ammonium salt tetrahydrate",
      "old_amount": {
        "value": "3e-06",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Molybdic acid ammonium salt tetrahydrate",
        "source_label": "molybdate trace, printed formula unresolved",
        "source_value": "0.003",
        "source_unit": "micromolar",
        "value_mM": "0.000003",
        "locator": "page 4363, Table 1 footnote b or c",
        "calculation": "1 micromolar = 0.001 mM"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[33].concentration",
      "ingredient": "Ammonium chloride",
      "old_amount": {
        "value": "9.5",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Ammonium chloride",
        "source_label": "NH4Cl",
        "source_value": "9.5",
        "source_unit": "mM",
        "value_mM": "9.5",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    },
    {
      "field_path": "ingredients[34].concentration",
      "ingredient": "Sodium acetate",
      "old_amount": {
        "value": "15.0",
        "unit": "MILLIMOLAR"
      },
      "status": "evidence_only",
      "qualification": "Numerical comparison only, not chemical-form or whole-parent certification; evidence attached to the preparation-qualified variant.",
      "source_reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "source_fact": {
        "record_label": "Sodium acetate",
        "source_label": "Na-acetate",
        "source_value": "15",
        "source_unit": "mM",
        "value_mM": "15",
        "locator": "page 4363, Table 1 BL column",
        "calculation": "No conversion"
      },
      "action": "parent unchanged; variant evidence added",
      "proposed_parent_amount": null
    }
  ],
  "variant_field": "variants[0]",
  "old_variant": null,
  "action": "add",
  "variant": {
    "name": "Jensen 1993 BL Medium + Arg + Ser + Trp reported preparation",
    "description": "Historical Table 3 liquid-culture treatment with the source's preparation and pantothenate form. Numerical parent amounts match the selected Table 1/3 treatment, but unresolved hydrate details are not asserted as exact parent equivalence. This preparation-qualified inline variant does not duplicate or replace the existing BL/low-MOPS full-record relationship.",
    "modifications": [
      "Use the paper's stock-solution filtration through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer filtration of the complete mixture; no additional final-medium sterilization step is inferred.",
      "Use calcium pantothenate as specified in the text; Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar calcium salt or add an inferred calcium concentration.",
      "Keep the published nominal molar formulation from Table 1 and this Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate labels are not promoted to verified study identities. No mass or hydrate conversion is performed.",
      "Retain this existing treatment dose: L-Arginine 1.1 mM, L-Serine 2.9 mM, L-Tryptophan 0.5 mM. Table 3 footnote b points to the Table 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows state their own doses. No new base-versus-child link is created."
    ],
    "purpose": "Reported liquid batch-culture treatment for MG1363.",
    "evidence": [
      {
        "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
        "supports": "SUPPORT",
        "snippet": "All stock solutions were passed through Millipore filters (0.2-μm pore size).",
        "explanation": "Locator: page 4363, Growth on plates containing eight amino acids, preparation paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid treatment +Arg, Ser, and Trp. All numeric ingredient amounts were compared with the original scans; micromolar footnote values were divided by 1000 solely for comparison to existing mM fields. No parent amount was rewritten. The printed molybdate formula/hydration remains unresolved; no unsupported exact chemical identity is claimed."
      }
    ]
  },
  "parent_amounts_changed": false,
  "conversion": "No mass, density, hydrate or stock dilution conversion. Jensen micromolar-to-mM comparison divides by1000; original facts and basis remain explicit.",
  "scope": "All direct ingredients; none of these parents contains nested solutions. The Mattanovich added variant retains an explicit trace stock in modification prose."
}

### Scientific name, current taxonomy and growth scope

grounding: supported. Targets: CultureMech:007306.

Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain; Table3 growth is variant-only.

{
  "preferred_term": "Lactococcus lactis subsp. lactis",
  "term": {
    "id": "NCBITaxon:416870",
    "label": "Lactococcus cremoris subsp. cremoris MG1363"
  },
  "strain": "MG1363",
  "scoped_to_variant": "Jensen 1993 BL Medium + Arg + Ser + Trp reported preparation",
  "evidence": [
    {
      "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
      "supports": "SUPPORT",
      "snippet": "MG1363 in unaerated batch cultures of BL medium or modified BL medium",
      "explanation": "Locator: original page 4364, Table 3 caption and treatment row +Arg, Ser, and Trp; that row reports positive growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis. No growth-rate value, OD conversion, pH optimum or broad species growth assertion is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870. The historical subspecies wording differs from current taxonomy; retain it as the reported name, not a current classification. No equivalence between all historical L. lactis strains and L. cremoris is inferred."
    }
  ]
}

### Unresolved parent chemistry and preparation

evidence: concern. Targets: CultureMech:007250, CultureMech:007302, CultureMech:007303, CultureMech:007304, CultureMech:007305, CultureMech:007306.

Parent molar conversions/acid density, salt hydration and preparation cannot all be certified. The variants explicitly retain source units and qualification; no hidden normalization or blanket parent approval.

## Findings

### variant-export: KGX drops these six inline variant scopes

major / open / confirmed; issue key: kgx-variant-growth-scope-loss-original-papers.

YAML scopes the observations correctly, but current edge construction emits the parent medium ID. Withholding publication is a mitigation, not an exporter repair.

### fungal-category: Yeast cultivation record retains bacterial category

major / open / confirmed; issue key: mattanovich-batch-fungal-category-007250.

The record remains category bacterial although the source organism is the yeast Komagataella pastoris. This pre-existing routing/classification mismatch was retained during citation-only curation, not endorsed.

## Recommended Actions And Acceptance Checks

### preserve-variant-export

Repair or fail closed on variant-scoped growth before publishing.

- None of these parent records receives a variant-only growth edge.
- Tests retain valid ordinary unscoped growth and explicitly cover variant scope.

### review-fungal-category

Correct the yeast recipe category through a separately scoped ownership and path/link audit.

- Permanent ID and all inbound links survive any relocation.
- Category matches documented fungal cultivation and maintained record validators pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| mattanovich | doi:10.1186/1475-2859-8-29; Material and methods, Strain; Experimental secretome analysis; PMID19490607 | supports | Full HTML and Markdown inspected; strain and experimental-secretome methods explicitly support glucose chemostat cultivation, not the glycerol batch parent. PubMed title/authors/year/DOI agree; no correction/retraction notice in the archived XML. |
| supplement | doi:10.1186/1475-2859-8-29; Additional file 3, Fermentation data and Analysis: A2:A11 batch, A13:A22 chemostat, A24:A33 trace stock, A35:A40 conditions | supports | Original publisher XLS read with xlrd; all nonempty cells rendered to addressable Markdown. Literal A-column text, not computed results, supports separate batch/chemostat recipes and shared trace stock. Stock quantities are not final-medium quantities. |
| jensen | doi:10.1128/aem.59.12.4363-4366.1993; Original pages 4363-4366; page4363 preparation/Table1 and footnotes, page4364 Table3 caption and selected rows; provenance file pins all four scan hashes | supports | All four original scans visually inspected. Table 1 BL composition and Table 3 liquid treatments support five nominal recipes and positive MG1363 growth. Stock filtration and pantothenate form differ from the imported preparation. PubMed metadata agrees; no correction/retraction notice in archived XML. Scans and abstract Markdown are archived; no full-text PDF or complete OCR transcript is claimed. |
| jensen-facts | doi:10.1128/aem.59.12.4363-4366.1993; Bounded Table1/3 extraction; recipe-extract.md gives readable transcription | supports | Manually checked numerical table facts, not a fabricated contiguous quotation. Micromolar to mM comparison divides by 1000. Hydration and printed molybdate formula remain unresolved; no mass conversion performed. |
| tax-638632 | NCBITaxon:638632; NCBI Taxonomy XML TaxId, ScientificName, Rank, synonyms and LineageEx; retrieved2026-10-13 | supports | Current NCBI XML confirms canonical label Komagataella pastoris DSMZ 70382, rank strain. Historical organism name is retained separately; MG1363 identity is strain-specific despite changed species/subspecies classification. |
| tax-416870 | NCBITaxon:416870; NCBI Taxonomy XML TaxId, ScientificName, Rank, synonyms and LineageEx; retrieved2026-10-13 | supports | Current NCBI XML confirms canonical label Lactococcus cremoris subsp. cremoris MG1363, rank strain. Historical organism name is retained separately; MG1363 identity is strain-specific despite changed species/subspecies classification. |
| other-strains | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy; Four All Names queries combined with OR; genus verified in MG1363 archived lineage | context_only | Bounded exact-name queries for NCDO712/NCDO 712 and Lactococcus lactis/cremoris C2 returned no match. This is not proof that no exact taxon exists; the notes use verified genus Lactococcus, NCBITaxon1357, parent_rank_only, with no positive liquid-medium edge. |
| readback | CultureMech six-record curation readback; Guarded before/after record comparison and in-memory organism_grows_in_medium_edge reproduction | context_only | Every previous field and history prefix is unchanged; exactly one event, citation, inline variant and variant-scoped organism were added per target. The in-memory KGX edge builder returns the parent ID and loses scope for all six; no output was published. |
| gate-0 | reports/paper_citation_curation/20261013-original-papers/baseline-00-validate-schema.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-1 | reports/paper_citation_curation/20261013-original-papers/baseline-01-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-2 | reports/paper_citation_curation/20261013-original-papers/baseline-02-validate-schema.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-3 | reports/paper_citation_curation/20261013-original-papers/baseline-03-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-4 | reports/paper_citation_curation/20261013-original-papers/baseline-04-validate-schema.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-5 | reports/paper_citation_curation/20261013-original-papers/baseline-05-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-6 | reports/paper_citation_curation/20261013-original-papers/baseline-06-validate-schema.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-7 | reports/paper_citation_curation/20261013-original-papers/baseline-07-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-8 | reports/paper_citation_curation/20261013-original-papers/baseline-08-validate-schema.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-9 | reports/paper_citation_curation/20261013-original-papers/baseline-09-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-10 | reports/paper_citation_curation/20261013-original-papers/baseline-10-validate-schema.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-11 | reports/paper_citation_curation/20261013-original-papers/baseline-11-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-12 | reports/paper_citation_curation/20261013-original-papers/final-00-validate.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-13 | reports/paper_citation_curation/20261013-original-papers/final-01-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-14 | reports/paper_citation_curation/20261013-original-papers/final-02-validate.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-15 | reports/paper_citation_curation/20261013-original-papers/final-03-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-16 | reports/paper_citation_curation/20261013-original-papers/final-04-validate.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-17 | reports/paper_citation_curation/20261013-original-papers/final-05-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-18 | reports/paper_citation_curation/20261013-original-papers/final-06-validate.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-19 | reports/paper_citation_curation/20261013-original-papers/final-07-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-20 | reports/paper_citation_curation/20261013-original-papers/final-08-validate.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-21 | reports/paper_citation_curation/20261013-original-papers/final-09-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-22 | reports/paper_citation_curation/20261013-original-papers/final-10-validate.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-23 | reports/paper_citation_curation/20261013-original-papers/final-11-validate-strict.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-24 | reports/paper_citation_curation/20261013-original-papers/merge-00-verify-merges.log; Retained complete command output | context_only | Actual exit code 143; automated validation is not scientific approval. |
| gate-25 | reports/paper_citation_curation/20261013-original-papers/merge-01-audit-merge-freshness.log; Retained complete command output | context_only | Actual exit code 1; automated validation is not scientific approval. |
| gate-26 | reports/paper_citation_curation/20261013-original-papers/extra-00.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-27 | reports/paper_citation_curation/20261013-original-papers/extra-01.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-28 | reports/paper_citation_curation/20261013-original-papers/extra-02.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |
| gate-29 | reports/paper_citation_curation/20261013-original-papers/extra-03.log; Retained complete command output | context_only | Actual exit code 0; automated validation is not scientific approval. |

## Limits And Additional Notes

- 181 parent instances compared does not mean181 supported/corrected amounts; all parent amounts remain unchanged.
- Mattanovich batch conversions, sulfuric-acid density, generic preparation and dangling XLS text remain unresolved; no inferred growth metric.
- Jensen MgCl2 hydration and printed molybdate formula/hydration remain unresolved. Calcium-pantothenate wording is not converted into an invented calcium dose.
- No table2 solid-medium observations or table4 SA/M17 results are promoted to these liquid BL treatments. Other-strain taxonomy lookup was bounded.
- Merge verification was deliberately interrupted after1247 canonical-name conflicts and more than18 minutes; no completed current fingerprint/completeness result is claimed. Freshness has a separately retained result. No untouched whole-corpus baseline or publication is claimed.
- The related AMS1 exporter finding is not superseded or closed; its targets were not re-reviewed here.
- Source caches are ignored local archives, not committed publications. The full citation-exhaustion goal remains incomplete.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T055302Z-original-paper-variants
kind: batch
repository: culturebotai/CultureMech
title: Mattanovich and Jensen paper citations, recipe variants and strain evidence
started_at: '2026-10-13T05:30:34Z'
finished_at: '2026-10-13T05:53:02Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same agent curated and checked this batch; no independent
    reviewer is claimed.
skill: culturemech-add-paper-citation; review-ingredient-concentrations evidence contract
completion: partial
verdict: needs_curation
scientific_review: true
summary: Six paper-record citations for two papers, six inline variants and six variant-only
  strain growth assertions; all parent ingredients preserved. Focused record gates
  pass, but export scope loss, retained category mismatch, chemical uncertainties
  and global merge diagnostics prevent publication-ready approval.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
    sha256: d7b12adb212b6b16f5e7a85937ffd25fde85333511f88da0b46b0c8b611a58be
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium.yaml
    sha256: e6c916970fe767115371333f5bc6e991b0f9d3b8e87cd6b99fbfb7155ebab71f
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_arg.yaml
    sha256: 7f25e7cb2791204fa39e95d5b8aebf81e07e8325e157f877e7026aa2f4a87808
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
    sha256: 5383545a363dac9dc71abe20ca9a72b21bc206dbc73482cd32dead149efeb9f1
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_asp.yaml
    sha256: bf326dd778e325fa6f4da70fc6ca77b5810bd1cda09bfedfca2f8d24fb647d50
    role: target
  - path: data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
    sha256: c234e3095aa45e99b3f921352b46e01f1091df9c574b53f45b8e5279f6ded863
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Six exact MediaDB source11/128 normalized owners and 181 direct ingredient
    instances, with source recipe and strain comparison.
  selection: Frozen targets.yaml exact paths/IDs; no source128 SA record invented
    and no other cohort expansion.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  exclusions:
  - target: Other CultureMech records and outside-paper organisms
    reason: This is bounded citation/variant curation, not exhaustive record review
      or whole-corpus literature coverage.
targets:
- target_id: CultureMech:007250
  path: data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  label: Batch medium; mattanovich et al
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; prior parent/child links are preserved.
- target_id: CultureMech:007302
  path: data/normalized_yaml/bacterial/bl_medium.yaml
  label: BL Medium
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; prior parent/child links are preserved.
- target_id: CultureMech:007303
  path: data/normalized_yaml/bacterial/bl_medium_arg.yaml
  label: BL Medium + Arg
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; prior parent/child links are preserved.
- target_id: CultureMech:007304
  path: data/normalized_yaml/bacterial/bl_medium_asp.yaml
  label: BL Medium + Asp
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; prior parent/child links are preserved.
- target_id: CultureMech:007305
  path: data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  label: BL Medium, Low MOPS
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; prior parent/child links are preserved.
- target_id: CultureMech:007306
  path: data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  label: BL Medium + Arg + Ser + Trp
  kind: maintained
  record_class: MediaRecipe
  ownership_note: Authoritative normalized recipe; prior parent/child links are preserved.
checks:
- check_id: gate-0
  name: just validate-schema data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  command: just validate-schema data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  evidence_ids:
  - gate-0
- check_id: gate-1
  name: just validate-strict data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  command: just validate-strict data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  evidence_ids:
  - gate-1
- check_id: gate-2
  name: just validate-schema data/normalized_yaml/bacterial/bl_medium.yaml
  command: just validate-schema data/normalized_yaml/bacterial/bl_medium.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - gate-2
- check_id: gate-3
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - gate-3
- check_id: gate-4
  name: just validate-schema data/normalized_yaml/bacterial/bl_medium_arg.yaml
  command: just validate-schema data/normalized_yaml/bacterial/bl_medium_arg.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - gate-4
- check_id: gate-5
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - gate-5
- check_id: gate-6
  name: just validate-schema data/normalized_yaml/bacterial/bl_medium_asp.yaml
  command: just validate-schema data/normalized_yaml/bacterial/bl_medium_asp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - gate-6
- check_id: gate-7
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_asp.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_asp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - gate-7
- check_id: gate-8
  name: just validate-schema data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  command: just validate-schema data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - gate-8
- check_id: gate-9
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - gate-9
- check_id: gate-10
  name: just validate-schema data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  command: just validate-schema data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - gate-10
- check_id: gate-11
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - gate-11
- check_id: gate-12
  name: just validate data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  command: just validate data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  evidence_ids:
  - gate-12
- check_id: gate-13
  name: just validate-strict data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  command: just validate-strict data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  evidence_ids:
  - gate-13
- check_id: gate-14
  name: just validate data/normalized_yaml/bacterial/bl_medium.yaml
  command: just validate data/normalized_yaml/bacterial/bl_medium.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - gate-14
- check_id: gate-15
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - gate-15
- check_id: gate-16
  name: just validate data/normalized_yaml/bacterial/bl_medium_arg.yaml
  command: just validate data/normalized_yaml/bacterial/bl_medium_arg.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - gate-16
- check_id: gate-17
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - gate-17
- check_id: gate-18
  name: just validate data/normalized_yaml/bacterial/bl_medium_asp.yaml
  command: just validate data/normalized_yaml/bacterial/bl_medium_asp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - gate-18
- check_id: gate-19
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_asp.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_asp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - gate-19
- check_id: gate-20
  name: just validate data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  command: just validate data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - gate-20
- check_id: gate-21
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_low_mops.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - gate-21
- check_id: gate-22
  name: just validate data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  command: just validate data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - gate-22
- check_id: gate-23
  name: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  command: just validate-strict data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - gate-23
- check_id: gate-24
  name: just verify-merges
  command: just verify-merges
  status: failed
  required: true
  exit_code: 143
  summary: Interrupted after the YAML-parse stage and1247 canonical-name conflicts;
    remaining completeness/fingerprint/synonym diagnostics did not finish. Not a completed
    full merge audit. See merge-interruption.json.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - gate-24
- check_id: gate-25
  name: just audit-merge-freshness --json
  command: just audit-merge-freshness --json
  status: failed
  required: true
  exit_code: 1
  summary: 'Completed freshness audit failed: 6320 existing on-disk merged files versus10781
    regenerated,4275 only existing,8736 only fresh,2045 changed,0 unchanged. The tracked_total
    label is the audit tool terminology, not an exact git ls-files inventory. Regeneration
    was temporary; no merged outputs replaced.'
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - gate-25
- check_id: gate-26
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/.codex/skills/.system/skill-creator/scripts/quick_validate.py
    .claude/skills/culturemech-add-paper-citation
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/.codex/skills/.system/skill-creator/scripts/quick_validate.py
    .claude/skills/culturemech-add-paper-citation
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - gate-26
- check_id: gate-27
  name: /tmp/culturemech-parallel-env-20261012/bin/python -m pytest tests/test_fetch_pubmed_abstracts.py
    tests/test_claude_skills.py tests/test_skill_frontmatter.py tests/test_record_review_contract.py
    tests/test_record_review_routes.py tests/test_mediadb_sql_parsing.py --no-cov
    -q
  command: /tmp/culturemech-parallel-env-20261012/bin/python -m pytest tests/test_fetch_pubmed_abstracts.py
    tests/test_claude_skills.py tests/test_skill_frontmatter.py tests/test_record_review_contract.py
    tests/test_record_review_routes.py tests/test_mediadb_sql_parsing.py --no-cov
    -q
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - gate-27
- check_id: gate-28
  name: /tmp/culturemech-parallel-env-20261012/bin/python /tmp/curate-original-papers-20261013.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /tmp/curate-original-papers-20261013.py
    --apply
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - gate-28
- check_id: gate-29
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Maintained baseline/post-edit or repository merge gate.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - gate-29
- check_id: quote-check
  name: Primary-source excerpts and recipe comparison
  status: passed
  required: true
  summary: Read main methods, XLS source cells, original scans, table headings and
    footnotes; retain explicit limits on chemical forms and parent amounts.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - mattanovich
  - supplement
  - jensen
  - jensen-facts
- check_id: scope-check
  name: KGX variant scope
  status: failed
  required: true
  summary: In-memory edge construction drops variant scope for all six targets. No
    edges or generated pages published.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - readback
evidence:
- evidence_id: mattanovich
  kind: primary_source
  reference: doi:10.1186/1475-2859-8-29
  locator: Material and methods, Strain; Experimental secretome analysis; PMID19490607
  accessed_at: '2026-10-13T05:53:02Z'
  support: supports
  snapshot_sha256: 235b70b7b98d8bebc00a8d68f845259b85f409316f2453d3c7c08a22bfc6711a
  summary: Full HTML and Markdown inspected; strain and experimental-secretome methods
    explicitly support glucose chemostat cultivation, not the glycerol batch parent.
    PubMed title/authors/year/DOI agree; no correction/retraction notice in the archived
    XML.
- evidence_id: supplement
  kind: primary_source
  reference: doi:10.1186/1475-2859-8-29
  locator: 'Additional file 3, Fermentation data and Analysis: A2:A11 batch, A13:A22
    chemostat, A24:A33 trace stock, A35:A40 conditions'
  accessed_at: '2026-10-13T05:53:02Z'
  support: supports
  snapshot_sha256: 5a9895037d69eec142443c94b3a81ed40ff75e09a51c5c6f404c7c8e14b90bc8
  summary: Original publisher XLS read with xlrd; all nonempty cells rendered to addressable
    Markdown. Literal A-column text, not computed results, supports separate batch/chemostat
    recipes and shared trace stock. Stock quantities are not final-medium quantities.
- evidence_id: jensen
  kind: primary_source
  reference: doi:10.1128/aem.59.12.4363-4366.1993
  locator: Original pages 4363-4366; page4363 preparation/Table1 and footnotes, page4364
    Table3 caption and selected rows; provenance file pins all four scan hashes
  accessed_at: '2026-10-13T05:53:02Z'
  support: supports
  snapshot_sha256: e69ef026bfae4b8b13246dc25f0a62ee83802b02158ce8bc0ffa284e1f39810d
  summary: All four original scans visually inspected. Table 1 BL composition and
    Table 3 liquid treatments support five nominal recipes and positive MG1363 growth.
    Stock filtration and pantothenate form differ from the imported preparation. PubMed
    metadata agrees; no correction/retraction notice in archived XML. Scans and abstract
    Markdown are archived; no full-text PDF or complete OCR transcript is claimed.
- evidence_id: jensen-facts
  kind: primary_source
  reference: doi:10.1128/aem.59.12.4363-4366.1993
  locator: Bounded Table1/3 extraction; recipe-extract.md gives readable transcription
  accessed_at: '2026-10-13T05:53:02Z'
  support: supports
  snapshot_sha256: 395d3b0ca838fa790acd16710f29271aa7973bbf2741e2f3f40d360258d2feb1
  summary: Manually checked numerical table facts, not a fabricated contiguous quotation.
    Micromolar to mM comparison divides by 1000. Hydration and printed molybdate formula
    remain unresolved; no mass conversion performed.
- evidence_id: tax-638632
  kind: authority
  reference: NCBITaxon:638632
  locator: NCBI Taxonomy XML TaxId, ScientificName, Rank, synonyms and LineageEx;
    retrieved2026-10-13
  accessed_at: '2026-10-13T05:53:02Z'
  support: supports
  snapshot_sha256: 5d564b1a7abce12a565f22f64afc4547b6c7813aea90990ff1dbd9a19af71a35
  summary: Current NCBI XML confirms canonical label Komagataella pastoris DSMZ 70382,
    rank strain. Historical organism name is retained separately; MG1363 identity
    is strain-specific despite changed species/subspecies classification.
- evidence_id: tax-416870
  kind: authority
  reference: NCBITaxon:416870
  locator: NCBI Taxonomy XML TaxId, ScientificName, Rank, synonyms and LineageEx;
    retrieved2026-10-13
  accessed_at: '2026-10-13T05:53:02Z'
  support: supports
  snapshot_sha256: c40e7cc667216a811c723be5fc1575a78ca77a3676da4e80521717f46cd4d8c3
  summary: Current NCBI XML confirms canonical label Lactococcus cremoris subsp. cremoris
    MG1363, rank strain. Historical organism name is retained separately; MG1363 identity
    is strain-specific despite changed species/subspecies classification.
- evidence_id: other-strains
  kind: search
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy
  locator: Four All Names queries combined with OR; genus verified in MG1363 archived
    lineage
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: bfd90ace54855450fc283277ca49cb9fd3c446d2342dd9ec81769d12d7f09f53
  summary: Bounded exact-name queries for NCDO712/NCDO 712 and Lactococcus lactis/cremoris
    C2 returned no match. This is not proof that no exact taxon exists; the notes
    use verified genus Lactococcus, NCBITaxon1357, parent_rank_only, with no positive
    liquid-medium edge.
  search_scope: 'NCBI Taxonomy ESearch, 2026-10-13: "NCDO712"[All Names] OR "NCDO
    712"[All Names] OR "Lactococcus lactis C2"[All Names] OR "Lactococcus cremoris
    C2"[All Names]. The archived response reports zero results and phrase-not-found
    warnings. No exhaustive synonym search or absence claim; filesystem ignore rules
    are not applicable to this remote query.'
- evidence_id: readback
  kind: record_content
  reference: CultureMech six-record curation readback
  locator: Guarded before/after record comparison and in-memory organism_grows_in_medium_edge
    reproduction
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 4c5eb77a3fec6d0c6c42cc4bee3f58241f1fe63d94210ce5d81e18605e419337
  summary: Every previous field and history prefix is unchanged; exactly one event,
    citation, inline variant and variant-scoped organism were added per target. The
    in-memory KGX edge builder returns the parent ID and loses scope for all six;
    no output was published.
- evidence_id: gate-0
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-00-validate-schema.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-1
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-01-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-2
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-02-validate-schema.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-3
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-03-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-4
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-04-validate-schema.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-5
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-05-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-6
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-06-validate-schema.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-7
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-07-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-8
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-08-validate-schema.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-9
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-09-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-10
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-10-validate-schema.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 7f6c83aa39bdbb10305b80868a767cd345f0b6beecce0de70fdaa684c8eda050
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-11
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/baseline-11-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-12
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-00-validate.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-13
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-01-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-14
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-02-validate.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-15
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-03-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-16
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-04-validate.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-17
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-05-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-18
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-06-validate.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-19
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-07-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-20
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-08-validate.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-21
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-09-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-22
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-10-validate.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-23
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/final-11-validate-strict.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-24
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/merge-00-verify-merges.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 410ddf47ede233fb2beacd9d03876ff8075a97d9d61af96af244646464544557
  summary: Actual exit code 143; automated validation is not scientific approval.
- evidence_id: gate-25
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/merge-01-audit-merge-freshness.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 247699adf7b585b82d7808c5e752c9b2a86ed42ea2dbafa6c1e9b79199410da5
  summary: Actual exit code 1; automated validation is not scientific approval.
- evidence_id: gate-26
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/extra-00.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: db349825903d66adffea3ecf1bd8e1803043e8a71cf1a051235dabc5371f5bb0
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-27
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/extra-01.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 71114a820d0c09712f135c422394d690752073ec7c240fd16bd0475123bba8f4
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-28
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/extra-02.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: 13957f27bb8716d56d57dbaef530296a69cc7474cf821b3e10be376f20a3ea28
  summary: Actual exit code 0; automated validation is not scientific approval.
- evidence_id: gate-29
  kind: validation
  reference: reports/paper_citation_curation/20261013-original-papers/extra-03.log
  locator: Retained complete command output
  accessed_at: '2026-10-13T05:53:02Z'
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: Actual exit code 0; automated validation is not scientific approval.
assessments:
- assessment_id: variant-007250
  area: quantity
  topic: Source-specific formulation and parent preservation
  outcome: supported
  target_ids:
  - CultureMech:007250
  evidence_ids:
  - mattanovich
  - supplement
  - readback
  summary: Supported source-defined chemostat variant preserves stock/final boundaries;
    parent molar conversions remain unverified.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"Sulfate\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.41587\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\": \"5\
    \ mL H2SO4 (95-98% w/w)\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A33\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[1].concentration\",\n      \"ingredient\": \"Glycerol\",\n   \
    \   \"old_amount\": {\n        \"value\": \"433.27\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\": \"39.9\
    \ g glycerol, 1.8 g \",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A3\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[2].concentration\",\n      \"ingredient\": \"Biotin\",\n     \
    \ \"old_amount\": {\n        \"value\": \"0.001637\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\": \"2\
    \ mL of Biotin (0.2 g L-1)\",\n      \"source_locator\": \"additional file 3,\
    \ 'Fermentation data and Analysis'!A9\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[3].concentration\",\n      \"ingredient\": \"Citrate\",\n    \
    \  \"old_amount\": {\n        \"value\": \"9.369\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\": \"1.8\
    \ g citric acid\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A4\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[4].concentration\",\n      \"ingredient\": \"Calcium chloride\
    \ anhydrous\",\n      \"old_amount\": {\n        \"value\": \"0.1496\",\n    \
    \    \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n\
    \      \"source_excerpt\": \"0.022 g CaCl2 · 2H2O\",\n      \"source_locator\"\
    : \"additional file 3, 'Fermentation data and Analysis'!A7\",\n      \"source_reference\"\
    : \"doi:10.1186/1475-2859-8-29\",\n      \"reason\": \"Parent molar amount not\
    \ recertified from mass/stock/acid source units; no molecular-weight or density\
    \ conversion undertaken.\",\n      \"action\": \"parent unchanged; separately\
    \ source-defined chemostat variant added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[5].concentration\"\
    ,\n      \"ingredient\": \"Boric acid\",\n      \"old_amount\": {\n        \"\
    value\": \"0.001488\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"unsupported\",\n      \"source_excerpt\": \"0.02 g H3BO3\",\n      \"source_locator\"\
    : \"additional file 3, 'Fermentation data and Analysis'!A29\",\n      \"source_reference\"\
    : \"doi:10.1186/1475-2859-8-29\",\n      \"reason\": \"Parent molar amount not\
    \ recertified from mass/stock/acid source units; no molecular-weight or density\
    \ conversion undertaken.\",\n      \"action\": \"parent unchanged; separately\
    \ source-defined chemostat variant added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[6].concentration\"\
    ,\n      \"ingredient\": \"Sodium molybdate\",\n      \"old_amount\": {\n    \
    \    \"value\": \"0.003802\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n  \
    \    \"status\": \"unsupported\",\n      \"source_excerpt\": \"0.2g Na2MoO4 ·\
    \ 2H2O\",\n      \"source_locator\": \"additional file 3, 'Fermentation data and\
    \ Analysis'!A28\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[7].concentration\",\n      \"ingredient\": \"Potassium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"12.072\",\n        \"unit\":\
    \ \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"0.9 g KCl\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A5\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[8].concentration\",\n      \"ingredient\": \"Magnesium sulfate\"\
    ,\n      \"old_amount\": {\n        \"value\": \"2.0286\",\n        \"unit\":\
    \ \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"0.5 g MgSO4 · 7H2O\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A8\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[9].concentration\",\n      \"ingredient\": \"Manganese sulfate\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.08165\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"3.0 g MnSO4 ·H2O\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A27\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[10].concentration\",\n      \"ingredient\": \"Ferrous sulfate\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.08273\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"5.0 g FeSO4 · 7H2O\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A32\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[11].concentration\",\n      \"ingredient\": \"Cobalt chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.017714\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"0.5 g CoCl2\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A30\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[12].concentration\",\n      \"ingredient\": \"Cupric sulfate\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.11054\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"6.0 g CuSO4 · 5H2O\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A25\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[13].concentration\",\n      \"ingredient\": \"Zinc Chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.6749\",\n        \"unit\":\
    \ \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"20.0 g ZnCl2\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A31\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[14].concentration\",\n      \"ingredient\": \"Ammonium phosphate\"\
    ,\n      \"old_amount\": {\n        \"value\": \"95.414\",\n        \"unit\":\
    \ \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"12.6 g (NH4)2HPO4\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A6\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[15].concentration\",\n      \"ingredient\": \"Sodium iodide\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.002455\",\n        \"unit\"\
    : \"MILLIMOLAR\"\n      },\n      \"status\": \"unsupported\",\n      \"source_excerpt\"\
    : \"0.08 g NaI\",\n      \"source_locator\": \"additional file 3, 'Fermentation\
    \ data and Analysis'!A26\",\n      \"source_reference\": \"doi:10.1186/1475-2859-8-29\"\
    ,\n      \"reason\": \"Parent molar amount not recertified from mass/stock/acid\
    \ source units; no molecular-weight or density conversion undertaken.\",\n   \
    \   \"action\": \"parent unchanged; separately source-defined chemostat variant\
    \ added\",\n      \"proposed_parent_amount\": null\n    }\n  ],\n  \"variant_field\"\
    : \"variants[0]\",\n  \"old_variant\": null,\n  \"action\": \"add\",\n  \"variant\"\
    : {\n    \"name\": \"Mattanovich 2009 glucose chemostat formulation\",\n    \"\
    description\": \"Source-defined glucose chemostat formulation, distinct from the\
    \ imported glycerol batch medium. All recipe quantities retain supplement source\
    \ units and stock/final boundaries; not a certification of the parent's concentrations,\
    \ ingredient grounding or preparation.\",\n    \"modifications\": [\n      \"\
    Replace the batch parent's glycerol (433.27 mM) with glucose monohydrate at the\
    \ source's 50.0 g per liter of chemostat medium.\",\n      \"Use 0.9 g/L citric\
    \ acid, 1.7 g/L KCl and 4.35 g/L (NH4)2HPO4, replacing the parent's molar citrate,\
    \ KCl and ammonium-phosphate entries; preserve the source's chemical forms and\
    \ mass basis.\",\n      \"Use 0.01 g/L CaCl2 dihydrate and 0.65 g/L MgSO4 heptahydrate\
    \ rather than inheriting the parent's batch amounts and anhydrous/unspecified\
    \ forms.\",\n      \"Add 1 mL of 0.2 g/L biotin stock per liter of chemostat medium\
    \ instead of inheriting the parent's direct biotin molarity.\",\n      \"Replace\
    \ the parent's nine flattened trace/acid entries (sulfate, boric acid, sodium\
    \ molybdate, manganese sulfate, ferrous sulfate, cobalt chloride, cupric sulfate,\
    \ zinc chloride and sodium iodide) with 1.6 mL of trace-salts stock per liter\
    \ of chemostat medium. Do not retain both the flattened ingredients and this stock\
    \ dose.\",\n      \"Trace-salts stock, per liter of stock: 6.0 g CuSO4 pentahydrate,\
    \ 0.08 g NaI, 3.0 g MnSO4 monohydrate, 0.2 g Na2MoO4 dihydrate, 0.02 g H3BO3,\
    \ 0.5 g CoCl2, 20.0 g ZnCl2, 5.0 g FeSO4 heptahydrate and 5 mL H2SO4 (95-98% w/w).\
    \ These are stock amounts, not final-medium amounts; no acid density or molar\
    \ conversion is inferred.\",\n      \"Set initial medium pH to 5.0 using 25% HCl\
    \ as stated in the supplement; its percentage basis and a fixed titrant volume\
    \ are not specified. The chemostat pH was controlled at 5.0 with 25% ammonium\
    \ hydroxide. The inspected source does not establish the parent's generic final-medium\
    \ filter-sterilization procedure, so that procedure is not inherited as verified\
    \ study preparation.\"\n    ],\n    \"purpose\": \"Glucose-limited chemostat cultivation\
    \ for experimental secretome analysis.\",\n    \"evidence\": [\n      {\n    \
    \    \"reference\": \"doi:10.1186/1475-2859-8-29\",\n        \"supports\": \"\
    SUPPORT\",\n        \"snippet\": \"50.0g glucose · H2O\",\n        \"explanation\"\
    : \"Locator: additional file 3, sheet 'Fermentation data and Analysis', A13:A33;\
    \ source=https://media.springernature.com/original/springer-static/esm/art%3A10.1186%2F1475-2859-8-29/MediaObjects/12934_2009_349_MOESM3_ESM.xls.\
    \ A13: 'Chemostat medium contained per Liter'; A14: '50.0g glucose · H2O'; A15:\
    \ '0.9g citric acid'; A16: '1.7 g KCl'; A17: '4.35 g (NH4)2HPO4'; A18: '0.01 g\
    \ CaCl2 · 2H2O'; A19: '0.65 g MgSO4 · 7H2O'; A20: '1 mL of Biotin (0.2 g L-1)';\
    \ A21: '1.6 mL of trace salts stock solution. '; A22: 'pH set to 5.0 using 25%\
    \ HCl'; A24: 'Trace salts stock solution contained per Liter'; A25: '6.0 g CuSO4\
    \ · 5H2O'; A26: '0.08 g NaI'; A27: '3.0 g MnSO4 ·H2O'; A28: '0.2g Na2MoO4 · 2H2O';\
    \ A29: '0.02 g H3BO3'; A30: '0.5 g CoCl2'; A31: '20.0 g ZnCl2'; A32: '5.0 g FeSO4\
    \ · 7H2O'; A33: '5 mL H2SO4 (95-98% w/w)'. The heading in A13 establishes the\
    \ per-liter chemostat-medium basis, A24 establishes the separate per-liter stock\
    \ basis. Quotes are individual literal cell values, not a spliced sentence. No\
    \ molecular weights, acid density, stock dilution results or unreported preparation\
    \ steps are inferred.\"\n      }\n    ]\n  },\n  \"parent_amounts_changed\": false,\n\
    \  \"conversion\": \"No mass, density, hydrate or stock dilution conversion. Jensen\
    \ micromolar-to-mM comparison divides by1000; original facts and basis remain\
    \ explicit.\",\n  \"scope\": \"All direct ingredients; none of these parents contains\
    \ nested solutions. The Mattanovich added variant retains an explicit trace stock\
    \ in modification prose.\"\n}"
  dimensions:
  - name: native_decisions
    value: unsupported parent conversions; add source-defined variant
    definition: Bounded concentration-contract dispositions; not global parent approval.
    evidence_ids:
    - mattanovich
    - supplement
    - readback
  metrics:
  - name: parent ingredient instances compared
    value: 16
    unit: ingredient instances
    denominator: 16
    minimum: 0
    maximum: 16
    definition: Direct nodes inspected for this paper comparison, not an evidence
      completeness percentage.
- assessment_id: organism-007250
  area: grounding
  topic: Scientific name, current taxonomy and growth scope
  outcome: supported
  target_ids:
  - CultureMech:007250
  evidence_ids:
  - mattanovich
  - supplement
  - tax-638632
  - readback
  summary: Exact strain DSMZ70382 maps to Komagataella pastoris DSMZ70382, NCBITaxon638632,
    rank strain; growth is on the glucose chemostat variant.
  details: "{\n  \"preferred_term\": \"Pichia pastoris\",\n  \"term\": {\n    \"id\"\
    : \"NCBITaxon:638632\",\n    \"label\": \"Komagataella pastoris DSMZ 70382\"\n\
    \  },\n  \"strain\": \"DSMZ 70382\",\n  \"scoped_to_variant\": \"Mattanovich 2009\
    \ glucose chemostat formulation\",\n  \"evidence\": [\n    {\n      \"reference\"\
    : \"doi:10.1186/1475-2859-8-29\",\n      \"supports\": \"SUPPORT\",\n      \"\
    snippet\": \"P. pastoris DSMZ 70382 was grown in fully aerobic chemostat cultures\
    \ on minimal medium with glucose as carbon source\",\n      \"explanation\": \"\
    Locator: Material and methods, Strain and Experimental secretome analysis, together\
    \ with additional file 3 A13:A40. Growth belongs to the glucose chemostat variant,\
    \ not the glycerol batch parent. Supplement A38 reports 25 C, A39 pH 5.0 and A36\
    \ oxygen control above 20%; these are study conditions, not optima. The database's\
    \ 0.2/h growth value is not imported. A40's dilution-rate/flow wording is not\
    \ converted into a growth metric. Reported scientific name=Pichia pastoris; strain=DSMZ\
    \ 70382 (=CBS704 in the paper). taxonomy_match=exact_strain; NCBITaxon:638632;\
    \ canonical_label=Komagataella pastoris DSMZ 70382; rank=strain in NCBI Taxonomy\
    \ XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=638632.\
    \ NCBI lists Pichia pastoris DSMZ 70382 as a synonym; species ancestor=Komagataella\
    \ pastoris, NCBITaxon:4922.\"\n    }\n  ]\n}"
- assessment_id: variant-007302
  area: quantity
  topic: Source-specific formulation and parent preservation
  outcome: supported
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - jensen
  - jensen-facts
  - readback
  summary: Selected BL liquid treatment is represented as preparation-qualified variant;
    numerical agreement is not exact chemical-form equivalence.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"Ammonium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"9.5\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Ammonium chloride\",\n        \"source_label\": \"NH4Cl\"\
    ,\n        \"source_value\": \"9.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"9.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"L-Valine\",\n      \"old_amount\": {\n        \"value\"\
    : \"2.6\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"L-Valine\",\n        \"source_label\"\
    : \"L-Valine\",\n        \"source_value\": \"2.6\",\n        \"source_unit\":\
    \ \"mM\",\n        \"value_mM\": \"2.6\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[2].concentration\"\
    ,\n      \"ingredient\": \"L-Methionine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.5\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Methionine\",\n   \
    \     \"source_label\": \"L-Methionine\",\n        \"source_value\": \"0.5\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.5\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[3].concentration\",\n      \"ingredient\": \"L-Leucine\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Leucine\",\n        \"source_label\": \"L-Leucine\",\n\
    \        \"source_value\": \"1.5\",\n        \"source_unit\": \"mM\",\n      \
    \  \"value_mM\": \"1.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[4].concentration\"\
    ,\n      \"ingredient\": \"L-Histidine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.3\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Histidine\",\n    \
    \    \"source_label\": \"L-Histidine\",\n        \"source_value\": \"0.3\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.3\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[5].concentration\",\n      \"ingredient\": \"L-Glutamine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.7\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamine\",\n        \"source_label\": \"L-Glutamine\"\
    ,\n        \"source_value\": \"0.7\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.7\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[6].concentration\"\
    ,\n      \"ingredient\": \"L-Glutamate\",\n      \"old_amount\": {\n        \"\
    value\": \"21.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Glutamate\",\n    \
    \    \"source_label\": \"L-Glutamate\",\n        \"source_value\": \"21\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"21\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[7].concentration\",\n      \"ingredient\": \"Pantothenate\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.002\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Pantothenate\",\n        \"source_label\": \"pantothenate\"\
    ,\n        \"source_value\": \"2\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.002\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[8].concentration\"\
    ,\n      \"ingredient\": \"Boric acid\",\n      \"old_amount\": {\n        \"\
    value\": \"0.0004\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Boric acid\",\n     \
    \   \"source_label\": \"H3BO3\",\n        \"source_value\": \"0.4\",\n       \
    \ \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.0004\",\n      \
    \  \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[9].concentration\",\n      \"ingredient\"\
    : \"Riboflavin\",\n      \"old_amount\": {\n        \"value\": \"0.0026\",\n \
    \       \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Riboflavin\",\n        \"\
    source_label\": \"riboflavin\",\n        \"source_value\": \"2.6\",\n        \"\
    source_unit\": \"micromolar\",\n        \"value_mM\": \"0.0026\",\n        \"\
    locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"\
    1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant\
    \ evidence added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n \
    \     \"field_path\": \"ingredients[10].concentration\",\n      \"ingredient\"\
    : \"Thiamine HCl\",\n      \"old_amount\": {\n        \"value\": \"0.003\",\n\
    \        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Thiamine HCl\",\n        \"\
    source_label\": \"thiamine-HCl\",\n        \"source_value\": \"3\",\n        \"\
    source_unit\": \"micromolar\",\n        \"value_mM\": \"0.003\",\n        \"locator\"\
    : \"page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[11].concentration\",\n      \"ingredient\": \"Nicotinamide\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.008\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Nicotinamide\",\n        \"source_label\": \"niacinamide\"\
    ,\n        \"source_value\": \"8\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.008\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"L-Asparagine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Asparagine\",\n   \
    \     \"source_label\": \"L-Asparagine\",\n        \"source_value\": \"0.8\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[13].concentration\",\n      \"ingredient\": \"L-Isoleucine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Isoleucine\",\n        \"source_label\": \"L-Isoleucine\"\
    ,\n        \"source_value\": \"0.8\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.8\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[14].concentration\"\
    ,\n      \"ingredient\": \"Potassium sulfate\",\n      \"old_amount\": {\n   \
    \     \"value\": \"0.28\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n     \
    \ \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium sulfate\",\n\
    \        \"source_label\": \"K2SO4\",\n        \"source_value\": \"0.28\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.28\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[15].concentration\",\n      \"ingredient\": \"Potassium dihydrogen\
    \ phosphate\",\n      \"old_amount\": {\n        \"value\": \"1.3\",\n       \
    \ \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n \
    \     \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Potassium dihydrogen phosphate\"\
    ,\n        \"source_label\": \"KH2PO4\",\n        \"source_value\": \"1.3\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"1.3\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[16].concentration\",\n      \"ingredient\": \"Molybdic acid ammonium\
    \ salt tetrahydrate\",\n      \"old_amount\": {\n        \"value\": \"3e-06\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Molybdic acid ammonium salt\
    \ tetrahydrate\",\n        \"source_label\": \"molybdate trace, printed formula\
    \ unresolved\",\n        \"source_value\": \"0.003\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.000003\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[17].concentration\",\n      \"ingredient\": \"Cobalt chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"3e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Cobalt chloride\",\n        \"source_label\": \"CoCl2\"\
    ,\n        \"source_value\": \"0.03\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00003\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[18].concentration\",\n      \"ingredient\": \"Sodium acetate\",\n\
    \      \"old_amount\": {\n        \"value\": \"15.0\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Sodium acetate\",\n        \"source_label\": \"Na-acetate\"\
    ,\n        \"source_value\": \"15\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"15\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[19].concentration\"\
    ,\n      \"ingredient\": \"Glucose\",\n      \"old_amount\": {\n        \"value\"\
    : \"50.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Glucose\",\n        \"\
    source_label\": \"Glucose\",\n        \"source_value\": \"50\",\n        \"source_unit\"\
    : \"mM\",\n        \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[20].concentration\"\
    ,\n      \"ingredient\": \"MOPS\",\n      \"old_amount\": {\n        \"value\"\
    : \"190.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"MOPS\",\n        \"source_label\"\
    : \"MOPS\",\n        \"source_value\": \"190\",\n        \"source_unit\": \"mM\"\
    ,\n        \"value_mM\": \"190\",\n        \"locator\": \"page 4363, Table 1 BL\
    \ column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"action\"\
    : \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[21].concentration\"\
    ,\n      \"ingredient\": \"Tricine\",\n      \"old_amount\": {\n        \"value\"\
    : \"4.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Tricine\",\n        \"source_label\"\
    : \"Tricine\",\n        \"source_value\": \"4\",\n        \"source_unit\": \"\
    mM\",\n        \"value_mM\": \"4\",\n        \"locator\": \"page 4363, Table 1\
    \ BL column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"\
    action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[22].concentration\"\
    ,\n      \"ingredient\": \"Calcium chloride anhydrous\",\n      \"old_amount\"\
    : {\n        \"value\": \"0.0005\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n\
    \      \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Calcium chloride anhydrous\"\
    ,\n        \"source_label\": \"CaCl2\",\n        \"source_value\": \"0.0005\"\
    ,\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.0005\",\n     \
    \   \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"\
    No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[23].concentration\",\n      \"ingredient\": \"Magnesium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.52\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Magnesium chloride\",\n        \"source_label\": \"MgCl2\"\
    ,\n        \"source_value\": \"0.52\",\n        \"source_unit\": \"mM\",\n   \
    \     \"value_mM\": \"0.52\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[24].concentration\"\
    ,\n      \"ingredient\": \"Ferrous sulfate\",\n      \"old_amount\": {\n     \
    \   \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Ferrous sulfate\",\n\
    \        \"source_label\": \"FeSO4\",\n        \"source_value\": \"0.01\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.01\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[25].concentration\",\n      \"ingredient\": \"Sodium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"50.0\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Sodium chloride\",\n        \"source_label\": \"NaCl\"\
    ,\n        \"source_value\": \"50\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[26].concentration\"\
    ,\n      \"ingredient\": \"Cupric sulfate\",\n      \"old_amount\": {\n      \
    \  \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Cupric sulfate\",\n \
    \       \"source_label\": \"CuSO4\",\n        \"source_value\": \"0.01\",\n  \
    \      \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00001\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[27].concentration\",\n      \"ingredient\"\
    : \"Zinc sulfate\",\n      \"old_amount\": {\n        \"value\": \"1e-05\",\n\
    \        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Zinc sulfate\",\n        \"\
    source_label\": \"ZnSO4\",\n        \"source_value\": \"0.01\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.00001\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[28].concentration\",\n      \"ingredient\": \"Folate\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.0023\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Folate\",\n        \"source_label\": \"folic acid\",\n\
    \        \"source_value\": \"2.3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.0023\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[29].concentration\",\n      \"ingredient\": \"Biotin\",\n      \"\
    old_amount\": {\n        \"value\": \"0.0004\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Biotin\",\n        \"source_label\": \"biotin\",\n    \
    \    \"source_value\": \"0.4\",\n        \"source_unit\": \"micromolar\",\n  \
    \      \"value_mM\": \"0.0004\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[30].concentration\"\
    ,\n      \"ingredient\": \"Manganese chloride\",\n      \"old_amount\": {\n  \
    \      \"value\": \"8e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n   \
    \   \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Manganese chloride\"\
    ,\n        \"source_label\": \"MnCl2\",\n        \"source_value\": \"0.08\",\n\
    \        \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00008\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[31].concentration\",\n      \"ingredient\"\
    : \"Pyridoxal HCl\",\n      \"old_amount\": {\n        \"value\": \"0.01\",\n\
    \        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Pyridoxal HCl\",\n       \
    \ \"source_label\": \"pyridoxal-HCl\",\n        \"source_value\": \"10\",\n  \
    \      \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.01\",\n   \
    \     \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    }\n \
    \ ],\n  \"variant_field\": \"variants[0]\",\n  \"old_variant\": null,\n  \"action\"\
    : \"add\",\n  \"variant\": {\n    \"name\": \"Jensen 1993 BL Medium reported preparation\"\
    ,\n    \"description\": \"Historical Table 3 liquid-culture treatment with the\
    \ source's preparation and pantothenate form. Numerical parent amounts match the\
    \ selected Table 1/3 treatment, but unresolved hydrate details are not asserted\
    \ as exact parent equivalence. This preparation-qualified inline variant does\
    \ not duplicate or replace the existing BL/low-MOPS full-record relationship.\"\
    ,\n    \"modifications\": [\n      \"Use the paper's stock-solution filtration\
    \ through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer\
    \ filtration of the complete mixture; no additional final-medium sterilization\
    \ step is inferred.\",\n      \"Use calcium pantothenate as specified in the text;\
    \ Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret\
    \ that as 2 micromolar calcium salt or add an inferred calcium concentration.\"\
    ,\n      \"Keep the published nominal molar formulation from Table 1 and this\
    \ Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration\
    \ are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate\
    \ labels are not promoted to verified study identities. No mass or hydrate conversion\
    \ is performed.\",\n      \"Retain the Table 3 unmodified BL treatment, including\
    \ 190 mM MOPS and the Table 1 BL-column amino-acid doses; this is not the 19-amino-acid\
    \ SA medium.\"\n    ],\n    \"purpose\": \"Reported liquid batch-culture treatment\
    \ for MG1363.\",\n    \"evidence\": [\n      {\n        \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n        \"supports\": \"SUPPORT\",\n        \"snippet\": \"All stock solutions\
    \ were passed through Millipore filters (0.2-μm pore size).\",\n        \"explanation\"\
    : \"Locator: page 4363, Growth on plates containing eight amino acids, preparation\
    \ paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin\
    \ footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid\
    \ treatment None (=BL). All numeric ingredient amounts were compared with the\
    \ original scans; micromolar footnote values were divided by 1000 solely for comparison\
    \ to existing mM fields. No parent amount was rewritten. The printed molybdate\
    \ formula/hydration remains unresolved; no unsupported exact chemical identity\
    \ is claimed.\"\n      }\n    ]\n  },\n  \"parent_amounts_changed\": false,\n\
    \  \"conversion\": \"No mass, density, hydrate or stock dilution conversion. Jensen\
    \ micromolar-to-mM comparison divides by1000; original facts and basis remain\
    \ explicit.\",\n  \"scope\": \"All direct ingredients; none of these parents contains\
    \ nested solutions. The Mattanovich added variant retains an explicit trace stock\
    \ in modification prose.\"\n}"
  dimensions:
  - name: native_decisions
    value: evidence_only numerical comparison, chemically qualified; add source-preparation
      variant
    definition: Bounded concentration-contract dispositions; not global parent approval.
    evidence_ids:
    - jensen
    - jensen-facts
    - readback
  metrics:
  - name: parent ingredient instances compared
    value: 32
    unit: ingredient instances
    denominator: 32
    minimum: 0
    maximum: 32
    definition: Direct nodes inspected for this paper comparison, not an evidence
      completeness percentage.
- assessment_id: organism-007302
  area: grounding
  topic: Scientific name, current taxonomy and growth scope
  outcome: supported
  target_ids:
  - CultureMech:007302
  evidence_ids:
  - jensen
  - jensen-facts
  - tax-416870
  - readback
  summary: Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity
    to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain;
    Table3 growth is variant-only.
  details: "{\n  \"preferred_term\": \"Lactococcus lactis subsp. lactis\",\n  \"term\"\
    : {\n    \"id\": \"NCBITaxon:416870\",\n    \"label\": \"Lactococcus cremoris\
    \ subsp. cremoris MG1363\"\n  },\n  \"strain\": \"MG1363\",\n  \"scoped_to_variant\"\
    : \"Jensen 1993 BL Medium reported preparation\",\n  \"evidence\": [\n    {\n\
    \      \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"supports\"\
    : \"SUPPORT\",\n      \"snippet\": \"MG1363 in unaerated batch cultures of BL\
    \ medium or modified BL medium\",\n      \"explanation\": \"Locator: original\
    \ page 4364, Table 3 caption and treatment row None (=BL); that row reports positive\
    \ growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle\
    \ magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis.\
    \ No growth-rate value, OD conversion, pH optimum or broad species growth assertion\
    \ is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363.\
    \ taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus\
    \ cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved\
    \ 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870.\
    \ The historical subspecies wording differs from current taxonomy; retain it as\
    \ the reported name, not a current classification. No equivalence between all\
    \ historical L. lactis strains and L. cremoris is inferred.\"\n    }\n  ]\n}"
- assessment_id: variant-007303
  area: quantity
  topic: Source-specific formulation and parent preservation
  outcome: supported
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - jensen
  - jensen-facts
  - readback
  summary: Selected BL liquid treatment is represented as preparation-qualified variant;
    numerical agreement is not exact chemical-form equivalence.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"L-Valine\",\n   \
    \   \"old_amount\": {\n        \"value\": \"2.6\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Valine\",\n        \"source_label\": \"L-Valine\",\n\
    \        \"source_value\": \"2.6\",\n        \"source_unit\": \"mM\",\n      \
    \  \"value_mM\": \"2.6\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"Thiamine HCl\",\n      \"old_amount\": {\n        \"\
    value\": \"0.003\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Thiamine HCl\",\n   \
    \     \"source_label\": \"thiamine-HCl\",\n        \"source_value\": \"3\",\n\
    \        \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.003\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[2].concentration\",\n      \"ingredient\"\
    : \"L-Arginine\",\n      \"old_amount\": {\n        \"value\": \"1.1\",\n    \
    \    \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"source_value_mM\": \"1.1\",\n        \"locator\"\
    : \"pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[3].concentration\",\n      \"ingredient\": \"Pantothenate\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.002\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Pantothenate\",\n        \"source_label\": \"pantothenate\"\
    ,\n        \"source_value\": \"2\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.002\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[4].concentration\"\
    ,\n      \"ingredient\": \"Sodium chloride\",\n      \"old_amount\": {\n     \
    \   \"value\": \"50.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Sodium chloride\",\n\
    \        \"source_label\": \"NaCl\",\n        \"source_value\": \"50\",\n    \
    \    \"source_unit\": \"mM\",\n        \"value_mM\": \"50\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[5].concentration\",\n      \"ingredient\": \"L-Methionine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Methionine\",\n        \"source_label\": \"L-Methionine\"\
    ,\n        \"source_value\": \"0.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[6].concentration\"\
    ,\n      \"ingredient\": \"Biotin\",\n      \"old_amount\": {\n        \"value\"\
    : \"0.0004\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Biotin\",\n        \"\
    source_label\": \"biotin\",\n        \"source_value\": \"0.4\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.0004\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[7].concentration\",\n      \"ingredient\": \"MOPS\",\n      \"\
    old_amount\": {\n        \"value\": \"190.0\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"MOPS\",\n        \"source_label\": \"MOPS\",\n        \"\
    source_value\": \"190\",\n        \"source_unit\": \"mM\",\n        \"value_mM\"\
    : \"190\",\n        \"locator\": \"page 4363, Table 1 BL column\",\n        \"\
    calculation\": \"No conversion\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[8].concentration\",\n      \"ingredient\"\
    : \"L-Asparagine\",\n      \"old_amount\": {\n        \"value\": \"0.8\",\n  \
    \      \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"L-Asparagine\",\n        \"\
    source_label\": \"L-Asparagine\",\n        \"source_value\": \"0.8\",\n      \
    \  \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[9].concentration\",\n      \"ingredient\": \"Nicotinamide\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.008\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Nicotinamide\",\n        \"source_label\": \"niacinamide\"\
    ,\n        \"source_value\": \"8\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.008\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[10].concentration\"\
    ,\n      \"ingredient\": \"L-Glutamate\",\n      \"old_amount\": {\n        \"\
    value\": \"21.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Glutamate\",\n    \
    \    \"source_label\": \"L-Glutamate\",\n        \"source_value\": \"21\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"21\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[11].concentration\",\n      \"ingredient\": \"L-Glutamine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.7\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamine\",\n        \"source_label\": \"L-Glutamine\"\
    ,\n        \"source_value\": \"0.7\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.7\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"L-Leucine\",\n      \"old_amount\": {\n        \"value\"\
    : \"1.5\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"L-Leucine\",\n        \"source_label\"\
    : \"L-Leucine\",\n        \"source_value\": \"1.5\",\n        \"source_unit\"\
    : \"mM\",\n        \"value_mM\": \"1.5\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[13].concentration\"\
    ,\n      \"ingredient\": \"L-Histidine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.3\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Histidine\",\n    \
    \    \"source_label\": \"L-Histidine\",\n        \"source_value\": \"0.3\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.3\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[14].concentration\",\n      \"ingredient\": \"Riboflavin\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.0026\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Riboflavin\",\n        \"source_label\": \"riboflavin\"\
    ,\n        \"source_value\": \"2.6\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.0026\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[15].concentration\",\n      \"ingredient\": \"Tricine\",\n      \"\
    old_amount\": {\n        \"value\": \"4.0\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Tricine\",\n        \"source_label\": \"Tricine\",\n  \
    \      \"source_value\": \"4\",\n        \"source_unit\": \"mM\",\n        \"\
    value_mM\": \"4\",\n        \"locator\": \"page 4363, Table 1 BL column\",\n \
    \       \"calculation\": \"No conversion\"\n      },\n      \"action\": \"parent\
    \ unchanged; variant evidence added\",\n      \"proposed_parent_amount\": null\n\
    \    },\n    {\n      \"field_path\": \"ingredients[16].concentration\",\n   \
    \   \"ingredient\": \"Sodium acetate\",\n      \"old_amount\": {\n        \"value\"\
    : \"15.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Sodium acetate\",\n \
    \       \"source_label\": \"Na-acetate\",\n        \"source_value\": \"15\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"15\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[17].concentration\",\n      \"ingredient\": \"Potassium dihydrogen\
    \ phosphate\",\n      \"old_amount\": {\n        \"value\": \"1.3\",\n       \
    \ \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n \
    \     \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Potassium dihydrogen phosphate\"\
    ,\n        \"source_label\": \"KH2PO4\",\n        \"source_value\": \"1.3\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"1.3\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[18].concentration\",\n      \"ingredient\": \"Ferrous sulfate\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.01\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Ferrous sulfate\",\n        \"source_label\": \"FeSO4\"\
    ,\n        \"source_value\": \"0.01\",\n        \"source_unit\": \"mM\",\n   \
    \     \"value_mM\": \"0.01\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[19].concentration\"\
    ,\n      \"ingredient\": \"Folate\",\n      \"old_amount\": {\n        \"value\"\
    : \"0.0023\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Folate\",\n        \"\
    source_label\": \"folic acid\",\n        \"source_value\": \"2.3\",\n        \"\
    source_unit\": \"micromolar\",\n        \"value_mM\": \"0.0023\",\n        \"\
    locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"\
    1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant\
    \ evidence added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n \
    \     \"field_path\": \"ingredients[20].concentration\",\n      \"ingredient\"\
    : \"L-Isoleucine\",\n      \"old_amount\": {\n        \"value\": \"0.8\",\n  \
    \      \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"L-Isoleucine\",\n        \"\
    source_label\": \"L-Isoleucine\",\n        \"source_value\": \"0.8\",\n      \
    \  \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[21].concentration\",\n      \"ingredient\": \"Pyridoxal HCl\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.01\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Pyridoxal HCl\",\n        \"source_label\": \"pyridoxal-HCl\"\
    ,\n        \"source_value\": \"10\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.01\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[22].concentration\",\n      \"ingredient\": \"Cupric sulfate\",\n\
    \      \"old_amount\": {\n        \"value\": \"1e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Cupric sulfate\",\n        \"source_label\": \"CuSO4\"\
    ,\n        \"source_value\": \"0.01\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00001\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[23].concentration\",\n      \"ingredient\": \"Cobalt chloride\",\n\
    \      \"old_amount\": {\n        \"value\": \"3e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Cobalt chloride\",\n        \"source_label\": \"CoCl2\"\
    ,\n        \"source_value\": \"0.03\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00003\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[24].concentration\",\n      \"ingredient\": \"Magnesium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.52\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Magnesium chloride\",\n        \"source_label\": \"MgCl2\"\
    ,\n        \"source_value\": \"0.52\",\n        \"source_unit\": \"mM\",\n   \
    \     \"value_mM\": \"0.52\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[25].concentration\"\
    ,\n      \"ingredient\": \"Manganese chloride\",\n      \"old_amount\": {\n  \
    \      \"value\": \"8e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n   \
    \   \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Manganese chloride\"\
    ,\n        \"source_label\": \"MnCl2\",\n        \"source_value\": \"0.08\",\n\
    \        \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00008\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[26].concentration\",\n      \"ingredient\"\
    : \"Boric acid\",\n      \"old_amount\": {\n        \"value\": \"0.0004\",\n \
    \       \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Boric acid\",\n        \"\
    source_label\": \"H3BO3\",\n        \"source_value\": \"0.4\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.0004\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[27].concentration\",\n      \"ingredient\": \"Calcium chloride\
    \ anhydrous\",\n      \"old_amount\": {\n        \"value\": \"0.0005\",\n    \
    \    \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Calcium chloride anhydrous\"\
    ,\n        \"source_label\": \"CaCl2\",\n        \"source_value\": \"0.0005\"\
    ,\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.0005\",\n     \
    \   \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"\
    No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[28].concentration\",\n      \"ingredient\": \"Glucose\",\n   \
    \   \"old_amount\": {\n        \"value\": \"50.0\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Glucose\",\n        \"source_label\": \"Glucose\",\n  \
    \      \"source_value\": \"50\",\n        \"source_unit\": \"mM\",\n        \"\
    value_mM\": \"50\",\n        \"locator\": \"page 4363, Table 1 BL column\",\n\
    \        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"parent\
    \ unchanged; variant evidence added\",\n      \"proposed_parent_amount\": null\n\
    \    },\n    {\n      \"field_path\": \"ingredients[29].concentration\",\n   \
    \   \"ingredient\": \"Potassium sulfate\",\n      \"old_amount\": {\n        \"\
    value\": \"0.28\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium sulfate\",\n\
    \        \"source_label\": \"K2SO4\",\n        \"source_value\": \"0.28\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.28\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[30].concentration\",\n      \"ingredient\": \"Molybdic acid ammonium\
    \ salt tetrahydrate\",\n      \"old_amount\": {\n        \"value\": \"3e-06\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Molybdic acid ammonium salt\
    \ tetrahydrate\",\n        \"source_label\": \"molybdate trace, printed formula\
    \ unresolved\",\n        \"source_value\": \"0.003\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.000003\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[31].concentration\",\n      \"ingredient\": \"Ammonium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"9.5\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Ammonium chloride\",\n        \"source_label\": \"NH4Cl\"\
    ,\n        \"source_value\": \"9.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"9.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[32].concentration\"\
    ,\n      \"ingredient\": \"Zinc sulfate\",\n      \"old_amount\": {\n        \"\
    value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Zinc sulfate\",\n   \
    \     \"source_label\": \"ZnSO4\",\n        \"source_value\": \"0.01\",\n    \
    \    \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00001\",\n  \
    \      \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    }\n \
    \ ],\n  \"variant_field\": \"variants[0]\",\n  \"old_variant\": null,\n  \"action\"\
    : \"add\",\n  \"variant\": {\n    \"name\": \"Jensen 1993 BL Medium + Arg reported\
    \ preparation\",\n    \"description\": \"Historical Table 3 liquid-culture treatment\
    \ with the source's preparation and pantothenate form. Numerical parent amounts\
    \ match the selected Table 1/3 treatment, but unresolved hydrate details are not\
    \ asserted as exact parent equivalence. This preparation-qualified inline variant\
    \ does not duplicate or replace the existing BL/low-MOPS full-record relationship.\"\
    ,\n    \"modifications\": [\n      \"Use the paper's stock-solution filtration\
    \ through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer\
    \ filtration of the complete mixture; no additional final-medium sterilization\
    \ step is inferred.\",\n      \"Use calcium pantothenate as specified in the text;\
    \ Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret\
    \ that as 2 micromolar calcium salt or add an inferred calcium concentration.\"\
    ,\n      \"Keep the published nominal molar formulation from Table 1 and this\
    \ Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration\
    \ are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate\
    \ labels are not promoted to verified study identities. No mass or hydrate conversion\
    \ is performed.\",\n      \"Retain this existing treatment dose: L-Arginine 1.1\
    \ mM. Table 3 footnote b points to the Table 1 SA-column Arg/Ser/Trp doses; the\
    \ Asp and low-MOPS rows state their own doses. No new base-versus-child link is\
    \ created.\"\n    ],\n    \"purpose\": \"Reported liquid batch-culture treatment\
    \ for MG1363.\",\n    \"evidence\": [\n      {\n        \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n        \"supports\": \"SUPPORT\",\n        \"snippet\": \"All stock solutions\
    \ were passed through Millipore filters (0.2-μm pore size).\",\n        \"explanation\"\
    : \"Locator: page 4363, Growth on plates containing eight amino acids, preparation\
    \ paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin\
    \ footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid\
    \ treatment +Arg. All numeric ingredient amounts were compared with the original\
    \ scans; micromolar footnote values were divided by 1000 solely for comparison\
    \ to existing mM fields. No parent amount was rewritten. The printed molybdate\
    \ formula/hydration remains unresolved; no unsupported exact chemical identity\
    \ is claimed.\"\n      }\n    ]\n  },\n  \"parent_amounts_changed\": false,\n\
    \  \"conversion\": \"No mass, density, hydrate or stock dilution conversion. Jensen\
    \ micromolar-to-mM comparison divides by1000; original facts and basis remain\
    \ explicit.\",\n  \"scope\": \"All direct ingredients; none of these parents contains\
    \ nested solutions. The Mattanovich added variant retains an explicit trace stock\
    \ in modification prose.\"\n}"
  dimensions:
  - name: native_decisions
    value: evidence_only numerical comparison, chemically qualified; add source-preparation
      variant
    definition: Bounded concentration-contract dispositions; not global parent approval.
    evidence_ids:
    - jensen
    - jensen-facts
    - readback
  metrics:
  - name: parent ingredient instances compared
    value: 33
    unit: ingredient instances
    denominator: 33
    minimum: 0
    maximum: 33
    definition: Direct nodes inspected for this paper comparison, not an evidence
      completeness percentage.
- assessment_id: organism-007303
  area: grounding
  topic: Scientific name, current taxonomy and growth scope
  outcome: supported
  target_ids:
  - CultureMech:007303
  evidence_ids:
  - jensen
  - jensen-facts
  - tax-416870
  - readback
  summary: Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity
    to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain;
    Table3 growth is variant-only.
  details: "{\n  \"preferred_term\": \"Lactococcus lactis subsp. lactis\",\n  \"term\"\
    : {\n    \"id\": \"NCBITaxon:416870\",\n    \"label\": \"Lactococcus cremoris\
    \ subsp. cremoris MG1363\"\n  },\n  \"strain\": \"MG1363\",\n  \"scoped_to_variant\"\
    : \"Jensen 1993 BL Medium + Arg reported preparation\",\n  \"evidence\": [\n \
    \   {\n      \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"\
    supports\": \"SUPPORT\",\n      \"snippet\": \"MG1363 in unaerated batch cultures\
    \ of BL medium or modified BL medium\",\n      \"explanation\": \"Locator: original\
    \ page 4364, Table 3 caption and treatment row +Arg; that row reports positive\
    \ growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle\
    \ magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis.\
    \ No growth-rate value, OD conversion, pH optimum or broad species growth assertion\
    \ is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363.\
    \ taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus\
    \ cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved\
    \ 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870.\
    \ The historical subspecies wording differs from current taxonomy; retain it as\
    \ the reported name, not a current classification. No equivalence between all\
    \ historical L. lactis strains and L. cremoris is inferred.\"\n    }\n  ]\n}"
- assessment_id: variant-007304
  area: quantity
  topic: Source-specific formulation and parent preservation
  outcome: supported
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - jensen
  - jensen-facts
  - readback
  summary: Selected BL liquid treatment is represented as preparation-qualified variant;
    numerical agreement is not exact chemical-form equivalence.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"L-Leucine\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Leucine\",\n        \"source_label\": \"L-Leucine\",\n\
    \        \"source_value\": \"1.5\",\n        \"source_unit\": \"mM\",\n      \
    \  \"value_mM\": \"1.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"Potassium sulfate\",\n      \"old_amount\": {\n   \
    \     \"value\": \"0.28\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n     \
    \ \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium sulfate\",\n\
    \        \"source_label\": \"K2SO4\",\n        \"source_value\": \"0.28\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.28\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[2].concentration\",\n      \"ingredient\": \"Sodium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"50.0\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Sodium chloride\",\n        \"source_label\": \"NaCl\"\
    ,\n        \"source_value\": \"50\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[3].concentration\"\
    ,\n      \"ingredient\": \"L-Isoleucine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Isoleucine\",\n   \
    \     \"source_label\": \"L-Isoleucine\",\n        \"source_value\": \"0.8\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[4].concentration\",\n      \"ingredient\": \"Folate\",\n     \
    \ \"old_amount\": {\n        \"value\": \"0.0023\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Folate\",\n        \"source_label\": \"folic acid\",\n\
    \        \"source_value\": \"2.3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.0023\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[5].concentration\",\n      \"ingredient\": \"Pyridoxal HCl\",\n  \
    \    \"old_amount\": {\n        \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Pyridoxal HCl\",\n        \"source_label\": \"pyridoxal-HCl\"\
    ,\n        \"source_value\": \"10\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.01\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[6].concentration\",\n      \"ingredient\": \"L-Glutamine\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.7\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamine\",\n        \"source_label\": \"L-Glutamine\"\
    ,\n        \"source_value\": \"0.7\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.7\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[7].concentration\"\
    ,\n      \"ingredient\": \"Tricine\",\n      \"old_amount\": {\n        \"value\"\
    : \"4.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Tricine\",\n        \"source_label\"\
    : \"Tricine\",\n        \"source_value\": \"4\",\n        \"source_unit\": \"\
    mM\",\n        \"value_mM\": \"4\",\n        \"locator\": \"page 4363, Table 1\
    \ BL column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"\
    action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[8].concentration\"\
    ,\n      \"ingredient\": \"L-Aspartate\",\n      \"old_amount\": {\n        \"\
    value\": \"1.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"source_value_mM\": \"1.0\",\n        \"\
    locator\": \"pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where\
    \ directed\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[9].concentration\",\n      \"ingredient\": \"L-Histidine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.3\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Histidine\",\n        \"source_label\": \"L-Histidine\"\
    ,\n        \"source_value\": \"0.3\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.3\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[10].concentration\"\
    ,\n      \"ingredient\": \"L-Methionine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.5\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Methionine\",\n   \
    \     \"source_label\": \"L-Methionine\",\n        \"source_value\": \"0.5\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.5\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[11].concentration\",\n      \"ingredient\": \"L-Glutamate\",\n\
    \      \"old_amount\": {\n        \"value\": \"21.0\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamate\",\n        \"source_label\": \"L-Glutamate\"\
    ,\n        \"source_value\": \"21\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"21\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"L-Asparagine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Asparagine\",\n   \
    \     \"source_label\": \"L-Asparagine\",\n        \"source_value\": \"0.8\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[13].concentration\",\n      \"ingredient\": \"Biotin\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.0004\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Biotin\",\n        \"source_label\": \"biotin\",\n    \
    \    \"source_value\": \"0.4\",\n        \"source_unit\": \"micromolar\",\n  \
    \      \"value_mM\": \"0.0004\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[14].concentration\"\
    ,\n      \"ingredient\": \"Nicotinamide\",\n      \"old_amount\": {\n        \"\
    value\": \"0.008\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Nicotinamide\",\n   \
    \     \"source_label\": \"niacinamide\",\n        \"source_value\": \"8\",\n \
    \       \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.008\",\n \
    \       \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[15].concentration\",\n      \"ingredient\"\
    : \"Cupric sulfate\",\n      \"old_amount\": {\n        \"value\": \"1e-05\",\n\
    \        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Cupric sulfate\",\n      \
    \  \"source_label\": \"CuSO4\",\n        \"source_value\": \"0.01\",\n       \
    \ \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00001\",\n     \
    \   \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[16].concentration\",\n      \"ingredient\"\
    : \"MOPS\",\n      \"old_amount\": {\n        \"value\": \"190.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n     \
    \ \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"MOPS\",\n        \"source_label\"\
    : \"MOPS\",\n        \"source_value\": \"190\",\n        \"source_unit\": \"mM\"\
    ,\n        \"value_mM\": \"190\",\n        \"locator\": \"page 4363, Table 1 BL\
    \ column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"action\"\
    : \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[17].concentration\"\
    ,\n      \"ingredient\": \"Potassium dihydrogen phosphate\",\n      \"old_amount\"\
    : {\n        \"value\": \"1.3\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n\
    \      \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium dihydrogen\
    \ phosphate\",\n        \"source_label\": \"KH2PO4\",\n        \"source_value\"\
    : \"1.3\",\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"1.3\",\n\
    \        \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\"\
    : \"No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[18].concentration\",\n      \"ingredient\": \"Thiamine HCl\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.003\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Thiamine HCl\",\n        \"source_label\": \"thiamine-HCl\"\
    ,\n        \"source_value\": \"3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.003\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[19].concentration\"\
    ,\n      \"ingredient\": \"Glucose\",\n      \"old_amount\": {\n        \"value\"\
    : \"50.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Glucose\",\n        \"\
    source_label\": \"Glucose\",\n        \"source_value\": \"50\",\n        \"source_unit\"\
    : \"mM\",\n        \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[20].concentration\"\
    ,\n      \"ingredient\": \"Riboflavin\",\n      \"old_amount\": {\n        \"\
    value\": \"0.0026\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Riboflavin\",\n     \
    \   \"source_label\": \"riboflavin\",\n        \"source_value\": \"2.6\",\n  \
    \      \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.0026\",\n \
    \       \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[21].concentration\",\n      \"ingredient\"\
    : \"L-Valine\",\n      \"old_amount\": {\n        \"value\": \"2.6\",\n      \
    \  \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"L-Valine\",\n        \"source_label\"\
    : \"L-Valine\",\n        \"source_value\": \"2.6\",\n        \"source_unit\":\
    \ \"mM\",\n        \"value_mM\": \"2.6\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[22].concentration\"\
    ,\n      \"ingredient\": \"Ferrous sulfate\",\n      \"old_amount\": {\n     \
    \   \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Ferrous sulfate\",\n\
    \        \"source_label\": \"FeSO4\",\n        \"source_value\": \"0.01\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.01\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[23].concentration\",\n      \"ingredient\": \"Cobalt chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"3e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Cobalt chloride\",\n        \"source_label\": \"CoCl2\"\
    ,\n        \"source_value\": \"0.03\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00003\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[24].concentration\",\n      \"ingredient\": \"Zinc sulfate\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Zinc sulfate\",\n        \"source_label\": \"ZnSO4\",\n\
    \        \"source_value\": \"0.01\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00001\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[25].concentration\",\n      \"ingredient\": \"Manganese chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"8e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Manganese chloride\",\n        \"source_label\": \"MnCl2\"\
    ,\n        \"source_value\": \"0.08\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00008\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[26].concentration\",\n      \"ingredient\": \"Magnesium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.52\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Magnesium chloride\",\n        \"source_label\": \"MgCl2\"\
    ,\n        \"source_value\": \"0.52\",\n        \"source_unit\": \"mM\",\n   \
    \     \"value_mM\": \"0.52\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[27].concentration\"\
    ,\n      \"ingredient\": \"Pantothenate\",\n      \"old_amount\": {\n        \"\
    value\": \"0.002\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Pantothenate\",\n   \
    \     \"source_label\": \"pantothenate\",\n        \"source_value\": \"2\",\n\
    \        \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.002\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[28].concentration\",\n      \"ingredient\"\
    : \"Boric acid\",\n      \"old_amount\": {\n        \"value\": \"0.0004\",\n \
    \       \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Boric acid\",\n        \"\
    source_label\": \"H3BO3\",\n        \"source_value\": \"0.4\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.0004\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[29].concentration\",\n      \"ingredient\": \"Calcium chloride\
    \ anhydrous\",\n      \"old_amount\": {\n        \"value\": \"0.0005\",\n    \
    \    \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Calcium chloride anhydrous\"\
    ,\n        \"source_label\": \"CaCl2\",\n        \"source_value\": \"0.0005\"\
    ,\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.0005\",\n     \
    \   \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"\
    No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[30].concentration\",\n      \"ingredient\": \"Molybdic acid ammonium\
    \ salt tetrahydrate\",\n      \"old_amount\": {\n        \"value\": \"3e-06\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Molybdic acid ammonium salt\
    \ tetrahydrate\",\n        \"source_label\": \"molybdate trace, printed formula\
    \ unresolved\",\n        \"source_value\": \"0.003\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.000003\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[31].concentration\",\n      \"ingredient\": \"Ammonium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"9.5\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Ammonium chloride\",\n        \"source_label\": \"NH4Cl\"\
    ,\n        \"source_value\": \"9.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"9.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[32].concentration\"\
    ,\n      \"ingredient\": \"Sodium acetate\",\n      \"old_amount\": {\n      \
    \  \"value\": \"15.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Sodium acetate\",\n \
    \       \"source_label\": \"Na-acetate\",\n        \"source_value\": \"15\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"15\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    }\n  ],\n  \"variant_field\": \"\
    variants[0]\",\n  \"old_variant\": null,\n  \"action\": \"add\",\n  \"variant\"\
    : {\n    \"name\": \"Jensen 1993 BL Medium + Asp reported preparation\",\n   \
    \ \"description\": \"Historical Table 3 liquid-culture treatment with the source's\
    \ preparation and pantothenate form. Numerical parent amounts match the selected\
    \ Table 1/3 treatment, but unresolved hydrate details are not asserted as exact\
    \ parent equivalence. This preparation-qualified inline variant does not duplicate\
    \ or replace the existing BL/low-MOPS full-record relationship.\",\n    \"modifications\"\
    : [\n      \"Use the paper's stock-solution filtration through 0.2-micrometer\
    \ Millipore filters rather than the parent's generic 0.22-micrometer filtration\
    \ of the complete mixture; no additional final-medium sterilization step is inferred.\"\
    ,\n      \"Use calcium pantothenate as specified in the text; Table 1 expresses\
    \ the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar\
    \ calcium salt or add an inferred calcium concentration.\",\n      \"Keep the\
    \ published nominal molar formulation from Table 1 and this Table 3 treatment.\
    \ MgCl2 hydration and the printed molybdate formula/hydration are not resolved\
    \ by the inspected source; the parent's hexahydrate/tetrahydrate labels are not\
    \ promoted to verified study identities. No mass or hydrate conversion is performed.\"\
    ,\n      \"Retain this existing treatment dose: L-Aspartate 1.0 mM. Table 3 footnote\
    \ b points to the Table 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows\
    \ state their own doses. No new base-versus-child link is created.\"\n    ],\n\
    \    \"purpose\": \"Reported liquid batch-culture treatment for MG1363.\",\n \
    \   \"evidence\": [\n      {\n        \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n        \"supports\": \"SUPPORT\",\n        \"snippet\": \"All stock solutions\
    \ were passed through Millipore filters (0.2-μm pore size).\",\n        \"explanation\"\
    : \"Locator: page 4363, Growth on plates containing eight amino acids, preparation\
    \ paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin\
    \ footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid\
    \ treatment +Asp (1 mM). All numeric ingredient amounts were compared with the\
    \ original scans; micromolar footnote values were divided by 1000 solely for comparison\
    \ to existing mM fields. No parent amount was rewritten. The printed molybdate\
    \ formula/hydration remains unresolved; no unsupported exact chemical identity\
    \ is claimed.\"\n      }\n    ]\n  },\n  \"parent_amounts_changed\": false,\n\
    \  \"conversion\": \"No mass, density, hydrate or stock dilution conversion. Jensen\
    \ micromolar-to-mM comparison divides by1000; original facts and basis remain\
    \ explicit.\",\n  \"scope\": \"All direct ingredients; none of these parents contains\
    \ nested solutions. The Mattanovich added variant retains an explicit trace stock\
    \ in modification prose.\"\n}"
  dimensions:
  - name: native_decisions
    value: evidence_only numerical comparison, chemically qualified; add source-preparation
      variant
    definition: Bounded concentration-contract dispositions; not global parent approval.
    evidence_ids:
    - jensen
    - jensen-facts
    - readback
  metrics:
  - name: parent ingredient instances compared
    value: 33
    unit: ingredient instances
    denominator: 33
    minimum: 0
    maximum: 33
    definition: Direct nodes inspected for this paper comparison, not an evidence
      completeness percentage.
- assessment_id: organism-007304
  area: grounding
  topic: Scientific name, current taxonomy and growth scope
  outcome: supported
  target_ids:
  - CultureMech:007304
  evidence_ids:
  - jensen
  - jensen-facts
  - tax-416870
  - readback
  summary: Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity
    to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain;
    Table3 growth is variant-only.
  details: "{\n  \"preferred_term\": \"Lactococcus lactis subsp. lactis\",\n  \"term\"\
    : {\n    \"id\": \"NCBITaxon:416870\",\n    \"label\": \"Lactococcus cremoris\
    \ subsp. cremoris MG1363\"\n  },\n  \"strain\": \"MG1363\",\n  \"scoped_to_variant\"\
    : \"Jensen 1993 BL Medium + Asp reported preparation\",\n  \"evidence\": [\n \
    \   {\n      \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"\
    supports\": \"SUPPORT\",\n      \"snippet\": \"MG1363 in unaerated batch cultures\
    \ of BL medium or modified BL medium\",\n      \"explanation\": \"Locator: original\
    \ page 4364, Table 3 caption and treatment row +Asp (1 mM); that row reports positive\
    \ growth and final yield. Page 4363 liquid-culture methods specify 30 C and gentle\
    \ magnetic stirring; 'unaerated' is not converted into a claim of anaerobiosis.\
    \ No growth-rate value, OD conversion, pH optimum or broad species growth assertion\
    \ is added. Reported scientific name=Lactococcus lactis subsp. lactis; strain=MG1363.\
    \ taxonomy_match=exact_strain_by_designation; NCBITaxon:416870; current canonical_label=Lactococcus\
    \ cremoris subsp. cremoris MG1363; rank=strain in NCBI Taxonomy XML retrieved\
    \ 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870.\
    \ The historical subspecies wording differs from current taxonomy; retain it as\
    \ the reported name, not a current classification. No equivalence between all\
    \ historical L. lactis strains and L. cremoris is inferred.\"\n    }\n  ]\n}"
- assessment_id: variant-007305
  area: quantity
  topic: Source-specific formulation and parent preservation
  outcome: supported
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - jensen
  - jensen-facts
  - readback
  summary: Selected BL liquid treatment is represented as preparation-qualified variant;
    numerical agreement is not exact chemical-form equivalence.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"L-Leucine\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Leucine\",\n        \"source_label\": \"L-Leucine\",\n\
    \        \"source_value\": \"1.5\",\n        \"source_unit\": \"mM\",\n      \
    \  \"value_mM\": \"1.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"Potassium sulfate\",\n      \"old_amount\": {\n   \
    \     \"value\": \"0.28\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n     \
    \ \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium sulfate\",\n\
    \        \"source_label\": \"K2SO4\",\n        \"source_value\": \"0.28\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.28\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[2].concentration\",\n      \"ingredient\": \"Sodium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"50.0\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Sodium chloride\",\n        \"source_label\": \"NaCl\"\
    ,\n        \"source_value\": \"50\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[3].concentration\"\
    ,\n      \"ingredient\": \"L-Isoleucine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Isoleucine\",\n   \
    \     \"source_label\": \"L-Isoleucine\",\n        \"source_value\": \"0.8\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[4].concentration\",\n      \"ingredient\": \"Folate\",\n     \
    \ \"old_amount\": {\n        \"value\": \"0.0023\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Folate\",\n        \"source_label\": \"folic acid\",\n\
    \        \"source_value\": \"2.3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.0023\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[5].concentration\",\n      \"ingredient\": \"Pyridoxal HCl\",\n  \
    \    \"old_amount\": {\n        \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Pyridoxal HCl\",\n        \"source_label\": \"pyridoxal-HCl\"\
    ,\n        \"source_value\": \"10\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.01\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[6].concentration\",\n      \"ingredient\": \"L-Glutamine\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.7\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamine\",\n        \"source_label\": \"L-Glutamine\"\
    ,\n        \"source_value\": \"0.7\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.7\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[7].concentration\"\
    ,\n      \"ingredient\": \"Tricine\",\n      \"old_amount\": {\n        \"value\"\
    : \"4.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Tricine\",\n        \"source_label\"\
    : \"Tricine\",\n        \"source_value\": \"4\",\n        \"source_unit\": \"\
    mM\",\n        \"value_mM\": \"4\",\n        \"locator\": \"page 4363, Table 1\
    \ BL column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"\
    action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[8].concentration\"\
    ,\n      \"ingredient\": \"L-Histidine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.3\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Histidine\",\n    \
    \    \"source_label\": \"L-Histidine\",\n        \"source_value\": \"0.3\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.3\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[9].concentration\",\n      \"ingredient\": \"L-Methionine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Methionine\",\n        \"source_label\": \"L-Methionine\"\
    ,\n        \"source_value\": \"0.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[10].concentration\"\
    ,\n      \"ingredient\": \"L-Glutamate\",\n      \"old_amount\": {\n        \"\
    value\": \"21.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Glutamate\",\n    \
    \    \"source_label\": \"L-Glutamate\",\n        \"source_value\": \"21\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"21\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[11].concentration\",\n      \"ingredient\": \"L-Asparagine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Asparagine\",\n        \"source_label\": \"L-Asparagine\"\
    ,\n        \"source_value\": \"0.8\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.8\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"Biotin\",\n      \"old_amount\": {\n        \"value\"\
    : \"0.0004\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Biotin\",\n        \"\
    source_label\": \"biotin\",\n        \"source_value\": \"0.4\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.0004\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[13].concentration\",\n      \"ingredient\": \"Nicotinamide\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.008\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Nicotinamide\",\n        \"source_label\": \"niacinamide\"\
    ,\n        \"source_value\": \"8\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.008\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[14].concentration\"\
    ,\n      \"ingredient\": \"Cupric sulfate\",\n      \"old_amount\": {\n      \
    \  \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Cupric sulfate\",\n \
    \       \"source_label\": \"CuSO4\",\n        \"source_value\": \"0.01\",\n  \
    \      \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00001\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[15].concentration\",\n      \"ingredient\"\
    : \"MOPS\",\n      \"old_amount\": {\n        \"value\": \"40.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n     \
    \ \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"source_value_mM\": \"40\",\n        \"locator\"\
    : \"pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[16].concentration\",\n      \"ingredient\": \"Potassium dihydrogen\
    \ phosphate\",\n      \"old_amount\": {\n        \"value\": \"1.3\",\n       \
    \ \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n \
    \     \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Potassium dihydrogen phosphate\"\
    ,\n        \"source_label\": \"KH2PO4\",\n        \"source_value\": \"1.3\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"1.3\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[17].concentration\",\n      \"ingredient\": \"Thiamine HCl\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.003\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Thiamine HCl\",\n        \"source_label\": \"thiamine-HCl\"\
    ,\n        \"source_value\": \"3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.003\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[18].concentration\"\
    ,\n      \"ingredient\": \"Glucose\",\n      \"old_amount\": {\n        \"value\"\
    : \"50.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Glucose\",\n        \"\
    source_label\": \"Glucose\",\n        \"source_value\": \"50\",\n        \"source_unit\"\
    : \"mM\",\n        \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[19].concentration\"\
    ,\n      \"ingredient\": \"Riboflavin\",\n      \"old_amount\": {\n        \"\
    value\": \"0.0026\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Riboflavin\",\n     \
    \   \"source_label\": \"riboflavin\",\n        \"source_value\": \"2.6\",\n  \
    \      \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.0026\",\n \
    \       \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[20].concentration\",\n      \"ingredient\"\
    : \"L-Valine\",\n      \"old_amount\": {\n        \"value\": \"2.6\",\n      \
    \  \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"L-Valine\",\n        \"source_label\"\
    : \"L-Valine\",\n        \"source_value\": \"2.6\",\n        \"source_unit\":\
    \ \"mM\",\n        \"value_mM\": \"2.6\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[21].concentration\"\
    ,\n      \"ingredient\": \"Ferrous sulfate\",\n      \"old_amount\": {\n     \
    \   \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Ferrous sulfate\",\n\
    \        \"source_label\": \"FeSO4\",\n        \"source_value\": \"0.01\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.01\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[22].concentration\",\n      \"ingredient\": \"Cobalt chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"3e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Cobalt chloride\",\n        \"source_label\": \"CoCl2\"\
    ,\n        \"source_value\": \"0.03\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00003\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[23].concentration\",\n      \"ingredient\": \"Zinc sulfate\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Zinc sulfate\",\n        \"source_label\": \"ZnSO4\",\n\
    \        \"source_value\": \"0.01\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00001\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[24].concentration\",\n      \"ingredient\": \"Manganese chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"8e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Manganese chloride\",\n        \"source_label\": \"MnCl2\"\
    ,\n        \"source_value\": \"0.08\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00008\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[25].concentration\",\n      \"ingredient\": \"Magnesium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.52\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Magnesium chloride\",\n        \"source_label\": \"MgCl2\"\
    ,\n        \"source_value\": \"0.52\",\n        \"source_unit\": \"mM\",\n   \
    \     \"value_mM\": \"0.52\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[26].concentration\"\
    ,\n      \"ingredient\": \"Pantothenate\",\n      \"old_amount\": {\n        \"\
    value\": \"0.002\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Pantothenate\",\n   \
    \     \"source_label\": \"pantothenate\",\n        \"source_value\": \"2\",\n\
    \        \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.002\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[27].concentration\",\n      \"ingredient\"\
    : \"Boric acid\",\n      \"old_amount\": {\n        \"value\": \"0.0004\",\n \
    \       \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Boric acid\",\n        \"\
    source_label\": \"H3BO3\",\n        \"source_value\": \"0.4\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.0004\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[28].concentration\",\n      \"ingredient\": \"Calcium chloride\
    \ anhydrous\",\n      \"old_amount\": {\n        \"value\": \"0.0005\",\n    \
    \    \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Calcium chloride anhydrous\"\
    ,\n        \"source_label\": \"CaCl2\",\n        \"source_value\": \"0.0005\"\
    ,\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.0005\",\n     \
    \   \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"\
    No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[29].concentration\",\n      \"ingredient\": \"Molybdic acid ammonium\
    \ salt tetrahydrate\",\n      \"old_amount\": {\n        \"value\": \"3e-06\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Molybdic acid ammonium salt\
    \ tetrahydrate\",\n        \"source_label\": \"molybdate trace, printed formula\
    \ unresolved\",\n        \"source_value\": \"0.003\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.000003\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[30].concentration\",\n      \"ingredient\": \"Ammonium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"9.5\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Ammonium chloride\",\n        \"source_label\": \"NH4Cl\"\
    ,\n        \"source_value\": \"9.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"9.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[31].concentration\"\
    ,\n      \"ingredient\": \"Sodium acetate\",\n      \"old_amount\": {\n      \
    \  \"value\": \"15.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Sodium acetate\",\n \
    \       \"source_label\": \"Na-acetate\",\n        \"source_value\": \"15\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"15\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    }\n  ],\n  \"variant_field\": \"\
    variants[0]\",\n  \"old_variant\": null,\n  \"action\": \"add\",\n  \"variant\"\
    : {\n    \"name\": \"Jensen 1993 BL Medium, Low MOPS reported preparation\",\n\
    \    \"description\": \"Historical Table 3 liquid-culture treatment with the source's\
    \ preparation and pantothenate form. Numerical parent amounts match the selected\
    \ Table 1/3 treatment, but unresolved hydrate details are not asserted as exact\
    \ parent equivalence. This preparation-qualified inline variant does not duplicate\
    \ or replace the existing BL/low-MOPS full-record relationship.\",\n    \"modifications\"\
    : [\n      \"Use the paper's stock-solution filtration through 0.2-micrometer\
    \ Millipore filters rather than the parent's generic 0.22-micrometer filtration\
    \ of the complete mixture; no additional final-medium sterilization step is inferred.\"\
    ,\n      \"Use calcium pantothenate as specified in the text; Table 1 expresses\
    \ the dose as 2 micromolar pantothenate. Do not reinterpret that as 2 micromolar\
    \ calcium salt or add an inferred calcium concentration.\",\n      \"Keep the\
    \ published nominal molar formulation from Table 1 and this Table 3 treatment.\
    \ MgCl2 hydration and the printed molybdate formula/hydration are not resolved\
    \ by the inspected source; the parent's hexahydrate/tetrahydrate labels are not\
    \ promoted to verified study identities. No mass or hydrate conversion is performed.\"\
    ,\n      \"Retain this existing treatment dose: MOPS 40 mM. Table 3 footnote b\
    \ points to the Table 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows\
    \ state their own doses. No new base-versus-child link is created.\"\n    ],\n\
    \    \"purpose\": \"Reported liquid batch-culture treatment for MG1363.\",\n \
    \   \"evidence\": [\n      {\n        \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n        \"supports\": \"SUPPORT\",\n        \"snippet\": \"All stock solutions\
    \ were passed through Millipore filters (0.2-μm pore size).\",\n        \"explanation\"\
    : \"Locator: page 4363, Growth on plates containing eight amino acids, preparation\
    \ paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin\
    \ footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid\
    \ treatment Low MOPS (0.04 M). All numeric ingredient amounts were compared with\
    \ the original scans; micromolar footnote values were divided by 1000 solely for\
    \ comparison to existing mM fields. No parent amount was rewritten. The printed\
    \ molybdate formula/hydration remains unresolved; no unsupported exact chemical\
    \ identity is claimed.\"\n      }\n    ]\n  },\n  \"parent_amounts_changed\":\
    \ false,\n  \"conversion\": \"No mass, density, hydrate or stock dilution conversion.\
    \ Jensen micromolar-to-mM comparison divides by1000; original facts and basis\
    \ remain explicit.\",\n  \"scope\": \"All direct ingredients; none of these parents\
    \ contains nested solutions. The Mattanovich added variant retains an explicit\
    \ trace stock in modification prose.\"\n}"
  dimensions:
  - name: native_decisions
    value: evidence_only numerical comparison, chemically qualified; add source-preparation
      variant
    definition: Bounded concentration-contract dispositions; not global parent approval.
    evidence_ids:
    - jensen
    - jensen-facts
    - readback
  metrics:
  - name: parent ingredient instances compared
    value: 32
    unit: ingredient instances
    denominator: 32
    minimum: 0
    maximum: 32
    definition: Direct nodes inspected for this paper comparison, not an evidence
      completeness percentage.
- assessment_id: organism-007305
  area: grounding
  topic: Scientific name, current taxonomy and growth scope
  outcome: supported
  target_ids:
  - CultureMech:007305
  evidence_ids:
  - jensen
  - jensen-facts
  - tax-416870
  - readback
  summary: Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity
    to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain;
    Table3 growth is variant-only.
  details: "{\n  \"preferred_term\": \"Lactococcus lactis subsp. lactis\",\n  \"term\"\
    : {\n    \"id\": \"NCBITaxon:416870\",\n    \"label\": \"Lactococcus cremoris\
    \ subsp. cremoris MG1363\"\n  },\n  \"strain\": \"MG1363\",\n  \"scoped_to_variant\"\
    : \"Jensen 1993 BL Medium, Low MOPS reported preparation\",\n  \"evidence\": [\n\
    \    {\n      \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"supports\": \"SUPPORT\",\n      \"snippet\": \"MG1363 in unaerated batch cultures\
    \ of BL medium or modified BL medium\",\n      \"explanation\": \"Locator: original\
    \ page 4364, Table 3 caption and treatment row Low MOPS (0.04 M); that row reports\
    \ positive growth and final yield. Page 4363 liquid-culture methods specify 30\
    \ C and gentle magnetic stirring; 'unaerated' is not converted into a claim of\
    \ anaerobiosis. No growth-rate value, OD conversion, pH optimum or broad species\
    \ growth assertion is added. Reported scientific name=Lactococcus lactis subsp.\
    \ lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation; NCBITaxon:416870;\
    \ current canonical_label=Lactococcus cremoris subsp. cremoris MG1363; rank=strain\
    \ in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870.\
    \ The historical subspecies wording differs from current taxonomy; retain it as\
    \ the reported name, not a current classification. No equivalence between all\
    \ historical L. lactis strains and L. cremoris is inferred.\"\n    }\n  ]\n}"
- assessment_id: variant-007306
  area: quantity
  topic: Source-specific formulation and parent preservation
  outcome: supported
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - jensen
  - jensen-facts
  - readback
  summary: Selected BL liquid treatment is represented as preparation-qualified variant;
    numerical agreement is not exact chemical-form equivalence.
  details: "{\n  \"parent_ingredient_comparisons\": [\n    {\n      \"field_path\"\
    : \"ingredients[0].concentration\",\n      \"ingredient\": \"L-Leucine\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Leucine\",\n        \"source_label\": \"L-Leucine\",\n\
    \        \"source_value\": \"1.5\",\n        \"source_unit\": \"mM\",\n      \
    \  \"value_mM\": \"1.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[1].concentration\"\
    ,\n      \"ingredient\": \"Potassium sulfate\",\n      \"old_amount\": {\n   \
    \     \"value\": \"0.28\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n     \
    \ \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium sulfate\",\n\
    \        \"source_label\": \"K2SO4\",\n        \"source_value\": \"0.28\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.28\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[2].concentration\",\n      \"ingredient\": \"Sodium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"50.0\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Sodium chloride\",\n        \"source_label\": \"NaCl\"\
    ,\n        \"source_value\": \"50\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[3].concentration\"\
    ,\n      \"ingredient\": \"L-Isoleucine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Isoleucine\",\n   \
    \     \"source_label\": \"L-Isoleucine\",\n        \"source_value\": \"0.8\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[4].concentration\",\n      \"ingredient\": \"Folate\",\n     \
    \ \"old_amount\": {\n        \"value\": \"0.0023\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Folate\",\n        \"source_label\": \"folic acid\",\n\
    \        \"source_value\": \"2.3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.0023\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[5].concentration\",\n      \"ingredient\": \"L-Tryptophan\",\n   \
    \   \"old_amount\": {\n        \"value\": \"0.5\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"source_value_mM\": \"0.5\",\n        \"locator\": \"pages 4363-4364, Table\
    \ 3 row/footnote b with Table 1 SA column where directed\"\n      },\n      \"\
    action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[6].concentration\"\
    ,\n      \"ingredient\": \"L-Serine\",\n      \"old_amount\": {\n        \"value\"\
    : \"2.9\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"source_value_mM\": \"2.9\",\n        \"locator\"\
    : \"pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where directed\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[7].concentration\",\n      \"ingredient\": \"Pyridoxal HCl\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Pyridoxal HCl\",\n        \"source_label\": \"pyridoxal-HCl\"\
    ,\n        \"source_value\": \"10\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.01\",\n        \"locator\": \"page 4363, Table 1\
    \ footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n \
    \     },\n      \"action\": \"parent unchanged; variant evidence added\",\n  \
    \    \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[8].concentration\",\n      \"ingredient\": \"L-Glutamine\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.7\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamine\",\n        \"source_label\": \"L-Glutamine\"\
    ,\n        \"source_value\": \"0.7\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.7\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[9].concentration\"\
    ,\n      \"ingredient\": \"Tricine\",\n      \"old_amount\": {\n        \"value\"\
    : \"4.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Tricine\",\n        \"source_label\"\
    : \"Tricine\",\n        \"source_value\": \"4\",\n        \"source_unit\": \"\
    mM\",\n        \"value_mM\": \"4\",\n        \"locator\": \"page 4363, Table 1\
    \ BL column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"\
    action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[10].concentration\"\
    ,\n      \"ingredient\": \"L-Arginine\",\n      \"old_amount\": {\n        \"\
    value\": \"1.1\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"source_value_mM\": \"1.1\",\n        \"\
    locator\": \"pages 4363-4364, Table 3 row/footnote b with Table 1 SA column where\
    \ directed\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[11].concentration\",\n      \"ingredient\": \"L-Histidine\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.3\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Histidine\",\n        \"source_label\": \"L-Histidine\"\
    ,\n        \"source_value\": \"0.3\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"0.3\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[12].concentration\"\
    ,\n      \"ingredient\": \"L-Methionine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.5\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Methionine\",\n   \
    \     \"source_label\": \"L-Methionine\",\n        \"source_value\": \"0.5\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.5\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[13].concentration\",\n      \"ingredient\": \"L-Glutamate\",\n\
    \      \"old_amount\": {\n        \"value\": \"21.0\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"L-Glutamate\",\n        \"source_label\": \"L-Glutamate\"\
    ,\n        \"source_value\": \"21\",\n        \"source_unit\": \"mM\",\n     \
    \   \"value_mM\": \"21\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[14].concentration\"\
    ,\n      \"ingredient\": \"L-Asparagine\",\n      \"old_amount\": {\n        \"\
    value\": \"0.8\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"L-Asparagine\",\n   \
    \     \"source_label\": \"L-Asparagine\",\n        \"source_value\": \"0.8\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.8\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[15].concentration\",\n      \"ingredient\": \"Biotin\",\n    \
    \  \"old_amount\": {\n        \"value\": \"0.0004\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Biotin\",\n        \"source_label\": \"biotin\",\n    \
    \    \"source_value\": \"0.4\",\n        \"source_unit\": \"micromolar\",\n  \
    \      \"value_mM\": \"0.0004\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[16].concentration\"\
    ,\n      \"ingredient\": \"Nicotinamide\",\n      \"old_amount\": {\n        \"\
    value\": \"0.008\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Nicotinamide\",\n   \
    \     \"source_label\": \"niacinamide\",\n        \"source_value\": \"8\",\n \
    \       \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.008\",\n \
    \       \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[17].concentration\",\n      \"ingredient\"\
    : \"Cupric sulfate\",\n      \"old_amount\": {\n        \"value\": \"1e-05\",\n\
    \        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Cupric sulfate\",\n      \
    \  \"source_label\": \"CuSO4\",\n        \"source_value\": \"0.01\",\n       \
    \ \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.00001\",\n     \
    \   \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[18].concentration\",\n      \"ingredient\"\
    : \"MOPS\",\n      \"old_amount\": {\n        \"value\": \"190.0\",\n        \"\
    unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n     \
    \ \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"MOPS\",\n        \"source_label\"\
    : \"MOPS\",\n        \"source_value\": \"190\",\n        \"source_unit\": \"mM\"\
    ,\n        \"value_mM\": \"190\",\n        \"locator\": \"page 4363, Table 1 BL\
    \ column\",\n        \"calculation\": \"No conversion\"\n      },\n      \"action\"\
    : \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[19].concentration\"\
    ,\n      \"ingredient\": \"Potassium dihydrogen phosphate\",\n      \"old_amount\"\
    : {\n        \"value\": \"1.3\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n\
    \      \"status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Potassium dihydrogen\
    \ phosphate\",\n        \"source_label\": \"KH2PO4\",\n        \"source_value\"\
    : \"1.3\",\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"1.3\",\n\
    \        \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\"\
    : \"No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[20].concentration\",\n      \"ingredient\": \"Thiamine HCl\",\n\
    \      \"old_amount\": {\n        \"value\": \"0.003\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Thiamine HCl\",\n        \"source_label\": \"thiamine-HCl\"\
    ,\n        \"source_value\": \"3\",\n        \"source_unit\": \"micromolar\",\n\
    \        \"value_mM\": \"0.003\",\n        \"locator\": \"page 4363, Table 1 footnote\
    \ b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n      },\n\
    \      \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[21].concentration\"\
    ,\n      \"ingredient\": \"Glucose\",\n      \"old_amount\": {\n        \"value\"\
    : \"50.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"\
    evidence_only\",\n      \"qualification\": \"Numerical comparison only, not chemical-form\
    \ or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Glucose\",\n        \"\
    source_label\": \"Glucose\",\n        \"source_value\": \"50\",\n        \"source_unit\"\
    : \"mM\",\n        \"value_mM\": \"50\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[22].concentration\"\
    ,\n      \"ingredient\": \"Riboflavin\",\n      \"old_amount\": {\n        \"\
    value\": \"0.0026\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Riboflavin\",\n     \
    \   \"source_label\": \"riboflavin\",\n        \"source_value\": \"2.6\",\n  \
    \      \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.0026\",\n \
    \       \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[23].concentration\",\n      \"ingredient\"\
    : \"L-Valine\",\n      \"old_amount\": {\n        \"value\": \"2.6\",\n      \
    \  \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"L-Valine\",\n        \"source_label\"\
    : \"L-Valine\",\n        \"source_value\": \"2.6\",\n        \"source_unit\":\
    \ \"mM\",\n        \"value_mM\": \"2.6\",\n        \"locator\": \"page 4363, Table\
    \ 1 BL column\",\n        \"calculation\": \"No conversion\"\n      },\n     \
    \ \"action\": \"parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[24].concentration\"\
    ,\n      \"ingredient\": \"Ferrous sulfate\",\n      \"old_amount\": {\n     \
    \   \"value\": \"0.01\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Ferrous sulfate\",\n\
    \        \"source_label\": \"FeSO4\",\n        \"source_value\": \"0.01\",\n \
    \       \"source_unit\": \"mM\",\n        \"value_mM\": \"0.01\",\n        \"\
    locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\":\
    \ \"ingredients[25].concentration\",\n      \"ingredient\": \"Cobalt chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"3e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Cobalt chloride\",\n        \"source_label\": \"CoCl2\"\
    ,\n        \"source_value\": \"0.03\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00003\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[26].concentration\",\n      \"ingredient\": \"Zinc sulfate\",\n  \
    \    \"old_amount\": {\n        \"value\": \"1e-05\",\n        \"unit\": \"MILLIMOLAR\"\
    \n      },\n      \"status\": \"evidence_only\",\n      \"qualification\": \"\
    Numerical comparison only, not chemical-form or whole-parent certification; evidence\
    \ attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Zinc sulfate\",\n        \"source_label\": \"ZnSO4\",\n\
    \        \"source_value\": \"0.01\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00001\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[27].concentration\",\n      \"ingredient\": \"Manganese chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"8e-05\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Manganese chloride\",\n        \"source_label\": \"MnCl2\"\
    ,\n        \"source_value\": \"0.08\",\n        \"source_unit\": \"micromolar\"\
    ,\n        \"value_mM\": \"0.00008\",\n        \"locator\": \"page 4363, Table\
    \ 1 footnote b or c\",\n        \"calculation\": \"1 micromolar = 0.001 mM\"\n\
    \      },\n      \"action\": \"parent unchanged; variant evidence added\",\n \
    \     \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\": \"\
    ingredients[28].concentration\",\n      \"ingredient\": \"Magnesium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"0.52\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Magnesium chloride\",\n        \"source_label\": \"MgCl2\"\
    ,\n        \"source_value\": \"0.52\",\n        \"source_unit\": \"mM\",\n   \
    \     \"value_mM\": \"0.52\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[29].concentration\"\
    ,\n      \"ingredient\": \"Pantothenate\",\n      \"old_amount\": {\n        \"\
    value\": \"0.002\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\"\
    : \"evidence_only\",\n      \"qualification\": \"Numerical comparison only, not\
    \ chemical-form or whole-parent certification; evidence attached to the preparation-qualified\
    \ variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Pantothenate\",\n   \
    \     \"source_label\": \"pantothenate\",\n        \"source_value\": \"2\",\n\
    \        \"source_unit\": \"micromolar\",\n        \"value_mM\": \"0.002\",\n\
    \        \"locator\": \"page 4363, Table 1 footnote b or c\",\n        \"calculation\"\
    : \"1 micromolar = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged;\
    \ variant evidence added\",\n      \"proposed_parent_amount\": null\n    },\n\
    \    {\n      \"field_path\": \"ingredients[30].concentration\",\n      \"ingredient\"\
    : \"Boric acid\",\n      \"old_amount\": {\n        \"value\": \"0.0004\",\n \
    \       \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Boric acid\",\n        \"\
    source_label\": \"H3BO3\",\n        \"source_value\": \"0.4\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.0004\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[31].concentration\",\n      \"ingredient\": \"Calcium chloride\
    \ anhydrous\",\n      \"old_amount\": {\n        \"value\": \"0.0005\",\n    \
    \    \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n\
    \      \"qualification\": \"Numerical comparison only, not chemical-form or whole-parent\
    \ certification; evidence attached to the preparation-qualified variant.\",\n\
    \      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n     \
    \ \"source_fact\": {\n        \"record_label\": \"Calcium chloride anhydrous\"\
    ,\n        \"source_label\": \"CaCl2\",\n        \"source_value\": \"0.0005\"\
    ,\n        \"source_unit\": \"mM\",\n        \"value_mM\": \"0.0005\",\n     \
    \   \"locator\": \"page 4363, Table 1 BL column\",\n        \"calculation\": \"\
    No conversion\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[32].concentration\",\n      \"ingredient\": \"Molybdic acid ammonium\
    \ salt tetrahydrate\",\n      \"old_amount\": {\n        \"value\": \"3e-06\"\
    ,\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\"\
    ,\n      \"qualification\": \"Numerical comparison only, not chemical-form or\
    \ whole-parent certification; evidence attached to the preparation-qualified variant.\"\
    ,\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n   \
    \   \"source_fact\": {\n        \"record_label\": \"Molybdic acid ammonium salt\
    \ tetrahydrate\",\n        \"source_label\": \"molybdate trace, printed formula\
    \ unresolved\",\n        \"source_value\": \"0.003\",\n        \"source_unit\"\
    : \"micromolar\",\n        \"value_mM\": \"0.000003\",\n        \"locator\": \"\
    page 4363, Table 1 footnote b or c\",\n        \"calculation\": \"1 micromolar\
    \ = 0.001 mM\"\n      },\n      \"action\": \"parent unchanged; variant evidence\
    \ added\",\n      \"proposed_parent_amount\": null\n    },\n    {\n      \"field_path\"\
    : \"ingredients[33].concentration\",\n      \"ingredient\": \"Ammonium chloride\"\
    ,\n      \"old_amount\": {\n        \"value\": \"9.5\",\n        \"unit\": \"\
    MILLIMOLAR\"\n      },\n      \"status\": \"evidence_only\",\n      \"qualification\"\
    : \"Numerical comparison only, not chemical-form or whole-parent certification;\
    \ evidence attached to the preparation-qualified variant.\",\n      \"source_reference\"\
    : \"doi:10.1128/aem.59.12.4363-4366.1993\",\n      \"source_fact\": {\n      \
    \  \"record_label\": \"Ammonium chloride\",\n        \"source_label\": \"NH4Cl\"\
    ,\n        \"source_value\": \"9.5\",\n        \"source_unit\": \"mM\",\n    \
    \    \"value_mM\": \"9.5\",\n        \"locator\": \"page 4363, Table 1 BL column\"\
    ,\n        \"calculation\": \"No conversion\"\n      },\n      \"action\": \"\
    parent unchanged; variant evidence added\",\n      \"proposed_parent_amount\"\
    : null\n    },\n    {\n      \"field_path\": \"ingredients[34].concentration\"\
    ,\n      \"ingredient\": \"Sodium acetate\",\n      \"old_amount\": {\n      \
    \  \"value\": \"15.0\",\n        \"unit\": \"MILLIMOLAR\"\n      },\n      \"\
    status\": \"evidence_only\",\n      \"qualification\": \"Numerical comparison\
    \ only, not chemical-form or whole-parent certification; evidence attached to\
    \ the preparation-qualified variant.\",\n      \"source_reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\"\
    ,\n      \"source_fact\": {\n        \"record_label\": \"Sodium acetate\",\n \
    \       \"source_label\": \"Na-acetate\",\n        \"source_value\": \"15\",\n\
    \        \"source_unit\": \"mM\",\n        \"value_mM\": \"15\",\n        \"locator\"\
    : \"page 4363, Table 1 BL column\",\n        \"calculation\": \"No conversion\"\
    \n      },\n      \"action\": \"parent unchanged; variant evidence added\",\n\
    \      \"proposed_parent_amount\": null\n    }\n  ],\n  \"variant_field\": \"\
    variants[0]\",\n  \"old_variant\": null,\n  \"action\": \"add\",\n  \"variant\"\
    : {\n    \"name\": \"Jensen 1993 BL Medium + Arg + Ser + Trp reported preparation\"\
    ,\n    \"description\": \"Historical Table 3 liquid-culture treatment with the\
    \ source's preparation and pantothenate form. Numerical parent amounts match the\
    \ selected Table 1/3 treatment, but unresolved hydrate details are not asserted\
    \ as exact parent equivalence. This preparation-qualified inline variant does\
    \ not duplicate or replace the existing BL/low-MOPS full-record relationship.\"\
    ,\n    \"modifications\": [\n      \"Use the paper's stock-solution filtration\
    \ through 0.2-micrometer Millipore filters rather than the parent's generic 0.22-micrometer\
    \ filtration of the complete mixture; no additional final-medium sterilization\
    \ step is inferred.\",\n      \"Use calcium pantothenate as specified in the text;\
    \ Table 1 expresses the dose as 2 micromolar pantothenate. Do not reinterpret\
    \ that as 2 micromolar calcium salt or add an inferred calcium concentration.\"\
    ,\n      \"Keep the published nominal molar formulation from Table 1 and this\
    \ Table 3 treatment. MgCl2 hydration and the printed molybdate formula/hydration\
    \ are not resolved by the inspected source; the parent's hexahydrate/tetrahydrate\
    \ labels are not promoted to verified study identities. No mass or hydrate conversion\
    \ is performed.\",\n      \"Retain this existing treatment dose: L-Arginine 1.1\
    \ mM, L-Serine 2.9 mM, L-Tryptophan 0.5 mM. Table 3 footnote b points to the Table\
    \ 1 SA-column Arg/Ser/Trp doses; the Asp and low-MOPS rows state their own doses.\
    \ No new base-versus-child link is created.\"\n    ],\n    \"purpose\": \"Reported\
    \ liquid batch-culture treatment for MG1363.\",\n    \"evidence\": [\n      {\n\
    \        \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n        \"\
    supports\": \"SUPPORT\",\n        \"snippet\": \"All stock solutions were passed\
    \ through Millipore filters (0.2-μm pore size).\",\n        \"explanation\": \"\
    Locator: page 4363, Growth on plates containing eight amino acids, preparation\
    \ paragraph; the next sentence names 'calcium pantothenate'. Table 1 and its vitamin\
    \ footnote specify the nominal amounts; page 4364 Table 3 identifies the liquid\
    \ treatment +Arg, Ser, and Trp. All numeric ingredient amounts were compared with\
    \ the original scans; micromolar footnote values were divided by 1000 solely for\
    \ comparison to existing mM fields. No parent amount was rewritten. The printed\
    \ molybdate formula/hydration remains unresolved; no unsupported exact chemical\
    \ identity is claimed.\"\n      }\n    ]\n  },\n  \"parent_amounts_changed\":\
    \ false,\n  \"conversion\": \"No mass, density, hydrate or stock dilution conversion.\
    \ Jensen micromolar-to-mM comparison divides by1000; original facts and basis\
    \ remain explicit.\",\n  \"scope\": \"All direct ingredients; none of these parents\
    \ contains nested solutions. The Mattanovich added variant retains an explicit\
    \ trace stock in modification prose.\"\n}"
  dimensions:
  - name: native_decisions
    value: evidence_only numerical comparison, chemically qualified; add source-preparation
      variant
    definition: Bounded concentration-contract dispositions; not global parent approval.
    evidence_ids:
    - jensen
    - jensen-facts
    - readback
  metrics:
  - name: parent ingredient instances compared
    value: 35
    unit: ingredient instances
    denominator: 35
    minimum: 0
    maximum: 35
    definition: Direct nodes inspected for this paper comparison, not an evidence
      completeness percentage.
- assessment_id: organism-007306
  area: grounding
  topic: Scientific name, current taxonomy and growth scope
  outcome: supported
  target_ids:
  - CultureMech:007306
  evidence_ids:
  - jensen
  - jensen-facts
  - tax-416870
  - readback
  summary: Historical Lactococcus lactis subsp. lactis MG1363 maps by strain identity
    to Lactococcus cremoris subsp. cremoris MG1363, NCBITaxon416870, rank strain;
    Table3 growth is variant-only.
  details: "{\n  \"preferred_term\": \"Lactococcus lactis subsp. lactis\",\n  \"term\"\
    : {\n    \"id\": \"NCBITaxon:416870\",\n    \"label\": \"Lactococcus cremoris\
    \ subsp. cremoris MG1363\"\n  },\n  \"strain\": \"MG1363\",\n  \"scoped_to_variant\"\
    : \"Jensen 1993 BL Medium + Arg + Ser + Trp reported preparation\",\n  \"evidence\"\
    : [\n    {\n      \"reference\": \"doi:10.1128/aem.59.12.4363-4366.1993\",\n \
    \     \"supports\": \"SUPPORT\",\n      \"snippet\": \"MG1363 in unaerated batch\
    \ cultures of BL medium or modified BL medium\",\n      \"explanation\": \"Locator:\
    \ original page 4364, Table 3 caption and treatment row +Arg, Ser, and Trp; that\
    \ row reports positive growth and final yield. Page 4363 liquid-culture methods\
    \ specify 30 C and gentle magnetic stirring; 'unaerated' is not converted into\
    \ a claim of anaerobiosis. No growth-rate value, OD conversion, pH optimum or\
    \ broad species growth assertion is added. Reported scientific name=Lactococcus\
    \ lactis subsp. lactis; strain=MG1363. taxonomy_match=exact_strain_by_designation;\
    \ NCBITaxon:416870; current canonical_label=Lactococcus cremoris subsp. cremoris\
    \ MG1363; rank=strain in NCBI Taxonomy XML retrieved 2026-10-13; source=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=416870.\
    \ The historical subspecies wording differs from current taxonomy; retain it as\
    \ the reported name, not a current classification. No equivalence between all\
    \ historical L. lactis strains and L. cremoris is inferred.\"\n    }\n  ]\n}"
- assessment_id: retained-gaps
  area: evidence
  topic: Unresolved parent chemistry and preparation
  outcome: concern
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  evidence_ids:
  - supplement
  - jensen
  - readback
  summary: Parent molar conversions/acid density, salt hydration and preparation cannot
    all be certified. The variants explicitly retain source units and qualification;
    no hidden normalization or blanket parent approval.
findings:
- finding_id: variant-export
  issue_key: kgx-variant-growth-scope-loss-original-papers
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: KGX drops these six inline variant scopes
  description: YAML scopes the observations correctly, but current edge construction
    emits the parent medium ID. Withholding publication is a mitigation, not an exporter
    repair.
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  field_paths:
  - target_organisms[0].scoped_to_variant
  evidence_ids:
  - readback
  owner_paths:
  - repository: culturebotai/CultureMech
    path: src/culturemech/export/kgx_export.py
    role: scope-preserving growth edge construction
  related_findings:
  - repository: culturebotai/CultureMech
    review_id: 20261013T044947Z-ams1-carini-paper-variants
    finding_id: variant-export
- finding_id: fungal-category
  issue_key: mattanovich-batch-fungal-category-007250
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Yeast cultivation record retains bacterial category
  description: The record remains category bacterial although the source organism
    is the yeast Komagataella pastoris. This pre-existing routing/classification mismatch
    was retained during citation-only curation, not endorsed.
  target_ids:
  - CultureMech:007250
  field_paths:
  - category
  evidence_ids:
  - mattanovich
  - tax-638632
  - readback
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
    role: maintained recipe category and ownership
actions:
- action_id: preserve-variant-export
  description: Repair or fail closed on variant-scoped growth before publishing.
  finding_ids:
  - variant-export
  target_ids:
  - CultureMech:007250
  - CultureMech:007302
  - CultureMech:007303
  - CultureMech:007304
  - CultureMech:007305
  - CultureMech:007306
  owner_paths:
  - repository: culturebotai/CultureMech
    path: src/culturemech/export/kgx_export.py
    role: scope-preserving growth edge construction
  acceptance_checks:
  - None of these parent records receives a variant-only growth edge.
  - Tests retain valid ordinary unscoped growth and explicitly cover variant scope.
- action_id: review-fungal-category
  description: Correct the yeast recipe category through a separately scoped ownership
    and path/link audit.
  finding_ids:
  - fungal-category
  target_ids:
  - CultureMech:007250
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/batch_medium_mattanovich_et_al.yaml
    role: maintained recipe category and ownership
  acceptance_checks:
  - Permanent ID and all inbound links survive any relocation.
  - Category matches documented fungal cultivation and maintained record validators
    pass.
limitations:
- 181 parent instances compared does not mean181 supported/corrected amounts; all
  parent amounts remain unchanged.
- Mattanovich batch conversions, sulfuric-acid density, generic preparation and dangling
  XLS text remain unresolved; no inferred growth metric.
- Jensen MgCl2 hydration and printed molybdate formula/hydration remain unresolved.
  Calcium-pantothenate wording is not converted into an invented calcium dose.
- No table2 solid-medium observations or table4 SA/M17 results are promoted to these
  liquid BL treatments. Other-strain taxonomy lookup was bounded.
- Merge verification was deliberately interrupted after1247 canonical-name conflicts
  and more than18 minutes; no completed current fingerprint/completeness result is
  claimed. Freshness has a separately retained result. No untouched whole-corpus baseline
  or publication is claimed.
- The related AMS1 exporter finding is not superseded or closed; its targets were
  not re-reviewed here.
- Source caches are ignored local archives, not committed publications. The full citation-exhaustion
  goal remains incomplete.
```
