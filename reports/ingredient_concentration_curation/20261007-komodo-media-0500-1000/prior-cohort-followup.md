# Prior-cohort preparation follow-up

The current manual source review also changes the next action for three
previously processed DSMZ records. Their existing amount snippets correctly
quote the provider's `g_l` data, but do not resolve the preparation conflicts.
They must not be counted as fully scientifically resolved because an earlier
evidence-only pass succeeded.

| Source | Current authoritative target | Current SHA256 | Existing amount entries |
| --- | --- | --- | ---: |
| 111 | `data/normalized_yaml/bacterial/beijerinckia_medium.yaml` (`CultureMech:000556`) | `01ead4d30e8caa21abc37da645b39e5b502de62be10cc4fdbd3f7763a90cbc7e` | 10 |
| 125 | `data/normalized_yaml/bacterial/methylobacterium_medium.yaml` (`CultureMech:000718`) | `06a56a51606291dff6ad45dc6dda946374bcc859051ee7e3f570a7fb86de54bf` | 12 |
| 187 | `data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml` (`CultureMech:001279`) | `990e1d04ea3d8b0169d73ef912c8d96e1b00cc904c364892a95da1788b4905ad` | 4 |

These exact files and their source IDs were re-read, including an ignored-inclusive
source-ID search. Their hashes still equal their historical
[first MediaDive batch](../20261007-mediadive-media-0000-0500/plan.json) results.
No historical plan or report was overwritten, and this handoff makes no YAML edit.

## Required Corrections

1. **111:** distinguish the 950 mL basal preparation from the separately
   sterilized glucose in 50 mL water and the resulting complete-medium context.
   The existing glucose `10.5263 G_PER_L` table-derived value is neither the
   glucose-stock strength nor a verified complete-medium concentration. Preserve
   its literal historical quote while correcting evidence scope and ingredient/
   stock placement with explicit source support. Do not infer measured final
   volume merely by summing water inputs.
2. **125:** represent the source's alternative methanol addition versus methane-
   air incubation without silently selecting or combining them. Preserve the
   common basal amounts with explicit scope, and reconcile existing evidence
   and variant/source-duplicate relationships before endorsing a complete recipe.
3. **187:** preserve the distinction/conflict between metadata pH 5.4 and the
   preparation instruction pH 5.6. The inspected linked PDF supplies neither
   a pH value nor evidence that one is pre- and the other post-sterilization.
   Resolve or document that uncertainty without manufacturing an interpretation.

The exact API snippets, hashes and locators supporting all three findings are
in [withholdings.json](withholdings.json); primary-PDF inspection and scope
decisions are detailed in [preparation findings](preparation-findings.md).
The corresponding KOMODO records remain unchanged with conflict results in
this batch. Any later correction must explicitly link the current before-hash
to its successor, preserve prior curation history, update readback tests and
coverage lineage, and rerun schema, snippet and merge-retention checks.

## Later Follow-Up

The [medium 111 preparation repair](../20261007-dsmz111-preparation/README.md)
links the baseline above to its corrected successor and also repairs the exact
KOMODO 111 record and standalone solution 190. It separates the glucose
preparation, withdraws the wrongly staged glucose rate, restores batch-water
inputs and preserves the prior quotes with corrected scope. Final volumes and
working stock concentrations remain unverified. The historical hashes and
findings above are retained. Consult the repair's terminal validation results
before publication.

The later [medium 125 alternatives repair](../20261007-dsmz125-alternatives/README.md)
links its historical hash to a successor and repairs the exact KOMODO 125 and
standalone solution 223 records. It represents separate methanol and methane-air
options, scopes the unchanged basal amounts, and restores source-supported water
inputs. Final concentrations and the separately inspected strain-modified
formulations remain unverified; existing duplicate links are not endorsed by
this repair. Medium 187's conflicting pH values still require the listed
follow-up. Historical plans, reports and hashes above remain unchanged.
