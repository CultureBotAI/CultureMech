# Remaining Ingredient Work

Superseded handoff: the prepared DSMZ/KOMODO 403/751 repairs are now applied in
[the next batch](../20261008-dsmz-albumin-preparations/README.md). Its
[next-work report](../20261008-dsmz-albumin-preparations/next-work.md) has current
queue counts and three still-unedited BSK candidates. The baseline analysis below
is retained as historical preparation, not a claim that those four are still pending.

The all-record goal remains active. This batch applied M194/M213/M244/J252 only.
Follow-up coverage is 11,784 of 15,910 exact normalized paths, with 4,126 outside
these reports and unresolved claims within covered records.

## Queues

`next-lb-identity-context.json` retains 111 unchanged candidates: 76 acid-name
and 35 albumin-name substitutions. SHA256:
`4d3b297916a66cfacb223656150877ec420d38010b0662fe383c6f46dd7303ed`.
The separate M142-dependent queue retains 71 unchanged records. These queues
are disjoint but are not additive to the uncovered-path count.

## Next DSMZ/KOMODO Pairs

`next-dsmz-albumin-context.json` pins four unchanged current baselines, fresh
MediaDive 403/751 responses, original DSMZ PDFs and their extracted text. SHA256:
`5767d9b9bed74466a4f490abe98b1d9735d7b864cfaec8af0d83b29520ee7cdb`.
All four complete YAMLs, both API responses and both original PDF pages were
read. PDF table alignment and symbols were visually inspected with JPEG renders.
Poppler is not installed in the searched Homebrew Cellar locations; extraction
used installed pypdf and rendering used macOS sips. Binary PDFs are hash-pinned
under ignored `references_cache/ingredient-albumin-next/`; do not stage them.
The PDF text extractor emits a private-use U+F0B0 character for the degree sign;
the page images confirm degrees Celsius. Preserve extraction provenance and
check literal snippets against the captured text instead of silently rewriting
quotes. The printed 2007 copyright is not a verified publication year.

- D403: `data/normalized_yaml/bacterial/bsk_medium.yaml`, `CultureMech:001513`,
  baseline `c345efa5f105c5d705165808a726dbac94f41a0edcc46e0bd8e6db68bf39a444`.
- K403: `data/normalized_yaml/bacterial/KOMODO_403_BSK-MEDIUM.yaml`,
  `CultureMech:005218`, baseline
  `6f1ce7009904b3a88cb0e4654926f8790e96cd3b47c226c7747155b926a0e87f`.
- D751: `data/normalized_yaml/bacterial/sc_medium.yaml`, `CultureMech:001884`,
  baseline `26e0ce906baf0b63115a989a7f4ededbdd4ff53021090de54c334e24ab2c75f6`.
- K751: `data/normalized_yaml/bacterial/KOMODO_751_SC_medium.yaml`,
  `CultureMech:006403`, baseline
  `cafa2439ebe6c2bae319c5de6ebb647fe51b881aebafc32c0beed2d4a2bfb4da`.

### DSMZ 403

The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium403.pdf)
has four separate preparations. API solution IDs are 818-822: a four-dose parent,
twelve-row A, two-row B, two-row C and one-row D. Only false LB nodes 13-15 in
each baseline should be removed; genuine tryptone peptone and yeastolate remain.

- Reconstruct A-D boundaries. The merged 1,243 water value combines 900 ml in A,
  200 ml in B and 143 ml in C. Preserve and explicitly supersede the old duplicate
  note; separate those water inputs without using their sum as final volume.
- A contains 100 ml of a named CMRL product, not 100 g/L; retain its source
  product qualifier without inventing a composition. Source-labelled 5 M NaOH
  adjusts A to pH 7.6, with no fixed dose. The PDF supplies its temperature/time
  context and filtration. K403's existing titrant must be scoped to A; D403 needs
  a source-backed titrant representation rather than a guessed concentration.
- B uses 14 g gelatin with 200 ml water. C uses 50.05 g albumin fraction V with
  143 ml water, with the specified Sigma product or its stated commercial-solution
  alternative. The API declares stock rates 70 and 350 g/L; if retained, attribute
  them only as provider-declared stock values, not independently measured final
  volumes or receiving-medium concentrations. Do not double-count alternatives.
- D is 86 ml inactivated rabbit serum, not 86 g/L. Preserve source product detail.
  API parent doses 1,000/200/143/86 ml are provider-declared; summed API volume
  1,429 ml does not prove a measured final-medium volume.
- The PDF permits adding B after filtration and separately describes purchased
  BSK-H as an alternative. Neither is another simultaneous ingredient or permission
  to import a typical commercial formulation. Use FILTER without a pore-size guess.

### DSMZ 751

The [original recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf)
and API solution 1537 have ten rows. Both current records have eleven ingredient
quantity fields and false LB nodes at indices 6-8. Preserve their reciprocal
SOURCE_DUPLICATE parent/child links after verifying the repaired formulations agree.

- Restore 10 ml of the 20% albumin fraction V preparation. Percentage basis is
  unspecified, unlike JCM252. Do not infer stock mass or strength from the API's
  calculated receiving-medium `g_l` field.
- Hemin is a 15 ml dose of a 0.1% preparation in 0.05 N NaOH, not the current
  0.015 g/L assertion. Restore the solvent boundary without converting normality.
- Glucose is 5 ml of 10% stock, not JCM220's 1 ml of 50% stock. Cysteine is
  explicitly free base, supplied as 10 ml of 10% stock. Preserve this form.
- Albumin/glucose/cysteine are added after basal autoclaving and cooling to
  50 C. Hemin occurs before this boundary. Use the PDF heading and API's
  `recipe_order: 8` preparation marker together; do not move every stock late.
- The liquid option omits corn-meal agar and replaces the two phosphate batch
  amounts with KH2PO4 1.5 g and K2HPO4 0.5 g. Represent it as a source-supported
  variant, not a sequential preparation step that changes the solid base recipe.
  D751 currently stores that option as a root preparation step; K751 lacks it.
- Water is a 1,000 ml batch input. Corn-meal agar's legacy pure-agar annotation
  is not automatically recertified by a concentration repair.

An ignored-inclusive exact-path search found one canonical concentration report
for each of these four records. Recheck before generating supplemental reports;
do not add another `- Record:` line elsewhere. New previews must reconcile current
IDs, append-only history, supplier nodes, source versions and existing links.
No next-candidate edits or review-coverage increments are claimed here.

## Other Outstanding Work

Keep corpus scans serial with tests unless every mutation test is known isolated.
This batch fixed two resolver tests that created/deleted real normalized YAML
during scans. Preserve the initial failed ID receipt and the serial recheck;
do not describe the failed invocation itself as a pass.

M247/M272/M273/M274 prepared reducing-stage sources, the M273/M274 FeSO4 source
conflict, J151/M142 bibliography gaps, and the broader uncovered corpus remain.
Global merge/freshness gates are not waived by target retention. Publication is
unfinished: the prior issue #150 progress draft remains unposted after an
external-disclosure rejection, with no new authorization. The historical LB issue
draft is local too. Do not bypass that rejection through another channel.
