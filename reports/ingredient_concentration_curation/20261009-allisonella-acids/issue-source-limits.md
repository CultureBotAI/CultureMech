# Open: Allisonella Source Limits

Local issue only; not published to GitHub.

## Evidence

- [DSMZ original](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf)
  specifies the source batch inputs, two stock addition doses and fatty-acid
  stock recipe. Its 1,000 ml distilled water is an input, not an explicit
  measured final-volume statement.
- [MediaDive API](https://mediadive.dsmz.de/rest/medium/1006) has a main-volume
  encoding of 1,004 ml and derived mass/molar fields. The inspected original
  does not independently verify that denominator or the liquid-acid densities.
- [KOMODO 1006](https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006)
  reports its own per-liter quantities and nulls. Its aerobic flag disagrees
  with the linked original's anoxic CO2 preparation. The row labels do not
  independently establish copied salt/stereochemical annotations.

## Current Resolution

The records now preserve source-specific quantities, explicitly separate stock
composition from receiving dose, archive displaced copied claims, and attach
exact source snippets. Unknown final concentrations, gas doses and chemical
forms are not inferred. No new ontology IDs are asserted. Authors/year are
omitted where not supplied, rather than borrowing a copyright year.

## Closure Evidence Needed

An exact-formulation source stating measured final volume and any required
density would permit further mass-per-volume conversion. A source-version
explanation or corrected provider record could resolve aerobic/normalization
disagreements. Chemical annotations require their own identity review. Until
then these are explicit limitations, not evidence-free numeric edits.
