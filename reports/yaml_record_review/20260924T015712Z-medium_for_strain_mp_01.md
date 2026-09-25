# YAML Record Review: Medium For Strain MP-01

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_mp_01.yaml
- Started UTC: 2026-09-24T01:55:06Z
- Finished UTC: 2026-09-24T01:57:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010405 |
| Record name | medium_for_strain_mp_01 |
| Original name | Medium For Strain MP-01 |
| Generated path | data/merge_yaml/merged/medium_for_strain_mp_01.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml |
| Upstream source | TOGO:M979, imported from JCM_M933 |
| Upstream URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=933 |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml`.
Future formula fixes belong in that normalized owner and need regeneration of
`data/merge_yaml/merged/medium_for_strain_mp_01.yaml`; the generated file
should not be edited directly.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_mp_01.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_mp_01.yaml --out /private/tmp/medium_for_strain_mp_01.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_mp_01.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_mp_01.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The TOGO source identity is internally consistent: the TOGO M979 API reports
  `gm=http://togomedium.org/medium/M979`, `name=Medium For Strain MP-01`,
  `original_media_id=JCM_M933`, and `src_url=https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=933`.
- The bacterial, complex, semi-defined, liquid classification is consistent
  with the inspected JCM and TOGO formula.
- The live JCM page for `GRMD=933` is now titled `THERMOANAEROBACULUM
  AQUATICUM MEDIUM`, but it is the same JCM source URL that TOGO M979 records
  as `JCM_M933`.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found a separate maintained record,
  `data/normalized_yaml/bacterial/thermoanaerobaculum_aquaticum_medium.yaml`,
  and a separate generated record,
  `data/merge_yaml/merged/THERMOANAEROBACULUM_AQUATICUM_MEDIUM.yaml`, for the
  same JCM `GRMD=933` URL. The current record is not a same-slug duplicate, but
  the two JCM 933 records need curation as a duplicate-or-alias conflict.

## Evidence

- The top-level salts, yeast extract, sodium nitrate, sodium pyruvate, TES, and
  distilled-water amounts in the TOGO main solution match the JCM main table:
  the source gives 1 L distilled water plus 0.5 g MgSO4 x 7 H2O, 0.1 g yeast
  extract, 0.25 g NaCl, 0.25 g CaCl2 x 2 H2O, 0.34 g each of KH2PO4, NH4Cl,
  and KCl, 0.85 g sodium nitrate, 1.1 g sodium pyruvate, and 1.0 g TES.
- The record overstates resazurin by three orders of magnitude. JCM and TOGO
  list `1 mg` resazurin per liter; the YAML stores `1 G_PER_L`.
- The five solution additions have the right names but the wrong units and no
  useful stock boundary. JCM and TOGO give 0.5 ml of 0.001% Coenzyme M, 1 ml of
  RST trace elements, 1 ml of trace vitamins from JCM 197/TOGO M190, 8 ml of
  5% Na2S x 9 H2O solution, and 8 ml of 5% L-cysteine HCl x H2O solution per
  liter. The YAML stores those quantities as `0.5`, `1`, `1`, `8`, and `8`
  `G_PER_L` with `composition: []`.
- The RST trace-element stock was flattened into final-medium ingredients.
  JCM places NTA, MnSO4 x xH2O, Fe(NH4)2(SO4)2 x 6 H2O, CoCl2 x 6 H2O,
  ZnSO4 x 7 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, Na2SeO4,
  Na2WO4 x 2 H2O, and a separate liter of distilled water inside the stock
  whose dosage is 1 ml/L. The reviewed YAML stores the stock concentrations
  themselves as if they were final-medium `G_PER_L` concentrations.
- The generated record still sums the main medium's 1 L water and the RST
  stock's 1 L water into `Distilled water` at `2.0 G_PER_L`. The maintained
  normalized owner has the later `REPAIRED_SUMMED_DUPLICATE_MERGE` event and
  has collapsed that row back to `1.0 G_PER_L`, so the merged YAML is stale
  relative to its owner for this specific duplicate-water repair.
- The source has preparation claims that are either missing or represented as
  variable ingredients: adjust the main medium to pH 7.0 with NaOH, distribute
  under an N2 gas stream, seal with butyl rubber stoppers, autoclave, then
  reduce the medium with the two 5% reducing solutions that were autoclaved
  under N2. RST trace elements also need the note to dissolve NTA, adjust that
  stock to pH 6.0 with KOH, and then add the minerals.
- The M190 trace-vitamin cross-reference resolves to TOGO M190, which is JCM
  M197. The cross-reference target is therefore plausible; the unsupported part
  in this record is its 1 ml/L amount encoded as `1 G_PER_L` with an empty
  solution body.

## Completeness

- Major stock-solution structure is absent for RST trace elements, trace
  vitamins, Coenzyme M, Na2S x 9 H2O, and L-cysteine HCl x H2O.
- The final-medium pH 7.0 and the RST-stock pH 6.0 are absent.
- Vessel, gas, autoclave, and post-autoclave reduction instructions from JCM
  are absent from structured preparation fields.
- Empty organism-growth assertions and empty literature references are not
  defects for this import-only source page; the inspected JCM recipe states the
  formulation, not a growth outcome.
- The exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` covered `TOGO:M979`, `M979`, `JCM_M933`,
  `GRMD=933`, `Medium For Strain MP-01`, and `medium_for_strain_mp_01`. It
  found the reviewed record, its maintained owner, adjacent M979 source IDs or
  cross-references in unrelated records, and the separate
  `thermoanaerobaculum_aquaticum_medium` record for the same JCM URL.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The record flattens RST trace elements into final-medium ingredients and stores the stock formulation values as final `G_PER_L` concentrations. | JCM and TOGO place the NTA, transition-metal salts, and RST distilled water inside a stock that is dosed at 1 ml/L; the reviewed YAML has those stock rows directly under `ingredients`. | `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml` |
| Major | Stock-solution additions are encoded as grams per liter instead of milliliters per liter. | The source gives 0.5 ml Coenzyme M, 1 ml RST trace elements, 1 ml trace vitamins, 8 ml 5% Na2S x 9 H2O, and 8 ml 5% L-cysteine HCl x H2O per liter; the YAML stores those five amounts as `G_PER_L` values with empty compositions. | `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml` |
| Major | Resazurin has the wrong unit. | The source formula gives 1 mg per liter; the reviewed YAML stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml` |
| Major | Preparation conditions are missing or represented as variable final ingredients. | NaOH adjusts the main medium to pH 7.0, N2 is a gas stream for distribution and autoclaving, and KOH adjusts only the RST trace-element stock to pH 6.0. The YAML stores NaOH, N2, and KOH as variable ingredients and has no matching preparation text. | `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml` |
| Major | JCM `GRMD=933` is represented by two maintained records. | An ignored-file search over normalized and merged YAML found both `medium_for_strain_mp_01` and `thermoanaerobaculum_aquaticum_medium` pointing at `GRMD=933`. | `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml`; `data/normalized_yaml/bacterial/thermoanaerobaculum_aquaticum_medium.yaml` |
| Minor | Generated output is stale relative to the maintained duplicate-water repair. | The normalized owner collapsed the duplicate distilled-water sum to 1.0 on 2026-09-02, but this generated record still has `Distilled water` at `2.0 G_PER_L`. | Regenerate `data/merge_yaml/merged/medium_for_strain_mp_01.yaml` from normalized YAML after curation. |
| Minor | Empty migrated stock names obscure the preferred stock identities. | All five entries in `solutions` still have `name: Unknown solution` even though their `preferred_term` values identify the imported stock additions. | `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/medium_for_strain_mp_01.yaml`, rebuild the
   five source stock additions as solution additions with milliliter-per-liter
   amounts: 0.5 ml/L 0.001% Coenzyme M, 1 ml/L RST trace elements, 1 ml/L trace
   vitamins from TOGO M190/JCM M197, 8 ml/L 5% Na2S x 9 H2O, and 8 ml/L 5%
   L-cysteine HCl x H2O.
2. Move NTA, MnSO4 x xH2O, Fe(NH4)2(SO4)2 x 6 H2O, CoCl2 x 6 H2O,
   ZnSO4 x 7 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, Na2SeO4,
   Na2WO4 x 2 H2O, distilled water, and the KOH pH adjustment under an RST
   trace-elements stock recipe instead of treating them as final-medium
   ingredients.
3. Change resazurin from `1 G_PER_L` to a 1 mg/L representation.
4. Move NaOH, N2, and KOH out of final variable ingredients unless a dedicated
   preparation reagent model is added; preserve final pH 7.0, N2 distribution,
   butyl-stopper sealing, autoclaving, post-autoclave reduction, RST pH 6.0,
   and reducing-solution sterilization as preparation text or structured
   condition fields.
5. Reconcile the two `GRMD=933` records by deciding whether
   `Medium For Strain MP-01` is a stale TOGO alias of `THERMOANAEROBACULUM
   AQUATICUM MEDIUM` or whether one record should be retained as a variant
   with an explicit alias relationship.
6. Regenerate merged YAML and downstream pages after the normalized owner is
   repaired so the generated `Distilled water` value no longer carries the
   stale `2.0 G_PER_L` sum.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_strain_mp_01.yaml`.
- Re-inspect TOGO M979 and JCM `GRMD=933` after regeneration and confirm that
  only final-medium rows remain under top-level `ingredients`.
- Confirm that the regenerated RST trace-elements stock retains its own 1 L
  distilled-water basis and pH 6.0 KOH preparation note.
- Confirm that the trace-vitamin addition remains a 1 ml/L cross-reference to
  TOGO M190/JCM M197 and is not expanded from an unrelated vitamin formula.
- Repeat an exact gitignore-independent search for `GRMD=933`, `JCM_M933`,
  `TOGO:M979`, and `mediadive.medium:J933` across normalized and merged YAML
  after duplicate-source reconciliation.

## Additional Notes

- Source fetches used the TOGO M979 API, the TOGO M190 API for the vitamin
  cross-reference, and the live JCM `GRMD=933` page.
- The JCM source uses the live title `THERMOANAEROBACULUM AQUATICUM MEDIUM`;
  TOGO M979 preserves the older or alternate name `Medium For Strain MP-01`.
- No record YAML was edited during this review.
