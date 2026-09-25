# YAML Record Review: Hyperthermus Butylicus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hyperthermus_butylicus_medium__c3d8d5c0.yaml
- Started UTC: 2026-09-23T13:56:10Z
- Finished UTC: 2026-09-23T13:59:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:009230 |
| Name | hyperthermus_butylicus_medium |
| Original name | Hyperthermus Butylicus Medium |
| Class | MediaRecipe |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source identity | TOGO Medium M2675; original source DSMZ Medium 491 |
| Generated path reviewed | data/merge_yaml/merged/hyperthermus_butylicus_medium__c3d8d5c0.yaml |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml |

The reviewed file is generated from the maintained TOGO M2675 import above. It
is also stale: the maintained record has a September 2 water-row duplicate
repair absent from the generated YAML. Future fixes should update the TOGO
normalization path or the maintained TOGO record, reconcile the duplicate DSMZ
491 imports, and regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hyperthermus_butylicus_medium__c3d8d5c0.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hyperthermus_butylicus_medium__c3d8d5c0.yaml --out /private/tmp/hyperthermus_butylicus_medium__c3d8d5c0.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hyperthermus_butylicus_medium__c3d8d5c0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hyperthermus_butylicus_medium__c3d8d5c0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The TOGO identity is coherent: `CultureMech:009230` is the TOGO M2675 import
  of DSMZ Medium 491, and the inspected TOGO payload points to the same DSMZ
  HYPERTHERMUS BUTYLICUS MEDIUM PDF.
- A gitignore-independent exact search for `CultureMech:009230` over the
  maintained TOGO record, generated TOGO merged record, ID registry, TOGO
  indexes, and review manifest found only the current TOGO record and its
  generated index rows.
- A gitignore-independent exact search for `TOGO:M2675` over the maintained
  archaeal normalized records, generated merged records, TOGO indexes, and
  review manifest found only the current TOGO M2675 record.
- A gitignore-independent filename search over `data/normalized_yaml/archaea`
  and `data/merge_yaml/merged` also found separate KOMODO 491 and MediaDive 491
  DSMZ imports for this same Hyperthermus butylicus source medium; those need
  to be deduplicated or explicitly related later.
- Most exact salt groundings are chemically adequate. MgSO4 x 7H2O has a
  correct primary term but a stale generic `mediaingredientmech_chebi_term`,
  NiCl2 x 6H2O is grounded to generic nickel dichloride, and gas rows are
  modeled as ingredients instead of atmospheric conditions.

## Evidence

- The DSMZ 491 PDF and the TOGO M2675 payload agree on the final medium table:
  five 0.1% stock-solution volumes, 1000 ml distilled water, gram-scale marine
  salts, 15 mg H3BO3, 10 mg ammonium sulfate, 10 ml Modified Wolin's mineral
  solution, 6 g tryptone, 6 g sulfur powder, and 0.3 g Na2S x 9H2O.
- The generated TOGO YAML turns the 15 mg H3BO3 row into `15 G_PER_L`, the
  10 mg ammonium sulfate row into `10 G_PER_L`, and the Modified Wolin 0.3 mg
  Na2SeO3 x 5H2O and 0.4 mg Na2WO4 x 2H2O rows into `0.3 G_PER_L` and
  `0.4 G_PER_L`.
- DSMZ lists Na-resazurin, NiCl2 x 6H2O, SrCl2 x 6H2O, KI, and citric acid as
  0.1% w/v stocks added by volume; the TOGO YAML migrates them to empty
  `solutions:` entries whose amounts are `G_PER_L`.
- DSMZ adds 10 ml Modified Wolin's mineral solution from DSMZ Medium 141; the
  YAML retains a 10 `G_PER_L` empty Trace element solution placeholder and also
  flattens the stock's component rows into the final ingredient list.
- Flattening merged final rows with Modified Wolin stock rows: MgSO4 x 7H2O is
  `6.5 G_PER_L` from 3.5 + 3.0, NaCl is `18.0 G_PER_L` from 17.0 + 1.0, CaCl2 x
  2H2O is `0.85 G_PER_L` from 0.75 + 0.1, and H3BO3 is `15.01 G_PER_L` from
  15.0 + 0.01.
- The generated merged file still has distilled water as `2000 G_PER_L`; the
  maintained September 2 normalized record collapsed that duplicate to
  `1000 G_PER_L`, but DSMZ has separate 1000 ml rows for the final medium and
  the Modified Wolin stock.
- TOGO parsed 100% N2, 80% H2 / 20% CO2 headspace, sulfuric acid, and KOH from
  preparation prose as ingredients or empty solutions. These are procedural
  atmosphere or pH-adjuster claims, not formula ingredients.

## Completeness

- The source pH range, 6.5 to 7.0 after reduction, is absent from the TOGO
  record.
- All five 0.1% stock additions need source volumes and populated identities.
- The 10 ml Modified Wolin stock needs to stay nested with its own water and
  preparation note.
- The final and stock water volumes need dimensional repair even after the
  maintained duplicate-water collapse is regenerated.
- The DSMZ heating, anoxic N2 sparging, sulfide reduction, sulfur handling, and
  H2/CO2 pressurization text is present.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale relative to its maintained normalized owner. | The generated YAML sums two 1000 ml water rows into `2000 G_PER_L`; the maintained September 2 repair collapsed the identical duplicate to `1000 G_PER_L`. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml`. |
| Major | Milligram rows are inflated to gram-per-liter values. | DSMZ has 15 mg H3BO3 and 10 mg ammonium sulfate in the final table, plus 0.3 mg selenite and 0.4 mg tungstate in Modified Wolin's mineral solution; the YAML records 15, 10, 0.3, and 0.4 as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml`; TOGO unit conversion. |
| Major | Stock-solution volumes were migrated to empty `G_PER_L` solution placeholders. | The five 0.1% w/v rows and the 10 ml Trace element solution are source stock additions by volume, but the YAML records them as empty `solutions:` entries with values like 0.5, 2, 7, 2.5, 5, and 10 `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml`; solution migration should preserve volume units and populate stock composition where available. |
| Major | Modified Wolin's mineral solution is flattened into the final medium. | DSMZ separates the 10 ml Modified Wolin stock and its Medium 141 composition; the YAML has the stock's salts as top-level final ingredients, including duplicate merges with MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, and H3BO3. | `data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml`; nested-stock handling. |
| Major | Source water volumes are still represented as mass concentrations. | DSMZ lists 1000 ml water in both the final medium and the Modified Wolin stock; the generated YAML has `2000 G_PER_L`, and the maintained owner still has a single `1000 G_PER_L` row. | `data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml`; TOGO volume handling. |
| Major | Gas and pH-adjuster procedure details are modeled as ingredients or solutions. | N2, H2/CO2, sulfuric acid, and KOH only appear in DSMZ preparation instructions, but the YAML imports them as variable final ingredients or empty solutions. | `data/normalized_yaml/archaea/TOGO_M2675_Hyperthermus_Butylicus_Medium.yaml`; TOGO prose parser. |
| Major | The same DSMZ 491 source exists as unresolved parallel imports. | The repository has separate TOGO M2675, MediaDive 491, and KOMODO 491 normalized records and generated outputs for HYPERTHERMUS BUTYLICUS MEDIUM. | Normalized duplicate-resolution inputs for the TOGO, MediaDive, and KOMODO records. |

## Recommended Edits

1. Regenerate the TOGO M2675 merged YAML so the reviewed generated file at
   least receives the September 2 duplicate-water repair.
2. Convert all milligram source rows correctly and keep Modified Wolin's mineral
   solution nested under a 10 ml final-medium addition.
3. Preserve the 0.1% w/v stock-solution additions as volumes with populated or
   explicitly unresolved stock contents rather than empty `G_PER_L` solutions.
4. Represent final-medium and Modified Wolin water as source volumes.
5. Move N2, H2/CO2, sulfuric acid, and KOH out of formula ingredients and into
   preparation, atmosphere, or pH-adjustment fields.
6. Add the DSMZ 6.5 to 7.0 final pH range.
7. Reconcile TOGO M2675 with the existing MediaDive 491 and KOMODO 491 imports
   so future DSMZ 491 fixes do not diverge across stable IDs.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M2675 merged record.
- Manually compare every regenerated amount against TOGO M2675 and the DSMZ 491
  PDF, including final-vs-stock boundaries.
- Verify the duplicate resolver either merges or explicitly relates the TOGO,
  MediaDive, and KOMODO DSMZ 491 records.

## Additional Notes

- The imported preparation text is broadly faithful; the main breakage is in
  unit conversion, solution boundaries, and parser leakage from procedural gas
  and pH-adjustment prose.
