# Medium-119 Pre-Implementation Findings

This is a partial scientific review and implementation handoff, not an applied
batch. All nineteen normalized records remain unchanged. The full YAMLs for
DSMZ 119/119a/119b/119c and KOMODO 119/119.1 were read in this turn. The other
thirteen KOMODO variant records have frozen baselines and extracted ingredient
nodes but still require complete reads and claim adjudication.

All twenty-three sources were captured successfully; all nine PDF pages were
visually inspected. See `next-119-family-context.json`,
`next-119-family-preflight.json`, and `next-119-pdf-visual-review.json` for exact
paths, IDs, hashes, quantities, source snippets and unresolved path links.

## Confirmed Problems in the Six Read Records

1. Each has the false supplier-tagged LB expansion in place of the source
   methylbutyric-acid ingredient. Removal must be supplier-node-specific.
2. H2SO4 currently has 1,000 g/L. The original stock table instead specifies
   1,000 ml of 0.1 N sulfuric acid for the ferrous-sulfate solution. Preserve
   acid strength and stock preparation volume; do not infer a mass or molarity.
3. DSMZ 119, 119b and 119c combine basal yeast extract with the sludge-fluid
   preparation input as if both were finished-medium concentrations. Separate
   the source stages and retain the historical combined value in history.
4. Sludge is stored as 1,000 g/L although the source gives a 1,000 ml stock
   preparation input and a separate 50 ml processed-fluid receiving dose.
   The preparation includes incubation and centrifugation; it is not evidence
   that all starting yeast extract reaches the receiving medium unchanged.
5. Trace-stock components and liquid fatty acids are flattened into medium
   g/L. Restore stock stages, liquid units, makeup instructions and doses.
6. KOMODO 119 and 119.1 contain copied methanol and selenite/tungstate entries
   absent from their inspected source recipe tables. Their copied composition
   follows DSMZ 119b, despite a history note naming DSMZ 119. Preserve the
   history but replace source-mismatched current assertions with evidence.
7. KOMODO 119.1's captured source has vitamins, Trypticase and rumen fluid
   that its copied normalized recipe omits. Do not use the false LB tryptone
   node as proof that genuine source Trypticase is already represented.
8. Existing exact-duplicate links, including KOMODO 119 to DSMZ 119b, rely on
   the copied composition and are not supportable from source identity.
   DSMZ 119 versus 119c also differs in gas preparation, not bicarbonate alone.

## Representation Decisions to Implement and Test

| Claim | Source locator | Required treatment |
| --- | --- | --- |
| DSMZ 119 base final volume | DSMZ119 PDF page 1, `Final volume: 1003 ml` | Use 1.003 L only for this explicitly identified base formulation; document each mass/1.003 conversion and its rounding. Do not transfer this denominator to 119a/b/c. |
| SL-10 stock final volume | Original PDFs, SL-10 preparation, `Finally make up to 1000.00 ml.` | Stock masses can be expressed per 1 L; keep receiving dose separate. HCl is a 10 ml input labeled 25%, with no inferred percent basis. |
| Fatty-acid stock inputs | DSMZ119 page 2 and corresponding variant stock tables | Four acids in ml plus 896 ml input water; concentrated NaOH titration has no fixed dose. No unstated density or final-volume conversion. |
| Ferrous-sulfate stock | Original PDFs, `FeSO4 x 7 H2O solution (0.1% w/v)` | Explicit stock strength and separate 2 ml receiving dose. Keep 0.1 N H2SO4 carrier context; no invented normality enum or g/L conversion. |
| Resazurin | Main tables, 0.1% w/v, 0.50 ml | Separate stock strength from receiving-medium dose. |
| Methanol in DSMZ 119b | PDF page 1, `Methanol (15% v/v)` and 10.00 ml | A 15% v/v stock with a 10 ml dose, not 10 ml neat methanol or its density-derived mass. |
| Sludge fluid | Sludge stock table and preparation | Separate 4 g yeast extract and 1,000 ml sludge inputs, processing, and 50 ml receiving dose. |
| Clarified rumen fluid | DSMZ119a page 2 | Preserve preparation and 200 ml receiving dose. The API stock has steps but no recipe rows; do not omit or invent its composition. |
| KOMODO Gram Amount | Each exact accession's recipe table and per-liter heading | Preserve reported precision and nulls, source qualification and conflicts. Do not substitute DSMZ current strain instructions silently. |
| Source-specific labels | Cysteine-HCl, Resazurin, 2-Methylbutyric acid, fluids and vitamins | Do not transfer unverified salt/stereochemistry/hydrate or pure-compound grounding from copied nodes. Archive withdrawn annotations; retain other annotations without claiming recertification. |

The independent audit must prove old-slot accounting even where one combined
yeast node splits into basal and stock-input nodes. A one-to-one old-name lookup
is insufficient. Test both directions of each reciprocal relationship and exact
path identity, not merely successful ID fallback.

## Conflicts That Must Stay Explicit

The later [exact source-table comparison](next-119-source-comparison.json)
compares all five source columns by exact ingredient label, ignoring row order
but not value precision. It finds the following KOMODO differences from K119:

| Accession | Source-table difference |
| --- | --- |
| 119_11975, 119_11977 | NH4Cl 10.40 rather than 0.40 g/L |
| 119_3468 | Adds methanol 5.00 g/L and unquantified N2 |
| 119_4855 | Adds cysteine 0.30 g/L and Na2S 0.30 g/L while retaining the separate hydrochloride/hydrate entries |
| 119_6216 | Na-acetate 3.99 rather than 0.99 g/L |
| 119_7057 | Adds Na2SO4 2.00 g/L |
| 119_7256 | Adds rumen fluid with provider-reported Gram Amount 200.00; this is not permission to infer a density or overwrite it with a volume |
| 119.1 | Twelve added rows including vitamins, Trypticase and rumen fluid; removes sludge; eighteen common rows have changed reported rates |

Other captured variants have identical five-column ingredient rows to K119,
but their identity, pH/aerobic metadata and linked strain instructions still
require review. Equal table rows alone do not establish exact recipe identity.
All thirteen underscore-variant normalized ingredient lists are structurally
identical to the fully read K119 list; a lossless structural comparison checked
every field, but the long metadata output was truncated and is not counted as
thirteen complete manual reads.

- DSMZ 6216 instructions say Na-acetate 3.00 g/L; KOMODO 119_6216 reports 3.99.
- The current DSMZ instructions for 11977/11978/11995/16643 omit sulfide and
  cysteine and add Wolin vitamins, dithiothreitol and coenzyme M. Captured KOMODO
  119_11977 retains reducing agents and reports NH4Cl 10.40 g/L. These are
  source/version disagreements, not permission to overwrite one with the other.
- DSMZ 15163 instructions omit sodium sulfide and add 0.3 g dithiothreitol,
  with final pH 6.0; its captured KOMODO table retains sodium sulfide.
- KOMODO 119.1 combines DSM 16632 and 16643, while current DSMZ instructions
  distinguish them. Its recipe may be represented as a provider-specific
  formulation, not a newly proven growth association for both strains.
- KOMODO 119/119.1 aerobic and pH metadata differ from the linked original's
  anoxic preparation and complete-medium pH. Preserve source scope explicitly.

## Source Links

The exact source URLs and snippets for all 645 extracted rows are in the
preflight. Main original recipes: [119](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf),
[119a](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119a.pdf),
[119b](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119b.pdf), and
[119c](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119c.pdf).
Provider-specific tables: [KOMODO 119](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=119)
and [119.1](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=119.1).

Do not count this handoff as nineteen completed reviews. Complete remaining
record reads, all source-row decisions, guarded previews, baseline checks,
evidence validation, independent audits and regression tests before applying.
