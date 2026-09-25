# YAML Record Review: Ignicoccus Medium (for DSM 18386)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml
- Started UTC: 2026-09-23T14:29:37Z
- Finished UTC: 2026-09-23T14:34:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:009166 |
| Name | ignicoccus_medium_for_dsm_18386 |
| Original name | Ignicoccus Medium (for DSM 18386) |
| Class | MediaRecipe |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | Not represented |
| Source identity | TOGO Medium M2599, derived from DSMZ Medium 897 |
| Generated path reviewed | data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml |
| Maintained owner | data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml |

The reviewed file is generated from the maintained TOGO M2599 variant record
above. Future fixes should update that normalized record, TOGO parser rules,
target-organism evidence, and duplicate or variant-linking inputs before
regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml --out /private/tmp/ignicoccus_medium_for_dsm_18386.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Failed with two exact-snippet errors for `doi:10.1128/JB.06130-11`; the validator could reach DOI metadata but the ASM PDF returned 403, leaving only the abstract. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `TOGO:M2599` media term, and source name identify TOGO's
  DSM 18386 variant of DSMZ Medium 897.
- A gitignore-independent exact search for `CultureMech:009166` over this
  maintained YAML, this generated YAML, the ID registry, TOGO and archaea
  indexes, and the media content-review manifest found this TOGO M2599 import
  and its generated index or manifest entries.
- A gitignore-independent exact search for `TOGO:M2599` over maintained
  archaeal records, generated merged records, and normalized indexes found only
  this TOGO M2599 import.
- DSMZ 897 and TOGO M2599 agree that the DSM 18386 variant is the base
  Ignicoccus Medium prepared without meat extract; the generated recipe
  correctly omits the meat-extract row that is present in TOGO M2614.

## Evidence

- The core formulation is the same DSMZ 897 salt, sulfur, and sodium sulfide
  formula with meat extract omitted for DSM 18386.
- TOGO M2599 exposes `ph: 5.0 - 5.5`, but the YAML has no `ph_range`.
- H3BO3 is 15 mg in TOGO/DSMZ but 15 g/L in the YAML, sodium resazurin is
  0.5 ml of a 0.1% w/v stock but 0.5 g/L in the YAML, and distilled water is
  1000 ml in the source but 1000 g/L in the YAML.
- The 7 ml SrCl2 x 6 H2O and 0.5 ml KI stock additions have been migrated to
  empty `Unknown solution` entries with `G_PER_L` quantities.
- H2SO4, N2, CO2, and H2 are preparation and atmosphere terms in the TOGO
  comments, but all four are variable-concentration ingredients in the YAML.
- The DOI and PMID for Mayer 2012 resolve, and the PMC full text supports
  growth of `I. hospitalis` DSM 18386 in 1/2 SME-Ignicoccus medium at 90 C with
  an H2-CO2 gas phase. The stored `I. hospitalis` snippet is a close paraphrase,
  not an exact source excerpt.
- The Koschnitzki 2017 dissertation record resolves and its PDF supports the
  `half_sme_s0_ignicoccus` recipe plus the `I. islandicus` DSM 13165T and
  `I. pacificus` DSM 13166T strain list. Those two organism entries are scoped
  to the 1/2 SME+S0 variant, not to the TOGO M2599 parent formulation itself.
- The Mayer 2012 PMC text supports the 0.1% yeast-extract supplemented variant,
  but the stored variant snippet is also a paraphrase rather than an exact
  excerpt.

## Completeness

- The record correctly represents the DSM 18386 variant as a meat-extract-free
  formulation distinct from TOGO M2614.
- The source pH range, row units, Sr/KI stock rows, and preparation gas
  scoping need the same TOGO cleanup as the base M2614 import.
- `I. islandicus` and `I. pacificus` growth evidence should move off the parent
  `target_organisms` list or be represented only as `half_sme_s0_ignicoccus`
  variant evidence.
- Empty optional fields for synonyms, direct publication references,
  discussions, and quality flags are acceptable only after the formula and
  evidence-scoping issues above are represented explicitly.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Source `mg` and `ml` rows were imported as `G_PER_L`. | The TOGO payload has 15 mg H3BO3, 0.5 ml sodium resazurin stock, and 1000 ml water; the YAML records 15 g/L, 0.5 g/L, and 1000 g/L. | `data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml`; TOGO unit import. |
| Major | Sr and KI stocks were migrated to empty, wrongly quantified solutions. | TOGO M2599 carries 7 ml SrCl2 x 6 H2O stock and 0.5 ml KI stock; the YAML has empty `Unknown solution` records with `G_PER_L` quantities. | `data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml`; `solution-migrator-v1.0`. |
| Major | Preparation-only acid and gases are final-medium ingredients. | H2SO4, N2, CO2, and H2 occur in TOGO/DSMZ preparation instructions, but the YAML records them as variable-concentration ingredient rows. | `data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml`; TOGO comment parsing. |
| Major | The TOGO pH range is missing. | TOGO M2599 exposes pH 5.0-5.5 in metadata and the YAML has neither `ph_range` nor `ph_value`. | `data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml`; TOGO pH extraction. |
| Major | Two Mayer evidence snippets are not exact source text. | Reference validation failed for both `doi:10.1128/JB.06130-11` snippets; manual PMC inspection supports the claims but not the stored wording as an exact excerpt. | `data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml`; evidence cleanup. |
| Major | Variant-scoped organisms are attached to the parent target-organism list. | Koschnitzki supports `I. islandicus` and `I. pacificus` on the 1/2 SME+S0 variant, and the YAML explanations warn not to assert identity with the parent. | `data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml`; target-organism enrichment. |

## Recommended Edits

1. Correct H3BO3, sodium resazurin, and distilled-water units from the original
   TOGO/DSMZ row units.
2. Replace the empty Sr/KI `Unknown solution` records with source-faithful
   stock additions at 7 ml and 0.5 ml.
3. Move 2 N H2SO4, N2, CO2, and H2 out of final ingredients and retain them
   only in preparation or atmosphere fields.
4. Restore `ph_range: 5.0-5.5` from TOGO M2599 metadata.
5. Replace the Mayer snippets with exact PMC excerpts.
6. Move `I. islandicus` and `I. pacificus` off parent `target_organisms` or
   attach them only to the `half_sme_s0_ignicoccus` variant.
7. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M2599 merged record; the reference validator should no longer report
  Mayer snippet mismatches.
- Manually compare the regenerated formula against TOGO M2599 and DSMZ 897.
- Recheck the Mayer 2012 PMC article and Koschnitzki 2017 PDF against every
  target-organism and variant evidence block.

## Additional Notes

- The DSM 18386 variant identity is correct; the material errors are inherited
  TOGO row parsing, pH omission, empty solution migration, and later
  organism-evidence scoping.
