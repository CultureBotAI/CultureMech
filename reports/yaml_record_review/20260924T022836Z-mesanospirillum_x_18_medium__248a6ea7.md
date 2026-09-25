# YAML Record Review: MESANOSPIRILLUM X-18 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mesanospirillum_x_18_medium__248a6ea7.yaml
- Started UTC: 2026-09-24T02:28:33Z
- Finished UTC: 2026-09-24T02:28:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003333 |
| Name | mesanospirillum_x_18_medium |
| Original name | MESANOSPIRILLUM X-18 MEDIUM |
| Category | bacterial |
| Medium term | mediadive.medium:J984, MESANOSPIRILLUM X-18 MEDIUM |
| Source | MediaDive J984, source JCM |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=984 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml |
| Merge fingerprint | 248a6ea7dd357b4480041f905b4d6ac1493d8102612156e4486037f316e41c9d |

This generated record is a single-source merge from `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml`.
Future edits belong in that maintained MediaDive owner, the MediaDive import path that generated it, or in source de-duplication rules that merge this JCM record with the TOGO M1037 copy before `data/merge_yaml/merged/` is regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mesanospirillum_x_18_medium__248a6ea7.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mesanospirillum_x_18_medium__248a6ea7.yaml --out /private/tmp/mesanospirillum_x_18_medium__248a6ea7.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mesanospirillum_x_18_medium__248a6ea7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mesanospirillum_x_18_medium__248a6ea7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The MediaDive identity resolves to one JCM recipe: MediaDive REST record `J984` is named `MESANOSPIRILLUM X-18 MEDIUM`, has source `JCM`, points to the JCM `GRMD=984` URL, and records pH 6.5.

The live JCM 984 URL was checked and currently returns a "Nothing found" medium-data page, so MediaDive J984 and TOGO M1037 are preserved snapshots of the JCM source rather than independently inspected live JCM content.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found a duplicate TOGO owner for the same JCM 984 source: `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml`, generated as `data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml`. No third exact owner or generated sibling was found in that bounded, ignored-file-inclusive search.

## Evidence

The MediaDive J984 payload supports the recipe name, JCM provenance, pH 6.5, complex-medium classification, the main 1040 ml solution, the trace element stock, the vitamin stock, and the preparation text imported into the YAML.

The top-level main-medium quantities for yeast extract, trypticase peptone, ammonium chloride, magnesium chloride hexahydrate, calcium chloride dihydrate, dipotassium hydrogen phosphate, sodium bicarbonate, and resazurin are supported by MediaDive's `g_l` normalization over the 1040 ml main solution.

The flattened stock ingredients are not supported as final-medium concentrations:

- MediaDive defines `Trace elements solution` as a 1 L stock added to the main medium at 10 ml, but the YAML records nitrilotriacetic acid and each trace metal as a final-medium `G_PER_L` ingredient at the stock concentration.
- MediaDive defines `Vitamin solution` as a 1 L stock and uses it twice at 10 ml per use-site, but the YAML records each vitamin as a top-level `G_PER_L` ingredient at the stock concentration and loses the two 10 ml addition boundaries.
- MediaDive defines the cysteine row as 10 ml of a 5% `L-Cysteine HCl x H2O` solution; the YAML records `L-Cysteine HCl x H2O` as `10 G_PER_L`, which is the source volume with the wrong dimension and without the 5% stock strength.

The imported preparation text is real but no longer scoped exactly. In the MediaDive payload, the nitrilotriacetic acid / KOH pH adjustment belongs to the trace element stock. In the YAML, it is appended as a top-level step after the main-medium sterilization and cysteine addition steps.

## Completeness

This MediaDive-generated sibling keeps pH and the JCM preparation prose that the TOGO M1037 generated record lacks. It is therefore the richer local input for JCM 984, but it still needs stock-solution structure before it can be the sole merged record for Mesanospirillum X-18 Medium.

Supplier attributes from the MediaDive rows are not retained for `Yeast extract` and `Trypticase peptone`; the payload marks them as `BD-Difco` and `BD-BBL`, respectively.

The source recipe includes water rows for the 1040 ml main solution and the 1 L trace and vitamin stocks. Because the MediaDive import flattened only rows with numeric `g_l` values, those water rows are absent from the generated ingredient list.

No target-organism, literature growth, or variant claims are present in this generated record, so there were no organism or growth-evidence claims to check.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace element stock rows are conflated with final-medium ingredients. | MediaDive J984 defines a 1 L `Trace elements solution` with nitrilotriacetic acid and the trace metals, then doses that stock into the main solution at 10 ml. The YAML records those stock recipe rows as direct final-medium ingredients at stock `g/L` values. | `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` and the MediaDive importer stock-boundary transform. |
| Major | Vitamin stock rows are flattened and their two use-sites are lost. | MediaDive J984 has one 1 L vitamin stock and two 10 ml additions to the main solution. The YAML has the ten vitamin compounds once at their stock concentrations and has no `solutions` entry or grouped use-site for either addition. | `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` and the MediaDive importer solution handling. |
| Major | The 5% cysteine stock volume is imported as an unsupported `G_PER_L` ingredient. | The MediaDive main solution row is 10 ml of `L-Cysteine HCl x H2O` with attribute `5%`; the YAML has `L-Cysteine HCl x H2O` at `10 G_PER_L`. | `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` and the MediaDive importer unit mapping for attributed liquid stock rows. |
| Major | Trace-stock preparation text is detached from its stock-solution context. | The KOH pH-adjustment step belongs to the MediaDive trace-element solution payload, but the YAML appends it as top-level `preparation_steps[3]` after the main-medium post-autoclave and cysteine-reduction steps. | `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` and nested solution preservation in the MediaDive importer. |
| Major | Two generated records represent the same JCM 984 medium. | This record and `data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml` both point to the JCM `GRMD=984` recipe through MediaDive `J984` and TOGO `M1037` / `JCM_M984`. | Source de-duplication or merge rules for the MediaDive and TOGO normalized owners. |
| Minor | Undefined component supplier attributes were dropped. | MediaDive J984 carries `BD-Difco` for yeast extract and `BD-BBL` for trypticase peptone, but the YAML records only generic `Yeast extract` and `Trypticase peptone`. | `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` and MediaDive importer handling of ingredient attributes. |

## Recommended Edits

1. Preserve the MediaDive trace element and vitamin recipes as stock-solution structures instead of flattening stock `g/L` values into final-medium `ingredients`.
2. Represent both 10 ml Vitamin solution use-sites distinctly, or fold them only with explicit arithmetic that accounts for the two additions.
3. Convert the 10 ml 5% cysteine solution row into a stock use-site instead of `10 G_PER_L`.
4. Keep the trace-stock KOH pH adjustment on the trace element solution when stock solutions become representable.
5. Add a MediaDive-JCM/TOGO-JCM source alias so MediaDive `J984` and TOGO `M1037` merge into one Mesanospirillum X-18 Medium record.
6. Preserve `BD-Difco` and `BD-BBL` as source attributes or notes on the undefined yeast extract and trypticase peptone rows.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` and the regenerated merge output after importer fixes.
- Re-run the merge generator and verify the exact source search over `data/merge_yaml/merged` finds one generated JCM 984 recipe instead of both `mesanospirillum_x_18_medium.yaml` and `mesanospirillum_x_18_medium__248a6ea7.yaml`.
- Compare regenerated trace, vitamin, and cysteine solution structures against MediaDive REST `J984`, including `solution_id` 5014 and 4964 and the two 10 ml vitamin rows in solution 5013.
- Confirm that the pH 6.5 value and main-medium gassing/autoclaving steps remain attached to the final medium, while the KOH adjustment stays attached to the trace element stock.

## Additional Notes

The source records disagree in detail because TOGO M1037 lacks pH and preparation steps while MediaDive J984 preserves them. That is a completeness difference between database snapshots of the same JCM source, not evidence for two separate Mesanospirillum X-18 Medium recipes.
