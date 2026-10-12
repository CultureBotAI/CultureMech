# Public Stock Evidence and Corrections

Two authoritative normalized records were curated locally against baseline
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
The all-record objective remains unfinished; this curation is uncommitted.

| Record | Stable ID | Scoped claim rows | New evidence entries |
| --- | --- | ---: | ---: |
| `taiyang_medium_no_9_prototype.yaml` (P2) | `CultureMech:010432` | 29 | 28 |
| `m9_sng_medium.yaml` (P8) | `CultureMech:010438` | 20 | 9 |

The [independent diff audit](diff-audit.json) verifies 37 added evidence entries
(36 supporting entries and one counterevidence entry), two added page references,
one enriched/normalized existing DOI citation, and two append-only events.
There are five quantity/unit corrections, all in P8: one stock-strength
correction and four stock-dose basis corrections. P2 adds one unquantified
makeup-water node; it does not add a numeric quantity. Scientific labels,
ontology mappings, physical state, pH, preparation, variants, stable IDs and
prior history are preserved. No growth association or new medium is created.

## P2

The complete [user-contributed P2 page](https://mediadive.dsmz.de/medium/P2)
supports 14 direct ingredient rates, ten artificial-seawater stock rates,
two haemin-stock input rates and two dataset-declared stock doses. All existing
numeric values remain unchanged. Each claim is scoped to its preparation stage;
the seawater ingredients are not added again to the receiving-medium ingredient
list. Conditional agar remains limited to this record's existing solid state.

The haemin preparation explicitly makes the stock up to 100 ml. Its 50 mg
haemin input therefore supports 0.5 g/L; 1 ml of the specified 1 N NaOH reagent
per 100 ml stock supports a 10 ml/L input rate, not a solid-NaOH mass or an
inferred molarity. The missing distilled-water node is restored with this
makeup instruction and no fixed water amount. It is not 100 ml added water.

Author: Taiyang Jin; page publication/last modification: 21 June 2023.
Source type is a user-contributed dataset page, discovered from the existing
record reference. The displayed untested/uncurated disclaimer and absence of a
valid journal reference are retained. Dataset quantities do not establish
experimental performance or an independently verified final-volume protocol.

The earlier [P2 handoff](../20261007-p2-claim-handoff.json) remains an immutable
pre-apply record. The applied per-record report is in [records](records/).

## P8

The [DOI-linked article](https://doi.org/10.1007/s11104-022-05822-6) is *Soil
microbiota promotes early developmental stages of Phelipanche ramosa L. Pomel
during plant parasitism on Brassica napus L.*, by Lisa Martinez, Jean-Bernard
Pouvreau, Gregory Montiel, Christophe Jestin, Philippe Delavault, Philippe Simier
and Lucie Poulin. Online publication is 8 December 2022; volume 483 is dated
2023. The citation uses 2023 with the online date separately recorded.

The publicly available [HAL v1 author manuscript](https://hal.inrae.fr/hal-04370677v1/file/Submitted_version_LM.pdf)
was found through the institutional laboratory publication list. Its matching
DOI, title, authors and publication context were checked. PDF page 11 (printed
10), methods lines 303-308, was inspected in extracted text and a PDFKit page
render. The publisher's methods and supplements were not inspected. This is
evidence from the identified author-manuscript version, not a claim of access
to the publisher's version of record.

- M9 5X potassium dihydrogen phosphate is corrected from 51 to 15 g/L.
  The [P8 dataset page](https://mediadive.dsmz.de/medium/P8) still says 51.0 g/L;
  its exact row remains as `REFUTE` counterevidence on the same ingredient.
  The conflict is explicit, not averaged or called an independently verified
  variant. The corrected value's `source` now identifies the DOI.
- Stock additions are represented as literal batch amounts: 0.002 L each of
  magnesium sulfate, sinigrin and M9 stocks, and 0.000010 L calcium chloride
  stock. These convert only ml/microliters to liters. They replace rates that
  used the dataset's unverified 6.1 ml denominator. The `L` unit is a batch
  amount, not a per-liter working concentration.
- All seven stock ingredient rates have article-backed evidence. Sinigrin's
  source hydrate description is recorded in notes without inventing a hydration
  number or molar conversion.
- The manuscript describes 10 ml cultures. No exact water input or final-medium
  component dilution is inferred. The malformed page-scoped M9 `NaN` anchor is
  not promoted to a global solution accession.

The existing bare DOI bibliography entry is normalized and enriched, not
duplicated. The page bibliography identifies its own 2024 publication year and
counterevidence role. The [earlier P8/P9 handoff](../20261007-p8-p9-primary-source-handoff.md)
remains unchanged; P9's separate identity conflict is not repaired by this batch.

## Source Guards

Captures accessed on 2026-10-07, under `/tmp/ingredient-media-20261007`:

| Capture | SHA256 |
| --- | --- |
| `P2-medium-page.html` | `b8081b72d9351bd6e873c6c77484baccd7c01a39cd6bd4cd557ec3568e6eff85` |
| `P8-medium-page.html` | `6730f629992bfb0c3e536c4a535361b85415212a4717b3c81f930606c4461c39` |
| `P8-P9-HAL-submitted.pdf` | `2788ca1a054d5ff67f02af146db31e0735153886d9c5de54c0c607629a9c9f1c` |

The guarded reviewer is `scripts/review_public_stock_concentrations.py`.
It checks byte hashes, HTML table/recipe identities and units, the reviewed
P2 claim map, PDF provenance and normalized method text, and full baseline
record hashes. It reconstructs the [frozen plan](plan.json) before any apply
or readback, including no-op replay. Exact tracked paths, file symlinks,
concurrent edits, changed claims or sources, and schema errors are checked
before writing. Each record has exactly one `- Record:` marker in its report.
No historical acquisition snapshot or prior corpus report is rewritten.

## Validation

Baseline/post-edit strict scans pass all 15,910 normalized records with zero
errors. Both targets' baseline/post schema checks, IDs, guarded apply,
readback, no-op replay, prior P3/P6 readback, independent semantic diff and
exact-path coverage pass. Actual-group retention passes both singleton groups.
The expanded [retention check](merge-retention-with-context.json) also passes
root notes and curation history, in addition to ingredients, stocks, preparation,
state, pH, evidence and references.

All 44 pre-apply tests passed. The initial broader run had 794 passing tests
and one historical-snapshot failure: its byte-for-byte P8 assumption predated
this explicit repair. The original fingerprint snapshot remains unchanged.
The test now verifies the successor's before/after hashes and independent
inversion, then requires the same ingredient-set fingerprint for both versions.
This is not a formulation-equivalence assertion. The targeted 55-test recheck
passes, followed by **795 passing focused tests**, with no errors, failures or
skips. The initial failure remains in [validation.json](validation.json);
the successful terminal rerun is recorded in
[validation-recheck.json](validation-recheck.json).

Checks use isolated Python 3.11, not the maintained Python 3.13 environment
or CI. The full test suite was not rerun. Both baseline target jobs and all 19
post-apply jobs are terminal, as are the test and expanded-retention rechecks.
Black, Ruff and `git diff --check` pass. Global merge verification fails with
1,247 name conflicts and 3,287 fingerprint issues. Product validation fails
because `oaklib` is missing; both reference validations fail because
`linkml-reference-validator` is unavailable. Manual source inspection is not
reported as an automated reference-validation pass.
[Freshness](merge-freshness.json) fails with 6,320 tracked and 6,492 fresh
records: 3,719 only tracked, 3,891 only fresh, 1,645 changed and 956 unchanged.
Regeneration was temporary only; no generated merges are published.

The [then-current cumulative audit](../20261007-diff-audit-after-public-stocks.json) counts
4,853 edited records, 28,128 new evidence entries, 4,887 new references,
4,859 curation events and 1,169 quantity/unit corrections. Four of those latest
five corrections change stock-dose basis, not stock strength.
[Then-current follow-up coverage](../20261007-followup-coverage-after-public-stocks.json) is
8,106 of 15,910 normalized records, leaving 7,804 outside these reports.
Reports can still contain unresolved claims. Six public targets remained at
this checkpoint: P1, P4, P5, P7, P9 and P10. P7/P10 now have the separate
[input-basis successor](../20261007-public-input-basis/README.md); this batch's
frozen artifacts and validation results are unchanged.
