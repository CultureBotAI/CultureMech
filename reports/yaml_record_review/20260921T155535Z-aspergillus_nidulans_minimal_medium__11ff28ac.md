# YAML Record Review: ASPERGILLUS NIDULANS MINIMAL MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/aspergillus_nidulans_minimal_medium__11ff28ac.yaml
- Started UTC: 2026-09-21T15:54:25Z
- Finished UTC: 2026-09-21T15:55:35Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/aspergillus_nidulans_minimal_medium__11ff28ac.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:001303` |
| Label | `ASPERGILLUS NIDULANS MINIMAL MEDIUM` |
| Normalized owner | `data/normalized_yaml/bacterial/aspergillus_nidulans_minimal_medium.yaml` |
| Source | MediaDive/DSMZ `mediadive.medium:204` |
| Generated status | Generated one-input merge of `aspergillus_nidulans_minimal_medium`; future fixes belong in the normalized owner, the KOMODO/DSMZ duplicate owner, or importer/deduplication rules and should be propagated by regenerating merges/pages. |

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/aspergillus_nidulans_minimal_medium__11ff28ac.yaml` exited 0 and emitted no issues. |
| Strict validation | Passed: the no-project Python 3.11 invocation of `scripts/validate_strict.py data/merge_yaml/merged/aspergillus_nidulans_minimal_medium__11ff28ac.yaml --out /private/tmp/aspergillus_nidulans_minimal_medium__11ff28ac.strict.tsv --workers 1 --quiet` scanned 1 file and wrote 0 error rows. |
| Reference validation | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/aspergillus_nidulans_minimal_medium__11ff28ac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file, ran 0 snippet checks, and reported all validations passed. |
| Term validation | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/aspergillus_nidulans_minimal_medium__11ff28ac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported validation passed after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone records under `history/`, not a focused embedded-`MediaRecipe.curation_history` validator for one generated merge record. |

The documented `just` entry points remain blocked by the project-level Python
3.13 `llvmlite==0.46.0` build failure, so the focused no-project Python 3.11
validator invocations above were used for this one record.

## Identity and Grounding

The MediaDive/DSMZ identity is coherent. MediaDive medium 204 is named
`ASPERGILLUS NIDULANS MINIMAL MEDIUM`, points to the DSMZ Medium 204 PDF, and
the normalized owner uses `mediadive.medium:204` for that source accession.

The local CultureMech identity is duplicated. A gitignore-independent exact
search found a second normalized owner,
`data/normalized_yaml/bacterial/KOMODO_204_ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM.yaml`,
and a second generated merge,
`data/merge_yaml/merged/ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM.yaml`, for KOMODO
medium 204 mapped back to the same DSMZ/MediaDive medium 204. The duplicate did
not collapse because the KOMODO owner added pH-adjustment NaOH as a ninth
ingredient and omitted the DSMZ/MediaDive preparation steps.

The fungal/bacterial filing also needs review. Both duplicate normalized
owners are under `data/normalized_yaml/bacterial/`, while MediaDive and KOMODO
identify the medium as Aspergillus nidulans-specific.

## Evidence

The generated record has no structured `references` or snippet-level
`evidence`, but the inspected MediaDive HTML and JSON for medium 204 support
the DSMZ source identity, pH, solution boundaries, ingredients with amounts,
and preparation statements.

Supported claims:

- MediaDive medium 204 is `ASPERGILLUS NIDULANS MINIMAL MEDIUM`, sourced from
  DSMZ, linked to `DSMZ_Medium204.pdf`, and fixed at pH 6.5.
- DSMZ/MediaDive medium 204 is a defined solid agar medium assembled from
  three subsolutions: 500 ml solution A, 250 ml solution B, and 200 ml solution
  C.
- Solution A contains 6 g NaNO3, 1.52 g KH2PO4, and 1.52 g KCl in 500 ml, then
  is adjusted to pH 6.5 with 2 N NaOH.
- Solution B contains 0.52 g MgSO4 x 7 H2O, FeSO4 x 7 H2O without a listed
  amount, ZnSO4 x 7 H2O without a listed amount, and 15 g agar in 250 ml.
- Solution C contains 10 g glucose in 200 ml and requires an autoclave; the
  main solution says to autoclave the subsolutions separately for 15 minutes
  and mix A, B, and C before pouring plates.

Unsupported or over-scoped assertions:

| Record assertion | Problem |
|---|---|
| `12 G_PER_L` NaNO3, `3.04 G_PER_L` KH2PO4, `3.04 G_PER_L` KCl, `2.08 G_PER_L` MgSO4 x 7 H2O, `60 G_PER_L` agar, and `50 G_PER_L` glucose as final-medium ingredient concentrations | These are MediaDive's per-subsolution `g_l` normalizations, not final-medium concentrations after 500 ml A, 250 ml B, and 200 ml C are mixed. |
| One flattened eight-ingredient recipe | The DSMZ/MediaDive source is three separately prepared subsolutions; flattening erases the 500:250:200 ml mixing ratio, three water volumes, and the preparation boundary around the pH adjustment and autoclaving. |
| Top-level preparation order | The record puts the main "autoclave separately" instruction before the pH-adjustment instruction; the source scopes pH adjustment inside solution A and the separate-autoclave instruction to the main solution. |
| `category: bacterial` | DSMZ/MediaDive and KOMODO identify the record as an Aspergillus nidulans medium. |

## Completeness

- FeSO4 x 7 H2O and ZnSO4 x 7 H2O are left at `VARIABLE` concentration. That
  is preferable to an invented amount because the inspected MediaDive JSON
  lists those two solution B rows without `amount`, `unit`, or `g_l` values.
- MediaDive exposes the solution water volumes as 500 ml, 250 ml, and 200 ml
  distilled-water rows. Neither the MediaDive/DSMZ owner nor the KOMODO owner
  represents them structurally.
- No inspected source supplied an organism growth result, so the empty
  `target_organisms` and `growth_metrics` slots are not defects in this record.
- `find data/normalized_yaml -name 'aspergillus_nidulans_minimal_medium.yaml' -o -name 'KOMODO_204_ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM.yaml'`
  found the target owner and one KOMODO/DSMZ duplicate owner.
- `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nidulans_minimal_medium__11ff28ac.md'`
  found no prior report for this generated record.
- A gitignore-independent exact search for
  `CultureMech:001303|mediadive.medium:204|aspergillus_nidulans_minimal_medium__11ff28ac|ASPERGILLUS NIDULANS MINIMAL MEDIUM|komodo.medium:204`
  under `data`, `scripts`, `history`, `src`, `reports`, and
  `references_cache` found the target owner, its generated merge, the KOMODO
  duplicate owner and generated merge, generated indexes, archived validation
  output, trace-solution records whose identifiers start with `204`, and the
  immediately preceding KOMODO-side review report.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The DSMZ 204 three-solution recipe has been flattened into incorrect final-medium concentrations. | MediaDive's JSON reports 6 g NaNO3 in 500 ml solution A, 15 g agar in 250 ml solution B, and 10 g glucose in 200 ml solution C; the record stores the subsolution `g_l` values as final `G_PER_L` concentrations. | `data/normalized_yaml/bacterial/aspergillus_nidulans_minimal_medium.yaml` and the MediaDive importer that flattens nested solutions. |
| Major | The DSMZ/MediaDive copy is a duplicate of the KOMODO medium 204 import but did not merge with it. | Both imports represent DSMZ/MediaDive medium 204; the generated target and `ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM.yaml` each have a one-item `merged_from` list. | `data/normalized_yaml/bacterial/aspergillus_nidulans_minimal_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_204_ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM.yaml`, and the merge/import normalization rules. |
| Minor | The pH-adjustment preparation step is no longer scoped to solution A. | MediaDive nests the pH 6.5 / 2 N NaOH step under solution A, while the YAML emits it as top-level step 2 after the top-level autoclaving and mixing step. | `data/normalized_yaml/bacterial/aspergillus_nidulans_minimal_medium.yaml`, or the MediaDive importer that flattens solution steps. |
| Minor | The target and its KOMODO duplicate are filed under the bacterial category despite being Aspergillus nidulans media. | KOMODO and MediaDive both identify medium 204 as `ASPERGILLUS NIDULANS MINIMAL MEDIUM`. | Both normalized Aspergillus nidulans minimal-medium owners, or the importer/category assignment rule. |

## Recommended Edits

1. Re-model DSMZ/MediaDive medium 204 as three mixed subsolutions, or otherwise
   convert amounts using the 500 ml, 250 ml, and 200 ml source volumes instead
   of copying each stock's `g_l` as a final concentration.
2. Reconcile the MediaDive/DSMZ and KOMODO normalized owners so a regenerated
   merge contains both `aspergillus_nidulans_minimal_medium` and
   `KOMODO_204_ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM` in one canonical record.
3. Keep the 2 N NaOH pH adjustment scoped to solution A when nested solutions
   are represented.
4. Review and correct the category assignment for both Aspergillus nidulans
   minimal-medium owners.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on both
  normalized owners after curation.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating `aspergillus_nidulans_minimal_medium__11ff28ac.yaml` and
  `ASPERGILLUS_NIDULANS_MINIMAL_MEDIUM.yaml`.
- Re-fetch MediaDive medium 204 and compare every solution volume, ingredient
  amount, and preparation step against the curated normalized representation.
- Re-run a gitignore-independent exact search for
  `mediadive.medium:204|komodo.medium:204|ASPERGILLUS NIDULANS MINIMAL MEDIUM`
  to confirm that DSMZ 204 no longer produces two canonical generated records.

## Additional Notes

- The DSMZ 204 PDF cited by the MediaDive record was fetched, but direct PDF
  text extraction was not available in this environment; this review therefore
  used the MediaDive HTML and JSON representation of DSMZ medium 204 for the
  source ingredient, solution, pH, and preparation checks.
