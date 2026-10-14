"""Compatibility alias for the current read-only artifact checks."""
from final_release_gate import main

if __name__ == "__main__":
    raise SystemExit(main())
