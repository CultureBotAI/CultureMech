# Public-Medium Sources: Acquired, Not Applied

All ten remaining public-medium targets in frozen inventory offsets
`[3319:3329]` now have accessible HTML recipe captures. The metadata-only REST
responses do not mean the recipes are unavailable. The earlier failed REST
acquisition is preserved; no missing `solutions` key was replaced by an empty list.

[Source snapshot](20261007-public-medium-source-pages.json) records all ten exact
paths and IDs, their unchanged baseline hashes, page URLs and SHA256 hashes,
embedded dataset identity, source metadata, 21 recipe tables, main-volume
controls, table headers, ingredient/step rows, and row-local links/images.
Captures were downloaded on 2026-10-07. The complete extracted ingredient and
preparation tables were read. The two embedded RS preparation diagrams were
also inspected. This is source acquisition and triage, not ten completed
per-record concentration reviews or applied YAML changes.

The source is a user-contributed MediaDive dataset page, not automatically a
curated culture-collection recipe or a verified journal method. Displayed author,
publication and modification metadata refer to the page; linked journal DOIs
remain uninspected leads. The P1 composition-export link returns the non-JSON
body `nothing to be shown`; its HTTP success is not a successful recipe export.

## Review Leads

| Medium | Source-specific review needed |
| --- | --- |
| [P1](https://mediadive.dsmz.de/medium/P1) | A 700 ml final makeup is stated, with nested ASW, washed agar and supplements. Some displayed calculated g/L values conflict with their stock strengths and doses. The ASW bicarbonate table itself reports 1000 g; do not silently replace this suspicious value without the original method. |
| [P2](https://mediadive.dsmz.de/medium/P2) | Direct per-liter rates coexist with stock doses and conditional agar. Haemin has an explicit 100 ml makeup; artificial seawater has its own per-liter rates. Review each preparation stage and the solid/liquid condition separately. |
| [P3](https://mediadive.dsmz.de/medium/P3) | The page declares a 1000 ml main volume and lists 10 ml glycerol, not 10 g. The local record already uses `ML_PER_L`; verify and preserve that distinction. |
| [P4](https://mediadive.dsmz.de/medium/P4) | Explicit 1 L makeup and many different stock strengths/doses support source-specific dilution checks. The current local record already has calculated concentrations; compare arithmetic and existing evidence before changing anything. TiCl3's commercial percentage/range must not be converted to a guessed mass concentration. |
| [P5](https://mediadive.dsmz.de/medium/P5) | Single stocks feed five 50 ml mixes, which feed a 150 ml final NM component. Many stocks use NNM, not pure water. The local record already models these stages; do not flatten it. The carbon table names D-Xylose while the mixing prose names Xylan, an unresolved source-identity conflict. |
| [P6](https://mediadive.dsmz.de/medium/P6) | Six mass rows use the page's declared 1000 ml main volume. Verify the linked article and local scope before claiming its methods confirm those rows. |
| [P7](https://mediadive.dsmz.de/medium/P7) | Base water, later liquid doses, iron percentage basis and B12 stock need reconciliation. The modified recipe is not established as identical to another N27 formulation by its name. |
| [P8](https://mediadive.dsmz.de/medium/P8) | The page mixes stock strengths with dose annotations and labels the nested M9 container `sol-NaN`. Preserve page-scoped locators; do not fabricate a globally valid solution accession or treat stock concentrations as final-medium concentrations. |
| [P9](https://mediadive.dsmz.de/medium/P9) | The page name/reference and displayed formulation need identity review. Its preparation specifies SL-10 or SL-6, while the table and local graph contain both. Do not silently combine mutually exclusive trace stocks. |
| [P10](https://mediadive.dsmz.de/medium/P10) | A trace-stock table and preparatory masses are shown, but the receiving dose is only `trace`; no fixed working concentration follows. The CuSO4 hydrate table lacks a unit while the prose supplies a mass, requiring an explicit cross-locator check. |

For example, P1's KH2PO4 row specifies 7 ml of 50 g/L stock, while its
calculated column says 23.4 g/L. The source's 700 ml final makeup would give
`50 g/L * 0.007 L / 0.700 L = 0.5 g/L`, not 23.4. That comparison identifies
an upstream calculation conflict; it is not an applied correction or endorsement
of every other P1 field. Existing normalized structure and evidence must be
reviewed first, and the original DOI-linked method remains a priority lead.

## Diagram Captures

The source snapshot retains each image's exact HTML locator. Both diagrams were
visually inspected; no image text was invented as an evidence snippet.

| Page | Official image | Local capture SHA256 |
| --- | --- | --- |
| P4 | [NNM preparation](https://mediadive.dsmz.de/img/usermedia/Fig1_RSmedium_NNM_GraficScheme_MediaDive.png) | `245e477ae6e3c0f514270e7e62fc4c000110c022ae18c153c7ec8ceb9f03e4a2` |
| P5 | [NM preparation](https://mediadive.dsmz.de/img/usermedia/Fig2_RSmedium_NM_GraficScheme_MediaDive.png) | `e90144dbb695abd6ac4279e294fe7b6b8a1b3d28dce4a26346fd14d78aa28917` |

Local captures are `/tmp/ingredient-media-20261007/P4-preparation-figure.png`
and `P5-preparation-figure.png`. The P4 figure shows the 1 L NNM and sparging
stages; the P5 figure separates single stocks, five mixes and final NM, including
NNM as diluent. Source text supplies the numeric mix volumes. Other uninspected
documents are not promoted to evidence. All ten records remain in the full
objective and outside the completed follow-up report inventory.
