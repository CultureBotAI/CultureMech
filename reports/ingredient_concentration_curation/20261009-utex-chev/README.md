# UTEX CHEV Ingredient Amount Review

## Applied Locally, Validation Recorded

The nine exact tracked CHEV records in [the plan](plan.json) are applied locally.
The [source ledger](source-review.json) pins the inspected official HTML pages
and their linked recipe PDFs. Each record has a [claim-level report](records/).
This is ingredient-amount curation, not certification of the complete recipes.

- 21 amount representations corrected to absolute input volumes in liters.
- Nine existing amounts retain their values and gain concentration evidence.
- Three fixed drop counts retain unresolved legacy encodings, with notes-only evidence.
- The Modified CHEV magnesium-carbonate discrepancy remains unresolved, with notes-only evidence.
- 34 evidence entries, nine bibliography enrichments, 32 clarified ingredient/stock notes,
  and nine append-only curation events. No new references or taxa-media associations.

Eight recipes are prepared tube-by-tube. The 15 mL figure is vessel capacity,
not a measured final volume. Soil, water, seawater and F/2 inputs are recorded as
absolute volumes; no concentration is derived from summed liquid inputs. The
separate bulk Modified 2X CHEV recipe explicitly specifies a 1 L total and keeps
its supported 800 mL/L water and 200 mL/L F/2 additions.

Seven magnesium-carbonate molarities are directly reported by the source, not
recalculated from mass or inferred chemical form. Modified CHEV prints 1 mg/12 mL
alongside 0.5 mM; both HTML and PDF contain this discrepancy. Its retained
molarity remains unverified. Drop counts are not converted using an assumed drop size.

IDs, mappings, preparation, organism claims, parent/child links and referenced
F/2 composition are preserved, not newly certified. Existing relationship notes
about a 12 mL liquid fill do not establish a final-volume basis. The nine source
formulations are not being merged with each other.

## Validation

[Preview](preview.json): all 36 baseline/proposed schema commands, 191 focused
tests, Ruff, Black and diff checks pass. The first exploratory test run had four
fixture errors (three wording expectations and one unchanged forged identity);
the fixtures were corrected before the recorded passing preview. No recipe
writes occurred during the preview.

[Application](apply.json): exactly nine normalized records changed; guarded
readback and repeat no-op pass. The [baseline](baseline.json) confirms all nine
were outside previous follow-up report coverage. The search included ignored files.

[Live references](references.json): all 34 snippets pass; nine title checks fail
because the validator expects the website title with the publisher suffix
`| UTEX Culture Collection of Algae`. The stored titles match the recipe headings.
This is a failing reference gate, not an automated pass or a waived failure.

[Cumulative reconciliation](reconcile-cumulative.json) verifies 5,366 edited
records, 37,093 added evidence entries, 5,997 added reference entries, 5,605 history
events and 1,742 quantity corrections. Follow-up coverage is 11,894 of 15,910
records, leaving 4,016 outside coverage; report presence does not certify every
concentration. [Index comparisons](reconcile-indexes.json) find no semantic changes.

[Post-edit checks](post.json) pass all eighteen schema commands and 284 focused
tests. [Runtime merge retention](reconcile-retention.json) passes for all nine
records, preserving nine distinct cohort groups, claim evidence and valid links.

[Corpus checks](corpus.json): strict schema, canonical IDs and product validation
pass. Product validation has 91 warnings and 96,008 no-adapter skips. Global merge
verification still fails with 1,247 name conflicts and 3,287 fingerprint issues.
Freshness still fails: 6,320 tracked outputs versus 10,781 fresh outputs, with
2,045 changed, 4,275 only tracked, 8,736 only fresh, and none unchanged.
The temporary fresh derivation was not written over tracked merged YAML.

The [fresh fast test tier](fast.json) passes **14,796 tests**, with sixteen
skipped, 3,498 deselected and two dependency deprecation warnings. This is not
a full-suite pass. The [terminal checkpoint](validation.json) verifies the
tested code, source plan, logs and all 15,910 normalized-record hashes, and
retains the failing reference and global merge gates explicitly. The guarded
nine-record readback remains a no-op.
The all-record goal remains active; this work is uncommitted and not publication-ready.
