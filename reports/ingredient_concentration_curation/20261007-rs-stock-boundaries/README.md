# RS stock-boundary follow-up

This is a two-record source-backed repair within the unfinished all-record goal.
The frozen [plan](plan.json) accounts for all 100 original concentration claims
and all resulting ingredient/stock claims. The repair is applied locally;
guarded readback, no-op rerun and independent audits pass. All validation jobs
are terminal, with unavailable validators and failed global merge gates recorded
below. No all-green or publication claim is made.

## Sources and decisions

- [P4](https://mediadive.dsmz.de/medium/P4): preserve nine direct solute rates;
  restore 23 individual stock stages and their separately stated working doses.
  The 22 mass-stock strengths reproduce their prior final contributions exactly.
  TiCl3's old quantity is a diluted-stock addition, not a solute concentration.
  Its commercial percent basis remains unknown. Restore water as unquantified
  stock solvent and final makeup, never as an assumed 1 L water addition.
- [P5](https://mediadive.dsmz.de/medium/P5): restore 37 nested stocks containing
  54 relocated solutes. Represent single-stock H2O/NNM carriers explicitly,
  without guessing their amounts or inventing a commercial MEM solvent.
  Retain the glycerol calculation using the source's explicit density.
  Replace five rounded per-liter mix additions with the source's exact batch
  volumes; distinguish 50 ml mix preparation from final 150 ml assembly.
  Withdraw six subtraction-derived NNM makeup amounts. The ingredient table
  and Mix 5 instructions conflict for D-Mannose/L-mannose and D-Xylose/Xylan;
  withdraw both asserted mix concentrations, retain the table identities and
  mappings with conflict flags, and do not choose an alternative.

Both pages are user-contributed, explicitly not curated/tested by MediaDive;
neither supplies a valid journal reference. Evidence supports the stated dataset
formulation, not experimental performance or a current manufacturer formulation.
The bibliography records actual page authors, title, year, discovery mode,
source type, access date and modification date. No DOI was invented.

The complete source tables, preparation steps, volume controls, dataset metadata
and qualifications are pinned to the [source inventory](../20261007-public-medium-source-pages.json).
HTML captures and inspected PNG preparation diagrams are hash-guarded. Numeric
evidence comes from page text, not diagram OCR. The original source handoff is
retained as historical evidence; it did not identify the additional mannose
conflict now preserved here.

## Applied accounting

The independent [audit](audit.py) verifies 155 evidence entries, two references
and two appended events. It separately counts:

- 77 ingredient relocations, including one TiCl3 dose moved to its stock.
- 76 concentration-stage rebases, not corrections of wrong numerical values.
- 60 new stock descriptors, with 59 new dose slots and one relocated dose.
- Five existing mix-dose basis corrections, eight unsupported quantity removals.
- 59 unquantified carrier/water nodes and two explicitly retained identity conflicts.

The audit independently recalculates source stock strengths and dilutions,
checks every field's attached quotations, and reconstructs the entire original
record. IDs, names, mappings, preparation, physical state, pH, salinity, prior
references/history and unrelated metadata must be unchanged. Fingerprint changes
must be limited to the explicitly added water labels; ingredient-set matching
still does not establish exact formulation identity.

## Validation and limitations

The initial offline guard run passed 45 tests before application; the expanded
shared-guard baseline passed 116 tests with three post-apply integration checks
deselected. The post-apply focused suite passes **876 tests**, with no errors,
failures or skips, including the prior RS repair tests. Baseline and post-apply
strict scans passed all 15,910 normalized records with zero errors; both targets'
schema checks and the canonical-ID check passed. All four baseline and 22
post-apply jobs are terminal in [validation.json](validation.json). Independent
[source-text readback](snippet-readback.json) verifies all 155 evidence snippets
and 558 claim excerpts (105 distinct excerpts across the two pages), separately
from the mutator's parser and arithmetic audit.

The independent audit rejects deliberate changes to stock strengths, doses,
water amounts, TiCl3 percentage assertions, chemical IDs, carrier references,
mix-volume units, conflict quantities, invented MEM solvent, duplicate solutes
and historical events, even when the proposal's claimed new values are changed
to match. Source drift, exact-path identity, symlinks, plan tampering, concurrent
edits and duplicate application are also tested. The historic fingerprint-impact
snapshot was not rewritten: its test accepts P5 only through this hash-linked,
independently inverted successor and its explicit water-only membership change.

The [actual-group retention check](merge-retention.json) passes both singleton
groups, including complete nested stocks, ingredient evidence, root evidence,
bibliography, preparation, notes and curation history. This does not repair
other groups' known evidence loss or establish formulation equivalence.

Black, Ruff and `git diff --check` pass. These checks use isolated Python 3.11,
not the maintained Python 3.13 runtime or CI; the full repository suite was not
run. Product validation fails because `oaklib` is unavailable; both automated
reference checks fail because `linkml-reference-validator` is missing. Manual
source inspection and independent text readback are not described as passes
of those unavailable validators.

Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. [Freshness](merge-freshness.json) also fails: 6,320 tracked and 6,492
fresh records, 3,719 only tracked, 3,891 only fresh, 1,645 changed and 956
unchanged. These counts match the preceding batch's snapshot. Regeneration ran
in a temporary directory; no generated merge was published or hand-patched.

Remaining scientific gaps include the TiCl3 percentage basis, P5's two carbon
identity conflicts, unspecified makeup-fluid amounts and secondary ontology
groundings. Unknown quantities are intentionally absent, not zero. No complete
final-medium concentration expansion or growth association is asserted.
No generated merge, PR, commit, or publication is claimed by this report.
