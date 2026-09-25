# YAML Record Review: Lactic acid whey (medium 456)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml
- Started UTC: 2026-09-23T18:12:42Z
- Finished UTC: 2026-09-23T18:16:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml` |
| Generated status | Generated canonical merge from `data/normalized_yaml/bacterial/lactic_acid_whey_medium_456.yaml`; do not edit directly |
| Schema class used for validation | `MediaRecipe` |
| Conceptual kind | Standalone stock solution |
| CultureMech ID | `CultureMech:004985` |
| Name | `lactic_acid_whey_medium_456` |
| Original name | `Lactic acid whey (medium 456)` |
| Category | `bacterial` |
| Source identity in generated record | `komodo.medium:3137`; stale note also says `DSMZ Medium: 3137 (mediadive.medium:3137)` |
| Maintained owner inspected | `data/normalized_yaml/bacterial/lactic_acid_whey_medium_456.yaml` |

The generated YAML is a stale pre-repair merge. Its maintained owner now asserts
`record_kind: SOLUTION`, carries a DSMZ Medium 456 PDF reference, uses skim milk
as the single ingredient, and records preparation steps for the pH 5.5, pH 7.0,
and pH 5.5 adjustments. The generated target still lacks `record_kind`, still
has only a note-extracted `lactic` placeholder ingredient with variable
concentration, and still has the older March-to-August history ending in
`merge_recipes.py`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml` | Passed; `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml --out /private/tmp/lactic_acid_whey_medium_456.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded history | `just validate-history data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml` | Not checked: `just validate-history` validates standalone `history/` YAML records, not embedded `MediaRecipe.curation_history` lists |

The `just` validator entry points were not used because this checkout resolves
`llvmlite==0.46.0` under Python 3.13 and the build currently crashes in
`setuptools` before validators run. The focused Python 3.11 commands above
exercise the same record-level schema, strict, reference, and term validators.

## Identity and Grounding

- `CultureMech:004985`, `komodo.medium:3137`, the label, and the source name all
  identify the KOMODO import row for DSMZ Medium 456's lactic-acid-whey stock
  solution.
- The generated target is conceptually a stock solution, not a complete growth
  medium. The normalized owner explicitly records that as `record_kind: SOLUTION`;
  the generated target is stale and omits it.
- The generated target's ingredient identity is not grounded. It reports
  `preferred_term: lactic` with `concentration.value: variable` because an old
  import extracted `pH buffer: lactic acid` from notes. DSMZ Medium 456 and
  MediaDive solution 911 both define the stock itself as 10% skim milk, 100 g/L.
- The generated note conflates a KOMODO source ID with a MediaDive medium ID:
  live MediaDive `/rest/medium/3137` returned `DataNotFound`, while
  `/rest/solution/911` resolved `Lactic acid whey` to the same one-component
  skim-milk recipe and filtering protocol.

Ignored-inclusive searches were run before treating duplicates or missing
generated files as absent:

- `rg --no-ignore --hidden` over `data/normalized_yaml`, `data/merge_yaml`, and
  `reports/archive` found `CultureMech:004985` only in the reviewed generated
  target, the maintained normalized owner, normalized indexes, and old archived
  validation reports.
- The same ignored-inclusive search scope for `mediadive.solution:911` and
  `CultureMech:015267` found a second normalized owner at
  `data/normalized_yaml/bacterial/mediadive_911_Lactic_acid_whey.yaml` plus
  source indexes.
- `find data/merge_yaml/merged -maxdepth 1 -iname '*lactic*acid*whey*'` found
  only `data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml`.

## Evidence

Supported in inspected sources:

- DSMZ Medium 456 defines KPL medium with `Lactic acid whey (see below)` as a
  1000 ml stock addition and separately describes how to prepare lactic acid
  whey from 10% skim milk.
- The DSMZ PDF supports the maintained owner's preparation sequence: adjust 10%
  skim milk to pH 5.5 with lactic acid, heat at 100 C for 30 minutes, filter,
  for broth medium adjust the filtrate to pH 7.0 with 2 N NaOH, heat at 100 C
  for 30 minutes, filter, then adjust the filtrate to pH 5.5 with 2 N HCl.
- MediaDive solution 911 independently reports one recipe row, `Skim milk`,
  `amount: 10`, `unit: %`, and `g_l: 100`, plus the same preparation sentence
  and `Filter` equipment.

Unsupported or stale in the generated target:

- The direct ingredient `lactic` is not the solution composition. Lactic acid is
  a pH adjuster used during preparation of the skim-milk stock.
- `concentration.value: variable` and `unit: VARIABLE` are a placeholder, not a
  source amount for lactic acid whey.
- `DSMZ Medium: 3137 (mediadive.medium:3137)` is not a valid MediaDive medium
  accession for this stock solution; the inspected MediaDive solution endpoint
  for the actual solution is `mediadive.solution:911`.
- The generated target omits the DSMZ PDF reference and the pH/heating/filtering
  steps that now exist in the maintained owner.

## Completeness

Consequential gaps:

- The generated record is missing the maintained stock-solution assertion
  `record_kind: SOLUTION`.
- The generated record is missing the only source-supported ingredient, skim
  milk at 100 g/L.
- The generated record is missing all DSMZ preparation steps and the DSMZ source
  reference from its maintained owner.
- The normalized layer still has a separate `mediadive.solution:911` owner for
  the same lactic-acid-whey stock, so the source-specific KOMODO and MediaDive
  records remain unconsolidated upstream even though they now describe the same
  solution.

Empty or absent fields that are not defects for this generated stock solution:

- `target_organisms`, growth metrics, organism culture type, salinity, storage,
  shelf life, and genome assembly slots can stay empty unless a source-specific
  claim is added later.

## Findings

| Severity | Finding | Evidence | Maintained owner for fix |
|---|---|---|---|
| Major | The reviewed generated record is stale relative to its normalized owner. | The generated file still contains the old `lactic` placeholder ingredient, no `record_kind`, no DSMZ reference, and no preparation steps; `data/normalized_yaml/bacterial/lactic_acid_whey_medium_456.yaml` has the September 7 repair that added skim milk, `record_kind: SOLUTION`, a DSMZ PDF reference, and five preparation steps. | Regenerate `data/merge_yaml/merged/` with `just merge-recipes`; if regeneration drops data, repair `src/culturemech/merge/merge_recipes.py`, not this generated YAML by hand. |
| Major | The generated ingredient list represents a pH-adjusting reagent as if it were the stock solution's composition. | DSMZ Medium 456 and MediaDive solution 911 support 10% skim milk as the stock composition. Lactic acid appears only as the reagent used to adjust the skim milk to pH 5.5 before heating and filtration. | Already corrected in `data/normalized_yaml/bacterial/lactic_acid_whey_medium_456.yaml`; regenerate the merge output and verify this stale ingredient disappears. |
| Major | The generated source note still carries an invalid MediaDive medium accession. | MediaDive `/rest/medium/3137` returned `DataNotFound`; MediaDive `/rest/solution/911` resolved the same `Lactic acid whey` stock recipe. | Remove stale `mediadive.medium:3137` provenance from the normalized KOMODO import or merge transform, then regenerate `data/merge_yaml/merged/`. |
| Major | Lactic acid whey remains duplicated as both the KOMODO-derived `CultureMech:004985` record and the MediaDive-derived `CultureMech:015267` record. | An ignored-inclusive search found `data/normalized_yaml/bacterial/mediadive_911_Lactic_acid_whey.yaml`; its `mediadive.solution:911` source is the same skim-milk stock represented by the repaired KOMODO owner. No separate generated `*lactic*acid*whey*` record currently exists for that source. | Reconcile `data/normalized_yaml/bacterial/mediadive_911_Lactic_acid_whey.yaml` with `data/normalized_yaml/bacterial/lactic_acid_whey_medium_456.yaml` through the normalized/source merge path and refresh solution indexes. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` with
   `just merge-recipes` and inspect `data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml`
   to confirm it reflects the September 7 normalized repair.
2. In the regenerated output, verify that the target has `record_kind: SOLUTION`,
   a single skim-milk ingredient at 100 g/L, DSMZ-derived preparation steps, and
   no direct `lactic` placeholder ingredient.
3. Remove the stale `DSMZ Medium: 3137 (mediadive.medium:3137)` assertion from
   whatever maintained KOMODO import field or merge note still emits it.
4. Reconcile the separate MediaDive solution 911 normalized record with
   `CultureMech:004985`, either by merging source provenance for the same stock
   solution or by documenting why two stable CultureMech IDs must remain.

## Follow-up Checks

- Run `just merge-recipes`, then rerun the focused open, strict, reference, and
  term validators against `data/merge_yaml/merged/lactic_acid_whey_medium_456.yaml`.
- Run `just audit-merge-freshness --json --list` and confirm
  `lactic_acid_whey_medium_456.yaml` is not in the `changed`,
  `only_in_tracked`, or `only_in_fresh` lists.
- Run `just verify-merges` after regeneration to check merge integrity.
- Run an ignored-inclusive search for `mediadive.medium:3137` across
  `data/normalized_yaml` and `data/merge_yaml` and confirm it is gone from this
  record's emitted provenance.
- Re-query `https://mediadive.dsmz.de/rest/solution/911` and manually compare
  `data/normalized_yaml/bacterial/mediadive_911_Lactic_acid_whey.yaml` with
  `data/normalized_yaml/bacterial/lactic_acid_whey_medium_456.yaml` after the
  duplicate-source reconciliation.

## Additional Notes

- The review inspected `CLAUDE.md`, `justfile`, `project.justfile`, the local
  review and curation skills, the review checklist, the relevant MediaRecipe,
  SolutionRecipe, `record_kind`, and curation-history schema sections, the
  generated target, its normalized owner, the MediaDive solution 911 owner, DSMZ
  Medium 456, MediaDive `/rest/medium/3137`, and MediaDive `/rest/solution/911`.
- `record_kind: SOLUTION` on a MediaRecipe-shaped KOMODO YAML is intentional.
  `scripts/record_kinds.py` documents that KOMODO stock solutions were imported
  with MediaRecipe shape and therefore still validate structurally as
  `MediaRecipe`.
- `data/merge_yaml/merged/LACTIC_ACID_WHEY_MEDIUM.yaml` is not present; a
  `find` search over `data/merge_yaml/merged` included ignored files and found
  only `lactic_acid_whey_medium_456.yaml` for `*lactic*acid*whey*`.
