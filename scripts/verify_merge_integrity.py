#!/usr/bin/env python3
"""Reconstruct every single-parent PR landing in a push without executing PR code.

Requires Git >= 2.38 and authenticated gh. Exit 0 means the range was examined;
explicitly skipped multi-parent commits are not verified. A single-parent
commit without a merged PR mapping is incomplete: API propagation delays cannot
be distinguished safely from a direct push or rebase landing.
Exit 1 means at least one reconstructed tree differs; exit 2 means incomplete
coverage (including missing history, API errors, conflicts, or reporting errors).
An issue is filed only for a demonstrated tree mismatch, never for an error.

Based on DisMech's merge-tree monitor, extended with exact API identity checks,
whole-range failure handling, isolated Git storage, and structured evidence.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
ISSUE_MARKER = "<!-- claw-merge-integrity -->"
TIMEOUT = 120
MAX_PAGES = 1000
MAX_MISSING_OBJECTS = 32
MISSING_OBJECT = re.compile(
    r"(?:unable to read (?:blob|tree) object |bad tree object )([0-9a-f]{40}|[0-9a-f]{64})(?![0-9a-f])"
)


class Incomplete(RuntimeError):
    """Evidence was insufficient; this is not evidence of corruption."""


def command(args: list[str], *, cwd: Path | None = None,
            env: dict[str, str] | None = None, input_text: str | None = None,
            check: bool = True) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(args, cwd=cwd, env=env, input=input_text,
                                capture_output=True, text=True, timeout=TIMEOUT,
                                check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise Incomplete(f"{args[0]} could not complete: {type(exc).__name__}") from exc
    if check and result.returncode:
        raise Incomplete(f"{args[0]} failed (exit {result.returncode}): "
                         f"{result.stderr.strip()[:500]}")
    return result


class GitHub:
    def request(self, endpoint: str, method: str = "GET",
                body: dict[str, Any] | None = None) -> Any:
        args = ["gh", "api", "--hostname", "github.com", endpoint,
                "--method", method, "-H", "Accept: application/vnd.github+json",
                "-H", "X-GitHub-Api-Version: 2022-11-28"]
        if body is not None:
            args.extend(["--input", "-"])
        result = command(args, input_text=json.dumps(body) if body is not None else None)
        try:
            return json.loads(result.stdout)
        except (ValueError, TypeError) as exc:
            raise Incomplete("GitHub returned invalid JSON") from exc

    def pages(self, endpoint: str) -> list[dict[str, Any]]:
        rows = []
        separator = "&" if "?" in endpoint else "?"
        for page in range(1, MAX_PAGES + 1):
            payload = self.request(f"{endpoint}{separator}per_page=100&page={page}")
            if not isinstance(payload, list) or any(not isinstance(x, dict) for x in payload):
                raise Incomplete("GitHub returned an invalid list page")
            rows.extend(payload)
            if len(payload) < 100:
                return rows
        raise Incomplete("GitHub pagination exceeded the bounded page limit")


class Git:
    """Use a disposable object store; neither index nor worktree is accessed.

The source config is read solely for identity/object paths. Repository/global
merge drivers, hooks, filters, replace objects, and Git environment overrides
cannot run during reconstruction. New objects/fetch state stay in the tempdir.
"""

    def __init__(self, root: Path, repository: str, directory: Path):
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith("GIT_")}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_NO_REPLACE_OBJECTS="1", GIT_TERMINAL_PROMPT="0", LC_ALL="C")
        self.path = directory
        source = ["git", "-c", f"core.hooksPath={os.devnull}", "-C", str(root)]
        origin = command([*source, "remote", "get-url", "origin"], env=self.env).stdout.strip()
        match = re.fullmatch(r"(?:https://github\.com/|git@github\.com:|ssh://git@github\.com/)([^/]+/[^/]+?)(?:\.git)?/?", origin)
        if not match or match.group(1).lower() != repository.lower():
            raise Incomplete("origin does not identify the requested GitHub repository")
        self.url = f"https://github.com/{repository}.git"
        objects = command([*source, "rev-parse", "--path-format=absolute", "--git-path", "objects"],
                          env=self.env).stdout.strip()
        if not Path(objects).is_dir() or "\n" in objects:
            raise Incomplete("source Git object directory is invalid")
        command(["git", "init", "--bare", str(directory)], env=self.env)
        (directory / "objects" / "info" / "alternates").write_text(objects + "\n")

    def run(self, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return command(["git", "-c", f"core.hooksPath={os.devnull}",
                        "-c", "gc.auto=0", "-c", "maintenance.auto=false",
                        "-c", "protocol.ext.allow=never", "--git-dir", str(self.path),
                        *args], env=self.env, check=check)

    def text(self, *args: str) -> str:
        return self.run(*args).stdout.strip()

    def have_commit(self, sha: str) -> bool:
        return self.run("cat-file", "-e", f"{sha}^{{commit}}", check=False).returncode == 0

    def ensure_commit(self, sha: str, number: int | None = None) -> None:
        if not OID.fullmatch(sha) or set(sha) == {"0"}:
            raise Incomplete("missing or invalid immutable commit ID")
        if self.have_commit(sha):
            return
        self.run("fetch", "--no-tags", "--no-write-fetch-head", "--no-recurse-submodules",
                 self.url, sha, check=False)
        if not self.have_commit(sha) and number is not None:
            # The source branch may have been deleted. Fetching GitHub's retained
            # PR ref is a transport fallback, never permission to use a new head.
            self.run("fetch", "--no-tags", "--no-write-fetch-head", "--no-recurse-submodules",
                     self.url, f"refs/pull/{number}/head", check=False)
        if not self.have_commit(sha):
            raise Incomplete(f"immutable commit {sha} is unavailable")

    def merge_tree(self, parent: str, head: str) -> str:
        """Hydrate only immutable objects named by a failed reconstruction.

Full-history partial clones may have commits but omit their blobs. Fetch these
into our isolated store, never by inheriting the source's promisor/configuration
or materializing its entire history. Unknown errors and repeated missing objects
fail closed, and the bounded loop also handles inaccessible upstream objects.
        """
        fetched: set[str] = set()
        for _ in range(MAX_MISSING_OBJECTS + 1):
            merged = self.run("merge-tree", "--write-tree", parent, head, check=False)
            expected = merged.stdout.splitlines()[0] if merged.stdout else ""
            if not merged.returncode and OID.fullmatch(expected):
                return expected
            missing = MISSING_OBJECT.search(merged.stderr)
            if not missing:
                raise Incomplete("merge-tree could not reconstruct a clean merge (conflict or missing history)")
            oid = missing.group(1)
            if oid in fetched or len(fetched) >= MAX_MISSING_OBJECTS:
                raise Incomplete("merge-tree exceeded its missing-object recovery limit")
            if self.run("cat-file", "-e", oid, check=False).returncode == 0:
                raise Incomplete("merge-tree could not read an existing object")
            fetched.add(oid)
            self.run("fetch", "--no-tags", "--no-write-fetch-head", "--no-recurse-submodules",
                     self.url, oid, check=False)
            if self.run("cat-file", "-e", oid, check=False).returncode:
                raise Incomplete(f"immutable reconstruction object {oid} is unavailable")
        raise Incomplete("merge-tree exceeded its missing-object recovery limit")


def pr_identity(pr: dict[str, Any], repository: str, branch: str,
                commit: str) -> tuple[int, str]:
    try:
        number, head = pr["number"], pr["head"]["sha"]
        valid = (isinstance(number, int) and not isinstance(number, bool) and number > 0
                 and pr["state"] == "closed" and bool(pr["merged_at"])
                 and pr["merge_commit_sha"] == commit
                 and pr["base"]["repo"]["full_name"].lower() == repository.lower()
                 and pr["base"]["ref"] == branch
                 and isinstance(head, str) and OID.fullmatch(head))
    except (KeyError, TypeError, AttributeError) as exc:
        raise Incomplete("PR mapping lacks required identity evidence") from exc
    if not valid:
        raise Incomplete("PR mapping does not match the merged commit, target, or head")
    return number, head


def verify_commit(git: Git, api: GitHub, repository: str, branch: str,
                  commit: str) -> dict[str, Any]:
    result: dict[str, Any] = {"commit": commit}
    try:
        parents = git.text("rev-list", "--parents", "-n", "1", commit).split()[1:]
        if len(parents) != 1:
            return dict(result, status="skipped_merge_commit", detail=f"{len(parents)} parents")
        result["parent"] = parents[0]
        associated = api.pages(f"repos/{repository}/commits/{commit}/pulls")
        if any("merge_commit_sha" not in pr or "number" not in pr for pr in associated):
            raise Incomplete("associated PR response lacks merge identity fields")
        candidates = [pr for pr in associated if pr.get("merge_commit_sha") == commit]
        if not candidates:
            raise Incomplete("no exact merged PR mapping; direct/rebase or delayed API association is unverified")
        if len(candidates) != 1:
            raise Incomplete("multiple PRs map to this merge commit")
        number, head = pr_identity(candidates[0], repository, branch, commit)
        detail = api.request(f"repos/{repository}/pulls/{number}")
        if not isinstance(detail, dict) or detail.get("merged") is not True:
            raise Incomplete("PR detail does not confirm a merged PR")
        if pr_identity(detail, repository, branch, commit) != (number, head):
            raise Incomplete("PR head changed between associated-PR and detail lookups")
        result.update(pr_number=number, head=head)
        git.ensure_commit(head, number)
        expected = git.merge_tree(parents[0], head)
        actual = git.text("rev-parse", f"{commit}^{{tree}}")
        # A reused PR branch or racing API snapshot must never become an incident.
        final_pr = api.request(f"repos/{repository}/pulls/{number}")
        if (not isinstance(final_pr, dict) or final_pr.get("merged") is not True
                or pr_identity(final_pr, repository, branch, commit) != (number, head)):
            raise Incomplete("PR identity changed during reconstruction")
        result.update(expected_tree=expected, actual_tree=actual,
                      status="verified" if expected == actual else "mismatch")
        if expected != actual:
            result["changed_paths"] = git.text("diff-tree", "--no-commit-id", "--name-only", "-r",
                                                expected, actual).splitlines()
        return result
    except Incomplete as exc:
        return dict(result, status="incomplete", detail=str(exc))


def report_issue(api: GitHub, report: dict[str, Any]) -> str | None:
    mismatches = [row for row in report["commits"] if row["status"] == "mismatch"]
    if not mismatches:
        return None
    repository = report["repository"]
    lines = [ISSUE_MARKER, "A pushed tree differs from its reconstructed PR merge.", "",
             f"Range: `{report['before']}..{report['after']}`.", "",
             "Inspect the evidence before diagnosing lost content or GitHub corruption."]
    for row in mismatches:
        lines.extend(["", f"- Commit `{row['commit']}`, PR #{row['pr_number']}",
                      f"  - Parent: `{row['parent']}`; PR head: `{row['head']}`",
                      f"  - Expected tree: `{row['expected_tree']}`",
                      f"  - Actual tree: `{row['actual_tree']}`"])
    body = "\n".join(lines) + "\n"
    existing = [issue for issue in api.pages(f"repos/{repository}/issues?state=open")
                if "pull_request" not in issue and ISSUE_MARKER in (issue.get("body") or "")]
    if existing:
        number = min(issue["number"] for issue in existing)
        # Do not repeat the same evidence when a workflow is re-run.
        prior = api.pages(f"repos/{repository}/issues/{number}/comments")
        known_bodies = [issue.get("body", "") for issue in existing] + [x.get("body", "") for x in prior]
        if not any(body == value for value in known_bodies):
            api.request(f"repos/{repository}/issues/{number}/comments", "POST", {"body": body})
        return f"https://github.com/{repository}/issues/{number}"
    issue = api.request(f"repos/{repository}/issues", "POST",
                        {"title": "Merge integrity: reconstructed tree mismatch", "body": body})
    return issue["html_url"]


def verify(repository: str, root: Path, before: str, after: str,
           api: GitHub | None = None, report_issues: bool = False) -> dict[str, Any]:
    report: dict[str, Any] = {"schema_version": 1, "repository": repository,
                              "before": before, "after": after,
                              "checked_at": datetime.now(timezone.utc).isoformat(),
                              "commits": [], "errors": []}
    api = api or GitHub()
    try:
        if not REPOSITORY.fullmatch(repository):
            raise Incomplete("repository must be OWNER/REPO")
        with tempfile.TemporaryDirectory(prefix="merge-integrity-") as temporary:
            git = Git(root.resolve(), repository, Path(temporary) / "objects.git")
            git.ensure_commit(before)
            git.ensure_commit(after)
            if git.run("merge-base", "--is-ancestor", before, after, check=False).returncode:
                raise Incomplete("before is not an ancestor of after, or history is incomplete")
            commits = git.text("rev-list", "--first-parent", "--reverse", f"{before}..{after}").split()
            if not commits:
                raise Incomplete("the push range is empty; no commits examined")
            first_parents = git.text("rev-list", "--parents", "-n", "1", commits[0]).split()[1:]
            if not first_parents or first_parents[0] != before:
                raise Incomplete("before is not on after's first-parent history")
            metadata = api.request(f"repos/{repository}")
            if (not isinstance(metadata, dict)
                    or metadata.get("full_name", "").lower() != repository.lower()
                    or not isinstance(metadata.get("default_branch"), str)
                    or not metadata["default_branch"]):
                raise Incomplete("GitHub repository identity/default branch is unavailable")
            report["base_branch"] = metadata["default_branch"]
            report["commits"] = [verify_commit(git, api, repository, metadata["default_branch"], commit)
                                 for commit in commits]
        if report_issues:
            report["issue_url"] = report_issue(api, report)
    except (Incomplete, KeyError, TypeError, ValueError, OSError) as exc:
        report["errors"].append(str(exc))
    report["counts"] = dict(Counter(row["status"] for row in report["commits"]))
    report["complete"] = not report["errors"] and not report["counts"].get("incomplete")
    report["mismatch"] = bool(report["counts"].get("mismatch"))
    report["exit_code"] = 2 if not report["complete"] else (1 if report["mismatch"] else 0)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repository", required=True)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--before", required=True)
    parser.add_argument("--after", required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--report-issues", action="store_true",
                        help="explicitly authorize deduplicated issue reporting for confirmed mismatches")
    args = parser.parse_args(argv)
    report = verify(args.repository, args.repo_root, args.before, args.after,
                    report_issues=args.report_issues)
    try:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", dir=args.report.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(report, handle, indent=2)
            handle.write("\n")
        temporary.replace(args.report)
    except OSError as exc:
        print(f"Could not save integrity report: {exc}")
        return 2
    print(json.dumps({key: report[key] for key in ("complete", "counts", "errors", "exit_code")}))
    return int(report["exit_code"])


if __name__ == "__main__":
    raise SystemExit(main())
