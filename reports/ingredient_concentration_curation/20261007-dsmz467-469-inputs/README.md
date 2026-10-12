# Media 467 And 469 Input Repairs

Six authoritative normalized records have been repaired locally through the
[frozen preview](plan.json): the DSMZ and exact mapped KOMODO copies of media
467/469, plus standalone solutions 959/961. This is part of the unfinished
all-record objective, not completion of the concentration corpus.

The [independent applied audit](diff-audit.json) verifies thirty new evidence
entries, eight references and six appended curation events. Four existing
water-unit fields are corrected; six ingredient nodes move to separate stocks;
six unsupported stock-rate fields are removed; and eight source-explicit water
input fields are added. These are separate count categories, not thirty newly
determined concentrations. Ten existing evidence explanations receive explicit
scope corrections while their exact snippets and historical explanations remain.

## Scientific Decisions

- **Medium 467:** the official recipe specifies 1000 ml tap water. All three
  copies now encode 1 L of input, not 1000 g/L or 1000 percent. The six existing
  solute amounts and their evidence are unchanged. Neither density nor a
  measured final volume is inferred.
- **Medium 469:** magnesium sulfate heptahydrate and catalase are prepared and
  filtered separately. Their respective 0.2 g and 60 mg source batch inputs
  remain in scoped notes, with exact source-row and preparation snippets. No
  20 g/L or 6 g/L stock strength, final-medium rate, or numeric stock dose is
  inferred from the 10 ml water input for each stock.
- **Source detail:** the MediaDive API explicitly allocates 980 ml water in the
  base and 10 ml per filtered stock. The original DSMZ PDF lists 1000 ml without
  that allocation. The records follow the API's allocation and explicitly
  preserve the PDF difference. Both agree on separate filtration. The retained
  four non-stock g/L values are provider-reported nominal recipe rates, not
  concentrations in the 980 ml basal preparation or independently measured
  final-medium concentrations.
- **Preparation:** the DSMZ 469 action is no longer `AUTOCLAVE` for the mixed
  instruction; `ADJUST_PH` names its opening instruction and the full verbatim
  text is retained. The KOMODO copy gains that source instruction. No filter
  pore size or sterilization temperature/time is invented.

Primary source URLs, retrieval metadata, SHA256 hashes, literal JSON excerpts
and PDF excerpts are recorded in the YAML and plan. The original one-page
[467](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium467.pdf) and
[469](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium469.pdf) PDFs were
inspected, with local PDF bytes matched against the earlier source captures.
The KOMODO mapping establishes source identity only, not recipe amounts.
Individual authors and publication years remain unknown; the PDF copyright
year is not substituted for a publication year.

## Per-Record Results

These are hash-linked supplements to the existing exact-path reports, not six
additional unique reviewed paths. They preserve the original reports and
explicitly supersede only the identified claims:

- [467 DSMZ](467-dsmz-followup.md)
- [467 KOMODO](467-komodo-followup.md)
- [467 standalone solution](467-solution-followup.md)
- [469 DSMZ](469-dsmz-followup.md)
- [469 KOMODO](469-komodo-followup.md)
- [469 standalone solution](469-solution-followup.md)

The related TOGO M2316 and M3060 records were inspected locally: their water
units are already L. M3060 is an NBRC supplemented variant using distilled
water, not the DSMZ tap-water formulation. Both remain outside this repair;
their exact source evidence needs its own review. No variant links, IDs,
chemical mappings, organism claims, legacy solution placeholders or quality
flags were changed.

The [next medium-489 handoff](next-medium489-handoff.json) freezes three inspected
but unchanged records, their API/PDF sources and remaining preparation decisions.
It is not an applied plan or an additional reviewed-path count.

## Verification

The [adversarial review](adversarial-review.md) records the scientific defects,
guard changes and remaining limitations; it is not a hosted PR or human review.

All eight [baseline checks](baseline.json) passed: 194 focused tests, strict
validation of 15,910 normalized records, and open-schema validation of all six
targets. The [preflight](preflight.json) independently inverts every proposed
record change to recover the entire baseline. The [presentation review](presentation.json)
tracks changed text blocks; moved ingredient nodes and extended evidence
explanations account for the replacements, while unrelated YAML presentation
and historical events are retained.

The apply changed six records. Readback verifies all six result hashes and 59
scoped API-backed claims; reapplication changes zero records. The separate
applied audit also checks PDF evidence, source differences, quantities, stock
boundaries, historical provenance and unchanged whole-record fields.

Post-apply [validation.json](validation.json) is terminal. The final reruns pass
326 selected tests on isolated Python 3.11 and 249 on cached Python 3.13; these
are not a full maintained-project environment or CI run. Both initial test
failures remain recorded: a verifier checked record hashes before provenance,
changing the expected tampering diagnostic. Checking provenance first retains
both guards and fixes the regression. Explicit readback of the affected second
medium and solution batches also passes, alongside the earlier first-batch and
fourth KOMODO-batch checks. This does not claim source readback of every batch.

Full strict validation passes for all 15,910 normalized records, as do all six
open-schema checks, ID and variant-link gates, Ruff, Black and whitespace checks.
Product and reference validators remain unavailable (`oaklib` and
`linkml-reference-validator` dependencies); neither is counted as a pass.
The initial validation session disappeared
after its successful apply; the missing handle and process were verified, the
six applied hashes checked, and the remaining checks resumed without redoing
the apply. Unjournaled output was not treated as an exit-status proof.

The [actual-group retention audit](merge-retention.json) fails. Four media
participate in two current groups; the two standalone solutions are correctly
excluded. All forty record-scoped source snippets survive, but the DSMZ 467 and
469 copies do not retain complete ingredient/provenance/context fields. The
KOMODO copies retain all checked fields. In particular, the DSMZ 467 preparation
instruction is not preserved by selecting its KOMODO sibling. Shared quotations
do not prove retention of full explanations, bibliography, history or procedure.
This does not justify editing the scientific inputs merely to satisfy a lossy
merge rule. The authoritative six-record repair is retained; generated merges
remain unpublished pending a provenance-preserving pipeline repair.

Global merge verification still fails with 1,247 canonical-name conflicts and
3,287 fingerprint issues. [Freshness](merge-freshness.json) also fails: 6,320
tracked outputs versus 6,493 temporary regenerated outputs; 3,719 only tracked,
3,892 only fresh, 1,668 changed and 933 unchanged. The temporary run did not
publish generated merges. Of 32 journaled checks, the two initial test failures
are superseded by passing reruns; the effective 30 checks contain 25 passes,
two unavailable validators and three failing merge gates.

All edits remain local and uncommitted. No generated merge is hand-edited or
published, and no PR, issue closure, merge or branch cleanup is claimed.
