# YAML Record Review: ILYOBACTER MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ilyobacter_medium__cc6d60d9.yaml
- Started UTC: 2026-09-23T14:45:00Z
- Finished UTC: 2026-09-23T14:48:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:002915 |
| Name | ilyobacter_medium |
| Original name | ILYOBACTER MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 7.0 |
| Source identity | MediaDive JCM Medium J566 |
| Generated path reviewed | data/merge_yaml/merged/ilyobacter_medium__cc6d60d9.yaml |
| Maintained owner | data/normalized_yaml/bacterial/ilyobacter_medium.yaml |

The reviewed file is generated from the maintained MediaDive/JCM owner above.
Future fixes should update that normalized record and the MediaDive stock
importer before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ilyobacter_medium__cc6d60d9.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/ilyobacter_medium__cc6d60d9.yaml --out /private/tmp/ilyobacter_medium__cc6d60d9.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/ilyobacter_medium__cc6d60d9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/ilyobacter_medium__cc6d60d9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `mediadive.medium:J566` source term, and source URL
  identify the MediaDive import of JCM Medium 566.
- A gitignore-independent exact search for `CultureMech:002915` over bacterial
  normalized records, normalized indexes, and merged records found only this
  MediaDive owner, its generated merged copy, and index entries.
- A gitignore-independent exact search for `mediadive.medium:J566` over the
  same paths found only this MediaDive owner, its generated merged copy, and
  index entries.
- A gitignore-independent exact search for `TOGO:M570` found a separate TOGO
  import of the same JCM medium that has not been merged with this MediaDive
  record.

## Evidence

- MediaDive J566 exposes a 2020 ml main solution with 2000 ml distilled water,
  10 ml Wolfe's mineral solution, and 10 ml trace vitamins.
- The normalized YAML omits the 2000 ml distilled-water row and flattens
  nickel, selenite, tungstate, and all ten trace vitamins into top-level final
  ingredients at stock concentrations.
- The source resazurin row is a 100 ul addition of 1% resazurin solution; the
  YAML records `Resazurin` as `100 G_PER_L`.
- MediaDive J566 does not contain a mandatory Na2S x 9 H2O ingredient. It says
  to add one drop of 5% Na2S from a sterile stock only if the medium stays pink.
- The preparation steps for pH 7.0, boiling to 1.0 L, N2 dispensing into
  Hungate tubes, and the conditional Na2S addition are represented.
- The live JCM GRMD=566 endpoint now returns `Nothing found`, so MediaDive and
  TOGO are the recoverable upstream formula views for this JCM identifier.

## Completeness

- The core salt and organic substrate quantities are represented with
  MediaDive's final-volume-normalized G_PER_L values.
- The two 10 ml stock additions have been flattened into final ingredients, so
  their subrecipe context and dilution by 10 ml into a 2020 ml main solution
  are missing.
- The source water carrier is absent.
- The conditional sodium-sulfide rescue step has become a mandatory final
  sodium sulfide nonahydrate ingredient.
- Empty optional fields for synonyms, publication references, target organisms,
  discussions, variants, and quality flags are acceptable only after the stock
  solution structure and conditional reducing-agent step are represented
  explicitly.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Wolfe's mineral solution and trace vitamins were flattened as undiluted final ingredients. | MediaDive lists both as 10 ml additions to a 2020 ml main solution; the YAML records nickel, selenite, tungstate, and all vitamin stock rows as top-level G_PER_L ingredients. | `data/normalized_yaml/bacterial/ilyobacter_medium.yaml`; MediaDive stock import. |
| Major | Resazurin volume units were misread as a gram-per-liter quantity. | MediaDive and TOGO both describe 100 ul of 1% resazurin solution; the YAML records 100 g/L resazurin. | `data/normalized_yaml/bacterial/ilyobacter_medium.yaml`; MediaDive micro-liter import. |
| Major | A conditional Na2S stock step became a mandatory Na2S x 9 H2O ingredient. | MediaDive has only a conditional one-drop 5% Na2S addition when O2 is present; the YAML has 0.296736 g/L `Na2S x 9 H2O` in `ingredients`. | `data/normalized_yaml/bacterial/ilyobacter_medium.yaml`; MediaDive preparation import. |
| Major | The 2000 ml main water row is missing. | MediaDive J566 lists 2000 ml distilled water in the main solution, but the YAML has no water carrier. | `data/normalized_yaml/bacterial/ilyobacter_medium.yaml`; MediaDive import. |
| Minor | The MediaDive and TOGO imports of the same JCM medium are not deduplicated. | `ilyobacter_medium__cc6d60d9.yaml` comes from `mediadive.medium:J566`, while `ILYOBACTER_MEDIUM.yaml` comes from `TOGO:M570` / JCM_M566. | Duplicate detection between `data/normalized_yaml/bacterial/ilyobacter_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M570_Ilyobacter_Medium.yaml`. |

## Recommended Edits

1. Restore Wolfe's mineral solution and trace vitamins as 10 ml stock additions
   instead of flattened top-level stock components.
2. Preserve the 100 ul 1% resazurin stock row with the source volume unit and
   concentration rather than importing `100 G_PER_L`.
3. Remove mandatory Na2S x 9 H2O from final ingredients and retain the 5% Na2S
   stock only as a conditional preparation addition.
4. Restore the 2000 ml distilled-water carrier from MediaDive J566.
5. After the MediaDive and TOGO JCM-566 imports are both stock-aware, compare
   them for source-duplicate merging.
6. Regenerate `data/merge_yaml/merged/` from the corrected MediaDive owner.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after correcting
   `data/normalized_yaml/bacterial/ilyobacter_medium.yaml`.
2. Recompare the regenerated record to the live MediaDive J566 REST payload,
   checking the 2020 ml main volume, both 10 ml stock additions, and the 100 ul
   resazurin row.
3. Recompare the separate TOGO M570 record after TOGO stock-solution cleanup so
   the two JCM Medium 566 imports can be deduplicated intentionally.

## Additional Notes

- JCM's current public GRMD=566 page reports no matching medium, so the original
  JCM table could not be used directly for this review.
- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
