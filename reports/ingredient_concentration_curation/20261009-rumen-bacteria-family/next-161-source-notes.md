# Medium161 Source Preparation

Read-only preparation, not a completed concentration review or an applied batch.
No normalized record, canonical report count or evidence total changes here.

The [approved discovery receipt](next-161-discovery-approved.json) preserves
three official public source captures. The initial network failures remain in
`next-161-discovery-initial.json`; successful discovery did not erase them.
The [exact-root inventory](next-161-local-inventory.json) pins the full current
15,910-record corpus and six local records with their full original text.
Filesystem enumeration included ignored files and was reconciled to exact git
paths. One root record matches each of KOMODO161, MediaDive161, and MediaDive
solutions209, 241, 277 and5980. No normalized root accession matches
`mediadive.solution:2618`. Nested references are not standalone records.

## Original PDF Inspection

Both rendered pages of the captured [DSMZ medium161 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium161.pdf)
were visually inspected. Source PDF SHA256 is
`0f4ea6194efcb146abe36366dd72ce890643e9cfe39bc947a9df7281959478e0`;
rendered-page paths and hashes are retained in the local inventory receipt.

- Page1 explicitly states `Final volume: 1001 ml` and `Final pH: 6.5`.
  Eighteen main rows distinguish mass inputs, prepared reagent doses and
  stock-solution additions. The arithmetic sum of listed liquid inputs is
  1001.5 ml; it must not silently replace the source's nominal final volume.
- The clarified-rumen-fluid subsection is procedural. Its 30% vial filling
  instruction concerns storage, not a final-medium concentration. No numeric
  ingredient composition may be invented for its separate source accession.
- The mineral-stock heading is at the bottom of page1; its sixteen rows
  continue on page2. Selenium and tungsten inputs use mg, not g. Its titrant
  amount is unspecified, and its listed water input alone does not establish
  a measured final volume.
- The five fatty-acid-stock rows on page2 use ml; liquid inputs must not become
  percentages or mass concentrations without supporting basis or density.
  The separate NaOH titration gives a target pH, not a fixed added amount.
- The eleven vitamin-stock rows on page2 include mg inputs and water. Keep
  this stock's preparation distinct from its dose in the main medium.
- The copyright footer is not evidence for a publication year or author list.

## Next Checks

Read every existing quantity and evidence path in the six pinned records;
preserve prior supported evidence. Compare exact standalone stock captures
with parent-medium rows before citing them as equivalent. Independently inspect
the KOMODO table, including chemical forms, displayed rates and null entries;
do not replace one provider's formulation with another. Re-evaluate exact family
paths and duplicate relationships. Baseline checks, complete claim decisions,
an independent proposal audit and guarded application are still pending.
