import argparse
import os
from smartsheet.models import Folder, Sheet, Report, Sight, Template

import smartsheet

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace_id", type=int, help="Smartsheet workspace ID")
    args = parser.parse_args()

    token = os.getenv("SMARTSHEET_API_TOKEN")
    if not token:
        raise RuntimeError("Missing required environment variable: SMARTSHEET_API_TOKEN")
    workspace_id = args.workspace_id

    smart = smartsheet.Smartsheet(token)
 
    workspace = smart.Workspaces.get_workspace(
        workspace_id
    )
    assert isinstance(workspace, smartsheet.models.workspace.Workspace)

    for child in workspace.folders:
        print(f"Folder: {child.name}")
    for child in workspace.sheets:
        print(f"Sheet: {child.name}")
    for child in workspace.reports or []:
        print(f"Report: {child.name}")
    for child in workspace.sights or []:
        print(f"Sight: {child.name}")
    for child in workspace.templates or []:
        print(f"Template: {child.name}")

if __name__ == "__main__":
    main()
