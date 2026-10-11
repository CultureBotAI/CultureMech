# Original-Source Percent Supplement Repairs

Five existing normalized records were repaired locally against baseline commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`: DSMZ 618 and 956, their two KOMODO
source wrappers, and the existing KOMODO methylamine-specific variant. No new
record, ID, or growth association was created. The all-record goal is unfinished;
these changes remain uncommitted.

## Scientific Scope

Both complete original recipes were visually inspected:
[DSMZ 618](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium618.pdf) and
[DSMZ 956](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium956.pdf).
Each gives starting water and subsequent percent supplementation without defining
the percentage basis or final receiving volume. A starting liter of water is not
an explicit final-volume makeup. The API's nominal g/L columns do not supply that
missing information. DSMZ 618's original agar instruction is a batch mass, whereas
the API encodes it as a per-liter rate.

The exact three [KOMODO table](https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList)
rows link those original PDFs. The replacement accession explicitly selects
methylamine. Source linkage was checked before curating each wrapper; another
local record was not used as concentration evidence.

- Removed 31 unsupported final mass-concentration slots. This is not a claim
  that all 31 numerical values were experimentally disproved: their asserted
  denominator or percent-to-mass conversion is unsupported.
- Relocated 23 base input nodes, preserving each stated mass in notes and an
  exact source excerpt. Difco attributes and chemical forms were retained.
- Added five explicit 1 L starting-water amounts, not five final-volume claims.
- Preserved Tween 80 at source-stated 1.0%, methanol at 0.5%, and methylamine
  at 0.3% in scoped notes/variants without assigning percent units or density.
- Moved the two alternatives into separate inline options in each generic 956
  source record. Neither is selected as a silent default; the common base is
  not asserted to support growth without supplementation.
- Reused `CultureMech:006899` for the methylamine-specific branch, removed its
  methanol node, and added reciprocal links to the common-base family.
- Corrected seven earlier evidence scopes. Their original API snippets and
  prior curation history remain intact; the former final-concentration claims
  are explicitly withdrawn in the successor plan and replacement explanation.
- Added 43 evidence entries for 48 scoped claims, eight references, and five
  append-only agent-authored events. Removed alternative nodes and their old
  ontology annotations remain in the change events, not as new grounding claims.

The scalar schema has no plain mass-per-batch slot, so input masses remain in
notes with evidence. Neither `VARIABLE` nor a fabricated final volume is used
to hide this representation limit. Percent bases and final concentrations remain
unquantified. Stable IDs, existing unrelated metadata, pH and physical state were
preserved. Unknown authors/year are not invented; 2007 copyright notices are not
used as recipe publication dates.

## Provenance And Replay

[plan.json](plan.json) freezes full before/after records, hashes, claims, and
the seven explicit claim resolutions. The repair checks exact tracked paths,
full baseline semantics, both PDF hashes and complete extracted text, the API
captures and water identity, and all three KOMODO rows before writing. Every
scientific edit has a source URL and literal snippet in the YAML itself.

Source capture SHA256 values:

| Source | SHA256 |
| --- | --- |
| DSMZ 618 PDF | `cd503969dc2f910a9b50c270952adf4c00eaffb09762b02a50e60c23555d8f20` |
| DSMZ 956 PDF | `156fe7f9a826c658bf690c9c892ba7d137848d397f55cf93568c4c3145374f39` |
| KOMODO table | `d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a` |

The earlier [scope handoff](../20261007-mediadive-media-2000-2500/earlier-preparation-handoff.json)
and both historical DSMZ cohort reports remain unchanged. The two successor
reports use `- Follow-up target:`; the three new KOMODO follow-up reports each
use one exact `- Record:` line under [records](records/).

## Validation

[validation.json](validation.json) records actual terminal commands and logs.
All seven baseline jobs and 36 post-apply jobs are terminal.
The current focused selection passes **704 tests**, including 55 repair tests.
Baseline and post-edit strict scans cover all 15,910 normalized records without
errors. All five target schema checks, canonical IDs, guarded readback/no-op,
seven earlier medium readbacks and JCM 896/JCM 1105/KOMODO 12 readbacks pass.
Both variant-link scans have zero errors and warnings; the post-edit scan has
2,986 reciprocal parent/child links. The seven withdrawn claims are checked
explicitly by the second/third batch readbacks, not skipped.

These are isolated Python 3.11 results, not maintained-runtime or CI passes.
The existing pure-Python pypdf package was supplied through `PYTHONPATH` without
changing dependency pins or installed environments. Product validation lacks
`oaklib`, reference validation lacks its executable, and the full suite lacks
coverage support and other imports.

The independent [cumulative diff audit](../20261007-diff-audit-after-percent-supplements.json)
passes: 4,849 edited records, 28,074 new evidence entries, 4,882 references,
4,855 curation events, and 1,164 quantity corrections. Structural changes include
97 relocated stock nodes, 40 new quantity slots and 37 unsupported slots removed.
The [exact-path coverage audit](../20261007-followup-coverage-after-percent-supplements.json)
passes with 8,102 unique follow-up records; 7,808 normalized records remain
outside these reports. Report presence does not mean every claim is verified.

The [actual-group retention gate](merge-retention.json) fails: three of five
records pass across three groups. DSMZ 618 and 956 lose some scoped evidence,
references, or child links when their KOMODO wrappers are selected. The two
exclusive supplement options survive, and the methylamine-specific branch
remains distinct. All authoritative YAML evidence remains intact.

Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. Black and Ruff pass for the six current repair/audit/test files;
`git diff --check` passes, as does the ignored-inclusive trailing-whitespace
check of the new repair, tests, audits, and documentation.
[Freshness](merge-freshness.json) fails: 6,320 tracked and 6,492 fresh records,
with 3,719 only tracked, 3,891 only fresh, 1,645 changed, and 956 unchanged.
Regeneration was temporary only. No generated merge was published.
