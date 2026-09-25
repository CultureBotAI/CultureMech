# YAML Record Review: MMP-biotin, thiamine, and Ca pantothenate; Villasenor et al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml
- Started UTC: 2026-09-24T09:29:43Z
- Finished UTC: 2026-09-24T09:32:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:007063 |
| Record name | mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al |
| Original name | MMP-biotin, thiamine, and Ca pantothenate; Villasenor et al |
| Category | bacterial |
| Source accession | MEDIADB:172 |
| Reviewed generated file | data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml |
| Maintained owner | data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml |
| Merge source | mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al |
| Merge fingerprint | d12711bc8a022af4927095a1e0995acb828117f4cdfdb6e2c1497555a039bee3 |

The reviewed file is a stale generated merge from a maintained MediaDB normalized record. The maintained owner was updated on 2026-08-31 to repair the truncated `Iron(III) chloride` name, while this generated merge was last produced on 2026-08-06 and still contains the broken pre-repair ingredient. Future edits belong in `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml`, followed by merge regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml` | Passed; `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml --out /private/tmp/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.strict.tsv --workers 1 --quiet` | Passed; one file scanned, zero error rows. `/private/tmp/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.strict.tsv` had one line, the header only. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally; the validator ran zero reference checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run for this merged record. | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML. |

The validators do not detect that the generated merge is stale, that one ingredient name is syntactically truncated, or that the citation in the import history is not the MediaDB source.

## Identity and Grounding

The current record identity is mostly coherent:

- `CultureMech:007063`, `MEDIADB:172`, and the MediaDB medium 172 page identify `MMP-biotin, thiamine, and Ca pantothenate; Villasenor et al`.
- `find data/normalized_yaml -name mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml -print` resolved the maintained owner exactly.
- MediaDB source 64 identifies the source as Villasenor et al. 2011 and links to the paper `Housekeeping genes essential for pantothenate biosynthesis are plasmid-encoded in Rhizobium etli and Rhizobium leguminosarum`.
- Crossref resolves DOI `10.1186/1471-2180-11-66` to the same 2011 BMC Microbiology paper title.
- An ignored-aware exact search for `MEDIADB:172` and `CultureMech:007063` found this owner, this merge, and generated indexes; no second recipe YAML with this MediaDB accession was found.

Grounding and provenance defects remain:

- The reviewed merge still has a malformed `preferred_term: '''Iron(III` row. The maintained owner already repairs that label to `Iron(III) chloride`.
- `Iron(III) chloride` remains ungrounded in the maintained owner even though MediaDB's tab-delimited record exposes a ChEBI-like terminal identifier `30808` for that row.
- `Thiamine` still carries the legacy `mediaingredientmech_term` slot even though the row has `CHEBI:18385`.
- The first curation-history entry says the MediaDB import used Mazumdar et al. 2014 PLOS One; the inspected MediaDB medium page and source page point to Villasenor et al. 2011.

## Evidence

MediaDB medium 172 directly supports the nine imported ingredient rows and their millimolar amounts:

- Succinate 10.0 mM.
- Biotin 0.00409316 mM.
- Thiamine 0.033243 mM.
- Calcium chloride anhydrous 1.49 mM.
- Potassium dibasic phosphate 1.26 mM.
- Calcium pantothenate 0.001 mM.
- Magnesium sulfate 0.83 mM.
- Ammonium chloride 10.0 mM.
- Iron(III) chloride 0.0184 mM.

The generated record preserves the first eight ingredient amounts, but its iron row is stale and broken relative to both MediaDB and the maintained normalized owner:

- MediaDB text: `Iron(III) chloride` at 0.0184 mM.
- Maintained owner: `preferred_term: Iron(III) chloride` at 0.0184 mM.
- Generated merge: `preferred_term: '''Iron(III` at 0.0184 mM.

The MediaDB page also lists six organisms and six growth-data rows for this exact medium: Rhizobium etli CFN42, CFNX186, CFNX186-24, CFNX186-4, ReTV1, and ReTV2. None are represented in `target_organisms` or `growth_metrics`.

## Completeness

Consequential gaps:

- The generated merge is stale relative to the maintained normalized owner and needs regeneration before the generated corpus can be trusted.
- The maintained owner has no structured source reference for MediaDB source 64, Villasenor et al. 2011, or DOI `10.1186/1471-2180-11-66`.
- The six MediaDB growth-data links for the exact MMP variant are not represented.
- The preparation steps are generic importer prose. MediaDB medium 172 did not specify pH or filtration steps in the inspected medium page or tab-delimited formula, so `Adjust pH if specified in original formulation` and `Sterilize by filtration (0.22 um) to preserve heat-sensitive components` are unsupported placeholders.

Empty optional fields for variants and storage were not treated as defects on their own.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The reviewed merge is stale and still contains a repaired MediaDB parser defect. | The generated merge was built on 2026-08-06 and contains `'''Iron(III`; the maintained owner has a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` curation event and now stores `Iron(III) chloride`. | Regenerate from `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml`; freshness checks belong in merge verification. |
| Major | Source provenance names the wrong paper. | MediaDB medium 172 links source 64, Villasenor et al. 2011, and Crossref confirms DOI `10.1186/1471-2180-11-66` for that BMC Microbiology paper. The import history says Mazumdar et al. 2014 PLOS One. | `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml`. |
| Major | MediaDB growth evidence was not imported. | The MediaDB medium page lists six growth-data rows for Rhizobium etli strains on this exact MMP-biotin, thiamine, and Ca pantothenate formulation; the record has no target-organism or growth-metric entries. | `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml` and the MediaDB importer. |
| Major | Preparation steps are unsupported placeholders. | The inspected MediaDB medium and text pages list ingredients and linked source/growth data; they do not state a pH target or 0.22 um filtration for this formulation. | MediaDB importer defaults and `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml`. |
| Major | Ingredient grounding is incomplete. | Iron(III) chloride has no CHEBI or MIM grounding, and Thiamine still uses the legacy `mediaingredientmech_term` slot. | `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml` and ingredient enrichment. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml` from the maintained owner so the corrected `Iron(III) chloride` row appears in the generated corpus.

2. Correct MediaDB provenance by replacing the stale Mazumdar PLOS One citation with MediaDB source 64 and DOI `10.1186/1471-2180-11-66`.

3. Import or curate the six MediaDB growth-data rows for the Rhizobium etli strains on this exact formulation.

4. Remove unsupported generic preparation steps unless Villasenor et al. or another inspected primary source states the pH adjustment and 0.22 um filtration protocol.

5. Ground Iron(III) chloride exactly and migrate Thiamine from legacy `mediaingredientmech_term` to a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Follow-up Checks

- Rerun the focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/mmp_biotin_thiamine_and_ca_pantothenate_villasenor_et_al.yaml`.
- Regenerate merges and run `just verify-merges` plus `just audit-merge-freshness`.
- Diff the regenerated merge to confirm it contains `Iron(III) chloride`, not the truncated pre-repair label.
- Recheck `https://mediadb.systemsbiology.net/defined_media/media/172/`, `/media_text/172/`, and `/sources/64/` after provenance and growth-evidence curation.

## Additional Notes

- `medium_type: DEFINED` and `composition_type: DEFINED` are supported by the inspected chemically defined MediaDB formulation.
- The old BMC article URL linked by MediaDB redirected to a modern Springer page shell that did not expose the 2011 article; Crossref resolved the DOI instead.
