# YAML Record Review: Bacillus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Bacillus_Medium.yaml
- Started UTC: 2026-09-21T17:50:15Z
- Finished UTC: 2026-09-21T17:51:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:009007 |
| Generated record | data/merge_yaml/merged/Bacillus_Medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/bacillus_medium.yaml |
| Label | Bacillus Medium |
| Source identity | TOGO M2424, imported from ATCC Medium 0021 |
| Merge state | Single-source merge from `bacillus_medium` |

The generated target and normalized owner are identical in their scientific
content, so future formulation fixes belong in
`data/normalized_yaml/bacterial/bacillus_medium.yaml` or the TOGO import path
before regenerating merge products.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Bacillus_Medium.yaml` |
| Strict schema | Pass. `scripts/validate_strict.py data/merge_yaml/merged/Bacillus_Medium.yaml --workers 1 --quiet` |
| LinkML reference validator | Pass; 0 reference checks reported for this generated record. |
| LinkML term validator | Pass. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone `history/*.yaml`; I did not find a documented one-record validator for embedded `MediaRecipe.curation_history` events. |

The focused validators used the offline `uv --no-project` Python 3.11
workaround because direct project `just` validation currently fails during
Python 3.13 dependency resolution while building `llvmlite==0.46.0`.

## Identity and Grounding

- **Medium identity is correct.** TOGO M2424 and the original ATCC PDF identify
  the source as ATCC Medium 0021, Bacillus Medium.
- **Most ingredient identities are correct.** K2HPO4, glycerol, MgSO4, ferric
  ammonium citrate, and L-glutamic acid agree with the ATCC source at the
  displayed concentrations.
- **Citric acid is incorrectly grounded.** The source row is citric acid, but
  the record grounds it to `CHEBI:53258` / sodium citrate.
- **The water label is not source-faithful.** The ATCC PDF lists DI Water, while
  TOGO M2424 and this record list Tap water.

## Evidence

- The original ATCC PDF is headed `ATCC Medium 0021: Bacillus Medium`.
- ATCC lists K2HPO4 0.5 g, ferric ammonium citrate 0.5 g, MgSO4 0.5 g,
  glycerol 20.0 g, citric acid 2.0 g, L-glutamic acid 4.0 g, and DI Water
  1000.0 ml.
- ATCC instructs adjustment to pH 7.4 +/- 0.2 and autoclaving at 121 C.
- TOGO M2424 preserves the ingredient masses, pH range 7.2-7.6, and autoclave
  instruction, but it maps ATCC `DI Water` to `Tap water`.
- The generated record keeps the ingredient masses but has no `ph_value`,
  `preparation_steps`, or exact deionized-water label.

## Completeness

- pH 7.2-7.6 and the 121 C autoclave instruction are missing.
- The ATCC water identity needs correction from tap water to deionized water.
- Citric acid needs exact grounding rather than sodium citrate.
- `target_organisms`, growth metrics, incubation temperature, and salinity are
  empty. The inspected ATCC and TOGO payloads do not supply those claims, so I
  did not count them as defects.
- A gitignore-independent search of `reports/yaml_record_review` for
  `Bacillus_Medium` found no prior report before this file was written. A
  separate ignored-inclusive label search for `Bacillus Medium` found only a
  mention in a prior `BACILLUS_ACIDOCALDARIUS_MEDIUM` report.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Citric acid is grounded as sodium citrate. | The ATCC source and TOGO M2424 component name are Citric Acid, while the record uses `CHEBI:53258` / sodium citrate. | `data/normalized_yaml/bacterial/bacillus_medium.yaml`; MIM/CHEBI grounding. |
| Major | DI Water was imported as Tap water. | ATCC Medium 0021 lists `DI Water 1000.0 ml`; the TOGO payload and record say `Tap water 1000 G_PER_L`. | `data/normalized_yaml/bacterial/bacillus_medium.yaml`; TOGO import. |
| Major | pH and autoclave instructions were dropped. | ATCC and TOGO both provide pH 7.4 +/- 0.2 and autoclaving at 121 C; the record has neither structured pH nor preparation text. | `data/normalized_yaml/bacterial/bacillus_medium.yaml`; TOGO pH/comment import. |
| Minor | Source evidence is encoded only as a note. | The TOGO and original ATCC URLs appear in free text, but there is no structured reference or evidence tying ingredient rows to ATCC Medium 0021 / TOGO M2424. | `data/normalized_yaml/bacterial/bacillus_medium.yaml` or the TOGO importer. |

## Recommended Edits

1. Re-ground `Citric Acid` to an exact citric acid CHEBI term.
2. Correct `Tap water` to DI Water / deionized water from the original ATCC PDF.
3. Preserve pH 7.2-7.6 and the 121 C autoclave instruction from TOGO/ATCC.
4. Add structured source provenance for ATCC Medium 0021 and TOGO M2424.
5. Regenerate the merged record after repairing the normalized owner.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the maintained TOGO
  owner after term, water, pH/preparation, and provenance edits.
- Regenerate merges and verify `Bacillus_Medium.yaml` uses a citric acid term,
  no longer calls the solvent tap water, and carries the ATCC pH/autoclave
  instructions.
- Compare the regenerated record manually against the ATCC PDF and TOGO M2424.

## Additional Notes

- The exact prior-report searches used `find` and `rg --no-ignore --hidden`, so
  ignored review reports were included.
