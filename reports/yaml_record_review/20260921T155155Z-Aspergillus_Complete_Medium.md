# YAML Record Review: Aspergillus Complete Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml
- Started UTC: 2026-09-21T15:48:32Z
- Finished UTC: 2026-09-21T15:51:55Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007742` |
| Label | `Aspergillus Complete Medium` |
| Normalized owner | `data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml` |
| Source | TOGO Medium `TOGO:M1214`, derived from JCM `M1134` |
| Generated status | Generated one-input merge of `TOGO_M1214_Aspergillus_Complete_Medium`; future fixes belong in the normalized owner, the MediaDive/JCM duplicate owner, or importer/deduplication rules and should be propagated by regenerating merges/pages. |

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml` reported `No issues found`. |
| Strict validation | Passed: the no-project Python 3.11 invocation of `scripts/validate_strict.py data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml --out /private/tmp/Aspergillus_Complete_Medium.strict.tsv --workers 1 --quiet` scanned 1 file and wrote 0 error rows. |
| Reference validation | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file, ran 0 snippet checks, and reported all validations passed. |
| Term validation | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported validation passed after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone records under `history/`, not a focused embedded-`MediaRecipe.curation_history` validator for one generated merge record. |

The documented `just` entry points remain blocked by the project-level Python
3.13 `llvmlite==0.46.0` build failure, so the focused no-project Python 3.11
validator invocations above were used for this one record.

## Identity and Grounding

The TOGO source identity is coherent. The TOGO `M1214` API record is named
`Aspergillus Complete Medium`, points to original media ID `JCM_M1134`, and
links to JCM's `GRMD=1134` page. The generated record preserves those source
accessions in `media_term` and `notes`.

The local CultureMech identity is not fully resolved. A gitignore-independent
exact search found another normalized JCM 1134 import,
`data/normalized_yaml/bacterial/aspergillus_complete_medium.yaml`, with
`CultureMech:002307`, `mediadive.medium:J1134`, the same JCM URL, and the same
four non-water ingredients. MediaDive's JSON export for `J1134` also names
JCM as the source and links to the same JCM 1134 page, so the generated target
is a TOGO copy of an already imported MediaDive/JCM formulation rather than an
independent formulation.

The category needs curation. The reviewed owner and its MediaDive duplicate are
filed as `category: bacterial`, while the JCM and MediaDive names are
Aspergillus-specific and the MediaDive page exposes an Aspergillus nidulans JCM
19075 strain selector.

## Evidence

The generated record has no structured `references` or snippet-level
`evidence`, but the inspected TOGO, JCM, and MediaDive source records support
the basic JCM 1134 formulation.

Supported claims:

- TOGO `M1214` is `Aspergillus Complete Medium` imported from JCM `M1134`.
- JCM `M1134` is `ASPERGILLUS COMPLETE MEDIUM` and lists malt extract
  `(BD-Difco)` 20 g, peptone `(BD-Difco)` 10 g, glucose 20 g, and agar 20 g.
- MediaDive `J1134` is `ASPERGILLUS COMPLETE MEDIUM`, sourced from JCM, linked
  to `GRMD=1134`, and its JSON export lists the same four solid ingredients in
  a 1000 ml main solution with 1000 ml distilled water.
- The TOGO ingredient amounts match its API data: distilled water 1 L, malt
  extract 20 g/L, glucose 20 g/L, agar 20 g/L, and peptone 10 g/L.

Unsupported or over-scoped assertions:

| Record assertion | Problem |
|---|---|
| `Distilled water` at `1 G_PER_L` | TOGO reports 1 L and MediaDive reports 1000 ml; the generated record turns the final-volume solvent into a mass concentration. |
| `category: bacterial` | The inspected JCM and MediaDive identities are Aspergillus-specific. The filing should be checked against CultureMech's category policy for fungal media. |
| `Malt extract (BD--Difco)` and `Peptone (BD--Difco)` | JCM and MediaDive render the attribute as `BD-Difco`; the double hyphen is a TOGO/import label artifact. |
| First `curation_history` note `Source: JCM, ID: M1214` | `M1214` is the TOGO ID. The original JCM accession is `M1134`; the top-level `notes` field is more precise than this event note. |

## Completeness

- The JCM page gives no preparation, pH, sterilization, temperature,
  atmosphere, or storage instructions; leaving those optional slots empty is
  not a defect in this generated TOGO copy.
- The MediaDive page lists `Aspergillus nidulans JCM 19075` as a
  strain-specific view option, but the inspected page and JSON export do not
  supply a growth result or incubation condition that should be represented as
  a structured growth claim in this one record.
- The normalized MediaDive/JCM owner lacks the 1000 ml water row that
  MediaDive's JSON endpoint now returns, while the TOGO owner keeps TOGO's
  water row with the wrong `G_PER_L` unit. The two source imports need to be
  reconciled before the merge fingerprint can collapse the duplicate.
- `find data/normalized_yaml -name 'TOGO_M1214_Aspergillus_Complete_Medium.yaml' -o -iname '*aspergillus*complete*'`
  found the target owner and the MediaDive/JCM duplicate owner.
- `find reports/yaml_record_review -maxdepth 1 -name '*Aspergillus_Complete_Medium.md'`
  found no prior report for this generated record.
- A gitignore-independent exact search for
  `CultureMech:007742|TOGO:M1214|M1214|JCM_M1134|Aspergillus Complete Medium|mediadive.medium:J1134`
  under `data`, `scripts`, `history`, `src`, `reports`, and
  `references_cache` found the normalized owner, the generated target, the
  MediaDive/JCM duplicate, generated indexes, archived validation reports, and
  unrelated source-ID substrings such as NBRC/JCM `M1214`.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The TOGO copy of JCM 1134 did not merge with the MediaDive/JCM copy of the same formulation. | `TOGO:M1214` points to JCM `M1134`; `mediadive.medium:J1134` points to the same JCM `GRMD=1134` formulation; the generated record has only `TOGO_M1214_Aspergillus_Complete_Medium` in `merged_from`. | `data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml`, `data/normalized_yaml/bacterial/aspergillus_complete_medium.yaml`, and the merge/import normalization that handles source water rows and ingredient attributes. |
| Major | Distilled water is represented with the wrong dimension. | TOGO encodes distilled water as 1 L and MediaDive encodes it as 1000 ml; the YAML encodes `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml`, or the TOGO importer unit conversion for liter solvent rows. |
| Minor | The generated target and its MediaDive/JCM duplicate are filed under the bacterial category despite being an Aspergillus medium. | JCM, TOGO, and MediaDive all identify the formulation as Aspergillus Complete Medium. | `data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml`, `data/normalized_yaml/bacterial/aspergillus_complete_medium.yaml`, or the importer/category assignment rule. |
| Minor | TOGO-derived product attributes and import history contain accession artifacts. | TOGO changed `BD-Difco` to `BD--Difco` in two ingredient labels, and the initial curation event says `Source: JCM, ID: M1214` even though JCM's accession is `M1134`. | `data/normalized_yaml/bacterial/TOGO_M1214_Aspergillus_Complete_Medium.yaml`, or the TOGO importer that formats ingredient labels and event notes. |

## Recommended Edits

1. Reconcile `TOGO_M1214_Aspergillus_Complete_Medium.yaml` with
   `aspergillus_complete_medium.yaml`: represent the JCM 1134 final-volume
   water consistently, preserve the `BD-Difco` attributes consistently, and
   regenerate merges so only one canonical `Aspergillus Complete Medium`
   record remains for JCM 1134.
2. Correct the TOGO distilled-water conversion so the liter solvent row is not
   emitted as `1 G_PER_L`.
3. Review the category assignment for both JCM 1134 normalized records and move
   or classify the Aspergillus medium according to the repository's fungal
   media policy.
4. Normalize the TOGO attribute rendering from `BD--Difco` to `BD-Difco` and
   correct the import event to distinguish TOGO `M1214` from JCM `M1134`.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on both
  normalized owners after curation.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating `data/merge_yaml/merged/Aspergillus_Complete_Medium.yaml`.
- Re-fetch TOGO `M1214`, MediaDive `J1134`, and JCM `M1134` and compare all
  five solvent/solid source rows to the normalized records.
- Re-run a gitignore-independent exact search for
  `JCM_M1134|mediadive.medium:J1134|TOGO:M1214|Aspergillus Complete Medium`
  to confirm that no second JCM 1134 record remains outside the regenerated
  canonical merge.

## Additional Notes

- The `M1214` substring also appears in unrelated NBRC/JCM source IDs, so
  broad source-ID searches need the provider prefix to avoid mixing this TOGO
  record with `Halomarina_medium` or `surf_ana_1_medium`.
