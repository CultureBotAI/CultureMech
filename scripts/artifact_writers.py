#!/usr/bin/env python3
"""Decide whether a script WRITES an artifact or merely mentions it (#209).

`audit_derived_artifacts` attributed artifacts by grepping for the basename, so
its `writer` column listed readers too. `research_media.py` reads
`culturemech_id_registry.tsv` to build a resolution index and writes nothing, yet
appeared among that artifact's writers.

That column is what a curator reads to judge whether an artifact is a current view
or a snapshot, so a reader listed as a writer is misleading in exactly that
judgement — and the list grows with every new consumer.

## Why proximity does not work

The mention is almost always a module constant:

    ID_REGISTRY = REPO_ROOT / "data" / "culturemech_id_registry.tsv"

and the write, if any, happens elsewhere through that name. Looking for a write
call near the mention finds nothing in either case.

## What this does instead

Parses the module and traces the binding:

  1. Collect every name bound to an expression containing the artifact's basename
     — assignments, annotated assignments, and parameter defaults.
  2. Find write operations: `X.write_text(...)`, `X.write_bytes(...)`,
     `X.open("w")`, `open(X, "w")`, `csv`/`json`/`yaml` dumps into a handle opened
     from `X`.
  3. Report `writes` when a write target resolves to one of those names.

Deliberately conservative: an unparseable module, or a path built too indirectly
to follow, yields "unknown" rather than a guess. A wrong "yes" is worse than an
honest "unknown", because the whole point is to stop asserting things that are not
established.

## Known limitation

There is no scope analysis, so a local variable that shadows a module constant and
writes somewhere else produces a false "yes". No script in this repo currently does
that, and ten spot-checked attributions all held up, but it is a real hole —
tracked in #211 rather than left to be discovered.
"""

from __future__ import annotations

import ast
from pathlib import Path

WRITE_METHODS = {"write_text", "write_bytes", "write"}
DUMP_FUNCS = {"dump", "safe_dump", "to_csv", "writerow", "writerows", "writeheader"}


class _Tracer(ast.NodeVisitor):
    """Names bound to the artifact path, and names written through."""

    def __init__(self, basename: str) -> None:
        self.basename = basename
        self.bound: set[str] = set()
        self.written: set[str] = set()
        self._opened_from: dict[str, str] = {}  # handle name -> path name

    # --- binding ---------------------------------------------------------
    def _mentions(self, node: ast.AST) -> bool:
        return any(isinstance(n, ast.Constant) and isinstance(n.value, str)
                   and self.basename in n.value
                   for n in ast.walk(node))

    def visit_Assign(self, node: ast.Assign) -> None:
        if node.value is not None and self._mentions(node.value):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    self.bound.add(tgt.id)
        # handle = X.open(...) / open(X, ...)
        self._track_handle(node)
        # writer = csv.DictWriter(handle, ...) — the write goes through the writer
        # object, so the chain handle -> writer must be followed or every
        # DictWriter-based report looks unwritten.
        self._track_writer_object(node)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None and self._mentions(node.value) and isinstance(node.target, ast.Name):
            self.bound.add(node.target.id)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Bind parameters whose DEFAULT is the artifact path.

        `def collect(out: Path = DEFAULT_OUT)` is common here. Positional defaults
        align to the LAST n parameters, so the pairing is done from the right;
        getting it wrong would bind the wrong name and invent a writer.
        """
        args = node.args
        positional = [a.arg for a in args.args]
        for name, default in zip(positional[len(positional) - len(args.defaults):],
                                 args.defaults, strict=True):
            if self._mentions(default):
                self.bound.add(name)
        for kwarg, default in zip([a.arg for a in args.kwonlyargs],
                                  args.kw_defaults, strict=True):
            if default is not None and self._mentions(default):
                self.bound.add(kwarg)
        self.generic_visit(node)

    # --- writing ---------------------------------------------------------
    def _root_name(self, node: ast.AST) -> str | None:
        """The name a path expression resolves to.

        `args.out` resolves to "out", not "args": the argparse dest is what the
        binding pass records, since that is where the module constant ends up.
        """
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.attr in self.bound:
                return node.attr
        while isinstance(node, ast.Attribute):
            node = node.value
        return node.id if isinstance(node, ast.Name) else None

    def _track_handle(self, node: ast.Assign) -> None:
        call = node.value
        target = node.targets[0] if node.targets else None
        if not isinstance(call, ast.Call) or not isinstance(target, ast.Name):
            return
        path_name = mode = None
        if isinstance(call.func, ast.Attribute) and call.func.attr == "open":
            path_name = self._root_name(call.func.value)
            mode = call.args[0].value if call.args and isinstance(call.args[0], ast.Constant) else "r"
        elif isinstance(call.func, ast.Name) and call.func.id == "open":
            if call.args:
                path_name = self._root_name(call.args[0])
            mode = call.args[1].value if len(call.args) > 1 and isinstance(call.args[1], ast.Constant) else "r"
        for kw in call.keywords:
            if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                mode = kw.value.value
        if path_name and isinstance(mode, str) and ("w" in mode or "a" in mode):
            self._opened_from[target.id] = path_name

    def _track_writer_object(self, node: ast.Assign) -> None:
        call = node.value
        target = node.targets[0] if node.targets else None
        if not isinstance(call, ast.Call) or not isinstance(target, ast.Name):
            return
        for arg in call.args:
            name = self._root_name(arg)
            if name and name in self._opened_from:
                self._opened_from[target.id] = self._opened_from[name]
                return

    def visit_With(self, node: ast.With) -> None:
        for item in node.items:
            call = item.context_expr
            if isinstance(call, ast.Call) and isinstance(item.optional_vars, ast.Name):
                fake = ast.Assign(targets=[item.optional_vars], value=call)
                self._track_handle(fake)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        func = node.func
        # The dominant pattern in this repo: the path is a module constant used as
        # an argparse default, and the write goes through `args.out`. Without this
        # the tracer scored 1/6 on known cases, because the binding flows through
        # argparse rather than through a direct assignment.
        if isinstance(func, ast.Attribute) and func.attr == "add_argument":
            dest = None
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str) \
                        and arg.value.startswith("--"):
                    dest = arg.value.lstrip("-").replace("-", "_")
            default_bound = False
            for kw in node.keywords:
                if kw.arg == "dest" and isinstance(kw.value, ast.Constant):
                    dest = str(kw.value.value)
                if kw.arg == "default":
                    name = self._root_name(kw.value)
                    if (name and name in self.bound) or self._mentions(kw.value):
                        default_bound = True
            if dest and default_bound:
                self.bound.add(dest)
        if isinstance(func, ast.Attribute):
            if func.attr in WRITE_METHODS:
                name = self._root_name(func.value)
                if name:
                    self.written.add(self._opened_from.get(name, name))
            elif func.attr in DUMP_FUNCS:
                for arg in node.args:
                    name = self._root_name(arg)
                    if name:
                        self.written.add(self._opened_from.get(name, name))
                name = self._root_name(func.value)
                if name and name in self._opened_from:
                    self.written.add(self._opened_from[name])
        self.generic_visit(node)


def writes_artifact(source: str, basename: str) -> str:
    """Return "yes", "no" or "unknown" for whether `source` writes `basename`."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return "unknown"
    tracer = _Tracer(basename)
    tracer.visit(tree)
    if not tracer.bound:
        # The path is not bound to a name we can follow. If the module writes
        # nothing at all, "no" is still established; otherwise say so.
        return "no" if not tracer.written else "unknown"
    return "yes" if tracer.bound & tracer.written else "no"


def classify_file(path: Path, basename: str) -> str:
    try:
        return writes_artifact(path.read_text(errors="replace"), basename)
    except OSError:
        return "unknown"
