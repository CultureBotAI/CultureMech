"""
CultureMech CLI entry point.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "render":
        from culturemech.render import main
        sys.argv.pop(1)  # Remove 'render' from args
        main()
    else:
        print("CultureMech - Microbial Growth Media Knowledge Base")
        print("\nAvailable commands:")
        print("  python -m culturemech render - Generate HTML pages")
        print("\nFor more options, use the justfile commands:")
        print("  just --list")
