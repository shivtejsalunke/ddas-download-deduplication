# DDAS — Download Deduplication Alert System

DDAS is a cross-platform-oriented prototype for detecting exact duplicate files using streaming SHA-256 hashes and a transactional SQLite index.

## Current scope
- Chunked hashing with checks for file changes during scanning.
- SQLite-backed file index.
- Directory scanner that skips configured partial-download suffixes.
- Duplicate reporting without automatic deletion.
- AES-GCM authenticated encryption for metadata exports.
- CLI, tests, and GitHub Actions.

## Quick start
```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install -e '.[test]'
pytest -q
```

## Important limitations
This prototype matches exact file content; it does not infer semantic duplicates. Cross-device synchronization and notification delivery are not implemented. No “99%+ accuracy” claim is made: exact cryptographic hash equality is the matching criterion. The scanner intentionally does not delete files automatically.
