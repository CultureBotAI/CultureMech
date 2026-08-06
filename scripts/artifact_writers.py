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

## Scope

Analysis is per-scope (#211). A name is resolved to the artifact only where it is
actually bound to it: a function that reassigns a module constant's name to a
different path *shadows* the constant, so a write there is not a write to the
artifact. Module bindings flow INTO a function (that is how the `args.out` write
finds `DEFAULT_OUT`), but a local rebinding to a non-artifact expression drops the
name for the rest of that scope. Statements are processed in document order so the
shadow takes effect before the write it guards.
"""

from __future__ import annotations

import ast
from pathlib import Path

WRITE_METHODS = {"write_text", "write_bytes", "write"}
DUMP_FUNCS = {"dump", "safe_dump", "to_csv", "writerow", "writerows", "writeheader"}
_SCOPE_NODES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)


class _Scope:
    """One lexical scope: which names resolve to the artifact here, and whether a
    write to it happens. ``inherited`` seeds the names an enclosing scope bound to
    the artifact; a local rebinding to a non-artifact expression removes one."""

    def __init__(self, basename: str, inherited: set[str]) -> None:
        self.basename = basename
        self.bound: set[str] = set(inherited)
        self.wrote = False
        self.any_bound = False   # did any scope bind a NEW name to the artifact?
        self._opened_from: dict[str, str] = {}   # handle name -> path name
        # child (def/class) nodes with the bindings visible where they are defined
        self.children: list[tuple[ast.AST, set[str]]] = []

    def _mentions(self, node: ast.AST | None) -> bool:
        return node is not None and any(
            isinstance(n, ast.Constant) and isinstance(n.value, str)
            and self.basename in n.value for n in ast.walk(node))

    def _root_name(self, node: ast.AST) -> str | None:
        """The name a path expression resolves to. `args.out` resolves to "out"
        (the argparse dest that carries the module constant), not "args"."""
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.attr in self.bound:
                return node.attr
        while isinstance(node, ast.Attribute):
            node = node.value
        return node.id if isinstance(node, ast.Name) else None

    # --- ordered, scope-respecting walk ----------------------------------
    def run(self, body: list[ast.stmt]) -> tuple[bool, bool]:
        """Process ``body`` in document order (descending into control flow but not
        into nested def/class scopes), then recurse into those child scopes.
        Returns ``(wrote, any_bound)`` aggregated over this scope and its children."""
        for stmt in body:
            self._walk(stmt)
        wrote, any_bound = self.wrote, self.any_bound
        for node, visible in self.children:
            child_wrote, child_bound = _analyze_child(node, self.basename, visible)
            wrote = wrote or child_wrote
            any_bound = any_bound or child_bound
        return wrote, any_bound

    def _walk(self, node: ast.AST) -> None:
        if isinstance(node, _SCOPE_NODES):
            # A nested scope. Its parameter DEFAULTS are evaluated here, so record
            # the def with the bindings currently visible; the child scope handles
            # its own params and body.
            self.children.append((node, set(self.bound)))
            return
        if isinstance(node, ast.Assign):
            self._on_assign(node)
        elif isinstance(node, ast.AnnAssign):
            self._on_annassign(node)
        elif isinstance(node, ast.With):
            for item in node.items:
                if isinstance(item.context_expr, ast.Call) and isinstance(item.optional_vars, ast.Name):
                    self._track_handle(item.optional_vars, item.context_expr)
        elif isinstance(node, ast.Call):
            self._on_call(node)
        for child in ast.iter_child_nodes(node):
            self._walk(child)

    # --- binding ---------------------------------------------------------
    def _on_assign(self, node: ast.Assign) -> None:
        mentions = self._mentions(node.value)
        for tgt in node.targets:
            if isinstance(tgt, ast.Name):
                if mentions:
                    self.bound.add(tgt.id)
                    self.any_bound = True
                elif tgt.id in self.bound:
                    # Rebound to something that is NOT the artifact: shadow it for
                    # the rest of this scope (#211).
                    self.bound.discard(tgt.id)
                    self._opened_from.pop(tgt.id, None)
        if isinstance(node.value, ast.Call) and node.targets and isinstance(node.targets[0], ast.Name):
            self._track_handle(node.targets[0], node.value)
            self._track_writer_object(node.targets[0], node.value)

    def _on_annassign(self, node: ast.AnnAssign) -> None:
        if isinstance(node.target, ast.Name):
            if self._mentions(node.value):
                self.bound.add(node.target.id)
                self.any_bound = True
            elif node.value is not None and node.target.id in self.bound:
                self.bound.discard(node.target.id)

    def _track_handle(self, target: ast.Name, call: ast.Call) -> None:
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

    def _track_writer_object(self, target: ast.Name, call: ast.Call) -> None:
        for arg in call.args:
            name = self._root_name(arg)
            if name and name in self._opened_from:
                self._opened_from[target.id] = self._opened_from[name]
                return

    def _on_call(self, node: ast.Call) -> None:
        func = node.func
        # Dominant pattern here: the path is a module constant used as an argparse
        # default, and the write goes through `args.out`. The default resolves
        # against the bindings visible at this point (module constant inherited).
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
                self.any_bound = True
        if isinstance(func, ast.Attribute):
            if func.attr in WRITE_METHODS:
                name = self._root_name(func.value)
                if name and self._opened_from.get(name, name) in self.bound:
                    self.wrote = True
            elif func.attr in DUMP_FUNCS:
                for arg in node.args:
                    name = self._root_name(arg)
                    if name and self._opened_from.get(name, name) in self.bound:
                        self.wrote = True
                name = self._root_name(func.value)
                if name and name in self._opened_from and self._opened_from[name] in self.bound:
                    self.wrote = True


def _analyze_child(node: ast.AST, basename: str, inherited: set[str]) -> tuple[bool, bool]:
    """Analyze a nested def/class/lambda scope, binding parameter defaults locally.
    Returns ``(wrote, any_bound)``."""
    scope = _Scope(basename, inherited)
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
        args = node.args
        positional = [a.arg for a in args.args]
        for name, default in zip(positional[len(positional) - len(args.defaults):],
                                 args.defaults, strict=True):
            if scope._mentions(default):
                scope.bound.add(name)
                scope.any_bound = True
            elif name in scope.bound:
                scope.bound.discard(name)   # param shadows an inherited name
        for kwarg, default in zip([a.arg for a in args.kwonlyargs], args.kw_defaults, strict=True):
            if default is not None and scope._mentions(default):
                scope.bound.add(kwarg)
                scope.any_bound = True
    # A lambda's body is a single expression, not a statement list.
    body = node.body if isinstance(node.body, list) else [ast.Expr(value=node.body)]
    return scope.run(body)


def writes_artifact(source: str, basename: str) -> str:
    """Return "yes", "no" or "unknown" for whether `source` writes `basename`."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return "unknown"
    wrote, any_bound = _Scope(basename, set()).run(tree.body)
    if wrote:
        return "yes"
    if any_bound:
        # The path was bound to a followable name and no write went through it.
        return "no"
    # The path is not bound to a name we can follow. If the module writes SOMETHING
    # (through a path built too indirectly to trace) say "unknown" rather than "no",
    # since it could be writing the artifact by a route we cannot see.
    return "unknown" if _writes_something(tree) else "no"


def _writes_something(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in (WRITE_METHODS | DUMP_FUNCS):
            return True
    return False


def classify_file(path: Path, basename: str) -> str:
    try:
        return writes_artifact(path.read_text(errors="replace"), basename)
    except OSError:
        return "unknown"
