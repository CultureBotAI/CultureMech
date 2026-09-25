# YAML Record Review: Bacillus Okhensis Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_OKHENSIS_MEDIUM.yaml
- Started UTC: 2026-09-21T17:52:56Z
- Finished UTC: 2026-09-21T17:54:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:009863 |
| Generated record | data/merge_yaml/merged/BACILLUS_OKHENSIS_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M477_Bacillus_Okhensis_Medium.yaml |
| Label | Bacillus Okhensis Medium |
| Source identity | TOGO M477, imported from JCM_M476 |
| Merge state | Single-source merge from `TOGO_M477_Bacillus_Okhensis_Medium` |

The generated target and normalized owner are identical in their scientific
content, so future formulation fixes belong in
`data/normalized_yaml/bacterial/TOGO_M477_Bacillus_Okhensis_Medium.yaml` or the
TOGO import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_OKHENSIS_MEDIUM.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_OKHENSIS_MEDIUM.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, TOGO M477
  accession, original source note, and JCM GRMD=476 URL all identify Bacillus
  Okhensis Medium.
- **Main medium values match the source.** TOGO M477 and JCM 476 list 1 L
  distilled water, yeast extract 5 g, NaCl 50 g, KH2PO4 10 g, D-glucose 10 g,
  and peptone 5 g.
- **The sodium carbonate adjustment is underspecified.** JCM/TOGO supply a
  20% weight/volume Na2CO3 solution used after cooling to adjust pH to 9.0; the
  record stores only a variable `Na2CO3` ingredient.

## Evidence

- The original JCM page is GRMD=476 / BACILLUS OKHENSIS MEDIUM and lists the
  same main rows present in TOGO M477.
- The JCM page instructs mixing the components, autoclaving, cooling to room
  temperature, and adjusting pH to 9.0 with sterile 20% weight/volume Na2CO3.
- TOGO M477 preserves `ph: "9.0"` and the same Na2CO3 preparation comment.
- The generated record has no `ph_value` or `preparation_steps`; the only trace
  of the pH-adjustment solution is the defaulted `Na2CO3` row with `value:
  variable` and `unit: VARIABLE`.

## Completeness

- pH 9.0 is missing.
- The Na2CO3 adjustment needs its 20% stock concentration and post-autoclave pH
  adjustment context.
- The mix/autoclave/cool preparation instruction is missing.
- The source-specific D-glucose row is ungrounded even though TOGO identifies it
  as a defined carbon source.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected TOGO and JCM sources do not supply those claims, so I
  did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `BACILLUS_OKHENSIS_MEDIUM` and `BACILLUS OKHENSIS MEDIUM` found no prior
  report before this file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The 20% Na2CO3 pH-adjustment solution is encoded only as a variable ingredient. | JCM 476 and TOGO M477 specify sterile 20% weight/volume Na2CO3 added after cooling to adjust pH to 9.0; the record has `Na2CO3` with a schema-defaulted `VARIABLE` concentration and no solution concentration. | `data/normalized_yaml/bacterial/TOGO_M477_Bacillus_Okhensis_Medium.yaml`; TOGO pH-solution import. |
| Major | pH and preparation instructions were dropped. | JCM 476 and TOGO M477 instruct mixing, autoclaving, cooling, and adjusting pH to 9.0; the record has no structured pH or preparation steps. | `data/normalized_yaml/bacterial/TOGO_M477_Bacillus_Okhensis_Medium.yaml`; TOGO comment/pH import. |
| Minor | D-glucose is missing a CHEBI grounding. | The source identifies D-glucose as a defined component and carbon source, but the generated row has no `term` or `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/TOGO_M477_Bacillus_Okhensis_Medium.yaml`; MIM/CHEBI grounding. |
| Minor | Source evidence is encoded only as a note. | The TOGO and JCM URLs appear in free text, but there is no structured reference or evidence tying ingredient rows and pH adjustment to TOGO M477/JCM GRMD=476. | `data/normalized_yaml/bacterial/TOGO_M477_Bacillus_Okhensis_Medium.yaml` or the TOGO importer. |

## Recommended Edits

1. Represent the Na2CO3 addition as a sterile 20% weight/volume solution used
   to adjust the cooled medium to pH 9.0.
2. Preserve pH 9.0 and the mix/autoclave/cool preparation comment from TOGO
   M477 / JCM GRMD=476.
3. Ground D-glucose to an exact D-glucose CHEBI term and add the corresponding
   MediaIngredientMech CHEBI link if available.
4. Add structured source provenance for TOGO M477 and JCM GRMD=476.
5. Regenerate the merged record after repairing the normalized owner.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained TOGO
  owner after solution, pH/preparation, term, and provenance edits.
- Regenerate merges and verify `BACILLUS_OKHENSIS_MEDIUM.yaml` carries pH 9.0
  and a 20% Na2CO3 pH-adjustment solution rather than an unexplained variable
  ingredient.
- Compare the regenerated record manually against JCM GRMD=476.

## Additional Notes

- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
