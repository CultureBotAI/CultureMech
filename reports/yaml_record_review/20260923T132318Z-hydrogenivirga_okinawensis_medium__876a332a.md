# YAML Record Review: HYDROGENIVIRGA OKINAWENSIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenivirga_okinawensis_medium__876a332a.yaml
- Started UTC: 2026-09-23T13:18:00Z
- Finished UTC: 2026-09-23T13:23:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:000567 |
| Name | hydrogenivirga_okinawensis_medium |
| Original name | HYDROGENIVIRGA OKINAWENSIS MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | LIQUID |
| pH | 7.0 |
| Source identity | MediaDive/DSMZ Medium 1131 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenivirga_okinawensis_medium__876a332a.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml |

The reviewed YAML is generated from the maintained MediaDive import at
`data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml`.
Future fixes should land in that normalized file and in the MediaDive import,
solution, and duplicate-merge logic that flattened DSMZ Medium 1131 before the
merged YAML is regenerated.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenivirga_okinawensis_medium__876a332a.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenivirga_okinawensis_medium__876a332a.yaml --out /private/tmp/hydrogenivirga_okinawensis_medium__876a332a.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenivirga_okinawensis_medium__876a332a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenivirga_okinawensis_medium__876a332a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails while attempting to build
`llvmlite==0.46.0` under Python 3.13.

## Identity and Grounding

- The reviewed record denotes MediaDive/DSMZ Medium 1131,
  `HYDROGENIVIRGA OKINAWENSIS MEDIUM`; the ID, name, source accession,
  category, liquid physical state, and pH 7.0 agree with the MediaDive medium
  metadata.
- The inspected MediaDive REST payload for medium 1131 and the linked DSMZ PDF
  both show a nested formulation: a final `Main sol. 1131` containing Modified
  MJ synthetic seawater, vitamin solution, nitrate, bicarbonate, and sulfur;
  Modified MJ synthetic seawater then contains 10 ml of a trace-element
  solution.
- A gitignore-independent slug search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found the maintained MediaDive input, a separate
  KOMODO 1131 input with the same `hydrogenivirga_okinawensis_medium` name, and
  both generated YAML outputs for the duplicated source medium.
- An ignored-inclusive exact `CultureMech:000567` search over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  the MediaDive-owned normalized and generated records plus indexes or
  archival reports that refer back to that same stable ID.
- Grounding is mostly exact for hydrates in the flattened ingredient list, but
  the `NiCl2 x 6 H2O` row is grounded to generic nickel dichloride rather than
  nickel chloride hexahydrate.

## Evidence

- The source medium identity, pH, nitrate, bicarbonate, and sulfur rows are
  supported by the inspected MediaDive REST record and DSMZ PDF.
- The Modified MJ synthetic seawater and vitamin-stock compositions are present
  in the source, but they are nested stocks. The final medium uses 1000 ml of
  Modified MJ and 10 ml of vitamin solution; Modified MJ uses 10 ml of the
  trace-element stock. The reviewed YAML emits all three levels as a single
  flat ingredient list.
- Flattening created unsupported final concentrations: final NaCl is recorded
  as 31 g/L by adding 30 g from Modified MJ to 1 g from undiluted trace stock,
  calcium chloride dihydrate is 0.6 g/L by adding 0.5 and 0.1, magnesium
  sulfate heptahydrate is 6.4 g/L by adding 3.4 and 3.0, and ferrous sulfate
  heptahydrate is 0.11 g/L by adding 0.01 and 0.1.
- The live MediaDive trace stock includes `NiCl2 x 6 H2O` at 0.025 g/L and
  `Na2SeO3 x 5 H2O` at 0.3 mg/L. The reviewed YAML keeps only one 1 mg/L row
  for each after duplicate merging, so those trace-stock values are lost.
- The vitamin rows are expressed as undiluted 1 L stock concentrations and as
  direct final-medium ingredients. For example, the source vitamin stock has
  biotin at 2 mg/L stock and the main solution adds 10 ml of stock per liter;
  the reviewed final medium records biotin as a direct 0.002 g/L row.
- The preparation steps are internally faithful to the MediaDive REST `steps`
  array, but those REST steps conflict with the linked DSMZ PDF. The PDF says
  to mix the medium except bicarbonate and vitamin solution, autoclave under
  N2, add filter-sterilized bicarbonate, distribute the medium into sulfur
  vessels under H2/CO2 4:1, steam for 3 hours on each of 3 successive days,
  add sterile-filtered trace vitamins before inoculation, and pressurize
  inoculated bottles to 200 kPa H2/CO2 4:1.

## Completeness

- The record has no `solutions` entries for Main sol. 1131, Modified MJ
  synthetic seawater, Vitamin solution, or Modified Wolin's mineral solution
  II, so it cannot state the 1000 ml, 10 ml, and nested 10 ml stock additions
  that define DSMZ 1131.
- The source/version disagreement between the live MediaDive JSON and the DSMZ
  PDF is not captured. The JSON trace stock contains nickel and selenite rows
  and uses 0.18 g/L Co/Zn and 0.02 g/L alum, while the PDF trace stock omits
  those nickel/selenite rows and lists 0.10 g Co/Zn and 0.01 g alum.
- The separate KOMODO 1131 record remains a duplicate of the same DSMZ medium
  rather than a synonym or alternate import folded into this MediaDive-owned
  record.
- Empty optional fields such as synonyms, organisms, and publication
  references are not defects for this imported provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Nested source solutions are flattened into one final-medium ingredient list. | MediaDive Medium 1131 is `Main sol. 1131` plus Modified MJ, vitamin stock, nitrate, bicarbonate, and sulfur, and Modified MJ has its own trace stock. The YAML instead lists all stock members as direct final ingredients. | `data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml`; MediaDive solution import and MediaRecipe generation should preserve local stocks. |
| Major | Duplicate cleanup summed ingredients across incompatible stock boundaries. | NaCl, calcium chloride dihydrate, magnesium sulfate heptahydrate, and ferrous sulfate heptahydrate are sums of Modified MJ rows and undiluted trace-stock rows, not final DSMZ 1131 concentrations. | `data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml`; duplicate cleanup must merge only within the same solution scope. |
| Major | Trace nickel and selenite values from the live MediaDive stock were lost by unit-conflict resolution. | The current `Modified Wolin's mineral solution II` stock includes 0.025 g/L nickel chloride hexahydrate and 0.3 mg/L disodium selenite pentahydrate, but the reviewed YAML retains only the 1 mg/L Modified MJ rows after flattening created duplicate names. | `data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml`; the unit-conflict resolver should not decide between rows from different stock scopes. |
| Major | The record hides a source-version conflict between MediaDive REST and the linked DSMZ PDF. | The imported preparation steps and trace-stock composition follow the REST payload in places where the PDF has different handling and different trace-stock rows or masses. The YAML records only one unversioned DSMZ source note. | `data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml` and the MediaDive import provenance layer. |
| Minor | Hydrated nickel chloride is grounded to a generic nickel dichloride CHEBI term. | The source label is `NiCl2 x 6 H2O`, but the ingredient term and legacy mirror point to CHEBI:34887, nickel dichloride. | `data/normalized_yaml/bacterial/hydrogenivirga_okinawensis_medium.yaml`; hydrate grounding should be refreshed for this compound label. |
| Minor | The same DSMZ 1131 medium remains as a second KOMODO-derived CultureMech record. | Ignored-inclusive local search found `data/normalized_yaml/bacterial/KOMODO_1131_HYDROGENIVIRGA_OKINAWENSIS_MEDIUM.yaml` and `data/merge_yaml/merged/HYDROGENIVIRGA_OKINAWENSIS_MEDIUM.yaml` with the same normalized name and medium identity. | KOMODO and MediaDive deduplication, not the generated reviewed YAML directly. |

## Recommended Edits

1. Replace the flat 31-row ingredient list with structured solutions for Main
   sol. 1131, Modified MJ synthetic seawater, Vitamin solution, and Modified
   Wolin's mineral solution II, preserving the MediaDive/DSMZ nesting and
   stock-addition volumes.
2. Remove cross-stock duplicate sums and keep repeated chemical labels in the
   stock where they occur: Modified MJ NaCl, calcium chloride, magnesium
   sulfate, ferrous sulfate, nickel chloride, and disodium selenite must remain
   separate from trace-stock rows.
3. Preserve the live MediaDive trace-stock nickel and selenite rows instead of
   treating them as unit conflicts with Modified MJ nickel and selenite.
4. Add retrieval/version provenance or an explicit discussion item for the
   MediaDive REST versus DSMZ PDF differences so curators can decide whether
   to follow the live API, the linked static PDF, or both as alternative
   formulations.
5. Re-ground `NiCl2 x 6 H2O` to a chemically exact hexahydrate term where one
   is available in CHEBI.
6. Reconcile the KOMODO 1131 duplicate with this MediaDive 1131 record as an
   alternate source for the same DSMZ medium, or document why two CultureMech
   records must remain separate.
7. Regenerate `data/merge_yaml/merged/` after updating the maintained
   MediaDive and KOMODO inputs.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  MediaDive merged record.
- Manually compare the regenerated record against both the live MediaDive REST
  payload for medium 1131 and `DSMZ_Medium1131.pdf`; every disagreement should
  be either represented as versioned source provenance or listed as a bounded
  unresolved conflict.
- Verify no final-medium ingredient is produced from `Vitamin solution` or
  `Modified Wolin's mineral solution II` except through the intended 10 ml/L
  stock additions.
- Re-run the duplicate merge/cleanup step and confirm it never merges
  identical chemical labels across Main sol. 1131, Modified MJ, Vitamin
  solution, and Modified Wolin's mineral solution II.
- Search regenerated normalized and merged records by `mediadive.medium:1131`,
  `komodo.medium:1131`, and `hydrogenivirga_okinawensis_medium` to verify the
  duplicate MediaDive/KOMODO inventory has been resolved or explicitly
  documented.

## Additional Notes

- The current generated record has `merged_from:
  [hydrogenivirga_okinawensis_medium]`, so the duplicate KOMODO 1131 record is
  not being folded into this MediaDive-derived output by the August 2026 merge.
- Local KOMODO submedium records for Modified MJ synthetic sea water and
  Vitamin solution are currently flagged or effectively empty, so they are not
  a drop-in source for repairing the MediaDive record.
