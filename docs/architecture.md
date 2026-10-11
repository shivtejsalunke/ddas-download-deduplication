# Architecture and limitations

1. Traverse a selected directory and skip known partial-download suffixes.
2. Hash file contents incrementally with SHA-256.
3. Compare file size and modification time before/after hashing to catch common concurrent-write races.
4. Persist absolute paths, digest, size and mtime in a SQLite index.
5. Report groups sharing an exact digest; never auto-delete files.

This prototype does not implement cross-device synchronization, notification delivery, semantic duplicate detection or a 99% accuracy metric. Results are a point-in-time inventory.
