# YAML Record Review: Hyperthermus Butylicus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hyperthermus_butylicus_medium__f6540234.yaml
- Started UTC: 2026-09-23T14:00:15Z
- Finished UTC: 2026-09-23T14:01:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:001619 |
| Name | hyperthermus_butylicus_medium |
| Original name | HYPERTHERMUS BUTYLICUS MEDIUM |
| Class | MediaRecipe |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 6.5-7.0 |
| Source identity | MediaDive/DSMZ Medium 491, HYPERTHERMUS BUTYLICUS MEDIUM |
| Generated path reviewed | data/merge_yaml/merged/hyperthermus_butylicus_medium__f6540234.yaml |
| Maintained owner | data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml |

The reviewed file is generated from the maintained MediaDive/DSMZ import above.
Future fixes should update `data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml`,
repair MediaDive stock-solution import for DSMZ 491, and regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hyperthermus_butylicus_medium__f6540234.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hyperthermus_butylicus_medium__f6540234.yaml --out /private/tmp/hyperthermus_butylicus_medium__f6540234.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hyperthermus_butylicus_medium__f6540234.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hyperthermus_butylicus_medium__f6540234.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:001619` is the MediaDive import
  of DSMZ Medium 491, and the inspected DSMZ PDF and MediaDive REST record both
  identify HYPERTHERMUS BUTYLICUS MEDIUM.
- A gitignore-independent exact search for `CultureMech:001619` over
  `data/normalized_yaml/archaea`, `data/merge_yaml/merged`, MediaDive indexes,
  and the review manifest found only the maintained MediaDive 491 record and
  its generated merged copy.
- A gitignore-independent exact search for `mediadive.medium:491` over
  `data/normalized_yaml/archaea`, `data/merge_yaml/merged`, and MediaDive
  indexes found this MediaDive record plus a KOMODO 491 record that links to the
  same DSMZ source.
- The pH range, final-medium direct salts, 0.1% w/v stock additions, tryptone,
  sulfur, sodium sulfide, and DSMZ preparation text are imported with the
  correct DSMZ 491 identity.
- NiCl2 x 6H2O is grounded to generic nickel dichloride.

## Evidence

- MediaDive correctly normalizes the DSMZ final-medium grams, milligrams, and
  0.1% w/v stock additions against its 1027 ml final volume. Examples include
  17 g NaCl as 16.5531 g/L, 15 mg H3BO3 as 0.0146056 g/L, 2 ml 0.1% NiCl2 x
  6H2O as 0.00194742 g/L, and 0.5 ml 0.1% sodium resazurin as 0.000486855 g/L.
- DSMZ adds 10 ml Modified Wolin's mineral solution and lists that stock below
  the main formula. The YAML instead flattens the stock solutes into
  final-medium ingredients at undiluted stock concentrations.
- Flattening merged three final-medium rows with their stock namesakes: H3BO3
  is `0.0246056 G_PER_L`, CaCl2 x 2H2O is `0.830282 G_PER_L`, and NiCl2 x 6H2O
  is `0.03194742 G_PER_L`.
- MgSO4 x 7H2O and NaCl are also summed across main and Modified Wolin
  boundaries, giving `6.40798 G_PER_L` and `17.5531 G_PER_L`.
- DSMZ lists 1000 ml distilled water in the final medium and another 1000 ml in
  the Modified Wolin stock; neither water row appears in the YAML.
- The Modified Wolin NTA/KOH stock-preparation instruction appears as a
  top-level final-medium pH-adjustment step.

## Completeness

- The record needs a nested 10 ml Modified Wolin stock addition that preserves
  its water row and preparation note.
- The final-medium water row needs to be represented.
- The MediaDive import should be reconciled with the parallel TOGO M2675 and
  KOMODO 491 imports so all DSMZ 491 records converge on one formulation or an
  explicit source relationship.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Modified Wolin's mineral solution is flattened into the final medium. | DSMZ adds 10 ml of the mineral stock from Medium 141; the YAML has the stock's NTA and mineral rows as top-level ingredients at undiluted stock concentration. | `data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml`; MediaDive stock-solution import logic. |
| Major | Duplicate cleanup summed final-medium rows with stock-solution rows. | H3BO3, CaCl2 x 2H2O, NiCl2 x 6H2O, MgSO4 x 7H2O, and NaCl are recorded as sums of MediaDive main-solution g/L values and Modified Wolin stock g/L values. | `data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml`; duplicate cleanup must preserve solution boundaries. |
| Major | Source water volumes are omitted. | DSMZ 491 has 1000 ml distilled water in the final medium and 1000 ml in the Modified Wolin stock; no water row appears in the YAML. | `data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml`; MediaDive volume import. |
| Major | Modified Wolin stock preparation is scoped to the final medium. | The NTA/KOH pH-adjustment text belongs to the mineral stock, but the YAML records it as final-medium preparation step 3. | `data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml`; preparation import should keep stock preparation under the nested solution. |
| Major | DSMZ 491 exists as unresolved parallel imports. | The repository has separate MediaDive 491, TOGO M2675, and KOMODO 491 records for HYPERTHERMUS BUTYLICUS MEDIUM. | Normalized duplicate-resolution inputs for the MediaDive, TOGO, and KOMODO records. |
| Minor | NiCl2 x 6H2O lost exact hydrate grounding. | The source names nickel chloride hexahydrate, but the YAML grounds it to generic CHEBI:34887 nickel dichloride. | `data/normalized_yaml/archaea/hyperthermus_butylicus_medium.yaml`; hydrate-aware CHEBI mapping. |

## Recommended Edits

1. Restore Modified Wolin's mineral solution as a 10 ml nested stock addition
   and move all of its component rows out of final-medium `ingredients`.
2. Undo the H3BO3, CaCl2 x 2H2O, NiCl2 x 6H2O, MgSO4 x 7H2O, and NaCl
   cross-boundary sums.
3. Represent both DSMZ distilled-water rows as source volumes.
4. Attach the NTA/KOH pH-adjustment note to the Modified Wolin stock, not to the
   final medium.
5. Re-ground NiCl2 x 6H2O to an exact hydrated term if CHEBI exposes one.
6. Reconcile this record with TOGO M2675 and KOMODO 491 before or after
   regenerating `data/merge_yaml/merged/`.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  MediaDive 491 merged record.
- Manually compare the regenerated record against the MediaDive 491 REST record
  and the DSMZ 491 PDF.
- Verify DSMZ 491 appears as one merged recipe or as explicitly linked
  provider-specific records rather than three unrelated stable IDs.

## Additional Notes

- Unlike the TOGO M2675 import, MediaDive already applies correct
  final-volume-normalized amounts for the DSMZ final-medium 0.1% stock
  additions; those rows should not be converted back to raw stock volumes unless
  the model gains an explicit representation for the original 0.1% stocks.
