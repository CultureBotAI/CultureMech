# YAML Record Review: cellulosilyticum_ruminicola_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.yaml
- Started UTC: 2026-09-22T06:42:00Z
- Finished UTC: 2026-09-22T06:43:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010055 |
| Name | cellulosilyticum_ruminicola_medium |
| Original name | Cellulosilyticum Ruminicola Medium |
| Category | bacterial |
| Source | TOGO Medium M653, original source JCM_M639 |
| Generated status | Generated merged output |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.yaml |

The reviewed file is the generated merge for TOGO Medium M653/JCM Medium 639 and
was generated from a single maintained TOGO-normalized owner. Future edits
belong in that owner or in the TOGO import and solution-linking logic, followed
by merge/page regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.yaml --out /private/tmp/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with 0 errors; TSV written to `/private/tmp/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.strict.tsv`. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not checked | `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in the merged YAML. |

## Identity and Grounding

- The record identity is coherent at the medium level: the name, original name,
  `TOGO:M653` medium term, notes, and maintained TOGO owner all point to
  Cellulosilyticum Ruminicola Medium imported from JCM Medium 639.
- The direct JCM source at `GRMD=639` is authoritative for this medium and is
  live.
- The generated record incorrectly grounds generic local recipe parts named
  `Solution A`, `Solution B`, and `Solution C` to unrelated global MediaDive
  stock records:

| Reviewed solution | Linked record | Linked record content |
|---|---|---|
| Solution A, 800 | mediadive.solution:5342 | A different solution containing yeast extract, Casamino acids, sodium glutamate, citrate, MgSO4 x 7 H2O, CaSO4 x 2 H2O, KCl, and 100 g/L NaCl. |
| Solution B, 100 | mediadive.solution:5343 | A different solution containing 80 g/L Na2CO3 and 100 g/L NaCl. |
| Solution C, 100 | mediadive.solution:5312 | A different solution containing K2S4O6 and water, prepared as a 10 ml filtered stock. |

Those IDs resolve to files, but they do not denote the JCM 639 Solution A/B/C
subrecipes. The linkage appears to have matched non-unique solution labels
across sources.

## Evidence

The inspected JCM Medium 639 page lists this source formulation:

| JCM part | Source amount |
|---|---:|
| Solution A `(NH4)2SO4` | 0.9 g |
| Solution A NaCl | 0.9 g |
| Solution A `MgSO4*7H2O` | 0.9 g |
| Solution A `CaCl2*2H2O` | 0.9 g |
| Solution A cellobiose | 2.5 g |
| Solution A clarified rumen fluid, prepared from Medium 266 | 100 ml |
| Solution A distilled water | 700 ml |
| Solution B `KH2PO4` | 0.45 g |
| Solution B `K2HPO4` | 0.45 g |
| Solution B distilled water | 100 ml |
| Solution C `NaHCO3` | 3.5 g |
| Solution C distilled water | 100 ml |

JCM also says to autoclave Solutions A and B separately, filter-sterilize
Solution C, combine the three solutions, distribute the medium under an
`N2-CO2` 80:20 stream, seal with butyl rubber stoppers, and reduce before
inoculation with 0.05% `L-cysteine*HCl*H2O` that was autoclaved as a 5% stock
under `N2`.

The reviewed record preserves the JCM component list as top-level ingredients,
except that the TOGO M653 API supplied a conflicting 600 ml water plus 200 ml
rumen-fluid Solution A while direct JCM has 700 ml water plus 100 ml rumen
fluid. The generated record therefore has 800 g/L merged distilled water,
200 g/L rumen fluid, and empty Solution A/B/C shells whose amounts are recorded
as `G_PER_L`.

The maintained MediaDive sibling at
`data/normalized_yaml/bacterial/cellulosilyticum_ruminicola_medium.yaml`
confirms JCM Medium J639 identity and retains one combined preparation step,
but it divides solution-local masses by their local solution volumes. For
example, 0.9 g in 800 ml becomes 1.125 g/L, 0.45 g in 100 ml becomes 4.5 g/L,
and 3.5 g in 100 ml becomes 35 g/L. That sibling is evidence that the same JCM
medium was imported through MediaDive, not evidence that the reviewed TOGO
record is correct.

## Completeness

- The three JCM subsolutions are not represented as subrecipes. Instead,
  Solution A/B/C appear as empty `Unknown solution` references to unrelated
  generic MediaDive solution files.
- Preparation is absent from the TOGO-owned reviewed record even though the
  source distinguishes autoclaved, filter-sterilized, anaerobic, sealing, and
  reducing steps.
- The atmosphere/reducing-agent claims for `N2`, `CO2`, and
  `L-cysteine*HCl*H2O` are flattened to variable top-level ingredients, losing
  their procedural roles.
- Exact `rg --no-ignore --hidden` searches over YAML and JSON for the JCM 639
  source identity, TOGO M653 identity, Cellulosilyticum Ruminicola slug/name,
  and the three linked MediaDive solution IDs included ignored and hidden files.
  They found the TOGO owner, the separate MediaDive J639 owner, and widespread
  unrelated uses of the generic `Solution A/B/C` IDs; those reused solution IDs
  are not evidence for the JCM 639 subrecipes.
- Empty optional fields such as target organisms and explicit pH were not
  treated as defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | JCM 639 Solution A/B/C structure is lost and semantically wrong MediaDive solution links were generated. | Direct JCM 639 supplies three local subrecipes. The reviewed record points those local names to unrelated global stocks `mediadive.solution:5342`, `mediadive.solution:5343`, and `mediadive.solution:5312`, with empty `Unknown solution` placeholders. | `data/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.yaml`; solution migration/linking logic |
| Major | The water and clarified rumen-fluid volumes are wrong relative to the direct JCM source. | TOGO M653 imported 600 ml water plus 200 ml rumen fluid for Solution A, while direct JCM 639 says 700 ml water plus 100 ml clarified rumen fluid from JCM Medium 266. The merge flattened water into one 800 g/L row and retained 200 g/L rumen fluid. | TOGO importer/upstream transform feeding `data/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.yaml` |
| Major | Preparation conditions are materially incomplete. | JCM 639 gives separate autoclaving for Solutions A/B, filter sterilization for Solution C, combining order, `N2-CO2` 80:20 distribution, butyl-stopper sealing, and 0.05% `L-cysteine*HCl*H2O` reduction before inoculation. None of these steps are represented in the reviewed TOGO merge. | `data/normalized_yaml/bacterial/TOGO_M653_Cellulosilyticum_Ruminicola_Medium.yaml` |

## Recommended Edits

1. Update the TOGO M653 maintained owner or its importer so JCM 639 uses
   700 ml distilled water and 100 ml clarified rumen fluid in Solution A, not
   the current TOGO-derived 600 ml and 200 ml values.
2. Represent JCM 639 Solution A, Solution B, Solution C, and the clarified
   rumen-fluid cross-reference as source-local subrecipes or inline grouped
   ingredients without linking them to unrelated generic MediaDive
   `Solution A/B/C` records.
3. Add preparation steps for separate autoclaving, Solution C filtration,
   anaerobic `N2-CO2` 80:20 dispensing, butyl-stopper sealing, and pre-
   inoculation reduction with a 0.05% cysteine hydrochloride hydrate stock.
4. Regenerate the merged YAML and rendered products after the maintained TOGO
   owner/import path and solution-linking logic are fixed.
5. Review the separate MediaDive J639 normalized owner before allowing it to
   merge with the TOGO M653 record; its identity is correct but its quantities
   are solution-local concentrations rather than final recipe masses.

## Follow-up Checks

- Re-run open-schema and strict validation on the maintained TOGO owner, the
  regenerated `data/merge_yaml/merged/CELLULOSILYTICUM_RUMINICOLA_MEDIUM.yaml`,
  and any new source-local solution records.
- Re-run `just verify-merges` or the equivalent focused merge check to confirm
  the JCM 639 subsolutions do not link to unrelated MediaDive solution IDs.
- Inspect the regenerated merged YAML against direct JCM 639 and confirm the
  700/100/100 ml water partition, 100 ml clarified rumen fluid amount, and all
  Solution A/B/C ingredients are retained without flattening local solution
  context away.
- Re-run term and reference validation after regeneration to catch new
  ingredient or solution CURIE regressions.

## Additional Notes

- The reviewed record passes shape validation because the incorrect
  `mediadive.solution` CURIEs resolve structurally; the error is that they
  resolve to source-local stocks from a different recipe.
- The separate MediaDive solution file
  `data/normalized_yaml/bacterial/mediadive_5312_Solution_C.yaml` contains
  `K2S4O6`, but JCM 639 does not. That tetrathionate is an artifact of the
  incorrect generic `Solution C` link, not a Cellulosilyticum Ruminicola Medium
  ingredient.
