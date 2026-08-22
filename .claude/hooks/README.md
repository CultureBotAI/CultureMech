# Optional orchestration hooks

The hooks have two explicit modes:

- If `KG_MICROBE_ORCHESTRATION_ROOT` is unset, coordination is intentionally
  disabled and the hook exits successfully with a diagnostic.
- If it is set, `$KG_MICROBE_ORCHESTRATION_ROOT/scripts/check_lock.py` and the
  `status/` directory are required. A locked repository or checker failure
  blocks the pre-action; missing/broken infrastructure never fails open.

Example:

```bash
export KG_MICROBE_ORCHESTRATION_ROOT=/path/to/kg-microbe-orchestration
```

Do not commit a developer-specific value. Run
`uv run pytest tests/test_claude_hooks.py` after changing hook behavior.
