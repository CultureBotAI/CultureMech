# YAML Record Review: bacillus_okhensis_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_okhensis_medium__54b1c396.yaml
- Started UTC: 2026-09-21T17:54:34Z
- Finished UTC: 2026-09-21T17:55:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002825 |
| Generated record | data/merge_yaml/merged/bacillus_okhensis_medium__54b1c396.yaml |
| Maintained owner | data/normalized_yaml/bacterial/bacillus_okhensis_medium.yaml |
| Label | BACILLUS OKHENSIS MEDIUM |
| Source identity | MediaDive import of JCM J476 |
| Merge state | Single-source merge from `bacillus_okhensis_medium` |

The generated target and normalized owner are identical in their scientific
content, so future formulation fixes belong in
`data/normalized_yaml/bacterial/bacillus_okhensis_medium.yaml` or the
MediaDive/JCM import path before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_okhensis_medium__54b1c396.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/bacillus_okhensis_medium__54b1c396.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** The record's label, `media_term`, import
  history, and JCM GRMD=476 URL all identify BACILLUS OKHENSIS MEDIUM.
- **Main ingredient values match JCM 476.** D-glucose, KH2PO4, peptone, yeast
  extract, and NaCl are present at the source amounts per 1 L medium.
- **The pH-adjustment instruction is retained.** The preparation text preserves
  pH 9.0 and the sterile 20% weight/volume Na2CO3 solution used after cooling.

## Evidence

- The original JCM GRMD=476 page lists D-glucose 10 g, KH2PO4 10 g, peptone
  5 g, yeast extract 5 g, NaCl 50 g, and distilled water 1 L.
- JCM instructs mixing the components, autoclaving, cooling to room temperature,
  and adjusting pH to 9.0 with sterile 20% weight/volume Na2CO3.
- The generated record keeps all five non-water ingredient amounts, exact pH
  9.0, and the 20% Na2CO3 pH-adjustment instruction.
- The source 1 L distilled-water row is absent.

## Completeness

- The final 1 L distilled-water row is missing.
- The 20% Na2CO3 pH-adjustment solution is retained only in preparation text,
  not as a structured pH-adjustment solution.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected JCM page does not supply those claims, so I did not
  count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for the exact
  stem `bacillus_okhensis_medium__54b1c396` found no prior report before this
  file was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The 1 L distilled-water row is absent. | JCM GRMD=476 lists `Distilled water 1.0 L`; the record has no water ingredient. | `data/normalized_yaml/bacterial/bacillus_okhensis_medium.yaml`. |
| Minor | The Na2CO3 pH-adjustment solution is unstructured. | JCM specifies sterile 20% weight/volume Na2CO3 for pH adjustment; the generated record preserves it only inside preparation prose. | `data/normalized_yaml/bacterial/bacillus_okhensis_medium.yaml`; MediaDive/JCM import. |
| Minor | Source evidence is encoded only as a note. | The JCM URL appears in free text, but there is no structured reference or evidence tying ingredient rows to JCM GRMD=476. | `data/normalized_yaml/bacterial/bacillus_okhensis_medium.yaml` or the MediaDive/JCM importer. |

## Recommended Edits

1. Add the 1 L distilled-water row from JCM GRMD=476.
2. If pH-adjustment solutions are representable for this corpus, structure the
   sterile 20% weight/volume Na2CO3 solution instead of leaving it only in
   `preparation_steps`.
3. Add structured source provenance for JCM GRMD=476.
4. Regenerate merged products after the normalized owner is repaired.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained JCM
  owner after water, optional pH-solution, and provenance edits.
- Regenerate merges and verify `bacillus_okhensis_medium__54b1c396.yaml`
  retains pH 9.0 and the Na2CO3 pH-adjustment instruction while adding 1 L
  water.
- Compare the regenerated record manually against JCM GRMD=476.

## Additional Notes

- The exact prior-report search used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
