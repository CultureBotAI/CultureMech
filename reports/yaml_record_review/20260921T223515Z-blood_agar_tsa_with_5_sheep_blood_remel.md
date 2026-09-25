# YAML Record Review: blood_agar_tsa_with_5_sheep_blood_remel

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/blood_agar_tsa_with_5_sheep_blood_remel.yaml`
- Started UTC: 2026-09-21T22:35:17Z
- Finished UTC: 2026-09-21T22:36:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:009339` |
| Generated label | `blood_agar_tsa_with_5_sheep_blood_remel` |
| Original name | `Blood agar (TSA with 5% sheep blood) (Remel)` |
| Source term | `TOGO:M2791` / `Blood agar (TSA with 5% sheep blood) (Remel)` |
| Maintained owner | `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml` |
| Generated status | Derived from one active normalized TOGO input by `merge_recipes.py`; future fixes belong in normalized YAML or TOGO import/repair rules, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:009339`, `TOGO:M2791`,
and `M2791` found one active normalized owner plus generated normalized-index
and merged-record copies. It did not find another maintained YAML owner for the
same stable ID or TOGO accession.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/blood_agar_tsa_with_5_sheep_blood_remel.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/blood_agar_tsa_with_5_sheep_blood_remel.yaml --out /private/tmp/blood_agar_tsa_with_5_sheep_blood_remel.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/blood_agar_tsa_with_5_sheep_blood_remel.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/blood_agar_tsa_with_5_sheep_blood_remel.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema`, `just validate-strict`, and
`just validate-terms` entrypoints were not used directly because this checkout's
project `uv` environment currently tries to build `llvmlite==0.46.0` under
Python 3.13 and fails inside `setuptools` before a target-specific check runs.
The no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- `TOGO:M2791` identifies the intended Remel commercial blood agar variant:
  `Blood agar (TSA with 5% sheep blood) (Remel)`.
- The imported TOGO identity agrees between the generated merge and the single
  normalized owner.
- The formulation does not agree with TOGO. The source API lists
  demineralized water at 1 L, sheep blood at 5 percent, commercial
  `Tryptic soy agar (TSA)` at 40 g, CO2, and pH `7.3 +/- 0.2`; the YAML uses
  water at `1 G_PER_L`, keeps the sheep blood as `PERCENT_W_V`, expands the
  commercial TSA into a generic 45 g/L component set, and omits the pH.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/togo-M2791.json` | TOGO M2791 name, pH, component amounts, GMO labels, properties, roles, and source comments |
| `/private/tmp/wiki-tryptic-soy-broth.html` | The Wikipedia page cited by the YAML's generic TSB/TSA expansion |

Supported:

- The medium label and TOGO accession are supported by the TOGO API record.
- The presence of sheep blood and a commercial Tryptic Soy Agar component is
  supported.
- The presence of CO2 in the TOGO extraction is supported, but its scope is not
  a formulation ingredient: the source comment scopes 5 percent CO2 to
  incubation for 16 to 20 hours at 37 C.

Unsupported or over-scoped:

- The water row `1 G_PER_L` conflicts with TOGO's `demineralized water` value
  of 1 L.
- `Sheep blood` at `5 PERCENT_W_V` is over-specified; TOGO gives a 5 percent
  liquid blood component and does not establish weight per volume.
- The six generic TSA expansion rows are not supported for this exact Remel
  product. TOGO M2791 lists 40 g of opaque `Tryptic soy agar (TSA)`, while the
  YAML expands that to 45 g/L of casein digest, soymeal digest, glucose, NaCl,
  dipotassium phosphate, and agar from a generic Wikipedia article.
- `ph_value` is missing even though the TOGO API records pH `7.3 +/- 0.2`.

## Completeness

- Consequentially incomplete: the maintained owner is missing the TOGO pH.
- Consequentially incomplete: the record needs to preserve the 40 g/L opaque
  Remel TSA boundary instead of replacing it with an unsupported generic TSA
  formulation.
- Consequentially incomplete: the CO2 row needs manual scoping against the
  source sentence. It may belong under atmosphere or incubation metadata rather
  than in `ingredients`.
- Bounded search: ignored files were included in the exact M2791 search
  described under `Target`, and no duplicate maintained owner for M2791 was
  found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The record decomposes 40 g/L opaque Remel Tryptic Soy Agar into unsupported generic TSA constituents and the expansion sums to 45 g/L. | TOGO M2791 API JSON; Wikipedia TSB/TSA page cited by the current YAML. | `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml` |
| major | Demineralized water is dimensionally wrong at `1 G_PER_L`; TOGO gives 1 L. | TOGO M2791 API JSON. | `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml` |
| major | The 5 percent sheep blood supplement is over-specified as `PERCENT_W_V` without source support. | TOGO M2791 API JSON. | `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml` |
| major | The record omits the TOGO pH value `7.3 +/- 0.2`. | TOGO M2791 API JSON. | `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml` |
| major | CO2 is represented as a variable-concentration ingredient even though the TOGO source comment scopes 5 percent CO2 to the incubation atmosphere. | TOGO M2791 API JSON. | `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml`,
   replace the generic Wikipedia-derived TSA expansion with an opaque
   `Tryptic soy agar (TSA)` ingredient at 40 g/L that preserves the Remel
   product boundary.
2. Correct `demineralized water` from `1 G_PER_L` to `1000 ML_PER_L`.
3. Review and correct the sheep-blood unit so the YAML preserves TOGO's 5
   percent liquid supplement without asserting unsupported weight per volume.
4. Add `ph_value: 7.3` and preserve the `+/- 0.2` tolerance in a curation note
   or the narrowest available schema slot.
5. Re-scope CO2 from an ingredient to incubation atmosphere metadata if the
   schema supports it; otherwise flag that TOGO extracted a gas condition from
   the growth sentence rather than a chemical medium component.
6. Rerun merge generation so the derived record reflects the normalized
   curation.

## Follow-up Checks

- Run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/blood_agar_tsa_with_5_sheep_blood_remel.yaml`.
- Run the same validators on the regenerated
  `data/merge_yaml/merged/blood_agar_tsa_with_5_sheep_blood_remel.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch TOGO M2791 and manually compare water, sheep blood, opaque TSA,
  CO2, and pH before accepting the curation.

## Additional Notes

- `find reports/yaml_record_review -name '*blood_agar_tsa_with_5_sheep_blood_remel.md'`
  returned no path before this report was created.
- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
