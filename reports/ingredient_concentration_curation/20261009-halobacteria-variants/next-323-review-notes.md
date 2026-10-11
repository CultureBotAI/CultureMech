# Medium323 Follow-Up Inspection

This is source adjudication for the next four records, not an applied repair,
complete per-record concentration review or new canonical coverage. All four
record bytes still match the preceding captured baselines. The full-corpus
ingredient objective remains unchanged.

## Rechecked Evidence

The [captured sources](../20261009-synthrophomonas-family/next-323-captures-approved.json)
were reread, including the exact KOMODO HTML and MediaDive medium/stock data.
The single-page [DSMZ original](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium323.pdf)
was inspected visually again. Its PDF SHA256 is
`a9612ce4a0d0ab3cb0b8ec6924aa5076f1988dc4bc059a773dceb6898e2dceb7`;
the extracted-text hash is separately recorded in the capture metadata.

The original explicitly gives `Final volume: 1002 ml`. It gives the resazurin
reagent as 0.50 ml of 0.1% w/v solution. Therefore the existing 0.000499002 g/L
solute concentration remains supported after rounding; adding a second asserted
stock dose must not double-count the same input. The original also has a
separate fatty-acid-stock section with five volume inputs and a storage
instruction, not four direct medium mass concentrations or a heating step.

## Formulation Decisions

1. **Keep KOMODO separate.** Its own table explicitly says gram and mol amounts
   are per liter. It lists NaHCO3 at 5.67 g/L, NaCl at 1.02 g/L and glucose at
   2.27 g/L, not the copied DSMZ values currently in K323. Its 21 compound rows
   include nine null gram amounts. Do not replace those nulls with quantities
   copied from DSMZ or confuse the separate combined-SEED table with reagent
   amounts. Preserve source ambiguities in identity and physical state.
2. **Do not erase a supported solid selection in D323 by accident.** The current
   DSMZ record explicitly represents `SOLID_AGAR`; the original has a solid
   option. Its table-derived/provider agar value is 11.976 g/L, while the
   separate procedure says 12.00 g/l. A proposal can preserve the existing
   source-qualified value and disclose both bases; it must not silently turn
   the record into a liquid recipe, average the figures or assert equivalence.
   K323's solid classification is a different unresolved issue: its own table
   has no agar row and does not itself establish a liquid or solid selection.
3. **Keep reported mass rates distinct from volume inputs.** S6552 explicitly
   reports three g/L values (275.5, 131.46 and 130.34); their liquid starting
   reagents alone do not invalidate those provider statements. Its 290/140
   percent entries are unsupported. The exact 5.8/2.8 ml input volumes support
   batch-dose notes or volume-valued inputs, not an independently established
   final percentage or an assumed density.
4. **Do not inherit unrelated LB products.** Both medium records contain three
   appended LB ingredient/product entries. Removal must be supported by the
   complete exact source formulation and separate from restoring any real
   yeast extract, peptone or NaCl row. Prior history remains append-only.
5. **Preserve prior evidence and identity limits.** S599 has nine earlier
   evidence entries to retain. Glucose, resazurin and cysteine mappings require
   explicit treatment; this inspection does not recertify or replace their
   existing ontology IDs. New quantities must not silently change chemical form.
6. **Represent the missing S599 stock dose honestly.** Its exact provider row
   specifies 1.4 ml of solution 6552, but neither `SolutionRecipe` nor its nested
   `SolutionDescriptor` has an evidence slot. This record has no `source_data`,
   whose origin means imported source-repository provenance. The
   [captured schema-gap finding](next-323-schema-gap.json) requires a legitimate
   formulation-evidence container before asserting this nested dose; do not
   fabricate import provenance or use unrelated ingredient evidence as a workaround.

A complete guarded proposal, full old/new claim accounting, schema checks and
independent mutation tests are still required before these four records change.

## Isolated Schema Probe

The [current-schema probe](next-323-evidence-probe.json) confirms that the
closed validator and generated `SolutionRecipe` class both reject root evidence.
An [isolated successor prototype](next-solution-evidence-prototype-v2.json)
adds only an optional root evidence list to a temporary schema. All four
baseline records validate, generated dataclasses preserve the dose and snippet
on round-trip, and unknown root/evidence fields and inline solution evidence
remain rejected. No authoritative schema or record is edited.

The first prototype exposed a separate bibliography problem: the existing title
`MediaDive solution 599: Main sol. 323` does not match the provider's literal
`Main sol. 323` (`$.data.name`). Its new root evidence passed, but the title check
failed. That [failed receipt](next-solution-evidence-prototype.json) and its
[eleven-check diagnostic](next-schema-prototype-reference-diagnostic.json) are
preserved. The successor corrects the title only in memory; all eleven checks
then pass against the pinned capture, with network access disabled in the probe.

A production fix still needs the authoritative schema, generated Python/JSON
Schema/docs, the skill's evidence contract and focused compatibility tests
updated together. It must retain ingredient evidence on composition entries
and scope formulation claims to exact stock paths and preparation stages.
The temporary four-record check is not full downstream or corpus validation.
