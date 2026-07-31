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
# Same-path vendored files: identical relative path in every repo.
FILES=(
  scripts/validate_id_label_correspondence.py
  scripts/chem_formula.py
  tests/test_id_label_empty_adapter.py
  tests/test_id_label_unknown_prefix.py
  tests/test_id_label_plausibility.py
)
# Package-namespaced shared files: same bytes, per-repo path
# src/<lowercased-repo>/<suffix>. Listed by the suffix after src/<pkg>/.
MAPPED=(
  schema/mech_shared.yaml
)

# Lowercase a repo name to its package dir (CultureMech -> culturemech).
lc() { printf '%s' "$1" | tr '[:upper:]' '[:lower:]'; }

tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
fail=0
for f in "${FILES[@]}"; do
  hub_url="https://raw.githubusercontent.com/${ORG}/${HUB}/main/${f}"
  if ! curl -fsSL "$hub_url" -o "$tmp/hub"; then
    echo "ERROR: hub ${HUB} missing ${f}"; fail=1; continue
  fi
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
# Package-namespaced files: resolve the per-repo path from the lowercased name.
for suf in "${MAPPED[@]}"; do
  hubf="src/$(lc "$HUB")/${suf}"
  hub_url="https://raw.githubusercontent.com/${ORG}/${HUB}/main/${hubf}"
  if ! curl -fsSL "$hub_url" -o "$tmp/hub"; then
    echo "ERROR: hub ${HUB} missing ${hubf}"; fail=1; continue
  fi
  for r in "${REPOS[@]}"; do
    [ "$r" = "$HUB" ] && continue
    rf="src/$(lc "$r")/${suf}"
    url="https://raw.githubusercontent.com/${ORG}/${r}/main/${rf}"
    if ! curl -fsSL "$url" -o "$tmp/r"; then
      echo "DRIFT: ${r} missing ${rf} (hub has it)"; fail=1; continue
    fi
    if ! cmp -s "$tmp/hub" "$tmp/r"; then
      echo "DRIFT: ${r}:${rf} differs from hub ${HUB} (main)"; fail=1
    fi
  done
done
total=$(( ${#FILES[@]} + ${#MAPPED[@]} ))
[ "$fail" -eq 0 ] && echo "OK: all ${total} vendored files agree across ${#REPOS[@]} repos" || { echo ""; echo "Fleet drift detected — sync the lagging repo(s) from ${HUB} and bump their .vendored_canon_ref."; exit 1; }
