# YAML Record Review: Chloroflexus Aggregans Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml
- Started UTC: 2026-09-22T07:05:38Z
- Finished UTC: 2026-09-22T07:07:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008767` |
| Name | `chloroflexus_aggregans_medium` |
| Original name | `Chloroflexus Aggregans Medium` |
| Media term | `TOGO:M2173` / `Chloroflexus Aggregans Medium` |
| Source | TOGO Medium M2173, sourced to DSMZ Medium 87a |
| Generated status | Single-source derived merge generated from `data/normalized_yaml/bacterial/TOGO_M2173_Chloroflexus_Aggregans_Medium.yaml` |

This is a generated one-record merge. Future scientific corrections belong in
`data/normalized_yaml/bacterial/TOGO_M2173_Chloroflexus_Aggregans_Medium.yaml`
or in the TOGO import and solution migration code that produced its current
flattened shape.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml --out /private/tmp/chloroflexus_aggregans_medium__59ae5520.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The CultureMech ID and TOGO term consistently identify TOGO Medium M2173,
  `Chloroflexus Aggregans Medium`.
- TOGO M2173 reports DSMZ Medium 87a as its source URL, and the DSMZ 87a page
  defines Chloroflexus Aggregans Medium as Medium 87 with sterile Vitamin
  solution CA added.
- An ignored-independent `rg --no-ignore --hidden` search for `CultureMech:008767`,
  `TOGO_M2173`, `M2173`, the `59ae5520` merge fingerprint prefix, and
  `chloroflexus_aggregans_medium` across `data/normalized_yaml` and
  `data/merge_yaml/merged` found this single M2173 owner plus its generated
  merge. The broad normalized-name term also found DSMZ/KOMODO 87a owners,
  TOGO M3032, and their separate generated records, but those do not share the
  TOGO M2173 ID or this merge fingerprint.

## Evidence

I inspected the TOGO M2173 JSON, DSMZ Medium 87a, DSMZ Medium 87, and the
MediaDive 87a/87 JSON used to cross-check DSMZ solution composition. They
support the recipe identity and support many ingredient names, but not the
current flattened concentrations:

- TOGO lists Medium 87 as a `90 ml` component and separately expands Medium 87.
  The record stores `Medium 87` as a top-level ingredient at `90 G_PER_L`,
  then also stores Medium 87's ingredients at top level.
- TOGO and DSMZ keep Neutralized sulfide solution, Vitamin solution CA,
  Fe(III) citrate solution, and Trace element solution SL-6 as separate
  subcomponents. The record has stubs for all four under `solutions`, but it
  also flattens their members as top-level ingredients.
- Five separate water volumes were summed into one direct water ingredient:
  `1050 ml` from Medium 87 plus `100 ml`, `1000 ml`, `100 ml`, and `100 ml`
  stock volumes became `2350.0 G_PER_L`. The sources never define a 2350 g/L
  final water concentration.
- Vitamin solution CA amounts were imported as if their milligram values were
  gram-per-liter concentrations. Examples: Biotin `5 mg` appears as `5 G_PER_L`
  instead of `0.05 G_PER_L` in the stock, Vitamin B12 `1 mg` appears as
  `1 G_PER_L` instead of `0.01 G_PER_L`, and Na3-EDTA `200 mg` appears as
  `200 G_PER_L` instead of `2 G_PER_L`.
- Fe(III) citrate solution is defined as `0.1 g in 100 ml H2O` and added at
  `5 ml`; the record stores Fe(III) citrate itself as `0.1 G_PER_L` and also
  stores an empty Fe(III) citrate solution stub at `5 G_PER_L`.

## Completeness

- The record has no usable solution topology. Two migrated solutions have empty
  `composition: []`, and the two shared MediaDive solutions are represented only
  by "See mediadive..." notes rather than by resolvable embedded references or
  full local composition.
- The two referenced shared solution records,
  `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml`
  and `data/normalized_yaml/bacterial/mediadive_5560_Vitamin_solution_CA.yaml`,
  are present in the ignored-independent local tree search, but both still carry
  `data_quality_flags: [incomplete_composition]` because their legacy
  `ingredients` placeholder was never removed after composition was populated.
- The preparation protocol from DSMZ 87/87a is absent: the generated record does
  not encode pH 8.2 adjustment, nitrogen handling, autoclaving, sulfide
  neutralization, sulfide injection after autoclaving, Vitamin solution CA
  filter sterilization, incubation at 50 C, or 300-500 lux illumination.
- Empty `target_organisms` and `growth_metrics` slots are not defects in this
  source-formulation record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | TOGO nested media and stock-solution rows were flattened into duplicate top-level ingredients. | `Medium 87` is both a `90 ml` source component and a `90 G_PER_L` ingredient; Neutralized sulfide solution, Vitamin solution CA, Fe(III) citrate solution, and SL-6 appear as solution stubs while their members also appear as direct ingredients. | Rebuild `data/normalized_yaml/bacterial/TOGO_M2173_Chloroflexus_Aggregans_Medium.yaml` from the TOGO component tree, or fix the TOGO importer / solution migrator before regenerating this file. |
| major | Amount units were misinterpreted for water and vitamin stock components. | Five water volumes were added to `2350.0 G_PER_L`; Vitamin solution CA milligram amounts were stored as gram-per-liter values, making Biotin, B12, Na3-EDTA, and related vitamin rows 100-fold too high even as stock concentrations. | Fix the normalized M2173 record so volumes remain volumes, milligrams in 100 ml are converted to stock `G_PER_L`, and final-medium concentrations are represented only after applying explicit solution additions. |
| major | The record omits DSMZ 87/87a preparation and incubation conditions. | The source requires pH adjustment, nitrogen sparging, autoclaving, post-autoclave neutralized sulfide injection, storage and incubation context, and Vitamin solution CA filtration. The M2173 YAML has no `preparation_steps`. | Add source-supported `preparation_steps` to `data/normalized_yaml/bacterial/TOGO_M2173_Chloroflexus_Aggregans_Medium.yaml` if TOGO M2173 remains a direct recipe rather than being deduplicated to DSMZ 87a. |
| minor | Several groundings lag known exact terms. | `Na3-EDTA` is grounded to disodium EDTA (`CHEBI:64734`) instead of trisodium EDTA (`CHEBI:63125`); `MgSO4 x 7 H2O` has primary `term` `CHEBI:31795` but a stale generic `mediaingredientmech_chebi_term` of `CHEBI:32599`; KNO3 and Fe(III) citrate still use legacy `mediaingredientmech_term`. | Refresh ingredient grounding in the normalized M2173 owner after the stock topology is corrected. |

## Recommended Edits

1. Decide whether TOGO M2173 should be a source duplicate of the curated DSMZ
   87a owner. If yes, replace this standalone exploded import with a
   `SOURCE_DUPLICATE` relationship to `data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml`.
2. If M2173 remains standalone, rebuild it as nested Medium 87 plus Neutralized
   sulfide solution, Vitamin solution CA, Fe(III) citrate solution, and Trace
   element solution SL-6. Remove duplicate direct rows for the stock members and
   keep stock water volumes scoped to each stock.
3. Correct Vitamin solution CA stock arithmetic from milligrams per 100 ml to
   gram-per-liter stock concentrations and then apply the source `1 ml/l`
   addition into the final medium only where final composition rows are wanted.
4. Add the missing DSMZ 87/87a preparation steps, including pH, anaerobic
   handling, sulfide injection after autoclaving, and light/incubation context.
5. Re-ground Na3-EDTA to `CHEBI:63125`, refresh the stale MgSO4 x 7 H2O
   `mediaingredientmech_chebi_term`, and migrate the remaining legacy MIM terms.
6. Regenerate `data/merge_yaml/merged/chloroflexus_aggregans_medium__59ae5520.yaml`
   after the normalized owner is repaired.

## Follow-up Checks

- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M2173_Chloroflexus_Aggregans_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M2173_Chloroflexus_Aggregans_Medium.yaml`
  after the Na3-EDTA, MgSO4, KNO3, and Fe(III) citrate grounding changes.
- Run `just merge-recipes` and `just verify-merges` to prove the generated
  hash-suffixed record reflects the corrected normalized owner.
- Re-open the regenerated M2173 record and compare Medium 87 nesting, four
  solution additions, water scoping, Vitamin solution CA arithmetic, and DSMZ
  87/87a preparation context against the TOGO JSON and DSMZ PDFs.

## Additional Notes

- The `N2 gas` row is supported as a sparging atmosphere in the source
  workflow, but the record should not need repeated default gas rows; older
  history already records that this duplication happened during schema
  defaulting.
