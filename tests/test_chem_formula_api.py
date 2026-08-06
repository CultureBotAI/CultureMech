"""Guard that chem_formula's public API stays declared in __all__ (#220).

#216 added `hydration_states` — a public helper called from
validate_id_label_correspondence.py — without adding it to `__all__`, so
`from chem_formula import *` silently omitted it and linters read it as
non-public. This pins the invariant so the next public function cannot slip the
same way: every top-level `def` whose name does not start with `_` must appear in
`__all__`.
"""
from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

CHEM_FORMULA = REPO_ROOT / "scripts" / "chem_formula.py"


def _load():
    spec = importlib.util.spec_from_file_location("chem_formula", CHEM_FORMULA)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["chem_formula"] = mod
    spec.loader.exec_module(mod)
    return mod


def _public_functions() -> list[str]:
    tree = ast.parse(CHEM_FORMULA.read_text())
    return [n.name for n in tree.body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
            and not n.name.startswith("_")]


def test_hydration_states_is_exported():
    assert "hydration_states" in _load().__all__


def test_every_public_function_is_in_all():
    exported = set(_load().__all__)
    missing = [f for f in _public_functions() if f not in exported]
    assert not missing, (
        f"public function(s) missing from chem_formula.__all__: {missing}. Add them, "
        "or prefix with _ if they are not part of the API (#220).")


def test_all_only_names_things_that_exist():
    mod = _load()
    absent = [name for name in mod.__all__ if not hasattr(mod, name)]
    assert not absent, f"__all__ lists names that do not exist: {absent}"
