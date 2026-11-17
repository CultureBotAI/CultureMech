# Emami 2015 citations and bounded algal study variants

- Review: 20261014T040628Z-algal-followup-citations
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-14T03:20:53Z
- Finished UTC: 2026-10-14T04:06:28Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Six citations from one archived paper; eight inline entries describe four bounded study variants. Six DOI/excerpt items support eight numeric amount claims, and two acid entries explicitly leave dose unquantified. All 63 pre-existing ingredients preserved; no new native growth association.

## Scope And Provenance

Six CCAP-derived AJS, JM and f/2 normalized owners; bibliography and bounded variant claims

Selection: Emami 2015 cultivation, time-course and antibiotic experiments with Table 1 identities
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000041 | data/normalized_yaml/algae/ajs.yaml | maintained | ajs |
| CultureMech:000338 | data/normalized_yaml/bacterial/ajs.yaml | maintained | ajs |
| CultureMech:000074 | data/normalized_yaml/algae/jm.yaml | maintained | jm |
| CultureMech:000350 | data/normalized_yaml/bacterial/jm.yaml | maintained | jm |
| CultureMech:000149 | data/normalized_yaml/algae/f_2.yaml | maintained | f_2 |
| CultureMech:000343 | data/normalized_yaml/bacterial/f_2.yaml | maintained | f_2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/algae/ajs.yaml | passed | True | CultureMech:000041 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/ajs.yaml | passed | True | CultureMech:000041 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/ajs.yaml | passed | True | CultureMech:000338 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/ajs.yaml | passed | True | CultureMech:000338 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/jm.yaml | passed | True | CultureMech:000074 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/jm.yaml | passed | True | CultureMech:000074 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/jm.yaml | passed | True | CultureMech:000350 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/jm.yaml | passed | True | CultureMech:000350 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/f_2.yaml | passed | True | CultureMech:000149 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/f_2.yaml | passed | True | CultureMech:000149 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/f_2.yaml | passed | True | CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/f_2.yaml | passed | True | CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/ajs.yaml | failed | True | CultureMech:000041 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/ajs.yaml | passed | True | CultureMech:000041 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/ajs.yaml | failed | True | CultureMech:000338 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/ajs.yaml | passed | True | CultureMech:000338 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/jm.yaml | passed | True | CultureMech:000074 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/jm.yaml | passed | True | CultureMech:000074 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/jm.yaml | passed | True | CultureMech:000350 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/jm.yaml | passed | True | CultureMech:000350 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/f_2.yaml | failed | True | CultureMech:000149 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/f_2.yaml | passed | True | CultureMech:000149 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/f_2.yaml | failed | True | CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/f_2.yaml | passed | True | CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| just verify-merges | failed | True | CultureMech:000041, CultureMech:000338, CultureMech:000074, CultureMech:000350, CultureMech:000149, CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| just audit-merge-freshness | failed | True | CultureMech:000041, CultureMech:000338, CultureMech:000074, CultureMech:000350, CultureMech:000149, CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:000041, CultureMech:000338, CultureMech:000074, CultureMech:000350, CultureMech:000149, CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| git diff --check | passed | True | CultureMech:000041, CultureMech:000338, CultureMech:000074, CultureMech:000350, CultureMech:000149, CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-algal-followup-citations/curate.py --apply | passed | True | CultureMech:000041, CultureMech:000338, CultureMech:000074, CultureMech:000350, CultureMech:000149, CultureMech:000343 | Actual check outcome; failures retained without waiver. |
| just test-fast | passed | True | CultureMech:000041, CultureMech:000338, CultureMech:000074, CultureMech:000350, CultureMech:000149, CultureMech:000343 | Actual check outcome; failures retained without waiver. |

## Scientific And Domain Assessments

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000041.

One paper citation with verified title, eight authors, 2015 year, DOI/PMID, raw XML and Markdown.

### Study variants and unresolved full formula

evidence: unknown. Targets: CultureMech:000041.

HCl instead of the CCAP H2SO4 instruction; pH 1.5 is explicit but HCl dose is unquantified. Complete base formula, stock encoding and physical-state equivalence remain unresolved; parent fields unchanged.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000041.

Dunaliella acidophila CCAP 19/35. Verified name/rank and qualified strain mapping retained in notes; no positive native growth assertion.

### Existing claims and file presentation

evidence: supported. Targets: CultureMech:000041.

All 1 ingredients and pre-existing fields preserved. Reversing additions recovers original bytes; one history event; no-op replay changes nothing.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000041.

status=not_quantified; field=variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0]; old=absent study-variant entry; new=Use hydrochloric acid for the reported adjustment to pH 1.5, rather than inheriting the canonical sulfuric-acid instruction. HCl strength and dose are not quantified; no dose or substitution arithmetic is inferred.

Reference: doi:10.1038/srep10036. Exact snippet: Dunaliella acidophila was grown in AJS medium that was acidified to pH 1.5 using hydrochloric acid. Locator and scope: Supports only variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0]. Locator: Methods / Microalgae and cyanobacteria strains and culture conditions. Reported scientific name=Dunaliella acidophila; strain=CCAP 19/35; canonical scientific name=Dunaliella acidophila; NCBITaxon:38272; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=38272; scope=AJS acidified with hydrochloric acid. The paper reports the acid and pH but not its concentration or volume: concentration_decision=not_quantified. The inspected CCAP AJS PDF page 1 instead specifies concentrated H2SO4. This is a study difference, not a correction of the parent. No conversion. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000338.

One paper citation with verified title, eight authors, 2015 year, DOI/PMID, raw XML and Markdown.

### Study variants and unresolved full formula

evidence: unknown. Targets: CultureMech:000338.

HCl instead of the CCAP H2SO4 instruction; pH 1.5 is explicit but HCl dose is unquantified. Complete base formula, stock encoding and physical-state equivalence remain unresolved; parent fields unchanged.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000338.

Dunaliella acidophila CCAP 19/35. Verified name/rank and qualified strain mapping retained in notes; no positive native growth assertion.

### Existing claims and file presentation

evidence: supported. Targets: CultureMech:000338.

All 16 ingredients and pre-existing fields preserved. Reversing additions recovers original bytes; one history event; no-op replay changes nothing.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000338.

status=not_quantified; field=variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0]; old=absent study-variant entry; new=Use hydrochloric acid for the reported adjustment to pH 1.5, rather than inheriting the canonical sulfuric-acid instruction. HCl strength and dose are not quantified; no dose or substitution arithmetic is inferred.

Reference: doi:10.1038/srep10036. Exact snippet: Dunaliella acidophila was grown in AJS medium that was acidified to pH 1.5 using hydrochloric acid. Locator and scope: Supports only variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0]. Locator: Methods / Microalgae and cyanobacteria strains and culture conditions. Reported scientific name=Dunaliella acidophila; strain=CCAP 19/35; canonical scientific name=Dunaliella acidophila; NCBITaxon:38272; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=38272; scope=AJS acidified with hydrochloric acid. The paper reports the acid and pH but not its concentration or volume: concentration_decision=not_quantified. The inspected CCAP AJS PDF page 1 instead specifies concentrated H2SO4. This is a study difference, not a correction of the parent. No conversion. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000074.

One paper citation with verified title, eight authors, 2015 year, DOI/PMID, raw XML and Markdown.

### Study variants and unresolved full formula

evidence: unknown. Targets: CultureMech:000074.

Study uses Jaworski medium with deionized water; no supported ingredient difference for a new variant. Complete base formula, stock encoding and physical-state equivalence remain unresolved; parent fields unchanged.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000074.

Chlorella vulgaris CCAP 211/63. Verified name/rank and qualified strain mapping retained in notes; no positive native growth assertion.

### Existing claims and file presentation

evidence: supported. Targets: CultureMech:000074.

All 4 ingredients and pre-existing fields preserved. Reversing additions recovers original bytes; one history event; no-op replay changes nothing.

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000350.

One paper citation with verified title, eight authors, 2015 year, DOI/PMID, raw XML and Markdown.

### Study variants and unresolved full formula

evidence: unknown. Targets: CultureMech:000350.

Study uses Jaworski medium with deionized water; no supported ingredient difference for a new variant. Complete base formula, stock encoding and physical-state equivalence remain unresolved; parent fields unchanged.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000350.

Chlorella vulgaris CCAP 211/63. Verified name/rank and qualified strain mapping retained in notes; no positive native growth assertion.

### Existing claims and file presentation

evidence: supported. Targets: CultureMech:000350.

All 15 ingredients and pre-existing fields preserved. Reversing additions recovers original bytes; one history event; no-op replay changes nothing.

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000149.

One paper citation with verified title, eight authors, 2015 year, DOI/PMID, raw XML and Markdown.

### Study variants and unresolved full formula

evidence: unknown. Targets: CultureMech:000149.

Silicate, nitrate and antibiotic contexts are separate; unresolved double strength is not equated to Quad. Complete base formula, stock encoding and physical-state equivalence remain unresolved; parent fields unchanged.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000149.

34 f/2-relevant rows, with two other-medium organisms explicitly excluded. Verified name/rank and qualified strain mapping retained in notes; no positive native growth assertion.

### Existing claims and file presentation

evidence: supported. Targets: CultureMech:000149.

All 13 ingredients and pre-existing fields preserved. Reversing additions recovers original bytes; one history event; no-op replay changes nothing.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000149.

status=add; field=variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0]; old=absent study-variant entry; new=The study reports f/2 supplemented with 1.06e-4 M silicate. Preserve this stated supplementation concentration without assigning an unreported silicate salt, hydrate, stock recipe or additional mass conversion.

Reference: doi:10.1038/srep10036. Exact snippet: Isochrysis galbana was cultured using f/2 supplemented with 1.06 × 10−4 M silicate Locator and scope: Supports only variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0]. Locator: Methods / Microalgae and cyanobacteria strains and culture conditions. Reported scientific name=Isochrysis galbana; strain=CCAP 927/1; canonical scientific name=Isochrysis galbana; NCBITaxon:37099; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=37099; scope=silicate-supplemented f/2. Directly stated supplement value in the study medium, not a stock concentration or calculated total including background. No calculation. Local f/2 + Si owners specify sodium silicate nonahydrate and differently encoded stock amounts; the paper does not establish exact equivalence. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000149.

status=add; field=variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0]; old=absent study-variant entry; new=The study reports f/2 supplemented with 29.4 mM NaNO3 and adjusted to pH 8. Retain the stated supplement concentration; do not infer whether it includes the base-medium nitrate or calculate a total nitrate concentration.

Reference: doi:10.1038/srep10036. Exact snippet: A. platensis was cultured using f/2 supplemented with 29.4 mM NaNO3 and adjusted to pH 8. Locator and scope: Supports only variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0]. Locator: Methods / Microalgae and cyanobacteria strains and culture conditions. Reported scientific name=Arthrospira platensis; strain=CCMP 1295; canonical scientific name=Limnospira platensis; NCBITaxon:118562; actual rank=species; taxonomy_match=verified_synonym_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=118562; scope=nitrate-supplemented f/2 at pH 8. Directly reported supplementation value and study pH, not a stock quantity or a universal optimum. No arithmetic; base-plus-supplement total remains unresolved. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000149.

status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0]; old=absent study-variant entry; new=Reported penicillin G treatment concentration: 200 micrograms per mL in the treated f/2 culture; no unreported salt form, stock strength or conversion is assigned.

Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1. Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2]. Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial interference experiment, not an unresolved maintenance-strength assignment. The two directly stated culture-treatment amounts share this exact excerpt; no arithmetic. Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella on that agar. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000149.

status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[1]; old=absent study-variant entry; new=Reported dihydrostreptomycin sulphate treatment concentration: 50 micrograms per mL in the same treated culture; not streptomycin, not a stock concentration, and no hydrate assumption.

Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1. Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2]. Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial interference experiment, not an unresolved maintenance-strength assignment. The two directly stated culture-treatment amounts share this exact excerpt; no arithmetic. Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella on that agar. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000343.

One paper citation with verified title, eight authors, 2015 year, DOI/PMID, raw XML and Markdown.

### Study variants and unresolved full formula

evidence: unknown. Targets: CultureMech:000343.

Silicate, nitrate and antibiotic contexts are separate; unresolved double strength is not equated to Quad. Complete base formula, stock encoding and physical-state equivalence remain unresolved; parent fields unchanged.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000343.

34 f/2-relevant rows, with two other-medium organisms explicitly excluded. Verified name/rank and qualified strain mapping retained in notes; no positive native growth assertion.

### Existing claims and file presentation

evidence: supported. Targets: CultureMech:000343.

All 14 ingredients and pre-existing fields preserved. Reversing additions recovers original bytes; one history event; no-op replay changes nothing.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000343.

status=add; field=variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0]; old=absent study-variant entry; new=The study reports f/2 supplemented with 1.06e-4 M silicate. Preserve this stated supplementation concentration without assigning an unreported silicate salt, hydrate, stock recipe or additional mass conversion.

Reference: doi:10.1038/srep10036. Exact snippet: Isochrysis galbana was cultured using f/2 supplemented with 1.06 × 10−4 M silicate Locator and scope: Supports only variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0]. Locator: Methods / Microalgae and cyanobacteria strains and culture conditions. Reported scientific name=Isochrysis galbana; strain=CCAP 927/1; canonical scientific name=Isochrysis galbana; NCBITaxon:37099; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=37099; scope=silicate-supplemented f/2. Directly stated supplement value in the study medium, not a stock concentration or calculated total including background. No calculation. Local f/2 + Si owners specify sodium silicate nonahydrate and differently encoded stock amounts; the paper does not establish exact equivalence. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000343.

status=add; field=variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0]; old=absent study-variant entry; new=The study reports f/2 supplemented with 29.4 mM NaNO3 and adjusted to pH 8. Retain the stated supplement concentration; do not infer whether it includes the base-medium nitrate or calculate a total nitrate concentration.

Reference: doi:10.1038/srep10036. Exact snippet: A. platensis was cultured using f/2 supplemented with 29.4 mM NaNO3 and adjusted to pH 8. Locator and scope: Supports only variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0]. Locator: Methods / Microalgae and cyanobacteria strains and culture conditions. Reported scientific name=Arthrospira platensis; strain=CCMP 1295; canonical scientific name=Limnospira platensis; NCBITaxon:118562; actual rank=species; taxonomy_match=verified_synonym_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=118562; scope=nitrate-supplemented f/2 at pH 8. Directly reported supplementation value and study pH, not a stock quantity or a universal optimum. No arithmetic; base-plus-supplement total remains unresolved. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000343.

status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0]; old=absent study-variant entry; new=Reported penicillin G treatment concentration: 200 micrograms per mL in the treated f/2 culture; no unreported salt form, stock strength or conversion is assigned.

Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1. Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2]. Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial interference experiment, not an unresolved maintenance-strength assignment. The two directly stated culture-treatment amounts share this exact excerpt; no arithmetic. Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella on that agar. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

### Inline study-variant concentration decision

evidence: supported. Targets: CultureMech:000343.

status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[1]; old=absent study-variant entry; new=Reported dihydrostreptomycin sulphate treatment concentration: 50 micrograms per mL in the same treated culture; not streptomycin, not a stock concentration, and no hydrate assumption.

Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1. Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2]. Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903; scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial interference experiment, not an unresolved maintenance-strength assignment. The two directly stated culture-treatment amounts share this exact excerpt; no arithmetic. Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella on that agar. Calculation: none. Parent amounts unchanged; complete formulation unresolved.

## Findings

### merge-gates: Repository merge gates failed

major / open / confirmed; issue key: algal-followup-citations-merge-gates.

Failures retained without assuming equal aggregate counts prove unchanged rows or attributing all failures to this batch. No generated publication.

### reference-checks: Full-text excerpts are unavailable to the automatic reference fetch

minor / open / confirmed; issue key: algal-followup-citations-reference-checks.

All baseline commands passed. Four post-edit aggregate validations fail on eight new variant excerpts because the automatic DOI fetch has only the abstract. Primary JATS and derived Markdown contain each exact methods excerpt. Schema, term and strict checks pass. These are newly exposed failures, not baseline failures or waived checks.

### formulation-and-scope: Full formulas and native growth scope remain unresolved

informational / open / confirmed; issue key: algal-followup-citations-formulation-and-scope.

The paper does not restate complete formulas. Current source recipes and flattened imports cannot establish historical stock amounts or solid/liquid equivalence. General maintenance strength is unassigned per strain. Name-level taxonomy is not strain reidentification. The exporter does not honor inline variant growth scope.

## Recommended Actions And Acceptance Checks

### resolve-merge-gates

Repository merge gates failed

- Diagnose maintained merge inputs and rules, then pass both gates before publication.

### resolve-reference-checks

Full-text excerpts are unavailable to the automatic reference fetch

- Make verified full text available through the maintained reference resolver; preserve correct source quotations and rerun reference validation.

### resolve-formulation-and-scope

Full formulas and native growth scope remain unresolved

- Resolve full study formulation, source-owner and organism/strain scope before adding or exporting positive native growth assertions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| baseline-00 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-00.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-00.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-01 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-01.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-01.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-02 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-02.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-02.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-03 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-03.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-03.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-04 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-04.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-04.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-05 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-05.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-05.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-06 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-06.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-06.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-07 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-07.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-07.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-08 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-08.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-08.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-09 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-09.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-09.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-10 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-10.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-10.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-11 | reports/paper_citation_curation/20261014-algal-followup-citations/baseline-11.log; reports/paper_citation_curation/20261014-algal-followup-citations/baseline-11.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-00 | reports/paper_citation_curation/20261014-algal-followup-citations/post-00.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-00.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| post-01 | reports/paper_citation_curation/20261014-algal-followup-citations/post-01.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-01.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-02 | reports/paper_citation_curation/20261014-algal-followup-citations/post-02.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-02.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| post-03 | reports/paper_citation_curation/20261014-algal-followup-citations/post-03.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-03.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-04 | reports/paper_citation_curation/20261014-algal-followup-citations/post-04.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-04.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-05 | reports/paper_citation_curation/20261014-algal-followup-citations/post-05.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-05.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-06 | reports/paper_citation_curation/20261014-algal-followup-citations/post-06.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-06.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-07 | reports/paper_citation_curation/20261014-algal-followup-citations/post-07.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-07.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-08 | reports/paper_citation_curation/20261014-algal-followup-citations/post-08.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-08.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| post-09 | reports/paper_citation_curation/20261014-algal-followup-citations/post-09.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-09.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-10 | reports/paper_citation_curation/20261014-algal-followup-citations/post-10.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-10.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| post-11 | reports/paper_citation_curation/20261014-algal-followup-citations/post-11.log; reports/paper_citation_curation/20261014-algal-followup-citations/post-11.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| merge-00 | reports/paper_citation_curation/20261014-algal-followup-citations/merge-00.log; reports/paper_citation_curation/20261014-algal-followup-citations/merge-00.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| merge-01 | reports/paper_citation_curation/20261014-algal-followup-citations/merge-01.log; reports/paper_citation_curation/20261014-algal-followup-citations/merge-01.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| extra-00 | reports/paper_citation_curation/20261014-algal-followup-citations/extra-00.log; reports/paper_citation_curation/20261014-algal-followup-citations/extra-00.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| extra-01 | reports/paper_citation_curation/20261014-algal-followup-citations/extra-01.log; reports/paper_citation_curation/20261014-algal-followup-citations/extra-01.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| extra-02 | reports/paper_citation_curation/20261014-algal-followup-citations/extra-02.log; reports/paper_citation_curation/20261014-algal-followup-citations/extra-02.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| fast-00 | reports/paper_citation_curation/20261014-algal-followup-citations/fast-test.log; reports/paper_citation_curation/20261014-algal-followup-citations/fast-test.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| paper | doi:10.1038/srep10036; references_cache/papers/primary_xml/ccap-19-18-PMC4650328-20261014.xml; Full primary JATS with Table 1 and separate cultivation/assay methods | supports | Publication identity, Table 1 and separate cultivation/assay passages inspected; bounded claims only. |
| pubmed | PMID:25963242; references_cache/papers/PMID_25963242.xml; Title, eight authors, year, identifiers and notices | supports | Publication metadata agrees with primary JATS; archived notice list is empty, not an exhaustive notice search. |
| taxonomy | NCBI Taxonomy; references_cache/papers/taxonomy/emami-2015-20261014.xml; Scientific names, actual ranks, synonyms and included strain labels | supports | Thirty-six organism/strain rows use 21 verified nodes; name matching is not independent reidentification. |
| strain-taxonomy | NCBI Taxonomy; references_cache/papers/taxonomy/emami-2015-strains-20261014.xml; Scientific names, actual ranks, synonyms and included strain labels | supports | Thirty-six organism/strain rows use 21 verified nodes; name matching is not independent reidentification. |
| ccap-ajs | Current CCAP recipe; references_cache/papers/primary_pdf/ccap-ajs-algal-followup-20261014.pdf; Page 1 visually inspected; quantities distinguish stocks and final additions | context_only | Present-day recipe is a source comparison, not proof of every 2015 study ingredient. |
| ccap-jm | Current CCAP recipe; references_cache/papers/primary_pdf/ccap-jm-algal-followup-20261014.pdf; Page 1 visually inspected; quantities distinguish stocks and final additions | context_only | Present-day recipe is a source comparison, not proof of every 2015 study ingredient. |
| ccap-f2 | Current CCAP recipe; references_cache/papers/primary_pdf/ccap-f2-algal-followup-20261014.pdf; Page 1 visually inspected; quantities distinguish stocks and final additions | context_only | Present-day recipe is a source comparison, not proof of every 2015 study ingredient. |
| exporter | Current KGX implementation; src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge | context_only | Positive edges use the parent ID and do not honor scoped_to_variant; no new native growth assertions added. |
| claims | Guarded curation receipt; reports/paper_citation_curation/20261014-algal-followup-citations/claim-plan-v2.json; claim-plan-v2.json | context_only | Applied scope, exact excerpts, preservation checks and unfinished discovery. |
| readback | Guarded curation receipt; reports/paper_citation_curation/20261014-algal-followup-citations/final-readback.json; final-readback.json | context_only | Applied scope, exact excerpts, preservation checks and unfinished discovery. |
| excerpts | Guarded curation receipt; reports/paper_citation_curation/20261014-algal-followup-citations/evidence-readback.json; evidence-readback.json | context_only | Applied scope, exact excerpts, preservation checks and unfinished discovery. |
| pending | Guarded curation receipt; reports/paper_citation_curation/20261014-algal-followup-citations/pending-frontier.json; pending-frontier.json | context_only | Applied scope, exact excerpts, preservation checks and unfinished discovery. |

## Limits And Additional Notes

- Focused self-review, not independent adversarial or complete scientific review.
- Thirty-six medium-relevant organism/strain rows, not every organism in the full paper or analytical calibration.
- Complete historical formulas, unspecified stock/chemical forms, nitrate total and silicate salt remain unresolved.
- Current species-rank matches, including unclassified strain labels, do not independently reidentify the experimental cultures.
- No new native positive growth assertion, canonical amount change, record merge, export, or GitHub mutation.
- Reference and global merge gate failures remain open; corpus-wide citation discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T040628Z-algal-followup-citations
kind: batch
repository: culturebotai/CultureMech
title: Emami 2015 citations and bounded algal study variants
started_at: '2026-10-14T03:20:53Z'
finished_at: '2026-10-14T04:06:28Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Curator-performed focused assessment, not independent review.
skill: culturemech-add-paper-citation; review-ingredient-concentrations
completion: partial
verdict: needs_curation
scientific_review: false
summary: Six citations from one archived paper; eight inline entries describe four
  bounded study variants. Six DOI/excerpt items support eight numeric amount claims,
  and two acid entries explicitly leave dose unquantified. All 63 pre-existing ingredients
  preserved; no new native growth association.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/algae/ajs.yaml
    sha256: 6a96f45eba5e91e591a4f9160c43422b561ed8c281d07ecaa9901550feabb2ba
    role: target
  - path: data/normalized_yaml/algae/f_2.yaml
    sha256: d26f89b16d5f29891fa768338f944ccf9faae842aaa90f312c179fe1a0ba69c9
    role: target
  - path: data/normalized_yaml/algae/jm.yaml
    sha256: e5b2c6558f8f000b9f669ec7c1622add5fcb07bd8cb1f5a48deb9969fc435e84
    role: target
  - path: data/normalized_yaml/bacterial/ajs.yaml
    sha256: 3c5158c29f2130e01452d8f7a0428863db898c6a32b10b20d14a0f8c9881c4c6
    role: target
  - path: data/normalized_yaml/bacterial/f_2.yaml
    sha256: 7fbdf890cb835a4156614f731c3709d7922bd26153dd9f6b572130557af984f9
    role: target
  - path: data/normalized_yaml/bacterial/jm.yaml
    sha256: 2720b2117d6585e6de46346cb913b430a083a82a56da961353bde985979bb5c1
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Six CCAP-derived AJS, JM and f/2 normalized owners; bibliography and
    bounded variant claims
  selection: Emami 2015 cultivation, time-course and antibiotic experiments with Table
    1 identities
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  exclusions:
  - target: Existing recipe amounts, growth claims and full-record certification
    reason: Preserved without new scientific approval; not a canonical concentration
      audit.
  - target: Other records and all possible citations
    reason: Separate active discovery queue, not an exhaustion claim.
targets:
- target_id: CultureMech:000041
  path: data/normalized_yaml/algae/ajs.yaml
  label: ajs
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000338
  path: data/normalized_yaml/bacterial/ajs.yaml
  label: ajs
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000074
  path: data/normalized_yaml/algae/jm.yaml
  label: jm
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/jm.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000350
  path: data/normalized_yaml/bacterial/jm.yaml
  label: jm
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/jm.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000149
  path: data/normalized_yaml/algae/f_2.yaml
  label: f_2
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000343
  path: data/normalized_yaml/bacterial/f_2.yaml
  label: f_2
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-00
  name: just validate data/normalized_yaml/algae/ajs.yaml
  command: just validate data/normalized_yaml/algae/ajs.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - baseline-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-01
  name: just validate-strict data/normalized_yaml/algae/ajs.yaml
  command: just validate-strict data/normalized_yaml/algae/ajs.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - baseline-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-02
  name: just validate data/normalized_yaml/bacterial/ajs.yaml
  command: just validate data/normalized_yaml/bacterial/ajs.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - baseline-02
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-03
  name: just validate-strict data/normalized_yaml/bacterial/ajs.yaml
  command: just validate-strict data/normalized_yaml/bacterial/ajs.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - baseline-03
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-04
  name: just validate data/normalized_yaml/algae/jm.yaml
  command: just validate data/normalized_yaml/algae/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - baseline-04
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-05
  name: just validate-strict data/normalized_yaml/algae/jm.yaml
  command: just validate-strict data/normalized_yaml/algae/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - baseline-05
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-06
  name: just validate data/normalized_yaml/bacterial/jm.yaml
  command: just validate data/normalized_yaml/bacterial/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - baseline-06
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-07
  name: just validate-strict data/normalized_yaml/bacterial/jm.yaml
  command: just validate-strict data/normalized_yaml/bacterial/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - baseline-07
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-08
  name: just validate data/normalized_yaml/algae/f_2.yaml
  command: just validate data/normalized_yaml/algae/f_2.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - baseline-08
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-09
  name: just validate-strict data/normalized_yaml/algae/f_2.yaml
  command: just validate-strict data/normalized_yaml/algae/f_2.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - baseline-09
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-10
  name: just validate data/normalized_yaml/bacterial/f_2.yaml
  command: just validate data/normalized_yaml/bacterial/f_2.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - baseline-10
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-11
  name: just validate-strict data/normalized_yaml/bacterial/f_2.yaml
  command: just validate-strict data/normalized_yaml/bacterial/f_2.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - baseline-11
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-00
  name: just validate data/normalized_yaml/algae/ajs.yaml
  command: just validate data/normalized_yaml/algae/ajs.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - post-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-01
  name: just validate-strict data/normalized_yaml/algae/ajs.yaml
  command: just validate-strict data/normalized_yaml/algae/ajs.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - post-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-02
  name: just validate data/normalized_yaml/bacterial/ajs.yaml
  command: just validate data/normalized_yaml/bacterial/ajs.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - post-02
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-03
  name: just validate-strict data/normalized_yaml/bacterial/ajs.yaml
  command: just validate-strict data/normalized_yaml/bacterial/ajs.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - post-03
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-04
  name: just validate data/normalized_yaml/algae/jm.yaml
  command: just validate data/normalized_yaml/algae/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - post-04
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-05
  name: just validate-strict data/normalized_yaml/algae/jm.yaml
  command: just validate-strict data/normalized_yaml/algae/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - post-05
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-06
  name: just validate data/normalized_yaml/bacterial/jm.yaml
  command: just validate data/normalized_yaml/bacterial/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - post-06
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-07
  name: just validate-strict data/normalized_yaml/bacterial/jm.yaml
  command: just validate-strict data/normalized_yaml/bacterial/jm.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - post-07
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-08
  name: just validate data/normalized_yaml/algae/f_2.yaml
  command: just validate data/normalized_yaml/algae/f_2.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - post-08
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-09
  name: just validate-strict data/normalized_yaml/algae/f_2.yaml
  command: just validate-strict data/normalized_yaml/algae/f_2.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - post-09
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-10
  name: just validate data/normalized_yaml/bacterial/f_2.yaml
  command: just validate data/normalized_yaml/bacterial/f_2.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - post-10
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-11
  name: just validate-strict data/normalized_yaml/bacterial/f_2.yaml
  command: just validate-strict data/normalized_yaml/bacterial/f_2.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - post-11
  summary: Actual check outcome; failures retained without waiver.
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - merge-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: merge-01
  name: just audit-merge-freshness
  command: just audit-merge-freshness
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - merge-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - extra-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: extra-01
  name: git diff --check
  command: git diff --check
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - extra-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: extra-02
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-algal-followup-citations/curate.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-algal-followup-citations/curate.py
    --apply
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - extra-02
  summary: Actual check outcome; failures retained without waiver.
- check_id: fast-00
  name: just test-fast
  command: just test-fast
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - fast-00
  summary: Actual check outcome; failures retained without waiver.
evidence:
- evidence_id: baseline-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-00.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-01.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-02.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-02.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-03.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-03.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-04
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-04.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-04.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-05
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-05.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-05.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-06
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-06.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-06.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-07
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-07.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-07.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-08
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-08.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-08.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-09
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-09.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-09.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-10
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-10.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-10.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-11
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-11.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/baseline-11.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-00.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 8e12be514d2e3646658ef32b3ede66e52db8a0b6559d82669e30ebaaa4bd23d5
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-01.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-02.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-02.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 8e12be514d2e3646658ef32b3ede66e52db8a0b6559d82669e30ebaaa4bd23d5
- evidence_id: post-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-03.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-03.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-04
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-04.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-04.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: post-05
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-05.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-05.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-06
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-06.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-06.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: post-07
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-07.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-07.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-08
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-08.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-08.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: f6f8d0775221692535ed9ead5f097a81837c6c1e218e9d9e546f1a6059a0ef40
- evidence_id: post-09
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-09.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-09.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-10
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-10.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-10.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: f6f8d0775221692535ed9ead5f097a81837c6c1e218e9d9e546f1a6059a0ef40
- evidence_id: post-11
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/post-11.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/post-11.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/merge-00.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/merge-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/merge-01.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/merge-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: db0b7b54fe69800bb252f0f5a14838bde836302b3118f3c97409b72248cc205d
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/extra-00.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/extra-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/extra-01.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/extra-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/extra-02.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/extra-02.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: f4d811a0b10f3cf775ee60a06d8e3512639766975de6ac17259e6bc02ccd5cd0
- evidence_id: fast-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-algal-followup-citations/fast-test.log
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/fast-test.log;
    Complete terminal output
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 29689f951a4c00f1a9a3da9899338d9efa54b1bc8e92371547471f0a1a05c5f1
- evidence_id: paper
  kind: primary_source
  reference: doi:10.1038/srep10036
  locator: references_cache/papers/primary_xml/ccap-19-18-PMC4650328-20261014.xml;
    Full primary JATS with Table 1 and separate cultivation/assay methods
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Publication identity, Table 1 and separate cultivation/assay passages inspected;
    bounded claims only.
  support: supports
  snapshot_sha256: 7e3ddf65f336955a2c875b18361e878ffcf16bc341fe9b404308d014df4c3319
- evidence_id: pubmed
  kind: authority
  reference: PMID:25963242
  locator: references_cache/papers/PMID_25963242.xml; Title, eight authors, year,
    identifiers and notices
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Publication metadata agrees with primary JATS; archived notice list is
    empty, not an exhaustive notice search.
  support: supports
  snapshot_sha256: b579567685f772aad96ee3f49e946c6f3acfb5b038158f5be442e1114ab8275f
- evidence_id: taxonomy
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/emami-2015-20261014.xml; Scientific names,
    actual ranks, synonyms and included strain labels
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Thirty-six organism/strain rows use 21 verified nodes; name matching is
    not independent reidentification.
  support: supports
  snapshot_sha256: d5b46402f19e9e8bbf8d954acc1d506d0aec9b763cc44533d740bf691146c017
- evidence_id: strain-taxonomy
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/emami-2015-strains-20261014.xml; Scientific
    names, actual ranks, synonyms and included strain labels
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Thirty-six organism/strain rows use 21 verified nodes; name matching is
    not independent reidentification.
  support: supports
  snapshot_sha256: 59c27f65c8add1a9dd0f8620b893fd42a3b8ef04d33a32711c65405d006e38d5
- evidence_id: ccap-ajs
  kind: primary_source
  reference: Current CCAP recipe
  locator: references_cache/papers/primary_pdf/ccap-ajs-algal-followup-20261014.pdf;
    Page 1 visually inspected; quantities distinguish stocks and final additions
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Present-day recipe is a source comparison, not proof of every 2015 study
    ingredient.
  support: context_only
  snapshot_sha256: ceee3a6c3b8693f5fee386aae0d30b1541d8f753e44c9c068701d049621977ca
- evidence_id: ccap-jm
  kind: primary_source
  reference: Current CCAP recipe
  locator: references_cache/papers/primary_pdf/ccap-jm-algal-followup-20261014.pdf;
    Page 1 visually inspected; quantities distinguish stocks and final additions
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Present-day recipe is a source comparison, not proof of every 2015 study
    ingredient.
  support: context_only
  snapshot_sha256: a7fe2b43a517e0a110d11b08f52ef8447ab6f254c0bbb4eeea42a58e8981e53e
- evidence_id: ccap-f2
  kind: primary_source
  reference: Current CCAP recipe
  locator: references_cache/papers/primary_pdf/ccap-f2-algal-followup-20261014.pdf;
    Page 1 visually inspected; quantities distinguish stocks and final additions
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Present-day recipe is a source comparison, not proof of every 2015 study
    ingredient.
  support: context_only
  snapshot_sha256: a3f1d24bf0341a6ee2045af8929616467bd594f8dffd7ae8bd7ea42de515324c
- evidence_id: exporter
  kind: record_content
  reference: Current KGX implementation
  locator: src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Positive edges use the parent ID and do not honor scoped_to_variant; no
    new native growth assertions added.
  support: context_only
  snapshot_sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
- evidence_id: claims
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/claim-plan-v2.json;
    claim-plan-v2.json
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Applied scope, exact excerpts, preservation checks and unfinished discovery.
  support: context_only
  snapshot_sha256: b5cf43a5da8926b0500759b05bf6249315a8e19f4f7c7251077f8bb30edd24bb
- evidence_id: readback
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/final-readback.json;
    final-readback.json
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Applied scope, exact excerpts, preservation checks and unfinished discovery.
  support: context_only
  snapshot_sha256: e71ad0be4bdbc31e3bfbfcc4e4a35b750c2389119c756e3cfae6836bf7cbf29e
- evidence_id: excerpts
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/evidence-readback.json;
    evidence-readback.json
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Applied scope, exact excerpts, preservation checks and unfinished discovery.
  support: context_only
  snapshot_sha256: 1f4a18d6ff8d348d723507e116caa0a7e74099e79f1d128dc15c5ff15223c29e
- evidence_id: pending
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-algal-followup-citations/pending-frontier.json;
    pending-frontier.json
  accessed_at: '2026-10-14T04:06:28Z'
  summary: Applied scope, exact excerpts, preservation checks and unfinished discovery.
  support: context_only
  snapshot_sha256: 2f4097df4b49475d0848819ed793cf7671896d79ba98cdb8c8e72e46d4a9b96d
assessments:
- assessment_id: identity-000041
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - paper
  - pubmed
  - claims
  summary: One paper citation with verified title, eight authors, 2015 year, DOI/PMID,
    raw XML and Markdown.
- assessment_id: formulation-000041
  area: evidence
  topic: Study variants and unresolved full formula
  outcome: unknown
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - paper
  - ccap-ajs
  - claims
  summary: HCl instead of the CCAP H2SO4 instruction; pH 1.5 is explicit but HCl dose
    is unquantified. Complete base formula, stock encoding and physical-state equivalence
    remain unresolved; parent fields unchanged.
- assessment_id: taxonomy-000041
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - paper
  - taxonomy
  - strain-taxonomy
  - excerpts
  - exporter
  summary: Dunaliella acidophila CCAP 19/35. Verified name/rank and qualified strain
    mapping retained in notes; no positive native growth assertion.
- assessment_id: preservation-000041
  area: evidence
  topic: Existing claims and file presentation
  outcome: supported
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - readback
  - extra-02
  summary: All 1 ingredients and pre-existing fields preserved. Reversing additions
    recovers original bytes; one history event; no-op replay changes nothing.
- assessment_id: variant-amount-000041-0-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000041
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: status=not_quantified; field=variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0];
    old=absent study-variant entry; new=Use hydrochloric acid for the reported adjustment
    to pH 1.5, rather than inheriting the canonical sulfuric-acid instruction. HCl
    strength and dose are not quantified; no dose or substitution arithmetic is inferred.
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: Dunaliella acidophila
    was grown in AJS medium that was acidified to pH 1.5 using hydrochloric acid.
    Locator and scope: Supports only variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0].
    Locator: Methods / Microalgae and cyanobacteria strains and culture conditions.
    Reported scientific name=Dunaliella acidophila; strain=CCAP 19/35; canonical scientific
    name=Dunaliella acidophila; NCBITaxon:38272; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=38272;
    scope=AJS acidified with hydrochloric acid. The paper reports the acid and pH
    but not its concentration or volume: concentration_decision=not_quantified. The
    inspected CCAP AJS PDF page 1 instead specifies concentrated H2SO4. This is a
    study difference, not a correction of the parent. No conversion. Calculation:
    none. Parent amounts unchanged; complete formulation unresolved.'
  dimensions:
  - name: concentration_decision
    value: not_quantified
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: identity-000338
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - paper
  - pubmed
  - claims
  summary: One paper citation with verified title, eight authors, 2015 year, DOI/PMID,
    raw XML and Markdown.
- assessment_id: formulation-000338
  area: evidence
  topic: Study variants and unresolved full formula
  outcome: unknown
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - paper
  - ccap-ajs
  - claims
  summary: HCl instead of the CCAP H2SO4 instruction; pH 1.5 is explicit but HCl dose
    is unquantified. Complete base formula, stock encoding and physical-state equivalence
    remain unresolved; parent fields unchanged.
- assessment_id: taxonomy-000338
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - paper
  - taxonomy
  - strain-taxonomy
  - excerpts
  - exporter
  summary: Dunaliella acidophila CCAP 19/35. Verified name/rank and qualified strain
    mapping retained in notes; no positive native growth assertion.
- assessment_id: preservation-000338
  area: evidence
  topic: Existing claims and file presentation
  outcome: supported
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - readback
  - extra-02
  summary: All 16 ingredients and pre-existing fields preserved. Reversing additions
    recovers original bytes; one history event; no-op replay changes nothing.
- assessment_id: variant-amount-000338-0-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000338
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: status=not_quantified; field=variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0];
    old=absent study-variant entry; new=Use hydrochloric acid for the reported adjustment
    to pH 1.5, rather than inheriting the canonical sulfuric-acid instruction. HCl
    strength and dose are not quantified; no dose or substitution arithmetic is inferred.
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: Dunaliella acidophila
    was grown in AJS medium that was acidified to pH 1.5 using hydrochloric acid.
    Locator and scope: Supports only variants[name=ajs_hydrochloric_acid_ph_1_5].modifications[0].
    Locator: Methods / Microalgae and cyanobacteria strains and culture conditions.
    Reported scientific name=Dunaliella acidophila; strain=CCAP 19/35; canonical scientific
    name=Dunaliella acidophila; NCBITaxon:38272; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=38272;
    scope=AJS acidified with hydrochloric acid. The paper reports the acid and pH
    but not its concentration or volume: concentration_decision=not_quantified. The
    inspected CCAP AJS PDF page 1 instead specifies concentrated H2SO4. This is a
    study difference, not a correction of the parent. No conversion. Calculation:
    none. Parent amounts unchanged; complete formulation unresolved.'
  dimensions:
  - name: concentration_decision
    value: not_quantified
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: identity-000074
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - paper
  - pubmed
  - claims
  summary: One paper citation with verified title, eight authors, 2015 year, DOI/PMID,
    raw XML and Markdown.
- assessment_id: formulation-000074
  area: evidence
  topic: Study variants and unresolved full formula
  outcome: unknown
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - paper
  - ccap-jm
  - claims
  summary: Study uses Jaworski medium with deionized water; no supported ingredient
    difference for a new variant. Complete base formula, stock encoding and physical-state
    equivalence remain unresolved; parent fields unchanged.
- assessment_id: taxonomy-000074
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - paper
  - taxonomy
  - strain-taxonomy
  - excerpts
  - exporter
  summary: Chlorella vulgaris CCAP 211/63. Verified name/rank and qualified strain
    mapping retained in notes; no positive native growth assertion.
- assessment_id: preservation-000074
  area: evidence
  topic: Existing claims and file presentation
  outcome: supported
  target_ids:
  - CultureMech:000074
  evidence_ids:
  - readback
  - extra-02
  summary: All 4 ingredients and pre-existing fields preserved. Reversing additions
    recovers original bytes; one history event; no-op replay changes nothing.
- assessment_id: identity-000350
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - paper
  - pubmed
  - claims
  summary: One paper citation with verified title, eight authors, 2015 year, DOI/PMID,
    raw XML and Markdown.
- assessment_id: formulation-000350
  area: evidence
  topic: Study variants and unresolved full formula
  outcome: unknown
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - paper
  - ccap-jm
  - claims
  summary: Study uses Jaworski medium with deionized water; no supported ingredient
    difference for a new variant. Complete base formula, stock encoding and physical-state
    equivalence remain unresolved; parent fields unchanged.
- assessment_id: taxonomy-000350
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - paper
  - taxonomy
  - strain-taxonomy
  - excerpts
  - exporter
  summary: Chlorella vulgaris CCAP 211/63. Verified name/rank and qualified strain
    mapping retained in notes; no positive native growth assertion.
- assessment_id: preservation-000350
  area: evidence
  topic: Existing claims and file presentation
  outcome: supported
  target_ids:
  - CultureMech:000350
  evidence_ids:
  - readback
  - extra-02
  summary: All 15 ingredients and pre-existing fields preserved. Reversing additions
    recovers original bytes; one history event; no-op replay changes nothing.
- assessment_id: identity-000149
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - pubmed
  - claims
  summary: One paper citation with verified title, eight authors, 2015 year, DOI/PMID,
    raw XML and Markdown.
- assessment_id: formulation-000149
  area: evidence
  topic: Study variants and unresolved full formula
  outcome: unknown
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - ccap-f2
  - claims
  summary: Silicate, nitrate and antibiotic contexts are separate; unresolved double
    strength is not equated to Quad. Complete base formula, stock encoding and physical-state
    equivalence remain unresolved; parent fields unchanged.
- assessment_id: taxonomy-000149
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - taxonomy
  - strain-taxonomy
  - excerpts
  - exporter
  summary: 34 f/2-relevant rows, with two other-medium organisms explicitly excluded.
    Verified name/rank and qualified strain mapping retained in notes; no positive
    native growth assertion.
- assessment_id: preservation-000149
  area: evidence
  topic: Existing claims and file presentation
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - readback
  - extra-02
  summary: All 13 ingredients and pre-existing fields preserved. Reversing additions
    recovers original bytes; one history event; no-op replay changes nothing.
- assessment_id: variant-amount-000149-0-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0];
    old=absent study-variant entry; new=The study reports f/2 supplemented with 1.06e-4
    M silicate. Preserve this stated supplementation concentration without assigning
    an unreported silicate salt, hydrate, stock recipe or additional mass conversion.
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: Isochrysis galbana was
    cultured using f/2 supplemented with 1.06 × 10−4 M silicate Locator and scope:
    Supports only variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0].
    Locator: Methods / Microalgae and cyanobacteria strains and culture conditions.
    Reported scientific name=Isochrysis galbana; strain=CCAP 927/1; canonical scientific
    name=Isochrysis galbana; NCBITaxon:37099; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=37099;
    scope=silicate-supplemented f/2. Directly stated supplement value in the study
    medium, not a stock concentration or calculated total including background. No
    calculation. Local f/2 + Si owners specify sodium silicate nonahydrate and differently
    encoded stock amounts; the paper does not establish exact equivalence. Calculation:
    none. Parent amounts unchanged; complete formulation unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: variant-amount-000149-1-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0];
    old=absent study-variant entry; new=The study reports f/2 supplemented with 29.4
    mM NaNO3 and adjusted to pH 8. Retain the stated supplement concentration; do
    not infer whether it includes the base-medium nitrate or calculate a total nitrate
    concentration.
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: A. platensis was cultured
    using f/2 supplemented with 29.4 mM NaNO3 and adjusted to pH 8. Locator and scope:
    Supports only variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0].
    Locator: Methods / Microalgae and cyanobacteria strains and culture conditions.
    Reported scientific name=Arthrospira platensis; strain=CCMP 1295; canonical scientific
    name=Limnospira platensis; NCBITaxon:118562; actual rank=species; taxonomy_match=verified_synonym_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=118562;
    scope=nitrate-supplemented f/2 at pH 8. Directly reported supplementation value
    and study pH, not a stock quantity or a universal optimum. No arithmetic; base-plus-supplement
    total remains unresolved. Calculation: none. Parent amounts unchanged; complete
    formulation unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: variant-amount-000149-2-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: 'status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0];
    old=absent study-variant entry; new=Reported penicillin G treatment concentration:
    200 micrograms per mL in the treated f/2 culture; no unreported salt form, stock
    strength or conversion is assigned.'
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics
    penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1.
    Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2].
    Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella
    polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha;
    NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported
    scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific
    name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These
    strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial
    interference experiment, not an unresolved maintenance-strength assignment. The
    two directly stated culture-treatment amounts share this exact excerpt; no arithmetic.
    Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella
    on that agar. Calculation: none. Parent amounts unchanged; complete formulation
    unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: variant-amount-000149-2-1
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000149
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: 'status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[1];
    old=absent study-variant entry; new=Reported dihydrostreptomycin sulphate treatment
    concentration: 50 micrograms per mL in the same treated culture; not streptomycin,
    not a stock concentration, and no hydrate assumption.'
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics
    penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1.
    Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2].
    Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella
    polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha;
    NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported
    scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific
    name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These
    strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial
    interference experiment, not an unresolved maintenance-strength assignment. The
    two directly stated culture-treatment amounts share this exact excerpt; no arithmetic.
    Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella
    on that agar. Calculation: none. Parent amounts unchanged; complete formulation
    unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: identity-000343
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - pubmed
  - claims
  summary: One paper citation with verified title, eight authors, 2015 year, DOI/PMID,
    raw XML and Markdown.
- assessment_id: formulation-000343
  area: evidence
  topic: Study variants and unresolved full formula
  outcome: unknown
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - ccap-f2
  - claims
  summary: Silicate, nitrate and antibiotic contexts are separate; unresolved double
    strength is not equated to Quad. Complete base formula, stock encoding and physical-state
    equivalence remain unresolved; parent fields unchanged.
- assessment_id: taxonomy-000343
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - taxonomy
  - strain-taxonomy
  - excerpts
  - exporter
  summary: 34 f/2-relevant rows, with two other-medium organisms explicitly excluded.
    Verified name/rank and qualified strain mapping retained in notes; no positive
    native growth assertion.
- assessment_id: preservation-000343
  area: evidence
  topic: Existing claims and file presentation
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - readback
  - extra-02
  summary: All 14 ingredients and pre-existing fields preserved. Reversing additions
    recovers original bytes; one history event; no-op replay changes nothing.
- assessment_id: variant-amount-000343-0-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0];
    old=absent study-variant entry; new=The study reports f/2 supplemented with 1.06e-4
    M silicate. Preserve this stated supplementation concentration without assigning
    an unreported silicate salt, hydrate, stock recipe or additional mass conversion.
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: Isochrysis galbana was
    cultured using f/2 supplemented with 1.06 × 10−4 M silicate Locator and scope:
    Supports only variants[name=f_2_silicate_supplement_1_06e_4_m].modifications[0].
    Locator: Methods / Microalgae and cyanobacteria strains and culture conditions.
    Reported scientific name=Isochrysis galbana; strain=CCAP 927/1; canonical scientific
    name=Isochrysis galbana; NCBITaxon:37099; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=37099;
    scope=silicate-supplemented f/2. Directly stated supplement value in the study
    medium, not a stock concentration or calculated total including background. No
    calculation. Local f/2 + Si owners specify sodium silicate nonahydrate and differently
    encoded stock amounts; the paper does not establish exact equivalence. Calculation:
    none. Parent amounts unchanged; complete formulation unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: variant-amount-000343-1-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0];
    old=absent study-variant entry; new=The study reports f/2 supplemented with 29.4
    mM NaNO3 and adjusted to pH 8. Retain the stated supplement concentration; do
    not infer whether it includes the base-medium nitrate or calculate a total nitrate
    concentration.
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: A. platensis was cultured
    using f/2 supplemented with 29.4 mM NaNO3 and adjusted to pH 8. Locator and scope:
    Supports only variants[name=f_2_nitrate_supplement_29_4_mm].modifications[0].
    Locator: Methods / Microalgae and cyanobacteria strains and culture conditions.
    Reported scientific name=Arthrospira platensis; strain=CCMP 1295; canonical scientific
    name=Limnospira platensis; NCBITaxon:118562; actual rank=species; taxonomy_match=verified_synonym_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=118562;
    scope=nitrate-supplemented f/2 at pH 8. Directly reported supplementation value
    and study pH, not a stock quantity or a universal optimum. No arithmetic; base-plus-supplement
    total remains unresolved. Calculation: none. Parent amounts unchanged; complete
    formulation unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: variant-amount-000343-2-0
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: 'status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0];
    old=absent study-variant entry; new=Reported penicillin G treatment concentration:
    200 micrograms per mL in the treated f/2 culture; no unreported salt form, stock
    strength or conversion is assigned.'
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics
    penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1.
    Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2].
    Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella
    polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha;
    NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported
    scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific
    name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These
    strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial
    interference experiment, not an unresolved maintenance-strength assignment. The
    two directly stated culture-treatment amounts share this exact excerpt; no arithmetic.
    Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella
    on that agar. Calculation: none. Parent amounts unchanged; complete formulation
    unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
- assessment_id: variant-amount-000343-2-1
  area: evidence
  topic: Inline study-variant concentration decision
  outcome: supported
  target_ids:
  - CultureMech:000343
  evidence_ids:
  - paper
  - claims
  - excerpts
  - readback
  summary: 'status=add; field=variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[1];
    old=absent study-variant entry; new=Reported dihydrostreptomycin sulphate treatment
    concentration: 50 micrograms per mL in the same treated culture; not streptomycin,
    not a stock concentration, and no hydrate assumption.'
  details: 'Reference: doi:10.1038/srep10036. Exact snippet: treated with the antibiotics
    penicillin G and dihydrostreptomycin sulphate in a ratio of 200 μg mL−1: 50 μg mL−1.
    Locator and scope: Supports only variants[name=f_2_penicillin_g_dihydrostreptomycin_supplement].modifications[0:2].
    Locator: Methods / Bacterial interference experiment. Reported scientific name=Dunaliella
    polymorpha; strain=CCAP 19/7A; canonical scientific name=Dunaliella polymorpha;
    NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. Reported
    scientific name=Dunaliella polymorpha; strain=CCAP 19/7C; canonical scientific
    name=Dunaliella polymorpha; NCBITaxon:346903; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=346903;
    scope=f/2 or double-strength f/2; general maintenance assignment unresolved. These
    strain rows have a separate assay-specific assignment to f/2 in Methods / Bacterial
    interference experiment, not an unresolved maintenance-strength assignment. The
    two directly stated culture-treatment amounts share this exact excerpt; no arithmetic.
    Marine-agar sampling concerns co-occurring bacteria, not growth of Dunaliella
    on that agar. Calculation: none. Parent amounts unchanged; complete formulation
    unresolved.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Direct study-variant amount or explicit unquantified HCl dose; never
      inferred from pH
    evidence_ids:
    - paper
findings:
- finding_id: merge-gates
  issue_key: algal-followup-citations-merge-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repository merge gates failed
  description: Failures retained without assuming equal aggregate counts prove unchanged
    rows or attributing all failures to this batch. No generated publication.
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - merge-00
  - merge-01
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
- finding_id: reference-checks
  issue_key: algal-followup-citations-reference-checks
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Full-text excerpts are unavailable to the automatic reference fetch
  description: All baseline commands passed. Four post-edit aggregate validations
    fail on eight new variant excerpts because the automatic DOI fetch has only the
    abstract. Primary JATS and derived Markdown contain each exact methods excerpt.
    Schema, term and strict checks pass. These are newly exposed failures, not baseline
    failures or waived checks.
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - post-00
  - post-02
  - post-08
  - post-10
  - paper
  - excerpts
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
- finding_id: formulation-and-scope
  issue_key: algal-followup-citations-formulation-and-scope
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Full formulas and native growth scope remain unresolved
  description: The paper does not restate complete formulas. Current source recipes
    and flattened imports cannot establish historical stock amounts or solid/liquid
    equivalence. General maintenance strength is unassigned per strain. Name-level
    taxonomy is not strain reidentification. The exporter does not honor inline variant
    growth scope.
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  evidence_ids:
  - claims
  - taxonomy
  - strain-taxonomy
  - ccap-ajs
  - ccap-jm
  - ccap-f2
  - exporter
  - pending
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-merge-gates
  description: Repository merge gates failed
  finding_ids:
  - merge-gates
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Diagnose maintained merge inputs and rules, then pass both gates before publication.
- action_id: resolve-reference-checks
  description: Full-text excerpts are unavailable to the automatic reference fetch
  finding_ids:
  - reference-checks
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000149
  - CultureMech:000343
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Make verified full text available through the maintained reference resolver; preserve
    correct source quotations and rerun reference validation.
- action_id: resolve-formulation-and-scope
  description: Full formulas and native growth scope remain unresolved
  finding_ids:
  - formulation-and-scope
  target_ids:
  - CultureMech:000041
  - CultureMech:000338
  - CultureMech:000074
  - CultureMech:000350
  - CultureMech:000149
  - CultureMech:000343
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/ajs.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/jm.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/f_2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/f_2.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Resolve full study formulation, source-owner and organism/strain scope before
    adding or exporting positive native growth assertions.
limitations:
- Focused self-review, not independent adversarial or complete scientific review.
- Thirty-six medium-relevant organism/strain rows, not every organism in the full
  paper or analytical calibration.
- Complete historical formulas, unspecified stock/chemical forms, nitrate total and
  silicate salt remain unresolved.
- Current species-rank matches, including unclassified strain labels, do not independently
  reidentify the experimental cultures.
- No new native positive growth assertion, canonical amount change, record merge,
  export, or GitHub mutation.
- Reference and global merge gate failures remain open; corpus-wide citation discovery
  remains active.
```
