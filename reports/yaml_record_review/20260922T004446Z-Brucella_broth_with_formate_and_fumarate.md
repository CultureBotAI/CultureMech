# YAML Record Review: Brucella broth with formate and fumarate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml
- Started UTC: 2026-09-22T00:44:46Z
- Finished UTC: 2026-09-22T00:44:46Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008875 |
| Label | brucella_broth_with_formate_and_fumarate |
| Original label | Brucella broth with formate and fumarate |
| Category | bacterial |
| Source accession | TOGO:M2289 |
| Source URL | ATCC PDF `2DA0E266AE7E419288C2291420B9E93E.ashx` |
| Generated path | data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml |
| Maintained owner | data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml |
| Merge fingerprint | 3c7b99e12e94e6df17584eacb7eb6d5d73054eb383170d9f208ac5dfac88f722 |

The reviewed target is a generated merge under `data/merge_yaml/merged`, derived
from the single normalized owner `brucella_broth_with_formate_and_fumarate`.
Future fixes belong in that normalized file, not in the generated merge.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml --out /private/tmp/Brucella_broth_with_formate_and_fumarate.strict.tsv --workers 1 --quiet` | Passed; TSV contained only the header |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 structured URL checks |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and
`just validate-references` were not rerun because the project uv environment tries
to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The record's TOGO M2289 identity is internally consistent. The live TOGO API
names `Brucella broth with formate and fumarate`, uses the same ATCC PDF URL
stored in the YAML notes, reports pH 7.0, and preserves three source quantities
from the final instruction: 0.25 ml of the formate/fumarate stock and
approximately 5 ml Brucella Broth.

The inspected ATCC PDF is the underlying source. It describes ATCC Medium 1540,
Brucella Albimi Broth/Agar with Formate and Fumarate, and defines ATCC Medium
9733 as a 6% sodium formate and 6% fumaric acid solution added separately to
ATCC Medium 1115. The generated record is therefore the correct broad medium but
has lost the stock-solution structure, the Brucella Albimi base recipe, the
source's milliliter units, and both pH 7.0 instructions.

The CHEBI mappings to fumaric acid and sodium formate are appropriate for the
two chemicals inside ATCC Medium 9733. They should be moved into a stock
composition, because the final medium receives a formate/fumarate solution, not
0.25 g/L of each dry chemical.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| TOGO M2289 denotes Brucella broth with formate and fumarate | The TOGO API returns that M2289 name and the same ATCC PDF URL embedded in the record |
| The source uses sodium formate and fumaric acid | The ATCC PDF defines a 6% Formate and 6% Fumarate Solution with both chemicals |
| The source uses Brucella Broth | The ATCC PDF defines an ATCC 1115 broth base from Brucella Broth powder and DI water |
| The final addition is 0.25 ml stock into approximately 5 ml broth | TOGO M2289 extracts these milliliter quantities from the ATCC final-use instruction |

Unsupported or incomplete:

| Generated claim | Problem |
| --- | --- |
| `fumaric acid`, `0.25 G_PER_L` | TOGO and ATCC say 0.25 ml of a 6% formate/fumarate solution, not 0.25 g/L dry fumaric acid. |
| `sodium formate`, `0.25 G_PER_L` | TOGO and ATCC say 0.25 ml of a 6% formate/fumarate solution, not 0.25 g/L dry sodium formate. |
| `Brucella Broth (BD 211088)`, `5 G_PER_L` | TOGO and ATCC say the 0.25 ml stock is added to about 5 ml of Brucella Broth. The Brucella Albimi Broth base itself is 28 g Brucella Broth powder per 1000 ml DI water. |
| No stock solution | The 6% solution's 6 g sodium formate, 6 g fumaric acid, 100 ml DI water, pH 7.0 adjustment, filter sterilization, and separate-delivery instruction are absent. |
| No Brucella Albimi base preparation | The source's broth base recipe, DI water, 121 C autoclave step, and optional scratch formula are absent. |
| No structured reference | The TOGO and ATCC URLs are only free text in `notes`, so reference validation had nothing to check. |

## Completeness

The record is a source identity match but not a complete ATCC Medium 1540 /
ATCC Medium 9733 representation. The maintained owner needs at least two nested
objects: the Brucella Albimi Broth base from ATCC Medium 1115 and the separate
6% formate/fumarate stock. The source also distinguishes broth and agar versions
of the base, says to deliver the formate/fumarate stock separately, and gives a
scratch recipe for Brucella Broth with dextrose, yeast extract, NaCl, sodium
metabisulfite, and peptone/digest ingredients. None of that structure survived
the flat three-row TOGO import.

A gitignore-independent `rg --no-ignore --hidden --pcre2` search for
`CultureMech:008875`, `TOGO:M2289`, the ATCC PDF hash
`2DA0E266AE7E419288C2291420B9E93E`, the active owner slug, and merge
fingerprint `3c7b99...` covered hidden and ignored files under
`data/normalized_yaml`, `data/merge_yaml/merged`, ID registries, generated
indexes, media reports, archived validation reports, and existing YAML review
reports. It found only the active normalized owner, this generated merge, and
expected generated indexes and historical report paths under the pre-rename
`TOGO_M2289_Brucella_broth_with_formate_and_fumarate.yaml` filename. I found no
pre-existing
`reports/yaml_record_review/*Brucella_broth_with_formate_and_fumarate.md`
report.

Empty target-organism and growth-evidence slots are not defects: TOGO and the
inspected ATCC PDF provide recipe instructions, not an organism-specific growth
claim.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | Every imported final-use volume was converted to a mass concentration: 0.25 ml formate/fumarate stock became two `0.25 G_PER_L` rows, and approximately 5 ml Brucella Broth became `5 G_PER_L`. | `data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml` and the TOGO import repair path for milliliter rows |
| Major | The 6% formate/fumarate stock solution was flattened into final-medium chemicals. This drops the 6 g/100 ml stock composition, pH 7.0 adjustment, filter sterilization, DI water, and separate-delivery instruction that define ATCC Medium 9733. | `data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml` |
| Major | The ATCC 1115 Brucella Albimi Broth base is represented only as `Brucella Broth (BD 211088)`. The 28 g/L commercial base, DI water, 121 C autoclave step, and optional from-scratch formula are not modeled. | `data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml` |
| Major | The record lacks structured TOGO/ATCC references, so formulation support is trapped in a `notes` URL and is invisible to reference validation. | `data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml` |

No blocker or minor findings found.

## Recommended Edits

1. Replace the two final `0.25 G_PER_L` chemical rows with one
   formate/fumarate stock addition that preserves the source addition of
   0.25 ml stock to approximately 5 ml Brucella Broth.
2. Model ATCC Medium 9733 as a separate 6% formate and 6% fumarate solution with
   6 g sodium formate, 6 g fumaric acid, 100 ml DI water, pH 7.0 adjustment, and
   filter sterilization.
3. Expand the Brucella Broth parent addition to the ATCC Medium 1115 broth base:
   Brucella Broth powder at 28 g/L in DI water with an autoclave step. Preserve
   the from-scratch recipe in a structured way only if the schema can represent
   it without confusing it with the commercial-powder formulation.
4. Add structured references for TOGO M2289 and the ATCC PDF.
5. Regenerate `data/merge_yaml/merged/Brucella_broth_with_formate_and_fumarate.yaml`.

## Follow-up Checks

- Rerun focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/brucella_broth_with_formate_and_fumarate.yaml`.
- Rerun `just verify-merges` after regeneration and inspect the generated
  Brucella formate/fumarate diff to confirm the merge carries the stock and
  base-broth structure forward.
- Manually compare the regenerated record against the ATCC PDF to confirm the
  6% stock, pH 7.0, filter sterilization, 0.25 ml addition, 5 ml base-broth
  quantity, and 28 g/L Brucella Broth base all survive curation.

## Additional Notes

- TOGO's non-English GMO property label on fumaric acid should be treated as
  imported classification noise; it does not affect the fumaric-acid chemical
  identity.
- The ATCC PDF is only two pages and was fully inspected with local PDF text
  extraction.
