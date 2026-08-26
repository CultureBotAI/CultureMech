#!/usr/bin/env bash
# Thin, byte-governed launcher for the dependency-free Python checker.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 -I "${SCRIPT_DIR}/check_vendored_sync.py" "$@"
