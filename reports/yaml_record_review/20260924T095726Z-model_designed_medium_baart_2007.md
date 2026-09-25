# YAML Record Review: Model-designed medium (Baart 2007)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/model_designed_medium_baart_2007.yaml
- Started UTC: 2026-09-24T09:57:26Z
- Finished UTC: 2026-09-24T09:57:26Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/model_designed_medium_baart_2007.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007298` |
| Name | `model_designed_medium_baart_2007` |
| Original name in generated record | `'''Model-designed medium (Baart 2007` |
| Category | `bacterial` |
| Medium source | MediaDB medium `394` |
| Maintained owner | `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml` |
| Generated status | Stale generated merge output from one normalized MediaDB record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/model_designed_medium_baart_2007.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/model_designed_medium_baart_2007.yaml --out /private/tmp/model_designed_medium_baart_2007.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/model_designed_medium_baart_2007.strict.tsv` contained only the header line, so no strict errors were reported. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/model_designed_medium_baart_2007.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/model_designed_medium_baart_2007.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The `MEDIADB:394` identity is correct: the live MediaDB medium page and tab-delimited text endpoint both identify medium 394 as `Model-designed medium (baart 2007)`, list 14 millimolar compounds, and link source 141, `Baart GJ et al, 2007`.

The generated record is stale and no longer matches its normalized owner. The maintained normalized file has already restored `Model-designed medium (Baart 2007)` and `Iron(III) chloride`; this generated file still has the truncated medium label `'''Model-designed medium (Baart 2007` and the truncated ingredient `'''Iron(III`.

Most ingredient names, amounts, and millimolar units match MediaDB medium 394. `Iron(III) chloride` remains under-grounded even in the repaired normalized source: MediaDB reports ChEBI ID `30808`, while the CultureMech row has no `term` or `mediaingredientmech_chebi_term`.

## Evidence

| Source claim | Record representation | Review |
| --- | --- | --- |
| MediaDB medium 394 is `Model-designed medium (baart 2007)` and contains 14 compounds. | The generated record has the correct `MEDIADB:394` CURIE and 14 ingredient rows, but the title is still truncated. | Source identity is recoverable; generated label is stale relative to the MediaDB page and normalized repair. |
| MediaDB lists ammonium chloride 23.5 mM, calcium chloride anhydrous 0.136 mM, cobalt chloride 0.00008 mM, cupric sulfate 0.00008 mM, D-glucose 31.1 mM, magnesium sulfate 2.43 mM, manganese chloride 0.0008 mM, dipotassium phosphate 12.5 mM, potassium dihydrogen phosphate 4.58 mM, sodium chloride 102.0 mM, sodium molybdate 0.00016 mM, sodium thiosulfate 0.38 mM, and zinc sulfate 0.00034 mM. | These 13 names and amounts are present. | Supported. |
| MediaDB lists `Iron(III) chloride` at 0.3 mM with ChEBI ID 30808 in the tab-delimited endpoint. | The generated row is `'''Iron(III` at 0.3 mM and has no chemical term. | Unsupported ingredient identity in the generated file and incomplete grounding in both generated and normalized data. |
| MediaDB source 141 is Baart GJ et al., 2007, Genome Biology, PMID 17617894; PubMed resolves PMID 17617894 to the Neisseria meningitidis metabolism article with DOI `10.1186/gb-2007-8-7-r136`. | The import history says `Reference: Mazumdar et al. (2014) PLOS One`, and the record has no PMID or DOI evidence object. | Provenance is wrong in the import event and incomplete in the record. |
| MediaDB growth record 767 links this medium to its Neisseria meningitidis serogroup B organism entry at pH 7.0 and 37.0. | No target organism, growth evidence, pH 7.0 growth condition, or 37.0 C growth condition is represented. | Incomplete: the source-linked growth context was not imported. |
| MediaDB medium 394 gives a compound list, source, organism, and growth-data link. | The record adds generic dissolve, adjust-pH, and 0.22 um filter-sterilization preparation steps. | Unsupported: the inspected MediaDB pages do not specify those preparation instructions. |

## Completeness

The formula has the right row count and nearly all source amounts, but the generated artifact needs regeneration from its repaired normalized owner to restore the medium and iron names.

The maintained normalized record still lacks a resolved Iron(III) chloride chemical term, durable Baart 2007 identifiers such as PMID `17617894` or DOI `10.1186/gb-2007-8-7-r136`, and the source-linked MediaDB growth context from growth record 767.

Empty optional fields were not considered defects by themselves. The missing growth context is consequential here only because MediaDB medium 394 explicitly links one growth-data record for this exact medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | `data/merge_yaml/merged/model_designed_medium_baart_2007.yaml` is stale relative to its normalized owner and still carries MediaDB SQL parser truncation artifacts. | The generated output was merged on 2026-08-06, while `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml` has 2026-08-31 repair events that restore `Model-designed medium (Baart 2007)` and `Iron(III) chloride`. | Regenerate `data/merge_yaml/merged/model_designed_medium_baart_2007.yaml` from `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml`; also run the merge freshness audit. |
| major | The Iron(III) chloride row is not chemically grounded. | MediaDB 394 reports `Iron(III) chloride`, 0.3 mM, ChEBI ID `30808`; the generated row is truncated and ungrounded, and the normalized repaired row is still ungrounded. | `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml`; MediaDB compound-to-CHEBI import or a focused normalized curation. |
| major | The import history names the wrong literature source. | The reviewed MediaDB medium links source 141, `Baart GJ et al, 2007`; PubMed resolves PMID `17617894` to Baart et al. in Genome Biology. The curation history says the MediaDB import used Mazumdar et al. 2014. | Append a corrective curation event in `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml` and add durable Baart 2007 source identifiers if the schema supports them. |
| major | Generic preparation steps are unsupported by the inspected MediaDB source. | MediaDB 394 lists compounds, a source, organism, and growth-data links; it does not instruct curators to dissolve all ingredients, adjust unspecified pH, or filter-sterilize with a 0.22 um filter. | `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml`; MediaDB importer defaults for `preparation_steps`. |
| minor | MediaDB growth record 767 is absent from the record. | MediaDB links growth record 767 for this medium and records pH 7.0 and 37.0 C for its Neisseria meningitidis serogroup B entry. | `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml`; MediaDB growth-data import if target-organism evidence is in scope. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/model_designed_medium_baart_2007.yaml` from the already repaired normalized record so the generated medium label and `Iron(III) chloride` row stop carrying stale parser damage.
2. Verify MediaDB ChEBI ID `30808` against ChEBI, then ground the repaired `Iron(III) chloride` row in `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml`.
3. Remove or qualify the generic preparation steps unless a Baart 2007 passage or another inspected source supports those exact operations.
4. Add durable Baart 2007 provenance from MediaDB source 141, preferably PMID `17617894` and DOI `10.1186/gb-2007-8-7-r136`, and append a curation event that corrects the prior Mazumdar citation.
5. If MediaDB growth assertions are in scope for MediaDB imports, add a narrow target-organism/growth-evidence entry for growth record 767 without promoting its pH 7.0 and 37.0 C values to source-free global recipe conditions.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/model_designed_medium_baart_2007.yaml` and the regenerated `data/merge_yaml/merged/model_designed_medium_baart_2007.yaml`.
2. Run the merge freshness audit to verify the regenerated `model_designed_medium_baart_2007` record is no longer older than its normalized owner.
3. Manually compare the regenerated record against MediaDB `/media_text/394/` and confirm all 14 compound names and millimolar amounts match, including `Iron(III) chloride`.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
