# CultureMech - Main Build File
# Imports project-specific recipes from project.justfile

import 'project.justfile'

# Default recipe: show help
default:
    @just --list --unsorted

# Quick validation shortcut
v file:
    just validate {{file}}

# Quick schema validation shortcut
vs file:
    just validate-schema {{file}}
