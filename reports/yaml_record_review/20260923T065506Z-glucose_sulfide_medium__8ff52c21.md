# YAML Record Review: glucose_sulfide_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_sulfide_medium__8ff52c21.yaml
- Started UTC: 2026-09-23T06:53:26Z
- Finished UTC: 2026-09-23T06:55:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:009906` |
| Name | `glucose_sulfide_medium` |
| Original name | `Glucose Sulfide Medium` |
| Category | `bacterial` |
| Media term | `TOGO:M515` |
| Maintained parent | `data/normalized_yaml/bacterial/TOGO_M515_Glucose_Sulfide_Medium.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_sulfide_medium__8ff52c21.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_sulfide_medium__8ff52c21.yaml --out /private/tmp/glucose_sulfide_medium__8ff52c21.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_sulfide_medium__8ff52c21.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_sulfide_medium__8ff52c21.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This record denotes Togo M515, a Togo copy of JCM `GRMD=514`, `GLUCOSE SULFIDE MEDIUM`. A gitignore-independent exact search for `TOGO:M515`, `JCM_M514`, `GRMD=514`, and `TOGO_M515_Glucose_Sulfide_Medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the Togo M515 maintained parent, this Togo generated merge, and the direct JCM 514 parent and generated merge.

The main-solution ingredient groundings are narrow, and the water grounding is exact. The Togo import preserves GMO roles and properties in ingredient notes, but those annotations do not compensate for the incorrect unit conversions described below.

## Evidence

Togo M515 and JCM 514 agree on the source structure:

| Source row | Amount |
|---|---:|
| Basal distilled water | 990 ml |
| Vitamin solution addition | 10 ml |
| Vitamin-solution water | 1 L |

The generated Togo record has `Distilled water` at `991.0 G_PER_L` with a note saying it merged `990.0` and `1.0`. That sums rows from two solution scopes and turns source milliliters/liters into grams per liter.

The generated record also has a synthetic `solutions` entry for `Vitamin solution (see below)` with `value: '10'` and `unit: G_PER_L` but no composition. In the source, that row is 10 ml of the vitamin stock, not 10 g/l.

Every vitamin stock amount was imported as if the numeric milligram amount were a g/l concentration. For example, JCM and Togo list 2 mg biotin in a 1 L vitamin stock; the generated Togo record stores Biotin as 2 g/l. The correct final-medium amount after adding 10 ml vitamin stock is 0.00002 g/l, so that row is inflated 100000-fold.

The Togo source comment instructs the curator to add everything except Vitamin solution to distilled water, bring the volume to 990 ml, adjust pH to 7.3, and add filter-sterilized Vitamin solution aseptically after autoclaving. The generated record has no `preparation_steps` and no `ph_value`.

## Completeness

The generated Togo record is incomplete for every stock-related field: water scope, vitamin-stock membership, stock-addition amount, final dilution, pH, and preparation. It also remains split from the direct JCM import of the same `GRMD=514` source.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects here.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Togo M515 water rows from different solution scopes were summed and recoded as `991.0 G_PER_L`. | The Togo payload has 990 ml basal water and 1 L vitamin-stock water; the generated row says `[Merged 2 duplicates: 990.0, 1.0]`. | `data/normalized_yaml/bacterial/TOGO_M515_Glucose_Sulfide_Medium.yaml` or the Togo importer / solution migrator. |
| Major | The 10 ml Vitamin solution addition was converted to an empty `10 G_PER_L` solution. | Togo and JCM make this a 10 ml stock addition; the generated `solutions` entry has no composition and a mass-concentration unit. | Togo solution migration for M515. |
| Major | Vitamin milligram amounts are represented as grams per liter and are therefore 100000-fold too high in the final medium. | JCM 514 puts milligram quantities in a 1 L vitamin stock and adds 10 ml of that stock; the generated record stores values such as Biotin `2 G_PER_L`, Folic acid `2 G_PER_L`, and Pyridoxine hydrochloride `10 G_PER_L`. | Togo unit conversion for nested stock recipes. |
| Major | pH and the post-autoclave Vitamin solution addition step were dropped. | Togo M515 carries the JCM instruction to adjust to pH 7.3 and aseptically add filter-sterilized Vitamin solution after autoclaving; the generated record has no `ph_value` or `preparation_steps`. | Togo importer for comments/preparation. |
| Major | The direct-JCM and Togo imports of JCM `GRMD=514` remain split into two generated records. | Exact ignored-inclusive search found the direct JCM branch at `glucose_sulfide_medium__78413021.yaml` and the Togo branch at `glucose_sulfide_medium__8ff52c21.yaml`; both point to `GRMD=514`. | Togo and direct-JCM import normalization followed by regenerated duplicate matching. |
| Minor | Several vitamin display labels have doubled hyphens or middle-dot artifacts. | The generated Togo record has labels such as `p--Aminobenzoic acid`, `myo--Inositol`, and hydrate names with middle dots. | Togo import label normalization. |

## Recommended Edits

1. Rebuild Togo M515 with separate basal and Vitamin solution scopes: 990 ml water in the basal solution, 1 L water in the Vitamin solution, and a 10 ml stock addition.
2. Convert vitamin stock milligram quantities to 1 L stock concentrations before applying the 10 ml final-medium dilution, or retain them as stock recipe amounts rather than final concentrations.
3. Import the Togo/JCM preparation comment as structured pH 7.3 and post-autoclave filter-sterilized Vitamin solution addition steps.
4. Normalize Togo vitamin labels such as p-aminobenzoic acid and myo-inositol while keeping the source string recoverable.
5. Regenerate merged records and verify the Togo M515 copy merges with `JCM_J514_GLUCOSE_SULFIDE_MEDIUM.yaml` after both branches represent the same stock structure.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation after regenerating the Togo M515 merge.
- Compare the regenerated Togo record with the Togo M515 API payload and live JCM `GRMD=514` table, checking the basal solution, Vitamin solution, 10 ml stock addition, pH, and preparation comment.
- Re-run the exact gitignore-independent search for `TOGO:M515`, `JCM_M514`, `GRMD=514`, and `TOGO_M515_Glucose_Sulfide_Medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` and confirm that only one generated record points to JCM 514.

## Additional Notes

The Togo M515 `curl` failed in the sandbox with a DNS resolution error and succeeded after rerunning `curl -L` with network escalation.
