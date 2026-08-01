# Curation history

Append-only provenance for curation sessions. One record per session per target,
written once and **never edited afterwards**. Corrections go in a new record that
references the old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

## Why this exists

Nothing else in the repo records *which model, using which tool, changed what,
why, and under which issue*. Git tells you a commit happened; it does not tell you
that an ingredient was grounded against a specific CHEBI release, or which
deep-research provider produced a recipe correction, or that a review deliberately
changed nothing.

That gap matters more as autonomous agents start doing the changing. See
`culturebotai-claw/docs/AUTONOMOUS_LOOPS.md`.

## Why the layout looks like that

The directory-per-slug plus unguessable `shortid` is the whole design. Two agents
curating the same medium concurrently cannot write the same file, so this layer
has **no merge-conflict surface**. A single shared changelog would conflict on
every parallel PR; this never does. That matters here more than most places —
CultureMech carries over 15,000 media records and several agents work it at once.

## Writing a record

Do not hand-write the filename or the timestamp — scaffold it:

```bash
just new-history --kind record --slug 1_10_r2a_medium \
  --target-root data/normalized_yaml/bacterial \
  --event EDIT --outcome changed \
  --sections ingredients,solutions \
  --summary "Ground two unmapped ingredients to CHEBI" \
  --model claude-opus-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/CultureMech/issues/123 \
  --details "What was done, what evidence was used, how it was validated."
```

Omit `--details` and you get a TODO placeholder to edit before committing —
`just validate-history` **fails** while it is still there, so an unfilled record
cannot slip through. The command prints the record path as its final stdout line,
so scripts can capture it.

`--kind record` and `--kind schema` can derive the target path from `--slug` plus
`--target-root`. Every other kind needs an explicit `--path`, because only those
two are reliably `.yaml`.

The `--target-root` for a medium is the taxon-group directory the record lives in:
`data/normalized_yaml/bacterial`, `.../archaea`, `.../fungal`, `.../algae`,
`.../solutions`, or `.../specialized`.

Then validate and stage:

```bash
just validate-history history/records/1_10_r2a_medium/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

Outcome is **orthogonal** to event on purpose. A `REVIEW` that found nothing is
`no_change` — a real result worth recording, because it says something was
checked. An `EDIT` that hit a wall is `blocked`, and `details` must say what the
wall was so the next session does not rediscover it.

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## How strictly this is enforced

Deliberately split:

- **Presence is advisory.** CI warns when a medium under `data/normalized_yaml/`
  changes without a matching history record. It does not block. A hard gate on
  provenance blocks legitimate work at inconvenient moments and trains people to
  route around it.
- **Validity is not.** If you write a record it must be schema-valid, and
  `just validate-history` fails like any other validation error.

## Where the schema lives

Two copies, on purpose:

- **Canonical**: `culturebotai-claw/shared/history/history.yaml`, with the
  scaffolder at `culturebotai-claw/src/kg_microbe_history/`.
- **Vendored here**: `src/culturemech/schema/history.yaml`, byte-identical.

Check that identity rather than trusting this file — with a claw checkout:

```bash
diff "${CLAW_SRC:-../culturebotai-claw/src}/../shared/history/history.yaml" \
     src/culturemech/schema/history.yaml && echo "in sync"
```

Do not write the md5 into this prose instead. TraitMech's copy of this README did
exactly that, and the hash went stale one commit later when the schema gained a
field — which is the argument against a hash in prose at all: nothing recomputes
it, so it decays into a confident false negative. A runnable command cannot go
stale.

The vendored copy exists so validation has **no dependency on claw**, which is
private — a public repo's CI cannot check it out without a token. `just
validate-history` and the `curation-history` workflow both use the local copy and
work with no claw checkout at all.

Only `just new-history` needs claw, via `CLAW_SRC` (default:
`../culturebotai-claw/src`). That is a dev-time scaffolder, and anyone writing
curation records has claw checked out.

Changing the schema means changing the canonical copy and re-vendoring here — the
same hub-and-spoke rule as `mech_shared.yaml`. Nothing automated enforces that rule
for this file yet. CultureMech has no vendored-drift check of its own to append it
to, and the obvious shortcut does not work: the canonical copy lives in claw, which
is private, so a tokenless `raw.githubusercontent` fetch cannot reach it. Until
that is solved, the `diff` above is the check, run by hand.
