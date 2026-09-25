# YAML Record Review: cytophaga_marine_medium__2e80a746

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/cytophaga_marine_medium__2e80a746.yaml`
- Started UTC: 2026-09-22T13:10:00Z
- Finished UTC: 2026-09-22T13:12:55Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:008092` |
| Name | `cytophaga_marine_medium` |
| Original name | `Cytophaga (Marine) Medium` |
| Source term | `TOGO:M1544` / TOGO Medium M1544 |
| Original source | NBRC Medium 336 |
| Generated from | `TOGO_M1544_Cytophaga_Marine_Medium` |
| Merge fingerprint | `2e80a7463d6e60dfa5444525fc44adfa09d7aa976f56e91051f75484adfa751d` |

The reviewed file is generated from
`data/normalized_yaml/bacterial/TOGO_M1544_Cytophaga_Marine_Medium.yaml`. It is
not the authoritative file to edit.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cytophaga_marine_medium__2e80a746.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/cytophaga_marine_medium__2e80a746.yaml --out /private/tmp/cytophaga_marine_medium__2e80a746.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/cytophaga_marine_medium__2e80a746.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/cytophaga_marine_medium__2e80a746.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a harmless `eutils`/`pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

## Identity and Grounding

- The TOGO API for M1544 identifies the source as NBRC Medium 336 and links the
  NBRC URL that appears in the generated `notes`.
- NBRC Medium 336 and TOGO M1544 agree on the four formulation entries:
  1 g Bacto Tryptone (Difco), 1 g yeast extract, 15 g agar if needed, and
  1 L seawater. Both sources report pH 7.2.
- The generated record correctly preserves the three dry ingredients and the
  TOGO source identity, but it turns the source seawater entry into an embedded
  `solutions` reference to `mediadive.solution:1801` at `1 G_PER_L`.
- The current maintained normalized input already repaired this identity and
  arithmetic problem: it now stores `Seawater*` as a main ingredient at `1.0`
  `L`, adds pH 7.2, marks `composition_type: SEMI_DEFINED`, and records the
  NBRC seawater footnote in `notes`.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/raw`, `data/normalized_yaml`, and `data/merge_yaml/merged` found no
  raw upstream capture for M1544 or NBRC 336; it found the normalized source,
  generated record, source indexes, and other records that reference the shared
  `mediadive.solution:1801` stock.

## Evidence

- Supported by NBRC Medium 336 and TOGO M1544: yeast extract at 1 g, Bacto
  Tryptone (Difco) at 1 g, optional agar at 15 g, seawater at 1 L, and pH 7.2.
- Supported by NBRC Medium 336 and TOGO M1544: the seawater asterisk denotes
  filtered aged seawater or artificial seawater made with Daigo's Artificial
  Seawater SP from Wako Pure Chemical Industries.
- Unsupported in the generated record: `solutions[0].concentration.value: '1'`
  with `unit: G_PER_L` for `Seawater*`. The source amount is a one-liter base,
  not a 1 g/L stock solution.
- Unsupported in the generated record: the absence of `ph_value` and the
  absence of the NBRC seawater footnote. Both claims are present in the
  inspected source and in the repaired normalized source.
- No target-organism, growth-metric, or incubation-temperature claims are
  present.

## Completeness

- Consequentially stale: generated `composition_type`, pH, seawater, references,
  quality flags, and explanatory notes all lag the maintained normalized input's
  2026-09-11 `RESOLVED_TOGO_M1544_SCORE15` repair.
- Correctly absent: no sterilization, incubation temperature, target-organism,
  or growth evidence is stated; NBRC and TOGO do not provide those details on
  the inspected pages.
- Empty `references` is stale, not source-inherent; the maintained input now
  cites both TOGO M1544 and NBRC Medium 336.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated output is stale relative to the repaired normalized TOGO M1544 source. | `data/normalized_yaml/bacterial/TOGO_M1544_Cytophaga_Marine_Medium.yaml` has a 2026-09-11 repair that moves `Seawater*` back into `ingredients` at `1.0 L`, adds pH 7.2, switches to `SEMI_DEFINED`, and adds references; none of those changes are present in the generated file. | Regenerate `data/merge_yaml/merged/cytophaga_marine_medium__2e80a746.yaml` from the current normalized input. |
| Major | The generated seawater amount is dimensionally wrong. | NBRC 336 and TOGO M1544 list `Seawater*` as 1 L in the main formula; the generated record stores a `mediadive.solution:1801` solution at 1 g/L with a placeholder `name: Unknown solution`. | Already fixed upstream in `data/normalized_yaml/bacterial/TOGO_M1544_Cytophaga_Marine_Medium.yaml`; regeneration should remove the bad generated solution block. |
| Major | The generated record omits pH 7.2 and the seawater footnote. | Both NBRC and TOGO state pH 7.2. NBRC explains the asterisked seawater as filtered aged seawater or artificial seawater using Daigo's Artificial Seawater SP; the generated record keeps only `Seawater*`. | Already fixed upstream in `data/normalized_yaml/bacterial/TOGO_M1544_Cytophaga_Marine_Medium.yaml`; regeneration should propagate these values. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so the 2026-09-11 repair of
   `data/normalized_yaml/bacterial/TOGO_M1544_Cytophaga_Marine_Medium.yaml`
   reaches this generated record.
2. After regeneration, confirm `Seawater*` is a main ingredient at `1.0 L`, not
   a `solutions` entry with `1 G_PER_L`, and that no `Unknown solution`
   placeholder remains.
3. Confirm the regenerated record carries pH 7.2, `SEMI_DEFINED`, the TOGO and
   NBRC references, and the NBRC footnote about aged or artificial seawater.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated
  `cytophaga_marine_medium__2e80a746.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` to prove the
  generated layer matches current normalized inputs.
- Manually compare the regenerated record against TOGO M1544 and NBRC Medium
  336 to ensure the optional agar row and seawater footnote are still scoped
  correctly.

## Additional Notes

- The referenced `data/normalized_yaml/bacterial/mediadive_1801_Seawater.yaml`
  stock is itself flagged `incomplete_composition` and is not the formula that
  NBRC 336 cites. The NBRC source only defines the asterisked seawater as
  filtered aged seawater or artificial seawater using Daigo's Artificial
  Seawater SP.
- The NBRC Medium 336 HTML was available through the source URL recorded in the
  TOGO API payload.
