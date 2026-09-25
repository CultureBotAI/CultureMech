# YAML Record Review: Artificial seawater medium for strain JS_SRB250Lac

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml`
- Started UTC: 2026-09-21T15:20:22Z
- Finished UTC: 2026-09-21T15:21:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:008354` |
| Name | `artificial_seawater_medium_for_strain_js_srb250lac` |
| Original name | Artificial seawater medium for strain JS_SRB250Lac |
| Category | `bacterial` |
| Source identity | `TOGO:M1787`, NBRC `NBRC_M1005` |
| Generated status | Generated single-source merge of `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml` |

Reviewed the generated merge record only. The authoritative record that owns future
field edits is `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml`;
after that, regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml --out /private/tmp/Artificial_seawater_medium_for_strain_JS_SRB250Lac.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and
`just validate-terms` entrypoints were not used because project `uv` attempts to
build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before the
target-specific validator starts. The no-project invocations above isolate the
same validator families from that environment issue.

## Identity and Grounding

The record identity is internally consistent: `CultureMech:008354`,
`TOGO:M1787`, the NBRC `NBRC_M1005` source note, and the label all denote NBRC's
"Artificial seawater medium for strain JS_SRB250Lac". TOGO's structured API for
`M1787` reports the same TOGO medium URL, source URL, original media ID
`NBRC_M1005`, and pH range `7.2 - 7.4`; the NBRC URL was fetchable and contained
the same recipe title and stock-solution sections.

The record is not source-faithful at the formulation level. TOGO and NBRC encode
one final medium with salts, 1 ml of SL-10 trace element solution, 1 ml of
selenite-tungstate solution, 1 ml of vitamin solution, and 10 ml of neutralized
sulfide solution. The CultureMech record carries the four additions as `G_PER_L`
solution links and also carries all of the stock-solution ingredients as direct
final-medium ingredients.

Hydrate identity is partly wrong in the flattened trace-stock block:

| Source ingredient | Current grounding |
|---|---|
| `CoCl2.6H2O` | `CHEBI:35696` / cobalt dichloride, missing hexahydrate identity |
| `NiCl2.6H2O` | `CHEBI:34887` / nickel dichloride, missing hexahydrate identity |

The generated record also leaves `HCl (25%; 7.7 M)` ungrounded, though that
unresolved ingredient belongs inside the SL-10 stock and should be fixed while
the nested stock boundary is restored.

## Evidence

The top-level source evidence supports these claims:

- NBRC M1005 via TOGO M1787 is the cited source for the medium name, source URL,
  original media ID, final pH range, main-solution ingredient names and amounts,
  four stock-solution addition rows, and gas mixture context.
- NBRC's main-solution preparation text says to dissolve the non-stock
  ingredients except dihydrogenphosphate, ammonium chloride, bicarbonate,
  lactate, vitamins, and sulfide; autoclave in an anaerobe cultivation device;
  cool under nitrogen; then add the named sterile stocks, adjust final pH to
  7.2-7.4, and dispense under N2/CO2 80/20 gas.
- NBRC's SL-10, selenite-tungstate, vitamin, and neutralized sulfide sections
  support nested stock recipes. They do not support listing the stock water and
  stock solutes as direct final-medium ingredients.
- NBRC's sulfide-solution note supports autoclaving that 100 ml stock under N2
  at 121 C for 15 min and adjusting it to about pH 7.3 with sterile 2 N H2SO4.
  It does not support adding `H2SO4` or the stock-preparation `N2` row directly
  to the final medium.

No reference snippets are present in the generated record, so no exact-snippet
claims were available to check.

## Completeness

The record is missing source-critical preparation detail:

- final-medium pH 7.2-7.4;
- separation of autoclaved basal ingredients from post-sterilization sterile
  additions;
- nitrogen cooling, N2/CO2 80/20 dispensing atmosphere, and culture-vessel
  dispensing;
- SL-10 stock composition and autoclaving;
- selenite-tungstate stock composition;
- vitamin stock composition; and
- neutralized sulfide stock composition plus its N2, autoclave, sulfuric-acid
  pH-adjustment, and final-appearance instructions.

Optional organism/growth fields are empty. I did not treat that absence as a
defect for this import-only source recipe because the inspected NBRC and TOGO
medium records establish the recipe, not experimental growth evidence for a
target organism.

Before reporting raw-source absence, I searched for `M1787`, `NBRC_M1005`, and
`JS_SRB250Lac` with `rg --no-ignore --hidden` across `data`, `scripts`,
`history`, `src`, `reports`, and `references_cache`. That gitignore-independent
search found the normalized owner, the generated merge, indexes, and archived
reports, but no maintained raw YAML or source transform that owns this specific
record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock solution boundaries are flattened into final-medium ingredients. `Distilled water` is merged from five independent contexts into `1093.0 G_PER_L`; trace metals, selenite/tungstate salts, vitamins, sulfide-stock water, `H2SO4`, and stock-preparation `N2` are direct ingredients instead of nested stock contents. | NBRC/TOGO separate the recipe into `main solution 1`, `*Trace element solution SL-10`, `**Selenite-tungstate solution`, `***Vitamin solution`, and `****Neutralized sulfide solution`. The four main-solution stock rows are 1 ml, 1 ml, 1 ml, and 10 ml. | `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml` |
| major | The four final-medium solution additions have mass-concentration units rather than volumes, and three of them point at generic MediaDive solution IDs instead of the M1787/NBRC-owned inline stocks. | The source rows are `Trace element solution SL-10*` 1 ml, `Selenite-tungstate solution**` 1 ml, `Vitamin solution***` 1 ml, and `Sulfide solution****` 10 ml, all with `reference_media_id: M1787`; the record stores them as 1, 1, 1, and 10 `G_PER_L`. | `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml` |
| major | Source-critical pH and preparation instructions are absent. | TOGO reports `ph: 7.2 - 7.4`; NBRC gives the basal autoclave, post-cooling sterile stock additions, N2/CO2 80/20 dispensing, SL-10 autoclave, and sulfide-stock pH-adjustment instructions. None of those claims are represented in the generated record. | `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml` |
| major | Two trace-metal hydrates are grounded to anhydrous chlorides. | The source names `CoCl2.6H2O` and `NiCl2.6H2O`, while the generated record grounds them to `CHEBI:35696` cobalt dichloride and `CHEBI:34887` nickel dichloride. | `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml`, model the three 1 ml additions and one 10 ml addition as final-medium solution additions with volume units, not `G_PER_L`.
2. Move SL-10 trace elements, selenite/tungstate salts, vitamins, the neutralized sulfide contents, stock water, `HCl (25%; 7.7 M)`, stock `H2SO4`, and stock `N2` out of the final-medium ingredient list and into M1787-owned nested stock recipes.
3. Preserve the source water rows in their proper contexts instead of merging the five stock/final waters into `1093.0 G_PER_L`.
4. Add the source pH and preparation instructions for final-medium autoclaving, sterile post-cool additions, N2/CO2 80/20 dispensing, SL-10 autoclaving, and neutralized sulfide solution preparation.
5. Revisit exact CHEBI groundings for stock-local chemicals after the stock boundary is restored, starting with `CoCl2.6H2O`, `NiCl2.6H2O`, and unresolved `HCl (25%; 7.7 M)`.
6. Regenerate `data/merge_yaml/merged/Artificial_seawater_medium_for_strain_JS_SRB250Lac.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/artificial_seawater_medium_for_strain_js_srb250lac.yaml`.
- Run `just verify-merges` after regenerating merge YAML.
- Manually compare the regenerated merge against NBRC M1005 or the TOGO M1787 API to confirm the four stock sections remain nested and the final medium keeps only the four volume-based stock additions.

## Additional Notes

- The record has `high_metal: true`; that is plausible for an SL-10-containing
  anaerobic seawater recipe and was not treated as a defect.
- The source fetches used TOGO's structured
  `gmdb_medium_by_gmid?gm_id=M1787` API and NBRC's `NBRCMediumDetailServlet?NO=1005`.
- The public `https://togomedium.org/medium/M1787` page is a client-rendered
  shell and was not useful for verification.
