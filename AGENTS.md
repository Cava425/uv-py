# Repository guidance

- This is a Python 3.12 learning/practice repository managed with `uv`; use `uv run python <path>.py` to run standalone examples. There is no configured test suite, linter, or formatter.
- Topic directories are standalone materials, not importable packages. Preserve the pairing between topic documentation and runnable examples (notably `python_datatypes/README.md` and `examples.py`); algorithm solutions may include executable assertions for self-checking.
- Study notes and README content are primarily Chinese. Keep additions consistent with each topic's existing format and language.
- Add project dependencies with `uv add <package>` so `pyproject.toml` and `uv.lock` stay in sync.
