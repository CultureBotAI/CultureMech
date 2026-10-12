# Medium-829 Source Review and Repair Decisions

Read-only preparation initially covering eight source-linked records. A later
ignored-inclusive accession/reference search expanded the identified candidates
to fourteen: add DSMZ 829b/c/d, TOGO M2587, KOMODO2027 and MediaDive solution1680.
The original eight-record receipts remain immutable and are not evidence of
complete family coverage. See `next-829-extended-preflight.json` and
`next-829-companion-context.json`; shared-stock dependencies remain in scope.
No medium-829 YAML is
edited and no claim is counted as applied. All eight baselines have been read;
four identical KOMODO ingredient subtrees were checked losslessly against the
fully read base, with their stock candidates, history and other fields read
separately. The immutable context includes ten successful public source captures.
The preflight inventories 246 source rows and 252 existing quantity slots.

## Source Identity

`next-829-family-context.json` pins every baseline and capture. Source-specific
row excerpts, persistent URLs, headings and locators are in
`next-829-family-preflight.json`; `next-829-source-comparison.json` compares all
six KOMODO tables. All four original PDF pages have been visually inspected.
`next-829-source-review.json` records per-row representation decisions, not a
complete guarded old/new record proposal.

All sixteen baseline schema/strict commands pass in `next-829-baseline.json`.
`next-829-old-slot-review.json` maps all 252 existing quantity fields and eight
cross-medium stock-dose candidates to source scope, removals or replacements.
It does not yet assign final after-YAML field paths or authorize an untested write.
`next-829-evidence-supplement.json` adds separately located stock-strength
headings and the final-volume discrepancy discovered during adversarial review;
the earlier receipts remain immutable.
The independent `next-829-source-audit.json` passes all 246 source-row checks,
rejects 246 invented-quantity challenges and verifies exact coverage of the
252 old fields and eight candidates. This checks source decisions, not an
after-YAML transformation that has yet to be built.

The source-accession search includes DSMZ 829a even though the old relationship
graph did not link it. Existing links have no stale exact paths in this family,
but several relationship claims are scientifically unsupported.

## Required Repairs

| Target key | Decision |
| --- | --- |
| D829 | Preserve basal masses using the original's explicit 1005 ml final volume. Restore six separately scoped stocks/indicator preparations, full compositions and receiving doses. Remove false LB expansion; restore both methylbutyric acids. Move stock-only preparation out of root steps; preserve the original's conditional DSM 16661/21157 modification. |
| D829a | Retain exact basal batch masses, without the unverified 1020 ml denominator inferred by the API. Restore resazurin 0.1% w/v and neutralized sulfide 3% w/v stocks, with 0.5 ml and 20 ml receiving inputs respectively. Keep sulfuric-acid titration unquantified and stock-scoped. |
| K829 | Rebuild from its exact 36-row Gram Amount table and nulls, not copied DSMZ stock-strength values or partial stock nesting. Preserve provider-specific sodium bicarbonate and dithionite differences explicitly. |
| K829a | Replace the incorrectly copied 829 formulation with its distinct 13-row exact-accession table. It names salts/thiosulfate, not the sea-salt/growth-factor base. Its source says `Is Complex: false`; correct the copied classification consistently. Link source derivation to D829a, not an exact duplicate of K829. |
| K829.1 | The 36-row table removes sulfur and adds yeast extract 0.50 g/L, as well as pH 6.5. The existing pH-only relationship and assertion of identical components are false; use a strain-specific variant with these explicit differences. |
| K829.2 | The 37-row table differs extensively: sulfate trace salts, additional vitamins, sulfide and other source-specific rates. Preserve pH 6.0-6.5 rather than the extra unsupported fixed 6.0. Replace exact-duplicate semantics with a source-qualified strain variant. |
| K829.3 | The 30-row table omits six growth-factor acids and changes 23 remaining rows relative to K829. Retain strain-specific scope but correct the existing claim of unchanged components. NaOH is explicitly quantified here, unlike the base table. |
| K829_16661 | The 36 displayed rows equal K829, but pH is null and strain metadata differ. Withdraw copied fixed pH 6.0 and exact-duplicate semantics. Preserve the conflict with the original's instruction to omit growth factors; do not silently substitute that formulation. |

K829 and D829 have explicit source linkage but are not exact formulation
duplicates. Correct reciprocal family metadata with evidence. Do not infer a
D829-to-D829a derivation direction merely from adjacent source accession numbers.
No taxa-media growth association is implied by this ingredient review.

## Stock and Volume Boundaries

- The original DSMZ 829 page 1 states `Final volume: 1005 ml`. This supports
  its base recipe's direct mass conversions only, using mass / 1.005 L.
  The listed liquid inputs sum to 1005.5 ml, not 1005 ml. Preserve this discrepancy
  explicitly: the reported denominator is not independently verified physical
  volume, and the input sum must not silently replace it. DSMZ 829a inputs sum
  to 1020.5 ml; its API volume 1020 ml is likewise not an original final-volume
  statement. A source-reported rate is distinct from a reconciled final volume.
- SL-10 explicitly makes up to 1000 ml. Its eight metal/borate mass inputs can
  be represented as stock concentrations; HCl is 10 ml of unspecified-basis
  25%, not a density-backed gram amount. Preserve the 1 ml receiving dose.
- Growth factors are five-gram isobutyric, valeric and two methylbutyric inputs,
  two grams caproic acid, six grams succinic acid and 1000 ml water. They are
  masses, not the liquid-acid volumes used by some other medium families.
  No final stock-volume statement was found in the inspected three-page PDF;
  retain batch masses and unquantified NaOH titration to pH 9.
- Selenite/tungstate and seven vitamins similarly state water inputs rather
  than explicit stock final volumes. Preserve exact batch quantities, not
  invented final-medium concentrations. Existing partial stocks must not
  coexist with their copied root ingredients after repair.
- Dithionite explicitly states 5% w/v. Its NaOH input is 0.50 ml of 1 N carrier,
  with 0.50 g dithionite and 9.50 ml water. Preserve preparation, storage and
  1 ml receiving dose separately; do not collapse this NaOH with a different
  stage's 0.50 g NaOH.
  The stock-strength heading must accompany the ingredient-row evidence: the
  mass row alone does not prove a percentage. The same requirement applies to
  the neutralized-sulfide heading in DSMZ 829a.
- DSMZ 829a gives no final-volume heading on its inspected single page. Its
  250 ml screw-capped bottle is equipment, not a solution denominator. Sulfide
  is explicitly 3% w/v and separately added at 20 ml. Titration uses 2 M H2SO4
  dropwise to stock pH about 7, not a fixed final-medium sulfuric-acid amount.

## Source Conflicts to Preserve

- KOMODO 829 reports NaHCO3 at 1.00 g/L; current DSMZ 829 uses 0.50 g Na2CO3
  per base batch. Do not rename one chemical to the other.
- KOMODO's 0.02 g/L dithionite does not equal the original's 1 ml dose of a
  5% w/v stock. Preserve version/source scope instead of overwriting both.
- K829_16661 retains all growth-factor acids, whereas the current original
  explicitly omits them for DSM 16661 and DSM 21157. K829.3 does omit them.
- KOMODO aerobic metadata for five accessions disagree with original anoxic
  preparation. Report source conflict without inferring biological growth.
- KOMODO's displayed Gram Amount rates and rounded Mol Amount values need
  separate interpretation. Use neither to recalculate the other without exact
  chemical identity and independently verified molecular weight.
- Copied anhydrous nickel annotations do not establish hexahydrate identity.
  Do not impose sodium-resazurin or a stereospecific pantothenate grounding on
  less specific source labels. Preserve unrelated annotations without claiming
  that all ontology mappings were reverified.

## Before Application

The supplementary `next-829-expanded-review.json` covers all 189 source rows and
164 old quantity fields in the six additional candidates. Combined scope is
435 source rows and 416 old quantity fields, plus the original eight stock-dose
candidates. `next-829-expanded-audit.json` independently checks all new rows,
rejects 189 invented quantities and recomputes the volume discrepancies.
The additional twelve baseline checks pass, for 28 across fourteen candidates.
Ten original PDF pages have been visually inspected in total. No candidate YAML
has been edited by this follow-up; these are source decisions, not an applied plan.

Additional source-specific requirements:

- D829b retains its genuine 0.50 g yeast while withdrawing the separately tagged
  false LB ingredients. Its reported 1005 ml denominator differs from the
  1005.5 ml liquid inputs. Keep five stocks and indicator separately scoped.
- D829c reports 1011 ml, against 1011.5 ml liquid inputs; D829d reports 1020 ml
  against 1011.5 ml. Use only source-reported denominators, preserve each
  discrepancy and never invent makeup water. Both restore full mineral and
  vitamin stocks, including B12 at 1 mg per stock batch, not 100 mg.
- D829c's DSM 16304 pH 5.5 instruction is conditional, not a base pH or a
  prescription for D829d. Mineral-stock KOH titration is unquantified and
  stock-scoped. A 10x vitamin title does not establish a universal working dose.
- M2587 preserves its source-specific bicarbonate/dithionite stock: 50 g of
  each in 1000 ml water, with an explicit 5% w/v dithionite title. Current
  DSMZ's NaOH carrier must not replace it. Restore separate stock water inputs,
  mg quantities and receiving doses. Its recipe supplies no final-medium volume.
  The source's hydrogen-gas item conflicts with its N2/CO2 stock preparation;
  retain the discrepancy rather than silently selecting an atmosphere.
- K2027's exact table supports six provider-reported acid rates, with null water
  and NaOH amounts. Correct the old claim that the DSMZ original explicitly
  supplies g/L; it gives batch masses and water instead. Keep current record-kind
  ownership until classifier and merge implications have been inspected.
- S1680's six previously evidenced, qualified API rates remain supported by the
  unchanged refreshed capture. Correct only the unsupported water percentage
  and spurious placeholder, preserve prior evidence/history, and retain NaOH
  titration as unquantified preparation. Do not infer a universal stock dose.

Build a complete guarded proposal for all fourteen identified candidates, with a row for every old slot,
source node, removed copied ingredient, stock candidate and changed contextual
claim. Put exact supporting snippets and PURLs in the YAML, not just here.
Keep source titles, discovery mode, source type and access date; missing authors
and publication years remain unknown. PDF footer copyright years are not
publication dates. Preserve prior history and append one actual-change event
per record. Run baseline, focused/negative tests, independent audit, reference,
readback/no-op, corpus, merge and presentation checks before counting repairs.
