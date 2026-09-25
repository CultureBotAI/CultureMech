# YAML Record Review: METHANOMASSILIICOCCUS ALVUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__eef9f818.yaml
- Started UTC: 2026-09-24T04:18:22Z
- Finished UTC: 2026-09-24T04:19:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001125 |
| Name | methanomassiliicoccus_alvus_medium |
| Original name | METHANOMASSILIICOCCUS ALVUS MEDIUM |
| Category | archaea |
| Media term | mediadive.medium:1640 |
| Source | DSMZ Medium 1640 through MediaDive |
| Generated path reviewed | data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__eef9f818.yaml |
| Canonical owner | data/normalized_yaml/archaea/methanomassiliicoccus_alvus_medium.yaml |

The reviewed file is a generated merge of one maintained DSMZ/MediaDive owner.
It is distinct from the same-slug TOGO M1231 and MediaDive/JCM 1149 records.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__eef9f818.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__eef9f818.yaml --out /private/tmp/methanomassiliicoccus_alvus_medium__eef9f818.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__eef9f818.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__eef9f818.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The DSMZ 1640 identity is correct.** The DSMZ PDF and MediaDive REST record
  both identify medium 1640 as `METHANOMASSILIICOCCUS ALVUS MEDIUM`.
- **The medium source grounding is correct.** `mediadive.medium:1640`,
  `DSMZ Medium 1640`, and the DSMZ PDF link all point to the inspected DSMZ
  recipe.
- **The methanol grounding is exact.** The source row is a methanol stock, and
  the YAML grounds it to `CHEBI:17790` methanol.
- **The sodium resazurin row is grounded too broadly.** The source row is
  `Sodium resazurin (0.1% w/v)`, but the YAML uses `CHEBI:8806` Resazurin,
  which loses the sodium salt.
- **The commercial basal broth is intentionally ungrounded.** Anaerobe Basal
  Broth CM0957 is a complex OXOID product rather than a single small molecule.

## Evidence

### Supported by inspected sources

- The DSMZ 1640 PDF and MediaDive REST record support 35.40 g Anaerobe Basal
  Broth CM0957, 10 ml 15 percent v/v methanol, 0.50 ml 0.1 percent w/v sodium
  resazurin, and 1000 ml distilled water.
- MediaDive explains the generated g/L values: it stores a 1010 ml main
  solution, 35.0495 g/L Anaerobe Basal Broth, 7.84158 g/L methanol, and
  0.00049505 g/L sodium resazurin.
- The DSMZ and MediaDive instructions support the retained pH range 7.4-7.6,
  boiling after pH adjustment, N2 sparging, distribution under N2 in
  Hungate-type tubes or serum vials, autoclaving, methanol addition from an
  anoxic autoclaved stock, 80 percent H2 plus 20 percent CO2 overpressure after
  inoculation, and 10 percent v/v inoculum.

### Unsupported or over-scoped in the YAML

- The source distilled-water row is absent from `ingredients`.
- The 10 ml methanol stock addition is represented only as a final
  `7.84158 G_PER_L` value; the record loses the 15 percent stock concentration,
  ml addition unit, anoxic stock scope, and post-sterilization addition timing.
- The 0.50 ml sodium resazurin stock addition is represented only as a final
  `0.00049505 G_PER_L` value; the record loses the 0.1 percent stock
  concentration and ml addition unit.
- `MIX` does not capture that step 2 specifically adds a gas mixture to
  overpressure after inoculation.

## Completeness

- **The main solution is not complete.** MediaDive lists distilled water as a
  1000 ml recipe row, but the YAML carries only the two stocks and Anaerobe
  Basal Broth.
- **Two stock additions need source dimensions.** Methanol and sodium
  resazurin should preserve their original stock concentrations and addition
  volumes in addition to any normalized final concentrations.
- **The gas overpressure step is only prose.** The record has the 80 percent H2
  and 20 percent CO2 instruction in a free-text `MIX` step, with no scoped gas
  addition or pressure field.
- **Bounded local search.** A gitignore-independent search for
  `mediadive.medium:1640`, `DSMZ Medium 1640`, and `DSMZ_Medium1640` under
  `data/normalized_yaml` and `data/merge_yaml/merged` found this DSMZ owner,
  its generated record, generated indexes, and one unrelated TOGO
  Methanosarcina baltica `kg_microbe_match` crosslink.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source water row was dropped. | DSMZ 1640 and MediaDive both list 1000 ml distilled water in the main solution; the YAML has no water ingredient. | `data/normalized_yaml/archaea/methanomassiliicoccus_alvus_medium.yaml` |
| Major | Methanol and sodium resazurin stock additions were flattened to final g/L values. | DSMZ lists 10 ml 15 percent v/v methanol and 0.50 ml 0.1 percent w/v sodium resazurin; the YAML stores only derived `G_PER_L` concentrations. | `data/normalized_yaml/archaea/methanomassiliicoccus_alvus_medium.yaml` and the MediaDive importer |
| Minor | Sodium resazurin is grounded to resazurin. | The source salt is `Sodium resazurin`; the YAML term is `CHEBI:8806` Resazurin. | Shared ingredient grounding maps |

## Recommended Edits

1. Restore the 1000 ml distilled water row from DSMZ 1640 and MediaDive.
2. Preserve 10 ml of 15 percent v/v methanol as an anoxic stock solution added
   after sterilization, rather than only a calculated final g/L value.
3. Preserve 0.50 ml of 0.1 percent w/v sodium resazurin as a stock addition,
   rather than only a calculated final g/L value.
4. Re-ground Sodium resazurin to an exact sodium resazurin term if one is
   available; otherwise add a curation note documenting why the parent
   resazurin term is the nearest available grounding.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/methanomassiliicoccus_alvus_medium.yaml` and the
  regenerated merged record.
- Manually compare the regenerated YAML with DSMZ Medium 1640 and MediaDive
  medium 1640 to confirm water, source stock amounts, pH, N2 anoxic handling,
  H2/CO2 overpressure, and inoculum instructions are still present.

## Additional Notes

- `kg_microbe_match: mediadive.medium:1640` also appears in
  `data/normalized_yaml/archaea/TOGO_M300_Methanosarcina_Baltica_Medium.yaml`,
  which is a different TOGO medium. This report is scoped to the direct DSMZ
  1640 owner and does not inspect that crosslink further.
