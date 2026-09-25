# YAML Record Review: METALLOSPHAERA CUPRINA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/metallosphaera_cuprina_medium__36e15dec.yaml
- Started UTC: 2026-09-24T02:34:02Z
- Finished UTC: 2026-09-24T02:34:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003091 |
| Name | metallosphaera_cuprina_medium |
| Original name | METALLOSPHAERA CUPRINA MEDIUM |
| Category | archaea |
| Medium term | mediadive.medium:J748, JCM Medium J748 |
| Source | JCM via MediaDive |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=748 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml |
| Merge fingerprint | 36e15decaad6aeeba136148cfba1d9b87bba320fb020f9a5f30be05f642bcb77 |

This generated record is a single-source merge from `data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml`.
Future fixes belong in that maintained MediaDive/JCM owner or in source-alias rules that should merge the duplicate TOGO M773 copy before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/metallosphaera_cuprina_medium__36e15dec.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/metallosphaera_cuprina_medium__36e15dec.yaml --out /private/tmp/metallosphaera_cuprina_medium__36e15dec.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/metallosphaera_cuprina_medium__36e15dec.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/metallosphaera_cuprina_medium__36e15dec.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The MediaDive identity is correct: REST medium `J748` is named `METALLOSPHAERA CUPRINA MEDIUM`, points to the inspected JCM `GRMD=748` URL, has pH 3.5, and describes an archaeal cultivation medium.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found two maintained owners for the same JCM 748 source: this MediaDive owner at `data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml` and the TOGO owner at `data/normalized_yaml/archaea/TOGO_M773_Metallosphaera_Cuprina_Medium.yaml`. No third exact owner for JCM 748 / Metallosphaera Cuprina Medium was found in that bounded, ignored-file-inclusive search.

The ChEBI groundings on main salts and most trace salts match the formula strings closely enough for this review. The manganese sulfate hydrate row remains intentionally generic because the source uses a variable hydrate.

## Evidence

The JCM 748 page and MediaDive J748 payload support the main 1 L recipe: ammonium sulfate 3 g, potassium dihydrogen phosphate 0.5 g, magnesium sulfate heptahydrate 0.5 g, potassium chloride 0.1 g, calcium nitrate 0.01 g, yeast extract 2 g, Tryptone (BD-Difco) 0.5 g, and distilled water to 1 L.

JCM and MediaDive also support the pH 3.5 autoclave step followed by aseptic addition of 2.0 ml of filter-sterilized Trace element solution.

The trace ingredients in the YAML are not final-medium ingredients. The source defines a separate 1 L Trace element solution holding ferric chloride hexahydrate, copper sulfate pentahydrate, boric acid, manganese sulfate hydrate, sodium molybdate dihydrate, cobalt chloride hexahydrate, zinc sulfate heptahydrate, and distilled water. Only 2.0 ml of that stock is added to the cooled main medium.

## Completeness

The record has no target-organism, strain, literature growth, or variant claims, so there were no growth-evidence assertions to check.

The preparation text still tells the reader to add 2.0 ml of Trace element solution, but the generated record has no `solutions` entry that represents that stock. The record is therefore incomplete even though every trace stock component appears somewhere in `ingredients`.

The `BD-Difco` source attribute on Tryptone is dropped in this MediaDive projection; the TOGO sibling preserves it in the preferred term.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Trace element solution was flattened into top-level ingredients at stock strength. | JCM 748 and MediaDive J748 define a 1 L filter-sterilized Trace element solution, then add 2.0 ml to the main medium after cooling. The YAML records the seven trace salts as direct final-medium `G_PER_L` rows at the stock concentrations. | `data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml` and MediaDive importer stock handling. |
| Major | The preparation step references a stock that is missing structurally. | The YAML says to aseptically add 2.0 ml Trace element solution after cooling, but has no `solutions` object for that stock and no way to connect the 2.0 ml dose to the trace composition. | `data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml`. |
| Major | JCM 748 is duplicated through MediaDive and TOGO import paths. | This owner and `data/normalized_yaml/archaea/TOGO_M773_Metallosphaera_Cuprina_Medium.yaml` both cite `GRMD=748` and merge to separate generated files. | Source aliasing for MediaDive J748 and TOGO M773, plus a regenerated merge. |
| Minor | Tryptone supplier detail is lost. | The JCM and MediaDive source row is `Tryptone` with `BD-Difco`; the YAML stores only `Tryptone`. | `data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml`. |

## Recommended Edits

1. Preserve the filter-sterilized Trace element solution as a nested stock solution dosed at 2.0 ml per 1 L main medium, instead of flattening its contents into `ingredients`.
2. Attach the post-autoclave aseptic addition step to that 2.0 ml stock use-site so the formula and preparation text agree.
3. Preserve the `BD-Difco` attribute on Tryptone.
4. Add a source alias between MediaDive J748 and TOGO M773 so one generated Metallosphaera Cuprina Medium record is emitted for JCM 748.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on `data/normalized_yaml/archaea/metallosphaera_cuprina_medium.yaml` and the regenerated merge output.
- Compare the regenerated record against live JCM `GRMD=748`: the seven main ingredients should remain top-level, the seven trace salts should live only inside the Trace element solution, and the solution dose should be 2.0 ml.
- Search `data/merge_yaml/merged` with ignored files included for exact `GRMD=748`, `mediadive.medium:J748`, and `TOGO:M773` after merge regeneration; the same JCM source should not publish as both a MediaDive and TOGO record.

## Additional Notes

The TOGO M773 owner keeps Trace element solution as an empty solution stub rather than flattening it into direct final-medium ingredients. That sibling still needs the same nested-stock reconstruction, but its current failure mode is less likely to be mistaken for correct final trace concentrations.
