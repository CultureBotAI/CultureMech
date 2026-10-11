# Medium 111 Preparation Follow-Up

This follows up three existing per-record reviews within the unfinished
all-record ingredient objective. It does not add new unique reviewed paths.
The [frozen plan](plan.json) links each prior file hash to its reviewed successor:

| Record | ID | Role |
| --- | --- | --- |
| `bacterial/beijerinckia_medium.yaml` | `CultureMech:000556` | DSMZ medium 111 |
| `bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml` | `CultureMech:003822` | Exact KOMODO 111 mapping |
| `bacterial/mediadive_190_Main_sol_111.yaml` | `CultureMech:011325` | Standalone source solution 190 |

All paths above are under `data/normalized_yaml/`. An ignored-inclusive source-ID
and original-recipe-link search in that authoritative tree identified these
three exact records. Source identity and ingredient forms were checked before
application; a similar name alone was not treated as formulation evidence.

## Source Decisions

The complete captured [medium API](https://mediadive.dsmz.de/rest/medium/111) and
[solution API](https://mediadive.dsmz.de/rest/solution/190) agree on the table,
950 ml main-preparation field and separate-glucose instruction. Their inspected
raw responses, retrieval metadata, literal excerpts and hashes are in the plan.
The [official one-page recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf)
was inspected again and agrees on those inputs and preparation stages.
The exact captured KOMODO table row supports the source mapping only, not
ingredient amounts, variants, atmosphere or organism growth.

- Move glucose out of the direct basal ingredients/composition and into a
  separately sterilized glucose preparation, preserving its chemical mappings.
- Withdraw the wrongly staged `10.5263 G_PER_L` glucose slot in all three
  records. Retain the supported 10 g mass and 50 ml H2O input in notes/evidence.
  The 950 ml denominator belongs to the basal preparation, not the glucose stock.
- Represent the 50 ml stock-water input as `0.05 L`, not a measured stock volume
  or `50 ML_PER_L` working dose. H2O does not establish distilled-water purity.
- Represent the 950 ml basal distilled-water input as `0.95 L` per batch. This
  corrects the standalone solution's unsupported `1000.0 PERCENT_V_V` slot and
  restores the omitted water input in both media records.
- Retain nine provider-declared basal g/L values per record, with explicit
  mass inputs and scope limitations. These are dataset-reported normalizations,
  not independently verified final-medium concentrations after glucose addition.
- Keep the parent pH instruction at the medium preparation level. The nested
  glucose preparation quotes only the separate sterilization/mixing instruction;
  it does not assert that the glucose stock is adjusted to pH 6.5.

Neither 200 g/L glucose stock, 10 g/L final-medium glucose, a fixed volumetric
stock dose, nor a measured 1 L final volume is asserted. Summing two water inputs
does not establish any of those quantities. Sterilization method, time and
temperature are not invented. Existing ontology mappings, source-duplicate links,
the KOMODO aerobic import annotation, and the standalone legacy placeholder and
quality flag are retained without claiming new scientific verification.

Every changed scientific assertion carries a source URL and exact snippet in
YAML. Existing ingredient quotes and historical explanations are retained, with
new scope text distinguishing current claims from superseded interpretations.
The standalone solution uses schema-supported `source_data.evidence`, with
`origin: MediaDive`, for preparation-level assertions. No unsupported root
evidence slot is added to `SolutionRecipe`. New bibliography entries record
title, source type, discovery mode and access date; unavailable authors, DOI and
publication year are not manufactured. A PDF copyright year is not used as a
publication date.

## Review And Guards

The repair defaults to preview, requires explicit apply, checks exact tracked
paths and IDs, rejects source or target drift, validates both record classes
and confirms a zero-change rerun. The independent auditor checks literal source
excerpts and inverts the entire edited record back to its exact baseline.
The plan also records explicit claim resolutions for the two previously accepted
API batches, preserving source snippets while withdrawing glucose and reindexing
the nine retained claims. Historical reports are not overwritten.

Application, guarded readback and a zero-change second apply have completed.
The [independent applied audit](diff-audit.json) verifies 20 new evidence entries,
five references and three appended events. It separately counts three glucose
relocations, three unsupported glucose concentration slots removed, five new
water-volume slots and one existing water-unit correction. Twenty previous
evidence explanations are rescoped without losing their original snippets or
historical explanations. The three follow-up reports are
[DSMZ](dsmz-followup.md), [KOMODO](komodo-followup.md) and
[standalone solution](solution-followup.md); they include unresolved stock doses
and do not count as new unique-path reports.

An early preview copied the parent pH sentence into the stock preparation.
Manual adversarial review rejected that preview before application; a regression
test now rejects the same scope error. A baseline test also caught a preview
record entering the optional successor resolver before it had an `after_sha256`.
The [first validation attempt](validation-baseline-attempt-1.json) stopped before
record edits; the resolver was fixed before the guarded retry.

## Validation

The guarded run is terminal; [validation.json](validation.json) records five
baseline and 23 post-apply checks. All 936 focused tests pass, as do the three
target schema checks, full 15,910-record strict scan, IDs, source readbacks,
independent inversion, cumulative diff, exact-path coverage and whitespace
checks. Product and automated reference checks cannot run successfully without
`oaklib` and `linkml-reference-validator` in this isolated environment.

The [actual-group retention check](merge-retention.json) fails for the DSMZ media
copy: its ingredients, stocks, notes, evidence, references and history are not
fully preserved. The KOMODO canonical copy retains the checked fields. The
standalone stock's in-memory singleton retains fields but is wrongly routed;
actual generation then drops its output with a missing `name` error. The
[freshness comparison](merge-freshness.json) also fails, and must not be mistaken
for a complete successful regeneration. Global verification still fails.

Validation uses isolated Python 3.11, not maintained Python 3.13 or CI. No
generated merge is hand-edited or published, and no commit, PR or merge is claimed
for this local follow-up. See the subsequent
[routing repair](../20261007-solution-merge-routing/README.md) for separately
recorded pipeline changes; the scientific record hashes are preserved.

## Remaining Work

The [observed fingerprint impact](fingerprint-impact.json) exposes a merge
pipeline defect: standalone solution 190 was previously unfingerprintable, but
its new nested preparation produces only `glucose` and `water` signatures.
The fingerprinter ignores all ten entries in the authoritative root composition.
The repository's record-class discriminator correctly recognizes this input as
`SolutionRecipe`; it must not enter medium merging through a partial signature.
Separate solution routing from medium fingerprinting and add explicit regression
coverage before publishing generated output. Do not remove the supported stock
boundary to hide this defect. Both media records retain all original chemical
signatures and add only the two explicitly represented water labels.

Final stock/medium volumes and working concentrations remain unverified from
these sources; the repair preserves the stated batch preparation rather than
inventing missing inputs. DSMZ/KOMODO 125 and 187 still need their previously
documented variant and pH follow-up. The remaining corpus, unresolved claims in
earlier reports, importer errors, merge evidence retention and publication
validation remain part of the full objective.
