# YAML Record Review: Bacto Marine Broth (Difco 2216) (For DSM 11879)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacto_marine_broth_difco_2216_for_dsm_11879.yaml
- Started UTC: 2026-09-21T18:24:15Z
- Finished UTC: 2026-09-21T18:24:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008906 |
| Name | bacto_marine_broth_difco_2216_for_dsm_11879 |
| Original name | Bacto Marine Broth (Difco 2216) (For DSM 11879) |
| Maintained input | data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml |
| Source ID | TOGO:M2319 |
| Primary checked sources | TOGO API payload for M2319; DSMZ Medium 514 PDF |
| Generated status | Generated merge under data/merge_yaml/merged from one normalized input |

This record is the TOGO DSM 11879 variant of Bacto Marine Broth (Difco 2216). It starts from DSMZ Medium 514 and adds `Na2S2O3 x 5 H2O` for DSM 11879 and DSM 16960.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacto_marine_broth_difco_2216_for_dsm_11879.yaml` | Passed: `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bacto_marine_broth_difco_2216_for_dsm_11879.yaml --out /private/tmp/bacto_marine_broth_difco_2216_for_dsm_11879.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bacto_marine_broth_difco_2216_for_dsm_11879.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Failed: 7 exact-snippet checks failed |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bacto_marine_broth_difco_2216_for_dsm_11879.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented; `just validate-history` targets standalone `history/` files. |

The repository `just` validators were not used for this target because the project environment currently fails while syncing the Python 3.13 dependency set. The equivalent no-project validators above ran against the checked-in schema and target file.

## Identity and Grounding

The TOGO M2319 and DSMZ Medium 514 sources support the recipe identity: this is the Bacto Marine Broth 2216 base formulation with an added DSM 11879 / DSM 16960 thiosulfate supplement. The generated merge has only one source recipe, so all reviewed defects belong to `data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml` or to the TOGO import path that created it.

The same TOGO unit bugs present in the base `bacto_marine_broth_difco_2216` record are present here. H3BO3, Na2HPO4, `(NH4)NO3`, NaF, SrCl2, and Na-silicate are milligram rows in DSMZ and in TOGO, but they were imported as gram-per-liter rows without dividing by 1000. Distilled water is also imported from 1000 ml as `1000` `G_PER_L`.

The supplemented `Na2S2O3 x 5 H2O` row is source-supported at 1 g/L, but its preparation context is missing: DSMZ and TOGO say to add it after autoclaving from a filter-sterilized stock solution and to check and adjust pH afterward.

## Evidence

TOGO:M2319 carries pH `7.4 - 7.8`, all DSMZ Medium 514 component rows, and the DSM 11879/16960 thiosulfate supplement. Its comments retain both DSMZ notes: final pH 7.6 +/- 0.2 at 25 C for the base medium and post-autoclave addition of 1 g/L `Na2S2O3 x 5 H2O` from a filter-sterilized stock for DSM 11879 and DSM 16960.

The enriched target-organism evidence is attached to the wrong formulation. The Cellulophaga, Kangiella, Phaeobacter, and Joostella Springer articles support cultivation in parent DSMZ Medium 514 or Marine Broth 2216. They do not say those strains used the DSM 11879-specific thiosulfate-supplemented variant. The Kangiella, Phaeobacter, and Joostella evidence also paraphrases source text, while the schema requires exact cited substrings.

The Roseobacter ponti and Rhodothermus profundi sources could not be manually inspected in this review because `curl -L` reached Cloudflare challenge pages at Oxford Academic and Microbiology Research. The reference validator independently failed both snippets because only abstracts are present in the local reference cache; the MB1/2 variant evidence failed for the same reason.

## Completeness

- The final pH tolerance and 25 C context are absent.
- The sodium thiosulfate post-autoclave, filter-sterilized stock addition and post-autoclave pH check are absent.
- Bacto yeast extract and Bacto peptone remain ungrounded despite exact local mappings.
- Phaeobacter caeruleus and Joostella marina target-organism entries lack `term` CURIEs, unlike the other taxon-grounded target organisms.
- Empty direct paper references for the TOGO/DSMZ source recipe are not automatically defective because the inspected source is a medium protocol; the broken DOI evidence applies to enriched growth claims, not the source recipe itself.

A gitignore-independent search of `reports/yaml_record_review` for `bacto_marine_broth_difco_2216_for_dsm_11879|Bacto_Marine_Broth_Difco_2216_for_DSM_11879|DSM_11879` found no existing report for this target before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Blocker | All seven DOI snippets are invalid exact substrings. | `linkml-reference-validator` failed six `target_organisms[*].evidence[0].snippet` checks plus the MB1/2 `variants[0].evidence[0].snippet` check. | data/normalized_yaml/bacterial/bacto_marine_broth_difco_2216_for_dsm_11879.yaml |
| Major | Parent-medium growth evidence is scoped to a DSM 11879-specific supplemented variant. | TOGO:M2319 and DSMZ define this recipe by adding sodium thiosulfate to DSMZ 514 for DSM 11879 and DSM 16960. The inspected Cellulophaga, Kangiella, Phaeobacter, and Joostella papers support parent DSMZ 514 / Marine Broth 2216 growth, not growth on the thiosulfate variant. | Move parent-medium `target_organisms` and MB1/2 variant evidence to the base DSMZ 514 / Marine Broth 2216 record |
| Major | Six milligram-scale trace salts were imported as grams per liter. | TOGO:M2319 records H3BO3 22 mg, Na2HPO4 8 mg, `(NH4)NO3` 1.6 mg, NaF 2.4 mg, SrCl2 34 mg, and Na-silicate 4 mg; the YAML stores those same numbers as `G_PER_L`. | TOGO unit normalization for M2319 |
| Major | The DSM 11879 thiosulfate preparation instructions are missing. | TOGO and DSMZ say the 1 g/L sodium thiosulfate pentahydrate supplement is added after autoclaving from a filter-sterilized stock and that pH should be checked afterward. The YAML keeps only a top-level 1 g/L ingredient row. | TOGO comment import into preparation steps |
| Major | Distilled water has the wrong unit. | TOGO and DSMZ specify 1000 ml; the YAML represents this as 1000 g/L. | TOGO unit normalization |
| Major | Bacto yeast extract and Bacto peptone are missing exact available groundings. | The packaged label index maps `Bacto yeast extract` to `FOODON:03315426` and `Bacto peptone` to `MICRO:0000178`; both rows are ungrounded. | Ingredient grounding in the normalized TOGO record, using the packaged label index |
| Major | Two target organisms are missing taxon CURIEs. | Phaeobacter caeruleus and Joostella marina have only `preferred_term` and strain values, while neighboring target-organism rows carry NCBITaxon terms. | Growth-evidence curation in the normalized record |
| Minor | Fe(III) citrate still uses the legacy MIM slot. | The ingredient has `term.id: CHEBI:144421`, and the packaged label index has an exact CHEBI-keyed Fe(III) citrate row, but the record still stores `mediaingredientmech_term: MediaIngredientMech:000186`. | Legacy-to-CHEBI MIM migration or targeted ingredient link refresh |

## Recommended Edits

1. Move the six parent-medium target-organism rows and the MB1/2 half-strength variant from this DSM 11879-specific supplement record to the base Bacto Marine Broth 2216 record, or replace them with evidence specific to DSM 11879 / DSM 16960 use of the thiosulfate-supplemented formulation.
2. Replace every enriched growth snippet with exact text from the cited source or remove claims whose full text cannot be inspected.
3. Convert the six milligram ingredients to grams per liter: SrCl2 0.034, H3BO3 0.022, Na-silicate 0.004, NaF 0.0024, `(NH4)NO3` 0.0016, and Na2HPO4 0.008 g/L.
4. Preserve distilled water as 1000 ml/L, not 1000 g/L.
5. Represent the sodium thiosulfate supplement as a post-autoclave, filter-sterilized stock addition and retain the post-autoclave pH check.
6. Import the DSMZ/TOGO final pH as pH 7.6 with the +/- 0.2 at 25 C tolerance retained in a preparation note or discussion field.
7. Link Bacto yeast extract and Bacto peptone to their exact packaged label-index terms and refresh the Fe(III) citrate link to `mediaingredientmech_chebi_term`.
8. Add exact NCBITaxon CURIEs for Phaeobacter caeruleus and Joostella marina if those rows remain after evidence is rescopied.
9. Regenerate `data/merge_yaml/merged/bacto_marine_broth_difco_2216_for_dsm_11879.yaml` and generated pages from the corrected normalized data.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validators on the edited normalized input and regenerated merge; the reference validator must reach 0 failed snippet checks.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regeneration to confirm this remains a one-source merge unless a duplicate is intentionally added.
- Manually compare the regenerated amounts against TOGO:M2319 to confirm every `mg` source amount was divided by 1000 exactly once and the 1 g/L thiosulfate supplement was not divided.
- Manually inspect all remaining DOI sources for `target_organisms` and `variants` after rescoping; full text that is blocked by Cloudflare in this review should be sourced from a local PDF, PMC mirror, or another accessible authoritative copy before the claim is kept.

## Additional Notes

- The DOI network fetches reached inspectable Springer full text for the four `10.4056/sigs.*` citations. `10.1093/gbe/evaa114` and `10.1099/ijs.0.012724-0` redirected to Cloudflare challenge pages, so the Roseobacter and Rhodothermus claims remain unresolved here.
- The exact ignored-inclusive pre-report search covered `reports/yaml_record_review`; no prior report for this target was present.
- The same TOGO milligram-to-gram defect was present in the previous base Bacto Marine Broth review.
