# YAML Record Review: deferribacter_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/deferribacter_medium__4cf00e52.yaml
- Started UTC: 2026-09-22T14:21:22Z
- Finished UTC: 2026-09-22T14:21:22Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002108`, label
`deferribacter_medium`, original name `DEFERRIBACTER MEDIUM`, under
`data/merge_yaml/merged/`.

The record is generated from maintained MediaDive/DSMZ input at
`data/normalized_yaml/bacterial/deferribacter_medium.yaml`. Future fixes belong
in that normalized owner, the MediaDive import that expands nested solutions,
and a source-link reconciliation for DSMZ Medium 935.

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/deferribacter_medium__4cf00e52.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/deferribacter_medium__4cf00e52.yaml --out /private/tmp/deferribacter_medium__4cf00e52.strict.tsv --workers 1 --quiet` | Pass |
| `linkml-reference-validator validate data data/merge_yaml/merged/deferribacter_medium__4cf00e52.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/deferribacter_medium__4cf00e52.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| `just validate-history` | Not checked: the documented validator targets standalone files under `history/`; this generated record stores embedded `curation_history`. |

Term validation emitted only the known `eutils` `pkg_resources` deprecation
warning before `Validation passed`.

## Identity and Grounding

The local `media_term` says this is DSMZ Medium 935, `DEFERRIBACTER MEDIUM`.
The MediaDive REST record for medium 935 supports that identity, pH range
6.5-6.7, and a 1003 ml main solution containing 1 ml Trace element solution
SL-10, 1 ml Selenite-tungstate solution, 1 ml Wolin's vitamin solution (10x),
and 1000 ml distilled water.

The evidence link embedded in the generated YAML is not currently a matching
source for this identity. It points to `DSMZ_Medium935a.pdf`; the fetched PDF is
headed `935a: DEFERRIBACTER DESULFURICANS MEDIUM` and contains a different
formula with KCl, KH2PO4, Modified Wolin's mineral solution, Na-acetate
0.80 g, Na2S, 10 ml Wolin's vitamin solution, and final pH 6.5. Those rows
match a sibling Deferribacter Desulfuricans medium, not the MediaDive 935
formula imported here.

The exact ignored-file search
`rg --no-ignore --hidden -n "mediadive.medium:935|DSMZ_Medium935a|DEFERRIBACTER MEDIUM|deferribacter_medium" data/normalized_yaml data/merge_yaml`
covered normalized records, generated merged records, and generated indexes. It
found this DSMZ 935 owner, the separate TOGO/NBRC M1677 Deferribacter owner,
and `DEFERRIBACTER_DESULFURICANS_MEDIUM.yaml`, whose `media_term` is
`mediadive.medium:935a`. The DSMZ 935 and DSMZ 935a links need explicit
source reconciliation.

## Evidence

The local ingredient values in this generated record match the MediaDive REST
object for medium 935, after MediaDive's 1003 ml final-volume normalization:
for example, 1 g NH4Cl becomes 0.997009 g/L, 30 g NaCl becomes 29.9103 g/L, and
2 g yeast extract becomes 1.99402 g/L.

The record loses solution boundaries after that point. MediaDive 935 lists
three nested 1 ml stock additions: Trace element solution SL-10, Selenite-
tungstate solution, and Wolin's vitamin solution (10x). The generated record
has no `solutions` array and instead promotes every stock child into top-level
`ingredients` at stock concentration. HCl 2.5 g/L, FeCl2 x 4H2O 1.5 g/L,
NaOH 0.5 g/L, Na2SeO3 x 5H2O 0.003 g/L, biotin 0.02 g/L, and the other vitamin
rows are stock concentrations, not final-medium concentrations after 1 ml is
added to the 1003 ml main solution.

The MediaDive REST object supports the main anoxic preparation step and the SL-10
stock preparation step, both of which are present. The imported recipe omits
the final 1000 ml distilled-water row from the main solution and the water rows
for the three nested stocks.

## Completeness

Consequential gaps:

- The maintained record's human `notes` point reviewers to a DSMZ 935a PDF that
  no longer supports the imported DSMZ 935 formula.
- Three 1 ml stock additions are missing as solution rows and are represented
  only by their unscaled child ingredients.
- Main-solution distilled water and each stock solution's water are absent.
- Selenite-tungstate and Wolin-vitamin stock ingredients are top-level final
  ingredients even though they should be nested or scaled by 1/1003.
- The SL-10 stock preparation step is copied as a final-medium
  `preparation_steps` entry without the context that it prepares an internal
  stock.

No `target_organisms` or `growth_data` rows are required for this DSMZ formula;
their absence is a non-defect.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The record's stored PDF link supports DSMZ 935a, not the DSMZ 935 formula imported here. | MediaDive REST medium 935 and local ingredients agree with each other, but the fetched `DSMZ_Medium935a.pdf` is headed `DEFERRIBACTER DESULFURICANS MEDIUM` and has a different formula. | `data/normalized_yaml/bacterial/deferribacter_medium.yaml`; MediaDive source-link import |
| Major | Three 1 ml stock solutions are flattened into final ingredients. | MediaDive 935 lists Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x) as nested 1 ml recipe rows; the generated record stores only their child rows at stock concentration. | MediaDive import and solution-expansion transform |
| Major | Water rows are missing. | MediaDive 935 includes 1000 ml distilled water in the 1003 ml main solution and water in each nested 1 L stock; none is present in this generated record. | `data/normalized_yaml/bacterial/deferribacter_medium.yaml`; MediaDive importer |
| Minor | Stock-preparation text is not scoped to the stock. | The FeCl2/HCl dissolution step belongs to Trace element solution SL-10, but the generated record lists it as step 2 of the final medium. | MediaDive preparation-step importer |

## Recommended Edits

- Reconcile DSMZ Medium 935 with the current DSMZ PDF links and correct the
  maintained `notes` URL or medium identity before changing formula rows.
- Preserve Trace element solution SL-10, Selenite-tungstate solution, and
  Wolin's vitamin solution (10x) as 1 ml solution ingredients, or scale their
  children into the final 1003 ml recipe with provenance back to the stock.
- Restore main and nested distilled-water rows in their owning solution scopes.
- Scope the SL-10 FeCl2/HCl preparation text to the SL-10 stock rather than the
  final medium.
- Regenerate `data/merge_yaml/merged/deferribacter_medium__4cf00e52.yaml` after
  the normalized DSMZ 935 owner is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated DSMZ
  935 record.
- Search ignored files for `mediadive.medium:935`, `mediadive.medium:935a`,
  `DSMZ_Medium935a`, and `DSMZ_Medium935b` to verify DSMZ 935 and DSMZ 935a/b
  are no longer cross-linked.
- Compare the regenerated 1003 ml main solution and three stock solutions
  against MediaDive REST medium 935 or the reconciled DSMZ primary source.

## Additional Notes

- The exact source and duplicate search included ignored and hidden files.
- `linkml-reference-validator` reported zero reference checks, so its pass does
  not exercise DSMZ or MediaDive source identifiers.
