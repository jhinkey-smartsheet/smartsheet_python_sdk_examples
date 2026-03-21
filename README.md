# Smartsheet Python SDK client examples

These modules demonstrate using the Python SDK client library functions.

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

## Run the example modules

### Prerequisites

1. Activate the virtual environment:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows: `.\.venv\Scripts\Activate.ps1`
2. Install the Smartsheet SDK:
   - `python -m pip install smartsheet-python-sdk`
3. Set your API token:
   - `$env:SMARTSHEET_API_TOKEN = "<your-smartsheet-api-token>"`
4. Set your workspace ID (optional convenience):
   - `$env:WORKSPACE_ID = "<your-workspace-id>"`

### `src/sdk_examples/get_workspace_children.py`

Lists workspace children (folders, sheets, reports, sights, templates) using paginated children APIs.

- `python src/sdk_examples/get_workspace_children.py $env:WORKSPACE_ID`

### `src/sdk_examples/collect_all_workspace_sheet_ids.py`

Traverses nested folders in a workspace and prints all sheet IDs.

- `python src/sdk_examples/collect_all_workspace_sheet_ids.py $env:WORKSPACE_ID`

### `src/sdk_examples/legacy_get_workspace_children.py`

Legacy version that calls `get_workspace` and prints sheet/report/sight/template names.

- `python src/sdk_examples/legacy_get_workspace_children.py $env:WORKSPACE_ID`

### `src/sdk_examples/legacy_collect_all_workspace_sheet_ids.py`

Legacy version that calls `get_workspace(load_all=True)` and prints sheet IDs.

- `python src/sdk_examples/legacy_collect_all_workspace_sheet_ids.py $env:WORKSPACE_ID`
