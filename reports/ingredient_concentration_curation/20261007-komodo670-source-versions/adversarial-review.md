# Adversarial Review

## Corrected Findings

1. **Source-version substitution:** treating DSM 9466 pH 3.5 as a transcription
   error would substitute the current pH 3.0 recipe into an older profile. The
   DOI-resolved archive explicitly supports 3.5. Current instructions are now
   separately evidenced inline alternatives, including their water/preparation
   differences. The archive-to-KOMODO historical attribution remains uncertain.
2. **Copied base formulation:** generic iron had been copied into three strains
   whose archived instructions use other substrates. Archived base composition
   plus the explicitly named instructions, corroborated by current iron-omission
   text, support removal. Sulfur/yeast supplements and the glucose stock now have
   claim-specific evidence. Removed iron nodes are retained in the audit history.
3. **False final concentrations and percent bases:** 1000 ml water input does not
   establish final volume. Sixteen batch salt masses remain as source text rather
   than asserted g/L. Archive percentages without an explicit basis remain
   unnormalized. Regression cases reject using current-source g/L as an
   unqualified repair of the archived preparation.
4. **Stock-to-medium denominator:** the archive's iron dose is per 5 ml receiving
   base, not per 5 ml final medium. The normalized 50 ml/L ratio retains this
   denominator; stock strength and acid carrier are separate. Tests reject an
   absolute-liter dose, a final-medium denominator, and invented acid molarity.
5. **Incorrectly defined / pH-only records:** yeast-containing media are not
   fully chemically defined. The four children have source-version and
   preparation differences, not only pH differences from their current-source
   parent. Reciprocal links and quality flags now reflect that scope. Corpus
   link validation found zero errors and zero warnings.
6. **Lost earlier audit layer:** the cumulative audit previously retained only
   the latest repair per path. It now independently inverts every hash-linked
   applied repair, rejects ambiguity/disconnection/identity drift, and preserves
   support for historical plans whose result was stored as a hash rather than
   embedded text. The complete cumulative delta matches the new batch audit.
7. **Ignored validator output directory:** the link validator accepted
   `--reports-dir` but wrote to its module-level default paths. The scoped fix
   writes and reports the requested paths. Regression tests protect existing
   default reports and external-directory CLI output. The first validation run
   occurred before this fix and wrote the default reports; no pre-existing dirty
   report was reverted. Final rerun results are recorded separately.

## Open Findings

- **PDF reference validation:** all five complete citation CLIs fail. The
  installed URL source implementation assigns `response.text` directly to
  reference content, with no PDF extraction. Its two PDF cache files contain
  `%PDF-` data, explaining the 51 failed PDF snippet matches; 14 other snippets
  pass. Eleven title errors use URL fallbacks. The DOI-resolved archive,
  DataCite metadata, exact PDF bytes/text and rendered pages were independently
  inspected. No cache was forged and no valid citation was weakened to force a
  green CLI result. PDF-aware reference validation remains a tooling follow-up.
- **Merge retention:** actual current groups preserve all tested formulation,
  version and provenance fields for DSM 9463, 9466 and 9467. The KOMODO parent and
  DSM 9468 share a three-record group and fail exact retention. DSM 9468 loses
  ingredients, stocks, preparation, pH, alternatives and provenance. Parent
  link/provenance fields also differ. This is a publication blocker, not a reason
  to collapse the two source formulations in normalized YAML.
- **Source attribution:** the archive reproduces the named strain instructions
  but does not establish the exact version KOMODO originally used. No new growth,
  temperature or taxonomy evidence is transferred from the BacDive DSM 2392
  biological record.
- **Unrepresented / unquantified values:** missing final volume, unsupported
  mass-only/normality units, unspecified percent bases and unreported stock doses
  remain open. Existing ontology mappings and inherited aerobic notes have not
  been independently re-curated; new source labels are not invented ontology IDs.
- **Corpus scope:** 5,300 normalized paths remain outside these follow-up reports,
  with unresolved claims in reported records too. The inherited 673/266 sulfur
  and yeast-preparation conflicts remain open. No claim of all-record completion
  or publication follows from this batch.

This is a local review artifact, not a claim that GitHub issues or a PR were
created. Consult the terminal validation and reference-check journals for
remaining automated gate failures.
