# Bristol Child Preparation Triage

Read-only source observations, not canonical per-record reviews or validated
apply proposals. The three complete local records were read. Their official
HTML pages and the Botryococcus/Proteose PDF text were inspected through the
web tool on 2026-10-10 UTC. No child PDF image or byte capture was inspected in
this triage. No recipe, report-coverage count or curation history changed.

## Botryococcus

Local path: `data/normalized_yaml/algae/Botryococcus_Medium.yaml`.

The [official recipe](https://utex.org/products/botryococcus-medium) distinguishes
a 940 mL Bristol input, 1 mL of phosphate stock and a one-litre final medium. Its
phosphate final-concentration cell is `0.151 mM`; that is not the stock strength.
The existing top-level notes incorrectly call it a 0.151 mM stock. The quantity
and root-note claims need separate evidence dispositions.

The source instructs: "Bring total volume to 1 L with dH2O." The existing 59 mL/L
water number is subtraction, not a source-reported fixed water amount. Audit
the volume-additivity assumption before certifying that number; retain make-up
instructions if the numeric water field is removed. Do not expand the Bristol
parent's ingredients as if they were undiluted in the child.

## Proteose

Local path: `data/normalized_yaml/algae/Proteose_Medium.yaml`.

The [official recipe](https://utex.org/products/proteose-medium) gives a one-litre
batch, one litre Bristol input and 1 g/L proteose peptone. Both existing structured
quantity fields need evidence. The optional solid formulation is separate:
"For 1.5% (w/v) agar medium: add 15 g of agar into the flask; do not mix."
Do not silently add agar to the liquid base record. The supplier catalog's
ingredient identity has not been independently rechecked in this triage.

## Bristol-NaCl

Local path: `data/normalized_yaml/algae/bristol_nacl_medium.yaml`.

The [official recipe](https://utex.org/products/bristol-nacl-medium) states:
"Prepare Bristol Medium through step one." It then adds NaCl before final volume
adjustment. The table's one-litre Bristol row cannot by itself certify the local
claim of dosing 1000 mL of finished Bristol per litre of finished child medium.
Reconcile the preparation stage with both parent and reciprocal child link notes.

The source separately lists the salt addition as 3.6 g/L and reports 0.062 M.
Any evidence must distinguish that addition from salt already present in the
Bristol base. No independent mass-to-molar conversion is claimed here. The agar
option remains outside the liquid formulation.

## Handoff

Capture the child sources, pin current recipe hashes, review every quantity and
relationship claim, resolve preparation-stage representation, and run baseline
gates before generating any apply plan. The two-parent structured preview and
these child observations do not constitute review of the entire Bristol/Bold
family.
