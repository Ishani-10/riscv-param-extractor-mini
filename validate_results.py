#!/usr/bin/env python3
"""Basic validator for the RISC-V extraction YAML.

Usage:
  python validate_results.py source.txt riscv_challenge_results.yaml
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency. Install it with: python -m pip install pyyaml")

REQUIRED = {"name", "description", "type", "constraints", "source", "confidence"}
VALID_CONFIDENCE = {"high", "medium", "low"}


def fail(message):
    print(f"FAIL: {message}")
    return False


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python validate_results.py source.txt results.yaml")

    source_path, yaml_path = map(Path, sys.argv[1:])
    source = source_path.read_text(encoding="utf-8")
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    ok = True

    if not isinstance(data, dict) or not isinstance(data.get("parameters"), list):
        raise SystemExit("FAIL: top-level 'parameters' list is missing")

    names = set()
    for number, item in enumerate(data["parameters"], start=1):
        prefix = f"parameters[{number}]"
        if not isinstance(item, dict):
            ok = fail(f"{prefix} is not a mapping") and ok
            continue
        missing = REQUIRED - set(item)
        if missing:
            ok = fail(f"{prefix} missing fields: {sorted(missing)}") and ok
        name = item.get("name")
        if not isinstance(name, str) or not name.strip():
            ok = fail(f"{prefix} has an invalid name") and ok
        elif name in names:
            ok = fail(f"duplicate parameter name: {name}") and ok
        else:
            names.add(name)
        if not isinstance(item.get("constraints"), list):
            ok = fail(f"{prefix}.constraints must be a list") and ok
        if item.get("confidence") not in VALID_CONFIDENCE:
            ok = fail(f"{prefix}.confidence must be high, medium, or low") and ok
        evidence = item.get("source", {}).get("evidence") if isinstance(item.get("source"), dict) else None
        if not isinstance(evidence, str) or not evidence:
            ok = fail(f"{prefix} has no source evidence") and ok
        elif evidence not in source:
            ok = fail(f"{prefix} evidence was not found in source.txt: {evidence!r}") and ok

    if ok:
        print(f"PASS: validated {len(data['parameters'])} parameters")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
