# YAML Record Review: Embryonated, antibiotic-free, and pathogen-free eggs

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml
- Started UTC: 2026-09-23T00:04:00Z
- Finished UTC: 2026-09-23T00:10:27Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:008861`
- Name: `embryonated_antibiotic_free_and_pathogen_free_eggs`
- Original label: `Embryonated, antibiotic-free, and pathogen-free eggs`
- Category: `bacterial`
- Medium term: `TOGO:M2275`
- Generated status: generated merge record with fingerprint `ca118df8a4c6dc94fbcbb096a956a16d54019b8247d763700a84b7d738ec708b`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml`

The merge record adds only the `merge_recipes.py` history entry, `merge_fingerprint`, and `merged_from` metadata on top of the maintained normalized record.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml --out /private/tmp/embryonated_antibiotic_free_and_pathogen_free_eggs.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is a TOGO-only import. TOGO M2275 has no `src_url`, but its extracted comments identify a host propagation method for `C. burnetii`: cells were propagated in embryonated, antibiotic-free, pathogen-free eggs; the eggs were inoculated, incubated for 9 days at 37 C and 98 percent humidity, continuously rocked, and harvested when about 50 percent of embryos had died.

The source article behind the TOGO comment resolves as PMID `18707130`, DOI `10.1021/ac800788k`, an Analytical Chemistry paper on mass-spectrometric detection and identification of Coxiella burnetii extracted proteins.

The local medium identity is therefore only partially grounded. `TOGO:M2275` is the correct TOGO accession, but the record classifies an embryonated egg infection substrate as a bacterial `LIQUID` medium and reduces the protocol to one variable `Whole egg` ingredient.

## Evidence

The `Whole egg` row is a coarse lead, not a complete recipe. The TOGO payload's only component is `Whole egg` with the GMO label `Egg, whole`, but all biologically important information is in the comments:

- The system is for propagation of `C. burnetii`, not generic microbial cultivation.
- The eggs are embryonated, antibiotic-free, and pathogen-free.
- The eggs are inoculated with `C. burnetii`.
- Incubation is 9 days at 37 C and 98 percent humidity.
- The eggs are continuously rocked.
- Yolk sacs are harvested after about 50 percent embryo death.

The reviewed record keeps none of those conditions except the title text in `original_name` and the TOGO accession in `media_term`. No PMID, DOI, target organism, incubation condition, humidity, rocking, or harvest criterion is represented.

## Completeness

The record is incomplete as a CultureMech recipe. It needs either a scoped representation for whole-egg host propagation or a quality flag that prevents users from treating the entry as an ordinary formulated liquid medium.

The exact local discovery command `find data/normalized_yaml -name '*embryonated*' -o -name '*antibiotic*' -o -name '*pathogen*'`, which includes ignored files, found this normalized owner plus unrelated antibiotic-supplemented media. It found no duplicate embryonated-egg record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | The physical and recipe model are wrong for an embryonated egg propagation system. | TOGO M2275 describes inoculated embryonated eggs with humidity, rocking, and yolk-sac harvest; the reviewed record sets `physical_state: LIQUID` and has only a variable `Whole egg` ingredient. | `data/normalized_yaml/bacterial/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml` |
| major | The Coxiella-specific propagation conditions are dropped. | TOGO comments state that antibiotic-free, pathogen-free eggs were inoculated with `C. burnetii`, incubated for 9 days at 37 C and 98 percent humidity, rocked continuously, and harvested after about 50 percent embryo death; no `target_organisms`, preparation steps, or incubation conditions encode those claims. | `data/normalized_yaml/bacterial/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml` |
| major | The PMID/DOI evidence chain is not structured. | TOGO cites PMID `18707130`; PubMed resolves that PMID to DOI `10.1021/ac800788k`, but the record has no `sources`, `references`, or evidence snippet. | `data/normalized_yaml/bacterial/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml` |

## Recommended Edits

1. Add explicit evidence for PMID `18707130` / DOI `10.1021/ac800788k`, with a note that TOGO M2275 has no direct `src_url` beyond its PubMed-backed prose.
2. Replace `LIQUID` and the variable `Whole egg` recipe with a structured whole-embryonated-egg propagation representation if the schema can express one; otherwise add a quality flag or discussion marking this TOGO import as outside ordinary formulated media.
3. Add `C. burnetii` as the scoped organism only if the strain and propagation claim can be verified from the inspected article or TOGO source.
4. Preserve the 9 day, 37 C, 98 percent humidity, continuous rocking, and approximately 50 percent embryo-death harvest conditions as protocol text.
5. Regenerate merged YAML and downstream pages.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/embryonated_antibiotic_free_and_pathogen_free_eggs.yaml`.
2. Reinspect TOGO M2275 and PMID `18707130` before promoting any `C. burnetii` growth or strain claim.
3. Manually inspect the generated page and confirm it does not read like a bottle- or plate-based liquid bacterial medium.

## Additional Notes

- This record has no JCM, DSMZ, CCAP, or MediaDive source accession; TOGO itself is the only medium accession inspected.
