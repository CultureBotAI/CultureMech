# YAML Record Review: haloalkaliphilic_growth_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloalkaliphilic_growth_medium__cf639565.yaml
- Started UTC: 2026-09-23T09:15:34Z
- Finished UTC: 2026-09-23T09:17:02Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000589 |
| Name | haloalkaliphilic_growth_medium |
| Original name | HALOALKALIPHILIC GROWTH MEDIUM |
| Category | bacterial |
| Generated path | data/merge_yaml/merged/haloalkaliphilic_growth_medium__cf639565.yaml |
| Maintained parent | data/normalized_yaml/bacterial/haloalkaliphilic_growth_medium.yaml |
| Merge fingerprint | cf639565fdb77ae784d1399ccce03def254f35e69d9801fb0759e95b5470fbc5 |

This is the generated August 2026 merge product for DSMZ/MediaDive medium 1150.
Future edits belong in `data/normalized_yaml/bacterial/haloalkaliphilic_growth_medium.yaml`
or in the source-equivalence merge logic, then `data/merge_yaml/merged/` should
be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloalkaliphilic_growth_medium__cf639565.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloalkaliphilic_growth_medium__cf639565.yaml --out /private/tmp/haloalkaliphilic_growth_medium_cf639565.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloalkaliphilic_growth_medium__cf639565.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloalkaliphilic_growth_medium__cf639565.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- `media_term` is correctly grounded to `mediadive.medium:1150` labeled
  `HALOALKALIPHILIC GROWTH MEDIUM`.
- MediaDive medium 1150 reports source `DSMZ`, pH 10, and the DSMZ Medium 1150
  PDF link named in the YAML notes.
- The live DSMZ PDF identifies medium 1150 as `HALOALKALIPHILIC GROWTH MEDIUM`
  and matches the MediaDive 1150 formula.
- The seven simple ingredients with CHEBI groundings are exact enough; sodium
  tetraborate is correctly hydrated as `Na2B4O7 x 10 H2O`.
- Yeast extract and Casamino acids are intentionally ungrounded complex
  ingredients.

## Evidence

Supported by inspected sources:

- DSMZ Medium 1150 and MediaDive 1150 support the label, pH 10.0, and liquid
  main solution.
- DSMZ and MediaDive support 5 g/L glucose, 4 g/L `Na2B4O7 x 10 H2O`, 0.5 g/L
  `NaNO3`, 1 g/L `NH4Cl`, 0.5 g/L `KH2PO4`, 1 g/L yeast extract, 0.5 g/L
  Casamino acids, and 100 g/L `NaCl`.
- DSMZ and MediaDive support adjusting the medium to pH 10.0 with concentrated
  NaOH.

Unsupported or incomplete in this generated record:

- The 1000 ml distilled-water row present in both DSMZ and MediaDive is absent
  from the generated record and its maintained normalized parent.
- `NaNO3` still carries `mediaingredientmech_term: MediaIngredientMech:000171`
  despite the 2026-06-05 migration away from legacy MediaIngredientMech IDs.
- The source PDF is only present in `notes`; it is absent from structured
  `references`, so the reference validator did not check the DSMZ source.

## Completeness

- The target preserves the salts, glucose, yeast extract, Casamino acids, NaCl,
  pH 10.0, and NaOH pH-adjustment instruction from the DSMZ source.
- The target is incomplete as an executable 1 L formula until distilled water is
  restored.
- The source-equivalent KOMODO record is still split from this direct
  DSMZ/MediaDive record; an exact `rg --no-ignore --hidden` search for
  `mediadive\.medium:1150\b|DSMZ_Medium1150\b|ID: 1150\b` across
  `data/merge_yaml` and `data/normalized_yaml` found the direct DSMZ import and
  a KOMODO ModelSEED record that names DSMZ 1150 in its notes.
- The KOMODO sibling adds NaOH as a variable ingredient even though DSMZ uses
  concentrated NaOH only as a pH adjuster; that over-specified ingredient should
  be removed before source-equivalence merging.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The formula omits the 1 L distilled-water component. | DSMZ Medium 1150 and MediaDive 1150 both list 1000 ml distilled water as the ninth recipe row; neither the generated record nor `data/normalized_yaml/bacterial/haloalkaliphilic_growth_medium.yaml` contains water. | Add the water row to `data/normalized_yaml/bacterial/haloalkaliphilic_growth_medium.yaml` and regenerate. |
| Major | The source-equivalent KOMODO record remains split under a separate CultureMech ID and merge fingerprint. | `data/normalized_yaml/bacterial/KOMODO_1150_HALOALKALIPHILIC_GROWTH_medium.yaml` names KOMODO ID 1150 and `DSMZ Medium: 1150 (mediadive.medium:1150)`, while this target is the direct MediaDive/DSMZ 1150 import. | After removing KOMODO's unsupported variable NaOH ingredient, add a source-equivalence or merge-key repair so KOMODO 1150 and DSMZ/MediaDive 1150 collapse into one generated record. |
| Minor | `NaNO3` still has a legacy `mediaingredientmech_term`. | The generated row has the correct `term: CHEBI:63005` but still includes `mediaingredientmech_term: MediaIngredientMech:000171` after a curation event that claims legacy MediaIngredientMech IDs were replaced. | Remove the stale legacy MIM slot from the maintained parent during the water-row repair. |
| Minor | The DSMZ PDF is not in structured `references`. | The URL appears only in free text under `notes`, so the reference validator ran 0 checks. | Add a structured `references` entry for the DSMZ PDF in the maintained parent. |

## Recommended Edits

1. Add `Distilled water` at 1000 ml/L, grounded to CHEBI water, to
   `data/normalized_yaml/bacterial/haloalkaliphilic_growth_medium.yaml`.
2. Add `references:` with the DSMZ Medium 1150 PDF URL to the maintained parent.
3. Remove the stale `mediaingredientmech_term` from the `NaNO3` row.
4. Remove variable NaOH as a KOMODO ingredient and keep the NaOH statement
   scoped to pH adjustment.
5. Add a source-identity merge rule or equivalence overlay for KOMODO 1150 and
   DSMZ/MediaDive 1150, then regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `haloalkaliphilic_growth_medium` output.
- Inspect the regenerated YAML and confirm it contains 1000 ml/L distilled
  water, a structured DSMZ Medium 1150 reference, no legacy
  `mediaingredientmech_term` on `NaNO3`, and no variable NaOH ingredient.
- Search `data/merge_yaml/merged` for exact `komodo.medium:1150`,
  `mediadive.medium:1150`, and `DSMZ_Medium1150` tokens with
  `rg --no-ignore --hidden`; after equivalence repair they should identify one
  merged source recipe group.
- Re-fetch MediaDive 1150 and the DSMZ Medium 1150 PDF to confirm the
  regenerated ingredients still match the live source records.

## Additional Notes

- The DSMZ Medium 1150 PDF was reachable and agreed with MediaDive 1150.
- The current pH adjustment is represented as a preparation step, which is a
  better shape than the KOMODO sibling's variable-concentration NaOH ingredient.
