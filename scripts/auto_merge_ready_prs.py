#!/usr/bin/env python3
"""Conservatively admit reviewed PRs to an existing native GitHub merge queue.

Standalone, standard-library-only, dry run by default. Reads use GH_TOKEN;
--apply passes GH_MERGE_TOKEN only to the head-pinned enqueue subprocess.
No direct merge, bypass, draft promotion, review, label or comment writes.

GitHub removal events have no PR-head identifier. Retry holds therefore count
complete failed_checks history since the current head's commit timestamp.
The earliest matching tree in PR commits and force-push events prevents empty
commits, tree reverts and same-tree force pushes from clearing a hold. Old/backdated commits can retain conservative holds.
This is admission throttling; GitHub's queue CI remains the integration gate.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SHA = re.compile(r"[0-9a-f]{40}")
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
HOLD_LABELS = frozenset({"hold", "do-not-merge", "merge-queue:hold", "wip"})
DEFAULT_CACHE_GLOBS = (
    "**/cache/**", "**/caches/**", "**/*_cache/**",
    "**/*cache*.csv", "**/*cache*.tsv",
)
TRUSTED_ASSOCIATIONS = frozenset({"OWNER", "MEMBER", "COLLABORATOR"})
MAX_PAGES = 100  # A bounded read must fail visibly, never claim completeness.


class AdmissionError(ValueError):
    """An API or policy input cannot be established safely."""


@dataclass(frozen=True)
class Rules:
    checks: tuple[tuple[str, int | None], ...]
    review_required: bool


def timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise AdmissionError("missing timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise AdmissionError("invalid timestamp") from exc
    if result.tzinfo is None:
        raise AdmissionError("timestamp has no timezone")
    return result


def require_sha(value: Any) -> str:
    if not isinstance(value, str) or not SHA.fullmatch(value):
        raise AdmissionError("missing or malformed commit SHA")
    return value


def config(path: Path | None) -> tuple[str, ...]:
    if path is None:
        return DEFAULT_CACHE_GLOBS
    try:
        value = json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise AdmissionError("cannot read admission configuration") from exc
    if not isinstance(value, dict) or set(value) != {"cache_path_globs"}:
        raise AdmissionError("config must contain only cache_path_globs")
    globs = value["cache_path_globs"]
    if not isinstance(globs, list) or not globs or any(
        not isinstance(item, str) or not item or item.startswith("/")
        or ".." in item.split("/") or any(ord(c) < 32 for c in item)
        for item in globs
    ):
        raise AdmissionError("cache_path_globs must be nonempty relative glob strings")
    return tuple(globs)


class GitHub:
    """Thin gh adapter, injectable in tests; all API methods below are reads."""

    def __init__(self, repository: str):
        if not REPOSITORY.fullmatch(repository):
            raise AdmissionError("repository must be OWNER/REPO")
        self.repository = repository
        self.owner, self.name = repository.split("/")

    def gh(self, args: list[str], *, write: bool = False) -> str:
        env = os.environ.copy()
        token = env.pop("GH_MERGE_TOKEN", "").strip()
        if write:
            if not token:
                raise AdmissionError("--apply requires GH_MERGE_TOKEN")
            env["GH_TOKEN"] = token
        try:
            result = subprocess.run(
                ["gh", *args], env=env, capture_output=True, text=True,
                check=True, timeout=90,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            # Avoid retaining subprocess environments or user-supplied stderr.
            raise AdmissionError("GitHub write failed" if write else "GitHub read failed") from exc
        return result.stdout

    def get(self, endpoint: str) -> Any:
        raw = self.gh(["api", endpoint])
        try:
            return json.loads(raw)
        except ValueError as exc:
            raise AdmissionError("GitHub returned invalid JSON") from exc

    def pages(self, endpoint: str, *, key: str | None = None) -> list[dict]:
        rows: list[dict] = []
        expected: int | None = None
        separator = "&" if "?" in endpoint else "?"
        for page in range(1, MAX_PAGES + 1):
            payload = self.get(f"{endpoint}{separator}per_page=100&page={page}")
            if key is not None:
                if not isinstance(payload, dict) or not isinstance(payload.get("total_count"), int):
                    raise AdmissionError("missing paginated total_count")
                total = payload["total_count"]
                if expected is not None and total != expected:
                    raise AdmissionError("collection changed during pagination")
                expected = total
                payload = payload.get(key)
            if not isinstance(payload, list) or any(not isinstance(row, dict) for row in payload):
                raise AdmissionError("invalid paginated response")
            rows.extend(payload)
            if len(payload) < 100:
                if expected is not None and len(rows) != expected:
                    raise AdmissionError("truncated paginated response")
                return rows
        raise AdmissionError("pagination safety limit reached")

    def graphql(self, body: str, **variables: Any) -> dict:
        query = "query($owner:String!,$name:String!" + "".join(
            f",${key}:{'Int!' if isinstance(value, int) else 'String'}"
            for key, value in variables.items()
        ) + "){repository(owner:$owner,name:$name){" + body + "}}"
        args = ["api", "graphql", "-f", f"query={query}",
                "-f", f"owner={self.owner}", "-f", f"name={self.name}"]
        for key, value in variables.items():
            args.extend(["-F" if isinstance(value, int) else "-f", f"{key}={value}"])
        try:
            payload = json.loads(self.gh(args))
            if payload.get("errors"):
                raise AdmissionError("GraphQL returned errors")
            result = payload["data"]["repository"]
            if not isinstance(result, dict):
                raise AdmissionError("repository unavailable")
            return result
        except (ValueError, KeyError, TypeError) as exc:
            raise AdmissionError("invalid GraphQL response") from exc

    def connection(self, body: str, path: tuple[str, ...], *,
                   filtered_timeline: bool = False, **variables: Any) -> list[dict]:
        rows: list[dict] = []
        seen: set[str] = set()
        total: int | None = None
        cursor = ""
        for _ in range(MAX_PAGES):
            # GitHub rejects an empty cursor, so omit after on the first page.
            fragment = body.replace("AFTER", ",after:$cursor" if cursor else "")
            values = dict(variables)
            if cursor:
                values["cursor"] = cursor
            value = self.graphql(fragment, **values)
            try:
                for key in path:
                    value = value[key]
                nodes = value["nodes"]
                count = value["totalCount"]
                info = value["pageInfo"]
                if not isinstance(nodes, list) or any(not isinstance(n, dict) for n in nodes):
                    raise AdmissionError("invalid connection nodes")
                if not isinstance(count, int) or (total is not None and count != total):
                    raise AdmissionError("connection changed during pagination")
                total = count
                rows.extend(nodes)
                if info["hasNextPage"] is False:
                    # GitHub timeline totalCount includes nonmatching events
                    # even when itemTypes filters nodes. Exhausting pageInfo is
                    # the completeness proof for that API, not node equality.
                    if not filtered_timeline and len(rows) != total:
                        raise AdmissionError("truncated connection")
                    return rows
                cursor = info["endCursor"]
                if not isinstance(cursor, str) or not cursor or cursor in seen:
                    raise AdmissionError("invalid pagination cursor")
                seen.add(cursor)
            except (KeyError, TypeError) as exc:
                raise AdmissionError("unavailable or malformed connection") from exc
        raise AdmissionError("connection safety limit reached")

    def queue(self) -> dict[int, str]:
        nodes = self.connection(
            'mergeQueue(branch:"main"){entries(first:100 AFTER){totalCount '
            'pageInfo{hasNextPage endCursor} nodes{pullRequest{number headRefOid}}}}',
            ("mergeQueue", "entries"),
        )
        result: dict[int, str] = {}
        for row in nodes:
            try:
                number = row["pullRequest"]["number"]
                head = require_sha(row["pullRequest"]["headRefOid"])
                if not isinstance(number, int) or number <= 0 or number in result:
                    raise AdmissionError("invalid or repeated queue entry")
                result[number] = head
            except (KeyError, TypeError) as exc:
                raise AdmissionError("invalid queue entry") from exc
        return result

    def rules(self) -> Rules:
        rules = self.pages(f"repos/{self.repository}/rules/branches/main")
        if not any(rule.get("type") == "merge_queue" for rule in rules):
            raise AdmissionError("main does not require a native merge queue")
        if not any(rule.get("type") == "pull_request" for rule in rules):
            raise AdmissionError("main does not require pull requests")
        checks: set[tuple[str, int | None]] = set()
        reviews = False
        for rule in rules:
            parameters = rule.get("parameters", {})
            if rule.get("type") == "required_status_checks":
                for check in parameters.get("required_status_checks", []):
                    name = check.get("context")
                    app = check.get("integration_id")
                    if not isinstance(name, str) or not name or (app is not None and not isinstance(app, int)):
                        raise AdmissionError("invalid required check rule")
                    checks.add((name, None if app in (None, -1) else app))
            elif rule.get("type") == "pull_request":
                reviews |= bool(parameters.get("required_approving_review_count", 0)
                                or parameters.get("require_code_owner_review")
                                or parameters.get("require_last_push_approval")
                                or parameters.get("required_reviewers"))
        # Rulesets and classic protection can coexist. A null rule means none;
        # an API failure does not mean none.
        classic = self.graphql(
            'ref(qualifiedName:"refs/heads/main"){branchProtectionRule{'
            'requiresApprovingReviews requiresCodeOwnerReviews '
            'requireLastPushApproval requiredStatusChecks{context app{databaseId}}}}'
        )
        try:
            protection = classic["ref"]["branchProtectionRule"]
            if protection:
                reviews |= bool(protection["requiresApprovingReviews"]
                                or protection["requiresCodeOwnerReviews"]
                                or protection["requireLastPushApproval"])
                for check in protection["requiredStatusChecks"]:
                    app = check.get("app")
                    checks.add((check["context"], app["databaseId"] if app else None))
        except (KeyError, TypeError) as exc:
            raise AdmissionError("classic protection is unreadable") from exc
        if not checks:
            raise AdmissionError("no required check contexts established")
        return Rules(tuple(sorted(checks, key=lambda item: (item[0], item[1] or -1))), reviews)

    def integrity_reason(self) -> str:
        commit = self.get(f"repos/{self.repository}/commits/main")
        head = require_sha(commit.get("sha"))
        runs, _ = self.checks(head)
        matching = [run for run in runs if run.get("name") == "merge-integrity"
                    and run.get("app", {}).get("id") == 15368]
        if not matching:
            return "main_integrity_pending: current main has no trusted integrity check"
        if any(run.get("head_sha") != head or run.get("status") != "completed"
               for run in matching):
            return "main_integrity_pending: current main integrity check is pending"
        if any(run.get("conclusion") != "success" for run in matching):
            return "main_integrity_failed: current main integrity check did not pass"
        return ""

    def open_prs(self) -> list[dict]:
        return self.pages(f"repos/{self.repository}/pulls?state=open&base=main&sort=created&direction=asc")

    def pr(self, number: int) -> dict:
        value = self.get(f"repos/{self.repository}/pulls/{number}")
        graph = self.graphql(
            "pullRequest(number:$number){headRefOid mergeable mergeStateStatus reviewDecision}",
            number=number,
        ).get("pullRequest")
        if not isinstance(value, dict) or not isinstance(graph, dict):
            raise AdmissionError("PR is unreadable")
        if value.get("head", {}).get("sha") != graph.get("headRefOid"):
            raise AdmissionError("PR head changed during read")
        return dict(value, **graph)

    def reviews(self, number: int) -> list[dict]:
        return self.pages(f"repos/{self.repository}/pulls/{number}/reviews")

    def checks(self, head: str) -> tuple[list[dict], list[dict]]:
        return (
            self.pages(f"repos/{self.repository}/commits/{head}/check-runs?filter=latest", key="check_runs"),
            self.pages(f"repos/{self.repository}/commits/{head}/statuses"),
        )

    def files(self, number: int, expected: int) -> list[dict]:
        rows = self.pages(f"repos/{self.repository}/pulls/{number}/files")
        if any(not isinstance(row.get("filename"), str) or not row["filename"] for row in rows):
            raise AdmissionError("changed-file name unavailable")
        if len(rows) != expected or len({row["filename"] for row in rows}) != len(rows):
            raise AdmissionError("changed files are truncated or duplicated")
        return rows

    def history(self, number: int) -> list[dict]:
        return self.connection(
            'pullRequest(number:$number){timelineItems(first:100 AFTER,'
            'itemTypes:[REMOVED_FROM_MERGE_QUEUE_EVENT,HEAD_REF_FORCE_PUSHED_EVENT]){totalCount '
            'pageInfo{hasNextPage endCursor} nodes{__typename '
            '... on RemovedFromMergeQueueEvent{createdAt reason} '
            '... on HeadRefForcePushedEvent{createdAt '
            'beforeCommit{oid committedDate tree{oid}} '
            'afterCommit{oid committedDate tree{oid}}}}}}',
            ("pullRequest", "timelineItems"), filtered_timeline=True, number=number,
        )

    def commits(self, number: int, expected: int) -> list[dict]:
        rows = self.pages(f"repos/{self.repository}/pulls/{number}/commits")
        if len(rows) != expected:
            raise AdmissionError("PR commit history is truncated")
        return rows

    def enqueue(self, number: int, head: str, pull_request_id: str) -> None:
        if not isinstance(pull_request_id, str) or not pull_request_id:
            raise AdmissionError("PR node identity unavailable")
        require_sha(head)
        # Unlike `gh pr merge`, this operation cannot become a direct merge
        # if an administrator removes the queue between our read and write.
        query = (
            "mutation($id:ID!,$head:GitObjectID!){enqueuePullRequest(input:{"
            "pullRequestId:$id,expectedHeadOid:$head}){mergeQueueEntry{"
            "pullRequest{id number headRefOid isInMergeQueue}}}}"
        )
        raw = self.gh(["api", "graphql", "-f", f"query={query}",
                       "-f", f"id={pull_request_id}", "-f", f"head={head}"], write=True)
        try:
            payload = json.loads(raw)
            if payload.get("errors"):
                raise AdmissionError("queue-only mutation failed")
            pr = payload["data"]["enqueuePullRequest"]["mergeQueueEntry"]["pullRequest"]
            if (pr["id"] != pull_request_id or pr["number"] != number
                    or pr["headRefOid"] != head or pr["isInMergeQueue"] is not True):
                raise AdmissionError("queue admission receipt does not match verified PR")
        except (ValueError, KeyError, TypeError) as exc:
            raise AdmissionError("queue admission could not be confirmed") from exc


def basic_reason(pr: dict) -> str:
    if pr.get("state") != "open" or pr.get("base", {}).get("ref") != "main":
        return "not an open PR targeting main"
    if pr.get("draft") is not False:
        return "draft or unknown draft state"
    if not isinstance(pr.get("assignees"), list) or any(
        assignee.get("type") != "Bot" for assignee in pr["assignees"]
    ):
        return "human or unknown assignee holds this PR"
    if not isinstance(pr.get("labels"), list):
        return "labels unreadable"
    if any(str(label.get("name", "")).casefold() in HOLD_LABELS for label in pr["labels"]):
        return "hold label"
    return ""


def review_reason(reviews: list[dict], pr: dict, rules: Rules) -> str:
    latest: dict[str, dict] = {}
    requested_changes: set[str] = set()
    for review in sorted(reviews, key=lambda row: row.get("id", 0)):
        user = review.get("user") or {}
        login = user.get("login")
        if not isinstance(login, str) or not login:
            return "review author unavailable"
        # Pending reviews are private drafts, not a replacement decision.
        identity = login.casefold()
        state = review.get("state")
        if state == "CHANGES_REQUESTED":
            requested_changes.add(identity)
        elif state in {"APPROVED", "DISMISSED"}:
            requested_changes.discard(identity)
        if state != "PENDING":
            latest[identity] = review
    if requested_changes:
        return "changes requested"
    if rules.review_required and pr.get("reviewDecision") != "APPROVED":
        return "GitHub review requirements are not satisfied"
    for review in latest.values():
        if (review.get("state") == "APPROVED"
                and review.get("commit_id") == pr["headRefOid"]
                and review.get("author_association") in TRUSTED_ASSOCIATIONS
                and review.get("user", {}).get("login") != pr.get("user", {}).get("login")):
            return ""
    return "no trusted latest approval on the current head"


def check_reason(runs: list[dict], statuses: list[dict], rules: Rules, head: str) -> str:
    latest_status: dict[str, dict] = {}
    for status in sorted(statuses, key=lambda row: row.get("id", 0)):
        latest_status[status.get("context", "")] = status
    for name, app in rules.checks:
        matching = [run for run in runs if run.get("name") == name
                    and (app is None or run.get("app", {}).get("id") == app)]
        legacy = latest_status.get(name) if app is None else None
        if not matching and legacy is None:
            return f"required check missing from its trusted source: {name}"
        if any(run.get("head_sha") != head or run.get("status") != "completed"
               or run.get("conclusion") != "success" for run in matching):
            return f"required check is not successful on the current head: {name}"
        if legacy is not None and legacy.get("state") != "success":
            return f"required status is not successful: {name}"
    return ""


def cache_path(path: str, globs: tuple[str, ...]) -> bool:
    return any(fnmatch.fnmatchcase(path, pattern)
               or (pattern.startswith("**/") and fnmatch.fnmatchcase(path, pattern[3:]))
               for pattern in globs)


def cache_claims(files: list[dict], globs: tuple[str, ...]) -> set[str]:
    claims: set[str] = set()
    for row in files:
        paths = {row.get("filename"), row.get("previous_filename")} - {None}
        if any(not isinstance(path, str) for path in paths):
            raise AdmissionError("invalid changed-file path")
        matches = {path for path in paths if cache_path(path, globs)}
        if not matches:
            continue
        patch = row.get("patch")
        if not isinstance(patch, str) or not patch:
            raise AdmissionError("shared cache patch missing")
        # File reservations do not need row parsing, but validating the patch
        # prevents missing/truncated API evidence from silently passing.
        lines = patch.splitlines()
        additions = sum(line.startswith("+") for line in lines)
        deletions = sum(line.startswith("-") for line in lines)
        if (additions != row.get("additions") or deletions != row.get("deletions")
                or not any(line.startswith("@@ ") for line in lines)):
            raise AdmissionError("shared cache patch truncated or malformed")
        claims.update(matches)
    return claims


def retry_reason(commits: list[dict], events: list[dict], head: str, now: datetime) -> str:
    if not commits or commits[-1].get("sha") != head:
        raise AdmissionError("PR commit history does not end at current head")
    try:
        tree = require_sha(commits[-1]["commit"]["tree"]["sha"])
        dates = [timestamp(row["commit"]["committer"]["date"])
                 for row in commits if row["commit"]["tree"]["sha"] == tree]
        # Force-pushed commits may no longer appear in the PR's current commit
        # list. Preserve their tree/date evidence from the immutable timeline;
        # otherwise amending only a timestamp would replenish retry attempts.
        for event in events:
            if event.get("__typename") == "HeadRefForcePushedEvent":
                for key in ("beforeCommit", "afterCommit"):
                    previous = event[key]
                    require_sha(previous["oid"])
                    previous_tree = require_sha(previous["tree"]["oid"])
                    previous_date = timestamp(previous["committedDate"])
                    if previous_tree == tree:
                        dates.append(previous_date)
        if any(date > now for date in dates):
            raise AdmissionError("head has a future commit timestamp")
        since = min(dates)
        failures = 0
        for event in events:
            when = timestamp(event.get("createdAt"))
            if when > now:
                raise AdmissionError("queue event has a future timestamp")
            if event.get("__typename") == "HeadRefForcePushedEvent":
                continue
            if not isinstance(event.get("reason"), str) or not event["reason"]:
                raise AdmissionError("queue ejection reason is unavailable")
            if event.get("reason") == "failed_checks" and when >= since:
                failures += 1
    except (KeyError, TypeError) as exc:
        raise AdmissionError("commit or ejection history is unreadable") from exc
    return f"held after {failures} failed-check queue ejections on unchanged content" if failures >= 2 else ""


def eligibility(api: GitHub, number: int, rules: Rules, globs: tuple[str, ...],
                *, expected_head: str | None = None) -> tuple[dict, set[str], str]:
    pr = api.pr(number)
    reason = basic_reason(pr)
    head = require_sha(pr.get("headRefOid"))
    if expected_head is not None and head != expected_head:
        return pr, set(), "head changed during admission"
    if reason:
        return pr, set(), reason
    if pr.get("mergeable") != "MERGEABLE" or pr.get("mergeStateStatus") != "CLEAN":
        return pr, set(), "PR is not mergeable with satisfied branch rules"
    reason = review_reason(api.reviews(number), pr, rules)
    if reason:
        return pr, set(), reason
    reason = check_reason(*api.checks(head), rules, head)
    if reason:
        return pr, set(), reason
    reason = retry_reason(api.commits(number, pr["commits"]), api.history(number), head,
                          datetime.now(timezone.utc))
    if reason:
        return pr, set(), reason
    claims = cache_claims(api.files(number, pr["changed_files"]), globs)
    # Review/check/file/history reads are not atomic. Ensure they still refer
    # to the same head and no human hold arrived before returning eligibility.
    final = api.pr(number)
    if final.get("headRefOid") != head:
        return final, set(), "head changed during admission"
    reason = basic_reason(final)
    if reason:
        return final, set(), reason
    if final.get("mergeable") != "MERGEABLE" or final.get("mergeStateStatus") != "CLEAN":
        return final, set(), "branch eligibility changed during admission"
    if rules.review_required and final.get("reviewDecision") != "APPROVED":
        return final, set(), "review requirements changed during admission"
    return final, claims, ""


def run(api: GitHub, *, apply: bool, max_admissions: int, globs: tuple[str, ...]) -> dict:
    report: dict = {"repository": api.repository, "mode": "apply" if apply else "dry-run",
                    "rows": [], "errors": [], "admitted": 0}
    reserved: dict[str, int] = {}
    claimed_by_queue: dict[tuple[int, str], set[str]] = {}
    write_outcome_unknown = False
    try:
        rules = api.rules()
        api.queue()  # An absent/unreadable queue stops even an empty sweep.
        integrity = api.integrity_reason()
        report["main_integrity"] = integrity or "passed"
        prs = api.open_prs()
        prs.sort(key=lambda row: (timestamp(row["created_at"]), row["number"]))
    except (AdmissionError, KeyError, TypeError) as exc:
        report["errors"].append(str(exc))
        return report
    for listed in prs:
        number = listed.get("number")
        row = {"number": number, "status": "held", "reason": ""}
        report["rows"].append(row)
        if not isinstance(number, int) or number <= 0:
            row.update(status="error", reason="invalid PR number")
            continue
        if write_outcome_unknown:
            row["reason"] = "previous enqueue outcome unknown; sweep stopped"
            continue
        if integrity:
            row["reason"] = integrity
            continue
        if report["admitted"] >= max_admissions:
            row["reason"] = "admission limit reached"
            continue
        if reason := basic_reason(listed):
            row["reason"] = reason
            continue
        write_started = False
        try:
            # The queue can change after every admission. A queue member with
            # unreadable files blocks the sweep, as its reservations are unknown.
            queued = api.queue()
            if number in queued:
                row.update(status="already_queued", reason="already in native queue")
                continue
            active = dict(reserved)
            for queued_number, queued_head in queued.items():
                key = (queued_number, queued_head)
                if key not in claimed_by_queue:
                    queued_pr = api.pr(queued_number)
                    if queued_pr.get("headRefOid") != queued_head:
                        raise AdmissionError("queued PR changed while reading cache claims")
                    claimed_by_queue[key] = cache_claims(
                        api.files(queued_number, queued_pr["changed_files"]), globs)
                for path in claimed_by_queue[key]:
                    active[path] = queued_number
            pr, claims, reason = eligibility(api, number, rules, globs)
            if reason:
                row["reason"] = reason
                continue
            collisions = sorted(claims & active.keys())
            if collisions:
                row["reason"] = "shared cache reserved by " + ", ".join(
                    f"#{active[path]} ({path})" for path in collisions[:5])
                continue
            # Re-read rules and queue immediately before the final verification;
            # no fallback when the queue disappears or policies change.
            if reason := api.integrity_reason():
                row["reason"] = reason
                continue
            if api.rules() != rules or api.queue() != queued:
                row["reason"] = "rules or queue changed; reconsider next sweep"
                continue
            pr, final_claims, reason = eligibility(
                api, number, rules, globs, expected_head=pr["headRefOid"])
            if reason or final_claims != claims:
                row["reason"] = reason or "cache changes changed during admission"
                continue
            if api.queue() != queued:
                row["reason"] = "queue changed before admission"
                continue
            # Expensive history/file reads above can overlap human reviews or
            # a main integrity failure. Re-read these volatile gates at the
            # actual action boundary, including zero-required-review repos.
            final = api.pr(number)
            if final.get("headRefOid") != pr["headRefOid"]:
                row["reason"] = "head changed at admission boundary"
                continue
            reason = basic_reason(final)
            if not reason and (final.get("mergeable") != "MERGEABLE"
                               or final.get("mergeStateStatus") != "CLEAN"):
                reason = "branch eligibility changed at admission boundary"
            if not reason:
                reason = review_reason(api.reviews(number), final, rules)
            if not reason:
                reason = check_reason(*api.checks(pr["headRefOid"]), rules, pr["headRefOid"])
            if not reason:
                reason = api.integrity_reason()
            if reason:
                row["reason"] = reason
                continue
            row["head"] = pr["headRefOid"]
            if apply:
                write_started = True
                api.enqueue(number, pr["headRefOid"], pr["node_id"])
            row.update(status="enqueued" if apply else "would_enqueue", reason="all admission gates satisfied")
            report["admitted"] += 1
            reserved.update(dict.fromkeys(claims, number))
        except (AdmissionError, KeyError, TypeError) as exc:
            write_outcome_unknown |= write_started
            reason = ("enqueue outcome unknown; sweep stopped: " if write_started else "") + str(exc)
            row.update(status="error", reason=reason)
    return report


def bounded_count(value: str) -> int:
    parsed = int(value)
    if not 1 <= parsed <= 50:
        raise argparse.ArgumentTypeError("must be between 1 and 50")
    return parsed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repository", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--max-admissions", type=bounded_count, default=3)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.apply and not os.environ.get("GH_MERGE_TOKEN", "").strip():
            raise AdmissionError("--apply requires GH_MERGE_TOKEN")
        result = run(GitHub(args.repository), apply=args.apply,
                     max_admissions=args.max_admissions, globs=config(args.config))
        output = json.dumps(result, indent=2) + "\n"
        if args.report:
            args.report.write_text(output)
        print(output, end="")
        return int(bool(result["errors"] or any(row["status"] == "error" for row in result["rows"])))
    except (AdmissionError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
