# Next Ingredient Corrections

The PDF extraction defect is locally fixed, but the all-record objective remains
active. No normalized YAML changed in this validation follow-up. The prior
5,167 edited records, 32,948 evidence entries and 11,784/15,910 follow-up paths
are unchanged; covered records may still have unresolved claims.

## BSK Formulations

Continue the three source-specific BSK candidates pinned in
[`next-bsk-context.json`](../20261008-dsmz-albumin-preparations/next-bsk-context.json).
All remain unedited. Do not combine these formulations by name similarity.

DSMZ 1829 was re-read completely, along with the API, original PDF text and page
image. Fresh binary/text hashes match the prior capture. It explicitly specifies
final volume 100 ml, unlike the earlier 403 stock preparations.

- Keep the nine existing mass concentrations after attaching row plus final-volume
  evidence: HEPES 5.1, citrate dihydrate 0.5, glucose 4.2, pyruvate 0.6,
  N-acetylglucosamine 0.3, bicarbonate 1.8, genuine yeast extract 1.7,
  Bacto peptone 4.2 and MEM alpha Modification 8.9 g/L. Existing chemical
  groundings are not recertified by this amount check.
- Replace only false LB nodes 8-10 with fraction V albumin: 0.85 g / 0.1 L =
  8.5 g/L. Preserve genuine yeast extract at old index 6.
- Rabbit serum is 8.56 ml per 100 ml final medium, giving 85.6 mL/L, not the
  existing 8.56 g/L. No density assumption is needed for the volume ratio.
- Restore deionized water as makeup to final 100 ml, not a fixed 100 ml addition.
- Model the 1 M NaOH titrant at stock scope with no invented dose or final
  concentration. Preserve final pH 7.3.
- Preserve Becton Dickinson peptone and BioWest P0440 MEM product context; do not
  copy a CMRL composition from other BSK recipes.
- The preparation says filter-sterilize without a pore size. Replace the
  unsupported `FILTER_STERILIZE` enum's implicit 0.22 micrometers with `FILTER`
  and the exact source-supported description. Remove the false LB product note
  with scoped evidence, preserving unrelated notes and history.

JCM173 and TOGO M2410 were also re-read completely with their captured API/HTML
sources. Their incompatible serum treatment, CMRL inputs, NaOH normality and
filter sizes remain in the [prior handoff](../20261008-dsmz-albumin-preparations/next-work.md).

- JCM173's first pH/filtration instruction precedes the instruction to autoclave
  B, combine A/B and add serum. Reconcile it at that pre-combination stage; do
  not assert that the final combined medium was measured at pH 7.6 merely from
  this sequence. The API assigned the entire procedure to B; that placement
  must not make every component an autoclaved component.
- JCM173 API `g_l` values can only be explicitly attributed at stock scope,
  not final-medium scope. Its two water inputs are 500 and 100 ml, and neither
  independently establishes a measured stock final volume or a parent stock dose.
  Neopeptone's 2.5 mg is corroborated by the original and is not a transcription
  correction to 2.5 g. Preserve the evidence despite its unusual value.
- M2410's pH adjustment is before gelatin and serum additions. Keep the
  temperature-specific adjustment instruction without inventing a measured final
  pH. Its 900 ml water and 100 ml CMRL are batch inputs, not mass concentrations.
- M2410's gelatin stock has an explicit 200 ml dose but only an unexplained
  7 percent strength. The final rabbit-serum instruction says 6 percent with
  no stated basis or fixed dose. Neither permits silently choosing w/v or v/v,
  computing gelatin mass, or inventing serum volume.

The [article access follow-up](barbour-source-access.md) found a parsed-text match
for M2410's recipe in both a mirrored Barbour 1984 paper and the official
university PDF endpoint. Both direct binary downloads were forbidden and page
images were not inspectable, so the article is not yet
accepted as original-PDF amount evidence. Do not substitute it for the available
TOGO capture or claim successful access through the university permalink.

## Other Open Work

- Correct the 41 PDF bibliography title claims documented in the local issue.
- Continue the unchanged 107 identity candidates and separate 71-record M142
  queue. They are not additive to the 4,126 paths outside follow-up reports.
- Address the remaining reducing-stage and source-conflict reviews, global
  merge verification and generated-data freshness failures.
- Publication is incomplete. The prior external-disclosure rejection for the
  issue #150 progress draft still has no additional approval; do not bypass it.

Use the guarded mutator, independent claim audit, per-record supplement/canonical
report reconciliation, corpus checks and merge-retention workflow for actual
YAML edits. Revalidate all baselines and queues against current files first.

Implementation caution: DSMZ1829 and JCM173 each have a genuine `Yeast extract`
node and a false supplier-tagged LB node with the same label. The shared
`repair_methanogen_stock_boundaries.Review` initializer rejects duplicate labels.
Use explicit baseline pointers with identity/old-value guards for this cohort;
do not weaken unrelated batch helpers or select a node by label alone. Preserve
the existing legacy JCM173 mapping alongside other unaffected annotations unless
separate source-backed grounding work justifies a change.
