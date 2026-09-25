# YAML Record Review: archaeoglobus_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml`
- Started UTC: 2026-09-21T13:59:44Z
- Finished UTC: 2026-09-21T14:01:53Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| ID | `CultureMech:009219` |
| Name | `archaeoglobus_medium` |
| Original name | Archaeoglobus Medium |
| Category | `archaea` |
| Source identity | `TOGO:M2664`, Archaeoglobus Medium |
| Source URL | `https://togomedium.org/medium/M2664` |
| Primary source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium399.pdf` |
| Merge fingerprint | `9001fd4144f1dfa99b393bad7eb75d227445814f47d0d31a2632c42d9df9d619` |
| Merged from | `TOGO_M2664_Archaeoglobus_Medium` |

The reviewed file is a generated merge artifact under
`data/merge_yaml/merged/`. Its authoritative owner is
`data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`; curation
must update that normalized TOGO record or the TOGO importer and then
regenerate the merge output.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml --out /private/tmp/archaeoglobus_medium__9001fd41.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: no focused single-merge-record history validator is documented; `just validate-history` targets standalone records under `history/`. |

## Identity and Grounding

The record denotes the expected TOGO M2664 import of DSMZ Medium 399,
Archaeoglobus Medium. The TOGO API payload identifies `M2664` as
Archaeoglobus Medium, lists the DSMZ Medium 399 PDF as its source URL, and
reports the same pH 6.9 final medium context. DSMZ Medium 399 is also titled
Archaeoglobus Medium, so the TOGO source identity and record label agree.

An ignored-inclusive exact search across `data/normalized_yaml`,
`data/merge_yaml`, `data/culturemech_id_registry.tsv`,
`data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`, and the import-tracking
plausibility and duplicate reports found one normalized owner for
`CultureMech:009219` / `TOGO:M2664`, this generated merge, the expected
registry/catalog/manifest entries, and the existing water and duplicate-merge
diagnostics for the normalized owner.

The main recipe identity is correct, but one nested stock identity is not:
the source adds 10 ml of the Modified Wolin mineral solution from DSMZ medium
141, while the generated record references `mediadive.solution:6187`, a
different `Trace element solution` whose local normalized recipe has Na2-EDTA,
FeCl3 x 6 H2O, MnCl2 x 4 H2O, ZnCl2 x 6 H2O, CoCl2 x 6 H2O, and
Na2MoO4 x 2 H2O rather than the Modified Wolin formula.

Most source chemical names are grounded to matching hydrate-specific ChEBI
terms. Two rows still need focused resolver review:

- `MgSO4 x 7 H2O` has the correct primary term, `CHEBI:31795` magnesium
  sulfate heptahydrate, but its `mediaingredientmech_chebi_term` still points
  to generic `CHEBI:32599` magnesium sulfate.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` nickel dichloride, broader than
  the DSMZ and TOGO hexahydrate label. Leave this unresolved until OAK/OLS or a
  curator verifies whether an exact hexahydrate term exists.

## Evidence

DSMZ Medium 399 and the TOGO M2664 API agree on the final base formulation:
1000 ml water; gram quantities for KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, NH4Cl,
CaCl2 x 2 H2O, K2HPO4, NaCl, yeast extract, sodium L-lactate, NaHCO3, and
Na2S x 9 H2O; plus 0.5 ml sodium resazurin 0.1% w/v, 2 ml
Fe(NH4)2(SO4)2 x 7 H2O 0.1% w/v, and 10 ml Modified Wolin mineral solution.

The generated merge is not faithful to that source structure:

- `Na-resazurin solution (0.1% w/v)` is an empty solution row with `0.5
  G_PER_L`; the source says 0.5 ml of a 0.1% w/v stock.
- `Fe(NH4)2(SO4)2 x 7 H2O solution (0.1% w/v)` is an empty solution row with
  `2 G_PER_L`; the source says 2 ml of a 0.1% w/v stock.
- The 10 ml Modified Wolin mineral solution was split apart and inserted into
  the final-medium `ingredients` list. This incorrectly sums stock
  ingredients with final ingredients: MgSO4 x 7 H2O is `6.45 G_PER_L`
  instead of a final-medium `3.45 g` row plus a separate stock containing
  `3.00 g`/L; NaCl is `19.0 G_PER_L` instead of `18.00 g` plus `1.00 g`/L in
  the stock; CaCl2 x 2 H2O is `0.24000000000000002 G_PER_L` instead of
  `0.14 g` plus `0.10 g`/L in the stock.
- The Modified Wolin stock milligram rows were imported as grams per liter:
  the source stock says 0.30 mg Na2SeO3 x 5 H2O and 0.40 mg Na2WO4 x 2 H2O
  per 1000 ml, but the generated final medium has `0.3 G_PER_L` and
  `0.4 G_PER_L`.
- `KOH solution` appears as a variable final solution, but in DSMZ Medium 399
  KOH is used to adjust the Modified Wolin stock pH to 6.5 and 7.0.

The preparation conditions are also underrepresented. DSMZ specifies the
anoxic H2/CO2 sparging, bicarbonate addition and pH 6.9 adjustment, dispensing
under 80% H2/20% CO2 before autoclaving, reduction with sterile anoxic sodium
sulfide under N2 before use, and a 2 bar sterile H2/CO2 overpressure after
inoculation. The generated record has generic variable CO2, N2, and H2 rows and
no preparation notes that preserve these procedural claims.

## Completeness

Consequential source details are missing or mis-scoped:

- Final-medium milliliter additions are stored as gram-per-liter solution
  concentrations.
- The Modified Wolin stock is not represented as a distinct stock with its own
  volume, water, milligram units, KOH pH adjustment, and composition boundary.
- DSMZ 399 preparation steps, pH 6.9, gas ratios, anoxic reduction, and
  overpressure are absent.
- Growth targets are empty. The inspected DSMZ source is a medium formula, not
  strain growth evidence, so this is not a defect for this import.

The local import reports already flag some of the same arithmetic issues:
`data/import_tracking/reports/merged_duplicates.tsv` reports differing-part
duplicate merges for MgSO4 x 7 H2O and NaCl on the normalized owner, and
`data/import_tracking/reports/concentration_plausibility.tsv` reports the
1000 `G_PER_L` distilled-water row as `WATER_AS_VOLUME`. The CaCl2 x 2 H2O
duplicate sum remains visible in the YAML but was not listed in the
`merged_duplicates.tsv` excerpt found by the exact search above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale for the water repair. | The merge still stores distilled water as `2000.0 G_PER_L` with `[Merged 2 duplicates: 1000.0, 1000.0]`; the normalized owner stores `1000.0 G_PER_L` and has a 2026-09-02 `repair_merged_duplicates.py` history entry that collapsed the identical duplicate. | Regenerate `data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml` from `data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`. |
| Major | Even the repaired normalized water value is dimensionally wrong. | TOGO and DSMZ say the recipe uses 1000 ml distilled water. The normalized owner encodes that preparation volume as `1000.0 G_PER_L`, and the plausibility report flags it as `WATER_AS_VOLUME`. | Fix the TOGO unit mapping for water volume, then update `data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml` through the guarded YAML writer. |
| Major | Modified Wolin mineral solution has been flattened into the final medium and arithmetically blended with base ingredients. | DSMZ and TOGO model the 10 ml stock separately; the normalized owner has the stock solutes as top-level final `ingredients` and sums MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O across final and stock formulas. | Fix the TOGO stock parser/normalizer so subcomponents become nested `SolutionRecipe` records or inline solution composition, repair `data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`, and rerun the merge. |
| Major | Source milligram quantities are represented as grams per liter. | DSMZ and TOGO give Modified Wolin Na2SeO3 x 5 H2O as 0.30 mg and Na2WO4 x 2 H2O as 0.40 mg in 1000 ml; the reviewed merge stores `0.3 G_PER_L` and `0.4 G_PER_L`. | Fix the TOGO importer to preserve milligram units inside stock subcomponents, then repair the normalized owner. |
| Major | Three solution rows have unsupported identities or dimensions. | Resazurin and ammonium iron(II) sulfate are milliliter additions of 0.1% stocks, not `G_PER_L` final components; the 10 ml Modified Wolin stock is incorrectly linked to unrelated `mediadive.solution:6187`; KOH belongs to Modified Wolin pH adjustment, not a variable final solution. | Correct solution extraction/linking in the TOGO importer and repair `data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`. |
| Major | Preparation and atmosphere semantics are dropped. | The record replaces explicit 80% H2/20% CO2 sparging, pH 6.9 adjustment, under-gas autoclaving, sulfide reduction under N2, and post-inoculation 2 bar H2/CO2 overpressure with unscoped variable gas rows. | Extend the normalized TOGO record with preparation notes or structured condition slots supported by DSMZ 399. |
| Minor | Two ingredient groundings need resolver review. | `MgSO4 x 7 H2O` has a heptahydrate primary ChEBI term but a generic `mediaingredientmech_chebi_term`; `NiCl2 x 6 H2O` is represented by generic nickel dichloride. | Run the packaged MIM/OAK resolver against these exact labels and update only the mismatched or unsupported terms. |

## Recommended Edits

1. Update the TOGO importer so final milliliter additions remain stock-solution
   amounts and do not become `G_PER_L` final-medium concentrations.
2. Update the TOGO importer so named subcomponents such as Modified Wolin
   mineral solution retain their own composition boundary, water volume, and
   milligram units.
3. Repair `data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`
   through a guarded mutator: replace the wrong `mediadive.solution:6187` link,
   move the Modified Wolin rows out of top-level final `ingredients`, split the
   MgSO4, NaCl, and CaCl2 duplicate sums back into final-versus-stock
   quantities, convert Na2SeO3 and Na2WO4 stock rows back to milligrams, and
   preserve the DSMZ preparation text including pH and gas conditions.
4. Verify and correct the `mediaingredientmech_chebi_term` for MgSO4 x 7 H2O
   and the exact ChEBI grounding for NiCl2 x 6 H2O without inventing a
   replacement when no exact hexahydrate term exists.
5. Regenerate merge outputs so
   `data/merge_yaml/merged/archaeoglobus_medium__9001fd41.yaml` picks up the
   2026-09-02 water repair and the future stock-boundary repair.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`
  and `just validate-strict data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`
  after the normalized repair.
- Rerun `just validate-terms data/normalized_yaml/archaea/TOGO_M2664_Archaeoglobus_Medium.yaml`
  after grounding changes.
- Rerun `just verify-merges` and `just audit-merge-freshness` after merge
  regeneration; the reviewed generated file should no longer lag its normalized
  owner.
- Rerun the import-tracking duplicate and concentration-plausibility reports;
  `CultureMech:009219` should no longer appear for summed MgSO4/NaCl/CaCl2 or
  for water-as-`G_PER_L`.
- Manually compare the regenerated record against DSMZ Medium 399 and the TOGO
  M2664 API to ensure Modified Wolin stock ingredients remain nested and the
  Na2SeO3/Na2WO4 rows are still milligrams, not grams.

## Additional Notes

- Empty target-organism and growth-evidence slots were left unflagged because
  this TOGO/DSMZ source record is a medium formula and does not itself assert a
  tested growth organism.
- The generated merge includes the 2026-08-06 `merge_recipes.py` history event
  but not the normalized owner's 2026-09-02 duplicate-water repair event,
  confirming this artifact needs regeneration.
