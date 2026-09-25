# YAML Record Review: atribacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T16:34:40Z
- Finished UTC: 2026-09-21T16:35:19Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml`, a generated
`MediaRecipe` with stable ID `CultureMech:007906`, normalized name
`atribacterium_medium`, original name `Atribacterium Medium`, category
`bacterial`, `medium_type: COMPLEX`, `composition_type: UNDEFINED`,
`physical_state: LIQUID`, media term `TOGO:M1368`, and merge fingerprint
`d8c8b1a7d1db25f87967a76594347059effcf3c328d211ce68ab35839f18547d`.

The merge was generated from exactly one maintained source,
`data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml`. Future
curation must change that normalized owner, or the Togo import/solution
migration rules that populate it, then regenerate `data/merge_yaml/merged/`;
the generated merge file should not be edited directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml` | Pass, `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml --out /private/tmp/ATRIBACTERIUM_MEDIUM.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated, 0 reference checks emitted. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; the validator also emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused validator for `MediaRecipe.curation_history` in one generated merge record. |

The direct `just validate-schema`, `just validate-strict`, `just
validate-references`, and `just validate-terms` entrypoints were not used for
this target because this checkout currently reaches a project `uv` build of
`llvmlite==0.46.0` under Python 3.13 before target-specific validation and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`.

## Identity and Grounding

The Togo SPARQLIST API record for `M1368` supports the generated record's Togo
identity: it reports `gm` as `http://togomedium.org/medium/M1368`, `name` as
`Atribacterium Medium`, `original_media_id` as `JCM_M1272`, `src_url` as the
JCM GRMD 1272 URL, and `ph` as `7.0`. The generated `media_term` therefore
matches the imported Togo medium accession and label.

The current public JCM GRMD URL did not independently resolve the underlying
primary JCM recipe during this review. Fetching
`https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1272` returned a small
JCM `Medium data` page that searched for medium no. 1272 and reported
`Nothing found.` Claim-level source review therefore relied on Togo's
JCM-derived API copy, not on a live JCM primary page.

A gitignore-independent exact search covered `data`, `reports`, `history`, and
`.claude` for `CultureMech:007906`, `TOGO:M1368`, `M1368`, `JCM_M1272`,
`GRMD=1272`, and `Atribacterium Medium`. It found the generated Togo merge, its
normalized Togo owner, generated indexes and archived validation rows, and a
second JCM-derived owner at
`data/normalized_yaml/bacterial/atribacterium_medium.yaml` that uses the same
JCM GRMD 1272 URL but a different source accession, `mediadive.medium:J1272`.
An exhaustive `find` confirmed both maintained Atribacterium owners under
`data/normalized_yaml/`.

## Evidence

The inspected Togo API payload supports the main salts in the generated record:
1 L distilled water plus 3 g NaCl, 0.107 g NH4Cl, 0.15 g KCl, 0.3 g Na2SO4,
and 1.38 g NaH2PO4. It also supports a 5 ml addition of Mineral solution from
Togo M1029, procedural NaOH adjustment, and use of N2 while dispensing the
medium under gas.

The same Togo payload reports these post-autoclave additions as milliliter
volumes per liter: 10 ml of 1% yeast extract solution, 2 ml of 5% Na2S*9H2O
solution, 10 ml of 5% xylitol solution, 10 ml of 5% fucose solution, 10 ml of
a local `Solution A`, and 5 ml of Trace vitamins from M190. The generated
record keeps those rows under `solutions`, but stores every volume with
`unit: G_PER_L`; the schema has `ML_PER_L` specifically for solution/component
additions.

Togo's local `Solution A` subsection contains 10 ml distilled water, 0.123 g
MgSO4 heptahydrate, and 0.015 g CaCl2 dihydrate as a nested stock recipe. The
generated record instead leaves the `Solution A` row with empty composition and
moves those three stock components into top-level `ingredients`, merging the
10 ml water with the 1 L final-medium water as a synthetic
`Distilled water` value of `11.0 G_PER_L`.

The generated record has no `preparation_steps` and no `ph_value`, even though
the Togo API exposes pH 7.0 and a preparation comment that instructs mixing,
pH adjustment to 7.0 with NaOH, dispensing 10 ml portions in 25 ml serum
bottles or Balch tubes under N2, sealing with butyl rubber stoppers,
autoclaving, and making the listed stock-solution additions after cooling.

## Completeness

The missing target organism and growth-evidence fields are not findings in
this source-only generated record: neither the inspected Togo payload nor the
unresolved live JCM URL provides strain-level growth evidence that would
support a `target_organisms` assertion.

The empty `solutions[].composition` arrays are consequential for the local
`Solution A`, because the source gives its three-row composition inside M1368
itself. Empty composition for `Mineral solution (see Medium [M1029])` and
`Trace vitamins (see Medium [M190])` is less immediately resolvable from the
M1368 payload alone because those are explicit cross-medium references.

Before writing this report, `find reports/yaml_record_review -maxdepth 1 -name
'*ATRIBACTERIUM_MEDIUM.md' -print` covered ignored and unignored files in the
review-report directory and found no prior exact uppercase
`ATRIBACTERIUM_MEDIUM` report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Seven solution-addition volumes were converted from milliliters to `G_PER_L` mass concentrations. | Togo M1368 reports 5, 10, 2, 10, 10, 10, and 5 `ml` additions; the generated `solutions` rows record those same numbers as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml` and the Togo import or solution-migration logic that maps Togo volume units. |
| Major | The local `Solution A` stock recipe was flattened into top-level ingredients, and its water was merged with final-medium water into `11.0 G_PER_L`. | Togo places distilled water 10 ml, 0.123 g MgSO4 heptahydrate, and 0.015 g CaCl2 dihydrate under a `Solution A` subsection; the target has them as top-level direct ingredients and an empty `Solution A` composition. | `data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml` and any importer rule that fails to preserve local subsection boundaries. |
| Major | Supported preparation and pH claims are absent, while NaOH and N2 survive only as variable ingredients. | Togo gives pH 7.0 and a preparation comment covering pH adjustment with NaOH, N2 dispensing, serum bottles or Balch tubes, butyl stoppers, autoclaving, and aseptic post-cooling additions. The target has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml` or the Togo comment importer. |
| Major | The same JCM GRMD 1272 medium is split between two normalized owners and two generated merge records. | The reviewed target is sourced from Togo `M1368` with original `JCM_M1272`; `data/normalized_yaml/bacterial/atribacterium_medium.yaml` points at the same `GRMD=1272` URL as `mediadive.medium:J1272` and generates `data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml`. | Cross-source duplicate reconciliation between `data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml`, `data/normalized_yaml/bacterial/atribacterium_medium.yaml`, MediaDive solution imports, and merge rules. |

No blockers or minor findings were found beyond those major curation issues.

## Recommended Edits

1. Preserve Togo `M1368` paragraph and subcomponent boundaries in
   `data/normalized_yaml/bacterial/TOGO_M1368_Atribacterium_Medium.yaml`: keep
   the final-medium 1 L water and main salts as top-level ingredients, keep
   `NaOH` and `N2` as preparation or condition text rather than weighed
   variable ingredients, and nest the 10 ml `Solution A` composition instead of
   merging it into top-level ingredients.
2. Convert the seven Togo solution-addition rows from `G_PER_L` to the
   volume-addition unit supported by the schema, preserving the values as 5,
   10, 2, 10, 10, 10, and 5 ml per liter rather than pretending they are grams
   per liter.
3. Populate `ph_value: 7.0` and preparation steps from the Togo comment,
   including anaerobic dispensing under N2, vessel and stopper details,
   autoclaving, and post-cooling aseptic additions.
4. Reconcile the Togo and MediaDive/JCM imports for GRMD 1272 before merging:
   inspect which solution records back each import, preserve any unresolved
   version conflict as a quality flag or discussion, and ensure regeneration
   either produces one authoritative canonical merge or two explicitly
   distinguished source variants.

## Follow-up Checks

- Re-run open-schema LinkML, `scripts/validate_strict.py`, the reference
  validator, and the term validator against the edited normalized Togo owner
  and the regenerated `data/merge_yaml/merged/ATRIBACTERIUM_MEDIUM.yaml`.
- Manually diff the regenerated merge against the Togo `M1368` JSON to confirm
  all paragraph groups, milliliter stock additions, local `Solution A`
  components, pH, and preparation text survived the import and merge layers.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  generated merges to prove the derived Atribacterium outputs match their
  normalized sources.
- Re-review `data/merge_yaml/merged/atribacterium_medium__1e9c1fd9.yaml` and
  `data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml` while
  reconciling the GRMD 1272 duplicate.

## Additional Notes

The live JCM GRMD endpoint was not usable for this record during review; it
returned a `Nothing found` page for medium no. 1272. Togo's SPARQLIST API did
return the JCM-derived M1368 payload and was sufficient to verify the import
identity and the major formulation-shape defects above.

An exhaustive `find` resolved `data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml`
as the MediaDive solution target used by the lower-case JCM import. That
solution is not the two-mineral local `Solution A` embedded in Togo M1368, so
it should be treated as part of the adjacent `atribacterium_medium__1e9c1fd9`
review rather than as evidence for this TOGO-owned merge.
