#!/usr/bin/env python3
"""One way to write a corpus record, so curation diffs show only what changed (#141).

Writing a record back with `yaml.dump(..., width=120)` re-wraps EVERY long string
in the file, not just the field being edited. PR #140 added one organism and one
curation event and produced 47 added lines, 24 of them pure re-wrapping of
untouched `notes:`. Roughly half the diff was noise — semantically lossless, but
it buries the actual change exactly where a reviewer needs to see it, and it
scales badly on a bulk apply.

## Why `width=120` specifically

The corpus was written with PyYAML's DEFAULT width. Measured over 300 random
records, round-tripping load->dump gives:

    default (width 80)   279/300 byte-identical
    width=120              2/300
    width=100              3/300
    width=4096             2/300
    sort_keys=True         0/300

So the corpus convention is simply PyYAML's default, and passing `width=120`
is what causes the churn. Dropping it is the whole fix.

## Why not ruamel

`ruamel.yaml` was added as a dependency for this in #153 and is the usual answer
for round-trip-preserving YAML. It does not help here: no configuration of it
reproduces this corpus. Best measured was width=80 at 7/300 byte-identical, versus
279/300 for plain PyYAML defaults, because ruamel also differs in quoting and
indentation. Two scripts already use it; they are not made worse by this module,
but it is not the route to a clean diff.

## The residual 7%

About 21 of 300 records still differ under the default config. Those are records a
PREVIOUS width=120 run already reflowed — their `notes:` lines are longer than the
corpus convention allows. Rewriting them normalises the damage, which is a
one-time correction rather than new churn.

Usage::

    from record_io import dump_record, write_record

    write_record(path, doc)          # writes only if the text actually changed
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# PyYAML's defaults, stated explicitly so the absence of `width` is visibly
# deliberate rather than an oversight someone will "fix" by adding width=120 back.
DUMP_KWARGS: dict[str, Any] = {
    "default_flow_style": False,
    "sort_keys": False,      # record key order is meaningful; sorting rewrites every file
    "allow_unicode": True,
    # NO width: the corpus convention is PyYAML's default (80). See module docstring.
}


def dump_record(doc: dict[str, Any]) -> str:
    """Serialize a record using the corpus's own formatting convention."""
    return yaml.dump(doc, **DUMP_KWARGS)


def write_record(path: Path, doc: dict[str, Any]) -> bool:
    """Write `doc` to `path`. Returns True if the file changed.

    Skips the write when the serialization is identical to what is already there,
    so a no-op curation pass leaves no mtime churn and no diff at all.

    The comparison is done in BYTES. Reading as text raised UnicodeDecodeError on
    a record that is not valid UTF-8 — and that is not hypothetical: every corpus
    reader here uses `errors="replace"` precisely because some records do not
    decode cleanly, so a curation script would have crashed partway through a
    batch instead of repairing the file (#206). Comparing bytes sidesteps decoding
    entirely and is closer to what the check actually means.

    Creates the parent directory: this writer is also used to create new records
    (`import_jcm_grmd`), not only to edit existing ones.
    """
    text = dump_record(doc)
    data = text.encode("utf-8")
    try:
        if path.read_bytes() == data:
            return False
    except OSError:
        pass
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True
