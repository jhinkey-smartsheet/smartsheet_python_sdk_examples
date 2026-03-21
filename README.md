# sdk-examples

Python development environment for local work.

## Quick start (PowerShell)

1. Create virtual environment:
   - `py -m venv .venv`
2. Activate it:
   - `.\.venv\Scripts\Activate.ps1`
3. Install dev tools:
   - `python -m pip install --upgrade pip`
   - `python -m pip install -e ".[dev]"`
4. Run checks:
   - `ruff check .`
   - `pytest`

## Layout

- `src/` application code
- `tests/` test suite
