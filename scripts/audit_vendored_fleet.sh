#!/usr/bin/env bash
# Nightly fleet audit for vendored byte-identical files.
#
# The per-repo drift check (scripts/check_vendored_sync.sh in each spoke) verifies
# a spoke against the canonical hub, but NOTHING checks the hub itself, nor a
# spoke whose pinned ref lags the hub. This audit closes that gap: it fetches
# each vendored file from ALL FOUR repos' main branches and compares them,
# failing if any repo disagrees with the hub. Dependency-free (bash + curl).
set -euo pipefail

ORG="CultureBotAI"
HUB="CultureMech"
REPOS=(CultureMech MediaIngredientMech CommunityMech TraitMech)
FILES=(
  scripts/validate_id_label_correspondence.py
  scripts/chem_formula.py
  tests/test_id_label_empty_adapter.py
  tests/test_id_label_unknown_prefix.py
  tests/test_id_label_plausibility.py
)

tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
fail=0
for f in "${FILES[@]}"; do
  hub_url="https://raw.githubusercontent.com/${ORG}/${HUB}/main/${f}"
  if ! curl -fsSL "$hub_url" -o "$tmp/hub"; then
    echo "ERROR: hub ${HUB} missing ${f}"; fail=1; continue
  fi
  hubsum="$(shasum -a 256 "$tmp/hub" 2>/dev/null | cut -d' ' -f1 || sha256sum "$tmp/hub" | cut -d' ' -f1)"
  for r in "${REPOS[@]}"; do
    [ "$r" = "$HUB" ] && continue
    url="https://raw.githubusercontent.com/${ORG}/${r}/main/${f}"
    if ! curl -fsSL "$url" -o "$tmp/r"; then
      echo "DRIFT: ${r} missing ${f} (hub has it)"; fail=1; continue
    fi
    if ! cmp -s "$tmp/hub" "$tmp/r"; then
      echo "DRIFT: ${r}:${f} differs from hub ${HUB} (main)"; fail=1
    fi
  done
done
[ "$fail" -eq 0 ] && echo "OK: all ${#FILES[@]} vendored files agree across ${#REPOS[@]} repos" || { echo ""; echo "Fleet drift detected — sync the lagging repo(s) from ${HUB} and bump their .vendored_canon_ref."; exit 1; }
