# Merging through the queue

When `main` requires GitHub's native merge queue, a reviewed PR enters the queue
and its required checks run again against the candidate containing current
`main` and preceding queued changes. A green PR check run alone does not show
that this combined candidate passed.

After required PR checks pass, enqueue the reviewed revision with:

```sh
gh pr merge PR_NUMBER --repo CultureBotAI/CultureMech --match-head-commit HEAD_SHA
```

The queue selects the configured merge method. Avoid `--admin`, which bypasses
the queue. On failure, inspect the PR timeline and the `merge_group` Actions
run, fix the cause, and enqueue the updated revision after its PR checks pass.

The changed-Python check compares against the queue group base so changes earlier in the candidate are included. The nightly merge-YAML freshness report and Pages deployment have separate triggers.

Required workflow triggers and stable job names are checked by
`tests/test_merge_queue_workflows.py`. Coordinate job renames with the `main`
ruleset so the queue continues receiving every expected result.

References: [GitHub merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
and [`gh pr merge`](https://cli.github.com/manual/gh_pr_merge).
