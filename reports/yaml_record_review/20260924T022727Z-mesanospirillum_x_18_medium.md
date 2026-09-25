# YAML Record Review: Mesanospirillum X-18 Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml
- Started UTC: 2026-09-24T02:25:59Z
- Finished UTC: 2026-09-24T02:27:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007552 |
| Name | mesanospirillum_x_18_medium |
| Original name | Mesanospirillum X-18 Medium |
| Category | bacterial |
| Medium term | TOGO:M1037, Mesanospirillum X-18 Medium |
| Source | TOGO Medium M1037, originally JCM_M984 |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=984 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml |
| Merge fingerprint | 2cf6c5e99e63515b08f89ca9e939581ee2682c3950948e9e0370f95047db09f7 |

This reviewed file is a generated single-source merge from the maintained TOGO owner.
Future fixes belong in `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml`, the TOGO import logic that created that owner, or the source de-duplication and merge logic, then in regenerated `data/merge_yaml/merged/` outputs.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml --out /private/tmp/mesanospirillum_x_18_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only its header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The high-level recipe identity is coherent: `TOGO:M1037` resolves in the TOGO API to `Mesanospirillum X-18 Medium` with `original_media_id` `JCM_M984` and the same JCM `GRMD=984` URL carried in the YAML notes.

The live JCM 984 URL was checked and currently returns a small "Nothing found" medium-data page, so the surviving authoritative evidence for this import is the TOGO M1037 snapshot and the MediaDive J984 snapshot of the same JCM recipe. MediaDive REST record `J984` also names `MESANOSPIRILLUM X-18 MEDIUM`, source `JCM`, the same JCM URL, and pH 6.5.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found two maintained owners and two generated files for this same JCM 984 recipe:

- TOGO owner `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml`, generated as this reviewed `data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml`.
- MediaDive owner `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml`, generated as `data/merge_yaml/merged/mesanospirillum_x_18_medium__248a6ea7.yaml`.

No third exact owner or generated sibling was found in that bounded, ignored-file-inclusive search.

## Evidence

The source database identity, bacterial category, liquid state, and complex/undefined classification are supportable for a JCM medium.

The exact TOGO M1037 component feed supports a main 1 L aqueous recipe containing calcium chloride dihydrate, ammonium chloride, dipotassium hydrogen phosphate, 0.5 mg resazurin, magnesium chloride hexahydrate, sodium bicarbonate, yeast extract, trypticase peptone, a 10 ml Vitamin solution M991 use-site, carbon dioxide gas, and hydrogen gas. It also supports a second group containing 10 ml trace element solution, another 10 ml Vitamin solution M991 use-site, and nitrogen gas; a third group containing 10 ml of 5% L-cysteine HCl hydrate solution; and a separate 1 L trace element stock.

Several quantity claims in the YAML are not supported by that source structure:

- `Resazurin` is recorded as `0.5 G_PER_L`, but the TOGO feed states 0.5 mg and the MediaDive J984 import converts it to `0.000480769 G_PER_L` after the 1040 ml final-volume normalization.
- `Trace element solution (see below)`, both `Vitamin solution (see Medium [M991])` entries, and `5% L-Cysteine x HCl x H2O solution` are recorded as empty stock solutions with `10 G_PER_L`. The source rows are 10 ml additions, not 10 g/L concentrations.
- Trace stock ingredients such as sodium tungstate dihydrate, nitrilotriacetic acid, sodium molybdate dihydrate, and the other metals are flattened into final-medium `ingredients` at their stock `g/L` values. The source defines them inside a 1 L trace stock that is dosed into the medium at 10 ml/L.
- `KOH` is recorded as a variable top-level ingredient of the final medium. In the MediaDive J984 representation of the JCM preparation text, KOH appears only as the reagent used to adjust the trace element stock while dissolving nitrilotriacetic acid.

## Completeness

The generated TOGO merge lacks pH and all preparation steps even though the same JCM 984 recipe in the maintained MediaDive owner has pH 6.5, H2-CO2 80:20 vessel gassing before autoclaving, filter-sterilized post-autoclave additions, a reduction step under N2 for the cysteine solution, trace-stock pH adjustment with KOH, and the 10 to 20% inoculum note.

The reviewed TOGO import preserves the Medium M991 vitamin-solution cross-reference only as two empty solution stubs. It does not resolve the referenced vitamin stock composition or preserve enough group/order metadata to distinguish the two vitamin use-sites from an accidental duplicate.

The generated water row is stale relative to its maintained owner. `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` has already repaired the importer-cleanup artifact from `2.0 G_PER_L` back to `1.0 G_PER_L`; this generated file was last produced on 2026-08-06 and still carries the pre-repair `2.0 G_PER_L` value.

No target-organism, literature growth, or variant claims are present in this generated record, so there were no organism or growth-evidence claims to check.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated file is stale relative to its maintained TOGO owner. | The generated water row is `2.0 G_PER_L` with a 2026-08-06 merge event, while `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` has a 2026-09-02 repair event and `Distilled water` back at `1.0 G_PER_L`. | Regenerate from `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml`; no direct generated-file edit. |
| Major | TOGO milliliter solution rows were imported as gram-per-liter solution concentrations and left without composition. | The TOGO source has 10 ml additions for the trace solution, each Medium M991 vitamin-solution use-site, and the 5% L-cysteine solution; the YAML writes those as empty `solutions` with `concentration: 10 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` and the TOGO import logic that maps TOGO component units. |
| Major | The trace element stock is conflated with final-medium ingredients. | TOGO M1037 puts sodium molybdate, boric acid, nickel chloride, zinc sulfate, copper sulfate, sodium selenite, nitrilotriacetic acid, sodium tungstate, manganese sulfate, ferrous ammonium sulfate, aluminum chloride, water, and KOH in a separate trace element solution. The YAML stores most of those as final-medium ingredients at the stock `g/L` values. | `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` and the TOGO importer stock-boundary transform. |
| Major | The resazurin amount is 1000x too high before final-volume effects. | TOGO M1037 states 0.5 mg resazurin; the YAML states `0.5 G_PER_L`. The MediaDive J984 sibling normalizes the same row to `0.000480769 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` and the TOGO unit-conversion rule. |
| Major | Two maintained owners represent the same JCM 984 recipe and merge into two generated records. | The TOGO owner carries `Original source: JCM - JCM_M984` and `GRMD=984`; the MediaDive owner carries `Source: JCM`, `mediadive.medium:J984`, and the same JCM URL. The gitignore-independent exact search found both generated outputs. | Source de-duplication or merge rules for `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` and `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml`. |
| Major | The TOGO path drops JCM preparation and pH context that is available from the duplicate MediaDive import. | MediaDive J984 records pH 6.5 and four preparation/comment steps for gassing, autoclaving, post-autoclave additions, cysteine reduction, trace-stock KOH adjustment, and inoculum size. This generated TOGO record has no `ph_value` or `preparation_steps`. | Prefer de-duplicating against or enriching from `data/normalized_yaml/bacterial/mesanospirillum_x_18_medium.yaml` rather than manually editing the generated TOGO output. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml` from the maintained TOGO owner so the generated water row reflects the 2026-09-02 upstream repair.
2. Fix the TOGO importer path for `data/normalized_yaml/bacterial/TOGO_M1037_Mesanospirillum_X-18_Medium.yaml` so TOGO `ml` solution additions remain solution use-sites and do not become `G_PER_L` concentrations.
3. Fix the TOGO importer milligram conversion that mapped 0.5 mg resazurin to `0.5 G_PER_L`.
4. Preserve nested stock boundaries for the trace element solution, Medium M991 vitamin solution, and 5% L-cysteine solution before regenerating this merge.
5. Add or resolve an alias between TOGO `M1037` / `JCM_M984` and MediaDive `J984` so `merge_recipes.py` emits one Mesanospirillum X-18 Medium record rather than the TOGO and MediaDive siblings.
6. After de-duplication, prefer the JCM preparation details and pH preserved by the MediaDive J984 import unless direct JCM evidence becomes available again and conflicts.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the maintained TOGO owner after importer fixes and on the regenerated `data/merge_yaml/merged/mesanospirillum_x_18_medium.yaml`.
- Re-run the merge generator and verify no generated file named `mesanospirillum_x_18_medium__*.yaml` remains for the same JCM 984 source.
- Compare regenerated source rows against TOGO M1037 and MediaDive J984 for `Resazurin`, all 10 ml stock additions, and KOH.
- Manually verify that the Medium M991 vitamin solution is either resolved to an explicit stock recipe or retained as two grouped, ordered cross-reference use-sites with no unsupported stock composition.
- Recheck that the generated record contains pH and preparation context, or records a concrete data-layer reason why the TOGO-only projection intentionally excludes MediaDive J984 preparation text.

## Additional Notes

The live JCM URL was unavailable during review and returned "Nothing found"; TOGO M1037 and MediaDive J984 were treated as preserved database snapshots of that JCM source rather than independent literature support.

The gas rows for hydrogen, carbon dioxide, and nitrogen are better treated as preparation atmosphere than final ingredients, but they are secondary to the milliliter and stock-boundary errors above.
