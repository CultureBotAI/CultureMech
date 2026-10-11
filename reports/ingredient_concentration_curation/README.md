# Ingredient Concentration Curation Status

**The all-record objective is not finished.** These are evidence-backed local
curation batches, not a claim that the corpus audit's findings have all been
resolved. The historical full-corpus audit remains unchanged.

**Publication update, 2026-10-11:** the curation packet is committed and pushed
in [draft PR 577](https://github.com/CultureBotAI/CultureMech/pull/577).
The [publication review](20261011-publication-review/README.md) records
reproducibility fixes and remaining release holds. The PR is not merged and its
branch is retained. Statements below about denied or unattempted publication
describe the historical batch checkpoints, not this publication update.

The [initial structural audit](../ingredient_concentration_review/20261005T175229Z/summary.md)
produced one report for each of 15,910 normalized and 6,320 merged records at its
pinned checkout. The follow-up coverage below measures subsequent curation
reports, not whether an initial audit report exists or every quantity is verified.

Worktree baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
Branch: `codex/curate-ingredient-evidence`. Local status checked 2026-10-10.

## Current Volvocacean/BG-11 Follow-Up

The [three-record successor](20261010-utex-volvocacean-bg11/README.md) is applied
locally. It adds eight source-URL/snippet evidence entries and three canonical
reports covering fifteen claim rows, removes two unsupported prepared-base
doses, and records three optional agar formulations. Four structured quantities
retain their values and units. No taxa-media associations are added.

Six post-edit schema/strict commands and 112 focused tests pass. All three
fresh-network reference commands pass, with eleven valid title/excerpt checks;
the initial sandbox DNS failures are retained separately. Three rendered pages
preserve the quantities and variants. Two eligible singleton merges pass, while
Volvocacean has the same pre-existing ingredient-fingerprint exclusion. Fourteen
regenerated indexes are semantically unchanged and are not rewritten.

The fresh cumulative audit verifies **5,439 edited records, 38,329 added evidence
entries and 1,844 quantity corrections**. Canonical follow-up coverage is
**11,967 / 15,910**, with **3,943 outside this follow-up coverage**. These counts
do not imply every concentration is scientifically verified.

Corpus strict schema, IDs and product labels pass; merge verification and
freshness fail with 15,056 derivation differences. The
[terminal checkpoint](20261010-utex-volvocacean-bg11/applied-checkpoint.json)
pins the final state. Missing BG-11 thiosulfate doses and its source naming
discrepancy remain explicit. The full suite was not rerun, and no Git/GitHub
publication operation was attempted.

## Previous Eighteen-Record Checkpoint

The totals and checks in this section describe the preceding checkpoint, not
the current three-record successor above.

The [eighteen-record follow-up](20261010-next-utex-applied/README.md) is applied
locally: seven soil/seawater recipes, five organic media and six prepared blends.
It adds **69 evidence entries**, qualifies twelve dose bases, removes fourteen
unsupported quantity slots without inventing replacements, and records nine
optional formulations separately. Eighteen canonical reports cover 67 claim rows.
The nested-stock KGX fix is installed and passes an installed-wheel smoke check.

The cumulative audit verifies **5,436 edited records, 38,321 added evidence entries
and 1,844 quantity corrections**. Canonical follow-up reports cover **11,964 /
15,910**, leaving **3,946 outside this follow-up coverage**. No taxa-media
associations are added. These totals do not certify every concentration or
complete the all-record scientific objective.

All 36 actual schema/strict commands, 369 pre-apply tests and 357 post-edit tests
pass. Independent source readback, eighteen rendered pages, fourteen eligible
singleton merges and three targeted generated-index updates pass. Four prepared
blends have the same unmergeable composition boundary before and after curation.
Installed reference validation has fourteen passing records and four title-only
failures caused by HTML-encoded apostrophes; all 69 snippets pass. The broader
strict UTEX parser remains isolated. See the [local issues](20261010-next-utex-applied/ISSUES.md)
and [final checkpoint](20261010-next-utex-applied/applied-checkpoint.json) for
gate results and limits.

The terminal corpus check passes strict, ID, product-label and MIM-index gates.
Merge verification and freshness still fail, with 15,056 derivation differences.
The final checkpoint pins all 15,910 record hashes, the eighteen canonical
reports, generated indexes, source checks, installed wheel and current code.

The preceding full suite finished with 19,215 passed and nineteen skipped, but
failed its runtime gate for four tests. It predates the latest packet and is not
a full-suite pass for the current code. Publication access remains blocked; no
commit, push, PR, merge or branch deletion is claimed.

## Historical J/DAS And Preview Chronology

The status statements and totals below describe earlier checkpoints, including
then-running tests and then-unapplied proposals. The current state is above.

The [verified preview checkpoint](20261010-utex-receiving-preview-checkpoint.json)
pins the earlier nine-report preview state before the J/DAS application below.

The [J/DAS batch](20261010-utex-j-das/README.md) is now applied locally: two records,
fifty added evidence entries, seven unsupported water/carrier fractions removed,
and four DAS supplement doses qualified by their starting-seawater basis. The
final-volume conflict remains unresolved. Application/readback/no-op, four actual
schema/strict checks and 245 post-edit tests pass.

The cumulative audit verifies **5,418 edited records, 38,252 added evidence entries
and 1,844 quantity corrections**. Follow-up reports cover **11,946 / 15,910** exact
normalized paths, leaving **3,964 outside coverage**. Report presence is not full
scientific verification; no taxa-media associations are added by this batch.

A separate [seven-record soil/seawater review](20261010-utex-soil-seawater-preview/README.md)
documents 29 existing claims and proposes corrections to fixed teaspoon doses,
optional carbonate, carrier-volume bases and source-specific preparation details.
These seven soil/seawater previews are **not applied** and do not change the
canonical coverage or edit totals. The historical J/DAS preview reports remain
excluded; their applied successor reports are counted once.

The review also reproduces [volume-basis export/display omissions](20261010-volume-basis-consumers/README.md).
The isolated v3 fix passes eighteen new tests and 61 existing regression tests,
with one unavailable Koza integration module skipped. An independent rendered-record
check verifies 94 quantity cells and fifteen volume-basis cells across seventeen
records. V2's incomplete 62-cell expectation is explicitly superseded. The patch
was applied locally after sealing the earlier validation run. Installed-code and
wheel checks pass. J's live reference check passes; DAS aborts on a supplier timeout.
Generated-web coverage passes for all 15,910 records. Corpus strict, ID, product
and MIM-index gates pass; merge verification and freshness fail with 15,056
derivation differences. Full tests are still running. The isolated soil/seawater
guard passes 106 tests. No
complete scientific review or publication readiness is claimed. Totals in the
older batch sections below are historical checkpoints.

[Source preparation](20261010-utex-source-preparation/README.md) captured all 64
remaining UTEX recipe pages outside the seven soil/seawater proposals. These
records contain 818 existing claim rows. Source collection alone adds no reviewed
records, edits or canonical coverage.

A [five-record organic-medium preview](20261010-utex-organic-five-preview/README.md)
subsequently checks 22 existing claims and four optional agar formulations.
Twenty schema/strict commands pass and 82 corrupted variants are rejected; the
isolated guard passes 78 tests and a real-schema dry run. Rendering preserves
seventeen quantities, two volume bases and four optional variants. The five
records remain unapplied and excluded from canonical coverage.
Its v2 proposal removes preview-only wording from prospective applied history,
without changing scientific content; all checks are repeated for the new hashes.

A [six-record prepared-blend preview](20261010-utex-six-blends-preview/README.md)
checks twelve unchanged input doses and proposes eight evidence entries. All
24 schema/strict commands, 61 corruption checks and 92 guard tests pass. The
quarter-strength Erdschreiber table/prose ratio conflict remains explicit.
These six records are also unapplied. The three pending recipe batches total
eighteen records and 69 proposed evidence entries, with zero increment to the
applied totals above.

[Further adversarial export review](20261010-kgx-nested-stock-review/README.md)
reproduces omitted nested-stock edges, stock-ID collisions across volume bases
and nested formulations, and dropped stock-ingredient publications. The isolated
fix passes fourteen new tests, 71 existing tests and a read-only 15,910-record
graph check; one Koza module is skipped. It remains unapplied while the full
suite's applied inputs stay frozen.

The [local continuation checkpoint](20261010-local-continuation-checkpoint.json)
verifies all 15,910 normalized hashes and the frozen code inventory, separates
twelve then-unapplied recipe previews from the applied totals, and pins the tested
KGX patch and source captures. Its completion flag covers this accounting check,
not the still-running full suite or the all-record scientific objective.

The later [v2 accounting checkpoint](20261010-local-continuation-checkpoint-v2.json)
verifies the same unchanged corpus and frozen code, eighteen unapplied proposals
and five additional read-only conflict reviews. The [integration packet](20261010-next-utex-integration-preview/README.md)
checks all three audit-dispatch paths and fresh real-schema dry runs; its nine-file
code patch remains uninstalled until the full run is terminal and sealed.

The [revised integration packet](20261010-next-utex-integration-preview/v2/README.md)
supersedes that nine-file patch with eleven files, including a strict
[UTEX reference parser](20261010-utex-reference-parser-preview/README.md).
Five proposal snippets now preserve literal chemical formatting. All eighteen
live proposal commands pass: 69 snippet and 21 title checks. The parser passes
60 new and 544 existing tests; all 73 captured layouts parse. Current reports
still add zero canonical coverage. All eighteen rendered previews retain 44
quantity cells, twelve bases and nine variants in DOM checks. The packet remains
uninstalled. Captured-layout acceptance alone is not scientific review.

Broader parser review then found 32 snippet and ten title mismatches across
fourteen existing records, plus unsupported stock layouts and unassessed captures.
The [scoped v3 packet](20261010-next-utex-integration-preview/v3/README.md) therefore
excludes parser installation and retains the corrected eighteen proposals with
the separate KGX fix. [Local parser issues](20261010-utex-reference-parser-preview/ISSUES.md)
remain open; an isolated reference pass is not an installed-validator pass.
The [v3 accounting checkpoint](20261010-local-continuation-checkpoint-v3.json)
rechecks frozen inputs and preserves the applied totals separately from previews.

The [five-soilwater source review](20261010-utex-five-soilwater-conflicts-preview/README.md)
covers thirteen claims with ten passing baseline schema/strict checks. It
withholds mutations for soil input/final-volume ambiguity, optional carbonate
and source/supplier hydration conflicts in the two NH4 formulations. Conditional
arithmetic is diagnostic, not a replacement concentration. These five previews
add zero canonical coverage or evidence entries. At that checkpoint, forty-eight
of the 64 captured UTEX records had source preparation only.

A subsequent [three-record source review](20261010-utex-volvocacean-bg11-review-preview/README.md)
covers Volvocacean and both BG-11 salt variants: nine existing claims and five
additional optional-variant claims, with six passing baseline schema/strict
commands. It identifies missing preparation qualifications and unsupported
prepared-base fractions without making a mutation plan. These read-only previews
add no canonical coverage or edits; **45 of the 64 captured records remain at
source-preparation-only status**. The linked BG-11 page is context, not a fourth
completed record review.

The [v4 accounting checkpoint](20261010-local-continuation-checkpoint-v4.json)
verifies unchanged frozen code and all 15,910 corpus hashes after these additional
reviews. Applied totals and canonical coverage remain unchanged.

The two remaining `mediadive.medium` records were re-triaged on 2026-10-10:
[P1 HAHA](20261007-p1-primary-source-handoff.md) still has conflicting stock
formulations, and [P9 PDB-SNG](20261007-p8-p9-primary-source-handoff.md) still has
a medium-identity conflict. Both current file hashes match those handoffs.
Fresh MediaDive page access failed through the web tool; no new source validation,
ingredient edit or completed follow-up report is claimed for either record.

## Applied Seven-Stock UTEX Review

The [seven-stock batch](20261010-utex-seven-stocks/README.md) is applied locally.
It adds 57 evidence entries and two source-explicit component-stock strengths,
corrects seven supplied chemical identities, and separates the two DAS prepared
stocks from pure-ingredient composition. Numerical mass concentrations are retained;
source-volume, molarity, sterilization and ontology limitations remain explicit.
No taxa-media association is added.

The [cumulative audit](20261010-utex-seven-stocks/cumulative.json) verifies
**5,416 edited records, 38,202 added evidence entries and 1,844 quantity
corrections**. Canonical follow-up reports cover **11,944 / 15,910** normalized
records, leaving **3,966 outside coverage**. Report presence is not complete
scientific verification.

All 28 baseline/proposed and fourteen actual schema/strict commands pass, with
99 guard tests and 247 post-edit regression tests. Four indexes are regenerated;
all seven standalone stocks remain excluded from medium merging. Four live
reference commands pass; three abort on supplier timeouts. Corpus strict, ID,
product and MIM-index gates pass. Merge verification and freshness fail, with
15,056 derivation differences. The fast tier finished with 15,665 passed, sixteen
skipped and 3,498 deselected, but failed the 120-second runtime gate for one test
(155.1 seconds). The [terminal checkpoint](20261010-utex-seven-stocks/applied-checkpoint.json)
pins these results; it is not an all-gates pass. Publication readiness remains
incomplete. The three-stock totals below are historical.

## Applied Migrated UTEX Stock Review

The [three-stock batch](20261010-utex-migrated-stocks/README.md) is applied
locally. It adds thirteen evidence entries, enriches three bibliography entries
and corrects three context notes. All ten structured amounts and chemical
identities are retained; the manganese-form conflict remains unresolved.
No taxa-media association is added.

The [cumulative audit](20261010-utex-migrated-stocks/cumulative.json) verifies
**5,409 edited records, 38,145 added evidence entries and 1,844 quantity
corrections**. Canonical follow-up reports cover **11,937 / 15,910** normalized
records, leaving **3,973 outside coverage**. These are follow-up reports, not
certification that every concentration is verified; the initial structural audit
already produced a report for every record at its pinned checkout.

All twelve baseline/proposed and six actual schema/strict commands pass,
along with 43 guard tests and 190 post-edit regression tests. All thirteen new
snippets pass live reference checks, but three bibliography title checks fail.
Corpus strict, ID, product and MIM-index checks pass; merge verification and
freshness fail, with 15,056 derivation differences. The fast tier finishes with
**15,565 passed, sixteen skipped, 3,498 deselected and two dependency warnings**
in 43:57; this is not a full-suite pass. The
[terminal checkpoint](20261010-utex-migrated-stocks/applied-checkpoint.json)
pins the results and verifies the unchanged tested code and all 15,910
normalized-record hashes. The failed reference and merge gates still prevent an
all-gates pass. Publication readiness and the all-record goal remain incomplete.
The yeast and earlier totals below are historical checkpoints.

## Applied Yeast Mineral Review

The [four-record yeast mineral batch](20261010-yeast-mineral-ingredients/README.md)
is applied locally: 56 source-unit amount replacements, two new quantified
antifoam entries, two unquantified antifoam nodes, 218 evidence entries and fifty
references. Twenty-eight original amounts remain explicitly unresolved. Source
forms, preparation sequencing and ethanol variant descriptions are corrected
with scoped snippets; no taxa-media association is added.

The [original applied checkpoint](20261010-yeast-mineral-ingredients/applied-checkpoint.json)
records 386 passing regression tests, eight post-edit schema/strict passes,
three refreshed indexes and four successful runtime-retention checks. Its
cumulative audit verifies **5,406 edited records, 38,132 added evidence entries
and 1,844 quantity corrections**. Canonical follow-up reports cover
**11,934 / 15,910** records, leaving **3,976 outside coverage**. Coverage does not
mean every concentration is verified. Reference and merge/freshness gates fail;
the Hajjaj fast tier predates the new yeast code.

A separate [applied citation repair](20261010-yeast-chebi-urls/README.md) fixes
eighty live ChEBI URLs in the same four records, without changing concentrations,
identities, snippets or previous history. Its guard passes 42 tests and all
sixteen baseline/proposed and eight actual schema/strict checks pass. Broader
post-repair checks are recorded separately, not inferred from the original
checkpoint. The [three-stock UTEX draft](20261010-utex-migrated-stock-preview/README.md)
preserves the source captures and schema-valid proposals that led to the applied
successor above. The draft itself remains excluded from canonical coverage.

## Applied Hajjaj Ingredient Review

The [twenty-record Hajjaj-family batch](20261010-hajjaj-ingredients/README.md)
is applied locally. It restores 37 directly stated nutrient amounts in the
paper's mass units, corrects supplied chemical forms and removes unsupported
identity mappings. It adds 535 evidence entries and 150 references, with one
append-only curation event per record. No taxa-media associations are added.
The 206 retained molarities remain explicitly unresolved against primary
evidence; database assertions are not promoted to independently verified values.

All 80 baseline/proposed schema and strict commands, 254 adversarial tests,
lint and formatting pass. Application, readback and repeat no-op pass; exactly
twenty normalized paths changed. All 243 database rows are independently
rechecked against their own HTML and dated SQL sources. Twenty canonical
reports cover all 243 concentration claims. Index regeneration finds no semantic
changes in fourteen indexes, and all twenty runtime merge-retention checks pass.

Cumulative reconciliation verifies **5,402 edited records, 37,914 added evidence
entries and 1,788 structured quantity corrections**. Follow-up reports cover
**11,930 / 15,910** exact normalized paths, leaving **3,980 outside coverage**.
Coverage is not complete scientific verification. All forty post-edit schema
commands and 382 regression tests pass. The network-enabled reference rerun
passes 316 snippets and 130 titles, but fails 219 snippets and twenty titles;
manual source inspection is not an automatic reference pass. Corpus strict,
ID, product and MIM-index checks pass. Merge verification and freshness fail
with 1,247 name conflicts, 3,287 fingerprint issues and 15,056 derivation
differences. The [applied checkpoint](20261010-hajjaj-ingredients/applied-checkpoint.json)
pins these outcomes and the unchanged normalized-record hashes. The fresh fast
tier finishes with 15,409 passed, sixteen skipped, 3,498 deselected and two
dependency warnings in 34:30. The [terminal checkpoint](20261010-hajjaj-ingredients/validation.json)
pins the tested code and all 15,910 record hashes. This is not a full-suite,
all-gates or publication-ready pass. The Bristol/BBM and earlier totals below
are historical.

The [yeast mineral source preview](20261010-yeast-mineral-source-preview/README.md)
accounts for all 84 ingredient claims in four unchanged MediaDB records. Two
captured primary papers support 56 proposed source-unit replacements; 26
mineral amounts retain final-volume gaps and two molybdate claims retain a
printed-formula conflict. All eight baseline schema/strict checks pass. Missing
antifoam, supplied chemical forms, preparation and ethanol variant wording are
also documented. These are excluded previews, not applied edits or additional
canonical review coverage.
The second YAML preview passes eight proposed schema/strict checks and an
independent 84-claim semantic check with forty altered-preview rejections.
The application guard draft passes 68 tests, including drift, forged-plan,
rollback and no-op cases, plus lint and a real-schema dry run. Installation and
actual application remain pending; proposed additions are not included in the
applied totals above.

## Applied Bristol/BBM Review

The [five-record Bristol/BBM batch](20261010-utex-bristol-bbm/README.md) is applied
locally. It adds forty scoped evidence entries and removes eight unsupported
quantity fields without replacement numbers. It corrects stock/final wording,
the Bristol-NaCl preparation stage and the study-specific estradiol treatment
levels. The BBM manganese source conflict remains explicitly unresolved.

Preview validation passes twenty schema commands, 64 focused tests and lint.
Application, readback and repeat no-op pass. All ten post-edit schema commands
and 418 regression tests pass. Index regeneration finds no semantic changes,
and all five runtime merge-retention checks pass.

Cumulative reconciliation verifies **5,382 edited records, 37,379 added evidence
entries and 1,751 structured quantity corrections**. Follow-up reports cover
**11,910 / 15,910** exact paths, leaving **4,000 outside coverage**. Report presence
does not establish that every concentration is scientifically verified.

The initial reference commands abort on sandbox DNS without per-claim results.
The network-enabled rerun passes four records, 43 snippets and twelve titles;
one BBM methods snippet fails because the validator retrieves only the abstract.
Corpus strict, ID, product and MIM-index checks pass. Global merge verification
and freshness still fail with 1,247 name conflicts, 3,287 fingerprint issues and
15,056 derivation differences. The fresh fast tier finishes with **15,154 passed,
sixteen skipped, 3,498 deselected and two dependency warnings** in 32:01. This
is not a full-suite pass. The
[terminal checkpoint](20261010-utex-bristol-bbm/validation.json) verifies the
unchanged tested code and all 15,910 normalized-record hashes. All scheduled
validation runs are terminal; the failed reference and merge gates mean this
is still not publication-ready. The F/2 and earlier totals below are historical.

The [Hajjaj claim preview](20261010-hajjaj-source-preview/README.md) now covers 217
claims in eighteen source-linked records, with all 36 baseline schema/strict
checks passing. An ignored-inclusive boundary check adds two unlinked sibling
candidates and 26 claims to the next review queue. The candidate family is twenty
records / 243 claims, not twenty completed reviews at that historical checkpoint.
Those preview artifacts remain unchanged and excluded from canonical coverage;
the applied successor is documented above.

## Applied F/2 Evidence Follow-Up

The [two-record F/2 successor](20261010-utex-f2-followup/README.md) is applied
locally. It adds missing DOI/snippet support to literature variants, scopes the
selenite correction to the source's Table S1 value of 1 nM, and repairs the NH4
child's aliquot/flask descriptions and formula snippet. Canonical parent/stock
amounts and earlier curation history remain unchanged. Main-text access limits
and unresolved source conflicts remain explicit.

The preview passes eight schema commands, 32 focused tests and lint checks;
application, readback and repeat no-op pass. The two existing canonical reports
are extended rather than duplicated, with no coverage increment. Cumulative
reconciliation verifies **5,377 edited records, 37,339 added evidence entries
and 1,751 structured quantity corrections**, plus the separately counted
narrative selenite correction. Follow-up reports cover **11,905 / 15,910** exact
normalized paths, leaving **4,005 outside coverage**; report presence is not
complete scientific verification.

All four post-edit schema/strict checks and 354 focused tests pass. Index
regeneration finds no semantic changes, and both runtime merge-retention checks
pass. The fast tier finishes with **15,089 passed, sixteen skipped, 3,498
deselected and two dependency warnings**; this is not a full-suite pass. The NH4
reference check passes both snippets and its title; the F/2 parent command aborts
on a supplier timeout without per-claim results. Manual verification remains
separate from automatic validation.

Corpus strict, ID, product and MIM-index checks pass, with 91 product warnings
and 96,008 no-adapter skips. Global merge verification and freshness still fail
(1,247 name conflicts, 3,287 fingerprint issues and 15,056 derivation differences).
The [terminal checkpoint](20261010-utex-f2-followup/validation.json) pins actual
results and tested hashes. Nothing is committed, merged or publication-ready.
The all-record objective remains incomplete; the ES totals below are historical.

The historical [Bristol/Bold source preview](20261010-bristol-bbm-source-preview/README.md)
has 33 structured-quantity and four narrative-variant dispositions, plus separate
child preparation triage. It led to the applied five-record batch above; the
preview itself is not additional canonical follow-up coverage.

## Applied UTEX Enriched Seawater Review

The [six-record enriched-seawater batch](20261010-utex-es/README.md) is applied
locally. It relocates twenty stocks into the enrichment preparation, corrects
eight input-volume representations, removes 24 unsupported water quantities,
corrects eight vitamin identities and removes four unsupported glycerophosphate
identifier pairs. It adds 134 source-linked evidence entries while retaining
source conflicts and the exact 500/500 and 665/335 dilution recipes.

The final preview passes 24 baseline/proposed schema commands, 142 focused tests
and lint checks. Guarded application, readback and repeat no-op pass. Cumulative
reconciliation verifies **5,377 edited records, 37,337 added evidence entries
and 1,751 quantity corrections**. Follow-up reports cover **11,905 / 15,910**
exact normalized paths, leaving **4,005 outside coverage**. These reports do not
certify every concentration. Six new canonical reports cover 124 quantity claims.
All twelve post-edit schema/strict commands and 351 focused tests pass. Three
indexes are refreshed, and all six runtime merge-retention checks pass. The fast
tier finishes with **15,056 passed, sixteen skipped, 3,498 deselected and two
dependency warnings**; this is not a full-suite pass. Corpus strict, ID, product
and MIM-index checks pass, retaining 91 product warnings and 96,008 no-adapter
skips. Global merge verification and freshness still fail (1,247 name conflicts,
3,287 fingerprint issues and 15,056 derivation differences).

Live references pass for the two dilution records, but four expanded-recipe
commands abort on supplier timeouts without per-claim results. Manual source
inspection is not an automatic reference pass. The
[terminal checkpoint](20261010-utex-es/validation.json) pins the tested state and
records these remaining failures. Nothing is committed, merged or publication-ready,
and the all-record objective is not complete. The F/2 totals below describe the
preceding terminal checkpoint.

## Applied UTEX F/2 Ingredient Review

The [five-record F/2 review](20261010-utex-f2/README.md) is applied locally.
It adds 110 evidence entries, removes 21 unsupported or nonnumeric quantity
fields while retaining evidenced preparation notes, corrects twelve chemical
identities and records the NH4 variant's F/2 input as an absolute 0.175 L
aliquot. Nutrient doses remain formulation-specific; the trace-metal source
molarity discrepancy remains unresolved. Three inline literature variants are
outside this applied batch.

All twenty baseline/proposed schema commands and 116 adversarial tests pass,
as do guarded application, readback and repeat no-op. Cumulative reconciliation
verifies **5,371 edited records, 37,203 added evidence entries and 1,743 quantity
corrections**. Follow-up report coverage is **11,899 / 15,910**, leaving **4,011
outside coverage**; report presence is not complete scientific verification.
Ten post-edit schema commands and 209 focused tests pass. Index and five-record
merge-retention checks pass. Live reference validation fails: four records abort
on a Sigma timeout, and the NH4 record has a chemical-formula whitespace mismatch
in one snippet. Two child-side NH4 flask descriptions also remain to correct.
Corpus strict, ID, product and MIM-index checks pass; product validation retains
91 warnings and 96,008 no-adapter skips. Global merge verification fails with
1,247 name conflicts and 3,287 fingerprint issues; freshness fails with 15,056
differences. The fast tier passes **14,913 tests**, with sixteen skipped, 3,498
deselected and two dependency warnings. This is not a full-suite pass.
The [terminal checkpoint](20261010-utex-f2/validation.json) verifies unchanged
tested code and recipe hashes while retaining these failing gates and open
record issues. Nothing is committed, merged or publication-ready. The CHEV
totals below are the preceding terminal checkpoint.

The earlier [enriched-seawater source review](20261010-utex-es-source-review/README.md)
has six per-record previews covering 124 claims and an identity preview for
twelve ingredient nodes. Those historical previews led to the applied batch
above; they are not additional canonical review coverage. The
[F/2 literature preview](20261010-utex-f2-literature/source-review-preview.json)
records four historical claim-level dispositions, including the Table S1 selenite
discrepancy. That preview itself was read-only; the guarded F/2 successor above
subsequently applied the reviewed evidence and wording changes.

## Applied UTEX CHEV Amount Review

The [nine-record CHEV review](20261009-utex-chev/README.md) is applied locally.
It corrects 21 amount representations, adds 34 source-linked evidence entries,
enriches nine bibliography entries and appends nine history events. The corrected
litre amounts are per-tube input volumes, not final concentrations. Three fixed
drop-count encodings and one magnesium-carbonate discrepancy remain unresolved;
their added evidence supports notes only. No taxa-media associations are added.

All 36 baseline/proposed schema commands, 191 focused tests and lint checks pass.
Guarded application, readback and repeat no-op pass. Nine per-record reports
cover all 34 ingredient/stock amount claims. Cumulative reconciliation verifies
**5,366 edited records and 37,093 added evidence entries**. Follow-up coverage is
**11,894 / 15,910**, leaving **4,016 outside coverage**. Report coverage is not
complete concentration verification. Index regeneration finds no semantic changes.
All 34 new snippets pass live reference validation; nine title checks fail because
the website titles include UTEX's publisher suffix. All eighteen post-edit schema
commands and 284 focused tests pass. Nine runtime merge-retention checks pass,
keeping all nine formulations distinct. Corpus strict, ID and product checks pass,
with 91 product warnings and 96,008 no-adapter skips. Global merge verification
still fails (1,247 name conflicts and 3,287 fingerprint issues), as does freshness
(15,056 differences). The fresh fast tier passes **14,796 tests**, with sixteen
skipped, 3,498 deselected and two dependency deprecation warnings; this is not
a full-suite pass. The [terminal checkpoint](20261009-utex-chev/validation.json)
verifies unchanged tested code and recipe hashes and retains the failing gates.
Nothing is committed or publication-ready. Earlier sections retain historical
checkpoints.

The historical [F/2 source follow-up](20261009-utex-f2-source-followup/README.md)
captured the parent, four variants and four linked stocks. Its 105 concentration
claims were subsequently considered in the applied F/2 batch above. The source
inventory itself remains a read-only artifact, not additional review coverage.

## Applied Geobacter Primary-Source Review

The [56-record Geobacter review](20261009-geobacter-primary/README.md) is applied
locally. It corrects 238 quantity fields, 56 phosphate-hydrate identities,
eighteen acetate-salt identities and 56 sterilization instructions. It appends
350 evidence entries, 74 references and 56 history events. Four acetate endpoint
amounts remain unsupported and unchanged; their added evidence supports only
chemical identity. The reviewed quantities and chemical forms have separate
claim dispositions, not blanket formulation approval.

All 224 baseline/proposed schema commands, 804 adversarial/equivalence tests
and lint checks pass. Guarded application, readback and repeat no-op pass,
with exactly 56 normalized records changed. All 1,628 ingredient rows have
per-record dispositions; two existing canonical reports were extended without
duplicates. Cumulative reconciliation verifies **5,357 edited records and 37,059
added evidence entries**. Follow-up coverage is **11,885 / 15,910**, leaving
**4,025 outside coverage**. Report presence does not certify every concentration.
All 56 runtime merge-retention checks pass; indexes have no semantic changes.
Production reference validation fails 350 snippets and twenty titles, while
sixty historical database snippets and 58 titles pass. The failures include
unavailable DOI text, a PMC browser-check page and two SQL-export titles; manual
scan verification remains separate. All 112 post-edit schema commands and 961
focused tests pass. Corpus strict, ID and product checks pass, with 91 product
warnings and 96,008 no-adapter skips. Global merge verification still fails
(1,247 name conflicts and 3,287 fingerprint issues), as does freshness (15,056
differences). The fresh fast tier passes **14,604 tests**, with sixteen skipped,
3,498 deselected and two dependency deprecation warnings; this is not a full-suite
pass. The [terminal checkpoint](20261009-geobacter-primary/validation.json)
verifies unchanged tested code and recipe hashes and retains the failing gates.
Nothing is committed or publication-ready. Earlier sections retain historical
checkpoint totals.

The [Vogel source supplement](20261009-vogel-source-followup/README.md) preserves
the earlier source ledger and adds the inspected 2006 FGSC protocol. It is
read-only, with no recipe edits or coverage increment.

## Applied Modified M63 Primary-Source Review

The [twelve-record M63 review](20261009-m63-primary/README.md) is applied locally.
It adds **84 ingredient evidence entries**, 24 bibliography entries and twelve
history events, and corrects **36 chemical forms**: twelve phosphate identities
and 24 sulfate hydrate identities. All numeric amounts remain unchanged. The
2010 paper directly supports the carbon/salt conditions; its explicitly cited
1982 M63 definition supports the base inputs, with that inference stated in the
evidence. No taxa-media associations are added.

Guarded application, readback and repeat no-op pass. The final preview passes
395 tests and lint checks after two unapplied revisions and a corrected test
fixture. The independent cumulative audit verifies **5,303 edited records and
36,709 added evidence entries**. Exact follow-up coverage is **11,831 / 15,910**,
leaving **4,079 outside this follow-up**; report presence is not complete
scientific verification. The 24 post-edit schema commands and 552 focused tests
pass, as do merge-retention checks for the twelve changed inputs. Corpus strict,
ID and product checks pass; global merge verification and freshness still fail.
The reference validator fails 84 scan/full-text snippets and twelve PMC titles;
manual source inspection is recorded separately, not as an automated pass. The
fresh fast tier passes **13,799 tests**, with sixteen skipped and 3,498 deselected;
this is not a full-suite pass. The [terminal checkpoint](20261009-m63-primary/validation.json)
verifies unchanged tested code and recipe hashes. No indexes required content changes.
The work remains uncommitted and the all-record goal remains active. Older
sections below describe preceding checkpoints, not current cumulative totals.

The [Geobacter source follow-up](20261009-geobacter-source-followup/README.md)
traces the 1993 recipe through its 1988, 1984 and 1979 sources. Its 56-record
inventory, conditional omissions and twelve chemical-form candidates remain
read-only, with no concentration edits or review-coverage increment.

The subsequent Geobacter draft's parent-child identity conflict was resolved
in the applied follow-up above, without certifying its four endpoint quantities.
The earlier interrupted previews remain preserved as historical receipts.

## MediaDB Reference Validation Follow-Up

The [literal MediaDB table adapter](20261009-mediadb-reference-adapter/README.md)
now passes all 156 previously failing snippets and six page titles on the six
repaired records. The six SQL-export title failures remain, so the full reference
gate still fails. Source checks verify 469 pinned captures and 7,758 table rows;
686 focused regression tests pass after fixing an adversarially reproduced
hidden-container defect. The fresh fast tier finishes with **13,403 passed and
sixteen skipped**. The command exits 0; a subsequent recorder output-pipe error
is preserved and independently reconciled in the
[final checkpoint](20261009-mediadb-reference-adapter/validation.json).
No recipe values or cumulative curation/coverage counts change.
Database literal matching does not approve pending primary-source formulations.

## Applied Kaminskyj Stock Correction

The [primary-source Kaminskyj correction](20261009-kaminskyj-stocks/README.md)
is applied locally. It restores stock/final-medium boundaries, seven hydrate
forms, source pH/preparation, and two optional variants. Unsupported thiamine
molarity is withdrawn rather than replaced by an assumed percentage basis.
It adds twenty source-linked evidence entries, two references and one history
event; no taxa-media associations are added.

Current cumulative accounting verifies **5,291 edited records and 36,625 added
evidence entries**. Follow-up reports cover **11,819 exact paths**, leaving
**4,091 outside this follow-up**. This is not full concentration verification.
The 49 focused and 113 post-edit tests pass, as do source-capture, record schema,
term and runtime merge-retention checks. Four indexes are refreshed. The live
reference validator still fails sixteen raw-HTML table excerpts. Corpus strict,
ID and product checks pass with existing warnings; global merge verification
and freshness still fail. The terminal fast tier passes **13,208 tests**, with
sixteen skipped; source inventory and tested code hashes remain unchanged. The
[final checkpoint](20261009-kaminskyj-stocks/validation.json) preserves all gate
outcomes separately. Nothing is committed or publication-ready. The remaining
full-corpus objective stays active.

Record 308's historical evidence-only draft is superseded by this primary-source
correction; the other 452 draft candidates and ten AMS1 holds are still pending.
The older sections below describe historical checkpoints, not current totals.

## Applied MediaDB Exceptions

The [six-record MediaDB repair](20261009-mediadb-exceptions/README.md) restores
six source-reported fatty-acid entries, removes twelve unrelated LB ingredient
rows and withdraws nineteen VARIABLE defaults where the source amount is unknown.
It adds 156 source-linked evidence entries, twelve references and six history
events. The nineteen unknown amounts are not replaced with guessed numbers.
All 156 snippets match the captured official tables, and 243 post-edit tests
pass with one skipped. The network-enabled production reference validator still
fails on raw HTML table excerpts and export metadata; those failures are recorded
separately from the successful source-table checks. The terminal fast tier has
13,158 passed and sixteen skipped; corpus strict/ID/product checks pass, while
global merge verification and freshness still fail. The batch's
[final checkpoint](20261009-mediadb-exceptions/validation.json) preserves those
distinct outcomes. No new taxa-media associations are added.

This earlier cumulative accounting verified **5,290 edited records and 36,605 added
evidence entries**. Follow-up reports cover **11,818 exact paths**, leaving
**4,092 outside this follow-up**. Coverage is not complete scientific verification.
Three generated indexes are refreshed and all six formulations retain their
claims through runtime merging. The full all-record objective remains active.
Older sections below describe earlier checkpoints, not current cumulative totals.

The subsequent [MediaDB evidence draft](20261009-mediadb-evidence-draft/README.md)
proposes 7,406 entries for 453 further records. It is **not applied** and adds
nothing to the totals above. A read-only comparison checked 7,606 database rows
across 463 records; ten AMS1 records are held for a primary-source formulation
conflict. Proposal checks reject 2,718 semantic forgeries, but neither those
checks nor live/export agreement certify original-article quantities.
Further primary-source inspection found a stock/final-medium conflict in the
Kaminskyj candidate, so that draft is not approved for batch application. Its
source-linked hold and unresolved Kazan/Vogel priorities remain explicit.

## Applied Medium323 Review

The [four-record source-specific review](20261009-medium323/README.md) is now
applied locally, adding 65 evidence entries, seven references and four history
events. It corrects fifteen quantity fields, removes fourteen unsupported
quantity fields and adds five quantity fields. Guarded application, readback and
repeat no-op pass. All twelve actual-record schema/strict/reference commands
pass, including 82 reference checks; broader regressions and reconciliation are
now terminal: 312 post-edit tests, 204 reconciliation tests and 13,064 fast tests
pass. Cumulative accounting verifies 5,284 edited records and 36,449 added evidence
entries. Follow-up coverage remains 11,812, with 4,098 outside it. Global merge
verification and freshness still fail. No taxa-media associations are added.

Full-page KOMODO evidence supports retaining its existing L-cysteine hydrate
links, superseding the older draft's proposed withdrawal. Source-specific
formulations stay separate, and uncertain physical state, conditional agar and
upstream sodium-resazurin mapping issues remain explicit. The following sections
describe earlier checkpoints, not current application state.

## Resazurin Stock Identity Follow-Up

The [three-record identity follow-up](20261009-resazurin-stock-identity/README.md)
is applied locally. Unsupported exact primary CHEBI:8806 mappings were withdrawn
from sodium-resazurin stocks, with all doses and other quantities unchanged.
Three existing PDF evidence explanations were extended in place and three
history events appended; no new evidence entries, references or taxa-media
associations were added. Guarded application, readback and repeat no-op pass.
The packaged MIM resolver still returns the same sodium-free chemical identity
for the exact stock label. That upstream publication-time conflict remains open;
neither the immutable index nor the resolver was changed. Terminal post-edit
and corpus receipts, not this scoped application, determine gate outcomes.
All nine post-edit schema/strict/reference commands and 943 focused regression
tests pass. The cumulative audit verifies 5,281 edited records, 36,384 added
evidence entries and 5,517 history events. Exact follow-up coverage remains
11,812, with 4,098 outside it.

The [final local checkpoint](20261009-resazurin-stock-identity/validation.json)
records a passing fast tier: 13,063 passed, sixteen skipped, 3,423 deselected
and two dependency warnings. This does not replace the earlier failed full-suite
run. Corpus strict/ID/product gates pass with the documented product warnings
and adapter limits. Global merge verification still fails with 1,247 name
conflicts and 3,287 fingerprint issues; freshness reports 15,056 differing
records. The work is local and uncommitted, not publication-ready.

The [four-record medium323 draft](20261009-medium323-draft-v2/README.md) now contains
source-linked proposed YAML and diffs. Independent checks account for all 62
old quantity fields, pass 79 production reference checks and reject 18 adversarial
draft mutations. An unrelated note-whitespace change found in the first draft
is fixed in this successor. The drafts remain
unapplied pending the full inverse audit, mutation-tested guarded write path and
explicit source-conflict dispositions; they add nothing to applied totals.

## Solution Evidence Schema Follow-Up

The [solution-evidence schema follow-up](20261009-solution-evidence-schema/README.md)
implements optional root formulation evidence for standalone stock recipes.
Generated Python/JSON Schema/docs and the skill contract are updated. All 830
final targeted tests and closed-schema checks on all 15,910 normalized records pass;
ID/product checks pass with existing warnings and unsupported-adapter limits.
The actual pending S599 stock dose also passes eleven in-memory source checks
without altering its recipe. The full regression run finished with 16,405 passed,
25 failed and nineteen skipped. Documentation and historical-test repairs cover
24 failures in the passing targeted rerun; the original failed run remains
preserved, not certified green. The remaining grounding failure is localized to
three sodium-resazurin stock inputs; their quantities are unchanged. The local
identity withdrawal is now applied in the follow-up above, while the MIM
publication-time mapping conflict remains unresolved. Generated documentation
now has 341 type-separated pages without the former filename collisions.

This step changes **zero ingredient records** and adds **zero in-record evidence
entries**. The applied curation totals below remain unchanged; the four medium323
recipes still require guarded curation. Their source projections now account for
all 62 old quantity fields without asserting unknown amounts or conflating
KOMODO with DSMZ. No global merge/freshness failure or
all-record completion requirement is waived.

## Latest Applied Variant Follow-Up

The [sixteen-record Halobacteria variant review](20261009-halobacteria-variants/README.md)
is applied locally. Thirteen records receive ingredient/preparation review;
three parents receive reciprocal relationship changes with their ingredient
arrays unchanged. Guarded application, independent readback and repeat no-op
account for **575 evidence-linked claims and 127 reviewed old quantity fields**,
adding **335 evidence entries, 45 references and sixteen history events**.
No taxa-media associations are added. Only the intended sixteen normalized
records changed; earlier IDs, mappings, roles and history are preserved.

The [cumulative audit](20261009-halobacteria-variants/cumulative-audit.json)
verifies **5,281 edited records and 36,384 added evidence entries**. All 725
focused tests pass. Actual-written schema/strict checks and 417 supported
reference checks pass; 25 provider-export entries are checked separately and
two existing bibliography entries remain explicitly unverified. Presentation
checks pass, six indexes are refreshed for seven affected records, and runtime
merging retains all fifteen medium targets while excluding the standalone
solution. Corpus strict validation covers all 15,910 records successfully.

Report reconciliation finds **11,812 exact follow-up paths**, leaving **4,098**
outside these reports, with 65 previews excluded. Report presence is not full
concentration verification. All **699 final QA tests** pass, along with corpus
ID/product and variant-link checks. The terminal fast test tier passes
**12,702 tests**, with sixteen skipped, 3,374 deselected and two dependency
warnings. The [final applied checkpoint](20261009-halobacteria-variants/validation.json)
pins all terminal cohort checks and the unchanged full-corpus hash. A temporary
schema prototype demonstrates a possible solution-level evidence container for
the next batch; no production schema change is claimed.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues; freshness also fails with the same counts as the preceding
checkpoint. Nothing here certifies clean
CI, publication or all-record completion. The following sections are historical
checkpoints, not current totals.

## Latest Applied Halobacteria Follow-Up

The [five-record Halobacteria review](20261009-halobacteria-family/README.md)
is applied locally. Guarded application, independent readback and no-op checks
account for 171 evidence-linked claims, 51 previous quantity fields and 55
ingredient/stock nodes. This adds **94 evidence entries, eleven references and
five history events**, with no new taxa-media associations. Only the five
reviewed normalized records changed.

All ten actual-written schema/strict commands, five reference CLI commands,
105 captured-source reference checks and 332 focused tests pass. Corpus
strict/ID/product and presentation checks pass. The cumulative audit verifies
**5,268 edited records and 36,049 added evidence entries**. Report reconciliation
finds **11,805 exact follow-up paths**, leaving **4,105** outside these reports;
49 historical preview ledgers are excluded. Report presence does not certify
every concentration. Three indexes are refreshed for two changed metadata
records, all five targets pass merge-retention checks, and **260 final QA tests**
pass. The fast tier passes **12,701 tests**, with 16 skipped, 2,962 deselected
and two dependency warnings. The 117 family tests are classified as corpus-tier
and pass separately within the focused and QA runs. The terminal applied
checkpoint is recorded in
[validation.json](20261009-halobacteria-family/validation.json). These are local
checks in the existing partial Python 3.13 environment, not clean CI. Global
merge verification and freshness still fail; no publication or all-record
completion is claimed.

The next source review accounts for thirteen unchanged records and 127
quantity fields, including the existing J168 preparation. A newly captured
MediaDive J1132 export provides the prepared-base stage, while the original
JCM1132 page still returns no recipe. Stage boundaries, source qualifications
and the remaining variant repairs must be resolved before application.
Earlier sections below are historical checkpoints.

## Applied Medium212 Checkpoint

The [22-record medium212 review](20261009-synthrophomonas-family/README.md)
has been applied locally: **21 changed records and one byte-exact no-op**.
Independent readback accounts for 887 evidence-linked claims, 271 source nodes
and 259 previous quantity fields. This batch adds **186 evidence entries, six
references and 21 history events**, with no new taxa-media associations.
Guarded application, readback and no-op pass; only the intended normalized
records changed. All 44 post-edit schema/strict commands, 21 supported reference
CLI commands and 241 supported reference checks pass. BacDive remains a separate
manual primary-HTML check, not a complete automated reference pass.

[Cumulative accounting](20261009-synthrophomonas-family/cumulative-audit.json)
is **5,263 edited records and 35,955 added evidence entries**. Exact follow-up
coverage remains **11,802 of 15,910**, leaving **4,108** outside these reports.
Having a report does not certify every concentration. Both historical preview
ledger versions remain preserved and explicitly excluded from canonical
coverage; all 22 canonical reports link to their applied ledgers.

Corpus strict/ID/product, six-index refresh, four-medium merge-retention and
post-application presentation checks pass. All 127 final QA tests pass, along
with Ruff, Black and whitespace checks. The current fast-tier run passes
**12,700 tests**, with 16 skipped, 2,829 deselected and two dependency warnings.
The medium212 module is now classified as corpus-tier and passes separately
within the 837-test focused run; the different historical preview count is
not a like-for-like selection. The terminal applied checkpoint is recorded in
[validation.json](20261009-synthrophomonas-family/validation.json). Global merge
verification and freshness remain failing. This is local work in the existing
partial Python 3.13 environment, not clean CI or publication. The full objective
remains open, including 31 acid-name candidates, the separate 71-record queue
and all other unresolved records. Medium323 remains an unapplied source review.
The [five-record Halobacteria preview](20261009-halobacteria-family/README.md)
passes 103 focused tests and 105 supported reference checks but remains
**unapplied**. Its proposed 94 evidence entries are excluded from applied totals.
Earlier sections below are historical checkpoints.

## Applied Methanofollis Checkpoint

The [six-record medium161 repair](20261009-methanofollis-family/README.md)
is applied locally. Independent readback accounts for 433 evidence-linked claims,
130 previous quantity fields and 147 ingredient/stock nodes, adding **118 evidence
entries, six references and six history events**. All eighteen per-record checks,
corpus strict/ID/product gates and 530 focused tests pass. Guarded application,
readback and no-op pass; only the six intended normalized records changed.

[Cumulative accounting](20261009-methanofollis-family/cumulative-audit.json)
is **5,258 edited records and 35,769 added evidence entries**. Exact follow-up
coverage remains **11,802 of 15,910**, leaving **4,108** outside these reports.
Having a report does not certify every concentration. All six canonical reports
link to their applied ledgers. Six indexes are refreshed; runtime merging keeps
both medium formulations separate and excludes four standalone solutions. The
[terminal validation](20261009-methanofollis-family/validation.json) records
**12,699 fast-tier passes**, 16 skipped, 2,243 deselected and two warnings;
106 additional QA tests pass. Global merge verification and freshness fail with
the same counts as the preceding checkpoint. This is local work in the existing
partial Python 3.13 environment, not clean CI or publication.

The full objective remains open, including 33 acid-name candidates, the separate
71-record queue and all other unresolved records. The
[22-record medium212 successor preview](20261009-synthrophomonas-family/README.md)
has 887 evidence-linked claims, 827 focused-test passes, 44 passing schema/strict
commands and 241 passing supported reference checks. BacDive page evidence is
checked separately against its primary HTML capture because the production
validator has no adapter. The fast tier passes **13,255 tests**, with 16 skipped,
2,243 deselected and two dependency warnings. The preview fixes
nine nickel-form mappings and reporting/auditor issues, but **no edits to that
family are applied**. Its proposed 186 evidence entries are not included in the
cumulative totals above. The next four-record medium323 family has source
preparation only.
Earlier sections below are historical checkpoints.

## Applied Rumen Bacteria Checkpoint

The [thirteen-record medium330 repair](20261009-rumen-bacteria-family/README.md)
is applied locally. Independent readback accounts for 717 evidence-linked
claims, 187 old quantity fields and 214 output nodes, adding **214 evidence
entries, fifteen references and thirteen history events**. Guarded application,
readback and no-op pass; only the thirteen intended YAML records changed in
this batch. All 39 per-record schema/strict/reference commands, corpus
strict/ID/product gates, 700 focused tests and 101 QA tests pass. Seven indexes
are refreshed; runtime merging retains seven medium-shaped targets and excludes
six standalone solutions.

[Cumulative accounting](20261009-rumen-bacteria-family/cumulative-audit.json)
is **5,255 edited records and 35,651 added evidence entries**. Exact follow-up
coverage is **11,802 of 15,910**, with **4,108** outside these reports. Report
presence is not complete concentration verification. The current
[terminal validation](20261009-rumen-bacteria-family/validation.json) records
**12,698 fast-tier passes**, 16 skipped, 1,980 deselected and two warnings.
Global merge verification and freshness remain failing. This is the
existing partial Python 3.13 environment, not clean CI or full-suite
certification. Thirty-five acid-name candidates, the separate 71-record queue
and every other record remain within scope. No publication or all-record
completion is claimed. Earlier sections are historical checkpoints.

## Applied Ruminococcus Albus Checkpoint

The [ten-record medium436 repair](20261009-ruminococcus-albus-family/README.md)
is applied locally. Independent readback accounts for 507 evidence-linked
claims, 126 old quantity fields and 138 output nodes, adding **155 evidence
entries, sixteen references and ten history events**. Guarded application,
readback and no-op pass; only ten intended YAML records changed. All thirty
per-record schema/strict/reference commands, corpus strict/ID/product gates,
568 focused tests and 96 QA tests pass. Six indexes are refreshed; runtime
merging preserves the six medium-shaped targets and excludes four solutions.

[Cumulative accounting](20261009-ruminococcus-albus-family/cumulative-audit.json)
is **5,245 edited records and 35,437 added evidence entries**. Exact follow-up
coverage is **11,801 of 15,910**, with **4,109** outside these reports. Report
presence is not complete concentration verification. The
[terminal validation](20261009-ruminococcus-albus-family/validation.json)
records **12,269 fast-tier passes**, 16 skipped, 1,975 deselected and two
dependency warnings. This is the existing partial Python 3.13 environment,
not clean CI or full-suite certification. Global merge verification and
freshness remain failing.
At that checkpoint, the [medium330 preparation](20261009-ruminococcus-albus-family/next-330-preparation.json)
pins thirteen unchanged records and 187 old quantity fields, sixteen successful
source captures and an explicit JCM1029 source-access gap. Thirty-eight
acid-name candidates, the separate 71-record queue and the rest of the corpus
remain within scope. No publication or all-record completion is claimed.

## Applied OTEB Checkpoint

The [six-record OTEB repair](20261009-oteb-family/README.md) is applied locally.
Independent readback accounts for 449 evidence-linked claims, 115 old quantity
fields and 127 output nodes, adding **154 evidence entries, nine references and
six history events**. Guarded application and no-op pass; only six intended
YAML records changed. All eighteen per-record commands and corpus strict/ID/
product checks pass. Five indexes are refreshed, and runtime merging preserves
four medium-shaped records while excluding two standalone solutions.

[Cumulative accounting](20261009-oteb-family/cumulative-audit.json) is now
**5,236 edited records and 35,282 added evidence entries**. Exact coverage is
still **11,799 of 15,910**, leaving **4,111** outside these reports. All six
canonical reports link to applied ledgers. Source conflicts remain explicit.
The [terminal validation](20261009-oteb-family/validation.json) records
**11,972 fast-tier passes** (16 skipped), 91 QA passes and 495 focused passes.
Global merge verification still has 1,247 name conflicts and 3,287 fingerprint
issues, and freshness fails. These are not clean-CI or full-suite results.
Forty-three acid-name candidates, a separate 71-record
queue and the rest of the corpus remain within scope. Earlier sections are
historical checkpoints, not current totals.

## Applied Medium-829 Checkpoint

The [fourteen-record medium-829 successor](20261009-desulfurobacterium-family/README.md)
is **applied locally**. Its 2,067 evidence-linked claims account for
416 old quantity fields, eight inferred-dose candidates and 447 source/input
nodes. The independent applied audit confirms 621 added evidence entries,
32 references and fourteen history events. Guarded application, readback and
no-op pass, and only the fourteen intended YAML files changed.

The successor passes 930 focused tests and all 661 offline, capture-backed
reference checks. The first proposal's sole reference failure was an existing
S1680 title prefix; the corrected successor preserves the old failed receipt
and all six existing acid entries. Text checks preserve 137 unchanged metadata
sections and 146 prior history entries. All 42 per-record post-edit commands
pass. Seven indexes were refreshed. Full-corpus strict/ID/product gates and
thirteen-record runtime merge retention pass; S1680 remains excluded from medium
merging. Product validation retains 91 warnings and 96,008 no-adapter skips.
Global merge verification still reports 1,247 name conflicts and 3,287 fingerprint
issues; freshness also fails with the predecessor's same counts. The
[terminal validation](20261009-desulfurobacterium-family/validation.json) records
11,748 passing fast-tier tests (sixteen skipped), 75 QA tests and fifteen
explicit legacy corpus-tier tests. The earlier single legacy-contract failure
is retained; the fix changes no recipe. The legacy module's automatic corpus
classification is documented rather than hiding its exclusion from fast tests.
Historical previews remain immutable beside new applied ledgers.

[Cumulative accounting](20261009-desulfurobacterium-family/cumulative-audit.json)
is now **5,232 edited records and 35,128 added evidence entries**. Exact follow-up
report coverage is **11,799 of 15,910**, with **4,111** outside these reports.
Report presence does not certify every concentration. Thirteen canonical reports
link to applied ledgers; M2587 has one new canonical report. Forty-six acid-name
candidates and the separate 71-record queue remain unchanged.

The applied-corpus inventory identifies 4,866 title-prefix candidate paths for
[structured source follow-up](20261009-desulfurobacterium-family/issue-title-prefixes.md),
with 4,868 root-reference entries. These are leads, not confirmed errors.
At this historical checkpoint, the six-record OTEB successor preview had
449 evidence-linked claims covering 115 old quantity fields and 127 output
nodes, with 154 proposed evidence entries. All 495 focused tests, 180 reference
checks and twelve preview schema/strict commands pass. These are separate from
the earlier medium-829 fast-tier collection. No OTEB edits were applied at that
checkpoint; its additions were excluded from the medium-829 cumulative totals.
The complete normalized corpus is still
15,910 records, and the all-record objective remains unfinished.

## Latest Applied Medium-119 Follow-Up

The [nineteen-record medium-119 family](20261009-methanobacterium-family/README.md)
is applied locally: **3,095 claims** account for
**633 old quantity slots** and **650 source/input nodes**. All **1,187 focused
tests**, **38 baseline schema/strict commands** and **904 capture-backed reference
checks** pass. The independent applied audit confirms 847 added evidence entries,
57 references and nineteen history events. Guarded application, readback and
no-op pass, as do all 57 per-record post-edit checks and corpus strict/ID/product
checks. Five indexes were refreshed, and runtime merging preserves the claims.

Only the nineteen intended YAML records changed. [Cumulative accounting](20261009-methanobacterium-family/cumulative-audit.json)
is now **5,219 edited records and 34,507 added evidence entries**. Follow-up
coverage remains **11,798 of 15,910**, with **4,112** outside these reports.
Historical previews are preserved alongside new applied claim ledgers. The
[terminal validation](20261009-methanobacterium-family/validation.json) records
**11,100 passing fast-tier tests** (16 skipped), 32 final QA checks including
55 registry tests, and the unchanged post-edit corpus hash. Global merge
verification still has 1,247 name conflicts and 3,287 fingerprint issues;
freshness also fails. The [handoff](20261009-methanobacterium-family/next-work.md)
retains the entire remaining corpus scope and fourteen identified medium-829
candidates with 435 inspected source rows and 416 mapped old quantity fields.
This is offline capture-backed reference verification,
not a new live refresh or all-record completion. Earlier totals below are
historical checkpoints.

## Latest Allisonella Follow-Up

The [two Allisonella records](20261009-allisonella-acids/README.md) are applied
locally, adding **67 evidence entries, five references and two history events**.
All 42 prior quantity slots and 43 source/input nodes are accounted for by
194 evidence-linked claims. The repair separates liquid fatty-acid stock inputs,
resazurin strength and stock doses, preserves source-specific KOMODO rates and
nulls, restores the missing acid, and replaces unsupported exact-duplicate links.

All **526 focused tests** and **72 live reference checks** pass. Three sources
refresh identically, with the initial sandbox network failure retained. All six
post-edit schema/strict/reference commands, independent applied audits, readback
and no-op pass. Four generated indexes were refreshed; runtime merging retains
both formulations separately and preserves their claims. Corpus strict-schema
and ID checks pass for 15,910 records. Product validation retains 91 warnings
and 96,040 no-adapter skips. Global merge verification/freshness remain failing.
The fast tier passes **10,167 tests** (16 skipped, 1,945 deselected). The
[terminal validation receipt](20261009-allisonella-acids/validation.json) retains
all results and known failures. This uses the existing partial locked Python
3.13 environment, not clean CI or the complete test suite.

[Cumulative accounting](20261009-allisonella-acids/cumulative-audit.json) is
**5,200 edited records and 33,660 added evidence entries**. Follow-up coverage
remains **11,798 of 15,910**, with **4,112** outside these reports. The two
existing canonical reports link to the current claim ledgers. The remaining
[handoff](20261009-allisonella-acids/next-work.md) retains 74 acid-name candidates,
the separate 71-record M142 queue, one additional family neighbor and 21 stale
exact family references. The next 19-record medium-119 family has 23 successful
source captures, 645 extracted rows and nine visually inspected PDF pages, but
no applied edits. All-record completion and publication remain open.

## Previous Linked Middlebrook Follow-Up

The [eleven linked Middlebrook records](20261009-middlebrook-linked/README.md)
are now applied locally, adding **274 evidence entries, 23 references and
eleven history events**. All 244 prior quantity slots and 781 claims are
independently accounted for. The repair restores source-specific ingredients,
separates preparation alternatives and stock scopes, and replaces unsupported
exact-duplicate links with reciprocal, source-qualified relationships.

All **792 focused tests** and **297 cached reference checks** pass, as do
per-record schema/strict/reference checks, independent applied audit, readback
and no-op. The original fourteen-source refresh succeeded; two later live
attempts returned HTTP 403 and remain preserved separately. Four indexes were
regenerated, and runtime merging retains all eleven formulations separately
with their claims. Corpus strict-schema and ID checks pass for 15,910 records;
variant-link validation has no findings under its current ID-fallback rules.
The broader queue inventory separately found [21 stale exact family references](20261009-middlebrook-linked/issue-stale-family-paths.md)
outside this repaired cohort. Product checks retain 91 warnings and
96,042 no-adapter skips. Global merge verification still has 1,247 name conflicts
and 3,287 fingerprint issues; freshness still differs. The fast tier passes
**10,086 tests** (16 skipped). The [terminal validation receipt](20261009-middlebrook-linked/validation.json)
retains every completed check and known failure; this is not clean CI or a
complete-suite claim.

[Cumulative accounting](20261009-middlebrook-linked/cumulative-audit.json) is
**5,198 edited records and 33,593 added evidence entries**. Exact follow-up
coverage remains **11,798 of 15,910**, with **4,112** outside these reports.
All eleven canonical reports already existed and now link to the new ledgers.
The remaining [handoff](20261009-middlebrook-linked/next-work.md) preserves
76 acid-name candidates, the separate 71-record M142 queue and the full outside-
report scope. At that checkpoint the Allisonella pair was unchanged; its later
applied review is documented above. Publication and the all-record goal remain
open. Earlier sections retain their historical totals.

## Latest NBRC Evidence Validation

The [NBRC recipe-table parser repair](20261009-nbrc-reference-validation/README.md)
passes all **240 reference checks** and all thirteen reference CLI commands for
the unchanged Middlebrook batch. All fifteen original sources refresh
identically. The focused suite passes **523 tests** and the fast tier passes
**9,913 tests** (16 skipped). The [final receipt](20261009-nbrc-reference-validation/validation.json)
confirms unchanged recipe/evidence bytes, curation counts and coverage counts.
The historical single-reference failure below is retained, not overwritten.

An exact-reference inventory across all 15,910 records finds 196 records with
199 entries across 188 NBRC URLs, but only one explicit snippet-bearing entry.
Only NBRC 1219 was source-verified in this validator batch. At that checkpoint,
the next eleven linked Middlebrook records had [233 inspected source rows and
representation decisions](20261009-middlebrook-linked/decisions.md), not applied
changes; the later applied batch is documented above.

## Latest Middlebrook Follow-Up

The [13-record Middlebrook stage repair](20261009-middlebrook-stages/README.md)
is applied locally. It adds **225 evidence entries, 15 references and 13 history
events**, covering 234 prior quantity slots and 548 explicit claims.
False LB expansions are removed, albumin is restored, and commercial-base
details, stock compositions and addition doses are separated. Unsupported
final-volume and percentage bases remain unresolved rather than guessed.

All 526 focused tests, lint, formatting, baseline schema/strict, independent
applied audit, readback and no-op checks pass. Fourteen DSMZ/TOGO captures
refresh identically. This batch's original automated receipt passed 239 of 240
checks; the sole NBRC snippet failure was manually verified against its captured
original. Its [local issue](20261009-middlebrook-stages/issue-nbrc-reference-matcher.md)
is resolved by the later parser repair above, without rewriting the old receipt.
Strict schema and ID checks pass for all 15,910 normalized records; product
validation retains 91 warnings and 96,053 no-adapter skips. Four generated
indexes were refreshed, and all 13 formulations retain their claims in separate
schema-valid runtime merges. The fast tier passes 9,819 tests (16 skipped).
The [final receipt](20261009-middlebrook-stages/validation.json) retains global
merge failures (1,247 name conflicts and 3,287 fingerprint issues) and freshness
differences (4,275 tracked-only, 8,732 fresh-only and 2,045 changed files).

[Cumulative accounting](20261009-middlebrook-stages/cumulative-audit.json) is
**5,187 edited records and 33,319 added evidence entries**. Exact follow-up
[coverage](20261009-middlebrook-stages/followup-coverage.json) is **11,798 of
15,910**, with **4,112** outside these reports. Report presence does not mean
all claims are resolved. Earlier sections retain their historical totals.
Publication and the all-record goal remain open.

## Previous Evidence Validation

The [KOMODO parser repair](20261008-komodo-reference-validation/README.md) now
passes all **86 reference checks** and all four reference CLI commands for the
four hydrolysate records, without changing any recipe or evidence bytes.
All 31 earlier table/pH failures are covered by immutable regression cases.
The focused suite passes **452 tests**; the new fast tier passes **9,644 tests**
(16 skipped). The [final receipt](20261008-komodo-reference-validation/validation.json)
preserves the unchanged corpus, actual source-fetch failures and successful checks.

All five public sources refreshed identically. The requests fetch received
HTTP 403 on KOMODO; an explicit separate urllib capture succeeded, and the
cached CLI checks pass. Both outcomes are retained. This repairs table matching,
not the failed requests transport. Counts and all-record scope are unchanged.

## Latest Recipe Follow-Up

The [four hydrolysate repairs](20261008-lactalbumin-formulations/README.md) are
applied locally to DSMZ 1021, KOMODO 1021/1021_16929 and TOGO M2287. They remove
false LB expansions, restore source-specific hydrolysates, separate stock/basal
and final-medium amounts, and correct unsupported exact-duplicate links.
They add 77 evidence entries, nine references and four history events.

[Cumulative accounting](20261008-lactalbumin-formulations/cumulative-audit.json)
is **5,174 edited records and 33,094 added evidence entries**.
[Coverage](20261008-lactalbumin-formulations/followup-coverage.json) is
**11,786 of 15,910** exact normalized paths, with **4,124** outside these reports.
M2287 adds one follow-up path; historical full-corpus audits remain separate,
and report presence does not mean all claims are resolved.

All 344 focused tests, independent audit, readback and no-op checks pass.
All five sources refresh identically and all 201 excerpts match their captures.
The historical applied retry passed 55 of 86 checks: 31 KOMODO table quotations
failed because the generic cache retained raw HTML, as reproduced in the
[parser diagnostic](20261008-lactalbumin-formulations/komodo-parser-diagnostic.json).
The later parser repair above passes all 86 unchanged checks. Strict schema/ID checks pass for
all 15,910 records; product validation has 91 warnings and 96,066 no-adapter skips.
Five generated indexes were refreshed, and all four repaired formulations
retain their claims in separate schema-valid runtime merges. The batch's fast
tier passes 9,541 tests (16 skipped); this predates the later parser change.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues, and freshness fails. The
[consolidated receipt](20261008-lactalbumin-formulations/validation.json) records
all terminal checks. Publication and the all-record goal remain open.
The [next-work handoff](20261008-lactalbumin-formulations/next-work.md) retains
100 identity candidates, the separate 71-record M142 queue and source limits.

## Earlier BSK Follow-Up

The [three BSK formulation repairs](20261008-bsk-formulations/README.md) are
applied locally to M2410, DSMZ 1829 and JCM 173. They restore albumin, remove
false LB constituents, correct liquid/mass and stock/final-medium scopes, and
preserve each source's distinct preparation. They add 69 evidence entries,
five references and three history events, not taxa-media associations.

[Cumulative accounting](20261008-bsk-formulations/cumulative-audit.json) is
**5,170 edited records and 33,017 added evidence entries**.
[Coverage](20261008-bsk-formulations/followup-coverage.json) is
**11,785 of 15,910** exact normalized paths, with **4,125** outside follow-up
reports. Only M2410 adds a new path to this follow-up coverage; report presence
does not mean all scientific claims are resolved.

All 74 reference checks against five refreshed official sources pass, as do
373 focused tests, applied schema/strict checks, independent audit, readback
and no-op. Five generated metadata indexes were refreshed. Full-corpus merge
routing retains all three repaired formulations separately, with their claims
and schema validity. Strict schema and ID checks pass for all 15,910 normalized
records. Product validation passes with 91 warnings and 96,070 no-adapter skips.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues; generated-data freshness also fails. The fast tier passes
9,443 tests (16 skipped). All intended checks are terminal in the
[validation receipt](20261008-bsk-formulations/validation.json).
This is not a clean-CI, complete-suite or all-record completion claim.
The [next-work handoff](20261008-bsk-formulations/next-work.md) preserves 104
identity candidates, the separate 71-record M142 queue and M2410's unresolved
ingredient addition order. Publication remains incomplete.

## Earlier Evidence Validation

The [official PDF validator repair](20261008-recipe-pdf-validation/README.md)
now passes all 122 reference checks for the four DSMZ/KOMODO 403/751 records,
without changing any YAML evidence or amounts. Binary hashes, exact extracted
text and heading/accession identity are checked, including wrapped titles.
The earlier failing receipts remain preserved. All 288 focused tests and 9,357
fast-tier tests pass (16 skipped in the fast tier). The
[final validation receipt](20261008-recipe-pdf-validation/validation.json)
preserves the unchanged normalized corpus and evidence counts. This is not a
complete-suite or clean-CI claim.

The broader PDF-only check found 220 explicit claims across 61 records: all 152
snippets and 27 titles pass; 41 bibliography title mismatches in 34 records
remain open in a [local issue draft](20261008-recipe-pdf-validation/issue-dsmz-pdf-bibliography-titles.md).
Another 172 records have PDF references without explicit snippet/title claims;
they were inventoried, not verified. This is not an all-source reference audit
or a concentration-completion claim. No new recipe edits or coverage increments
occurred, and publication remains incomplete.

## Earlier DSMZ Albumin Follow-Up

The [DSMZ/KOMODO 403/751 preparation repair](20261008-dsmz-albumin-preparations/README.md)
is applied locally. It restores albumin identities, separates stock compositions
and liquid inputs, corrects the scope of Solution A's pH/titrant, and preserves
liquid SC as a separate inline variant. It adds 114 evidence entries, eight
references and four events, not taxa-media associations.

[Cumulative accounting](20261008-dsmz-albumin-preparations/cumulative-audit.json)
is **5,167 edited records and 32,948 added evidence entries**.
[Coverage](20261008-dsmz-albumin-preparations/followup-coverage.json) remains
**11,784 of 15,910** exact normalized paths, with **4,126** outside follow-up
reports. All four already had reports; covered claims can still be unresolved.

All 126 dedicated tests and 459 focused regression tests pass, as do baseline
schema/strict, independent applied audit, readback and no-op checks. Five metadata
artifacts were refreshed through the generator, and all four targets retain
their claims in schema-valid runtime merges. The fast tier passes 9,300 tests
(16 skipped). Strict schema and serial ID checks pass for all 15,910 normalized
records. Product validation passes with 91 warnings and 96,073 no-adapter skips;
chemical mappings are not comprehensively recertified. All intended checks are
terminal in the [validation receipt](20261008-dsmz-albumin-preparations/validation.json).
The original receipt retained 60 failing PDF snippet and four title checks.
Those checks now pass after the PDF validator repair above; the historical
receipt is not rewritten. Global merge/freshness and publication remain incomplete.

The [next-work handoff](20261008-dsmz-albumin-preparations/next-work.md) retains
107 unchanged identity candidates (76 acid-name, 31 albumin-name), the separate
71-record M142 queue, and three prepared but unedited BSK candidates.

## Earlier Albumin Counterparts

The [M194/M213/M244/J252 albumin repair](20261008-albumin-counterparts/README.md)
is applied locally. It restores albumin identities and preparation boundaries,
retains the explicitly supported 10% w/v albumin stock and calculated batch dose
in M244/J252, corrects liquid/mass scopes, and withdraws M244's unsupported
high-metal flag. It adds 101 evidence entries, seven references and four history
events. No taxa-media associations were added.

[Cumulative accounting](20261008-albumin-counterparts/cumulative-audit.json) is
**5,163 edited records and 32,834 added evidence entries**.
[Follow-up coverage](20261008-albumin-counterparts/followup-coverage.json) is
**11,784 of 15,910** exact normalized paths, with **4,126** outside these reports.
Report coverage is not scientific completion.

All four baseline/applied schema, strict and reference checks pass, as do
independent readback, no-op, 155 dedicated tests and 498 focused tests. Five
generated indexes were refreshed. All four repaired outputs retain their claims
in separate schema-valid runtime merge groups. The fast tier passed 9,173 tests
(16 skipped) before a subsequent test-only resolver isolation fix; all 11 direct
resolver tests pass after that fix. Strict schema and serial ID checks pass for
all 15,910 records. The original ID race failure is retained alongside the retry.
Product validation passes with 91 warnings and 96,077 no-adapter skips; chemical
identities are not all recertified. Global merge verification and generated-data
freshness still fail. All intended checks are terminal in the
[validation receipt](20261008-albumin-counterparts/validation.json).
Publication is incomplete.

The [next-work handoff](20261008-albumin-counterparts/next-work.md) retains 111
unchanged identity candidates and the separate 71-record M142 queue. The next
DSMZ/KOMODO 403/751 pairs have inspected sources and pinned unchanged baselines,
not applied edits or new completed-review claims.

## Earlier JCM Albumin Follow-Up

The [J201/J220 albumin and reagent repair](20261008-jcm-albumin-inputs/README.md)
is applied locally. It removes false LB expansions, restores albumin fraction V,
and separates product/stock doses, late additions and unknown stock strengths.
It adds 35 evidence entries, three references and two history events. No taxa-media
associations were added. J201 is provider-backed; its original page is unavailable
and is not cited as formulation evidence.

[Current cumulative accounting](20261008-jcm-albumin-inputs/cumulative-audit.json)
is **5,159 edited records and 32,733 added evidence entries**.
[Current coverage](20261008-jcm-albumin-inputs/followup-coverage.json) remains
**11,781 of 15,910** exact normalized paths, with **4,129** outside follow-up
reports. Existing report coverage is not scientific completion.

Both applied schema/strict/reference checks, readback, no-op, 73 dedicated tests
and 819 focused tests pass. The fast tier passes 9,017 tests (16 skipped);
strict schema and ID checks pass for all 15,910 records. Product validation
passes with 91 warnings and 96,081 no-adapter skips; chemical identities are
not all recertified. Three generated indexes were refreshed, and both
repaired outputs retain their claims in separate schema-valid runtime merge
groups. Global merge verification and generated-data freshness still fail.
All intended checks are terminal in the
[validation receipt](20261008-jcm-albumin-inputs/validation.json).
Publication remains incomplete. The
[next-work handoff](20261008-jcm-albumin-inputs/next-work.md) retains 115 unchanged
identity candidates and the separate 71-record M142 queue. M194/M213/M244/J252
sources and unchanged baselines are prepared, not counted as completed reviews.

## Earlier JCM Acid Follow-Up

The [J266/J675/J1203 identity and preparation repair](20261008-jcm-lb-acids/README.md)
is applied locally. It removes false LB expansions, restores source-listed
methylbutyric acids, and separates liquid batch inputs, stock compositions,
stock doses and receiving-medium contributions. It adds 167 evidence entries,
eight references and three history events. No taxa-media associations were added.

[Current cumulative accounting](20261008-jcm-lb-acids/cumulative-audit.json)
is **5,157 edited records and 32,698 added evidence entries**.
[Current coverage](20261008-jcm-lb-acids/followup-coverage.json) remains
**11,781 of 15,910** exact normalized paths, with **4,129** outside follow-up
reports. All three targets already had canonical reports; this repair does not
increase unique report coverage or prove that all covered claims are resolved.

All three applied schema/strict/reference checks, readback, no-op, 746 focused
tests and 8,943 fast-tier tests pass. Strict corpus and ID checks pass for all
15,910 records. Product validation passes with 91 warnings and 96,083 no-adapter
skips; chemical identities are not all recertified. Four generated metadata
indexes were refreshed. The three repaired outputs retain their claims in
separate schema-valid runtime merge groups. Global merge and freshness gates
still fail, with the preceding batch's failure counts. All intended checks are
terminal in the [validation receipt](20261008-jcm-lb-acids/validation.json).
Publication remains incomplete.

The [next-work handoff](20261008-jcm-lb-acids/next-work.md) preserves 117 unchanged
LB-identity candidates (76 acid-name, 41 albumin-name) and the separate 71-record
M142 queue. J201/J220 baselines and four responses are captured for the next
review; the JCM201 original page currently returns no recipe and is not accepted
as formulation evidence. This capture work is not a coverage increment.

## Earlier M258/M260 Follow-Up

The [M258/M260 identity and nested-stock repair](20261008-m258-m260-stocks/README.md)
is applied locally. It removes M258's erroneous LB expansion, restores its
source-backed fatty acid and separate preparations, and places M260's trace
minerals inside its seawater stock. It adds 163 evidence entries and ten
references. No taxa-media associations were added.

[Current cumulative accounting](20261008-m258-m260-stocks/cumulative-audit.json)
is **5,154 edited records and 32,531 added evidence entries**.
[Current coverage](20261008-m258-m260-stocks/followup-coverage.json) is
**11,781 of 15,910** exact normalized paths, with **4,129** outside follow-up
reports. Covered records can still have unresolved claims.

Both applied schema/strict/reference checks, readback, no-op, 740 focused tests
and 8,849 fast-tier tests pass. Strict corpus and ID checks pass for all 15,910
records. Product validation passes with 91 warnings and 96,086 no-adapter
skips; chemical identities are not all recertified. The global merge/freshness
gates remain failing. All intended checks are terminal in the
[validation receipt](20261008-m258-m260-stocks/validation.json).
Publication is incomplete.

A historical identity audit found 80 acid-name and 42 albumin-name substitutions
among 145 LB expansions. M258 is now repaired; M2366 was previously restored.
The other 120 records remain priority source-review candidates, not completed
reviews. Ninety already have follow-up reports. The
[next-work handoff](20261008-m258-m260-stocks/next-work.md) preserves these exact
baselines, the inspected J266 source, and the separate 71-record M142 queue.

## Earlier Reducing-Agent Follow-Up

The [five-record reducing-agent/stock repair](20261008-reducing-stages/README.md)
is applied locally to M225, M229, M234, M236 and M243. It adds 431 evidence
entries and 26 references while correcting stock boundaries and preserving
source batch amounts without assumed final-volume concentrations.

[Current cumulative accounting](20261008-reducing-stages/cumulative-audit.json)
is **5,152 edited records and 32,368 added evidence entries**.
[Current coverage](20261008-reducing-stages/followup-coverage.json) is
**11,779 of 15,910** exact normalized paths, with **4,131** outside follow-up
reports. Covered paths can still have unresolved claims. No taxa-media
associations were added in this batch.

All five applied schema/strict/reference checks, guarded readback, no-op,
817 focused tests and 8,776 fast-tier tests pass. Strict corpus and ID checks
pass for all 15,910 records. Product validation exits successfully with 91
warnings and 96,087 no-adapter skips; chemical identities are not all recertified.
The global merge/freshness gates remain failing. All intended checks are terminal
in the [validation receipt](20261008-reducing-stages/validation.json).
Publication remains incomplete. The
[next-work handoff](20261008-reducing-stages/next-work.md) preserves 73 pending
M142-dependent records and prioritizes the discovered M258 product-substitution
error and M273/M274 source-variant conflict.

## Earlier JCM261 Follow-Up

The [JCM261 / TOGO M253 variant repair](20261008-j261-variant/README.md)
applies the three explicit final rates, sulfur omission, pH 7.0, separate
stock boundaries and corrected reciprocal parent links. Parent formulations
are unchanged. Four records receive 193 new evidence entries, ten references
and four events; all 36 old child quantity fields are accounted for.

[Cumulative accounting](20261008-diff-audit-after-j261.json) is **5,127 edited
records, 30,962 new evidence entries, 5,477 references and 5,329 events**.
[Coverage](20261008-followup-coverage-after-j261.json) is **11,754 of 15,910**
paths, with **4,156** outside follow-up reports. Coverage is not scientific
completion. No growth associations were added.

Target schema/strict, full-corpus strict, readback, no-op and 225 focused
tests pass. All four records retain their claims in separate runtime merge
groups. Five generated metadata artifacts were refreshed. Reference validation
remains red despite literal captured-source matches for all 193 new snippets;
the installed matcher accepts 97 and rejects 96. The fast tier passes 8,036
tests (16 skipped); IDs and variant links pass. Products exit 0 with 91
warnings and 96,081 no-adapter skips. Broad checks are terminal: merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues;
freshness fails with 4,275 tracked-only, 8,732 fresh-only and 2,045 changed
shared paths. Publication is not complete. Sources for the next 98 pending
M142-dependent records are captured, not yet counted as reviewed.

## Previous Follow-Up

The [six-record JCM stock/preparation repair](20261008-jcm-stock-preparations/README.md)
restores separate stocks in J151/J187/J197 and TOGO M142/M180/M190. It adds
217 evidence entries and withdraws 111 unsupported quantity assertions while
preserving source batch amounts in notes. All 185 old quantity fields are
accounted for; unknown percentage bases, doses and sulfide identity conflict
remain explicit. It follows the completed local
[methanogen-boundary repair](20261008-methanogen-boundaries/README.md).

The [current cumulative audit](20261008-diff-audit-after-jcm-stock-preparations.json)
records **5,125 edited records, 30,769 new evidence entries, 5,467 references
and 5,325 events**. [Follow-up coverage](20261008-followup-coverage-after-jcm-stock-preparations.json)
is **11,753 of 15,910 paths**, with **4,157** outside this coverage.
Coverage does not mean all concentration claims are verified. No growth
association was added in this cohort.

All six records and the 15,910-record corpus pass strict schema. Readback and
no-op apply pass; 186 repair/I-O/plausibility tests and 8,035 fast-tier tests
pass (16 skipped). Runtime merge retention
preserves the six targets as separate formulation groups. Five indexes and
recipe statistics were refreshed from generator output. The installed reference
gate remains red: all 217 primary snippets match frozen sources literally,
but four JCM table snippets fail automated matching and API titles mismatch
URL fallbacks. Broad checks are terminal. Products pass with 91 warnings and
96,077 no-adapter skips; merge verification fails with 1,247 name conflicts
and 3,287 fingerprint issues. Freshness fails with 4,275 tracked-only,
8,732 fresh-only and 2,045 changed shared paths. Final hashes and checks are
recorded in the cohort artifacts. Publication remains incomplete.

## Previous Stock Follow-Up

The [FeCl2 stock repair](20261008-fecl2-stock/README.md) separates the explicitly
stated **7.7 M HCl reagent** from its **0.01 L batch dose** in one already-reported
stock record. Three evidence entries, one reference and one event are added;
the existing FeCl2 and water quantities retain their qualified source support.
The percentage basis and measured final volume are not inferred.

The [cumulative audit](20261008-diff-audit-after-fecl2.json) records **5,116 edited
records, 30,449 new evidence entries, 5,451 references and 5,316 events**. The
stock-stage rebase is separate from the unchanged 1,386 quantity-correction count.
[Coverage](20261008-followup-coverage-after-fecl2.json) remains **11,749 of 15,910
paths**, with **4,161** outside follow-up reports and unresolved claims within
covered records. No growth associations were added.

All 15,910 records pass strict schema, IDs pass, and record readback/no-op checks
pass. The initial focused selection passes 76 tests; the strengthened repair,
index and manifest selection passes 55 tests. All five snippets match pinned
source text, but the citation validator fails on the existing API title and one
JCM table-text match. Three generated indexes were refreshed for this record.
The fast tier passes 7,885 tests; product validation exits 0 with 91 warnings and
96,063 no-adapter skips. All broad checks are terminal. Merge verification fails
with 1,247 name conflicts and 3,287 fingerprint issues; freshness fails with
4,275 tracked-only, 8,732 fresh-only and 2,045 changed shared paths. Publication
remains unfinished; the tracked merged corpus was not rewritten.
The [final source/hash/report check](20261008-fecl2-stock/final-checks.json) passes,
including all 27 current repair tests, lint, formatting and diff checks. The
standalone stock remains outside medium merging; source-backed corrections for
receiving media and the rest of the corpus remain active work.

## Latest Integration

The [formulation-aware merge repair](20261008-formulation-merge/README.md)
separates ingredient-set candidates from automatic consolidation and preserves
scoped evidence. Its [final independent retention audit](20261008-formulation-merge/retention-strict.json)
checks all 15,910 tracked normalized paths: **10,783 eligible media retain their
claims and provenance across 10,777 closed-schema-valid outputs**, with no newly
omitted eligible input. The existing routing excludes 4,785 standalone solutions
and 342 empty/unfingerprintable media. That integration repair changed no source
YAML; the subsequent FeCl2 follow-up above is separate. The M1038 stock
loss below is repaired in newly computed results, not in the stale tracked merges.

This is not additional scientific concentration verification: edited-record and
evidence counts below do not increase. The focused run passes 120 tests. The full
run reports 9,729 passed, 19 skipped and two derived-data freshness failures.
The manifest was refreshed and retested; eight generated index files were
refreshed for 66 records, and all 27 recipe-index tests pass. The original full
run remains failed; the fast tier passes 7,858 tests. All broad checks are now
terminal. Legacy merge verification fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness comparison fails with 4,275 tracked-only, 8,732
fresh-only and 2,045 changed shared paths (6,320 tracked versus 10,777 fresh
outputs). Full-record curation, citation validation and publication remain
unfinished. These checks used the partial locked Python 3.13 runtime, not full CI.
The [final combined check](20261008-formulation-merge/final-checks.json) passes
148 tests plus lint/format/diff checks and verifies source, code and refreshed
metadata hashes. All checks are terminal; publication is not ready.

## Previous Follow-Up

The [methanogen repair](20261008-togo-methanogens/README.md) changes **three
records**: TOGO M1038/M1039 and MediaDive J986. It corrects nine quantities,
adds the missing trimethylamine hydrochloride supplement, and withdraws 44
unsupported quantity slots. Thirty-seven withdrawals replace copied base
ingredients with an explicit base-medium reference, not a claim that those
constituents are excluded. It adds **19 evidence entries, eight references and
three events**, while preserving the unresolved 3%/30% trimethylamine-stock
conflict. No growth associations were added.

The [current cumulative independent audit](20261008-diff-audit-after-methanogens.json)
verifies **5,116 distinct edited records, 30,446 new evidence entries, 5,450 new
references, 5,315 appended events and 1,386 quantity corrections**. Withdrawals,
stock rebases and added quantity slots are separate counters. Evidence includes
batch-mass, preparation and identity support, not just verified concentrations.
[Coverage](20261008-followup-coverage-after-methanogens.json) is **11,749 of
15,910 normalized paths**, with **4,161** outside these follow-up reports and
unresolved claims inside reported records.

Readback, no-op rerun, independent audit, schema, full-corpus strict validation,
IDs, variant links and 92 focused tests pass. The batch's historical merge retention fails for
M1038: an existing three-record group drops its corrected stock entries and root
provenance. The other two recipes retain their data in singleton groups. Citation
validation fails on six API titles and five text matches; all literal excerpts
are independently checked against captured JSON/rendered HTML. The terminal
fast suite passes 7,808 tests (16 skipped, 1,889 deselected). Product validation
exits 0 with 91 warnings and 96,063 no-adapter skips. Global merge verification
fails with 1,247 name conflicts and 3,287 fingerprint issues; freshness fails
with 3,724 tracked-only, 3,903 fresh-only and 1,710 changed shared paths. These
checks use the partial locked Python 3.13 environment, not full CI. Publication
remains gated; local changes are not committed, pushed or merged.

## Previous Follow-Up

The [JCM973 preparation repair](20261008-jcm973-preparations/README.md) changes
**four already-reported records**: TOGO M1023/M1024, MediaDive J973 and solution
4996. It restores separate preparation stages, rebases four magnesium chloride
stock strengths, corrects two water units and adds two water inputs. Twenty-five
unsupported g/L values are withdrawn, with source gram amounts preserved in
evidence-backed batch notes. The repair adds **45 evidence entries, eight
references and four events**. Stock-addition volumes after autoclaving and final
medium concentrations remain unquantified; no growth associations were added.

The [then-current cumulative independent audit](20261008-diff-audit-after-jcm973.json)
verifies **5,113 distinct edited records, 30,427 new evidence entries, 5,442 new
references, 5,312 appended events and 1,377 quantity corrections**. Four new
stock-stage rebases and 25 withdrawals are separate count categories. Evidence
counts include preparation and batch-mass support, not just concentrations.
[Coverage](20261008-followup-coverage-after-jcm973.json) remains **11,747 of 15,910
normalized paths**, with **4,163** outside these follow-up reports and unresolved
claims inside reported records.

Readback, no-op rerun, independent audit, class-specific schema, full-corpus
strict validation, IDs, variant links, historical continuity and 116 focused
tests pass. Complete provenance is retained in the three current singleton
merge groups; the standalone solution is excluded. This does not prove
multi-source merging is fixed. All 45 snippets pass the installed text matcher,
but full citation validation fails on eight API-title mismatches. The fast suite
passes 7,773 tests (16 skipped, 1,889 deselected). Product validation exits 0 with
91 warnings and 96,061 no-adapter skips. Global merge verification fails with
1,247 name conflicts and 3,287 fingerprint issues; freshness fails with 3,723
tracked-only, 3,901 fresh-only and 1,709 changed shared paths. These checks use
the partial locked Python 3.13 environment, not full CI. The
[next TOGO pair source handoff](20261008-togo-next-pair-handoff.md) is triage only,
not an additional review or applied change. Local work is not committed, pushed
or merged; publication remains gated.

## Previous Follow-Up

The [first TOGO liquid/agar pairs](20261008-togo-first-pairs/README.md) add four
exact-path reports and change two records (M1001/M1002). Eight batch-volume
quantities are corrected, two explicit NH4Cl stock strengths are added, and the
solid-medium agar concentration receives evidence. The changes add **38 evidence
entries, four references and two events**. Twelve retained mass concentrations
remain unverified; their new evidence supports batch-mass notes only. M1023/M1024
were unchanged in that batch because the unavailable original JCM973 recipe and
the preserved two-stage preparation needed further resolution. The preparation
repair above subsequently supersedes those two unchanged outcomes.

The [then-current cumulative independent audit](20261008-diff-audit-after-togo-pairs.json)
verifies **5,109 distinct edited records, 30,382 new evidence entries, 5,434 new
references, 5,308 appended events and 1,375 quantity corrections**. Evidence
includes identity, preparation and batch-mass notes, not just verified
concentrations. The [then-current coverage snapshot](20261008-followup-coverage-after-togo-pairs.json)
covers **11,747 of 15,910 normalized paths**, with **4,163** outside these follow-up
reports. Reported records still have unresolved claims. No taxa-media growth
associations were added.

Applied hashes, no-op rerun, independent semantic inversion, open schema,
full-corpus strict schema, IDs, variant links and 64 focused tests pass. Both
changed inputs retain their complete provenance in their current singleton
merge groups; this is not proof that multi-source merging is fixed. The
network-enabled citation gate fails with 20 snippet errors and two API title
mismatches, while actual JSON excerpts and JCM table text are verified separately.
The fast suite passes 7,739 tests (16 skipped, 1,889 deselected). Product
validation exits 0 with 91 warnings and 96,061 no-adapter skips. Global merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues;
freshness fails with 3,721 tracked-only, 3,899 fresh-only and 1,709 changed shared
paths. The terminal source/hash/report check passes. These checks ran in the
partial locked Python 3.13 environment, not full CI. Publication remains gated,
and local changes have not been committed, pushed or merged.

## Previous Follow-Up

The [DSMZ 1157/1164 stock-stage repair](20261008-dsmz1157-1164-stocks/README.md)
changes **six already-reported normalized records**. It separates fifteen stock
components, restores three explicit riboflavin stock strengths, removes twelve
unsupported stock-stage quantities, adds twelve batch stock-dose quantities and
four water-input quantities, and corrects two existing water units. It adds
**47 evidence entries, ten references and six events**, preserving prior quotes
and history. Two stale exact parent/child paths are corrected.

The [then-current cumulative independent audit](20261008-diff-audit-after-stocks-1157.json)
verifies **5,107 distinct edited records, 30,344 new evidence entries, 5,430 new
references, 5,306 appended events and 1,367 quantity corrections**. Stock-stage
rebases, added quantities and withdrawals are separate categories. Evidence
includes preparation and identity claims, not only concentrations. The
[then-current coverage snapshot](20261008-followup-coverage-after-stocks-1157.json)
remains **11,743 of 15,910 normalized paths**, with **4,167** outside these
follow-up reports. Reported records can still contain unresolved claims. No
taxa-media growth associations were added.

All six applied hashes, a no-op rerun, open schema, full-corpus strict schema,
IDs, variant links, historical report continuity and 156 focused tests pass.
Actual merging retains these stocks and their quantities but loses complete
source-specific provenance from two medium inputs; the strict retention check
fails. Network-enabled citation validation also fails on PDF text extraction
and API/PDF title handling; 65 of 71 snippets pass its matcher and the actual PDF
snippets are separately verified. The fast suite passes 7,713 tests (16 skipped,
1,889 deselected). Product validation exits 0 with 91 warnings and 96,061
no-adapter skips. Global merge verification still fails with 1,247 name conflicts
and 3,287 fingerprint issues; freshness fails with 3,720 tracked-only, 3,898
fresh-only and 1,708 changed shared paths. The terminal aggregate source/hash/
report check passes. These checks used the partial locked Python 3.13
environment, not full CI. Publication remains gated; local changes have not
been committed, pushed or merged.

## Previous Follow-Up

The [final KOMODO inventory source pass](20261008-komodo-media-3000-3633/README.md)
reports **633 previously uncovered exact normalized paths**. It adds **226
concentration snippets and 38 identity-only mapping snippets** across **38
records**, plus 76 references and 38 curation events. Quantities, units,
formulations and organism associations are unchanged. Twenty source-pinned
withholdings exclude 158 initial candidate claims; those records remain
unresolved. Two water-input corrections are proposed separately, not applied.

The [then-current cumulative independent audit](20261008-diff-audit-after-komodo-3633.json)
verifies **5,105 distinct edited records, 30,297 new evidence entries, 5,420 new
references, 5,300 appended events and 1,365 quantity corrections**. Evidence
entries include identity and preparation claims, not just concentrations. The
[then-current coverage snapshot](20261008-followup-coverage-after-komodo-3633.json)
covers **11,743 of 15,910 normalized paths**, with **4,167** outside these
follow-up reports and unresolved claims inside reported records. No taxa-media
growth associations were added. Report coverage is not scientific completion.

Application, readback, no-op rerun, all 633 target schema checks, 279 focused
tests, full-corpus strict validation, IDs and variant links pass. The actual
[merge-retention check](20261008-komodo-media-3000-3633/merge-retention.json)
fails: fourteen records lose complete concentration evidence entries from their
canonical ingredient locations. Full citation validation fails on 38 API title
checks, while all 264 new snippets pass the installed text matcher. Product
validation passes with 91 warnings and 96,057 entries skipped for lack of an
adapter. Global merge and freshness checks fail. The fast suite passes 7,673
tests (16 skipped, 1,889 deselected); the 25 new cohort tests are included in the
focused count, not the fast tier. The terminal aggregate check verifies all 633
record hashes and reports, 13,521 report rows, 534 API captures and ten original
PDF captures. These checks ran in the partial locked Python 3.13 environment,
not full CI. Publication remains gated, and the local changes have not been
committed, pushed or merged.

## Previous Follow-Up

The [DSMZ 803/1046/1065 water-input repair](20261008-dsmz803-1046-1065-water/README.md)
corrects **nine already-reported records**, replacing incorrect mass/percentage
water encodings with the source-supported **1 L batch input**. It adds **18
evidence entries, nine references and nine curation events**. The nine reports
also retain 45 verified unchanged quantities and three unsupported legacy
placeholder rows; this does not resolve every claim in those records.

The [then-current cumulative independent audit](20261008-diff-audit-after-water-803.json)
verifies **5,067 distinct edited records, 30,033 new evidence entries, 5,344 new
references, 5,262 appended events and 1,365 quantity corrections**. Evidence
entries include identity and preparation claims, not just concentrations. The
[then-current coverage snapshot](20261008-followup-coverage-after-water-803.json)
covers **11,110 of 15,910 normalized paths**, with **4,800** outside these follow-up
reports and unresolved claims inside reported records. Report coverage is not
scientific completion. No taxa-media growth associations were added.

All nine schema checks, full-corpus strict validation and 107 focused tests pass.
The scoped merge-retention check passes for all six media and excludes the three
standalone solutions as expected. Full citation validation does not pass; the
PDF snippets were checked separately against actual PDF text. The fast suite
passes 7,673 tests (16 skipped, 1,864 deselected). Product validation succeeds
with 91 warnings and 96,057 entries skipped for lack of an adapter. The terminal
global merge check fails with 1,247 name conflicts and 3,287 fingerprint issues;
freshness also fails (3,720 tracked-only, 3,898 fresh-only and 1,700 changed shared
paths). The final source/hash/report check passes. These checks ran in the
partial locked Python 3.13 environment, not full CI. Publication remains gated;
the latest local edits have not been committed, pushed or merged.

## Previous Follow-Up

The [sixth KOMODO source pass](20261007-komodo-media-2500-3000/README.md)
reports **500 previously uncovered exact normalized paths**. It adds **250
concentration snippets and 43 identity-only mapping snippets** across **43
records**, plus 86 references and 43 curation events. Numeric values, units,
formulations and organism associations are unchanged. Eleven source-pinned
withholdings exclude 75 initially proposed claims; those records remain
unresolved. New mapping references use the verified captured page title.

The [then-current cumulative independent audit](20261007-diff-audit-after-komodo-3000.json)
verifies **5,067 distinct edited records, 30,015 new evidence entries, 5,335 new
references, 5,253 appended events and 1,356 quantity corrections**. Evidence
entries include identity and preparation claims, not just concentrations. The
[then-current coverage snapshot](20261007-followup-coverage-after-komodo-3000.json)
covers **11,110 of 15,910 normalized paths**, with **4,800** outside these follow-up
reports and unresolved claims inside reported records. Report coverage is not
scientific completion. No taxa-media growth associations were added.

The batch's [actual merge-retention check](20261007-komodo-media-2500-3000/merge-retention.json)
loses complete concentration evidence entries in eight records. Full citation
validation also fails on 43 API titles, despite all 293 new snippets passing the
installed text matcher. Publication remains gated; consult the batch's own
validation artifacts for complete results. Its three [water-input proposals](20261007-komodo-media-2500-3000/water-input-handoff.json)
were subsequently applied across nine linked records in the follow-up above;
the historical handoff and frozen cohort plan remain unchanged.
That batch's terminal checks pass 269 focused tests and 7,638 fast tests (16
skipped, 1,864 deselected), plus strict validation of all 15,910 normalized
records. These ran in the partial locked Python 3.13 environment, not full CI;
passing tests do not resolve the failed publication checks.

## Earlier Follow-Up

The [KOMODO 670 source-version follow-up](20261007-komodo670-source-versions/README.md)
curates four strain formulations and their parent links. It adds **55 evidence
entries, 19 references and five curation events**, with nine new quantity slots,
one stock-stage concentration rebase, and 22 unsupported/default quantity slots
withdrawn. Source batch masses remain in notes. The archived 2017 formulations
and four current-DSMZ alternatives are kept separate; source-version attribution,
unquantified amounts and ontology mapping gaps remain explicit.

The [then-current cumulative independent audit](20261007-diff-audit-after-komodo670-versions.json)
verifies **5,024 distinct edited records, 29,722 new evidence entries, 5,249 new
references, 5,210 appended events and 1,356 quantity corrections**. The
[then-current coverage snapshot](20261007-followup-coverage-after-komodo670-versions.json)
still covers **10,610 of 15,910 normalized paths**, with **5,300** outside these
reports and unresolved claims inside reported records. No taxa-media growth
associations were added. Publication and all-record completion remain unproven;
consult the batch's validation artifacts for gate results.

## Earlier Follow-Up

The [DSMZ 546/659/670 stock-stage repair](20261007-dsmz546-659-670-stocks/README.md)
corrects nine already-reported paths, including three previously unchanged
KOMODO records. It adds 57 evidence entries and six references, clarifies 30
existing evidence scopes, and appends nine curation events. Three water-unit
corrections, twelve stock concentration rebases, twelve ingredient relocations
and eighteen new quantity slots are distinct count categories.

The [then-current cumulative independent audit](20261007-diff-audit-after-dsmz-stock-stages.json)
verifies **5,020 distinct edited records, 29,667 new evidence entries, 5,230 new
references, 5,205 appended events and 1,356 quantity corrections**. The
[then-current coverage snapshot](20261007-followup-coverage-after-dsmz-stock-stages.json)
still covers **10,610 of 15,910 normalized paths**, with **5,300** outside these
reports and unresolved claims inside reported records. No taxa-media growth
associations were added. Publication and all-record completion remain unproven;
consult the batch's terminal validation artifacts for the gate results.

## Applied Batches

The initial quantity/evidence-only passes are listed first; the subsequent
structural correction is accounted separately below.

| Batch | Unique edited records | Quantity corrections | New evidence entries |
| --- | ---: | ---: | ---: |
| [JCM recipes](20261007-jcm/README.md) | 3 | 7 | 20 |
| [MediaDive stocks](20261007-mediadive-stocks/README.md) | 5 | 5 | 45 |
| [MediaDive solutions, first 500](20261007-mediadive-solutions-0000-0500/README.md) | 442 | 189 | 2,322 |
| [MediaDive solutions, records 500-999](20261007-mediadive-solutions-0500-1000/README.md) | 412 | 159 | 2,269 |
| [MediaDive solutions, records 1000-1499](20261007-mediadive-solutions-1000-1500/README.md) | 461 | 129 | 2,881 |
| [MediaDive solutions, records 1500-1999](20261007-mediadive-solutions-1500-2000/README.md) | 457 | 99 | 2,822 |
| [MediaDive solutions, records 2000-2499](20261007-mediadive-solutions-2000-2500/README.md) | 442 | 102 | 2,794 |
| [MediaDive solutions, records 2500-2999](20261007-mediadive-solutions-2500-3000/README.md) | 445 | 103 | 2,479 |
| [MediaDive solutions, records 3000-3499](20261007-mediadive-solutions-3000-3500/README.md) | 465 | 120 | 2,784 |
| [MediaDive solutions, records 3500-3999](20261007-mediadive-solutions-3500-4000/README.md) | 443 | 103 | 2,823 |
| [MediaDive solutions, records 4000-4499](20261007-mediadive-solutions-4000-4500/README.md) | 409 | 114 | 2,200 |
| [MediaDive solutions, records 4500-4769](20261007-mediadive-solutions-4500-4770/README.md) | 150 | 15 | 532 |
| [M1308 nested-stock follow-up](20261007-m1308-stock-followup/README.md) | 0 additional | 0 | 12 |
| Initial-pass total, distinct edited paths | 4,134 | 1,145 | 23,983 |

Those initial-pass totals were checked by [comparing normalized YAML against `HEAD`](20261007-diff-audit-after-4770.json),
not inferred from the number of reports. The 23,983 entries support 23,987 record-local
claims: 1,145 corrected quantities and 22,842 evidence-only claims. Five earlier stock
doses share one scoped recipe-level evidence entry. Source-duplicate records
are not independent scientific confirmations. No taxa-media associations were
added by these batches. The M1308 follow-up edits an already counted record;
it adds twelve stock claims, not a new unique reviewed or edited path.

The [DSMZ 1399 structural follow-up](20261007-dsmz1399-stock-boundary/README.md)
subsequently repaired two records, one already counted above. It relocates eight
ingredients into the correct stock, removes two unsupported iron concentration
encodings while preserving the source drop dose in notes, and adds three explicit
batch-volume amounts. Sixteen further evidence entries were added. The
[then-current independent diff audit](20261007-diff-audit-after-1399.json) verifies
**4,135 distinct edited records and 23,999 new evidence entries**, including
4,142 new references and 4,137 appended curation events. The original 1,145
quantity/unit corrections, two removals, three new quantities, and eight stock
relocations are separate categories, not interchangeable count units.

The [first receiving-medium source pass](20261007-mediadive-media-0000-0500/README.md)
adds 907 evidence entries to 160 further records, without changing numeric
amounts, chemical identities, stocks, or variants. It produces one result for
each of 500 exact paths, including the 340 unchanged records. Its scoped claims
are provider-declared main-recipe concentrations, not measurements of final
volume or evidence for other formulations. The [then-current independent diff audit](20261007-diff-audit-after-media-0500.json)
verifies **4,295 distinct edited records, 24,906 new evidence entries, 4,302 new
references, and 4,297 curation events**. The earlier quantity-correction and
structural-change counts are unchanged.

The subsequent [DSMZ 2 follow-up](20261007-dsmz2-stock-boundary/README.md) repairs
one previously unchanged receiving record: three ingredients moved into its
explicit base solution, two batch-volume fields added, two preparation texts
moved to the base, and one misleading preparation action corrected. Six new
evidence entries support eight scoped changes. The [then-current independent audit](20261007-diff-audit-after-dsmz2.json)
verifies **4,296 distinct edited records, 24,912 new evidence entries, 4,306 new
references, and 4,298 curation events**. Cumulative structural counts are eleven
ingredient relocations, five new quantity slots, two unsupported quantity-slot
removals, two preparation-text relocations, and one action correction. These are
separate categories from the unchanged 1,145 earlier quantity/unit corrections.

The [seven-record stock-boundary batch](20261007-medium-stock-boundaries/README.md)
subsequently repairs DSMZ 79, 98, 129, 260, 261, 369, and 452. It relocates
44 ingredients, adds 23 explicit batch-volume fields, and moves three stock
preparation texts. There are 100 new evidence entries for 105 scoped changes;
existing numeric concentrations are unchanged. The [then-current independent audit](20261007-diff-audit-after-stock-boundaries.json)
verifies **4,303 distinct edited records, 25,012 new evidence entries, 4,326 new
references, and 4,305 curation events**. Cumulative structural counts are
55 ingredient relocations, 28 new quantity slots, two unsupported quantity-slot
removals, five preparation-text relocations, and one action correction. The
1,145 earlier quantity/unit corrections remain a separate category.

The [DSMZ 13 follow-up](20261007-dsmz13-stock-only/README.md) restores its two
stocks without inventing direct ingredients: seven relocations, four explicit
batch-volume fields, and one preparation-stage move. Ten evidence entries support
twelve scoped changes. The [then-current independent audit](20261007-diff-audit-after-dsmz13.json)
verifies **4,304 distinct edited records, 25,022 new evidence entries, 4,328 new
references, and 4,306 curation events**. Cumulative structural counts are
62 ingredient relocations, 32 new quantity slots, two unsupported quantity-slot
removals, six preparation-text relocations, and one action correction, separate
from the unchanged 1,145 quantity/unit corrections.

The associated fingerprint fix now traverses nested stock compositions and
supports stock-only media with explicit valid constituents. Its full-corpus
before-curation comparison made 32 previously skipped records fingerprintable
and corrected six fingerprints that omitted nested constituents. These are
pipeline changes, not additional source reviews or evidence-backed data edits;
concentration-independent fingerprints still do not establish exact formulations.

The [second receiving-medium pass](20261007-mediadive-media-0500-1000/README.md)
adds 653 evidence entries across 117 further records and reports all 500 selected
paths, including 383 unchanged records. It makes no numeric or ingredient-identity
changes. The [then-current independent semantic diff](20261007-diff-audit-after-media-1000.json)
verifies **4,421 distinct edited records, 25,675 new evidence entries, 4,445 new
references, and 4,423 curation events**. All earlier quantity and structural
counts are unchanged. Evidence-entry totals are not counts of scientifically
resolved claims; the DSMZ 12 scope error is corrected by the follow-up below.

The [extraction-boundary follow-up](20261007-extraction-boundaries/README.md)
repairs DSMZ 12 and 657 without adding new unique reviewed paths. Four input
nodes move into extraction preparations; two initial-water quantities are
corrected, two unsupported soil/manure concentration slots removed, and one
source-explicit prepared-extract amount added. Starting solid masses remain
in notes. Three existing evidence scopes are corrected, including explicit
withdrawal of the earlier soil-concentration interpretation. Five new evidence
entries, two references, and two curation events support the repairs.
The [then-current independent semantic diff](20261007-diff-audit-after-extraction.json)
verifies **4,421 distinct edited records, 25,680 new evidence entries, 4,447
new references, and 4,425 curation events**. Cumulative quantity/unit corrections
are **1,147**, separate from 66 ingredient relocations, 33 new quantity slots,
four unsupported quantity-slot removals, and the preparation changes.

The [KOMODO 12 extraction repair](20261007-komodo12-extraction/README.md) adds one
new exact-path review and corrected record. The verified official KOMODO row
links the original DSMZ 12 recipe; the recipe, not the mapping table or another
local YAML, supports its quantities and preparation. Two inputs move into an
extraction preparation, one water quantity is corrected, and one unsupported
soil-concentration slot is removed while retaining the input mass in notes.
Five evidence entries, three references, and one curation event are added.
The [then-current independent semantic diff](20261007-diff-audit-after-komodo12.json)
verifies **4,422 distinct edited records, 25,685 new evidence entries, 4,450
new references, and 4,426 curation events**. Cumulative quantity/unit corrections
are **1,148**, separate from 68 ingredient relocations, 33 new quantity slots,
five unsupported quantity removals, and preparation changes. Duplicate-source
evidence entries are not independent scientific confirmations.

The [third receiving-medium pass](20261007-mediadive-media-1000-1500/README.md)
reports all 500 selected paths and adds 869 evidence entries to 142 records,
with 358 unchanged. It makes no numerical, chemical-identity, stock, variant,
or growth-association changes. The [then-current independent semantic diff](20261007-diff-audit-after-media-1500.json)
verifies **4,564 distinct edited records, 26,554 new evidence entries, 4,592
new references, and 4,568 curation events**. Earlier quantity and structural
counts are unchanged. An adversarial preparation review withheld seven proposed
claims across DSMZ 1076b and 1293 before applying; their mutually exclusive
ingredients and stock-to-medium preparation basis remain unresolved. Eleven
new guard regression cases cover these errors and nonexclusive controls.

The [fourth receiving-medium pass](20261007-mediadive-media-1500-2000/README.md)
reports all 500 selected paths and adds 551 evidence entries to 86 records,
with 414 unchanged. It makes no numerical, chemical-identity, stock, variant,
or growth-association changes. The [then-current independent semantic diff](20261007-diff-audit-after-media-2000.json)
verifies **4,650 distinct edited records, 27,105 new evidence entries, 4,678
new references, and 4,654 curation events**. Earlier quantity and structural
counts are unchanged. Original-recipe review withheld 23 preliminary claims
across DSMZ 1431, 1462, 1624, and 1641 for physical-state, stock-volume, and
possible duplicate-ingredient conflicts. Thirteen new guard regression cases
cover those errors and relevant controls. All 419 previously accepted medium
records were checked for the new guard conditions, with zero hits.

The [fifth receiving-medium pass](20261007-mediadive-media-2000-2500/README.md)
reports all 500 selected paths and adds 492 evidence entries to 107 records,
with 393 unchanged. It extends exact-source matching to JCM without treating
DSMZ, the dataset provider, as the original recipe collection. No numeric,
ingredient-identity, stock, variant, or growth-association change is made.
The [then-current independent semantic diff](20261007-diff-audit-after-media-2500.json)
verifies **4,757 distinct edited records, 27,597 new evidence entries, 4,785
new references, and 4,761 curation events**. Earlier quantity and structural
counts are unchanged. Manual preparation review withheld 151 preliminary
claims across 24 records; source-pinned vetoes are frozen into the plan and
cannot authorize amounts. Two partially supported records retain evidence for
their unambiguous rows. Withholding does not repair the unresolved formulations.

The [sixth receiving-medium pass](20261007-mediadive-media-2500-3000/README.md)
reports all 500 selected JCM paths and adds 223 evidence entries to 50 records,
with 450 unchanged. It makes no numerical, unit, chemical-identity, stock,
variant, or growth-association changes. The [then-current independent semantic diff](20261007-diff-audit-after-media-3000.json)
verifies **4,807 distinct edited records, 27,820 new evidence entries, 4,835
new references, and 4,811 curation events**. Earlier quantity and structural
counts are unchanged, including 1,148 quantity/unit corrections. Source review
withheld 135 preliminary claims across 18 whole records for omitted stocks,
fractional-volume rounding, extraction, and other preparation conflicts.
Those formulations still need scientific repairs; withholding is not resolution.

The [JCM 896 original-source follow-up](20261007-jcm896-final-volume/README.md)
repairs one previously unchanged record. It corrects ten mass concentrations
using the explicit 584 ml final volume, corrects serum to volume per liter,
restores the TC Yeastolate product label, and fixes the filtration symbol.
Twelve evidence entries support thirteen scoped changes. The [then-current independent semantic diff](20261007-diff-audit-after-jcm896.json)
verifies **4,808 distinct edited records, 27,832 new evidence entries, 4,836
new references, and 4,812 curation events**. Quantity/unit corrections now total
**1,159**; the label and text-encoding corrections are separately counted.
Historical cohort findings remain intact and are linked to the explicit successor.

The [seventh receiving-medium pass](20261007-mediadive-media-3000-3319/README.md)
reports all 319 selected JCM paths and adds 192 evidence entries to 37 records,
with 282 unchanged. It makes no numerical, unit, chemical-identity, stock,
variant, or growth-claim changes. The [then-current independent semantic diff](20261007-diff-audit-after-media-3319.json)
verifies **4,845 distinct edited records, 28,024 new evidence entries, 4,873
new references, and 4,849 curation events**. Quantity/unit corrections remain
**1,159**. Source review withheld 47 preliminary claims across nine records,
six whole and three partial. Existing stock-dose and variant-annotation conflicts
remain explicit follow-ups, not newly supported formulations.

The [JCM 1105 original-source follow-up](20261007-jcm1105-stock-boundary/README.md)
repairs one previously unchanged record. Five concentrations now use the
source-explicit one-liter base; the separately autoclaved carbonate stock and
its batch dose are represented separately, without inventing a percentage basis
or final receiving volume. Seven evidence entries support eleven scoped claims.
The [then-current independent semantic diff](20261007-diff-audit-after-jcm1105.json)
verifies **4,846 distinct edited records, 28,031 new evidence entries, 4,874
new references, and 4,850 curation events**. Quantity/unit corrections total
**1,164**, separately from 74 ingredient relocations, 35 new quantity slots,
and six unsupported quantity-slot removals.

The [percent-supplement follow-up](20261007-percent-supplements/README.md) repairs
DSMZ 618/956, two KOMODO wrappers, and the existing methylamine-specific record.
It adds 43 evidence entries for 48 scoped claims, withdraws seven earlier
concentration-evidence interpretations, and removes 31 unsupported mass-rate
slots while preserving all source batch masses and percentages in scoped notes
or variants. It adds five starting-water amounts, not final-volume claims.
The [then-current independent semantic diff](20261007-diff-audit-after-percent-supplements.json)
verifies **4,849 distinct edited records, 28,074 new evidence entries, 4,882
new references, and 4,855 curation events**. Quantity/unit corrections remain
**1,164**; cumulative ingredient relocations are 97, new quantity slots 40,
and unsupported quantity-slot removals 37. Four inline option entries describe
two exclusive formulations in two source wrappers, not four independent media.
The existing methylamine variant is reused and linked; no new ID or growth
association was created.

The [public direct-ingredient follow-up](20261007-public-direct/README.md) adds
17 evidence entries supporting eleven existing concentrations in King B (P3)
and mTA10 (P6), with no numeric or formulation changes. Both user-contributed
dataset pages were inspected; the six mTA10 concentrations also have independent
DOI-backed methods snippets from the 2020 article. The
[then-current independent semantic diff](20261007-diff-audit-after-public-direct.json)
verifies **4,851 distinct edited records, 28,091 new evidence entries, 4,885
new references, and 4,857 curation events**. Quantity/unit corrections remain
**1,164**; the preceding structural counts are unchanged. No taxa-media
association was added.

The [public stock follow-up](20261007-public-stocks/README.md) adds 37 evidence
entries across P2 and P8, including one explicit counterevidence entry. P2's
existing quantities are unchanged and its haemin-stock makeup water is restored
without a fixed amount. P8's original article supports a 51-to-15 g/L phosphate
stock correction and four stock-dose changes from unsupported per-liter rates
to explicit batch volumes. Its conflicting dataset row is preserved. The
[then-current independent semantic diff](20261007-diff-audit-after-public-stocks.json)
verifies **4,853 distinct edited records, 28,128 new evidence entries, 4,887
new references, and 4,859 curation events**. Quantity/unit corrections total
**1,169**, including the four stock-dose basis corrections. One existing DOI
citation was normalized/enriched, separately from the added references; one
unquantified makeup node was added, separately from numeric quantity slots.
All preceding relocation and quantity-slot counts are unchanged.

The [public input-basis follow-up](20261007-public-input-basis/README.md) adds
39 evidence entries across P7 and P10. It corrects four liquid additions to
source-explicit batch volumes, removes three unsupported quantity assertions,
and restores five water nodes (four quantified batch inputs and one unquantified
solvent). Twenty-nine existing dataset-reported rates are retained with scoped
evidence, not promoted to measured final-medium concentrations. The
[then-current independent semantic diff](20261007-diff-audit-after-public-input-basis.json)
verifies **4,855 distinct edited records, 28,167 new evidence entries, 4,889
new references, and 4,861 curation events**. Quantity/unit corrections total
**1,173**, separate from **44 new quantity slots** and **40 unsupported slot
removals**. The seven cumulative stock-dose basis corrections are a subset of
quantity corrections, not an additional total. Percentage bases, final-volume
ambiguities and P10's trace dose remain explicit; no growth association was added.

The [RS stock-boundary follow-up](20261007-rs-stock-boundaries/README.md) repairs
P4 and P5 with 155 new evidence entries. It restores 60 source stock descriptors,
relocates 77 ingredient nodes and rebases 76 concentrations to stock stages;
these rebases are not corrections of numerically wrong final contributions.
It adds 59 stock-dose slots, moves one existing TiCl3 dose to its stock, corrects
five mix-dose bases, and removes eight unsupported quantities. Fifty-nine
unquantified carrier/water nodes retain the source preparation context. P5's
D-Mannose/L-mannose and D-Xylose/Xylan conflicts remain explicit and unquantified.
The [then-current independent semantic diff](20261007-diff-audit-after-rs-stock-boundaries.json)
verifies **4,857 distinct edited records, 28,322 new evidence entries, 4,891 new
references, and 4,863 curation events**. Cumulative quantity/unit corrections are
**1,178**, including twelve stock-dose basis corrections, separate from 174
ingredient relocations, 103 new quantity slots, 48 unsupported slot removals and
the 76 stock-stage rebases. No taxa-media association was added.

The [first KOMODO source pass](20261007-komodo-media-0000-0500/README.md) reports
all 500 selected exact paths, with 25 changed and 475 unchanged. It adds 137
ingredient concentration evidence entries and 25 separate identity-mapping
entries, without changing any quantity or formulation. The inspected mapping
does not authorize base amounts for the 423 variant accessions in this batch.
Three preliminary candidates were withheld for formulation/pH differences;
one mapped amount endpoint returns HTTP 404. The [then-current independent semantic diff](20261007-diff-audit-after-komodo-0500.json)
verifies **4,882 distinct edited records, 28,484 new evidence entries, 4,941 new
references, and 4,888 curation events**. Quantity/unit corrections remain
**1,178**; all preceding structural counts are unchanged. Duplicate-source
entries are not independent confirmations, and no growth association was added.

The [second KOMODO source pass](20261007-komodo-media-0500-1000/README.md) reports
another 500 exact paths, with 24 changed and 476 unchanged. It adds 141
ingredient concentration entries and 24 separate identity-mapping entries,
without changing any quantity or formulation. Source evidence is not propagated
to its 378 variant accessions. Three inspected candidates are withheld for
preparation/variant/pH conflicts; nine mapped endpoints return HTTP 404, affecting
eleven paths. The [then-current independent semantic diff](20261007-diff-audit-after-komodo-1000.json)
verifies **4,906 distinct edited records, 28,649 new evidence entries, 4,989 new
references, and 4,912 curation events**. Quantity/unit corrections remain
**1,178**; preceding structural counts are unchanged. The linked prior-cohort
handoff explicitly identifies unresolved preparation scope in earlier DSMZ
111, 125 and 187 evidence-only results. No growth association was added.

The [medium 111 preparation follow-up](20261007-dsmz111-preparation/README.md)
repairs three previously reviewed records, preserving their source snippets and
chemical mappings. It separates glucose sterilization, withdraws three wrongly
staged rates, represents supported water inputs, and corrects the standalone
water unit. The [then-current independent semantic diff](20261007-diff-audit-after-dsmz111.json)
verifies **4,907 distinct edited records, 28,669 new evidence entries, 4,994 new
references, and 4,915 curation events**. It counts **1,179 quantity/unit
corrections**, separate from 177 stock relocations, 108 new quantity slots and
51 unsupported quantity slots removed. Final glucose stock and medium volumes
remain unresolved; these counts do not imply scientific completeness.

The [medium 125 alternatives follow-up](20261007-dsmz125-alternatives/README.md)
repairs the DSMZ and exact KOMODO medium records and standalone solution 223.
It represents methanol addition and methane-air incubation as separate options,
preserves all 36 basal amounts and 24 existing ingredient evidence entries,
and restores source-supported water inputs. Its independent applied audit
verifies 23 new evidence entries, five references, three curation events,
one water-unit correction, two new quantity slots and four inline options.
The three separately inspected strain-modified records remain unchanged;
neither their exact formulations nor final liquid concentrations are inferred.
The full all-record objective and the publication workflow remain unfinished.

The [third KOMODO source pass](20261007-komodo-media-1000-1500/README.md) reports
another 500 exact paths, with 46 changed and 454 unchanged. It adds 264 ingredient
concentration entries and 46 separate identity-mapping entries, without changing
any quantity or formulation. Evidence is not propagated to its 273 strain/variant
accessions. Fifteen source-pinned preparation/formulation withholdings veto 97
preliminary endorsements; 34 actual unavailable endpoints affect 40 paths.
The linked prior-cohort handoff reopens preparation scope for fifteen earlier
DSMZ records without rewriting those records or their historical reports.
No growth association was added.

The [medium 265 preparation follow-up](20261007-dsmz265-preparations/README.md)
repairs the DSMZ and exact KOMODO medium records and standalone solution 531.
It separates the mineral base, yeast-extract, sucrose, sulfide and lipid
preparations, restores explicit batch additions and corrects the standalone
water unit. The original recipe supports 20 ml of 10% w/v yeast extract,
not the API's conflicting 20 mg/l. The independent applied audit verifies
50 new evidence entries, five references and three curation events, with all
historical snippets preserved. The original lipid dose remains a 6-12 ml range;
neither its composition nor final base/receiving-medium volumes are inferred.
Retained basal rates are scoped provider normalizations, not independently
verified final concentrations. No growth association or unique reviewed path
was added, and the all-record objective remains unfinished.

The [fourth KOMODO source pass](20261007-komodo-media-1500-2000/README.md) reports
another 500 exact paths, with six changed and 494 unchanged. It adds 25
ingredient concentration entries and six separate identity-mapping entries,
without changing any quantity or formulation. Original DSMZ recipe PDFs were
cross-checked for all eight preliminary candidates. Two preparation-stage
withholdings veto fifteen preliminary endorsements; seven actual unavailable
API endpoints affect eight paths. Its prior-cohort handoff identifies two
earlier DSMZ records with fifteen same-source entries needing scope review.
The separately inspected exact KOMODO 457_7098 page demonstrates that variant
sources can be accessible even when base-recipe evidence is insufficient.
No evidence is propagated to the cohort's 414 variant accessions, and no
growth association is added.

The [media 467/469 input follow-up](20261007-dsmz467-469-inputs/README.md)
repairs six exact source copies. It corrects four water-unit fields, restores
six separately filtered ingredient nodes, withdraws six unsupported stock-rate
fields and adds eight source-explicit water inputs. Thirty new evidence entries,
eight references and six append-only curation events support these changes.
The API's 980/10/10 ml allocation for medium 469 is explicitly distinguished
from the original PDF's unpartitioned 1000 ml. Stock strengths, numeric stock
doses and measured final volumes remain unasserted. The historical reports and
snippets are preserved through explicit hash-linked follow-ups; no unique
reviewed path or growth association is added. Wider post-edit verification is
recorded separately in the new batch's validation journal.

The [medium 489 follow-up](20261007-dsmz489-stocks/README.md) now repairs three
further exact source copies: separate resazurin strength/dose, post-sterilization
reducing stocks, and water-input units. Its independent applied inversion checks
23 new evidence entries, five references and three append-only events, with
nine ingredient relocations, three stock-stage rebases, six unsupported rate
removals, one water-unit correction and five added volume fields. Reducer stock
strengths, solvent and dose volumes remain unknown. The guarded readback passes
and reapplication changes nothing; the terminal validation results are recorded
below. The all-record objective remains unfinished.

The [pH-7.0 water follow-up](20261007-solutions-water-ph7/README.md) has applied
52 source-explicit water-input corrections, each with a persistent source URL,
literal snippet, conversion and appended curation event. The 18 other candidates
in this preparation group remain unchanged. All 210 selected baseline and
post-edit tests pass; all 52 new snippets also pass the installed deterministic
URL-content validator. Its separate full-reference check fails on the API
title fallback and is not counted as a pass. The batch's terminal post journal
records full strict/ID gates, all ten earlier solution-batch read-backs, exact
water-source verification and a zero-change rerun. The expanded Python 3.13
environment also completes the ontology-product gate with 91 non-blocking
warnings, superseding the older missing-`oaklib` limitation. That environment
deliberately excludes five visualization packages, so it is not full project CI;
its [terminal runtime journal](20261007-solutions-water-ph7/expanded-runtime-validation.json)
records `just test-fast` passing with 7,490 passed, 16 skipped and 1,710
deselected. The separate reference-title validation failure remains unresolved.

The [other pH-adjustment water follow-up](20261007-solutions-water-ph-adjustments/README.md)
has applied 107 further literal water-input corrections, with 107 evidence
entries, 107 append-only events and two new references. The independent
saved-record inversion verifies every unrelated field is preserved and all 51
deferred candidates are unchanged. Baseline and post-edit regression suites
each pass 339 tests. All 107 new snippets pass the installed deterministic
URL-content matcher; the separate reference-title gate still fails on the
dataset API's URL-as-title fallback. The terminal results of the wider run are
recorded in the batch's post-validation journal: 23 of 24 commands pass,
including `just test-fast` with 7,491 passed, 16 skipped and 1,839 deselected.
The separate reference-title failure remains open. This uses the same partial
locked Python 3.13 environment described above, not full project CI. The final
saved-record inversion confirms all 107 results and 51 deferred hashes again.

The [water-follow-up semantic diff](20261007-diff-audit-after-water-ph-adjustments.json)
verifies **4,968 distinct edited records, 29,295 new evidence entries, 5,126 new
references and 5,141 curation events**. There are **1,345 quantity/unit
corrections**, separate from 241 stock relocations, 137 new quantity slots and
69 unsupported quantity slots removed. The audit separately counts 88
stock-stage concentration rebases; the three medium-265 yeast conflict repairs
overlap that category and must not be added to it as independent changes.

The [water-follow-up coverage snapshot](20261007-followup-coverage-after-water-ph-adjustments.json)
has per-record results for 10,110 exact tracked paths: 4,968 changed and
5,142 unchanged when reconciled with the semantic diff. The
[readback summary](20261007-solutions-water-ph-adjustments/post-readbacks-summary.json)
checks this exact-path partition and confirms all ten original solution batches
still retain their 23,902 supported snippets across 4,770 records, through 166
explicit successor hashes. Four withdrawn quantity claims retain their historical
snippets separately. These are unique-path counts; explicit later follow-ups can
revisit an earlier reviewed record without adding another unique path. Processed does not
mean fully verified. In the historical ten solution source-review snapshots,
18,331 claim rows remain unsupported and 1,380 conflicted, including legacy
placeholders and source-only stock references. No concentration slots were newly
filled in those ten batches; their edits are quantity corrections or evidence
for already-present values.
The DSMZ 1399 follow-up resolves one formerly unsupported standalone iron row
through notes and evidence; historical first-pass rows are not overwritten.

The [fifth KOMODO cohort](20261007-komodo-media-2000-2500/README.md) now reports
500 further exact paths, with 46 changed and 454 unchanged. Complete inspection
of its 69 preliminary candidates withheld 155 proposed concentration claims
across 23 records for stock, supplement, extraction and conflicting-source
contexts. The guarded application adds 220 concentration snippets and 46
identity-only mapping entries, 92 references and 46 curation events. It changes
no quantities, chemical identities, stocks, variants or growth associations.
The independent inversion, read-back, no-op rerun, all-target schema check,
246 selected tests, full strict corpus gate and ID gate pass. Separate merge
retention fails: 198/220 amount quotes and 184/220 complete evidence entries
survive the actual current merge groups. Do not publish these as fully retained
canonical evidence; the normalized records remain authoritative.
Product validation passes with 91 non-blocking warnings and 96,044 no-adapter
skips. All 266 new snippets pass the installed deterministic URL matcher against
retrieved/cached content. The full reference gate nevertheless fails: API
URL-as-title fallback mismatches, a source-confirmed KOMODO descriptive-versus-HTML
title discrepancy, and fetch errors are separately documented. The
[bibliographic correction handoff](20261007-komodo-media-2000-2500/reference-title-handoff.json)
remains open; snippet success does not override that failure.

The [then-current independent semantic diff](20261007-diff-audit-after-komodo-2500.json)
verifies **5,014 distinct edited records, 29,561 new evidence entries, 5,218 new
references and 5,187 curation events**. Quantity and structural counts above are
unchanged, including 1,345 quantity/unit corrections. The [then-current coverage](20261007-followup-coverage-after-komodo-2500.json)
and [report-contract check](20261007-komodo-media-2000-2500/report-contract.json)
reconcile **10,610 unique reported paths: 5,014 changed and 5,596 unchanged**,
with **5,300** still outside these follow-up reports. Reports with unresolved
claims are not scientific completion. All-record work remains active.

The [KOMODO 650/752/762 preparation follow-up](20261007-komodo650-752-762-preparations/README.md)
subsequently corrects three previously unchanged reported records. It restores
source-explicit pyruvate molarity, metal-stock strengths and doses, batch-water
units, and separate carbonate preparation, without inventing final volumes.
Twenty-nine new evidence entries support the changes, with six references and
three append-only events. The [then-current independent semantic diff](20261007-diff-audit-after-komodo-preparations.json)
verifies **5,017 distinct edited records, 29,590 new evidence entries, 5,224
references and 5,190 curation events**. Counts now include **1,347 quantity/unit
corrections**, 245 ingredient relocations, 142 new quantity slots, 71 unsupported
quantity-slot withdrawals, and 90 stock-stage concentration rebases. These are
separate categories. The [then-current coverage](20261007-followup-coverage-after-komodo-preparations.json)
remains **10,610 unique reported paths**, with **5,300** outside follow-up reports.
The related DSMZ and standalone-solution records required their own corrections,
now applied in the follow-up below; neither historical duplicate links nor
generated merge retention is assumed valid.
All three specific repaired formulations and their evidence survive their actual
merge groups. Final fast tests pass (7,514 passed, 16 skipped), as do source
readback and all 29 snippet checks. Full reference validation still fails on
three API URL-as-title fallback mismatches; global merge and freshness checks
also fail. See the follow-up's adversarial review for limits and terminal results.

The [DSMZ/standalone 650/752/762 follow-up](20261007-dsmz650-752-762-preparations/README.md)
corrects those six already edited records with twenty new evidence entries and
32 clarified earlier evidence scopes. All previous excerpts are retained; four
carbonate concentration claims are explicitly withdrawn at the separate-stock
stage. It adds six events and no references, with six quantity corrections,
four stock-stage concentration rebases, eight relocations and eight new quantity
slots. The [current cumulative audit](20261007-diff-audit-after-dsmz-preparations.json)
verifies **5,017 distinct edited records, 29,610 new evidence entries, 5,224
references and 5,196 events**, including **1,353 quantity corrections**.
The [current coverage](20261007-followup-coverage-after-dsmz-preparations.json)
remains **10,610 reported paths**, with **5,300** outside these reports. The
independent inversion, source readback, no-op, six schema checks, strict corpus
and ID gates, and three affected historical cohorts pass. All 52 snippets match;
six full reference checks still fail API-title fallback comparisons. Actual-group
retention fails for all three DSMZ media, while the standalone solutions pass
exclusion/routing checks. Post-edit focused tests pass 264/264 and the fast suite
passes **7,557 tests** (16 skipped). Product validation passes after an authorized
FoodOn-cache retry, with 91 warnings and 96,051 no-adapter skips; its initial
sandbox failure remains recorded. Global merge verification fails with 1,247
name conflicts and 3,287 fingerprint issues. Freshness also fails (6,320 tracked
versus 6,495 fresh files). All runs are terminal and journaled in the batch;
this does not establish publication readiness or completion of the full goal.

Every changed quantity has an inspected source DOI or persistent recipe URL and
exact source snippet in its YAML, with claim scope and conversion explanation. Stable IDs,
prior evidence snippets, and prior history were preserved. These changes remain local and
uncommitted; no PR/merge is asserted for this curation work.

## Remaining Work

- Review the [remaining standalone water-unit candidates](20261007-remaining-water-preparation-inventory.json).
  This read-only, hash-checked inventory identifies 2,710 potential legacy
  percentage errors across 2,233 exact preparation groups. The largest groups
  are simple pH-only instructions (70 at pH 7.0; 35 at pH 7.2). These are
  candidates, not newly reviewed paths or approved amounts. Inspect complete
  sources/current records, make-up-volume context and source conflicts before
  producing a guarded apply plan. The existing blanket preparation guard has
  not been relaxed. This larger cohort can advance the remaining corrections
  without repeatedly treating every simple water input as a one-medium task.
  The 52 matching flat records in the 70-record pH-7.0 group now have applied
  water corrections; the other 18 remain deferred, with stock rows and
  preparation mismatches overlapping. The [reconciled handoff](20261007-solutions-water-ph7/remaining-handoff.json)
  verifies **2,658** remaining unchanged water candidates from this frozen
  inventory and records three additional glycerol-unit leads. Those leads are
  not approved quantities or completed reviews.
  The [next reconciled handoff](20261007-solutions-water-ph-adjustments/remaining-handoff.json)
  verifies another 107 applied corrections, leaving **2,551** unchanged water
  candidates. It records 14 non-water leads, including seven liquid inputs,
  three agar conflicts and four stock/preparation or alternative-substrate
  findings. The [original agar source investigation](20261007-solutions-water-ph-adjustments/agar-original-source-handoff.md)
  supports literal batch inputs but does not establish final concentrations.

- Resolve medium evidence-retention failures before publishing regenerated
  media. The [standalone-solution routing repair](20261007-solution-merge-routing/README.md)
  now excludes all 4,785 standalone roots from medium matching without changing
  normalized data, and blocks direct merge bypasses. Its current corpus audit
  still detects loss of the DSMZ medium 111 copy's ingredient/stock evidence,
  notes, references and history. The [partial-signature defect](20261007-dsmz111-preparation/fingerprint-impact.json)
  was a pipeline error, not a reason to remove the supported stock boundary.
- Prioritize the [prior-cohort preparation findings](20261007-komodo-media-0500-1000/prior-cohort-followup.md)
  for DSMZ/KOMODO 187: conflicting pH instructions remain unresolved. The
  [medium 125 follow-up](20261007-dsmz125-alternatives/README.md) now represents
  alternative carbon sources, but final concentrations and exact strain-modified
  formulations remain unverified. The [medium 111 follow-up](20261007-dsmz111-preparation/README.md)
  repairs glucose-stock staging and water input bases in both media and solution
  190; final stock and medium volumes remain unverified. Earlier amount snippets
  are not proof that these recipes are scientifically complete.
- Resolve the [KOMODO source-scope findings](20261007-komodo-media-0000-0500/preparation-findings.md):
  reduced-medium and pH mismatches, liquid doses encoded as mass rates, omitted
  stock/extraction boundaries, the unavailable DSMZ 72 source, and exact variant
  evidence. An unchanged result does not resolve the underlying formulation.
- Resolve the [third KOMODO pass's preparation findings](20261007-komodo-media-1000-1500/preparation-findings.md):
  fifteen whole-record withholdings cover missing supplements, stock/extraction
  boundaries, alternative substrates, inconsistent volume bases and source
  conflicts. Its [prior-cohort handoff](20261007-komodo-media-1000-1500/prior-cohort-handoff.json)
  pins fifteen unchanged earlier DSMZ records with 97 same-source ingredient
  entries requiring scope reassessment. Withholding does not automatically
  disprove every basal amount or repair a formulation. Original 425/426 recipes
  also disagree with the API's agar amount; those agar claims remain unsupported.
  The [medium 265 successor](20261007-dsmz265-preparations/README.md) now repairs
  stock staging, batch doses and the yeast amount conflict in three copies;
  basal/final-volume and lipid-composition/source-version questions remain open.
  The historical handoff is preserved, not silently rewritten as resolved.
- Resolve the [fourth KOMODO pass's findings](20261007-komodo-media-1500-2000/preparation-findings.md):
  exact variant reconstruction and remaining preparation uncertainties.
  The [489 successor](20261007-dsmz489-stocks/README.md) now represents its
  resazurin and anoxic reducing stocks; reducer strengths/dose volumes and
  resazurin chemical grounding remain explicitly unverified.
  The [467/469 successor](20261007-dsmz467-469-inputs/README.md) now repairs
  medium 467's tap-water units and represents medium 469's filtered preparations
  with its API/PDF water-detail difference explicit. It does not establish
  final stock strengths or final-medium concentrations. The inspected 457_7098 source
  differs from the local record, while original 457 separates reactivation
  media from mineral-medium cultivation. The legacy resolver's suffix-collapsing
  and unchecked base-copy rules need a separate guarded repair, not reuse as
  evidence of variant identity. Neither the importer nor these unresolved
  formulations was repaired by the evidence-only batch.
- Review other extraction recipes and source-duplicate records independently.
  The [DSMZ 12 scope finding](20261007-mediadive-media-0500-1000/extraction-scope-finding.md)
  and DSMZ 657 extraction boundary are now repaired. The earlier literal-snippet
  and hash checks did not detect that scientific-scope error. No extraction
  yield or unspecified recovered volume is inferred. The subsequent KOMODO 12
  repair verifies that exact source mapping and brings its ingredients and
  preparation into agreement with the original recipe. The
  [earlier merge-retention failure](20261007-extraction-boundaries/merge-retention.json)
  remains a historical snapshot, not a claim about the newly corrected pair.
  Other source-duplicate records need their own exact-source review.
- Complete source-specific review and supported corrections across all records,
  including direct ingredients, standalone and nested stocks, and variants.
- Resolve the remaining [seventh-pass source-scope findings](20261007-mediadive-media-3000-3319/preparation-findings.md),
  including J1249's missing acid addition, J1264's
  rounded liquid volume, and three partial ingredient withholdings. Reconcile
  the separately identified stock-dose/mass-unit variant comparisons against
  both exact source recipes. Withholding does not repair the underlying records.
  J1105's omitted base volume now has an explicit original-source repair;
  its historical first-pass report and withholding remain unchanged.
- Resolve the [sixth pass's 18 source-scope findings](20261007-mediadive-media-2500-3000/preparation-findings.md),
  including rounded-away fractional liquid volumes and missing stock additions.
  JCM 896 is now repaired through its [original-source successor](20261007-jcm896-final-volume/README.md);
  the other seventeen whole-record withholdings remain unresolved. The original
  handoff and first-pass report are preserved rather than rewritten.
- Resolve the [fifth pass's 24 source-scope findings](20261007-mediadive-media-2000-2500/preparation-findings.md),
  including omitted supplements, extraction boundaries, alternative substrates,
  and stock solvent/volume ambiguity. The [original-source follow-up](20261007-mediadive-media-2000-2500/earlier-preparation-handoff.json)
  identified seven previously supported DSMZ 618/956 claims requiring scope
  reassessment and three legacy percent-to-g/L encodings without a verified
  percentage basis. Those claims now have the explicit
  [five-record successor](20261007-percent-supplements/README.md), including
  source-verified KOMODO wrappers and the existing methylamine branch. Original
  histories and cohort reports are unchanged. Percent bases and final-volume
  concentrations remain unquantified rather than guessed.
- Resolve the [fourth medium pass's source-scope findings](20261007-mediadive-media-1500-2000/preparation-findings.md).
  DSMZ 1431 and 1462 need liquid/agar distinctions; DSMZ 1624 requires complete
  stock and volume-basis representation; DSMZ 1641 repeats pyruvate under two
  names in the original table. All four remain unchanged, not scientifically
  repaired by the new guards. Review the separately identified DSMZ 550
  mixture-versus-agar ontology mapping without equating the two source rows.
- Continue collection-specific CCAP/JCM curation.
  The [CCAP S77 handoff](20261007-mediadive-media-1500-2000/ccap-s77-handoff.md)
  verifies the original PDF and identifies missing ingredients in both normalized
  copies. The MediaDive API is a placeholder for that record, not usable amount
  evidence. Neither copy has been repaired. The bacterial C102 copy now has an
  unchanged result in the fifth pass; that report does not resolve its missing
  ingredients or replace the original-source handoff.
- Resolve the [third medium pass's preparation-scope findings](20261007-mediadive-media-1000-1500/preparation-findings.md).
  DSMZ 1076b must not combine mutually exclusive energy-source branches; DSMZ
  1293 needs reconciliation of table amounts and its explicit stock-to-medium
  mixing ratio. Both records remain unchanged and receive no new support.
  The new guards prevent automatic endorsement; they do not resolve those recipes.
- Resolve six main-medium M1308 denominator gaps and review its two variants.
  Twelve nested-stock claims were supported only after verifying the exact
  receiving recipe's source links and doses; that does not resolve the main medium.
- Restore source-supported stock boundaries in the identified DSMZ 962a/1255
  and other flattened medium records. [DSMZ 1399](20261007-dsmz1399-stock-boundary/README.md)
  now has its stock boundary and drop-dose representation repaired; its unknown
  drop volume and percent basis have not been invented.
- Address the MediaDive importer's volume/percentage and stock-attribute handling
  before broad reimport. The current inventory still has 3,282 numeric stock
  `PERCENT_V_V` claims above 100 across 3,155 exact tracked record paths.
  The [new executable diagnostic handoff](20261007-solution-importer-unit-handoff.json)
  reproduces nine legacy solution-import defects with synthetic inputs: volume
  amounts mislabeled as percent, double-normalized concentration rates, assumed
  percentage bases and final volumes, unknown-unit fallback, and lost stock
  attributes. No importer or corpus repair is claimed by that read-only check;
  its synthetic rows are not scientific source evidence.
- Resolve or explicitly retain the SL-10 HCl percentage-basis gap and legacy
  placeholders, without converting ambiguity into SUPPORT evidence.
- Reconcile generated merge products through the maintained pipeline; the full
  merge checks expose existing drift and fingerprint/name inconsistencies.
  The [post-DSMZ-2 actual-group retention snapshot](20261007-mediadive-media-0000-0500/merge-retention-after-dsmz2.json)
  found that the merger retained only 230 of the 907 new medium claims:
  119 records lose some or all new evidence, and 112 lose the new bibliography
  entry. This remains unresolved; the authoritative edits are intact, and no
  generated merge files were copied into the worktree. Do not propagate evidence
  across concentration-independent groups without exact formulation matching.
- Review secondary ingredient identity mappings separately from amount evidence,
  including the [confirmed molybdate-form conflict](20261007-molybdate-form-conflict/README.md)
  affecting five exact-label records and the pinned MIM index. No identity fix is
  claimed for those records.
- Resolve source denominator and preparation-stage conflicts using original
  recipes. Inspection of both original DSMZ 1656 PDF pages did not establish a
  main-batch final volume; the [solution 3435 finding](20261007-mediadive-solutions-2500-3000/README.md)
  remains unresolved, without a guessed replacement concentration.
- Complete source-backed stock repairs requiring variant handling:
  DSMZ 464a's original recipe makes
  agar conditional after liquid reactivation, unlike the embedded API base.
  The [new batch findings](20261007-medium-stock-boundaries/README.md#remaining-findings)
  also identify the incorrect 261-to-369 source-duplicate relationship and
  retain the separate secondary chemical-form mapping questions.
  DSMZ 13's stock-only representation and its fingerprinting blocker are now
  repaired in the separate follow-up; name-only unresolved stocks are not
  silently treated as complete compositions.
- Fix the mixed-source merge of DSMZ 261/369. The [actual-group check](20261007-medium-stock-boundaries/merge-retention.json)
  preserves every checked field for five of the seven newly repaired records,
  but combines 261's stocks/procedure with 369's direct ingredient evidence.
  Correct authoritative records do not make that generated result publishable.
- The [second medium-batch actual-group audit](20261007-mediadive-media-0500-1000/merge-retention.json)
  independently confirms the merge evidence-loss defect: only 140 of 653 newly
  added amount/evidence pairs survive across 117 groups; 92 edited records lose
  evidence and 87 lose their bibliography entry. Fix formulation-aware retention
  before publishing regenerated merges.
- The [third medium-batch actual-group audit](20261007-mediadive-media-1000-1500/merge-retention.json)
  checks 142 edited records in 130 real groups. Only 242 of 869 new amount/evidence
  pairs survive; 106 records lose evidence and 100 lose their bibliography entry.
  This gate fails. Authoritative normalized edits remain intact; no generated
  result is published and no evidence is copied across unverified formulations.
- The [fourth medium-batch actual-group audit](20261007-mediadive-media-1500-2000/merge-retention.json)
  checks 86 edited records in 81 groups. Only 446 of 551 new amount/evidence
  pairs survive; 20 records lose evidence and 19 lose their bibliography entry.
  This gate also fails. The normalized evidence is intact; formulation-aware
  merging remains necessary before publishing regenerated records.
- The [fifth medium-batch actual-group audit](20261007-mediadive-media-2000-2500/merge-retention.json)
  checks 107 edited records in 97 groups. Only 414 of 492 new amount/evidence
  pairs survive; 24 records lose evidence and 26 lose the bibliography entry.
  This gate fails too. The authoritative normalized evidence remains intact;
  no generated merge was published or hand-patched.
- The [sixth medium-batch actual-group audit](20261007-mediadive-media-2500-3000/merge-retention.json)
  checks 50 edited records in 50 groups. Only 187 of 223 new amount/evidence
  pairs survive; nine records lose evidence and ten lose their bibliography
  entry. This gate fails. All 223 entries remain intact in authoritative YAML;
  no evidence was copied across unverified formulations to force a pass.
- The [seventh medium-batch actual-group audit](20261007-mediadive-media-3000-3319/merge-retention.json)
  checks 37 edited records in 36 groups. Only 187 of 192 new amount/evidence
  pairs survive; three records lose evidence and seven lose the bibliography
  entry. This gate fails. All entries remain intact in authoritative YAML;
  no generated merge is published or hand-patched.
- The [percent-supplement actual-group audit](20261007-percent-supplements/merge-retention.json)
  checks five repaired records in three groups. Three records pass full retention;
  the two DSMZ source records lose some scoped evidence, references, or child
  links when their KOMODO wrappers are selected. Both exclusive supplement
  options survive, and the methylamine-only branch remains distinct. The
  authoritative YAML is intact; regenerated merges remain unpublished.
- The [first KOMODO actual-group audit](20261007-komodo-media-0000-0500/merge-retention.json)
  checks 25 edited records. Of 137 concentration claims, 117 retain the exact
  amount/reference/snippet/field-scope match, but only 103 retain the complete
  new evidence entry. Four records lose amount quotes; eight each lose full
  entries, mapping evidence, bibliography or history. These overlapping sets
  affect nine records in total. This gate fails; authoritative
  normalized evidence remains intact and no generated merge is published.
- The [second KOMODO actual-group audit](20261007-komodo-media-0500-1000/merge-retention.json)
  checks 24 edited records. Of 141 concentration claims, 131 retain the exact
  amount/reference/snippet/field-scope match, but only 120 retain the complete
  new evidence entry. Three records lose amount quotes, five lose full entries,
  and six each lose mapping evidence, bibliography or history. These overlapping
  sets affect eight records in total; sixteen pass every checked field. This
  gate fails. All additions remain intact in authoritative normalized YAML;
  no generated merge is published or evidence copied across unverified recipes.
- The [third KOMODO actual-group audit](20261007-komodo-media-1000-1500/merge-retention.json)
  checks 46 edited records in 45 groups. Of 264 concentration claims, 257 retain
  the exact amount/reference/snippet/field-scope match and 240 retain complete
  evidence entries. Two records lose amount quotes, four lose full entries, and
  six each lose mapping evidence, bibliography or history. These overlapping
  sets affect seven distinct records; 39 pass every checked field. This gate
  fails. All additions remain intact in authoritative normalized YAML and no
  generated merge is published.
- The [medium 265 actual-group audit](20261007-dsmz265-preparations/merge-retention.json)
  checks both repaired media in one group. The canonical KOMODO copy retains all
  checked fields and all 25 scoped snippets. The DSMZ copy retains 24 of 25
  snippets, but not its complete solution metadata, preparation, notes, record
  evidence, references or history. The gate fails despite intact authoritative
  YAML. Standalone solution 531 is correctly outside medium matching, and no
  generated merge is published.

- The [fourth KOMODO actual-group audit](20261007-komodo-media-1500-2000/merge-retention.json)
  checks six edited records in six groups. All 25 ingredient amount quotes and
  all 25 complete ingredient evidence entries survive. Five records pass every
  checked field, but KOMODO 464 loses complete mapping evidence, bibliographic
  additions and its curation event. These failures affect one record and fail
  the gate. All additions remain intact in authoritative normalized YAML;
  no generated merge is published.

The [historical stock inventory](20261007-stock-inventory-after-1399.json) is a subset
of the full objective, not a replacement for it.
At that snapshot, 4,775 root `mediadive.solution:` records contained 34,966 composition
concentration objects; 11,015 lacked an ingredient-level
nonempty snippet plus HTTP(S)/DOI reference. This is only an evidence-presence
check; neither presence nor schema validity proves scientific correctness.
The stock iron dose remains represented in notes/evidence but is no longer
counted as a numeric concentration object after the unsupported slot was removed.
The later solution 190 preparation repair changes composition nesting and water
evidence, so those historical composition counts must not be quoted as current.

The [exact-path follow-up coverage inventory](20261007-followup-coverage-after-komodo-2500.json)
identifies **5,300** normalized records outside these per-record reports,
containing 74,998 ingredient rows, 5,935 stock-addition rows, and 36 textual
variant rows. This is not a claim that those records have never been reviewed:
the historical structural audit covers the whole corpus. Literal source prefixes
in this remaining follow-up inventory are:

| Source prefix | Records |
| --- | ---: |
| `komodo.medium` | 1,133 |
| `mediadive.medium` | 2 |
| `TOGO` | 2,915 |
| unspecified | 538 |
| `MEDIADB` | 469 |
| `UTEX` | 98 |
| `nbrc.medium` | 75 |
| `jcm.grmd` | 60 |
| `MediaIngredientMech` | 10 |

These prefixes are source identifiers, not proof of recipe equivalence. Each
receiving-medium pass must verify exact source membership and stock
boundaries; solution-only evidence cannot be propagated by name or fingerprint.
The [KOMODO offsets 2000-2499](20261007-komodo-media-2000-2500/README.md) now have
per-record source-pass results and 46 locally applied evidence-only changes.
Their 23 withheld formulations and other unresolved rows remain follow-up work,
not complete scientific reviews. The next inventory boundary is offset 2500;
the preceding 2,500 source-pass reports do not establish every amount or variant.
Within the historical first 500 medium reports, 293 records were blocked on
stock topology; DSMZ 2, DSMZ 13, and the seven-record batch now have explicit verified
repairs rather than rewritten first-pass results. Unresolved report rows also include missing/optional source ingredients,
preparation context, variant relationships, and arithmetic conflicts; they are
not all independent concentration claims. These remain in scope along with
records outside the reports.
The second 500-record medium pass adds 349 stock-topology-blocked records,
32 arithmetic-conflict rows in eight records, and further preparation/variant
follow-ups. The third pass adds 309 stock-topology-blocked records and three
agar arithmetic conflicts, as well as the preparation-scope findings above.
The fourth pass includes 221 stock-topology-blocked records and 157
collection/link-blocked records (101 CCAP and 56 DSMZ), plus the four new
source-scope findings. It does not extend the DSMZ-specific reviewer to CCAP.
The fifth pass covers the nine CCAP and 491 JCM entries at offsets 2000-2499.
Of these, 72 API responses have no recipe table and remain unresolved.
The S77 original PDF handoff is still pending curation. The sixth pass covers
the 500 JCM entries at offsets 2500-2999. Eighty-one API responses have no
recipe table, and its other unsupported/conflicted claims remain unresolved.
The public-medium boundary in the frozen receiving-medium inventory is
**3319**. Two of its ten public targets remain outside the follow-up reports;
P2-P8 and P10 were reviewed noncontiguously. Earlier unsupported claims remain in
scope too, and the frozen inventory is not rewritten.
The [historical sixth-cohort acquisition handoff](20261007-medium-source-fetch-2500-3000-preparation-leads.md)
is superseded by its applied batch report, not rewritten. J896's confirmed
40 ml versus 584 ml denominator conflict is now repaired by its explicit successor.
The [319 JCM source captures](20261007-medium-source-fetch-3000-3319.json)
now have applied seventh-pass reports. Twenty contain no recipe table and remain
unresolved. Their [historical preparation handoff](20261007-medium-source-fetch-3000-3319-preparation-leads.md)
is superseded by the applied cohort report, not rewritten. The original-source
J1105 conflict is now repaired by its original-source successor; J1249 and
the other unresolved stock/variant issues remain in scope.
The [initial 329-target fetch](20261007-medium-source-fetch-3000-3329-partial.json)
stopped at metadata-only public-medium payloads: P1-P3 failed the recipe contract,
and P4-P10 were unattempted. Subsequently, all ten public HTML pages were
retrieved, with 21 recipe tables and two inspected preparation diagrams; see the
[public-source handoff](20261007-public-medium-source-handoff.md). P2-P8 and P10
now have source-specific follow-up reports in the public and RS batches;
P1 and P9 remain outside those reports. Reviewed records still have explicitly
retained scientific gaps. All ten remain in the frozen inventory and
full objective; no missing API recipe is converted to an empty composition.
The [P1 primary-source handoff](20261007-p1-primary-source-handoff.md) adds the
author's inspected dissertation protocol, independently captured with a hash.
It corroborates some main-recipe dose inputs but exposes stock-formulation
differences and an internal bicarbonate table inconsistency. The journal full
text remains inaccessible; neither source is silently substituted for P1.
P1 remains unchanged and outside the completed follow-up report inventory.
The [P2 field-by-field handoff](20261007-p2-claim-handoff.json) identifies 28
candidate claims after inspecting all three recipe tables and preparation text.
At that checkpoint, the numeric values matched the scoped source inputs and
P2 was unchanged. Its [applied successor](20261007-public-stocks/README.md)
now adds scoped evidence and the missing haemin-stock water, explicitly without
an invented fixed water amount. Original preparation and user-contributed
provenance caveats are preserved.
The [P8/P9 primary-source handoff](20261007-p8-p9-primary-source-handoff.md)
adds an inspected public author manuscript with the matching DOI. Its methods
confirm P8's 15-versus-51 g/L phosphate stock conflict and an unsupported local
6.1 ml dose denominator. P9's cited broth formulation is not its current methane
agar graph. P8 now has an explicit original-source repair in the public stock
batch, with dataset counterevidence preserved. P9 remains unchanged and outside
the follow-up reports; its source-identity conflict still requires repair.
The [historical P7/P10 preparation handoff](20261007-p7-p10-preparation-handoff.json)
inspected 36 existing claim rows without editing either record. It identified eight
specific follow-ups, including P7's unsupported iron percentage conversion and
B12 solvent/final-volume ambiguity, and P10's undisclosed trace dose and
cross-locator copper-stock unit evidence. Its
[applied successor](20261007-public-input-basis/README.md) now provides per-record
results and source-backed input/evidence repairs. Unknown amounts remain
unquantified; the historical handoff itself is not an additional record review.
The [P4/P5 applied stock-boundary repair](20261007-rs-stock-boundaries/README.md)
now preserves single stocks, carriers, and mix stages independently. It also
identifies the D-Mannose/L-mannose conflict not described in the original handoff.
Neither that conflict nor the earlier Xylose/Xylan conflict has been resolved by
choosing a substance; both calculated doses were withdrawn. P4's unknown TiCl3
percentage basis and all unspecified makeup-fluid amounts remain unquantified.

## Verification

The [489 validation journal](20261007-dsmz489-stocks/validation.json) is terminal.
The final identical Python 3.11 selection passes 315 tests, superseding the
preserved historical-withholding test failure; cached Python 3.13 passes 238.
Strict validation passes for all 15,910 records, along with three schema checks,
IDs, variant links, the affected medium/solution and KOMODO source readbacks,
lint, formatting and whitespace. `test-fast` stops during collection because
`dotenv`, `rapidfuzz`, `pandas` and `bs4` are missing; product/reference validators
are also unavailable. Actual-group retention fails for both media, retaining
28/29 scoped snippets but not complete ingredient/stock/procedure/provenance
fields. Global merge verification still reports 1,247 name conflicts and 3,287
fingerprint issues. Freshness fails with 6,320 tracked versus 6,494 temporary
outputs: 3,720 only tracked, 3,894 only fresh, 1,668 changed and 932 unchanged.
No tracked merges were changed. These are local checks, not a CI pass.

The [467/469 validation journal](20261007-dsmz467-469-inputs/validation.json) is
terminal, including final passing selections of 326 tests on isolated Python
3.11 and 249 on cached Python 3.13. Explicit source readback of the affected
second medium/solution batches passes. Full strict validation passes for 15,910
records, along with six open-schema checks, IDs, variant links, lint, formatting
and whitespace. Two initial diagnostic-test failures are preserved and
superseded by passing reruns, not hidden. Product/reference validators remain
unavailable. Actual-group retention still loses complete context/provenance
from the two DSMZ inputs despite retaining all forty source snippets. Global
merge verification and freshness fail: 1,247 name conflicts, 3,287 fingerprint
issues; freshness has 6,320 tracked versus 6,493 temporary outputs, 3,719 only
tracked, 3,892 only fresh, 1,668 changed and 933 unchanged. These are local
checks, not a full CI pass or publication of generated merges.

The [fourth KOMODO batch validation](20261007-komodo-media-1500-2000/validation.json)
is terminal with 23 checks: eighteen pass, two are unavailable and three merge
gates fail. Focused tests pass **246 on isolated Python 3.11** and **169 on
cached Python 3.13**, with no errors, failures or skips. Strict validation scans
all 15,910 normalized records with zero schema errors. Representative schema,
IDs, variant links, guarded application/readback/no-op, independent inversion,
prior medium/solution/KOMODO readbacks, cumulative semantic diff, exact-path
coverage, Ruff, Black and whitespace checks pass. Product/reference validators
are unavailable for missing `oaklib` and `linkml-reference-validator`; these are
local checks, not full-project-environment, full-suite or CI passes. Actual-group
retention preserves all 25 ingredient evidence entries but fails complete
mapping/bibliography/history retention for KOMODO 464. Global verification still
reports 1,247 name conflicts and 3,287 fingerprint issues. [Freshness](20261007-komodo-media-1500-2000/merge-freshness.json)
fails with 6,320 tracked and 6,493 temporary outputs: 3,719 only tracked, 3,892
only fresh, 1,667 changed and 934 unchanged. All identified groups were written,
but 4,785 standalone solutions are excluded and 342 other inputs are skipped.
No tracked merge output changed; these curation edits remain uncommitted and
unpublished.

The [medium 265 follow-up validation](20261007-dsmz265-preparations/validation.json)
is terminal with 26 checks: twenty pass, three are unavailable and three merge
gates fail. Focused tests pass **359 on isolated Python 3.11** and **235 on
cached Python 3.13**, with no errors, failures or skips. Full strict validation
passes all 15,910 normalized records, as do all three target schemas, IDs,
variant links, applied readback/no-op, independent inversion, prior medium/
solution/KOMODO readbacks, semantic diff, coverage, Ruff, Black and whitespace
checks. The product check and two reference runs remain unavailable for missing
`oaklib` and `linkml-reference-validator`; these are not full-suite or CI passes.
Actual-group retention fails for the DSMZ medium copy, while the canonical
KOMODO copy retains all checked fields. Global verification still reports
1,247 name conflicts and 3,287 fingerprint issues. [Freshness](20261007-dsmz265-preparations/merge-freshness.json)
fails with 6,320 tracked and 6,493 temporary outputs: 3,719 only tracked, 3,892
only fresh, 1,665 changed and 936 unchanged. All identified temporary groups
were written, but the pipeline excludes 4,785 standalone solutions and skips
342 other inputs. No tracked merge output changed; curation remains uncommitted
and unpublished.

The [third KOMODO batch validation](20261007-komodo-media-1000-1500/validation.json)
is terminal with 21 checks: sixteen pass, two are unavailable and three merge
gates fail. Focused tests pass **242 on isolated Python 3.11** and **165 on cached
Python 3.13**, without errors, failures or skips. Full strict validation passes
all 15,910 records, as do the representative schema, IDs, variant links,
guarded application/readback/no-op, independent inversion, prior medium/solution/
KOMODO readbacks, semantic diff, coverage and whitespace checks. Black and Ruff
pass for the updated KOMODO regression tests. Product/reference checks remain
unavailable for missing `oaklib` and `linkml-reference-validator`; these are
local checks, not full-suite or CI passes. Actual-group retention fails for
seven distinct records. Global verification still reports 1,247 name conflicts
and 3,287 fingerprint issues. Freshness fails with 6,320 tracked and 6,493
temporary outputs: 3,719 only tracked, 3,892 only fresh, 1,665 changed and
936 unchanged. All temporary groups were written; no tracked merge output
changed. These curation edits remain uncommitted and unpublished.

The [medium 125 follow-up](20261007-dsmz125-alternatives/validation.json) passes
**976 focused regression tests**; its separate
[Python 3.13 cohort run](20261007-dsmz125-alternatives/python313-validation.json)
passes **21 tests**. Applied readback, independent inversion and a zero-change
second apply also pass. All 24 checks are terminal: strict validation of all
15,910 records, IDs, variant links, target schemas, prior-batch readbacks,
semantic diff, coverage and whitespace checks pass. Product/reference checks
remain unavailable because of missing dependencies. Actual-group retention
fails full metadata/provenance preservation for the DSMZ medium copy despite
retaining its literal snippets; the canonical KOMODO copy retains all checked
fields. Standalone solution 223 is correctly excluded from medium matching.
Global verification still reports 1,247 name conflicts and 3,287 fingerprint
issues. Freshness also fails: 6,493 temporary outputs versus 6,320 tracked,
with 3,719 only tracked, 3,892 only fresh, 1,657 changed and 944 unchanged.
No tracked merge outputs changed. These are local checks, not full-suite or CI
passes, and the curation batches remain uncommitted.

The [solution-routing repair](20261007-solution-merge-routing/README.md) passes
**955 focused regression tests** after fixing its initially detected preview
integration regression. **66 core merge tests also pass on Python 3.13** in a
cached environment, as do **45 solution-review tests**. These are not full-suite
or CI passes; the isolated Python
3.11 full-suite command stops before collection because `pytest-cov` is missing.
The 15,910-record routing audit passes and verifies byte preservation, while
medium 111's separate evidence-retention check remains unsuccessful.
Temporary regeneration now writes all 6,492 eligible medium groups with zero
group-write errors, but freshness still fails against 6,320 tracked outputs
(3,719 only tracked, 3,891 only fresh, 1,657 changed and 944 unchanged). Global
verification still reports 1,247 name conflicts and 3,287 fingerprint issues.
The scientific readback preserves the three medium 111 inputs and their snippets;
this pipeline repair adds no new concentration edits or review coverage.

The [medium 111 validation](20261007-dsmz111-preparation/validation.json) is
terminal: five baseline and 23 post-apply checks ran, with **936 focused tests
passing**. All 15,910 records pass strict schema validation; IDs, three schema
checks, guarded application/readback/no-op, historical batch readbacks,
independent full-record inversion, semantic diff, coverage and whitespace checks
pass. The [coverage snapshot](20261007-followup-coverage-after-dsmz111.json)
still leaves **6,800 exact paths outside the concentration follow-up**.
Actual-group retention fails for the DSMZ medium 111 copy; the standalone stock
was incorrectly admitted through a partial fingerprint and its generated output
failed on a missing medium `name`. The then-current freshness comparison is not
proof of a complete regeneration. Missing `oaklib` and reference-validator
dependencies prevent those checks. The subsequent routing repair has its own
[validation record](20261007-solution-merge-routing/validation.json); it does not
rewrite this historical result. That medium 111 run used isolated Python 3.11,
not maintained Python 3.13 or CI. No generated merge has been published.

The [second KOMODO batch validation](20261007-komodo-media-0500-1000/validation.json)
records **910 passing focused tests** with zero errors, failures or skips.
All three baseline jobs and seventeen post-apply jobs are terminal. Full strict
validation passes all 15,910 normalized records; the representative schema check,
canonical IDs, guarded apply/readback/no-op, first-batch readback, independent
full-record inversion, semantic diff and exact-path coverage pass. Black, Ruff
and `git diff --check` pass. The
[actual-group retention check](20261007-komodo-media-0500-1000/merge-retention.json)
fails for eight distinct records across overlapping evidence, bibliography and
history checks; all additions remain intact in authoritative normalized YAML.
Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. [Then-current freshness](20261007-komodo-media-0500-1000/merge-freshness.json)
fails with 6,320 tracked and 6,492 fresh records: 3,719 only tracked, 3,891 only
fresh, 1,657 changed and 944 unchanged. Product and automated reference validation
remain unavailable for missing `oaklib` and `linkml-reference-validator`.
This is isolated Python 3.11 validation, not maintained Python 3.13 or CI;
the full repository suite was not rerun. No generated merge was published.

The [first KOMODO batch validation](20261007-komodo-media-0000-0500/validation.json)
records **908 passing focused tests** with zero errors, failures or skips.
All three baseline jobs and fifteen post-apply jobs are terminal. Full strict
validation passes all 15,910 normalized records; canonical IDs, guarded
apply/readback/no-op, independent full-record inversion, literal source checks,
semantic diff and exact-path coverage pass. Black, Ruff and `git diff --check`
pass. The [actual-group retention check](20261007-komodo-media-0000-0500/merge-retention.json)
fails for nine distinct records across overlapping evidence, bibliography and
history checks; all appended entries remain intact in normalized YAML.
Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. [Then-current freshness](20261007-komodo-media-0000-0500/merge-freshness.json)
fails with 6,320 tracked and 6,492 fresh records: 3,719 only tracked, 3,891 only
fresh, 1,649 changed and 952 unchanged. Product and automated reference validation
remain unavailable for missing `oaklib` and `linkml-reference-validator`.
This is isolated Python 3.11 validation, not maintained Python 3.13 or CI;
the full repository suite was not rerun. No generated merge was published.

The [RS stock-boundary validation](20261007-rs-stock-boundaries/validation.json)
records **876 passing focused tests** with zero errors, failures or skips.
All four baseline jobs and 22 post-apply jobs are terminal. Full baseline/post
strict scans pass all 15,910 normalized records; both targets' schema checks,
canonical IDs, guarded apply/readback/no-op, earlier public-batch readbacks,
independent semantic diff and exact-path coverage pass. The independent
[source-text check](20261007-rs-stock-boundaries/snippet-readback.json) verifies
155 new evidence snippets and 558 claim excerpts against the captured pages.
Both records remain singleton groups and pass the
[actual-group retention check](20261007-rs-stock-boundaries/merge-retention.json),
including nested stocks, evidence, bibliography, notes and prior history.
The historical fingerprint-impact artifact is preserved; its test now verifies
P5's explicit, independently audited successor instead of ignoring source drift.
Black, Ruff and `git diff --check` pass. This is isolated Python 3.11 validation,
not maintained Python 3.13 or CI; the full repository suite was not rerun.
Product and automated reference validation remain unavailable for missing
`oaklib` and `linkml-reference-validator`. Global merge verification fails with
1,247 name conflicts and 3,287 fingerprint issues. [Then-current freshness](20261007-rs-stock-boundaries/merge-freshness.json)
fails with 6,320 tracked and 6,492 fresh records: 3,719 only tracked, 3,891 only
fresh, 1,645 changed and 956 unchanged. No generated merge was published.

The [public input-basis validation](20261007-public-input-basis/validation.json)
records **823 passing focused tests** with zero errors, failures or skips,
baseline/post strict scans of all 15,910 normalized records with zero errors,
both targets' open-schema checks, canonical IDs, guarded apply/readback/no-op,
P2/P3/P6/P8 source readbacks, independent semantic diff and exact-path coverage.
All three baseline jobs and twenty post-apply jobs are terminal. The independent
[snippet readback](20261007-public-input-basis/snippet-readback.json) verifies all
39 new evidence snippets against the captured source tables/preparation. The
[actual-group retention check](20261007-public-input-basis/merge-retention.json)
passes both singleton records, including notes and curation history. Black,
Ruff and `git diff --check` pass. These are isolated Python 3.11 checks, not
maintained Python 3.13 or CI passes; the full suite was not rerun.
Product validation still fails for missing `oaklib`; both reference checks fail
for a missing executable. Global merge verification fails with 1,247 name
conflicts and 3,287 fingerprint issues. [Then-current freshness](20261007-public-input-basis/merge-freshness.json)
fails with 6,320 tracked and 6,492 fresh records: 3,719 only tracked, 3,891 only
fresh, 1,645 changed and 956 unchanged. No generated merge was published.

The [public stock validation](20261007-public-stocks/validation.json) records
baseline/post-edit strict scans of 15,910 normalized records with zero errors,
both targets' schema checks, canonical IDs, guarded apply/readback/no-op,
P3/P6 readback, independent diff and exact-path coverage. All two baseline
target jobs and 19 post-apply jobs are terminal. The initial focused run had
one stale historical-snapshot test; the snapshot was preserved and the test
now checks P8's explicit hash-linked successor and independent inversion.
The [full focused recheck](20261007-public-stocks/validation-recheck.json) passes
**795 tests**, with zero errors, failures or skips. The expanded
[actual-group retention check](20261007-public-stocks/merge-retention-with-context.json)
passes both singleton records, including their notes and curation history.
Black, Ruff and `git diff --check` pass. These are isolated Python 3.11 checks,
not maintained Python 3.13 or CI passes; the full suite was not rerun.
Product validation still fails for missing `oaklib`, and both reference checks
fail for a missing executable. Global verification fails with 1,247 name
conflicts and 3,287 fingerprint issues. [Then-current freshness](20261007-public-stocks/merge-freshness.json)
fails: 6,320 tracked and 6,492 fresh records, with 3,719 only tracked, 3,891
only fresh, 1,645 changed and 956 unchanged. No generated merge was published.

The [public direct-ingredient validation](20261007-public-direct/validation.json)
records **750 passing focused tests**, baseline/post-edit strict scans of all
15,910 normalized records with zero errors, both targets' baseline/post schema
checks, canonical IDs, guarded apply/readback/no-op, independent diff and
exact-path coverage. The two baseline target jobs and all 18 post-apply jobs
are terminal, in addition to the separate baseline strict scan. Both targets
retain all checked fields in their actual full-corpus singleton merge groups.
Black, Ruff and `git diff --check` pass. Product validation fails for missing
`oaklib`; both reference validators fail for a missing executable. The full
suite was not rerun for this batch. These are isolated Python 3.11 results,
not maintained Python 3.13 or CI passes. Global verification fails with
1,247 name conflicts and 3,287 fingerprint issues. [Then-current freshness](20261007-public-direct/merge-freshness.json)
fails: 6,320 tracked and 6,492 fresh records, with 3,719 only tracked, 3,891
only fresh, 1,645 changed and 956 unchanged. No generated merge was published.

The [percent-supplement validation](20261007-percent-supplements/validation.json)
records **704 passing focused tests**, baseline/post-edit strict scans of all
15,910 normalized records, five target schema checks, canonical IDs, reciprocal
variant links, guarded apply/readback/no-op, all seven medium readbacks and
JCM 896/JCM 1105/KOMODO 12 readbacks. Independent diff and exact-path coverage
pass. All seven baseline and 36 post-apply jobs are terminal. These are isolated
Python 3.11 checks, not maintained-runtime or CI passes. Black, Ruff, and
`git diff --check` pass; product/reference/full-suite dependency failures remain.
Actual-group retention fails for two of five records in three groups, as
described above. Global verification fails with 1,247 name conflicts and 3,287
fingerprint issues. [Then-current freshness](20261007-percent-supplements/merge-freshness.json)
fails: 6,320 tracked and 6,492 fresh records, with 3,719 only tracked, 3,891 only
fresh, 1,645 changed, and 956 unchanged. No generated merge was published.

The [JCM 1105 validation](20261007-jcm1105-stock-boundary/validation.json)
records **636 passing focused tests**, baseline/post-edit strict scans of
15,910 normalized records without errors, target schema and canonical-ID
checks, guarded apply/readback/no-op, all seven medium readbacks, and both
JCM 896/KOMODO 12 readbacks. Independent diff, exact-path coverage, and the
corrected record's actual-group retention pass. All 26 post-apply jobs and
both baseline jobs are terminal. These are isolated Python 3.11 checks,
not maintained-runtime or CI passes. Black, Ruff, and `git diff --check` pass.
Product/reference/full-suite dependency failures remain explicit. Global merge
verification fails with 1,247 name conflicts and 3,287 fingerprint issues.
[Then-current freshness](20261007-jcm1105-stock-boundary/merge-freshness.json) fails:
6,320 tracked and 6,491 fresh records, with 3,719 only tracked, 3,890 only fresh,
1,645 changed, and 956 unchanged. No generated merge was published.

The [seventh-pass validation](20261007-mediadive-media-3000-3319/validation.json)
records **589 passing focused tests**, zero strict-schema errors across 15,910
records, open-schema/ID checks, guarded apply/readback/no-op, all six prior medium
readbacks and both JCM 896/KOMODO 12 readbacks. Semantic-diff and coverage checks
pass. All 25 post-apply jobs and both baseline jobs are terminal.
Product/reference/full-suite dependency failures remain explicit. Retention and
global verification fail, the latter with 1,247 name conflicts and 3,287
fingerprint issues. [Then-current freshness](20261007-mediadive-media-3000-3319/merge-freshness.json)
fails: 6,320 tracked and 6,491 fresh records, with 3,719 only tracked, 3,890
only fresh, 1,644 changed and 957 unchanged. Regeneration was temporary only.
Black, Ruff and `git diff --check` pass. These are isolated Python 3.11 results,
not maintained-runtime or CI passes.

The [JCM 896 validation](20261007-jcm896-final-volume/validation.json) records
**588 passing focused tests**, baseline/post-edit strict scans of 15,910 records
with zero errors, representative open-schema and ID checks, guarded readback,
and an unchanged second apply. All six earlier medium readbacks and KOMODO 12
readback pass; the sixth medium cohort explicitly follows the new successor.
Independent semantic-diff and coverage checks pass. All 24 post-apply jobs and
both baseline jobs are terminal. These are isolated Python 3.11 checks, not
maintained Python 3.13 or CI. Missing product/reference/test dependencies remain
explicit failures. Black, Ruff, and `git diff --check` pass.
The corrected JCM 896 singleton group retains every checked formulation and
evidence field. Global merge verification still fails with 1,247 name conflicts
and 3,287 fingerprint issues. [Then-current freshness](20261007-jcm896-final-volume/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,719 only tracked, 3,890 only fresh,
1,624 changed, and 977 unchanged. Regeneration was temporary, not published.

The [sixth-medium-pass validation](20261007-mediadive-media-2500-3000/validation.json)
records **553 passing focused tests**, full baseline/post-edit strict validation
of 15,910 normalized records, representative open-schema and ID checks,
independent preflight, and readback of all 500 hashes and 223 new snippets.
Reapplication changes zero records. All five earlier medium readbacks and
KOMODO 12 readback pass, as do independent semantic-diff and coverage checks.
All 23 post-apply jobs and both baseline jobs are terminal. These are isolated
Python 3.11 checks, not maintained-runtime or CI results. Product/reference
validation and both full-suite attempts fail on documented missing dependencies
or executables. Black, Ruff, and `git diff --check` pass.
All three merge gates fail. Global verification reports 1,247 name conflicts
and 3,287 fingerprint issues. [Then-current freshness](20261007-mediadive-media-2500-3000/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,624 changed, and 978 unchanged. Regeneration was temporary, not published.

The [fifth-medium-pass validation](20261007-mediadive-media-2000-2500/validation.json)
records **550 passing focused tests**, full baseline/post-edit strict validation
of 15,910 normalized records, open-schema and ID checks, independent preflight,
and readback of all 500 target hashes and 492 new snippets. Reapplication changes
zero records. All four earlier medium readbacks and KOMODO 12 readback pass.
The 22 post-apply jobs and both baseline jobs are terminal. These are isolated
Python 3.11 checks, not maintained-runtime or CI results. Dependency-related
product/reference/full-suite failures remain explicit. Black, Ruff and
`git diff --check` pass for the changed code and current tracked diff.
All three merge gates fail. Global verification reports 1,247 name conflicts
and 3,287 fingerprint issues. [Then-current freshness](20261007-mediadive-media-2000-2500/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,597 changed and 1,005 unchanged. Regeneration was temporary, not published.

The [fourth-medium-pass validation](20261007-mediadive-media-1500-2000/validation.json)
records 512 passing focused tests, full baseline/post-edit strict validation of
15,910 normalized records, representative open-schema and ID checks, independent
provenance-only preflight, and persisted source read-back. All 500 new hashes
and 551 snippets verify; reapplication changes zero records. Earlier medium and
KOMODO 12 read-back checks pass. These are isolated Python 3.11 results. A
[fresh maintained-runtime setup attempt](20261007-mediadive-media-1500-2000/runtime-attempts.json)
failed while building locked `llvmlite==0.46.0` for Python 3.13; neither the
dependency pins nor the worktree environment were changed. No maintained-runtime
or CI pass is claimed. Full-suite collection and product/reference dependency
failures remain recorded separately from the schema/source passes.
All 21 validation jobs are terminal. The actual-group retention, global merge
verification, and freshness gates fail. The global verifier reports 1,247 name
conflicts and 3,287 fingerprint issues. [Then-current freshness](20261007-mediadive-media-1500-2000/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,549 changed, and 1,053 unchanged. Temporary regeneration did not update the
tracked merge corpus.

The [third-medium-pass validation](20261007-mediadive-media-1000-1500/validation.json)
records 498 passing focused tests, full baseline/post-edit strict validation
of all 15,910 normalized records, the ID gate, representative open-schema
checks, independent provenance-only preflight, and persisted source read-back.
All 500 new hashes and 869 snippets verify; reapplication changes zero records.
Earlier medium and KOMODO 12 read-back checks pass. Full-suite execution cannot
start with missing coverage support; a no-coverage retry stops on four missing
dependency modules. Product/reference validators remain unavailable. These are
isolated Python 3.11 checks, not a maintained-runtime/CI pass. Global merge
verification, freshness, and actual-group evidence retention are separate gates
recorded with the batch; schema and source checks do not imply those gates pass.
All three merge gates fail. The verifier reports 1,247 name conflicts and 3,287
fingerprint issues. [Freshness](20261007-mediadive-media-1000-1500/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,526 changed, and 1,076 unchanged. Regeneration was temporary only.

The [KOMODO 12 validation](20261007-komodo12-extraction/validation.json) records
the preceding checks: 486 focused tests, full strict schema validation for 15,910
normalized records, the ID gate, before/after open-schema validation, source
read-back, independent semantic diff, and no-op reapplication pass. Product and
automated reference checks remain unavailable; full-suite dependency failures
from the preceding run remain unresolved. This is not a maintained-runtime/CI
pass. The [actual merge-retention check](20261007-komodo12-extraction/merge-retention.json)
now preserves all checked formulation fields and complete original evidence
entries for KOMODO 12, DSMZ 12, and DSMZ 657, allowing only additive unique-reference
root provenance. The specific soil-record loss is resolved. No general merger
fix or global merge pass is implied: its verifier still finds 1,247 name
conflicts and 3,287 fingerprint issues.

The [extraction-boundary validation](20261007-extraction-boundaries/validation.json)
records the preceding checks. All 449 focused tests passed, both edited records
passed before/after open and closed schema checks, all 15,910 normalized records
passed strict validation, and the ID gate passed. Read-back verifies both repair
hashes and 19 scoped claims; reapplication changes zero records. Earlier medium
read-back checks all 1,000 hashes: the first batch now distinguishes 906 retained
claims from one withdrawn soil claim through ten explicit successors, and the
second retains 653 snippets through one successor. Each has one relocated agar
claim. Full-suite, product, and reference checks remain unavailable due to the
dependency failures documented in that report. Ruff, Black, and the diff
whitespace check pass for this repair's changed Python/data surface.

That historical actual-group retention gate failed for soil extract, where the
legacy KOMODO record displaced corrected preparation/evidence; manure agar
retained all checked fields. That global verifier reported 1,247 name conflicts
and 3,287 fingerprint issues. Its [freshness snapshot](20261007-extraction-boundaries/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,513 changed, and 1,089 unchanged. Both global merge gates fail, and no generated
result was published. A [fresh original KOMODO source row](20261007-extraction-boundaries/komodo12-source-handoff.json)
confirms its record 12 links to the exact DSMZ 12 PDF; this is a source-mapping
handoff used by the subsequent KOMODO correction, not quantity evidence itself.

The [second medium-batch validation](20261007-mediadive-media-0500-1000/validation.json)
records the preceding checks. Its focused selection passed 406 tests. Both the fresh
baseline and post-edit strict checks passed for all 15,910 records, and the ID
gate passed. Read-back verifies all 500 new record hashes and all 653 new literal
snippets; reapplication changed zero records. That historical check matched
907 first-medium snippets through nine explicit successors, but did not resolve
the DSMZ 12 scope error subsequently corrected above. Product and
reference validators remain unavailable due to missing dependencies.
That global merge verifier reported 1,247 name conflicts and 3,287
fingerprint issues. Its [freshness snapshot](20261007-mediadive-media-0500-1000/merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,513 changed, and 1,089 unchanged. Both global merge gates and the new batch's
actual-group evidence-retention gate fail; no generated result was published.

The preceding [DSMZ 13 validation](20261007-dsmz13-stock-only/validation.json)
records that batch's checks. The focused regression selection passed 398 tests; all 15,910
normalized records passed strict schema validation. The actual maintained
DSMZ 13 merge group retains both stocks, the explicit empty direct list,
preparation, and all checked evidence/reference fields. The earlier 500-record
medium pass still verifies all 907 accepted snippets through nine explicit
successors. The full-suite attempt is not a pass: coverage support is missing,
and retrying without coverage stops during collection on four missing dependency
modules. The fingerprint module has 12 pre-existing Ruff findings and no new
ones; the remaining edited Python files pass Ruff.
The final DSMZ 13 read-back verifies twelve scoped claims and its rerun changes
zero records. Its full merge verifier still finds 1,247 name conflicts and
3,287 fingerprint issues. Temporary freshness regeneration produces 6,491
records versus 6,320 tracked: 3,718 only tracked, 3,889 only fresh, 1,494 changed,
and 1,108 unchanged. Neither global merge gate passes.

The preceding [stock-boundary batch validation](20261007-medium-stock-boundaries/validation.json)
records that batch's checks. All seven before/after open- and closed-schema checks
passed; full strict validation scanned all 15,910 records without errors, and
the ID gate passed. The final selected regression run passed 327 tests. The independent inversion verifies every old ingredient, new amount,
preparation move, and preservation of unrelated data. Read-back of the original
500-record medium pass still verifies all 907 accepted snippets through eight
explicit successor records. This batch's merge-retention gate fails as described
above, independently of schema and evidence checks.
Final batch read-back verified seven hashes and 105 scoped claims, and the rerun
changed zero records. That batch's full freshness gate exits 1: 6,320 tracked
versus 6,468 freshly generated records; 3,723 only tracked, 3,871 only fresh,
1,488 changed, and 1,109 unchanged. The global merge verifier still finds 1,247
name conflicts and 3,286 fingerprint issues. Product/reference validators exit
2 for unavailable dependencies; neither is a pass.

The preceding [DSMZ 2 validation snapshot](20261007-dsmz2-stock-boundary/validation.json)
records 283 passing selected regression tests, a zero-change rerun, current
full-corpus strict and ID gates, and exact source read-back. All 500 medium-batch
record hashes and 907 earlier snippets remain verified through the explicit
successor chain. The repaired record's actual merge group preserves all checked
fields; this does not resolve the separate evidence-loss findings or global
merge failures. Current structural and cumulative counts above come from the
independent semantic diff, not report-file counts. Freshness still fails, with
3,723 only-tracked, 3,865 only-generated, 1,487 changed, and 1,110 unchanged records.

The [initial-pass validation snapshot](20261007-validation-after-4770.json) and
[DSMZ 1399 follow-up validation](20261007-dsmz1399-stock-boundary/README.md#verification)
record the test selection, local runtime, successful checks, and unavailable gates.
The [medium-batch validation snapshot](20261007-mediadive-media-0000-0500/validation.json)
adds current source read-back, idempotence, corpus gates, and actual merge-retention
results. Its 257-test regression selection passed. Baseline and post-edit strict
validation both scanned all 15,910 records without errors; the ID gate passed.
All 500 medium record hashes and 907 new snippets matched the captured sources,
and reapplying the plan changed zero records. The full merge verification still
fails with 1,247 name conflicts and 3,286 fingerprint issues. Product/reference
validators remain unavailable in the isolated runtime and are not counted as passes.
That batch's freshness check also exited 1, with 3,723 only-tracked, 3,864
only-generated, 1,487 changed, and 1,110 unchanged records.
See the batch reports for per-record claims, exact source locators, pinned
hashes, unresolved decisions, and validation results. Full baseline and post-edit
closed-schema validation passed for all **15,910 normalized records**, with zero
errors. The ID gate also passed. The preceding regression selection passed **215
tests**, including source/record guards, all ten batch-integrity checks,
concentration audits, record I/O, and merge/freshness tests. The last batch's
rerun changed zero records and its 532 new snippets matched captured sources.
A [current read-back across all ten source-review batches](20261007-all-batch-readback-after-1399.json)
matched all 4,770 current record hashes, including one explicit hash-linked
successor, and all 23,906 original snippets. The new repair also passed its own
sixteen-snippet read-back and no-op rerun. An independent semantic diff verified
the cumulative quantities, scoped structural changes, and append-only provenance
above, with unrelated fields unchanged. The final standalone-solution
[1,770-source retrieval](20261007-source-fetch-3000-4770.json) finished without failures.
Ruff, Black, and `git diff --check` passed.
Missing/malformed source preparation-step metadata now blocks water correction;
report heading whitespace is trimmed without changing source names in data.
Existing merge-data failures are recorded separately. The full merge gates were
rerun after the DSMZ 1399 repair: 1,247 canonical-name conflicts and
3,286 fingerprint issues remain. The [freshness result](20261007-dsmz1399-stock-boundary/merge-freshness.json)
still reports 3,723 only-tracked, 3,864 only-generated, 1,469 changed, and 1,128
unchanged merge records. A maintained-merger check of M1308's actual fingerprint
group [preserved its solutions, references, and twelve new stock snippets](20261007-m1308-stock-followup/merge-retention.json).
The same check for [DSMZ 1399](20261007-dsmz1399-stock-boundary/merge-retention.json)
preserved the corrected medium and stock boundary plus all fifteen new medium
evidence entries.
The later solution batches preserve `ingredients` and `solutions`, the actual
merge input fields; root stock composition changes do not resolve these older
merge failures. No generated files were copied into the worktree.

`validate-products` was rerun but could not load ontology adapters because `oaklib` is unavailable;
`validate-references` exited 2 because `linkml-reference-validator` could not
be spawned. Neither unavailable check is counted as a successful validation or a
newly introduced data defect. Source checks do not validate secondary ontology
mappings or imply manual reading of every source sentence.
Checks used the isolated Python 3.11 environment after the maintained 3.13
environment hit an unrelated llvmlite build problem; no 3.13/CI pass is asserted.

The [frozen source inventory](20261007-source-inventory.json) supports resumable
review. All 4,770 entries now have their source pass; the five initially curated
standalone stocks were deliberately excluded from that queue. Do not confuse
completion of this solution-only queue with completion of the full all-record
objective. The separate medium-source queue has completed its first 1,000-record
pass, not all 3,329 entries; its stock and variant conflicts also remain open.
The coverage snapshot and unresolved findings above define remaining
work, including both outside-report records and unresolved claims within reports.

A fetch during the earlier batches found `origin/main` at `62d4ea2934`
(shared-schema synchronization, PR #568), one commit ahead of the reviewed local
baseline. Its diff does not alter the concentration fields used here. The dirty
curation branch was not automatically rebased, committed, or published.
