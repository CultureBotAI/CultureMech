# Linked Middlebrook Ingredient Repair

Eleven normalized records are applied locally, not an all-record completion
or publication claim. The [plan](plan.json) adds 274 evidence entries,
23 references and eleven append-only history events. Its 781 claims account
for all 244 prior quantity slots and 234 source/input nodes, including the
separately represented conditional alternative. No taxa-media association,
new record, permanent-ID change or record deletion was added.

## Scientific Changes

- Nine KOMODO records now follow their own recipe tables. Source-listed
  albumin is restored and the false LB expansion removed; genuine casein
  digest and NaCl are retained. Displayed Gram Amount precision and the
  literal per-liter basis are preserved, not explained by an invented dilution.
- Null water, glycerol and NAOH amounts stay unquantified. KOMODO 645a retains
  its provider-reported hemin 0.04 g/L, while the original DSMZ wording of
  60 micromoles without a denominator is separately documented. No 60 uM
  conversion, NaOH dose or experimentally glycerol-free formulation is inferred.
- DSMZ 645 separates its 19 g commercial-base route, later 100 ml OADC dose
  and conditional from-scratch alternative. The alternative's 1,000 ml water
  is not added to the commercial route's 900 ml. The commercial mixture's
  erroneous pure-agar grounding is withdrawn.
- DSMZ 911 separates its 21 g commercial base, base-table detail and later
  100 ml OADC dose. Stock composition is not a finished-medium concentration
  or an additional simultaneous set of basal inputs. pH is not a heat step.
- Nine reciprocal family edges now distinguish source derivation, explicitly
  strain-modified entries, and the uncertain hemin-family relationship.
  A shared copied ingredient signature no longer establishes exact identity.

Every changed scientific claim has a persistent source URL and exact excerpt
attached in YAML. Source titles, discovery mode, source type, access date and
capture hash are recorded; unavailable authors and publication years are not
invented. Existing chemical annotations are otherwise preserved, not recertified.

## Evidence and Checks

The initial [direct refresh](source-refresh.json) fetched all fourteen sources
with HTTP 200 and matching bytes. Subsequent [live](live.json) and
[retry](live-retry.json) attempts returned HTTP 403; those failures remain
unchanged. [Cached validation](cached.json) explicitly uses the hash-checked
captures, verifies their identities and original PDF binaries, and passes all
297 reference checks. This is not a successful later live refresh.

All 792 focused tests, lint and formatting pass. The [application receipt](apply.json)
records the independent preview/applied audits, exact readback and no-op rerun.
All eleven post-edit schema/strict/reference CLI checks pass. Full-corpus
strict-schema and ID checks pass for 15,910 normalized records.

Four metadata indexes were regenerated through the maintained generator, with
changes restricted to these eleven IDs. The [runtime retention audit](merge-retention.json)
groups all 15,910 inputs and verifies that all eleven repaired formulations
remain separate, schema-valid and claim-preserving. Derived merged YAML was
not written. Corpus variant-link validation has no findings under its current
ID-fallback rules; the separate acid-queue audit found [21 stale exact family
paths](issue-stale-family-paths.md) outside this repaired cohort. Product validation
retains 91 non-blocking warnings and 96,042 no-adapter skips. Global merge
verification still fails with 1,247 name conflicts and 3,287 fingerprint issues;
freshness has 4,275 tracked-only, 8,732 fresh-only and 2,045 changed files.
The fast tier passes **10,086 tests** (16 skipped, 1,945 deselected). The
[consolidated validation receipt](validation.json) verifies terminal checks
against the current worktree and retains all failed live/global gates. Final
local QA passes 24 checks, including a new cumulative-accounting run. This uses
the existing partial locked Python 3.13 environment, not clean CI or the
complete test suite.

[Cumulative accounting](cumulative-audit.json) is 5,198 edited records and
33,593 added evidence entries. [Follow-up coverage](followup-coverage.json)
remains 11,798 exact normalized paths, with 4,112 outside these reports.
All eleven canonical reports already existed and now link to the current
old/new claim ledgers under `records/`; no duplicate `- Record:` entries were
created. Report presence does not mean every scientific issue is resolved.

See the [adversarial review](adversarial-review.md), [open source issue](issue-source-limits.md)
and [remaining work](next-work.md). Publication is still incomplete; no
commit, push, public issue, PR, merge or branch deletion occurred in this batch.
