# Source Inspection

The source captures are immutable inputs to `plan.json`. Their response hashes,
exact extracted text and metadata are checked by the guarded mutator and the
independent audit. The terminal baseline source check also read the cached PDF,
HTML and DataCite response bytes and verified their recorded hashes.

## Archive Identity

The [DOI 10.13145/bacdive4303.20170829.2](https://doi.org/10.13145/bacdive4303.20170829.2)
resolved to the BacDive archive viewer.
An HTML-parser check confirmed its iframe points to the exact captured PDF;
the viewer explicitly identifies version 2. The [DataCite response](https://api.datacite.org/dois/10.13145/bacdive4303.20170829.2) confirms the
title *Acidiferrobacter thiooxydans Hallberg et al. 2011*, publication year 2017,
issue date 2017-08-29, and six creators. The year is not inferred from the DOI
suffix or from the species-authority year in the title.

The BacDive biological record concerns DSM 2392/JCM 17358. Its page 2 recipe
field reproduces instructions explicitly naming DSM 9463, 9466, 9467 and 9468.
Those instructions can support the named recipes, not a transfer of DSM 2392's
growth, optimum temperature or taxonomy to those strains.

The inspected recipes are the [versioned archive PDF](https://bacdive.dsmz.de/pdf/4303?doi=10.13145%2Fbacdive4303.20170829.2)
and the [current DSMZ 670 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf).

KOMODO's captured rows link DSMZ 670 and retain the older pH 3.5 for DSM 9466.
They do not identify the original recipe version. The correction explicitly
chooses the archived strain formulation, compatible with that pH profile, and
retains the current-source recipe as a separate inline alternative. It does not
claim that the original KOMODO import has been historically reconstructed.

## Visual And Text Checks

The web screenshot requests returned references but no inspectable image blocks.
Instead, the pinned archive PDF page 2 was extracted with pypdf and rendered with
macOS `sips`; the pinned current DSMZ PDF page 1 was rendered directly. PNGs had
transparent backgrounds that obscured black text in the viewer. JPEG renders
were inspected successfully. These are temporary read-only inspection outputs,
not replacements for the captured source PDFs.

- Archive: four base salt masses and 1000 ml distilled-water input; iron is added
  only in the named iron-using strain instructions.
- DSM 9466: archive pH 3.5 and autoclaved yeast stock; current source pH 3.0 and
  a sterile yeast stock without a stated sterilization method.
- DSM 9467: archive 2 N acid, 10% w/v glucose stock, 1% yeast stock, and autoclaved
  yeast stock. The archive does not give a basis for the 1% yeast stock or the
  0.2% glucose/0.01% yeast receiving-medium targets. Current source instead uses
  1 N acid and explicit 2.00 g/L D-glucose plus 0.1 g/L yeast targets from filtered
  stocks. These versions are not blended.
- DSM 9468: archive 0.25 ml of 40% w/v iron stock per 5 ml receiving MS-medium,
  not per 5 ml final medium. The archive offers filtration or autoclaving under
  N2; the current source specifies filtration under 100% N2.

Captured PDF bytes and all extracted pages were rechecked in the baseline
source-capture job. Individual claim snippets are literal substrings of those
pages. Arithmetic and curator interpretations are kept outside quotations.

## Remaining Gaps

No final volume is explicitly supplied for the archived batch masses. Acid
normality has no current schema concentration unit. Stock doses not specified
by the source, unspecified percent bases and new-label ontology mappings remain
unresolved. These gaps are not filled with conventions or values from the
current recipe. The inherited `Aerobic: No` notes are retained as legacy import
metadata, not independently validated incubation conditions.

## Automated Reference Limitation

The complete reference CLIs remain red. The installed
`linkml_reference_validator/etl/sources/url.py` uses `response.text` directly
and extracts titles only from HTML tags, falling back to the URL. Its cached
archive and current-DSMZ references contain raw `%PDF-` content rather than
extracted recipe text. Consequently 44 archive snippets and seven current-PDF
snippets fail the installed matcher, although the pinned pypdf text and visual
checks support them. Fourteen other evidence entries pass. Eleven title errors
also arise from URL fallback metadata. These automated failures are retained in
`reference-validation.json`; the manual/source-aware checks do not relabel that
command as successful.
