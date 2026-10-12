# Correct DSMZ Recipe Bibliography Titles From Original Headings

Status: open local issue draft; not submitted to GitHub. No recipe changes applied.

The repaired PDF validator found 41 exact-title mismatches in 34 current records,
covering 21 DSMZ sources. All 152 explicit PDF snippets in the reviewed scope
match the freshly captured originals. This is a bibliography issue, not evidence
that those ingredient amounts are unsupported or that every amount is verified.

Many current titles prepend `DSMZ` or change heading punctuation; others are
placeholders such as `DSMZ medium 13: official recipe`. Preserve provider
attribution in provenance notes and use the actual source heading as the title.
Do not weaken amount matching or change source URLs to make a check pass.

`pdf-checks-all-final.json` records each failed field, exact prior title, actual
title and source URL. `pdf-scope-all.json` pins record hashes. Source metadata contains
binary/text hashes and access time; cached originals can be re-extracted.
`title-followup.json` pins each proposed old/new title, exact heading snippet,
record hash and source provenance. These are unapplied candidates, not a claim
that the complete records have now been reviewed.

Before applying, read each complete target, confirm the source identity and
heading, and attach an exact heading snippet to the changed provenance claim in
an appropriate schema-supported evidence container. Preserve existing evidence
and append curation history. Use preview/apply guards and deduplicate references.
Standalone solution records need their own evidence-container handling.

DSMZ 261 has a two-line heading. The initial scope run truncated it; the final
run and offline fixture preserve the whole heading. Neither copyright dates nor
provider names should become invented publication years or authors.

Re-run complete reference checks for changed records, distinguish other-source
failures, and account for the edits in the cumulative audit without claiming new
record-review coverage merely because a bibliography title was corrected.
