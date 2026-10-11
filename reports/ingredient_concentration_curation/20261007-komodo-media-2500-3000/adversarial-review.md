# Adversarial Review

## Addressed In This Pass

1. **Constructed mapping-page title was not the source title.** New previews now
   parse the hash-checked captured HTML and freeze its actual title. Apply/verify
   reject title drift. Tests cover missing/empty/duplicate titles, captured-byte
   drift, frozen-title tampering, persistence/no-op and legacy reproduction.
   Historical references are not rewritten; their source-pinned repair remains
   a separate task. The new full citation check finds no mapping-title errors.
2. **Flat tables could hide stock and formulation conflicts.** Complete inspection
   of 54 candidate records/responses rejected 75 otherwise proposed entries on
   eleven records. The frozen vetoes contain exact source excerpts and hashes;
   they cannot authorize values. Regression tests bind all eleven decisions to
   their original sources and verify that their records remain unchanged.
3. **Inconsistent agar fields could be endorsed through the wrong API field.**
   Three records have 20 g API amounts but `g_l=15`; original PDFs use 15 g/l-scale
   inputs. Those agar claims remain conflicts. Tests prohibit adding evidence
   to them through this API-only pass; no number is selected by convenience.
4. **An old integrity test omitted applied successor plans.** Post-edit testing
   found six older MediaDive records whose verified stock/preparation repairs
   were absent from the test's explicit follow-up list. Two plans were added to
   that list. The hash and evidence assertions were not weakened, expected
   hashes were not replaced, and no normalized data changed to satisfy the test.
   The first failed journal remains available for comparison with the rerun.

## Still Open

- Full citation validation fails for 43 API titles. Installed
  `linkml-reference-validator` 0.1.6's URL source reads `response.text`, extracts
  HTML `<title>`, and falls back to the URL for JSON. All 250 concentration and
  43 identity snippets pass its installed text matcher. This does not turn the
  full title check into a pass or settle bibliographic representation of API
  resource names. Source titles were not replaced with URL strings just to pass.
- Parent links, inherited atmospheric notes, water-unit errors, secondary
  ontology mappings and source-version identity are not validated by these
  concentration excerpts. Specific consequential findings remain in the
  candidate-inspection report and per-record claim tables.
- The eleven withheld formulations require actual source-specific curation.
  A source-access/report pass is not resolution of their concentration issues.
- Actual merge retention fails: 215/250 complete concentration entries and
  222/250 scoped amount quotes survive. Eight records lose complete entries,
  six lose scoped quotes, and seven lose mapping evidence, references or events.
  The normalized evidence is intact. See `merge-retention.json` for exact paths
  and groups; do not repair this by copying variant evidence onto a different
  formulation. Global merge verification also fails (1,247 name conflicts and
  3,287 fingerprint issues). Freshness fails with 1,700 changed shared paths,
  3,720 tracked-only and 3,898 fresh-only paths; see `merge-freshness.json`.

No publication or all-record completion is asserted.
