# JCM 896: Original-Source Repair Handoff

**Unrepaired.** The sixth cohort withholds all six mechanically eligible claims
and leaves this record unchanged. The full original recipe supports an explicit
successor repair, not endorsement of the API's concentrations.

- Exact target: `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`
- Stable ID: `CultureMech:003244`
- Baseline commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Target SHA256: `b04cd5b9c8da3f84b37c7dbd3a8db2d91a432df510277c46ea426177a7fc6e7c`
- Original source: [JCM 896, MODIFIED BSK MEDIUM](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896)
- Accessed: 2026-10-07; source type: culture collection page; discovery mode:
  existing record reference. Individual authors/publication year are unknown;
  the website copyright year is not a recipe publication date.
- Inspected capture: `/tmp/ingredient-media-20261007/JCM_GRMD896.html`
- Capture SHA256: `c6e814a8bff1580ddd42179b7d401a204ae19469786fdafd140408d1522f03c8`

## Source Conflict

The preparation explicitly says **"fill up to 584 ml with distilled water"**.
The API divides its mass rows by 40 ml, the serum dose, instead of 584 ml.
The current serum amount is additionally encoded as mass per liter although
the original gives a volume. No density is established or needed for a
volume-per-liter correction.

The original table contains ten mass rows and one volume row:

| Table row | Original batch quantity |
| --- | --- |
| HEPES | 3.0 g |
| Trisodium citrate dihydrate | 0.35 g |
| Glucose | 2.5 g |
| Sodium pyruvate | 0.4 g |
| N-Acetyl-D-glucosamine | 0.2 g |
| NaHCO3 | 1.1 g |
| MEM alpha Modification (BioWest) | 5.2 g |
| TC Yeastolate (BD-Difco) | 1.0 g |
| Probumin Universal Grade (Millipore) | 25.0 g |
| Neopeptone (BD-Difco) | 2.5 g |
| Rabbit serum, specified Pel-Freez product | 40.0 ml |

These table labels are a readable inventory, not manufactured verbatim snippets.
Extract each exact rendered row with a structured HTML parser when creating its
YAML evidence. Preserve inline chemical digits and entities; do not use regex
tag stripping that splits chemical names.

## Required Successor

1. Recheck the exact target and original capture hashes before preparing a plan.
2. Correct ten mass rows using `source_mass_g / 0.584 L`, keeping the exact
   input and explicit rounding policy in evidence explanations.
3. Correct serum using `40.0 ml / 0.584 L` with `ML_PER_L`, not a guessed density.
4. Correct the nonspecific yeast-extract label to the original TC Yeastolate
   product; do not invent a chemical ontology mapping for this mixture.
5. Correct the corrupted micrometer symbol in the filtration instruction from
   the original text. Keep the pH and filtration action unchanged.
6. Attach ingredient-level source row excerpts and a separately quoted final
   volume statement, plus recipe-level evidence for the preparation correction.
7. Append bibliographic provenance and one agent-authored curation event while
   preserving all previous history and unrelated fields.
8. Freeze before/after text and hashes in a successor plan. Add it explicitly to
   cohort readback, coverage, and independent semantic-diff inversion; do not
   overwrite this first-pass result or the source inventory.
9. Test guarded apply, changed-source/target refusal, readback, no-op rerun,
   exact snippets, arithmetic, whole-record schema, and actual merge retention.

The corrected mixture name may intentionally change its ingredient fingerprint.
Concentration-independent grouping is not proof that another formulation may
inherit these corrected amounts or evidence.
