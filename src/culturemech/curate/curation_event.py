"""Standard helper for appending CurationEvent entries to a recipe.

Every script that mutates a media/solution YAML record should call
``record_curation_event`` to leave an audit trail. Centralizing here means:

* timestamps are ISO-8601 with UTC tz, consistently;
* the ``curation_history`` slot is created on demand;
* re-runs of idempotent migration scripts can short-circuit when the most
  recent event already matches (``skip_if_recent`` flag);
* the schema's ``CurationEvent`` field names (timestamp / curator / action /
  notes / source / changes) are honored, so future schema diffs only need
  to touch one file.

Drop-in usage::

    from culturemech.curate.curation_event import record_curation_event

    record_curation_event(
        recipe,
        curator="my_script.py",
        action="ENRICHED_CHEBI",
        notes="organisms=5 hits=4 misses=1",
    )
"""

from __future__ import annotations

import datetime
from typing import Any

__all__ = ["record_curation_event", "now_iso"]


def now_iso() -> str:
    """Current UTC timestamp as an ISO-8601 string."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def record_curation_event(
    recipe: dict[str, Any],
    *,
    curator: str,
    action: str,
    notes: str | None = None,
    source: str | None = None,
    changes: str | None = None,
    timestamp: str | None = None,
    skip_if_recent: bool = False,
) -> dict[str, Any]:
    """Append a CurationEvent to ``recipe['curation_history']``.

    Args:
        recipe: The recipe (or solution) dict being mutated. Mutated in place.
        curator: Script / human identifier (e.g. ``"migrate_legacy_fields.py"``
            or ``"jane.smith"``). Required because the schema requires it.
        action: Short action label (e.g. ``"ADDED_GROWTH_EVIDENCE"``,
            ``"MIGRATED_LEGACY_FIELDS"``). Required.
        notes: Optional free-text details.
        source: Optional source attribution (e.g. a sibling recipe ID or
            external dataset name). Maps to ``CurationEvent.source``.
        changes: Optional structured summary of what changed
            (e.g. ``"Set category to 'bacterial' (was MISSING)"``).
            Maps to ``CurationEvent.changes``.
        timestamp: Override the ISO-8601 timestamp (used for tests /
            deterministic snapshots). Defaults to current UTC.
        skip_if_recent: When True, do nothing if the most recent
            curation_history entry already matches the same
            ``(curator, action)`` pair. Useful when refactoring a script
            into the helper without producing duplicate trail entries
            during a re-run.

    Returns:
        The appended event dict (or the most recent matching one if
        ``skip_if_recent`` short-circuited).
    """
    history = recipe.setdefault("curation_history", [])

    if skip_if_recent and history:
        last = history[-1]
        if (
            isinstance(last, dict)
            and last.get("curator") == curator
            and last.get("action") == action
        ):
            return last

    event: dict[str, Any] = {
        "timestamp": timestamp or now_iso(),
        "curator": curator,
        "action": action,
    }
    if notes is not None:
        event["notes"] = notes
    if source is not None:
        event["source"] = source
    if changes is not None:
        event["changes"] = changes

    history.append(event)
    return event
