# YAML Record Review: Bacillus Acidocaldarius Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_acidocaldarius_medium__33ba22a7.yaml
- Started UTC: 2026-09-21T17:29:00Z
- Finished UTC: 2026-09-21T17:30:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010362 |
| Generated record | data/merge_yaml/merged/bacillus_acidocaldarius_medium__33ba22a7.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml |
| Label | Bacillus Acidocaldarius Medium |
| Source identity | TOGO M93, imported from JCM_M101 / JCM GRMD=101 |
| Merge state | Single-source merge from `TOGO_M93_Bacillus_Acidocaldarius_Medium` |

This is a generated TOGO/JCM sibling of
`data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml`. The generated
record should be regenerated from its normalized owner rather than edited
directly.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_acidocaldarius_medium__33ba22a7.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/bacillus_acidocaldarius_medium__33ba22a7.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct `just` validators currently fail during Python 3.13
dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **The source identity is correct.** The generated record points to TOGO M93,
  whose live API maps to `original_media_id: JCM_M101` and JCM GRMD=101 for
  Bacillus Acidocaldarius Medium.
- **The simple ingredient groundings are mostly exact.** MgSO4*7H2O,
  CaCl2*2H2O, KH2PO4, (NH4)2SO4, glucose, agar, and water are grounded to
  matching CHEBI terms where the record supplies a term.
- **The local sub-solutions are misgrounded.** TOGO M93 exposes Solution A and
  Solution B as subcomponents of M93 itself. The generated record instead links
  their generic names to `mediadive.solution:5342` and
  `mediadive.solution:5343`, which are unrelated global MediaDive solutions.

## Evidence

- JCM GRMD=101 and TOGO M93 split the recipe into Solution A and Solution B.
  Solution A has 500 ml water with MgSO4*7H2O 0.5 g, yeast extract 1 g,
  CaCl2*2H2O 0.25 g, KH2PO4 0.6 g, and (NH4)2SO4 0.2 g. Solution B has 500 ml
  water with glucose 1 g and agar 20 g.
- The direct final masses per combined liter in the generated record are
  source-faithful: 0.5 g/L MgSO4*7H2O, 1 g/L yeast extract, 0.25 g/L
  CaCl2*2H2O, 0.6 g/L KH2PO4, 0.2 g/L (NH4)2SO4, 1 g/L glucose, and 20 g/L agar.
- The water and solution rows are not source-faithful. TOGO M93 lists 500 ml
  Solution A and 500 ml Solution B at top level, each with its own 500 ml water
  row. The generated merge stores one `Distilled water` row as
  `1000.0 G_PER_L` and two solution entries as `500 G_PER_L`.
- The maintained normalized owner already differs from this generated artifact:
  a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` event changed the owner water
  value from the generated `1000.0` to `500.0`. That repair removed the stale
  arithmetic sum but still leaves a single top-level water row instead of two
  scoped 500 ml stock rows.
- JCM GRMD=101 and TOGO M93 preserve two preparation comments: adjust pH to
  3.0-4.0, then autoclave Solutions A and B separately and mix aseptically.
  The generated and maintained TOGO YAMLs have no pH field or preparation
  steps.

## Completeness

- Solution A and Solution B need to be represented as local sub-recipes of
  Bacillus Acidocaldarius Medium; generic external `Solution A`/`Solution B`
  solution IDs are insufficient and wrong.
- The pH range and sterilization/aseptic-mixing instruction are missing.
- The generated file is stale with respect to its maintained normalized owner
  for the water duplicate repair.
- `target_organisms`, growth metrics, light, salinity, and incubation
  temperature are empty. I did not count those as defects because the inspected
  JCM/TOGO recipe pages do not provide those claims.
- An exact gitignore-independent search for
  `bacillus_acidocaldarius_medium__33ba22a7` in `reports/yaml_record_review`
  found no prior report for this specific generated artifact before this file
  was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated artifact is stale relative to its normalized owner. | `data/merge_yaml/merged/bacillus_acidocaldarius_medium__33ba22a7.yaml` has `Distilled water 1000.0 G_PER_L`; `data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml` was repaired on 2026-09-02 and now has `500.0`. | Regenerate merges from `data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml`; do not patch the generated YAML. |
| Major | Solution A and Solution B are linked to unrelated global MediaDive solutions. | TOGO M93 and JCM 101 define local Solution A and Solution B subcomponents for this medium. The generated `mediadive.solution:5342` and `5343` records are different stock recipes reused by shared label alone. | `data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml`; if importer-owned, TOGO solution migration. |
| Major | The two 500 ml water rows are collapsed instead of scoped to their stocks. | TOGO M93 has 500 ml water inside Solution A and 500 ml water inside Solution B. The generated record sums them; the maintained owner collapses them to one unscoped 500 ml row. Neither representation lets a curator reconstruct the two separately autoclaved stocks. | `data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml`. |
| Major | Preparation and pH are missing. | The TOGO M93 API has the same pH 3.0-4.0 and separate-autoclave/aseptic-mix comments as JCM GRMD=101. The YAML has no `ph_range` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml`. |
| Minor | The TOGO source duplicate remains fragmented from the JCM/DSMZ duplicate group. | TOGO M93, JCM GRMD=101, and DSMZ Medium 13 are the same formulation after the JCM/DSMZ stock-strength error is corrected. The current generated corpus has this TOGO artifact separate from `BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml`. | Merge grouping after both normalized representations are curated. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so the stale `1000.0 G_PER_L` water sum
   disappears from `bacillus_acidocaldarius_medium__33ba22a7.yaml`.
2. Replace the `mediadive.solution:5342` and `mediadive.solution:5343` links in
   the TOGO M93 owner with local Solution A and Solution B structure: Solution A
   at 500 ml and Solution B at 500 ml.
3. Move the two 500 ml distilled-water rows into their respective local
   solutions rather than keeping an unscoped top-level water ingredient.
4. Add the source pH range 3.0-4.0 and preparation steps for separate
   autoclaving followed by aseptic mixing.
5. After the JCM/DSMZ `BACILLUS_ACIDOCALDARIUS_MEDIUM` sibling is corrected,
   rerun merge grouping so the TOGO M93 representation collapses with the same
   source-equivalent Bacillus Acidocaldarius group.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the normalized TOGO
  M93 owner after local solution and pH/preparation edits.
- Regenerate merges and verify this generated artifact no longer contains
  `1000.0 G_PER_L`, `mediadive.solution:5342`, or `mediadive.solution:5343`.
- Compare the regenerated record manually against TOGO M93 and JCM GRMD=101,
  focusing on Solution A/B boundaries, 500 ml water rows, pH, and aseptic
  combination after autoclaving.
- After the duplicate JCM/DSMZ source records are fixed, verify that a single
  Bacillus Acidocaldarius generated group remains and that BRYOCELLA ELONGATA
  is not part of it.

## Additional Notes

- The direct chemical final concentrations in this TOGO sibling are better than
  the JCM/DSMZ sibling reviewed immediately before it; the remaining scientific
  failures are loss of stock boundaries, wrong stock IDs, missing preparation,
  and stale generation.
- The exact prior-report search was run with `--no-ignore --hidden`, so ignored
  reports were included.
