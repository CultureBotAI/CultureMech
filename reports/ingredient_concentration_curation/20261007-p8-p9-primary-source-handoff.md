# P8/P9 Primary-Source Handoff

Source acquisition and conflict review only. Neither target YAML was changed,
and neither has a completed ingredient-concentration follow-up report.
Reviewed baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.

| Target | Stable ID | Unchanged SHA256 |
| --- | --- | --- |
| `data/normalized_yaml/bacterial/m9_sng_medium.yaml` | `CultureMech:010438` | `250cc259402cfc6454d35f34240ff492d027b548fee1773ac6f5b238f08d1af4` |
| `data/normalized_yaml/bacterial/pdb_sng_medium.yaml` | `CultureMech:010439` | `2db91d841dd7a45fdd60c10c9cf7f7a495f76d243a3a8d5bc01eba6d5ce722fd` |

## Inspected Source

Lisa Martinez, Jean-Bernard Pouvreau, Gregory Montiel, Christophe Jestin,
Philippe Delavault, Philippe Simier and Lucie Poulin, *Soil microbiota promotes
early developmental stages of Phelipanche ramosa L. Pomel during plant parasitism
on Brassica napus L.* DOI `10.1007/s11104-022-05822-6`.
The [publisher](https://link.springer.com/article/10.1007/s11104-022-05822-6)
gives online publication on 8 December 2022 and the 2023 volume 483, pages
667-691. Its public preview did not expose the methods.

The institutional laboratory publication list led to the public
[HAL v1 deposit](https://hal.science/hal-04370677v1) and its
[author manuscript](https://hal.inrae.fr/hal-04370677v1/file/Submitted_version_LM.pdf).
Source type: journal article, author-manuscript version. Discovery mode:
manual web search from the existing DOI, followed by the institutional link.
Accessed: 2026-10-07. The HAL cover identifies the DOI and 2023 citation;
the manuscript title page explicitly identifies the December 2022 published
version. HAL deposit date is 16 January 2024, not the publication year.

The 42-page PDF was downloaded publicly without authentication. The complete
relevant methods on PDF page 11 (printed page 10), lines 299-319, were read in
extracted text and visually inspected after PDFKit rendering. The title/cover
were read in extracted text. This is not an assertion that the publisher's
version of record or its supplements were inspected. Ghostscript rendering
failed for a missing X11 library; PDFKit rendering succeeded with a temporary
module cache and no dependency/environment changes.

| Capture in `/tmp/ingredient-media-20261007` | SHA256 |
| --- | --- |
| `P8-P9-HAL-page.html` | `4e93afb4cf1978c98a1ee7c877a9fea7ea605d3b71c9a21cc789425bb2ed6df1` |
| `P8-P9-HAL-submitted.pdf` | `2788ca1a054d5ff67f02af146db31e0735153886d9c5de54c0c607629a9c9f1c` |

## P8 Findings

- The manuscript's M9 5X stock specifies potassium dihydrogen phosphate at
  15 g/L. The captured P8 page and `solutions[3].composition[1]` both have
  51 g/L. This is a source conflict, not corroboration of the local value.
  Other listed M9 stock rates agree: disodium hydrogenphosphate 64 g/L,
  sodium chloride 2.5 g/L and ammonium chloride 5 g/L.
- Methods lines 303-307 describe a 10 ml culture, with input doses of 2 ml M9
  stock, 2 ml magnesium sulfate stock, 10 microliters calcium chloride stock,
  and 2 ml sinigrin stock. The latter stock rates are 24.65, 14.7 and 10 g/L,
  respectively. These are stock strengths, not final-medium concentrations.
- The listed inputs sum to 6.01 ml, not 6.1 ml. The local four stock-dose
  concentrations use the page's 6.1 ml control as their denominator. The
  manuscript's stated 10 ml culture does not endorse that denominator.
  A separate final-water makeup instruction is not given in this passage;
  do not encode a guessed fixed water input while repairing the batch basis.
- The manuscript calls the reagent sinigrin hydrate. Do not add a hydrate
  stoichiometry, molarity conversion, or stock accession from that label.
  The page's `NaN` solution identifier remains invalid.

Candidate next step: a guarded, source-specific proposal for the stock amount
and dose basis, with literal field-level snippets and explicit treatment of
the dataset/article disagreement. Do not globally replace every similarly
named M9 stock or propagate evidence through ingredient-only fingerprints.

## P9 Findings

The manuscript's PDB-SNG formulation is liquid quarter-strength potato dextrose
broth with sinigrin: 8 ml of 6 g/L PDB solution plus 2 ml of 10 g/L sinigrin
stock, at pH 5.6. It is not the current P9 methane-medium agar graph with
ammonium sulfate, iron/copper salts and trace-element stocks. The shared DOI
therefore does not support that current local formulation.

The [earlier P9 capture](20261007-public-medium-source-pages.json) already
records this identity conflict and a separate preparation instruction choosing
SL-10 or SL-6. The local graph contains both. Reconcile medium identity and
source history before repairing quantities; do not combine the broth formula
with the methane recipe, delete the old source history, or silently repurpose
the stable record ID. A split/new-record decision requires the recipe workflow
and duplicate/variant checks.

No ingredient evidence, growth association, ID, schema or generated merge was
changed. The historical acquisition snapshot and source inventory remain intact.
