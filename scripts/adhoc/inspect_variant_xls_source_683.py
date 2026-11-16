#!/usr/bin/env python3
"""Inspect source workbook cells for #683 curation (2026-11-16).

Input: one public legacy XLS; output: source SHA256 and nonempty addressed cells.
Run with xlrd==2.0.2. This is source extraction, not scientific validation.
"""

import argparse
import hashlib
import json
from pathlib import Path

import xlrd


def column_name(index):
    name = ""
    while index >= 0:
        index, remainder = divmod(index, 26)
        name = chr(65 + remainder) + name
        index -= 1
    return name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    workbook = xlrd.open_workbook(args.source)
    sheets = []
    for sheet in workbook.sheets():
        cells = {}
        for row in range(sheet.nrows):
            for column in range(sheet.ncols):
                value = sheet.cell_value(row, column)
                if value != "":
                    cells[column_name(column) + str(row + 1)] = value
        sheets.append({"name": sheet.name, "cells": cells})
    print(
        json.dumps(
            {
                "sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
                "xlrd_version": xlrd.__version__,
                "sheets": sheets,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
