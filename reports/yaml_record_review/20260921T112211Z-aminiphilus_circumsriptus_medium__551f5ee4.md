# YAML Record Review: aminiphilus_circumsriptus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml`
- Started UTC: 2026-09-21T11:21:27Z
- Finished UTC: 2026-09-21T11:22:12Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002898` |
| Name | `aminiphilus_circumsriptus_medium` |
| Original name | `AMINIPHILUS CIRCUMSRIPTUS MEDIUM` |
| Source identity | JCM Medium J550, `mediadive.medium:J550` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/aminiphilus_circumsriptus_medium.yaml` |

The generated record is a one-source merge and matches the normalized JCM owner. It has a TOGO sibling at `data/normalized_yaml/bacterial/TOGO_M552_Aminiphilus_Circumsriptus_Medium.yaml` for the same original JCM_M550 recipe.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml --out /private/tmp/aminiphilus_circumsriptus_medium__551f5ee4.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The top-level identity fields agree that this is the JCM J550 Aminiphilus circumsriptus medium:

- `id: CultureMech:002898`
- `name: aminiphilus_circumsriptus_medium`
- `media_term.preferred_term: JCM Medium J550`
- `media_term.term.id: mediadive.medium:J550`
- `notes: Source: JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=550`

The root ingredient list does not agree with JCM J550. The source lists `Trace minerals (see Medium No. 151)` as a 10 ml addition; the record expanded JCM 151's trace-minerals stock into root final-medium ingredients at stock strength and summed the JCM 151 1 g/L NaCl stock row with JCM 550's 10 g/L basal NaCl.

Grounding is exact for most simple salts. Remaining grounding gaps:

- `Yeast extract` and `Peptone` are ungrounded.
- `MnSO4 x n H2O` has the generic manganese(II) sulfate primary term but no `mediaingredientmech_chebi_term`.

## Evidence

Inspected source documents:

- JCM Medium J550 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=550`
- JCM Medium 151 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151`
- TOGO Medium M552 API at `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M552`

Supported claims:

- JCM J550 and TOGO M552 both support the Aminiphilus circumsriptus identity, JCM_M550 accession, pH 7.0, N2 atmosphere, Hungate-tube distribution, butyl-stopper sealing, and autoclaving.
- JCM J550 supports the basal rows: 0.3 g KH2PO4, 0.3 g K2HPO4, 1 g NH4Cl, 10 g NaCl, 0.1 g KCl, 0.1 g CaCl2, 0.5 g MgCl2 x 6 H2O, 2 g yeast extract, 10 g peptone, 0.5 g L-cysteine HCl x H2O, and 1 L distilled water.
- JCM J550 supports adding 10 ml/L of the JCM 151 trace-minerals solution.
- JCM 151 supports the trace-minerals stock composition that was expanded into the JCM record.

Unsupported or mismatched claims:

- JCM J550 does not support a final 10.90099 g/L NaCl concentration.
- JCM J550 does not support final 1.5 g/L nitrilotriacetic acid, 3 g/L MgSO4 x 7 H2O, or other full-strength JCM 151 trace-minerals stock rows in the root ingredient list.
- Preparation step 2 is the JCM 151 trace-minerals stock preparation, but it appears as though it belongs to the final JCM J550 medium.
- The TOGO M552 sibling keeps the trace-minerals row as a solution placeholder but stores it as `10 G_PER_L` with an empty composition, so neither import currently models the 10 ml/L JCM 151 stock correctly.

## Completeness

Consequential gaps:

- The 10 ml/L JCM 151 trace-minerals stock is not represented as a stock solution.
- Trace-minerals stock salts are at the wrong concentration layer.
- The JCM and TOGO copies of the same JCM_M550 recipe are not reconciled.
- Yeast extract and peptone are ungrounded.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- No storage condition was asserted by JCM.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*aminiphilus_circumsriptus_medium__551f5ee4.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the Aminiphilus slug, spelling variants, and `551f5ee4` found this JCM owner, the adjacent TOGO M552 owner, this generated output, and the older uppercase TOGO generated artifact.

## Findings

### Blocker

1. **JCM 151 trace minerals were flattened into the final JCM J550 recipe and merged with basal salts.**

   Evidence: JCM J550 lists `Trace minerals (see Medium No. 151)` at 10 ml/L. JCM 151 lists a trace-minerals stock containing 1 g/L NaCl, 1.5 g/L nitrilotriacetic acid, 3 g/L MgSO4 x 7 H2O, and other salts. The CultureMech final record includes those stock rows as direct final-medium ingredients and sums the 1 g/L trace-stock NaCl with the basal NaCl, leaving `NaCl: 10.90099 G_PER_L` with a `Merged 2 duplicates` note.

   Owner: reify the JCM 151 trace-minerals stock as a solution added at 10 ml/L in `data/normalized_yaml/bacterial/aminiphilus_circumsriptus_medium.yaml`, remove the full-strength stock rows from the final ingredient list, and regenerate.

### Major

1. **JCM 151 trace-stock preparation is stored as a JCM J550 final-medium step.**

   Evidence: generated step 2 starts with dissolving nitrilotriacetic acid and adjusting pH to 6.5 with KOH before adding minerals. JCM 151 shows that instruction below the trace-minerals stock table, not as a second final-medium step for JCM J550.

   Owner: attach that instruction to the trace-minerals solution, not to `preparation_steps` for the main JCM J550 recipe.

2. **The JCM and TOGO imports of JCM_M550 remain two canonical outputs.**

   Evidence: `data/normalized_yaml/bacterial/TOGO_M552_Aminiphilus_Circumsriptus_Medium.yaml` names the same original JCM_M550 source, but it stores distilled water as `1 G_PER_L`, adds N2 as a variable ingredient, and migrates the 10 ml trace-minerals row to an empty `Unknown solution` at `10 G_PER_L`. Those artifacts keep it separate from the JCM generated output.

   Owner: repair TOGO M552 with the same 10 ml/L JCM 151 solution model and reconcile it with the JCM import during merge generation.

### Minor

1. **Undefined basal ingredients are ungrounded.**

   Evidence: JCM supports the 2 g/L yeast extract and 10 g/L peptone rows, but both rows lack exact ontology terms in the JCM record.

   Owner: ground yeast extract and peptone during ingredient enrichment if exact terms are available.

## Recommended Edits

1. Model JCM 151 trace minerals as a reusable solution and attach it to the JCM J550 medium at 10 ml/L.
2. Remove JCM 151 stock ingredients from the JCM J550 root ingredient list; keep only the true JCM J550 basal rows plus the trace-minerals solution reference.
3. Move the nitrilotriacetic-acid/KOH preparation instruction onto the JCM 151 trace-minerals solution.
4. Apply the same solution model to TOGO M552 and correct its water, N2, and trace-minerals placeholder artifacts.
5. Reconcile the JCM and TOGO imports of JCM_M550 during merge generation.
6. Ground yeast extract, peptone, and the generic manganese sulfate stock row where exact local terms exist.
7. Regenerate generated merge records and rendered products.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected JCM and TOGO normalized owners plus the regenerated output.
- Rerun duplicate merging and confirm the JCM and TOGO copies of JCM_M550 are no longer unreconciled.
- Manually compare the regenerated JCM output against JCM J550 and JCM 151 to confirm NaCl is no longer summed with the trace-stock NaCl and the trace stock is added at 10 ml/L.
- Inspect the rendered page and confirm the trace-minerals preparation is displayed under the solution rather than as a main-medium pH step.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/aminiphilus_circumsriptus_medium__551f5ee4.yaml`, its normalized owner, the TOGO sibling, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/aminiphilus_circumsriptus_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M552_Aminiphilus_Circumsriptus_Medium.yaml`, and the import/merge rules that currently mishandle JCM stock links.
