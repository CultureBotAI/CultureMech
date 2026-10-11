# Next Stock Candidates

Subsequent status: the nine 546/659/670 targets were corrected in the
[stock-stage follow-up](../20261007-dsmz546-659-670-stocks/README.md). The frozen
JSON remains their historical before-state, not their current hashes. The three
673 targets remain unresolved; the newer follow-up also pins 670/673/266 PDF
captures and documents the separate 670 strain-variant conflicts.

Read-only investigation, not an approved apply plan or new completed reviews.
The companion JSON pins the exact then-current records and previously captured API
responses. Re-read entire records, primary recipes and evidence before proposing
changes. The original PDFs below were text-inspected through the web tool in
this follow-up; no visual inspection or new hashed PDF download is claimed.

## Explicit Stocks

- [DSMZ 546, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium546.pdf):
  990 ml water plus separate 5 ml additions of 1 M calcium chloride dihydrate
  and magnesium sulfate heptahydrate after cooling. This corroborates the API.
  The two medium records flatten these to mass concentrations; solution 1205
  also has water encoded as 990 percent. Prefer explicit stock strength/dose
  rather than molecular-weight conversion. Input-volume sums do not establish
  a measured final volume.
- [DSMZ 659, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium659.pdf):
  a post-autoclave 1.2 ml addition of 1 M calcium chloride dihydrate is distinct
  from the explicitly requested lactose concentration of 8 g/l. The three
  records flatten calcium chloride as 1.2 g/l or percent. Preserve the lactose
  final-medium claim separately; the source does not specify its stock strength
  or addition volume. The water input is 1000 ml.
- [DSMZ 670, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf):
  50 ml of a 40% w/v iron sulfate heptahydrate stock prepared in 0.2 N sulfuric
  acid is distinct from 950 ml base-water input. Preserve the acidic carrier,
  filtration and nitrogen instructions; do not invent a carrier-volume amount
  or treat the separate 4 N pH-adjustment reagent as the stock carrier.
  Strain-specific alternatives in this PDF are not simultaneous additions to
  the base recipe. Inspect them as variants, not automatic base corrections.

## Unresolved Parent Conflict

[DSMZ 673, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium673.pdf)
explicitly modifies medium 266: yeast extract 1 g/l, peptone 5 g/l, NaCl 25 g/l
and pH 7.2. Its captured API preparation text nevertheless carries the parent's
20 ml 10% w/v yeast-stock instruction, which corresponds to 2 g input rather
than the modified concentration. Do not restore that parent dose unchanged.

The [original medium 266, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium266.pdf)
itself has sulfur 5 g in the ingredient table but 10 g in preparation text.
The sulfur discrepancy is therefore present in the primary recipe, not merely
an API transcription problem. Both sources also require attention to separately
prepared sulfide and anaerobic handling. Do not choose a sulfur amount by
majority vote or copy stock concentrations into final-medium fields. Keep the
conflict explicit pending resolution. No DOI, author or publication year is
inferred from the copyright footer.

These twelve candidate snapshots do not enlarge unique reviewed-path coverage.
The next unreviewed KOMODO cohort still begins at offset 2500; this follow-up
does not replace the rest of the all-record objective.
