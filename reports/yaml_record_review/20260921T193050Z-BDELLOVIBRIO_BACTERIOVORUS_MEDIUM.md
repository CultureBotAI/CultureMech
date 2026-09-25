# YAML Record Review: BDELLOVIBRIO_BACTERIOVORUS_MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BDELLOVIBRIO_BACTERIOVORUS_MEDIUM.yaml
- Started UTC: 2026-09-21T19:29:04Z
- Finished UTC: 2026-09-21T19:30:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/BDELLOVIBRIO_BACTERIOVORUS_MEDIUM.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bdellovibrio_bacteriovorus_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:000433` |
| Name | `bdellovibrio_bacteriovorus_medium` |
| Original name | `BDELLOVIBRIO BACTERIOVORUS MEDIUM` |
| Source | MediaDive / DSMZ Medium `1012a` |
| Merge status | Generated one-source merge from `bdellovibrio_bacteriovorus_medium` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated DSMZ 1012a merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDive import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated DSMZ 1012a merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- `data/merge_yaml/merged/BDELLOVIBRIO_BACTERIOVORUS_MEDIUM.yaml` denotes MediaDive / DSMZ Medium 1012a, `BDELLOVIBRIO BACTERIOVORUS MEDIUM`, and is a one-source generated merge from `data/normalized_yaml/bacterial/bdellovibrio_bacteriovorus_medium.yaml`.
- The generated merge and normalized owner match for the scientific fields, so future fixes belong in the normalized owner followed by merge regeneration.
- The inspected MediaDive 1012a page and JSON support the bottom-layer amounts in the YAML: 0.8 g/L nutrient broth, 0.5 g/L casamino acids, 0.1 g/L yeast extract, 12 g/L agar, 0.6 g/L MgCl2 x 6 H2O, and 0.3 g/L CaCl2 x 2 H2O at pH 7.2.
- The source also specifies a double-layer plate procedure with 1000 ml distilled water in the bottom layer and a top layer made from 1 percent Bacto agar in 25 mM HEPES buffer plus host-cell suspension; these remain unstructured.
- Exact gitignore-independent searches for `CultureMech:000433`, exact `mediadive.medium:1012a`, `DSMZ Medium 1012a`, and `bdellovibrio_bacteriovorus_medium` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, indexes, and import-priority reports, but no local raw MediaDive 1012a source capture under `data`.

## Evidence

- The MediaDive 1012a JSON reports one 1000 ml `Main sol. 1012a` with nutrient broth, casamino acids, yeast extract, agar, MgCl2 x 6 H2O, CaCl2 x 2 H2O, and distilled water.
- The YAML captures every non-water bottom-layer component from `Main sol. 1012a` at the correct g/L amount and has pH 7.2.
- The MediaDive procedure says the medium is prepared as double-layered agar plates: a pH-adjusted and autoclaved bottom layer, dry plates held for 2 to 3 days, and a top layer with 5 ml aliquots of 1 percent Bacto agar in 25 mM HEPES buffer containing 6.0 g/L HEPES, 0.6 g/L MgCl2 x 6 H2O, and 0.3 g/L CaCl2 x 2 H2O at pH 7.2.
- The top-layer procedure further requires prey bacterium grown on agar slants using DSMZ medium 54 or medium 1, 0.5 ml host-organism cell suspension, and same-day top-layer inoculation.
- The YAML leaves that top-layer solution and host-cell assembly in one long HTML-containing preparation string instead of a structured overlay solution and ordered steps.

## Completeness

- Consequential gaps:
  - The 1000 ml bottom-layer distilled-water row is absent.
  - The 1 percent Bacto agar in 25 mM HEPES top layer is not represented as a solution or ingredient group.
  - The prey-bacterium slant culture, 0.5 ml host suspension, 45 C cooling step, top-layer pour, and same-day inoculation instructions are not scoped as individual ordered steps.
  - The MediaDive 1012a URL is absent from structured `references`.
- Correctly empty optional slots:
  - `target_organisms` and `growth_metrics` are absent; MediaDive 1012a is a formulation/protocol source and not a growth assay for a specific strain.
  - Nutrient broth, casamino acids, and yeast extract are complex mixture ingredients and are correctly left without narrow ChEBI terms.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDive 1012a page or JSON capture under `data/raw`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The double-layer top-layer recipe is unstructured. | MediaDive specifies 1 percent Bacto agar in 25 mM HEPES buffer with HEPES, MgCl2 x 6 H2O, CaCl2 x 2 H2O, pH 7.2, and host-cell suspension; the YAML leaves this in a single HTML-bearing preparation paragraph. | `data/normalized_yaml/bacterial/bdellovibrio_bacteriovorus_medium.yaml`. |
| Major | The bottom-layer final volume is incomplete. | MediaDive 1012a lists 1000 ml distilled water in `Main sol. 1012a`; the YAML omits the water row. | `data/normalized_yaml/bacterial/bdellovibrio_bacteriovorus_medium.yaml`. |
| Minor | Preparation text still contains source HTML and multiple procedural operations in one step. | Step 1 embeds `<p>` and `<b>` tags and combines bottom-layer pH adjustment, boiling, autoclaving, plate drying, prey growth, top-layer aliquot preparation, host-cell addition, and pouring. | `data/normalized_yaml/bacterial/bdellovibrio_bacteriovorus_medium.yaml`. |

## Recommended Edits

1. Add the 1000 ml distilled-water row from `Main sol. 1012a` to the normalized owner.
2. Represent the top layer as a separate solution or preparation substructure with 1 percent Bacto agar in 25 mM HEPES, 6.0 g/L HEPES, 0.6 g/L MgCl2 x 6 H2O, 0.3 g/L CaCl2 x 2 H2O, pH 7.2, 5 ml aliquots, and 0.5 ml host-cell suspension.
3. Split the imported HTML preparation paragraph into ordered plain-text steps that distinguish bottom-layer preparation, top-layer preparation, host-cell addition, pouring, and same-day inoculation.
4. Add a structured MediaDive 1012a reference.
5. Regenerate `data/merge_yaml/merged/BDELLOVIBRIO_BACTERIOVORUS_MEDIUM.yaml` from the repaired normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on the repaired normalized owner.
- Re-fetch MediaDive 1012a JSON and manually compare bottom-layer rows, final pH, double-layer top-layer composition, temperatures, host-suspension volume, and plate handling against the YAML.
- Run `just verify-merges` and `just audit-merge-freshness --json --list` after regenerating.
- Re-check exact `CultureMech:000433`, exact `mediadive.medium:1012a`, and `bdellovibrio_bacteriovorus_medium` occurrences with a gitignore-independent search to verify only the normalized owner and fresh generated merge carry the repaired DSMZ 1012a representation.

## Additional Notes

- The inspected upstream source was the live MediaDive 1012a page plus its JSON download.
- Exact gitignore-independent searches included ignored files where present.
