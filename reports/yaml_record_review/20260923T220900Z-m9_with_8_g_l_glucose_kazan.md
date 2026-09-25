# YAML Record Review: m9_with_8_g_l_glucose_kazan

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml
- Started UTC: 2026-09-23T22:06:42Z
- Finished UTC: 2026-09-23T22:09:00Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml`.

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007013 |
| Name | m9_with_8_g_l_glucose_kazan |
| Source accession | MEDIADB:125 |
| Source label in MediaDB | M9 with 8 g/l glucose (kazan) |
| Category | bacterial |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; owned by `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml` plus the merge generator in `src/culturemech/merge/merge_recipes.py` |

`data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml` is the
maintained source record. The merged record also carries generated
`merged_from`/`synonyms` metadata for the 2, 4, 16, 32, and 8 g/L MediaDB
Kazan glucose records.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml` | Passed: `No issues found`. |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml --out /private/tmp/m9_with_8_g_l_glucose_kazan.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 reference checks, all validations passed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded history | Not run | Not checked: the repository `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` arrays. |

These checks prove only LinkML shape, closed-schema shape, resolvable modeled
references, and modeled term syntax. They do not compare merged records with
MediaDB or verify source support.

## Identity and Grounding

MediaDB medium 125 identifies `M9 with 8 g/l glucose (kazan)` with 11
compounds, one organism, one source, and one growth-data record. Its tabular
export reports beta-D-Glucose at 44.405 mM with CHEBI 15903. The maintained
normalized record keeps that same MediaDB accession, display label, glucose
amount, and CHEBI grounding.

The generated merged record no longer has a one-source identity:

- It remains named `m9_with_8_g_l_glucose_kazan` and still points at
  `MEDIADB:125`.
- It reports beta-D-Glucose at `88.8099` mM, which is MediaDB medium 126,
  `M9 with 16 g/l glucose (kazan)`, not medium 125.
- It says the canonical record was merged from
  `m9_with_16_g_l_glucose_kazan`, `m9_with_2_g_l_glucose_kazan`,
  `m9_with_32_g_l_glucose_kazan`, `m9_with_4_g_l_glucose_kazan`, and
  `m9_with_8_g_l_glucose_kazan`, even though MediaDB exports distinct
  beta-D-Glucose amounts of 11.1012, 22.2025, 44.405, 88.8099, and 177.62
  mM for MediaDB IDs 123, 124, 125, 126, and 127.
- Its `original_name` and `media_term.term.label` have the old truncated
  value `'M9 with 8 g/l glucose (kazan`; the maintained normalized record was
  already repaired to `M9 with 8 g/l glucose (kazan)`.

The record has an internally consistent `CultureMech:007013`/`MEDIADB:125`
identity only before the generated merge layer.

## Evidence

Supported by inspected source:

| Claim | Assessment |
|---|---|
| `MEDIADB:125` denotes `M9 with 8 g/l glucose (kazan)` | Supported by the MediaDB medium 125 page and `media_text/125/`. |
| The 8 g/L formulation has 11 MediaDB compounds | Supported by MediaDB medium 125 and its tab-delimited export. |
| The 8 g/L formulation contains beta-D-Glucose at 44.405 mM | Supported by `media_text/125/`; contradicted by the generated merged value of 88.8099 mM. |
| The 8 g/L formulation contains L-Leucine 0.15247 mM, L-Proline 0.17371 mM, Ampicillin 0.0001431 mM, Calcium chloride anhydrous 0.1 mM, Dibasic sodium phosphate 42.2654 mM, Sodium chloride 8.55578 mM, Thiamine HCl 1000.0 mM, Potassium dihydrogen phosphate 22.0449 mM, Magnesium sulfate 1.0 mM, and Ammonium chloride 18.6947 mM | Supported by `media_text/125/` as the exact MediaDB ingredient list. |
| The formula belongs to the Kazan et al. 1995 source | Supported by the MediaDB medium 125 source link to MediaDB source 28, `Kazan et al, 1995`. |
| Escherichia coli JM109[pUC 13] has a MediaDB growth datum on this exact 8 g/L medium at growth rate 0.141 1/h, pH 7.3, and 37.0 C | Supported by MediaDB growth data 248; absent from the CultureMech record. |

Unsupported or mismatched in the record:

- `preparation_steps` are generic importer claims. The inspected MediaDB
  medium page and text export state compounds and amounts, not dissolve,
  pH-adjustment, or 0.22 um filter-sterilization instructions.
- The `applications` values `Cultivation of genome-sequenced organisms`,
  `Metabolic modeling`, and `Systems biology research` are broad database
  descriptors rather than claims attached to the narrow Kazan 8 g/L record.
- The merged record's `synonyms` are not synonyms; they are distinct MediaDB
  media with different glucose amounts.
- The merged record keeps four sibling source accessions under `synonyms`
  while leaving the canonical accession as `MEDIADB:125`, so a consumer cannot
  tell which beta-D-Glucose concentration belongs to which source.

## Completeness

Consequential gaps:

- `target_organisms` is absent even though MediaDB growth data 248 gives the
  strain, medium, source, pH, temperature, and growth-rate tuple for this
  exact formulation.
- The MediaDB source 28 bibliographic details are not modeled beyond the
  generic MediaDB homepage note.
- No explicit quality flag states that the `Thiamine HCl` source CHEBI list
  is `None` while the record grounds the ingredient to CHEBI:49105. The label
  is chemically plausible, but the support should come from the
  MediaIngredientMech enrichment rather than MediaDB.
- The generated merge layer has not preserved the August 2026 normalized-name
  and MIM-grounding repairs.

Empty optional recipe slots for storage, atmosphere, salinity, variants beyond
the glucose grid, and explicit publications are acceptable as empty because
neither the inspected MediaDB medium page nor `media_text/125/` supplies those
fields.

Bounded local search for `CultureMech:007013`, `m9_with_8_g_l_glucose_kazan`,
and `MEDIADB:125` included ignored and hidden files under
`data/normalized_yaml`, `data/merge_yaml`, `reports`, `src`, `tests`, `conf`,
`scripts`, `.claude`, `pyproject.toml`, `justfile`, and `README.md`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| blocker | The generated canonical merge conflates five M9 Kazan glucose-dose media with different defining glucose concentrations. The 8 g/L `MEDIADB:125` record now carries the 16 g/L glucose amount. | MediaDB `media_text/123/` through `media_text/127/` report 11.1012, 22.2025, 44.405, 88.8099, and 177.62 mM beta-D-Glucose; the merged record stores all five file stems in `merged_from` under the `MEDIADB:125` identity and uses `88.8099` mM. | Merge rules in `src/culturemech/merge/merge_recipes.py`; regenerate `data/merge_yaml/merged/`. |
| major | The generated merge output is stale relative to the maintained normalized record. | The normalized owner has `original_name: M9 with 8 g/l glucose (kazan)`, `media_term.term.label: M9 with 8 g/l glucose (kazan)`, and a grounded beta-D-Glucose CHEBI:15903 term; the merged record has the old truncated label and lacks the beta-D-Glucose `term`. | Merge regeneration from `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`. |
| major | Generic preparation instructions are unsupported by the inspected MediaDB record. | MediaDB medium 125 and `media_text/125/` provide only compounds, amounts, organism, source, and growth-data links; they do not say to dissolve all ingredients, adjust pH if specified, or filter sterilize through 0.22 um. | `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`, or the MediaDB importer if the same generic steps are introduced systematically. |
| major | Growth evidence from MediaDB is missing. | MediaDB growth data 248 links Escherichia coli JM109[pUC 13], `M9 with 8 g/l glucose (kazan)`, source 28, growth rate 0.141 1/h, pH 7.3, and temperature 37.0 C. The record has no `target_organisms`. | `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`. |
| minor | The applications are broad MediaDB import defaults, not narrow source claims. | The inspected MediaDB medium and growth-data pages do not call the Kazan 8 g/L recipe a general metabolic-modeling or systems-biology medium. | `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`, or the MediaDB importer if these values are generated for every MediaDB record. |

## Recommended Edits

1. Fix `src/culturemech/merge/merge_recipes.py` so concentration variants are
   not deduplicated when a defining ingredient concentration differs, then
   regenerate `data/merge_yaml/merged/`.
2. Regenerate the merged Kazan M9 records from the repaired normalized inputs
   and verify that MediaDB 123, 124, 125, 126, and 127 remain separate records
   with beta-D-Glucose at 11.1012, 22.2025, 44.405, 88.8099, and 177.62 mM.
3. In `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`,
   remove or qualify the generic preparation steps unless the Kazan primary
   article or another inspected source explicitly supports dissolution,
   pH-adjustment, and 0.22 um filter sterilization.
4. Add target-organism/growth evidence for Escherichia coli JM109[pUC 13] on
   MediaDB growth data 248, scoped to the 8 g/L glucose formulation and its
   pH 7.3, 37.0 C, 0.141 1/h observation.
5. Replace broad default `applications` with source-specific claims or leave
   the slot empty.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators above
  on `data/normalized_yaml/bacterial/m9_with_8_g_l_glucose_kazan.yaml`.
- Re-run the same validators on the regenerated
  `data/merge_yaml/merged/m9_with_8_g_l_glucose_kazan.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` to prove the merge
  layer was regenerated from current normalized inputs.
- Manually compare MediaDB `media_text/123/` through `media_text/127/` with
  the regenerated merged records and confirm the five glucose amounts remain
  distinct.
- If `target_organisms` is added, inspect the rendered YAML and confirm the
  evidence is attached to the Escherichia coli JM109[pUC 13] growth claim, not
  to the whole formulation.

## Additional Notes

- MediaDB source 28 identifies the Kazan 1995 Process Biochemistry article
  and links it by its ScienceDirect PII. The CultureMech record currently
  cites MediaDB generically, not that primary article.
- MediaDB reports no CHEBI ID for `Thiamine HCl`; the record's
  CHEBI:49105 grounding should be justified by MediaIngredientMech enrichment
  or another curated source.
- MediaDB's `media_text/125/` maps `Magnesium sulfate` to CHEBI 31795, while
  CultureMech maps the same label to CHEBI:32599. This review did not resolve
  the salt-vs-sulfate identity difference because the checked MediaDB page
  carries only a label and source database cross references, not a formula.
