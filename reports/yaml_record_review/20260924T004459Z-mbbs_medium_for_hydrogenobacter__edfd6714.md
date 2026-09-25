# YAML Record Review: mbbs_medium_for_hydrogenobacter

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mbbs_medium_for_hydrogenobacter__edfd6714.yaml
- Started UTC: 2026-09-24T00:43:21Z
- Finished UTC: 2026-09-24T00:45:00Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:003242 |
| Label | mbbs_medium_for_hydrogenobacter |
| Original label | MBBS MEDIUM FOR HYDROGENOBACTER |
| Category | bacterial |
| Generated path | data/merge_yaml/merged/mbbs_medium_for_hydrogenobacter__edfd6714.yaml |
| Maintained owner | data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml |
| Source accession | mediadive.medium:J893 |

The merged record is derived from the one maintained bacterial MediaDive import
and only appends merge metadata. Future fixes belong in
`data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml` or the
MediaDive importer that flattened the source recipe.

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mbbs_medium_for_hydrogenobacter__edfd6714.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/mbbs_medium_for_hydrogenobacter__edfd6714.yaml --out /private/tmp/mbbs_medium_for_hydrogenobacter__edfd6714.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. The TSV had only its header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/mbbs_medium_for_hydrogenobacter__edfd6714.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/mbbs_medium_for_hydrogenobacter__edfd6714.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator's expected `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the repository's `just validate-history` target validates standalone `history/` files, not embedded MediaRecipe history lists. |

The green validators did not catch unit/stock-boundary drift because the bad
rows are schema-valid flat ingredient rows.

## Identity and Grounding

- JCM GRMD 893 and MediaDive J893 both identify the source as `MBBS MEDIUM FOR
  HYDROGENOBACTER`.
- A scoped, gitignore-independent exact search of the target, maintained owner,
  ID registry, and normalized MediaDive/recipe indexes found
  `CultureMech:003242` and `mediadive.medium:J893` pointing to
  `data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml`; no
  second J893 owner was found in that searched set.
- A gitignore-independent exact scan of the target and maintained owner found
  no `solutions`, `references`, or `target_organisms` sections.
- The record's `pH 6.0`, liquid state, JCM source URL, and
  `H2-CO2-O2 (80:20:2, v/v)` gas note all agree with the inspected JCM/MediaDive
  source text.

## Evidence

### Supported

- The sulfur row is quantitatively supported: JCM specifies 1 g sulfur powder
  in a 1 L base plus 15 ml of added solutions, and MediaDive expresses that as
  `0.985222` g/l for the final 1015 ml top-level mixture.
- The Modified Brock's salt base ingredient identities and stock amounts match
  the JCM table and MediaDive nested solution.
- The preparation text preserves the source requirements to autoclave base and
  yeast-extract solutions separately, filter-sterilize the bicarbonate solution,
  steam sulfur, mix aseptically, dispense under gas, adjust to pH 6.0 if needed,
  and pressurize inoculated bottles with the same gas mixture.

### Unsupported or Over-scoped

- The top-level JCM recipe uses `10% Yeast extract solution` at 5 ml, but the
  YAML records a direct `Yeast extract` ingredient at `5 G_PER_L`.
- The top-level JCM recipe uses filter-sterilized `8% NaHCO3 solution` at 10 ml,
  but the YAML records a direct `NaHCO3` ingredient at `10 G_PER_L`.
- `Modified Brock's salt base solution` is a named 1 L nested solution in both
  JCM and MediaDive. The YAML lacks a `solutions` entry and presents the base
  solution salts as direct MBBS ingredients.
- `Sulfur` is grounded to `CHEBI:26833` / `sulfur atom`; the source says sulfur
  powder, so the exact supplied bulk form needs to be rechecked.

## Completeness

- The missing `solutions` block is consequential: the source recipe is a 1 L
  Modified Brock's salt base plus measured volumes of 10 percent yeast extract
  and 8 percent bicarbonate solutions, not a one-liter flat list of all
  components.
- `references` is empty. The JCM/MediaDive source is recoverable from
  `media_term`, `notes`, and the import history, but the source URL is not
  represented in a structured citation slot.
- `target_organisms` is empty. The medium name names `Hydrogenobacter`, but the
  record contains no strain-specific growth assertion, so the empty optional
  slot is not itself a defect.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The imported direct yeast-extract and bicarbonate concentrations are not source-supported. | JCM specifies 5 ml of 10 percent yeast extract solution and 10 ml of 8 percent filter-sterilized NaHCO3 solution; the YAML records `5 G_PER_L` yeast extract and `10 G_PER_L` NaHCO3 as if the milliliter solution additions were grams per liter. | `data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml` or the MediaDive importer. |
| major | `Modified Brock's salt base solution` was flattened into direct MBBS ingredients. | JCM and MediaDive make the Brock base a distinct 1 L nested solution; the YAML has no `solutions` block and stores the base salts under top-level `ingredients`. | `data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml` or the MediaDive importer. |
| major | The sulfur grounding should not be trusted without exact-form review. | The source ingredient is sulfur powder; the YAML maps it to `CHEBI:26833` labeled `sulfur atom`, which is narrower than the supplied bulk material. | `data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml`. |
| minor | The single structured preparation action is misleading. | The description includes autoclaving, filter sterilization, sulfur steaming, aseptic mixing, gas exchange, pH adjustment, and pressurization, but the only structured action is `AUTOCLAVE`. | `data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml` or the MediaDive importer. |
| minor | Structured source references are missing. | The JCM/MediaDive identity appears in `media_term`, `notes`, and the import history, but the record has no `references` section. | `data/normalized_yaml/bacterial/mbbs_medium_for_hydrogenobacter.yaml`. |

## Recommended Edits

1. Preserve the main JCM recipe as a solution-based formula: 1 L Modified
   Brock's salt base solution, 5 ml 10 percent yeast-extract solution, 10 ml
   8 percent NaHCO3 solution, and 1 g sulfur powder.
2. Remove or recompute the direct `Yeast extract` and `NaHCO3` grams-per-liter
   concentrations. Do not carry source milliliter volumes into `G_PER_L`.
3. Represent Modified Brock's salt base as a nested solution or a referenced
   `SolutionRecipe`, rather than flattening its ingredient rows into MBBS.
4. Recheck the exact ontology term for sulfur powder and leave it unresolved if
   no verified exact CHEBI or MIM label exists.
5. Split the preparation text into structured actions for autoclaving,
   filter-sterilizing, steaming sulfur, aseptic mixing, gas handling, pH
   adjustment, and inoculated-bottle pressurization.
6. Add structured source metadata for JCM 893 and MediaDive J893.

## Follow-up Checks

- Rerun the focused open-schema, strict, term, and reference validators on the
  maintained owner and regenerated merged record.
- Manually re-read JCM GRMD 893 after curation to confirm that 10 percent yeast
  extract solution and 8 percent NaHCO3 solution are represented as source
  solutions or otherwise unambiguously scoped.
- Re-run a gitignore-independent exact search for `CultureMech:003242`,
  `mediadive.medium:J893`, and `mbbs_medium_for_hydrogenobacter` to confirm that
  the normalized owner, indexes, and regenerated merge all point to the same
  corrected record.

## Additional Notes

- JCM states a default autoclave condition of 121 C for 15 min unless otherwise
  stated; the MBBS-specific text overrides sterilization for NaHCO3 and sulfur.
- MediaDive computes the final top-level liquid volume as 1015 ml. That explains
  the imported sulfur value of `0.985222 G_PER_L`.
