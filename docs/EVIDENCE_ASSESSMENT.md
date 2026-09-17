# Claim evidence assessment

`supports` states how the cited evidence bears on the **specific attached claim**.
`evidence_source` identifies the study or data-source type that produced it.
Neither field is a confidence score, a citation identifier, an ECO evidence code,
or a record of how a curator or language model found the source.

Applies to: `EvidenceItem`.

## Support values

- **SUPPORT**: The cited evidence supports the attached claim.
- **REFUTE**: The cited evidence contradicts the attached claim.
- **PARTIAL**: The cited evidence supports only part of the claim or only under stated conditions.
- **NO_EVIDENCE**: The citation provides no relevant evidence for the attached claim; not proof of a negative result.
- **WRONG_STATEMENT**: The attached claim was assessed as incorrect; retain the assessment and its explanation.

Omitted optional assessments mean **unassessed**, not SUPPORT or OTHER. Existing
required assessments remain required. Explain PARTIAL, REFUTE, NO_EVIDENCE and
WRONG_STATEMENT in the evidence's existing `notes` or `explanation` field.
A failed experiment is not automatically NO_EVIDENCE: it may refute a claim or
support a claim about the absence of an effect in a particular setting.

## Study and data-source values

- **FIELD_STUDY**: Observation or measurement made in a natural system.
- **MESOCOSM**: Experiment in a controlled enclosure representing a natural system.
- **LABORATORY**: Controlled laboratory study; use IN_VITRO or IN_VIVO when that distinction is known.
- **IN_VITRO**: Experiment outside an intact organism, such as a culture or biochemical assay.
- **IN_VIVO**: Experiment or observation in an intact living organism.
- **COMPUTATIONAL**: Model, simulation, prediction, or computational analysis providing the cited evidence.
- **META_ANALYSIS**: Systematic synthesis or quantitative analysis of results across studies.
- **REVIEW**: Narrative review or expert synthesis of published work.
- **REMOTE_SENSING**: Satellite, aerial, or other remotely sensed observations.
- **LONG_TERM_MONITORING**: Repeated observations from a long-term monitoring programme.
- **EXPERT_OPINION**: Expert judgement or consensus rather than a primary experimental result.
- **DATABASE**: Assertion or observation obtained from a database or curated data resource.
- **OTHER**: A known study or data-source type outside these categories; explain it in notes or explanation.

Choose the most specific defensible category. IN_VITRO and IN_VIVO preserve the
existing microbial-study distinction. LABORATORY is available when the study
is known to be laboratory-based but that distinction is not established.
REVIEW and META_ANALYSIS are separate; DATABASE identifies a database assertion
without promoting it to primary literature. Unknown source types stay omitted
where optional; OTHER requires a known type that does not fit the vocabulary.

## Compatibility and curation

No existing citation format, required field, evidence type, or provenance slot
has been removed. Newly introduced assessment fields are optional, with no
default and no automatic backfill. Populate them only after checking the source
against its attached claim. A citation's mere presence must not be interpreted
as positive support when its assessment is REFUTE or NO_EVIDENCE.

These fields belong to primary claim evidence. The imported shared
`SupportingReference.evidence_source` remains legacy free text describing where
a quote was obtained (abstract, full_text, figure, etc.). It has not been narrowed
to this enum. Likewise, typed strain/genome-link provenance and existing
`source`, `evidence_type` and `retrieved_on` fields retain their own meanings.

## Provenance

Motivated by [EcoMech's evidence schema](https://github.com/diatomsRcool/ecomech/blob/5d3f55467f3caaa6e88eb7f33037e4a8103873a7/src/ecomech/schema/ecomech.yaml)
and the existing CommunityMech, CultureMech and MediaIngredientMech assessment
models. Fleet agreement: [CLAW evidence contract](https://github.com/CultureBotAI/culturebotai-claw/blob/26d083901922650688aaa4937c34c7e68856183a/docs/standards/evidence_assessment.yaml).
