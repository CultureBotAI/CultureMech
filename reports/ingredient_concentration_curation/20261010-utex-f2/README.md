# UTEX F/2 Ingredient And Stock Review

## Applied Locally, Open Issues

The five exact tracked records in [the plan](plan.json) are applied locally.
The [source ledger](source-review.json) covers 105 structured concentration
claims using each formulation's own UTEX recipe and explicitly linked stock
recipes. Five formulation PDF page images were inspected; chemical identity
sources are separately scoped. [Per-record reports](records/) preserve the
remaining limitations, including the parent's three unverified literature
variants. Report coverage is not full scientific certification.

- 110 evidence entries, 17 references, 21 bibliography enrichments and five
  append-only curation events.
- 21 unsupported or nonnumeric concentration fields removed. The twenty
  solvent/makeup entries and one ammonium-magnesium-phosphate pinch remain
  present as ingredients with source-backed preparation notes.
- The ammonium variant's F/2 addition is corrected to an absolute 0.175 L
  aliquot in a 250 mL flask, not 1000 mL/L or a vessel-capacity denominator.
- Twelve chemical identities and names corrected: phosphate monohydrate,
  cyanocobalamin and thiamine hydrochloride in each of four expanded recipes.
- 66 ingredient/stock notes clarified, one unsupported filtration alternative
  removed, one unsupported dissolution assertion replaced by an addition
  action, and one parent child-link note corrected for aliquot/vessel context.
- No taxa-media associations added. Stable IDs, organism evidence and inline
  literature variants are preserved.

Nutrient and stock mass concentrations otherwise retain the explicitly
reported amounts. The 1% and 5% variants retain their 70 micromolar silicate;
the parent and 8 ppt formulation retain 106 micromolar. Stock composition is
not substituted for final-medium concentration or counted twice.

## Evidence Limits

The Trace Metals Solution mass column and molarity column remain discrepant.
Only its explicitly reported stock mass amounts support the retained g/L
values. No corrected molarity, molecular-weight conversion or receiving-medium
concentration is inferred from that inconsistent column.

The parent and 1% HTML/PDF seawater salinity versions differ. The 8 ppt PDF
explicitly carries a January 2020 revision date; no undated web publication
year is inferred from it. The 5% source lists vitamin doses but lacks a later
vitamin-addition step; no procedure is borrowed from another formulation.

Post-application inspection also identifies two retained child-side narrative
strings in `f_2_nh4_medium.yaml`: `parent_media.notes` and
`variant_modifications[0]` still say "175 mL flask". The corrected amount,
ingredient/stock notes, preparation step and parent-side link distinguish the
175 mL aliquot from the 250 mL vessel. The two legacy strings are not certified
by this batch and need an append-only follow-up correction using the same
explicit UTEX dispensing instruction; no concentration inference is required.

The packaged MIM index maps the old phosphate formula alias to a different,
non-hydrated term. The corrected full chemical name resolves to the verified
monohydrate identifier. The immutable index itself was not edited; the alias
issue remains an upstream limitation for other users of that spelling.

ChEBI pages were captured and hashed. The Sigma T1270 page was inspected with
the web tool after direct HTTP capture timed out. The ledger preserves an
explicitly labelled inspected excerpt, not a fabricated full HTTP capture.
These identity sources support chemical forms only, not ingredient amounts.

## Validation

[Preview](preview.json): twenty baseline/proposed schema commands, 116
adversarial/equivalence tests, Ruff, Black and diff checks pass. Captured tables,
source hashes and formulation-to-stock hyperlinks were revalidated.

[Baseline](baseline.json): all five exact paths were outside the previous
follow-up coverage and previously edited set. The report inventory included
ignored files. [Application](apply.json): exactly five normalized records
changed; guarded readback and repeat no-op pass.

[Cumulative reconciliation](reconcile-cumulative.json) verifies 5,371 edited
records, 37,203 added evidence entries and 1,743 quantity corrections. Follow-up
report coverage is 11,899 / 15,910, with 4,011 outside coverage. Ten post-edit
schema commands and 209 focused tests pass. Index regeneration has no semantic
changes; all five distinct merge groups retain the reviewed evidence.

[Live reference checks](references.json) do not pass. Four commands terminate
on a Sigma timeout and yield no per-snippet results. The NH4 command validates
the title and aliquot quote but rejects the pinch snippet because formula
subscripts were extracted with spaces. Manual source inspection is separate
from these automated failures. Do not infer 110 automatic snippet passes.

[Corpus checks](corpus.json): strict validation, stable-ID assignment, product
identity validation and the MIM-index check pass. Product validation retains
91 warnings and 96,008 no-adapter skips. Global merge verification fails with
1,247 name conflicts and 3,287 fingerprint issues. Freshness fails with 15,056
differences: 2,045 changed, 4,275 only in the tracked output and 8,736 only in a
fresh derivation. These are failing gates, not waived passes.

The [fast tier](fast.json) completes with **14,913 passed, sixteen skipped,
3,498 deselected and two dependency deprecation warnings**. This is not a
full-suite pass. The [terminal checkpoint](validation.json) rechecks source,
code, test, schema, audit-registry and all 15,910 normalized-record hashes,
and confirms a five-record guarded readback no-op. It explicitly retains the
failed production-reference and merge gates and the open record issues above.
This batch is uncommitted and not publication-ready; the all-record objective
remains active.

The separate [literature follow-up](../20261010-utex-f2-literature/README.md)
finds a sodium-selenite discrepancy in the 2021 study's Table S1 and DOI-backed
abstract support for the Tetraselmis nitrate treatment. These findings have not
yet changed the parent record and do not retroactively certify this batch's
unreviewed literature variants.
