# YAML Record Review: man_rogosa_and_sharpe_mrs_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/man_rogosa_and_sharpe_mrs_medium.yaml
- Started UTC: 2026-09-23T23:04:42Z
- Finished UTC: 2026-09-23T23:04:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009444 |
| name | man_rogosa_and_sharpe_mrs_medium |
| original_name | Man, Rogosa, and Sharpe (MRS) medium |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M2906, Man, Rogosa, and Sharpe (MRS) medium |
| generated path | data/merge_yaml/merged/man_rogosa_and_sharpe_mrs_medium.yaml |
| maintained owner | data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml |

The reviewed YAML is a derived merge artifact. Its terminal curation event reports a merge from the single normalized owner on fingerprint `63b6fbf7dbf5f28013f092fefcce446b26958fe1aac4389c15d99627e02296c4`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009444`, `TOGO:M2906`, `M2906`, and `Man, Rogosa, and Sharpe \(MRS\) medium` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or TOGO identifier. An ignored-file-inclusive filename search under `data/normalized_yaml` found only `data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml` for the exact generated stem.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/man_rogosa_and_sharpe_mrs_medium.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/man_rogosa_and_sharpe_mrs_medium.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The record identity agrees with TOGO M2906 at the medium level. The TOGO payload for `M2906` reports the same source name, `Man, Rogosa, and Sharpe (MRS) medium`, and the same component list that this generated CultureMech record attempts to represent.

Supported grounding:

| Ingredient | Source text in TOGO M2906 | CultureMech grounding |
|---|---|---|
| Distilled water | Distilled water, 1 L | CHEBI:15377, water |
| Yeast extract | Yeast extract, 4 g | Unresolved undefined component |
| Dipotassium hydrogen phosphate | Dipotassium hydrogen phosphate, 2 g | CHEBI:131527, dipotassium hydrogen phosphate |
| Sodium acetate | Sodium acetate, 5 g | CHEBI:32954, sodium acetate |
| Tween 80 | Tween 80, 1 ml | CHEBI:53426, polysorbate 80 |
| Magnesium sulfate | Magnesium sulfate, 0.2 g | CHEBI:32599, magnesium sulfate |
| Triammonium citrate | Triammonium citrate, 2 g | CHEBI:63037, triammonium citrate |
| Glucose | Glucose, 20 g | CHEBI:17234, glucose |
| Beef extract | Beef extract, 10 g | Unresolved undefined component |
| Peptone | Peptone, 10 g | Unresolved undefined component |

One grounding is over-specific relative to the inspected TOGO payload: the source says `Manganese sulfate`, while the record grounds the component to CHEBI:86364, `manganese(II) sulfate monohydrate`. The packaged MediaIngredientMech label index also maps the exact label `Manganese sulfate` to `MnSO4 x H2O`, so this should be resolved as a narrow curation decision rather than by guessing a sibling hydrate.

## Evidence

TOGO M2906 supports the recipe identity and the 11-component list. The nine solid ingredients have the same numeric gram amounts in the generated record as in the inspected TOGO response for a 1 L MRS recipe: 4 g yeast extract, 2 g dipotassium hydrogen phosphate, 5 g sodium acetate, 0.2 g magnesium sulfate, 2 g triammonium citrate, 0.05 g manganese sulfate, 20 g glucose, 10 g beef extract, and 10 g peptone.

Two TOGO volume components are not represented faithfully:

| Component | TOGO amount | Record amount |
|---|---:|---:|
| Distilled water | 1 L | 1 G_PER_L |
| Tween 80 | 1 ml | 1 G_PER_L |

The record omits structured pH even though TOGO M2906 has `ph: 6.2` in metadata and repeats pH 6.2 in a source comment. The same comment scopes a 37 C, no-shaking cultivation condition to the reported Lactobacillus casei LC2W culture from Chen et al. 2014; that should not be converted into a universal MRS property without the paper, but it is a citable lead for a bounded growth-evidence curation pass.

The imported `notes` field points to `https://togomedium.org/medium/M2906`, and the first history event records `Source: TOGO, ID: M2906`. Those entries recover the upstream source, but the record has no structured citation or evidence object for the Chen et al. 2014 statement embedded in TOGO.

## Completeness

Missing or incomplete:

- The source pH value of 6.2 is not present as a structured `pH` value or in any note. An ignored-file-inclusive exact search for pH, temperature, shaking, preparation, sterilization, target organism, and growth metric keys in the normalized owner and generated copy returned no matches.
- The CultureMech record has no structured target-organism or growth-evidence block for the Lactobacillus casei LC2W culture described in the TOGO comment. A curator should inspect Chen et al. 2014 before adding a taxon, strain, temperature, shaking condition, or citation.

Complete enough:

- No stock-solution references are needed; TOGO lists all components directly.
- The source formula directly lists a liquid 1 L recipe. The agar-at-15-g/L and erythromycin-at-10-mg/L comments in TOGO describe conditional additions, not mandatory base MRS ingredients, so their absence from this base liquid record is acceptable unless they are curated as variants.
- The empty structured reference set is consistent with a raw TOGO import that only retained the database URL and import history.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Two liquid source amounts were converted to mass concentration. `Distilled water` is stored as `1 G_PER_L` instead of the source `1 L`, and `Tween 80` is stored as `1 G_PER_L` instead of the source `1 ml`. | TOGO M2906 lists `Distilled water` with `volume: 1`, `unit: L` and `Tween 80` with `volume: 1`, `unit: ml`; the generated YAML stores both as `unit: G_PER_L`. The schema includes `ML_PER_L`, so Tween 80 can be represented without a mass-density assumption. | data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml; if other TOGO imports repeat this pattern, the TOGO unit-normalization code should be fixed before regenerating them |
| major | The pH supported by TOGO is missing. | TOGO M2906 reports metadata `ph: 6.2`; the normalized owner and generated copy contain no pH field or note matching a pH/temperature/shaking/preparation search. | data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml |
| major | The manganese sulfate CHEBI grounding is hydrate-specific without hydrate evidence in the inspected TOGO payload. | TOGO M2906 names `Manganese sulfate`; the generated record asserts CHEBI:86364, `manganese(II) sulfate monohydrate`. Hydration state is identity-significant for salts. | data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml, or the MediaIngredientMech mapping if the exact `Manganese sulfate` label should no longer resolve to `MnSO4 x H2O` |
| minor | Source provenance is only a free-text database URL plus import history. | The record has `notes: Source: https://togomedium.org/medium/M2906` but no structured source-data block or citation for the Chen et al. 2014 growth comment in TOGO. | data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml |

## Recommended Edits

1. Correct the two volume components in `data/normalized_yaml/bacterial/man_rogosa_and_sharpe_mrs_medium.yaml`: represent `Tween 80` as `1 ML_PER_L`, and represent the `1 L` distilled-water basis as `1000 ML_PER_L` or another schema-supported volume basis that does not claim grams.
2. Add the TOGO-supported pH 6.2 to the normalized record.
3. Resolve the `Manganese sulfate` grounding. Either add source support that TOGO `GMO_001763` denotes the monohydrate in this recipe or loosen the record so it does not assert unsupported hydrate specificity.
4. Optionally add a structured source-data or evidence entry for TOGO M2906, and inspect Chen et al. 2014 before adding Lactobacillus casei LC2W, 37 C, and static-culture growth details.

## Follow-up Checks

- Rerun the open schema, strict, term, and reference validators on the normalized record and on the regenerated merged record.
- Rerun merge generation and `just verify-merges` or the focused merge-freshness check that covers `man_rogosa_and_sharpe_mrs_medium`.
- Re-fetch TOGO M2906 and confirm the regenerated record keeps all nine gram quantities, changes the two volume quantities only, and carries pH 6.2.
- If manganese sulfate is fixed through MediaIngredientMech mapping, rerun the MIM label-index check and the term validator over this record.

## Additional Notes

- `applications: Microbial cultivation` is a broad classification and is consistent with a TOGO medium used to culture Lactobacillus casei LC2W.
- Triammonium citrate has CHEBI:63037 in the record but lacks the redundant `mediaingredientmech_chebi_term` companion that the other CHEBI-grounded simple compounds carry. The current packaged label index has an exact `Triammonium citrate` mapping to `(NH4)3 citrate`; adding the companion link would be a cleanup, not an identity blocker.
