# YAML Record Review: Astidious Anaerobe Agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml
- Started UTC: 2026-09-21T15:55:36Z
- Finished UTC: 2026-09-21T15:57:32Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:009091` |
| Label | `Astidious Anaerobe Agar` |
| Normalized owner | `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml` |
| Source | TOGO `TOGO:M2521`, derived from DSMZ Medium 1203 |
| Generated status | Generated one-input merge of `astidious_anaerobe_agar`; future fixes belong in the normalized owner, the DSMZ/KOMODO duplicate owners, or merge regeneration rather than in this generated file. |

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml` exited 0 and emitted no issues. |
| Strict validation | Passed: the no-project Python 3.11 invocation of `scripts/validate_strict.py data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml --out /private/tmp/Astidious_Anaerobe_Agar.strict.tsv --workers 1 --quiet` scanned 1 file and wrote 0 error rows. |
| Reference validation | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file, ran 0 snippet checks, and reported all validations passed. |
| Term validation | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported validation passed after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone records under `history/`, not a focused embedded-`MediaRecipe.curation_history` validator for one generated merge record. |

The documented `just` entry points remain blocked by the project-level Python
3.13 `llvmlite==0.46.0` build failure, so the focused no-project Python 3.11
validator invocations above were used for this one record.

## Identity and Grounding

The TOGO source identity is recoverable but spelling-divergent. TOGO `M2521`
is named `Astidious Anaerobe Agar`, cites `DSMZ_Medium1203.pdf`, reports pH
7.0-7.4, and its source comment describes the DSMZ Fastidious Anaerobe Agar
protocol. MediaDive/DSMZ medium 1203 is `FASTIDIOUS ANAEROBE AGAR` and exposes
the same 45.7 g Acumedia base, 1000 ml water, horse-blood supplement, pH range,
and preparation text.

The generated record is stale relative to its normalized owner. The target was
generated on 2026-08-06 with two ingredients and no preparation data, while the
maintained TOGO owner has a 2026-09-07 curation event that adds the horse-blood
supplement, pH range, preparation steps, autoclave sterilization, references,
and improved source notes.

The local CultureMech identity is still split. The repository already has
DSMZ/MediaDive and two KOMODO normalized records for Fastidious Anaerobe Agar;
the TOGO owner lacks a `parent_media` source-duplicate link and, unlike the
DSMZ/KOMODO owners, represents the deionized-water row as `1.0 L`.

## Evidence

The generated record has no structured `references` or snippet-level
`evidence`. Its old ingredient list is under-scoped relative to the inspected
TOGO and MediaDive data, and its maintained owner now carries newer curation
that is absent from the generated merge.

Supported claims:

- TOGO `M2521` is an import of the DSMZ Medium 1203 Fastidious Anaerobe Agar
  formulation under a misspelled `Astidious Anaerobe Agar` TOGO label.
- TOGO lists 45.7 g Fastidious Anaerobe Agar (Acumedia) and 1000 ml deionized
  water, and its source comment says to soak for 10 minutes, autoclave at
  121 C for 15 minutes, cool to 47 C, add 5-10% sterile defibrinated horse
  blood, and pour plates.
- MediaDive/DSMZ medium 1203 independently lists 45.7 g Fastidious Anaerobe
  Agar, 1000 ml deionized water, 10% horse blood with an adjustment condition,
  and the same soaking, autoclaving, cooling, horse-blood addition, and pH
  context.

Unsupported or over-scoped assertions:

| Record assertion | Problem |
|---|---|
| A complete generated merge with only two ingredients | The generated file omits the sterile defibrinated horse-blood additive that TOGO carries in its protocol text and MediaDive carries as a structured recipe row. |
| No pH or preparation fields | TOGO and MediaDive both expose pH and preparation text; the normalized owner has already added those fields. |
| `add deionized water to` as `1000 G_PER_L` | TOGO reports `volume: 1000, unit: ml`; the generated file coerces that final-volume row to a mass concentration. |
| `Fastidious Anaerobe Agar (acumedia)` | DSMZ/MediaDive and the maintained owner consistently capitalize the supplier as `Acumedia`. |

## Completeness

- `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml` now covers the
  missing pH, autoclaving, cooling, horse-blood addition, references, and
  source notes; the generated record simply has not been regenerated from that
  owner.
- A regenerated TOGO merge would still need duplicate reconciliation with
  `fastidious_anaerobe_agar.yaml`,
  `KOMODO_1203_FASTIDIOUS_ANAEROBE_AGAR.yaml`, and
  `KOMODO_3136_Fastidious_Anaerobe_Agar.yaml`.
- The TOGO metadata misspelling is source-real: TOGO `M2521` says `Astidious
  Anaerobe Agar` even though its ingredient, protocol, and DSMZ URL all point
  to Fastidious Anaerobe Agar.
- `find data/normalized_yaml -iname '*Astidious*Anaerobe*Agar*' -o -iname '*Fastidious*Anaerobe*Agar*' -o -iname '*anaerobe*agar*'`
  found the TOGO owner, the DSMZ/MediaDive owner, and two KOMODO Fastidious
  Anaerobe Agar owners.
- `find reports/yaml_record_review -maxdepth 1 -name '*Astidious_Anaerobe_Agar.md'`
  found no prior report for this generated record.
- A gitignore-independent exact search for
  `CultureMech:009091|TOGO:M2521|M2521|Astidious Anaerobe Agar|Fastidious Anaerobe Agar|DSMZ_Medium1203|komodo.medium:1203|komodo.medium:3136`
  under `data`, `scripts`, `history`, `src`, `reports`, and
  `references_cache` found the target owner, the generated target, the
  DSMZ/KOMODO sibling owners, one stale `FASTIDIOUS_ANAEROBE_AGAR` generated
  merge, the September DSMZ 1203 repair script, source-duplicate proposal
  reports, indexes, and archived validation output.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated merge is stale and lacks the maintained 2026-09-07 TOGO repair. | `Astidious_Anaerobe_Agar.yaml` was generated on 2026-08-06; the normalized owner later added horse blood, pH 7.0-7.4, four preparation steps, autoclave sterilization, source notes, and references. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml`. |
| Major | The generated ingredient list omits sterile defibrinated horse blood. | TOGO carries the 5-10% horse-blood supplement in its protocol text, MediaDive carries a structured horse-blood row, and the normalized owner now has `Sterile defibrinated horse blood` at `5-10 PERCENT_V_V`. | Already repaired in `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml`; regenerate the merge. |
| Major | The TOGO import is still a separate canonical generated record even though it denotes DSMZ Medium 1203 Fastidious Anaerobe Agar. | TOGO `M2521`, MediaDive `1203`, KOMODO `1203`, and KOMODO `3136` now share the same commercial agar base and horse-blood additive, but the TOGO owner still has no `parent_media` source-duplicate link and uses a distinct water unit. | `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml` plus the merge/import normalization for TOGO volume rows. |
| Minor | The generated water and supplier strings are old importer artifacts. | The generated record has `add deionized water to` at `1000 G_PER_L` and `acumedia`; the maintained owner has already moved water to `1.0 L` with better source notes and capitalizes `Acumedia`. | Already mostly repaired in `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml`; water should still be harmonized with the DSMZ/KOMODO owners. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/Astidious_Anaerobe_Agar.yaml` from the
   current normalized TOGO owner so the generated record includes the September
   horse-blood, pH, preparation, sterilization, and reference repair.
2. Reconcile `astidious_anaerobe_agar.yaml` with the DSMZ/KOMODO Fastidious
   Anaerobe Agar source-duplicate group, including a consistent representation
   for the 1000 ml deionized-water row.
3. Preserve the TOGO `Astidious` source label as provenance, but use the DSMZ
   `Fastidious Anaerobe Agar` identity for duplicate matching so the
   source-level spelling error does not create a separate canonical medium.
4. After the TOGO duplicate is reconciled, regenerate stale
   `FASTIDIOUS_ANAEROBE_AGAR.yaml` too so its contents match the repaired
   DSMZ/KOMODO owners.

## Follow-up Checks

- Re-run focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/astidious_anaerobe_agar.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating the Astidious/Fastidious generated outputs.
- Re-fetch TOGO `M2521` and MediaDive/DSMZ `1203` and compare 45.7 g agar
  base, 1000 ml water, 5-10% horse blood, pH 7.0-7.4, 121 C autoclaving, 47 C
  cooling, and plate-pouring steps to the regenerated YAML.
- Re-run a gitignore-independent exact search for
  `TOGO:M2521|mediadive.medium:1203|komodo.medium:1203|komodo.medium:3136`
  to confirm that DSMZ 1203 no longer produces an unreconciled TOGO canonical
  record.

## Additional Notes

- The unrelated generated `FASTIDIOUS_ANAEROBE_BROTH.yaml` points to
  `DSMZ_Medium1203a.pdf`, not the DSMZ 1203 agar formulation reviewed here.
