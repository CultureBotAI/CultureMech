# YAML Record Review: Artificial Seawater Medium With Pullulan

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml`
- Started UTC: 2026-09-21T15:23:22Z
- Finished UTC: 2026-09-21T15:23:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007551` |
| Name | `artificial_seawater_medium_with_pullulan` |
| Original name | Artificial Seawater Medium With Pullulan |
| Category | `bacterial` |
| Source identity | `TOGO:M1036`, JCM `JCM_M983` |
| Generated status | Generated single-source merge of `data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml` |

This review covers the TOGO-derived generated record. A separate normalized
MediaDive/JCM record,
`data/normalized_yaml/bacterial/artificial_seawater_medium_with_pullulan.yaml`,
has the same normalized name and is emitted as
`data/merge_yaml/merged/artificial_seawater_medium_with_pullulan__dbb4c222.yaml`;
it should be reviewed separately.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml --out /private/tmp/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

The documented `just` entrypoints remain unavailable for a single-record check
in this checkout because project `uv` tries to build `llvmlite==0.46.0` under
Python 3.13 and fails before the requested validator starts. The no-project
commands above ran the focused validators against the generated record.

## Identity and Grounding

The generated record denotes TOGO `M1036`, sourced from JCM `M983`. TOGO's API
reports the same title, original media ID `JCM_M983`, JCM source URL, and pH
range `7.2-7.5`; the live JCM page for `GRMD=983` serves the same "ARTIFICIAL
SEAWATER MEDIUM WITH PULLULAN" recipe.

The cross-reference notation is also internally explainable: TOGO `M180`
corresponds to JCM `M187`, TOGO `M190` corresponds to JCM `M197`, and TOGO
`M431` corresponds to JCM `M431`, which matches the live JCM links for the
FeCl2, trace-element, selenite-tungstate, and vitamin stocks.

The exact chemical groundings on simple salts are mostly adequate, but the
record leaves the post-autoclave solution rows ungrounded and empty. In
particular, the source-specific FeCl2, trace-element, and vitamin stock
references are represented only as text plus an empty `composition: []`, and
the source's 6 ml `5% Na2S x 9H2O` post-autoclave solution remains a direct
ingredient.

## Evidence

The inspected TOGO and JCM sources support the recipe identity, main-solution
ingredient names and amounts, cross-referenced stock additions, post-autoclave
additions, gas mixture, and final pH range.

The source does not support several values as currently encoded:

| Claim in record | Source evidence |
|---|---|
| `Resazurin` is `0.5 G_PER_L` | JCM M983 and TOGO M1036 state `0.5 mg` in the 1 L artificial seawater table. |
| Seven solution additions are `G_PER_L` concentrations | JCM and TOGO give 1 ml FeCl2, 1 ml trace element, 1 ml selenite-tungstate, 20 ml 5% Na2CO3, 10 ml 1% NH4Cl, 5 ml 1% KH2PO4, and 10 ml trace vitamins. |
| `5% Na2S x 9H2O` is a `6 G_PER_L` direct ingredient | JCM and TOGO put 6 ml of this solution in the anaerobic additions table. |
| `Carbon dioxide gas` and `Nitrogen gas` are variable direct ingredients | JCM and TOGO use an N2-CO2 4:1 gas mixture as an autoclave atmosphere; the gases are procedural conditions, not ingredient rows with variable concentration. |

## Completeness

The record is materially incomplete without:

- `ph_value` or equivalent preparation pH for the source range 7.2-7.5;
- the instruction to mix and autoclave the main components under N2-CO2 4:1;
- the aseptic, anaerobic post-autoclave addition boundary;
- the note that added solutions are autoclaved or filter-sterilized and stored
  under N2;
- pH adjustment with 5% Na2CO3 if necessary; and
- resolvable stock references or nested stock compositions for the M180/M431/M190
  cross-referenced solutions.

Optional target-organism and growth-evidence slots are empty. I did not flag
that as a defect because the inspected source records support a recipe, not a
strain-specific growth assertion.

Before reporting raw-source absence, I searched for `M1036`, `JCM_M983`,
`Artificial Seawater Medium With Pullulan`, and
`artificial_seawater_medium_with_pullulan` with `rg --no-ignore --hidden` across
`data`, `scripts`, `history`, `src`, `reports`, and `references_cache`. That
gitignore-independent search found normalized records, generated merge records,
indexes, and archived reports, but no maintained raw YAML source file or
source-specific transform for M1036.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Resazurin has a 1000x unit slip. | JCM M983 and TOGO M1036 state 0.5 mg; the generated record stores 0.5 `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml` |
| major | Seven post-autoclave solution addition volumes are stored as `G_PER_L`, and the sulfide solution addition is left as a direct ingredient. | The source rows are 1, 1, 1, 20, 10, 5, 6, and 10 ml additions, with the 6 ml row belonging to `5% Na2S x 9H2O`. The record stores seven solution rows as `G_PER_L` and stores `5% Na2S x 9H2O` as `6 G_PER_L` under `ingredients`. | `data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml` |
| major | Cross-referenced stock solution additions do not resolve to any actual stock composition or medium relation. | JCM points FeCl2 and trace element solution to JCM M187, selenite-tungstate solution to JCM M431, and trace vitamins to JCM M197; the generated record carries only empty `composition: []` arrays and prose `Cross-reference to Medium ...` notes. | `data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml` |
| major | The pH and anaerobic preparation procedure are absent. | JCM and TOGO specify autoclaving under N2-CO2 4:1, aseptic anaerobic stock addition, storage of those stocks under N2, and final pH adjustment to 7.2-7.5. | `data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml` |

## Recommended Edits

1. Correct `Resazurin` from `0.5 G_PER_L` to a representation of the source's `0.5 mg` in the 1 L main solution.
2. Represent all eight post-autoclave additions as volume-based solution additions: 1 ml FeCl2 solution, 1 ml trace element solution, 1 ml selenite-tungstate solution, 20 ml 5% Na2CO3, 10 ml 1% NH4Cl, 5 ml 1% KH2PO4, 6 ml 5% Na2S x 9H2O, and 10 ml trace vitamins.
3. Replace empty cross-reference stocks with resolvable references or nested stock recipes for TOGO M180, M431, and M190.
4. Move N2 and CO2 out of direct ingredient rows and into preparation/atmosphere semantics.
5. Add the pH range and JCM/TOGO preparation text covering autoclaving, anaerobic post-autoclave additions, N2 stock storage, and pH adjustment.
6. Regenerate `data/merge_yaml/merged/ARTIFICIAL_SEAWATER_MEDIUM_WITH_PULLULAN.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/TOGO_M1036_Artificial_Seawater_Medium_With_Pullulan.yaml`.
- Run `just verify-merges` after regeneration.
- Manually compare the regenerated merge with TOGO M1036 and JCM M983 to confirm all post-autoclave solution amounts are volumes, the sulfide solution is no longer direct, and the pH/preparation fields are present.

## Additional Notes

- TOGO's `M180` and `M190` identifiers correspond to JCM `M187` and `M197`;
  the apparent medium-number mismatch between the TOGO API and live JCM page is
  an identifier-system difference, not a source conflict.
