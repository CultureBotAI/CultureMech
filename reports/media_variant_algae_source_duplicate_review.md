# Algae Source-Duplicate Variant Review

Date: 2026-05-11

## Decision

The remaining algae `SOURCE_DUPLICATE` parent/child proposals were not applied.
They are now downgraded to `REVIEW_REQUIRED` because the parsed ingredient and
concentration signatures match, but the medium names are semantically broad
and often describe distinct source families such as Erdschreiber, enriched
seawater, soil/seawater, CHEV diatom, TAP, Bold, BG-11, F/2, WC, COMBO, and
organism-specific media.

This prevents exact-signature parsing artifacts from creating parent/child
links before source formulation review confirms that the records are true
duplicates or defensible variants under a shared parent medium.

## Current Counts

- YAML records scanned by link validation: 15,827
- Existing parent-to-child links: 1,487
- Existing child-to-parent links: 1,487
- Link validation errors: 0
- Link validation warnings: 0
- Algae parent groups downgraded for source/formulation review: 17
- Algae child proposals downgraded by this rule: 103
- Downgraded algae `SOURCE_DUPLICATE` child proposals: 99
- `just apply-media-variant-links --relationship SOURCE_DUPLICATE` planned
  actions after downgrade: 0

## Downgraded Parent Groups

| Parent path | Child proposals | Relationship counts | Notes |
|---|---:|---|---|
| `data/normalized_yaml/algae/chus_medium.yaml` | 28 | `SALINITY_VARIANT:3;SOURCE_DUPLICATE:25` | Includes enriched seawater, Erdschreiber, soil/seawater, Spirulina, and F/2/NH4 names. |
| `data/normalized_yaml/algae/J_Medium.yaml` | 23 | `SOURCE_DUPLICATE:23` | Includes CHEV diatom, soil/seawater, Cyanidium, Desmid, TAP, Trebouxia, and Volvox/dextrose names. |
| `data/normalized_yaml/algae/pj.yaml` | 12 | `CONCENTRATION_VARIANT:1;SOURCE_DUPLICATE:11` | Includes NCL/RPL/PJ combinations that need source-level relationship review. |
| `data/normalized_yaml/algae/Ag_Diatom_Medium.yaml` | 9 | `SOURCE_DUPLICATE:9` | Includes CR1, COMBO diatom, Polytomella, soilwater, and silicate/soil extract names. |
| `data/normalized_yaml/algae/1_F_2_Medium.yaml` | 5 | `SOURCE_DUPLICATE:5` | Includes Allen, Bold 3N, BG-11 N, and Volvox-related names. |
| `data/normalized_yaml/algae/WC_Medium.yaml` | 4 | `SOURCE_DUPLICATE:4` | Includes artificial seawater, LDM, modified Bold 3N, and N-20 names. |
| `data/normalized_yaml/algae/a_medium.yaml` | 4 | `SOURCE_DUPLICATE:4` | Includes Bold 1NV, Bold basal, snow algae, and BG-11 names. |
| `data/normalized_yaml/algae/Bristol_Medium.yaml` | 3 | `SOURCE_DUPLICATE:3` | Includes Erdschreiber and volvocacean 3N names. |
| `data/normalized_yaml/algae/WC+_Medium.yaml` | 3 | `SOURCE_DUPLICATE:3` | Includes DYIII, modified COMBO, and P49 names. |
| `data/normalized_yaml/algae/n75s.yaml` | 3 | `SOURCE_DUPLICATE:3` | Includes N75S/R75S natural-seawater names. |
| `data/normalized_yaml/algae/HEPES_Medium.yaml` | 2 | `SOURCE_DUPLICATE:2` | Includes modified Desmidiacean and Volvox names. |
| `data/normalized_yaml/algae/Waris_Medium.yaml` | 2 | `SOURCE_DUPLICATE:2` | Includes Dasycladales seawater and Euglena names. |
| `data/normalized_yaml/algae/DYV_Medium.yaml` | 1 | `SOURCE_DUPLICATE:1` | Modified artificial seawater requires source/formulation review. |
| `data/normalized_yaml/algae/F_2_Medium.yaml` | 1 | `SOURCE_DUPLICATE:1` | `8_ppt_F_2_Medium` should be reviewed as a salinity/formulation variant rather than auto-linked as a duplicate. |
| `data/normalized_yaml/algae/bg11.yaml` | 1 | `SOURCE_DUPLICATE:1` | `bg11r` requires source review before duplicate or variant modeling. |
| `data/normalized_yaml/algae/per.yaml` | 1 | `SOURCE_DUPLICATE:1` | `ses_mp` requires source review before duplicate or variant modeling. |
| `data/normalized_yaml/algae/sna.yaml` | 1 | `SOURCE_DUPLICATE:1` | `sna_5` requires source review before duplicate or variant modeling. |

## Follow-Up

Review these groups against the original media sources before applying links.
If source formulations match exactly, link as `SOURCE_DUPLICATE`. If source
differences are small and share a recognizable base medium, keep the parent
record canonical and model the child as a specific `MediaRecipe` variant with a
relationship such as `SALINITY_VARIANT`, `CONCENTRATION_VARIANT`,
`SUPPLEMENTED_VARIANT`, or `PHYSICAL_STATE_VARIANT`. If the source formulation
is not a defensible variant of the selected parent, keep it as an independent
parent candidate.
