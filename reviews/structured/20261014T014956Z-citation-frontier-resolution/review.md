# Bounded paper-citation frontier review

- Review: 20261014T014956Z-citation-frontier-resolution
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-14T00:44:21Z
- Finished UTC: 2026-10-14T01:49:56Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

20 new citations, six enrichments and two verified duplicates removed across 21 owners; 259 ingredients preserved. Bounded identity, taxonomy and recipe-discrepancy notes, not full scientific approval. Affected baseline 42/42 passed; post-edit 39/42 passed, with schema/terms/strict passing on all 21. Native URL and global merge failures retained. Fast-test gate exit code: 0.

## Scope And Provenance

21 normalized bibliography owners, including a stock solution.

Selection: Primary reference chains, verified publication aliases/corrections and historical MediaDB joins.
Coverage: full; 21 reviewed / 21 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:004981 | data/normalized_yaml/bacterial/vr_salts_b.yaml | maintained | vr_salts_b |
| CultureMech:007081 | data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml | maintained | m9_0_2_glycerol |
| CultureMech:007082 | data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml | maintained | m9_0_24_pyruvate |
| CultureMech:007083 | data/normalized_yaml/bacterial/m9_0_45_succinate.yaml | maintained | m9_0_45_succinate |
| CultureMech:007084 | data/normalized_yaml/bacterial/m9_0_27_acetate.yaml | maintained | m9_0_27_acetate |
| CultureMech:007085 | data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml | maintained | m9_0_4_glycerol |
| CultureMech:007086 | data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml | maintained | lr_0_4_glycerol |
| CultureMech:007087 | data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml | maintained | n_c_0_4_glycerol |
| CultureMech:007088 | data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml | maintained | modifed_m9_with_glucose |
| CultureMech:007089 | data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml | maintained | modified_m9_with_toluene |
| CultureMech:007090 | data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml | maintained | e2_medium_with_octanoate |
| CultureMech:007093 | data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml | maintained | e2_medium_with_gluconate |
| CultureMech:007094 | data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml | maintained | e2_medium_with_citrate |
| CultureMech:007150 | data/normalized_yaml/bacterial/isolation_medium.yaml | maintained | isolation_medium |
| CultureMech:007220 | data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml | maintained | mr_medium_d_fructose |
| CultureMech:007261 | data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml | maintained | minimal_medium_whitchurch_et_al |
| CultureMech:007293 | data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml | maintained | defined_freshwater_medium_coso4 |
| CultureMech:007294 | data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml | maintained | defined_freshwater_medium_cocl2 |
| CultureMech:007295 | data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml | maintained | nitrogen_limited_mr_medium |
| CultureMech:008841 | data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml | maintained | artificial_seawater_base_with_thiosulfate_as_the_electron_donor |
| CultureMech:009406 | data/normalized_yaml/bacterial/pye_solid_medium.yaml | maintained | pye_solid_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml | passed | True | CultureMech:008841 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml | passed | True | CultureMech:008841 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml | passed | True | CultureMech:007294 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml | passed | True | CultureMech:007294 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml | passed | True | CultureMech:007293 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml | passed | True | CultureMech:007293 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml | passed | True | CultureMech:007094 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml | passed | True | CultureMech:007094 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml | passed | True | CultureMech:007093 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml | passed | True | CultureMech:007093 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml | passed | True | CultureMech:007090 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml | passed | True | CultureMech:007090 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/isolation_medium.yaml | passed | True | CultureMech:007150 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/isolation_medium.yaml | passed | True | CultureMech:007150 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml | passed | True | CultureMech:007086 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml | passed | True | CultureMech:007086 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml | passed | True | CultureMech:007082 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml | passed | True | CultureMech:007082 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_27_acetate.yaml | passed | True | CultureMech:007084 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_27_acetate.yaml | passed | True | CultureMech:007084 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml | passed | True | CultureMech:007081 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml | passed | True | CultureMech:007081 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_45_succinate.yaml | passed | True | CultureMech:007083 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_45_succinate.yaml | passed | True | CultureMech:007083 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml | passed | True | CultureMech:007085 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml | passed | True | CultureMech:007085 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml | passed | True | CultureMech:007261 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml | passed | True | CultureMech:007261 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml | passed | True | CultureMech:007088 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml | passed | True | CultureMech:007088 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml | passed | True | CultureMech:007089 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml | passed | True | CultureMech:007089 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml | passed | True | CultureMech:007220 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml | passed | True | CultureMech:007220 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml | passed | True | CultureMech:007087 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml | passed | True | CultureMech:007087 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml | passed | True | CultureMech:007295 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml | passed | True | CultureMech:007295 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/pye_solid_medium.yaml | passed | True | CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/pye_solid_medium.yaml | passed | True | CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/vr_salts_b.yaml | passed | True | CultureMech:004981 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/vr_salts_b.yaml | passed | True | CultureMech:004981 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/vr_salts_b.yaml | failed | True | CultureMech:004981 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/vr_salts_b.yaml | passed | True | CultureMech:004981 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml | passed | True | CultureMech:007081 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml | passed | True | CultureMech:007081 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml | passed | True | CultureMech:007082 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml | passed | True | CultureMech:007082 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_45_succinate.yaml | passed | True | CultureMech:007083 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_45_succinate.yaml | passed | True | CultureMech:007083 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_27_acetate.yaml | passed | True | CultureMech:007084 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_27_acetate.yaml | passed | True | CultureMech:007084 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml | passed | True | CultureMech:007085 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml | passed | True | CultureMech:007085 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml | passed | True | CultureMech:007086 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml | passed | True | CultureMech:007086 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml | passed | True | CultureMech:007087 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml | passed | True | CultureMech:007087 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml | passed | True | CultureMech:007088 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml | passed | True | CultureMech:007088 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml | passed | True | CultureMech:007089 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml | passed | True | CultureMech:007089 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml | passed | True | CultureMech:007090 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml | passed | True | CultureMech:007090 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml | passed | True | CultureMech:007093 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml | passed | True | CultureMech:007093 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml | passed | True | CultureMech:007094 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml | passed | True | CultureMech:007094 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/isolation_medium.yaml | passed | True | CultureMech:007150 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/isolation_medium.yaml | passed | True | CultureMech:007150 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml | passed | True | CultureMech:007220 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml | passed | True | CultureMech:007220 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml | passed | True | CultureMech:007261 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml | passed | True | CultureMech:007261 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml | passed | True | CultureMech:007293 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml | passed | True | CultureMech:007293 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml | passed | True | CultureMech:007294 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml | passed | True | CultureMech:007294 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml | passed | True | CultureMech:007295 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml | passed | True | CultureMech:007295 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml | failed | True | CultureMech:008841 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml | passed | True | CultureMech:008841 | Actual required-check outcome retained; no waiver. |
| just validate data/normalized_yaml/bacterial/pye_solid_medium.yaml | failed | True | CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| just validate-strict data/normalized_yaml/bacterial/pye_solid_medium.yaml | passed | True | CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| just verify-merges | failed | True | CultureMech:004981, CultureMech:007081, CultureMech:007082, CultureMech:007083, CultureMech:007084, CultureMech:007085, CultureMech:007086, CultureMech:007087, CultureMech:007088, CultureMech:007089, CultureMech:007090, CultureMech:007093, CultureMech:007094, CultureMech:007150, CultureMech:007220, CultureMech:007261, CultureMech:007293, CultureMech:007294, CultureMech:007295, CultureMech:008841, CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| just audit-merge-freshness | failed | True | CultureMech:004981, CultureMech:007081, CultureMech:007082, CultureMech:007083, CultureMech:007084, CultureMech:007085, CultureMech:007086, CultureMech:007087, CultureMech:007088, CultureMech:007089, CultureMech:007090, CultureMech:007093, CultureMech:007094, CultureMech:007150, CultureMech:007220, CultureMech:007261, CultureMech:007293, CultureMech:007294, CultureMech:007295, CultureMech:008841, CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:004981, CultureMech:007081, CultureMech:007082, CultureMech:007083, CultureMech:007084, CultureMech:007085, CultureMech:007086, CultureMech:007087, CultureMech:007088, CultureMech:007089, CultureMech:007090, CultureMech:007093, CultureMech:007094, CultureMech:007150, CultureMech:007220, CultureMech:007261, CultureMech:007293, CultureMech:007294, CultureMech:007295, CultureMech:008841, CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| git diff --check | passed | True | CultureMech:004981, CultureMech:007081, CultureMech:007082, CultureMech:007083, CultureMech:007084, CultureMech:007085, CultureMech:007086, CultureMech:007087, CultureMech:007088, CultureMech:007089, CultureMech:007090, CultureMech:007093, CultureMech:007094, CultureMech:007150, CultureMech:007220, CultureMech:007261, CultureMech:007293, CultureMech:007294, CultureMech:007295, CultureMech:008841, CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-citation-frontier-resolution/curate.py --apply | passed | True | CultureMech:004981, CultureMech:007081, CultureMech:007082, CultureMech:007083, CultureMech:007084, CultureMech:007085, CultureMech:007086, CultureMech:007087, CultureMech:007088, CultureMech:007089, CultureMech:007090, CultureMech:007093, CultureMech:007094, CultureMech:007150, CultureMech:007220, CultureMech:007261, CultureMech:007293, CultureMech:007294, CultureMech:007295, CultureMech:008841, CultureMech:009406 | Actual required-check outcome retained; no waiver. |
| just test-fast | passed | True | CultureMech:004981, CultureMech:007081, CultureMech:007082, CultureMech:007083, CultureMech:007084, CultureMech:007085, CultureMech:007086, CultureMech:007087, CultureMech:007088, CultureMech:007089, CultureMech:007090, CultureMech:007093, CultureMech:007094, CultureMech:007150, CultureMech:007220, CultureMech:007261, CultureMech:007293, CultureMech:007294, CultureMech:007295, CultureMech:008841, CultureMech:009406 | Actual required-check outcome retained; no waiver. |

## Scientific And Domain Assessments

### Publication identity and provenance

evidence: supported. Targets: CultureMech:004981.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:004981.

VR salts B remains a stock SOLUTION; abstract does not enumerate the stock or prove growth on the stock alone.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:004981.

Reported organism/group=Acidaminococcus fermentans; canonical scientific name=Acidaminococcus fermentans; NCBITaxon:905; actual rank=species; taxonomy_match=exact_species; role=species studied, not growth on an isolated stock solution. Reported organism/group=Acidaminococcus; canonical scientific name=Acidaminococcus; NCBITaxon:904; actual rank=genus; taxonomy_match=exact_genus; role=taxonomic description/comparison, not a genus-wide cultivation assertion. Reported organism/group=Veillonella; canonical scientific name=Veillonella; NCBITaxon:29465; actual rank=genus; taxonomy_match=exact_genus; role=taxonomic description/comparison, not a genus-wide cultivation assertion. Reported organism/group=Peptococcus; canonical scientific name=Peptococcus; NCBITaxon:2740; actual rank=genus; taxonomy_match=exact_genus; role=taxonomic description/comparison, not a genus-wide cultivation assertion. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:004981.

0 new citations; 1 enrichments; 1 verified duplicate removals. 13 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007081.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007081.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007081.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007081.

1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007082.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007082.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007082.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007082.

1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007083.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007083.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007083.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007083.

1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007084.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007084.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007084.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007084.

1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007085.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007085.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007085.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007085.

1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007086.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007086.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007086.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007086.

1 new citations; 0 enrichments; 0 verified duplicate removals. 6 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007087.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007087.

Author-order correction only; conflicting main-article versus erratum author order retained. No recipe change follows.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007087.

Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain; role=organism in the corrected article title, not a new growth experiment. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007087.

1 new citations; 0 enrichments; 0 verified duplicate removals. 6 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007088.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007088.

Cited M9 base abstract lacks a complete recipe; historical B13 and its engineered clone are not the current KT2440 owner. Visually verified lower correction concerns substrate naming and assay reporting, not M9 concentrations. Upper notice/PMID excluded. Only prior unresolved-correction wording updated; other prior Nogales claims and taxa not re-reviewed.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007088.

Reported organism/group=Pseudomonas sp. strain B13 and its TOL-plasmid-bearing clone; canonical scientific name=Pseudomonas knackmussii B13; NCBITaxon:1301098; actual rank=strain; taxonomy_match=verified_B13_synonym_with_derivative_parent_only; role=historical base strain; exact engineered clone identity not asserted. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007088.

2 new citations; 1 enrichments; 0 verified duplicate removals. 13 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007089.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007089.

Cited M9 base abstract lacks a complete recipe; historical B13 and its engineered clone are not the current KT2440 owner. Visually verified lower correction concerns substrate naming and assay reporting, not M9 concentrations. Upper notice/PMID excluded. Only prior unresolved-correction wording updated; other prior Nogales claims and taxa not re-reviewed.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007089.

Reported organism/group=Pseudomonas sp. strain B13 and its TOL-plasmid-bearing clone; canonical scientific name=Pseudomonas knackmussii B13; NCBITaxon:1301098; actual rank=strain; taxonomy_match=verified_B13_synonym_with_derivative_parent_only; role=historical base strain; exact engineered clone identity not asserted. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007089.

2 new citations; 1 enrichments; 0 verified duplicate removals. 13 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007090.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007090.

E2 base abstract lacks complete salts/stocks; historical ATCC strain identity remains genus-only, distinct from the citing study strains.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007090.

Reported organism/group=Pseudomonas oleovorans ATCC 29347 (historical name); canonical scientific name=Pseudomonas; NCBITaxon:286; actual rank=genus; taxonomy_match=parent_rank_only; role=base-paper study strain; current species identity unresolved. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007090.

1 new citations; 0 enrichments; 0 verified duplicate removals. 11 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007093.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007093.

E2 base abstract lacks complete salts/stocks; historical ATCC strain identity remains genus-only, distinct from the citing study strains.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007093.

Reported organism/group=Pseudomonas oleovorans ATCC 29347 (historical name); canonical scientific name=Pseudomonas; NCBITaxon:286; actual rank=genus; taxonomy_match=parent_rank_only; role=base-paper study strain; current species identity unresolved. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007093.

1 new citations; 0 enrichments; 0 verified duplicate removals. 11 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007094.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007094.

E2 base abstract lacks complete salts/stocks; historical ATCC strain identity remains genus-only, distinct from the citing study strains.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007094.

Reported organism/group=Pseudomonas oleovorans ATCC 29347 (historical name); canonical scientific name=Pseudomonas; NCBITaxon:286; actual rank=genus; taxonomy_match=parent_rank_only; role=base-paper study strain; current species identity unresolved. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007094.

1 new citations; 0 enrichments; 0 verified duplicate removals. 11 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007150.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007150.

Bibliographic DOI equivalence only; pre-existing recipe and organism claims not re-reviewed.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007150.

No new organism mapping in this alias-only edit; prior taxonomy claims are not re-reviewed. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007150.

0 new citations; 1 enrichments; 0 verified duplicate removals. 13 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007220.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007220.

MR base abstract lacks a complete formula; recombinant E. coli results are not transferred to the current Cupriavidus owners.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007220.

Reported organism/group=Escherichia coli XL1-Blue carrying pSYL105 or pSYL107; canonical scientific name=Escherichia coli; NCBITaxon:562; actual rank=species; taxonomy_match=parent_rank_only; role=two distinct recombinant derivatives; exact strain/derivative nodes unresolved. Reported organism/group=Alcaligenes eutrophus; canonical scientific name=Cupriavidus necator; NCBITaxon:106590; actual rank=species; taxonomy_match=verified_species_synonym; role=gene source, not proof that the donor grew in these E. coli assays. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007220.

1 new citations; 0 enrichments; 0 verified duplicate removals. 12 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007261.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007261.

Non-operational publication and organism identity only; no experimental, cultivation, biofilm or virulence curation.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007261.

Reported organism/group=Pseudomonas aeruginosa; canonical scientific name=Pseudomonas aeruginosa; NCBITaxon:287; actual rank=species; taxonomy_match=verified_species_name; role=organism mention only; no strain-specific or cultivation assertion. Reported organism/group=Pseudomonas aeruginosa PAO1; canonical scientific name=Pseudomonas aeruginosa PAO1; NCBITaxon:208964; actual rank=strain; taxonomy_match=verified_strain_name; role=identity mention only; no experimental assertion. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007261.

1 new citations; 0 enrichments; 0 verified duplicate removals. 16 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007293.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007293.

Base-protocol abstract does not enumerate the freshwater formula; cobalt alternatives and combined assay contexts remain unresolved.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007293.

Reported organism/group=Geobacter metallireducens GS-15; canonical scientific name=Geobacter metallireducens GS-15; NCBITaxon:269799; actual rank=strain; taxonomy_match=verified_named_strain; role=organism characterized in the cited base paper, not the current Rhodoferax study. Reported organism/group=Desulfuromonas acetoxidans; canonical scientific name=Desulfuromonas acetoxidans; NCBITaxon:891; actual rank=species; taxonomy_match=exact_species; role=phylogenetic comparator, not cultivation on this owner. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007293.

1 new citations; 0 enrichments; 0 verified duplicate removals. 39 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007294.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007294.

Base-protocol abstract does not enumerate the freshwater formula; cobalt alternatives and combined assay contexts remain unresolved.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007294.

Reported organism/group=Geobacter metallireducens GS-15; canonical scientific name=Geobacter metallireducens GS-15; NCBITaxon:269799; actual rank=strain; taxonomy_match=verified_named_strain; role=organism characterized in the cited base paper, not the current Rhodoferax study. Reported organism/group=Desulfuromonas acetoxidans; canonical scientific name=Desulfuromonas acetoxidans; NCBITaxon:891; actual rank=species; taxonomy_match=exact_species; role=phylogenetic comparator, not cultivation on this owner. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007294.

1 new citations; 0 enrichments; 0 verified duplicate removals. 39 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:007295.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:007295.

MR base abstract lacks a complete formula; recombinant E. coli results are not transferred to the current Cupriavidus owners.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:007295.

Reported organism/group=Escherichia coli XL1-Blue carrying pSYL105 or pSYL107; canonical scientific name=Escherichia coli; NCBITaxon:562; actual rank=species; taxonomy_match=parent_rank_only; role=two distinct recombinant derivatives; exact strain/derivative nodes unresolved. Reported organism/group=Alcaligenes eutrophus; canonical scientific name=Cupriavidus necator; NCBITaxon:106590; actual rank=species; taxonomy_match=verified_species_synonym; role=gene source, not proof that the donor grew in these E. coli assays. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:007295.

1 new citations; 0 enrichments; 0 verified duplicate removals. 13 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:008841.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:008841.

Separate liquid and semisolid assays retained. Local aggregated seawater may hide components; cited bases/stocks remain unresolved, not an exact variant. Species description supports historical MC-1 identity, not exact-recipe growth or stock composition.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:008841.

Reported organism/group=Magnetococcus marinus MC-1(T); canonical scientific name=Magnetococcus marinus MC-1; NCBITaxon:156889; actual rank=strain; taxonomy_match=verified_type_strain_lineage; role=identity reconciliation for historical MC-1, not new exact-recipe growth. Reported organism/group=Magnetococcus marinus; canonical scientific name=Magnetococcus marinus; NCBITaxon:1124597; actual rank=species; taxonomy_match=exact_species; role=species described. Reported organism/group=Magnetococcus; canonical scientific name=Magnetococcus; NCBITaxon:162171; actual rank=genus; taxonomy_match=exact_named_group; role=taxonomic placement discussed, not a group-wide growth assertion. Reported organism/group=Magnetococcaceae; canonical scientific name=Magnetococcaceae; NCBITaxon:1191479; actual rank=family; taxonomy_match=exact_named_group; role=taxonomic placement discussed, not a group-wide growth assertion. Reported organism/group=Magnetococcales; canonical scientific name=Magnetococcales; NCBITaxon:1191478; actual rank=order; taxonomy_match=exact_named_group; role=taxonomic placement discussed, not a group-wide growth assertion. Reported organism/group=Alphaproteobacteria; canonical scientific name=Alphaproteobacteria; NCBITaxon:28211; actual rank=class; taxonomy_match=exact_named_group; role=taxonomic placement discussed, not a group-wide growth assertion. Reported organism/group=marine magnetotactic coccus strain MC-1; canonical scientific name=Magnetococcus marinus MC-1; NCBITaxon:156889; actual rank=strain; taxonomy_match=historical_strain_identity_supported_by_2013_species_description; role=primary study organism. Reported organism/group=Chlorobaculum tepidum; canonical scientific name=Chlorobaculum tepidum; NCBITaxon:1097; actual rank=species; taxonomy_match=exact_species; role=separate comparator culture, not growth on the MC-1 owner. Reported organism/group=Rhodospirillum rubrum; canonical scientific name=Rhodospirillum rubrum; NCBITaxon:1085; actual rank=species; taxonomy_match=exact_species; role=separate comparator culture, not growth on the MC-1 owner. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:008841.

1 new citations; 1 enrichments; 0 verified duplicate removals. 3 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

### Publication identity and provenance

evidence: supported. Targets: CultureMech:009406.

Verified identity and access scope; aliases and distinct correction notices accounted for.

### Exact formulation and claim boundary

evidence: unknown. Targets: CultureMech:009406.

PYE abstract distinguishes CB15 and NA1000 but does not resolve solid/liquid recipe assignment. Background mention is not growth evidence.

### Bounded scientific-name and rank assessment

evidence: supported. Targets: CultureMech:009406.

Reported organism/group=Caulobacter crescentus CB15; canonical scientific name=Caulobacter vibrioides; NCBITaxon:155892; actual rank=species; taxonomy_match=parent_rank_only; role=named study strain; current species synonym verified but exact strain node not assigned. Reported organism/group=Caulobacter crescentus NA1000; canonical scientific name=Caulobacter vibrioides; NCBITaxon:155892; actual rank=species; taxonomy_match=parent_rank_only; role=distinct laboratory derivative, not interchangeable with CB15. Reported organism/group=Pseudomonas aeruginosa; canonical scientific name=Pseudomonas aeruginosa; NCBITaxon:287; actual rank=species; taxonomy_match=exact_species; role=abstract background comparator only; no experimental or growth claim curated. No new growth associations.

### Mutation and export boundary

evidence: supported. Targets: CultureMech:009406.

0 new citations; 1 enrichments; 1 verified duplicate removals. 5 prior ingredients preserved; one appended history event. No new growth, quantity, resolved variant or generated publication.

## Findings

### merge-gates: Repository-wide merge verification and freshness gates failed

major / open / confirmed; issue key: citation-frontier-merge-gates.

Global diagnostics are not attributed to the bibliography edits; generated outputs were not published.

### native-url-checks: Three native URL reference checks failed

minor / open / confirmed; issue key: citation-frontier-native-url-checks.

Two PMC document titles include a site suffix; one ordinary DOI-URL request returned HTTP 403. Independently archived publication identity supports the retained article titles but does not turn these failed checks into passes.

### formulation-boundary: Citation support does not resolve exact formulation or growth

informational / open / confirmed; issue key: citation-frontier-formulation-boundary.

Abstract-only sources, existing chemical-identity discrepancies and uninspected base/stock references prevent exact recipe matching. Corrections are scoped separately; Whitchurch remains non-operational identity only. No resolved variants or positive growth assertions were added.

## Recommended Actions And Acceptance Checks

### resolve-merge-gates

Repository-wide merge verification and freshness gates failed

- Resolve derivation defects in a separately scoped change and rerun both gates before publication.

### resolve-native-url-checks

Three native URL reference checks failed

- Restore ordinary bibliographic access or separately improve URL-title handling with tests, then rerun. Do not fabricate cache metadata or rewrite correct article titles to match error/page-wrapper titles.

### resolve-formulation-boundary

Citation support does not resolve exact formulation or growth

- Keep unsupported formulation and growth unresolved; inspect relevant primary passages and preserve assay/strain scope before additional curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| paper-8387263-raw | PMID:8387263; references_cache/papers/PMID_8387263.xml; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-11135197-raw | PMID:11135197; references_cache/papers/PMID_11135197.xml; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-11135197-crossref_raw | PMID:11135197; references_cache/papers/primary_metadata/frontier-durner-2001-20261014.json; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-2687253-raw | PMID:2687253; references_cache/papers/PMID_2687253.xml; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-16461683-raw | PMID:16461683; references_cache/papers/PMID_16461683.xml; PubMed_abstract_and_selected_primary_full_HTML_methods | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-16461683-full_raw | PMID:16461683; references_cache/papers/primary_html/frontier-mc1-2006-20261014.html; PubMed_abstract_and_selected_primary_full_HTML_methods | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-20472802-raw | PMID:20472802; references_cache/papers/PMID_20472802.xml; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-5784223-raw | PMID:5784223; references_cache/papers/PMID_5784223.xml; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-11859186-raw | PMID:11859186; references_cache/papers/PMID_11859186.xml; author_posted_article_text_archived_with_bounded_markdown_summary | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-11859186-author_text | PMID:11859186; references_cache/papers/primary_browser/bibliographic-whitchurch-2002-20261013.web.txt; author_posted_article_text_archived_with_bounded_markdown_summary | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-22581902-raw | PMID:22581902; references_cache/papers/PMID_22581902.xml; PubMed_abstract_not_full_text | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-lee-raw | doi:10.1007/BF02074874; references_cache/papers/primary_html/lee-1996-mr-base-20261013.html; publisher_abstract_preview | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-paliy-erratum-raw | doi:10.1007/s00253-006-0683-0; references_cache/papers/primary_html/paliy-2006-erratum.html; publisher_erratum_body_and_metadata | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-abril-erratum-raw | doi:10.1128/jb.172.6.3534b.1990; references_cache/papers/primary_scans/abril-1990-20261014/page-3534.png; visually_verified_lower_correction_on_shared_page_scan | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| paper-abril-erratum-crossref_raw | doi:10.1128/jb.172.6.3534b.1990; references_cache/papers/primary_metadata/frontier-abril-1990-correction-20261014.json; visually_verified_lower_correction_on_shared_page_scan | supports | Publication identity and bounded inspected passages; not certification of the local recipe or growth. |
| taxonomy-0 | NCBI Taxonomy; references_cache/papers/taxonomy/bibliographic-url-leads-20261014.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| taxonomy-1 | NCBI Taxonomy; references_cache/papers/taxonomy/citation-frontier-20261014.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| taxonomy-2 | NCBI Taxonomy; references_cache/papers/taxonomy/citation-frontier-additional-20261014.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| taxonomy-3 | NCBI Taxonomy; references_cache/papers/taxonomy/ecoli-bl21-hb101-20261013.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| taxonomy-4 | NCBI Taxonomy; references_cache/papers/taxonomy/ecoli-species-20261013.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| taxonomy-5 | NCBI Taxonomy; references_cache/papers/taxonomy/environmental-study-candidates-20261013.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| taxonomy-6 | NCBI Taxonomy; references_cache/papers/taxonomy/growth-next-nonoperational-20261013.xml; ScientificName, Rank, synonyms and lineage | supports | Current scientific names and actual ranks; parent-only mappings remain qualified. |
| alias-primary-source-87-20261013 | Crossref publisher deposit; references_cache/papers/crossref/primary-source-87-20261013.json; Title, authors, journal, volume, issue, pages and print year | supports | Two DOI deposits identify the same Kawasumi publication. |
| alias-primary-source-87-alternate-20261013 | Crossref publisher deposit; references_cache/papers/crossref/primary-source-87-alternate-20261013.json; Title, authors, journal, volume, issue, pages and print year | supports | Two DOI deposits identify the same Kawasumi publication. |
| claims | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/claim-plan.json; claim-plan.json | context_only | Explicit owner edits, 17 registered quotes and 23 taxonomy nodes. |
| archives | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/source-preparation.json; source-preparation.json | context_only | 69 source files and access scopes for 11 publications; other alias deposits retained. |
| joins | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/prepared-sources.json; prepared-sources.json | context_only | Primary citing references and historical SQL bibliography joins. |
| readback | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/final-readback.json; final-readback.json | context_only | Only 21 intended owners changed; all prior bytes recovered from recorded patches. |
| excerpts | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/evidence-readback.json; evidence-readback.json | context_only | 38 exact excerpt occurrences and taxonomy assertions checked. |
| applied | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/applied.json; applied.json | context_only | 20 new citations, six enrichments, two verified duplicates removed; 259 ingredients preserved. |
| reference-access | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/native-check-assessment.json; native-check-assessment.json | context_only | Five unmodified baseline failures and three post-edit reference failures retained, not waived. |
| pending | Guarded curation receipt; reports/paper_citation_curation/20261014-citation-frontier-resolution/pending-frontier-v4.json; pending-frontier-v4.json | context_only | Access gaps, newly archived Hopwood scans/correction and two new base-paper abstracts leave the overall goal incomplete. |
| baseline-04 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-04.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-04.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-05 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-05.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-05.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-20 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-20.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-20.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-21 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-21.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-21.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-22 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-22.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-22.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-23 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-23.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-23.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-24 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-24.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-24.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-25 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-25.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-25.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-26 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-26.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-26.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-27 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-27.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-27.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-28 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-28.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-28.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-29 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-29.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-29.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-32 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-32.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-32.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-33 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-33.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-33.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-58 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-58.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-58.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-59 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-59.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-59.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-60 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-60.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-60.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-61 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-61.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-61.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-62 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-62.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-62.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-63 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-63.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-63.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-64 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-64.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-64.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-65 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-65.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-65.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-66 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-66.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-66.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-67 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-67.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-67.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-68 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-68.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-68.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-69 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-69.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-69.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-84 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-84.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-84.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-85 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-85.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-85.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-86 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-86.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-86.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-87 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-87.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-87.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-88 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-88.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-88.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-89 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-89.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-89.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-90 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-90.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-90.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-91 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-91.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-91.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-98 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-98.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-98.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-99 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-99.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-99.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-100 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-100.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-100.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-101 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-101.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-101.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-102 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-102.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-102.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-103 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-103.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-103.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-104 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-104.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-104.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| baseline-105 | reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-105.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-105.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-00 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-00.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-00.log; Terminal command output | context_only | Exit code 1; not scientific approval. |
| post-01 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-01.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-01.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-02 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-02.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-02.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-03 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-03.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-03.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-04 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-04.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-04.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-05 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-05.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-05.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-06 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-06.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-06.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-07 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-07.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-07.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-08 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-08.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-08.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-09 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-09.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-09.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-10 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-10.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-10.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-11 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-11.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-11.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-12 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-12.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-12.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-13 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-13.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-13.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-14 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-14.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-14.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-15 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-15.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-15.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-16 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-16.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-16.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-17 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-17.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-17.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-18 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-18.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-18.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-19 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-19.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-19.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-20 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-20.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-20.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-21 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-21.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-21.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-22 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-22.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-22.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-23 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-23.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-23.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-24 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-24.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-24.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-25 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-25.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-25.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-26 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-26.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-26.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-27 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-27.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-27.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-28 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-28.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-28.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-29 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-29.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-29.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-30 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-30.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-30.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-31 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-31.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-31.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-32 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-32.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-32.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-33 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-33.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-33.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-34 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-34.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-34.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-35 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-35.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-35.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-36 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-36.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-36.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-37 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-37.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-37.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-38 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-38.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-38.log; Terminal command output | context_only | Exit code 1; not scientific approval. |
| post-39 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-39.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-39.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| post-40 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-40.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-40.log; Terminal command output | context_only | Exit code 1; not scientific approval. |
| post-41 | reports/paper_citation_curation/20261014-citation-frontier-resolution/post-41.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/post-41.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| merge-00 | reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-00.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-00.log; Terminal command output | context_only | Exit code 1; not scientific approval. |
| merge-01 | reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-01.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-01.log; Terminal command output | context_only | Exit code 1; not scientific approval. |
| extra-00 | reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-00.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-00.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| extra-01 | reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-01.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-01.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| extra-02 | reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-02.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-02.log; Terminal command output | context_only | Exit code 0; not scientific approval. |
| fast-00 | reports/paper_citation_curation/20261014-citation-frontier-resolution/fast-test.log; reports/paper_citation_curation/20261014-citation-frontier-resolution/fast-test.log; Terminal command output | context_only | Exit code 0; not scientific approval. |

## Limits And Additional Notes

- Partial self-review, not independent review or complete scientific record approval.
- Organism inventory is limited to inspected passages; prior unaffected notes are not newly certified.
- NCBI actual ranks and parent-only mappings remain qualified; no growth inheritance from cited base papers.
- 69 source files include raw captures and Markdown with explicit access scope, not 69 papers or full texts.
- Three native reference failures are not waived. Five other baseline failures concern unmodified candidates.
- Equal global merge counts would not establish row-level equivalence or attribution.
- No generated or GitHub publication. Pending sources and further discovery leave the overall goal incomplete.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T014956Z-citation-frontier-resolution
kind: batch
repository: culturebotai/CultureMech
title: Bounded paper-citation frontier review
started_at: '2026-10-14T00:44:21Z'
finished_at: '2026-10-14T01:49:56Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Curator-performed assessment, not independent adversarial review.
skill: culturemech-add-paper-citation
completion: partial
verdict: needs_curation
scientific_review: false
summary: '20 new citations, six enrichments and two verified duplicates removed across
  21 owners; 259 ingredients preserved. Bounded identity, taxonomy and recipe-discrepancy
  notes, not full scientific approval. Affected baseline 42/42 passed; post-edit 39/42
  passed, with schema/terms/strict passing on all 21. Native URL and global merge
  failures retained. Fast-test gate exit code: 0.'
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    sha256: 681a28b2bb2cdcfe26fbfcaa01a07473d160416c0e255af178ff2816467ce0bc
    role: target
  - path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
    sha256: fe7cf4de4ae81305d23ffca99c3bf93eef5208baa0a89591d2fdf9616bed5f9e
    role: target
  - path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
    sha256: 6fefb75d7e06640ac2a0c2b1cbe1992ecba41ecd32b5fa7f22013cc0614898cc
    role: target
  - path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
    sha256: 2a14d6492826f4da98006269026be5ea301d2bf1e71e6aafa5fa3ab5e6303028
    role: target
  - path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
    sha256: ea666e770426415d3fdeeb8f3573deb99747a532335946cd6e5c731dc897ef98
    role: target
  - path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
    sha256: f4cb8f012b5c4febf4c9c8a7e442ace73cb19d4cd1dff283ba582cbd20c3f8a8
    role: target
  - path: data/normalized_yaml/bacterial/isolation_medium.yaml
    sha256: 2c0d5b06be133048ed12053ff1d0178ca50e5929f072e61a0d82bbb637b5165d
    role: target
  - path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
    sha256: c12f9d6417ebe022899d8e7687de50fb1d15804cafe93b88bf2f98fa28a3e917
    role: target
  - path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
    sha256: 7516e42c5de3f591daf3411dcdd52e02a5c110eba6463d1af124dd86a84bf1c6
    role: target
  - path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
    sha256: eac01fd756ff8e71f6799b8cfe787158288716c062205d15bdeb075027c61369
    role: target
  - path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
    sha256: 1b9e502e9410011d2a5ebe396b63f6a515eea2a627610b24916eca861e9c5348
    role: target
  - path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
    sha256: 268ca96eb214ec2e3e36416a5825b0e299c015680ead076bd25285a1de426da7
    role: target
  - path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
    sha256: e567195cc42c2762208887505627f63eb609ca14e6ba01b8011a75a9635de68f
    role: target
  - path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
    sha256: b5d954ba3fd2684cba5f4b8609f3077f5a65b67e368642a553e3ec611b1537b5
    role: target
  - path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
    sha256: 7e369500b7e73df7509dab4b2ff7ef85720b6cb96ce3578ca151e191920949b2
    role: target
  - path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
    sha256: 0291036cba7dad1250fd7ccdc4505478ecbddde082b2bde3fca14fab96e1b8e7
    role: target
  - path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
    sha256: 1d92baa867ee4534ccee5dd3c80089011d7165a073658b80ad06373fb59c209c
    role: target
  - path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
    sha256: eab628c9f2cf87df2e78703e57bd75fd9f6580e8533390bdf3859755b9c3a72e
    role: target
  - path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
    sha256: eca9d71c6fc8fc8b5a05169d6139a77bfbb4c40bc480e6c863efd62b30af8af0
    role: target
  - path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    sha256: 74a679494fc6cd28eae9776a6183f307be720e3d71b8eed5a66b64422a9e4fe8
    role: target
  - path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    sha256: 9657408916f38c591a9004c53b6c7823919eb342ff341fdc3cefff2a14a080e0
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: 21 normalized bibliography owners, including a stock solution.
  selection: Primary reference chains, verified publication aliases/corrections and
    historical MediaDB joins.
  coverage: full
  population_size: 21
  reviewed_target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  exclusions:
  - target: Full-record scientific approval, unresolved formulas and generated publication
    reason: Focused citation task; limited source access and unresolved formulation
      identities. Whitchurch experimental claims excluded.
targets:
- target_id: CultureMech:004981
  path: data/normalized_yaml/bacterial/vr_salts_b.yaml
  label: vr_salts_b
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007081
  path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  label: m9_0_2_glycerol
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007082
  path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  label: m9_0_24_pyruvate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007083
  path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  label: m9_0_45_succinate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007084
  path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  label: m9_0_27_acetate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007085
  path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  label: m9_0_4_glycerol
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007086
  path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  label: lr_0_4_glycerol
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007087
  path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  label: n_c_0_4_glycerol
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007088
  path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  label: modifed_m9_with_glucose
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007089
  path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  label: modified_m9_with_toluene
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007090
  path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  label: e2_medium_with_octanoate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007093
  path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  label: e2_medium_with_gluconate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007094
  path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  label: e2_medium_with_citrate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007150
  path: data/normalized_yaml/bacterial/isolation_medium.yaml
  label: isolation_medium
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/isolation_medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007220
  path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  label: mr_medium_d_fructose
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007261
  path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  label: minimal_medium_whitchurch_et_al
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007293
  path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  label: defined_freshwater_medium_coso4
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007294
  path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  label: defined_freshwater_medium_cocl2
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007295
  path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  label: nitrogen_limited_mr_medium
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:008841
  path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  label: artificial_seawater_base_with_thiosulfate_as_the_electron_donor
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:009406
  path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
  label: pye_solid_medium
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-04
  name: just validate data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  command: just validate data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - baseline-04
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-05
  name: just validate-strict data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  command: just validate-strict data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - baseline-05
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-20
  name: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  command: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - baseline-20
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-21
  name: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  command: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - baseline-21
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-22
  name: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  command: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - baseline-22
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-23
  name: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  command: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - baseline-23
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-24
  name: just validate data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  command: just validate data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - baseline-24
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-25
  name: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - baseline-25
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-26
  name: just validate data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  command: just validate data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - baseline-26
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-27
  name: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - baseline-27
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-28
  name: just validate data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  command: just validate data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - baseline-28
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-29
  name: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - baseline-29
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-32
  name: just validate data/normalized_yaml/bacterial/isolation_medium.yaml
  command: just validate data/normalized_yaml/bacterial/isolation_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - baseline-32
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-33
  name: just validate-strict data/normalized_yaml/bacterial/isolation_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/isolation_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - baseline-33
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-58
  name: just validate data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - baseline-58
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-59
  name: just validate-strict data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - baseline-59
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-60
  name: just validate data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - baseline-60
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-61
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - baseline-61
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-62
  name: just validate data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - baseline-62
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-63
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - baseline-63
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-64
  name: just validate data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - baseline-64
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-65
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - baseline-65
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-66
  name: just validate data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - baseline-66
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-67
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - baseline-67
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-68
  name: just validate data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - baseline-68
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-69
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - baseline-69
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-84
  name: just validate data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  command: just validate data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - baseline-84
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-85
  name: just validate-strict data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  command: just validate-strict data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - baseline-85
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-86
  name: just validate data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - baseline-86
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-87
  name: just validate-strict data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - baseline-87
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-88
  name: just validate data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  command: just validate data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - baseline-88
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-89
  name: just validate-strict data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  command: just validate-strict data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - baseline-89
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-90
  name: just validate data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  command: just validate data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - baseline-90
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-91
  name: just validate-strict data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - baseline-91
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-98
  name: just validate data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - baseline-98
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-99
  name: just validate-strict data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - baseline-99
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-100
  name: just validate data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  command: just validate data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - baseline-100
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-101
  name: just validate-strict data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - baseline-101
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-102
  name: just validate data/normalized_yaml/bacterial/pye_solid_medium.yaml
  command: just validate data/normalized_yaml/bacterial/pye_solid_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - baseline-102
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-103
  name: just validate-strict data/normalized_yaml/bacterial/pye_solid_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/pye_solid_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - baseline-103
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-104
  name: just validate data/normalized_yaml/bacterial/vr_salts_b.yaml
  command: just validate data/normalized_yaml/bacterial/vr_salts_b.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - baseline-104
  summary: Actual required-check outcome retained; no waiver.
- check_id: baseline-105
  name: just validate-strict data/normalized_yaml/bacterial/vr_salts_b.yaml
  command: just validate-strict data/normalized_yaml/bacterial/vr_salts_b.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - baseline-105
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-00
  name: just validate data/normalized_yaml/bacterial/vr_salts_b.yaml
  command: just validate data/normalized_yaml/bacterial/vr_salts_b.yaml
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - post-00
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-01
  name: just validate-strict data/normalized_yaml/bacterial/vr_salts_b.yaml
  command: just validate-strict data/normalized_yaml/bacterial/vr_salts_b.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - post-01
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-02
  name: just validate data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - post-02
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-03
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - post-03
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-04
  name: just validate data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - post-04
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-05
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - post-05
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-06
  name: just validate data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - post-06
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-07
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - post-07
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-08
  name: just validate data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - post-08
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-09
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - post-09
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-10
  name: just validate data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - post-10
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-11
  name: just validate-strict data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - post-11
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-12
  name: just validate data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - post-12
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-13
  name: just validate-strict data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - post-13
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-14
  name: just validate data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  command: just validate data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - post-14
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-15
  name: just validate-strict data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  command: just validate-strict data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - post-15
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-16
  name: just validate data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - post-16
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-17
  name: just validate-strict data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - post-17
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-18
  name: just validate data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  command: just validate data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - post-18
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-19
  name: just validate-strict data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  command: just validate-strict data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - post-19
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-20
  name: just validate data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  command: just validate data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - post-20
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-21
  name: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - post-21
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-22
  name: just validate data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  command: just validate data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - post-22
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-23
  name: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - post-23
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-24
  name: just validate data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  command: just validate data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - post-24
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-25
  name: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - post-25
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-26
  name: just validate data/normalized_yaml/bacterial/isolation_medium.yaml
  command: just validate data/normalized_yaml/bacterial/isolation_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - post-26
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-27
  name: just validate-strict data/normalized_yaml/bacterial/isolation_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/isolation_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - post-27
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-28
  name: just validate data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  command: just validate data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - post-28
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-29
  name: just validate-strict data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - post-29
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-30
  name: just validate data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  command: just validate data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - post-30
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-31
  name: just validate-strict data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  command: just validate-strict data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - post-31
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-32
  name: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  command: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - post-32
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-33
  name: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  command: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - post-33
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-34
  name: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  command: just validate data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - post-34
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-35
  name: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  command: just validate-strict data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - post-35
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-36
  name: just validate data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  command: just validate data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - post-36
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-37
  name: just validate-strict data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - post-37
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-38
  name: just validate data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  command: just validate data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - post-38
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-39
  name: just validate-strict data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  command: just validate-strict data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - post-39
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-40
  name: just validate data/normalized_yaml/bacterial/pye_solid_medium.yaml
  command: just validate data/normalized_yaml/bacterial/pye_solid_medium.yaml
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - post-40
  summary: Actual required-check outcome retained; no waiver.
- check_id: post-41
  name: just validate-strict data/normalized_yaml/bacterial/pye_solid_medium.yaml
  command: just validate-strict data/normalized_yaml/bacterial/pye_solid_medium.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - post-41
  summary: Actual required-check outcome retained; no waiver.
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  evidence_ids:
  - merge-00
  summary: Actual required-check outcome retained; no waiver.
- check_id: merge-01
  name: just audit-merge-freshness
  command: just audit-merge-freshness
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  evidence_ids:
  - merge-01
  summary: Actual required-check outcome retained; no waiver.
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  evidence_ids:
  - extra-00
  summary: Actual required-check outcome retained; no waiver.
- check_id: extra-01
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  evidence_ids:
  - extra-01
  summary: Actual required-check outcome retained; no waiver.
- check_id: extra-02
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-citation-frontier-resolution/curate.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-citation-frontier-resolution/curate.py
    --apply
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  evidence_ids:
  - extra-02
  summary: Actual required-check outcome retained; no waiver.
- check_id: fast-00
  name: just test-fast
  command: just test-fast
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  evidence_ids:
  - fast-00
  summary: Actual required-check outcome retained; no waiver.
evidence:
- evidence_id: paper-8387263-raw
  kind: primary_source
  reference: PMID:8387263
  locator: references_cache/papers/PMID_8387263.xml; PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 733c5c887780b85bcf0d0aeac38d6bd36110743abfcac78bc1e968b5f572279d
- evidence_id: paper-11135197-raw
  kind: primary_source
  reference: PMID:11135197
  locator: references_cache/papers/PMID_11135197.xml; PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 6354142afb7130c9ba3d2f89ed47e7431225d2227425f379390a27ca2fa06ba6
- evidence_id: paper-11135197-crossref_raw
  kind: primary_source
  reference: PMID:11135197
  locator: references_cache/papers/primary_metadata/frontier-durner-2001-20261014.json;
    PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 7920e044210ce51909f5b3d0f27c6b116c1962e813fc338772c7c4d79da3fa23
- evidence_id: paper-2687253-raw
  kind: primary_source
  reference: PMID:2687253
  locator: references_cache/papers/PMID_2687253.xml; PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 78d45796edfac158533763f6663527f2c3de4a87a944b08f1bdf6ce563df6fbb
- evidence_id: paper-16461683-raw
  kind: primary_source
  reference: PMID:16461683
  locator: references_cache/papers/PMID_16461683.xml; PubMed_abstract_and_selected_primary_full_HTML_methods
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: acc8e7e69d11c5a093094b15c92dbde8326ed03fa67ddad21048548839c85272
- evidence_id: paper-16461683-full_raw
  kind: primary_source
  reference: PMID:16461683
  locator: references_cache/papers/primary_html/frontier-mc1-2006-20261014.html; PubMed_abstract_and_selected_primary_full_HTML_methods
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 22b31d804795c3c466f8818aa1e64b8f0420ab02b7a41c13819790ef00da5d3e
- evidence_id: paper-20472802-raw
  kind: primary_source
  reference: PMID:20472802
  locator: references_cache/papers/PMID_20472802.xml; PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: c7b25fa861903f5e287f264ff27ebb12a94d5952620fce9508175fd02a3e2092
- evidence_id: paper-5784223-raw
  kind: primary_source
  reference: PMID:5784223
  locator: references_cache/papers/PMID_5784223.xml; PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 4cf3f84ef7c5f7a2f440d790f6acf29d3617fc199b9bc76f9bb4662f3b44fce2
- evidence_id: paper-11859186-raw
  kind: primary_source
  reference: PMID:11859186
  locator: references_cache/papers/PMID_11859186.xml; author_posted_article_text_archived_with_bounded_markdown_summary
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 8271f3d116dfe046bb0a8516a0bc8ed18abdb2c070ef6c83d6b493bb20bf35d8
- evidence_id: paper-11859186-author_text
  kind: primary_source
  reference: PMID:11859186
  locator: references_cache/papers/primary_browser/bibliographic-whitchurch-2002-20261013.web.txt;
    author_posted_article_text_archived_with_bounded_markdown_summary
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: f7d0aa9d260e795a7b7e57522111f478ecaa3a17d468dd6987524a9de9e45021
- evidence_id: paper-22581902-raw
  kind: primary_source
  reference: PMID:22581902
  locator: references_cache/papers/PMID_22581902.xml; PubMed_abstract_not_full_text
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 87ed6d7c2cbed944f8f38a219d0e0a0036b13748dc27e74b8f8fe0cd192df065
- evidence_id: paper-lee-raw
  kind: primary_source
  reference: doi:10.1007/BF02074874
  locator: references_cache/papers/primary_html/lee-1996-mr-base-20261013.html; publisher_abstract_preview
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: c88805ff63d3cc309cf9aa970824e88db5d8fd3db618310a19af1d3a730329e8
- evidence_id: paper-paliy-erratum-raw
  kind: primary_source
  reference: doi:10.1007/s00253-006-0683-0
  locator: references_cache/papers/primary_html/paliy-2006-erratum.html; publisher_erratum_body_and_metadata
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 7c45cb40cb1408273feac72a78e2e7799f22a0ca6c8c60fb7e61702e41c4481d
- evidence_id: paper-abril-erratum-raw
  kind: primary_source
  reference: doi:10.1128/jb.172.6.3534b.1990
  locator: references_cache/papers/primary_scans/abril-1990-20261014/page-3534.png;
    visually_verified_lower_correction_on_shared_page_scan
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: ecbf02e2757fa5be8f17fc34c4f3dc55e3afc86c49c9988def3c53bb9c55140e
- evidence_id: paper-abril-erratum-crossref_raw
  kind: primary_source
  reference: doi:10.1128/jb.172.6.3534b.1990
  locator: references_cache/papers/primary_metadata/frontier-abril-1990-correction-20261014.json;
    visually_verified_lower_correction_on_shared_page_scan
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Publication identity and bounded inspected passages; not certification
    of the local recipe or growth.
  support: supports
  snapshot_sha256: 4eda00122db6baf8b1b0eaace225bd9c566c5c5054ce434616dca6c04b15d336
- evidence_id: taxonomy-0
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/bibliographic-url-leads-20261014.xml;
    ScientificName, Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: d79b85f72f961d88947f7521939e4c5f3d69a848ca37d40d4e33d04904382e8f
- evidence_id: taxonomy-1
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/citation-frontier-20261014.xml; ScientificName,
    Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: 50cce5e880453611c0f4ffc07bf85de704752b990f4a338b02e535e44743dfa9
- evidence_id: taxonomy-2
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/citation-frontier-additional-20261014.xml;
    ScientificName, Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: c198b84c16ace9fd649d5c5aed56ade957d125c71ac0b491c831e0b6c9d9901b
- evidence_id: taxonomy-3
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/ecoli-bl21-hb101-20261013.xml; ScientificName,
    Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: aea6f829aba68717f5222095e73ca36b0e21517c6bac01e8afb7d07f6f89ddcb
- evidence_id: taxonomy-4
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/ecoli-species-20261013.xml; ScientificName,
    Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: 1d5618066f7d7b5fbf62b33b00b8928382362d9b9e017076caeb654151d980f8
- evidence_id: taxonomy-5
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/environmental-study-candidates-20261013.xml;
    ScientificName, Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: dce401ba739ffa8df63303da23203de94951c01649f26b47214080539a2629b0
- evidence_id: taxonomy-6
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/growth-next-nonoperational-20261013.xml;
    ScientificName, Rank, synonyms and lineage
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Current scientific names and actual ranks; parent-only mappings remain
    qualified.
  support: supports
  snapshot_sha256: e04e8849f8d562b081edfd1bef6a2bdbb44851f5370bf71139f6869fa3c1689c
- evidence_id: alias-primary-source-87-20261013
  kind: primary_source
  reference: Crossref publisher deposit
  locator: references_cache/papers/crossref/primary-source-87-20261013.json; Title,
    authors, journal, volume, issue, pages and print year
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Two DOI deposits identify the same Kawasumi publication.
  support: supports
  snapshot_sha256: 6126e90f534c700a1aba7c3fc8f05dd599c8894b791e907cb0350c9e9f2a2e99
- evidence_id: alias-primary-source-87-alternate-20261013
  kind: primary_source
  reference: Crossref publisher deposit
  locator: references_cache/papers/crossref/primary-source-87-alternate-20261013.json;
    Title, authors, journal, volume, issue, pages and print year
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Two DOI deposits identify the same Kawasumi publication.
  support: supports
  snapshot_sha256: 37275d1481d2f14aa6b55d75a95640ac2c4f5a9e7492e8baa8e0ebf181adbd27
- evidence_id: claims
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/claim-plan.json;
    claim-plan.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Explicit owner edits, 17 registered quotes and 23 taxonomy nodes.
  support: context_only
  snapshot_sha256: a82080e2814f79a227ae43c8a3223b3ca8eb66b9e0f1d28b95822d9c9a770e92
- evidence_id: archives
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/source-preparation.json;
    source-preparation.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: 69 source files and access scopes for 11 publications; other alias deposits
    retained.
  support: context_only
  snapshot_sha256: 11a4f66115313b375589ed0fbd9b47c25c8075ba85d65d769b663bc14fe9de86
- evidence_id: joins
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/prepared-sources.json;
    prepared-sources.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Primary citing references and historical SQL bibliography joins.
  support: context_only
  snapshot_sha256: c9a3563b947be45f5d343269199e1092b31557ead1d696fd104d12cdc66f6560
- evidence_id: readback
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/final-readback.json;
    final-readback.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Only 21 intended owners changed; all prior bytes recovered from recorded
    patches.
  support: context_only
  snapshot_sha256: 860d4a0dbec997ed64386889cbbd05b5b6c381102689e03874ae721b3b1e6e98
- evidence_id: excerpts
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/evidence-readback.json;
    evidence-readback.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: 38 exact excerpt occurrences and taxonomy assertions checked.
  support: context_only
  snapshot_sha256: 4326030a5f160ad9a7ccbf650bade0a0e3825be65c58022fc87d750fd0c53db0
- evidence_id: applied
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/applied.json;
    applied.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: 20 new citations, six enrichments, two verified duplicates removed; 259
    ingredients preserved.
  support: context_only
  snapshot_sha256: 94f7de40c5f1609f74f221bc0ce85ff6b5c9430504717c760163495912ae5ea0
- evidence_id: reference-access
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/native-check-assessment.json;
    native-check-assessment.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Five unmodified baseline failures and three post-edit reference failures
    retained, not waived.
  support: context_only
  snapshot_sha256: b6ff33fb01d6879aa42ac28b69ecaa5607dfe026de0a378858569fcab4649408
- evidence_id: pending
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/pending-frontier-v4.json;
    pending-frontier-v4.json
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Access gaps, newly archived Hopwood scans/correction and two new base-paper
    abstracts leave the overall goal incomplete.
  support: context_only
  snapshot_sha256: e92f66ac299213b138bc65287071e982d203fe2dca7ed3921821f7d7b75f6d3a
- evidence_id: baseline-04
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-04.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-04.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-05
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-05.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-05.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-20
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-20.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-20.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-21
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-21.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-21.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-22
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-22.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-22.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-23
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-23.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-23.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-24
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-24.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-24.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-25
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-25.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-25.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-26
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-26.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-26.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-27
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-27.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-27.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-28
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-28.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-28.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-29
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-29.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-29.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-32
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-32.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-32.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: baseline-33
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-33.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-33.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-58
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-58.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-58.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: baseline-59
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-59.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-59.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-60
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-60.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-60.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-61
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-61.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-61.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-62
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-62.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-62.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-63
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-63.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-63.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-64
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-64.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-64.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-65
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-65.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-65.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-66
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-66.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-66.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-67
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-67.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-67.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-68
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-68.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-68.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-69
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-69.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-69.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-84
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-84.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-84.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-85
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-85.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-85.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-86
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-86.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-86.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-87
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-87.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-87.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-88
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-88.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-88.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-89
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-89.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-89.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-90
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-90.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-90.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-91
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-91.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-91.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-98
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-98.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-98.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: baseline-99
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-99.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-99.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-100
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-100.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-100.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: baseline-101
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-101.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-101.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-102
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-102.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-102.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-103
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-103.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-103.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-104
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-104.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-104.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-105
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-105.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/baseline-105.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-00.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-00.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: f72d14fcef61e07caf2c5238864bb694f3aab137d407325c8da7756c8ec9813b
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-01.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-01.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-02.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-02.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-03.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-03.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-04
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-04.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-04.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-05
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-05.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-05.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-06
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-06.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-06.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-07
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-07.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-07.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-08
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-08.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-08.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-09
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-09.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-09.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-10
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-10.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-10.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-11
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-11.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-11.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-12
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-12.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-12.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: post-13
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-13.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-13.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-14
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-14.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-14.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 97210591a6bbc8db2524eff3b29c93c1400c4f52c99a24862ed2904238d9606d
- evidence_id: post-15
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-15.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-15.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-16
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-16.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-16.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: post-17
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-17.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-17.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-18
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-18.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-18.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: post-19
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-19.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-19.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-20
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-20.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-20.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-21
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-21.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-21.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-22
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-22.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-22.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-23
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-23.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-23.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-24
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-24.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-24.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-25
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-25.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-25.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-26
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-26.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-26.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: post-27
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-27.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-27.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-28
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-28.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-28.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-29
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-29.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-29.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-30
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-30.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-30.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 0a17e57921aaa892f17d530716a1d18d9c62576b0a0b41caff18b955cf84c818
- evidence_id: post-31
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-31.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-31.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-32
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-32.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-32.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-33
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-33.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-33.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-34
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-34.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-34.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-35
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-35.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-35.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-36
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-36.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-36.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: d795cd0f45d74ecbb50c5710adb49b2df66105da344aa71db38645c49a310c0d
- evidence_id: post-37
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-37.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-37.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-38
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-38.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-38.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 8065573d80f9cc7758a4073e2d3ccc3af7138e7d54e99d204514dfd87ea8caa2
- evidence_id: post-39
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-39.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-39.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-40
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-40.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-40.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 0ebf6c163d5c9cbd9f079f583cf637c2131617ab645dc2281d7028752fe2224d
- evidence_id: post-41
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-41.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/post-41.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-00.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-00.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-01.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/merge-01.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 1b19884870fd9db7c5918d1a225e98c0f51860c5b4a9405a0ab32837aa23f75e
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-00.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-00.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-01.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-01.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-02.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/extra-02.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 347d82f9e9389760da40073f645a2e319b8d4451598264c6c343c3259334aa9e
- evidence_id: fast-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-citation-frontier-resolution/fast-test.log
  locator: reports/paper_citation_curation/20261014-citation-frontier-resolution/fast-test.log;
    Terminal command output
  accessed_at: '2026-10-14T01:49:56Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: a49569c5d363caefa0e59c64193df8154643a5156c453a1af56d1a5c297fcaba
assessments:
- assessment_id: citation-004981
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - paper-5784223-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-004981
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - paper-5784223-raw
  - claims
  - pending
  summary: VR salts B remains a stock SOLUTION; abstract does not enumerate the stock
    or prove growth on the stock alone.
- assessment_id: organism-004981
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - paper-5784223-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Acidaminococcus fermentans; canonical scientific
    name=Acidaminococcus fermentans; NCBITaxon:905; actual rank=species; taxonomy_match=exact_species;
    role=species studied, not growth on an isolated stock solution. Reported organism/group=Acidaminococcus;
    canonical scientific name=Acidaminococcus; NCBITaxon:904; actual rank=genus; taxonomy_match=exact_genus;
    role=taxonomic description/comparison, not a genus-wide cultivation assertion.
    Reported organism/group=Veillonella; canonical scientific name=Veillonella; NCBITaxon:29465;
    actual rank=genus; taxonomy_match=exact_genus; role=taxonomic description/comparison,
    not a genus-wide cultivation assertion. Reported organism/group=Peptococcus; canonical
    scientific name=Peptococcus; NCBITaxon:2740; actual rank=genus; taxonomy_match=exact_genus;
    role=taxonomic description/comparison, not a genus-wide cultivation assertion.
    No new growth associations.
- assessment_id: preservation-004981
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:004981
  evidence_ids:
  - readback
  - applied
  summary: 0 new citations; 1 enrichments; 1 verified duplicate removals. 13 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007081
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007081
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007081
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007081
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007081
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007082
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007082
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007082
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007082
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007082
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007083
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007083
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007083
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007083
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007083
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007084
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007084
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007084
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007084
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007084
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007085
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007085
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007085
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007085
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007085
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 7 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007086
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007086
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007086
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007086
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007086
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 6 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007087
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - paper-paliy-erratum-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007087
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - paper-paliy-erratum-raw
  - claims
  - pending
  summary: Author-order correction only; conflicting main-article versus erratum author
    order retained. No recipe change follows.
- assessment_id: organism-007087
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - paper-paliy-erratum-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli BL21; canonical scientific name=Escherichia
    coli BL21; NCBITaxon:511693; actual rank=strain; taxonomy_match=verified_title_strain;
    role=organism in the corrected article title, not a new growth experiment. No
    new growth associations.
- assessment_id: preservation-007087
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007087
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 6 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007088
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - paper-2687253-raw
  - paper-abril-erratum-raw
  - paper-abril-erratum-crossref_raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007088
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - paper-2687253-raw
  - paper-abril-erratum-raw
  - paper-abril-erratum-crossref_raw
  - claims
  - pending
  summary: Cited M9 base abstract lacks a complete recipe; historical B13 and its
    engineered clone are not the current KT2440 owner. Visually verified lower correction
    concerns substrate naming and assay reporting, not M9 concentrations. Upper notice/PMID
    excluded. Only prior unresolved-correction wording updated; other prior Nogales
    claims and taxa not re-reviewed.
- assessment_id: organism-007088
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - paper-2687253-raw
  - paper-abril-erratum-raw
  - paper-abril-erratum-crossref_raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Pseudomonas sp. strain B13 and its TOL-plasmid-bearing
    clone; canonical scientific name=Pseudomonas knackmussii B13; NCBITaxon:1301098;
    actual rank=strain; taxonomy_match=verified_B13_synonym_with_derivative_parent_only;
    role=historical base strain; exact engineered clone identity not asserted. No
    new growth associations.
- assessment_id: preservation-007088
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007088
  evidence_ids:
  - readback
  - applied
  summary: 2 new citations; 1 enrichments; 0 verified duplicate removals. 13 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007089
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - paper-2687253-raw
  - paper-abril-erratum-raw
  - paper-abril-erratum-crossref_raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007089
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - paper-2687253-raw
  - paper-abril-erratum-raw
  - paper-abril-erratum-crossref_raw
  - claims
  - pending
  summary: Cited M9 base abstract lacks a complete recipe; historical B13 and its
    engineered clone are not the current KT2440 owner. Visually verified lower correction
    concerns substrate naming and assay reporting, not M9 concentrations. Upper notice/PMID
    excluded. Only prior unresolved-correction wording updated; other prior Nogales
    claims and taxa not re-reviewed.
- assessment_id: organism-007089
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - paper-2687253-raw
  - paper-abril-erratum-raw
  - paper-abril-erratum-crossref_raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Pseudomonas sp. strain B13 and its TOL-plasmid-bearing
    clone; canonical scientific name=Pseudomonas knackmussii B13; NCBITaxon:1301098;
    actual rank=strain; taxonomy_match=verified_B13_synonym_with_derivative_parent_only;
    role=historical base strain; exact engineered clone identity not asserted. No
    new growth associations.
- assessment_id: preservation-007089
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007089
  evidence_ids:
  - readback
  - applied
  summary: 2 new citations; 1 enrichments; 0 verified duplicate removals. 13 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007090
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007090
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - claims
  - pending
  summary: E2 base abstract lacks complete salts/stocks; historical ATCC strain identity
    remains genus-only, distinct from the citing study strains.
- assessment_id: organism-007090
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Pseudomonas oleovorans ATCC 29347 (historical name);
    canonical scientific name=Pseudomonas; NCBITaxon:286; actual rank=genus; taxonomy_match=parent_rank_only;
    role=base-paper study strain; current species identity unresolved. No new growth
    associations.
- assessment_id: preservation-007090
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007090
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 11 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007093
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007093
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - claims
  - pending
  summary: E2 base abstract lacks complete salts/stocks; historical ATCC strain identity
    remains genus-only, distinct from the citing study strains.
- assessment_id: organism-007093
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Pseudomonas oleovorans ATCC 29347 (historical name);
    canonical scientific name=Pseudomonas; NCBITaxon:286; actual rank=genus; taxonomy_match=parent_rank_only;
    role=base-paper study strain; current species identity unresolved. No new growth
    associations.
- assessment_id: preservation-007093
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007093
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 11 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007094
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007094
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - claims
  - pending
  summary: E2 base abstract lacks complete salts/stocks; historical ATCC strain identity
    remains genus-only, distinct from the citing study strains.
- assessment_id: organism-007094
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - paper-11135197-raw
  - paper-11135197-crossref_raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Pseudomonas oleovorans ATCC 29347 (historical name);
    canonical scientific name=Pseudomonas; NCBITaxon:286; actual rank=genus; taxonomy_match=parent_rank_only;
    role=base-paper study strain; current species identity unresolved. No new growth
    associations.
- assessment_id: preservation-007094
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007094
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 11 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007150
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - alias-primary-source-87-20261013
  - alias-primary-source-87-alternate-20261013
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007150
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - alias-primary-source-87-20261013
  - alias-primary-source-87-alternate-20261013
  - claims
  - pending
  summary: Bibliographic DOI equivalence only; pre-existing recipe and organism claims
    not re-reviewed.
- assessment_id: organism-007150
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - alias-primary-source-87-20261013
  - alias-primary-source-87-alternate-20261013
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: No new organism mapping in this alias-only edit; prior taxonomy claims
    are not re-reviewed. No new growth associations.
- assessment_id: preservation-007150
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007150
  evidence_ids:
  - readback
  - applied
  summary: 0 new citations; 1 enrichments; 0 verified duplicate removals. 13 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007220
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - paper-lee-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007220
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - paper-lee-raw
  - claims
  - pending
  summary: MR base abstract lacks a complete formula; recombinant E. coli results
    are not transferred to the current Cupriavidus owners.
- assessment_id: organism-007220
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - paper-lee-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli XL1-Blue carrying pSYL105 or pSYL107;
    canonical scientific name=Escherichia coli; NCBITaxon:562; actual rank=species;
    taxonomy_match=parent_rank_only; role=two distinct recombinant derivatives; exact
    strain/derivative nodes unresolved. Reported organism/group=Alcaligenes eutrophus;
    canonical scientific name=Cupriavidus necator; NCBITaxon:106590; actual rank=species;
    taxonomy_match=verified_species_synonym; role=gene source, not proof that the
    donor grew in these E. coli assays. No new growth associations.
- assessment_id: preservation-007220
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007220
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 12 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007261
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - paper-11859186-raw
  - paper-11859186-author_text
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007261
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - paper-11859186-raw
  - paper-11859186-author_text
  - claims
  - pending
  summary: Non-operational publication and organism identity only; no experimental,
    cultivation, biofilm or virulence curation.
- assessment_id: organism-007261
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - paper-11859186-raw
  - paper-11859186-author_text
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Pseudomonas aeruginosa; canonical scientific name=Pseudomonas
    aeruginosa; NCBITaxon:287; actual rank=species; taxonomy_match=verified_species_name;
    role=organism mention only; no strain-specific or cultivation assertion. Reported
    organism/group=Pseudomonas aeruginosa PAO1; canonical scientific name=Pseudomonas
    aeruginosa PAO1; NCBITaxon:208964; actual rank=strain; taxonomy_match=verified_strain_name;
    role=identity mention only; no experimental assertion. No new growth associations.
- assessment_id: preservation-007261
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007261
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 16 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007293
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - paper-8387263-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007293
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - paper-8387263-raw
  - claims
  - pending
  summary: Base-protocol abstract does not enumerate the freshwater formula; cobalt
    alternatives and combined assay contexts remain unresolved.
- assessment_id: organism-007293
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - paper-8387263-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Geobacter metallireducens GS-15; canonical scientific
    name=Geobacter metallireducens GS-15; NCBITaxon:269799; actual rank=strain; taxonomy_match=verified_named_strain;
    role=organism characterized in the cited base paper, not the current Rhodoferax
    study. Reported organism/group=Desulfuromonas acetoxidans; canonical scientific
    name=Desulfuromonas acetoxidans; NCBITaxon:891; actual rank=species; taxonomy_match=exact_species;
    role=phylogenetic comparator, not cultivation on this owner. No new growth associations.
- assessment_id: preservation-007293
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007293
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 39 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007294
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - paper-8387263-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007294
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - paper-8387263-raw
  - claims
  - pending
  summary: Base-protocol abstract does not enumerate the freshwater formula; cobalt
    alternatives and combined assay contexts remain unresolved.
- assessment_id: organism-007294
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - paper-8387263-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Geobacter metallireducens GS-15; canonical scientific
    name=Geobacter metallireducens GS-15; NCBITaxon:269799; actual rank=strain; taxonomy_match=verified_named_strain;
    role=organism characterized in the cited base paper, not the current Rhodoferax
    study. Reported organism/group=Desulfuromonas acetoxidans; canonical scientific
    name=Desulfuromonas acetoxidans; NCBITaxon:891; actual rank=species; taxonomy_match=exact_species;
    role=phylogenetic comparator, not cultivation on this owner. No new growth associations.
- assessment_id: preservation-007294
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007294
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 39 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-007295
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - paper-lee-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-007295
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - paper-lee-raw
  - claims
  - pending
  summary: MR base abstract lacks a complete formula; recombinant E. coli results
    are not transferred to the current Cupriavidus owners.
- assessment_id: organism-007295
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - paper-lee-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Escherichia coli XL1-Blue carrying pSYL105 or pSYL107;
    canonical scientific name=Escherichia coli; NCBITaxon:562; actual rank=species;
    taxonomy_match=parent_rank_only; role=two distinct recombinant derivatives; exact
    strain/derivative nodes unresolved. Reported organism/group=Alcaligenes eutrophus;
    canonical scientific name=Cupriavidus necator; NCBITaxon:106590; actual rank=species;
    taxonomy_match=verified_species_synonym; role=gene source, not proof that the
    donor grew in these E. coli assays. No new growth associations.
- assessment_id: preservation-007295
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:007295
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 0 enrichments; 0 verified duplicate removals. 13 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-008841
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - paper-16461683-raw
  - paper-16461683-full_raw
  - paper-22581902-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-008841
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - paper-16461683-raw
  - paper-16461683-full_raw
  - paper-22581902-raw
  - claims
  - pending
  summary: Separate liquid and semisolid assays retained. Local aggregated seawater
    may hide components; cited bases/stocks remain unresolved, not an exact variant.
    Species description supports historical MC-1 identity, not exact-recipe growth
    or stock composition.
- assessment_id: organism-008841
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - paper-16461683-raw
  - paper-16461683-full_raw
  - paper-22581902-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Magnetococcus marinus MC-1(T); canonical scientific
    name=Magnetococcus marinus MC-1; NCBITaxon:156889; actual rank=strain; taxonomy_match=verified_type_strain_lineage;
    role=identity reconciliation for historical MC-1, not new exact-recipe growth.
    Reported organism/group=Magnetococcus marinus; canonical scientific name=Magnetococcus
    marinus; NCBITaxon:1124597; actual rank=species; taxonomy_match=exact_species;
    role=species described. Reported organism/group=Magnetococcus; canonical scientific
    name=Magnetococcus; NCBITaxon:162171; actual rank=genus; taxonomy_match=exact_named_group;
    role=taxonomic placement discussed, not a group-wide growth assertion. Reported
    organism/group=Magnetococcaceae; canonical scientific name=Magnetococcaceae; NCBITaxon:1191479;
    actual rank=family; taxonomy_match=exact_named_group; role=taxonomic placement
    discussed, not a group-wide growth assertion. Reported organism/group=Magnetococcales;
    canonical scientific name=Magnetococcales; NCBITaxon:1191478; actual rank=order;
    taxonomy_match=exact_named_group; role=taxonomic placement discussed, not a group-wide
    growth assertion. Reported organism/group=Alphaproteobacteria; canonical scientific
    name=Alphaproteobacteria; NCBITaxon:28211; actual rank=class; taxonomy_match=exact_named_group;
    role=taxonomic placement discussed, not a group-wide growth assertion. Reported
    organism/group=marine magnetotactic coccus strain MC-1; canonical scientific name=Magnetococcus
    marinus MC-1; NCBITaxon:156889; actual rank=strain; taxonomy_match=historical_strain_identity_supported_by_2013_species_description;
    role=primary study organism. Reported organism/group=Chlorobaculum tepidum; canonical
    scientific name=Chlorobaculum tepidum; NCBITaxon:1097; actual rank=species; taxonomy_match=exact_species;
    role=separate comparator culture, not growth on the MC-1 owner. Reported organism/group=Rhodospirillum
    rubrum; canonical scientific name=Rhodospirillum rubrum; NCBITaxon:1085; actual
    rank=species; taxonomy_match=exact_species; role=separate comparator culture,
    not growth on the MC-1 owner. No new growth associations.
- assessment_id: preservation-008841
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:008841
  evidence_ids:
  - readback
  - applied
  summary: 1 new citations; 1 enrichments; 0 verified duplicate removals. 3 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
- assessment_id: citation-009406
  area: evidence
  topic: Publication identity and provenance
  outcome: supported
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - paper-20472802-raw
  - archives
  - joins
  - readback
  summary: Verified identity and access scope; aliases and distinct correction notices
    accounted for.
- assessment_id: scope-009406
  area: evidence
  topic: Exact formulation and claim boundary
  outcome: unknown
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - paper-20472802-raw
  - claims
  - pending
  summary: PYE abstract distinguishes CB15 and NA1000 but does not resolve solid/liquid
    recipe assignment. Background mention is not growth evidence.
- assessment_id: organism-009406
  area: evidence
  topic: Bounded scientific-name and rank assessment
  outcome: supported
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - paper-20472802-raw
  - taxonomy-0
  - taxonomy-1
  - taxonomy-2
  - taxonomy-3
  - taxonomy-4
  - taxonomy-5
  - taxonomy-6
  - claims
  - excerpts
  summary: Reported organism/group=Caulobacter crescentus CB15; canonical scientific
    name=Caulobacter vibrioides; NCBITaxon:155892; actual rank=species; taxonomy_match=parent_rank_only;
    role=named study strain; current species synonym verified but exact strain node
    not assigned. Reported organism/group=Caulobacter crescentus NA1000; canonical
    scientific name=Caulobacter vibrioides; NCBITaxon:155892; actual rank=species;
    taxonomy_match=parent_rank_only; role=distinct laboratory derivative, not interchangeable
    with CB15. Reported organism/group=Pseudomonas aeruginosa; canonical scientific
    name=Pseudomonas aeruginosa; NCBITaxon:287; actual rank=species; taxonomy_match=exact_species;
    role=abstract background comparator only; no experimental or growth claim curated.
    No new growth associations.
- assessment_id: preservation-009406
  area: evidence
  topic: Mutation and export boundary
  outcome: supported
  target_ids:
  - CultureMech:009406
  evidence_ids:
  - readback
  - applied
  summary: 0 new citations; 1 enrichments; 1 verified duplicate removals. 5 prior
    ingredients preserved; one appended history event. No new growth, quantity, resolved
    variant or generated publication.
findings:
- finding_id: merge-gates
  issue_key: citation-frontier-merge-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repository-wide merge verification and freshness gates failed
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  description: Global diagnostics are not attributed to the bibliography edits; generated
    outputs were not published.
  evidence_ids:
  - merge-00
  - merge-01
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/isolation_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
- finding_id: native-url-checks
  issue_key: citation-frontier-native-url-checks
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Three native URL reference checks failed
  target_ids:
  - CultureMech:004981
  - CultureMech:008841
  - CultureMech:009406
  description: Two PMC document titles include a site suffix; one ordinary DOI-URL
    request returned HTTP 403. Independently archived publication identity supports
    the retained article titles but does not turn these failed checks into passes.
  evidence_ids:
  - post-00
  - post-38
  - post-40
  - reference-access
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
- finding_id: formulation-boundary
  issue_key: citation-frontier-formulation-boundary
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Citation support does not resolve exact formulation or growth
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  description: Abstract-only sources, existing chemical-identity discrepancies and
    uninspected base/stock references prevent exact recipe matching. Corrections are
    scoped separately; Whitchurch remains non-operational identity only. No resolved
    variants or positive growth assertions were added.
  evidence_ids:
  - claims
  - excerpts
  - applied
  - pending
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/isolation_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-merge-gates
  description: Repository-wide merge verification and freshness gates failed
  finding_ids:
  - merge-gates
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/isolation_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Resolve derivation defects in a separately scoped change and rerun both gates
    before publication.
- action_id: resolve-native-url-checks
  description: Three native URL reference checks failed
  finding_ids:
  - native-url-checks
  target_ids:
  - CultureMech:004981
  - CultureMech:008841
  - CultureMech:009406
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Restore ordinary bibliographic access or separately improve URL-title handling
    with tests, then rerun. Do not fabricate cache metadata or rewrite correct article
    titles to match error/page-wrapper titles.
- action_id: resolve-formulation-boundary
  description: Citation support does not resolve exact formulation or growth
  finding_ids:
  - formulation-boundary
  target_ids:
  - CultureMech:004981
  - CultureMech:007081
  - CultureMech:007082
  - CultureMech:007083
  - CultureMech:007084
  - CultureMech:007085
  - CultureMech:007086
  - CultureMech:007087
  - CultureMech:007088
  - CultureMech:007089
  - CultureMech:007090
  - CultureMech:007093
  - CultureMech:007094
  - CultureMech:007150
  - CultureMech:007220
  - CultureMech:007261
  - CultureMech:007293
  - CultureMech:007294
  - CultureMech:007295
  - CultureMech:008841
  - CultureMech:009406
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/vr_salts_b.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_2_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_24_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_45_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_27_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/m9_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/lr_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/n_c_0_4_glycerol.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modifed_m9_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/modified_m9_with_toluene.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_octanoate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_gluconate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/e2_medium_with_citrate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/isolation_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/minimal_medium_whitchurch_et_al.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_coso4.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nitrogen_limited_mr_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/pye_solid_medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Keep unsupported formulation and growth unresolved; inspect relevant primary passages
    and preserve assay/strain scope before additional curation.
limitations:
- Partial self-review, not independent review or complete scientific record approval.
- Organism inventory is limited to inspected passages; prior unaffected notes are
  not newly certified.
- NCBI actual ranks and parent-only mappings remain qualified; no growth inheritance
  from cited base papers.
- 69 source files include raw captures and Markdown with explicit access scope, not
  69 papers or full texts.
- Three native reference failures are not waived. Five other baseline failures concern
  unmodified candidates.
- Equal global merge counts would not establish row-level equivalence or attribution.
- No generated or GitHub publication. Pending sources and further discovery leave
  the overall goal incomplete.
```
