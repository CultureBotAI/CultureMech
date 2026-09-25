# YAML Record Review: thermodesulfobacterium_hydrogenophilum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_hydrogenophilum_medium__c1daf6d7.yaml
- Started UTC: 2026-09-25T10:11:00Z
- Finished UTC: 2026-09-25T10:15:30Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobacterium_hydrogenophilum_medium__c1daf6d7`, which represents direct MediaDive/JCM medium `J301` as `CultureMech:002659`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The target is grounded to MediaDive/JCM `J301`, but its generated pH 9.0 is not the finished-medium pH on the live JCM 301 page. JCM adjusts the main medium to pH 6.5, then separately adjusts the 100 ml Growth stimulating factors stock to pH 9.0. An exact ignored-inclusive search for `mediadive.medium:J301` and `GRMD=301` found a separate `TOGO_M296_Thermodesulfobacterium_Hydrogenophilum_Medium` branch that still generates `data/merge_yaml/merged/THERMODESULFOBACTERIUM_HYDROGENOPHILUM_MEDIUM.yaml`.

## Evidence

JCM 301 and MediaDive J301 both describe a main solution with 1 ml Trace element solution, 10 ml Trace vitamins, 1 ml Growth stimulating factors, and 1000 ml distilled water. The Trace element solution is a 1 L stock prepared from 12.8 g nitrilotriacetic acid and trace salts. Growth stimulating factors is a 100 ml stock containing 0.5 g isobutyric acid, 0.5 g valeric acid, 0.5 g 2-methylbutyric acid, 0.5 g 3-methylbutyric acid, 0.2 g caproic acid, and 0.6 g succinic acid. Trace vitamins is a 1 L stock with milligram quantities of vitamins.

## Completeness

The generated record carries the JCM source note and much of the anaerobic preparation text, including the 200 kPa `H2-CO2` instruction. It does not preserve the Trace element, Trace vitamins, or Growth stimulating factors stock identities; it also lacks the 2-methylbutyric acid and 3-methylbutyric acid rows from the growth-factor stock.

## Findings

- High: pH 9.0 was promoted from the Growth stimulating factors stock to the top-level medium. The final JCM 301 medium is adjusted to pH 6.5 before dispensing and readjusted to pH 6.5 after a 70 C incubation; only the 100 ml Growth stimulating factors stock is adjusted to pH 9.0.
- High: Trace element, Trace vitamins, and Growth stimulating factors were flattened into direct ingredients at stock concentration. The generated record carries 12.8 g/L nitrilotriacetic acid, 5 g/L isobutyric acid, 5 g/L valeric acid, and several vitamin stock concentrations as final-medium rows.
- High: LB Medium constituent rows were injected into this JCM 301 recipe. The generated target contains commercial LB notes and 10 g/L Tryptone, 5 g/L Yeast extract, and 10 g/L Sodium chloride rows that do not appear in the JCM 301 source recipe.
- Medium: 2-methylbutyric acid and 3-methylbutyric acid from Growth stimulating factors are missing even though the neighboring isobutyric, valeric, caproic, and succinic acid rows were imported.
- Medium: the TOGO M296 import of the same JCM 301 source is unmerged with the direct MediaDive/JCM J301 branch.

## Recommended Edits

- Correct the J301 import so the top-level medium pH is 6.5 and the pH 9.0 adjustment remains scoped to the Growth stimulating factors stock.
- Rebuild `data/normalized_yaml/bacterial/thermodesulfobacterium_hydrogenophilum_medium.yaml` with Trace element, Trace vitamins, and Growth stimulating factors modeled as 1 ml, 10 ml, and 1 ml stock additions rather than top-level stock components.
- Add the missing 2-methylbutyric acid and 3-methylbutyric acid rows to the Growth stimulating factors stock.
- Remove the LB Medium commercial-product deconstruction from this record.
- Canonicalize the TOGO M296 and direct MediaDive/JCM J301 branches before merge generation.

## Follow-up Checks

- Regenerate merged YAML and verify J301 has pH 6.5, no LB Medium rows, and stock additions for Trace element, Trace vitamins, and Growth stimulating factors.
- Confirm the regenerated J301 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J301` and `GRMD=301` to ensure the duplicate uppercase TOGO output has collapsed into the canonical J301 record.

## Additional Notes

None found.
