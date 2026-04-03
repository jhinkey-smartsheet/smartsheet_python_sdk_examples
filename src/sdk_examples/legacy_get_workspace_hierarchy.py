import argparse
import os
from smartsheet.models import Folder, Sheet, Report, Sight, Template

import smartsheet


def print_folder_hierarchy(folder: Folder):
    # Recursively call the function to print the folder hierarchy
    def print_hierarchy(folder: Folder, level=1):
        indent = "  " * level
        print(f"{indent}- {folder.name} (ID: {folder.id})")
        
        for child in folder.folders:
            print_hierarchy(child, level + 1)

    print_hierarchy(folder)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace_id", type=int, help="Smartsheet workspace ID")
    args = parser.parse_args()

    token = os.getenv("SMARTSHEET_API_TOKEN")
    if not token:
        raise RuntimeError("Missing required environment variable: SMARTSHEET_API_TOKEN")
    workspace_id = args.workspace_id

    smart = smartsheet.Smartsheet(token)
 
    # Call Workspaces.get_workspace(...) to get the workspace's folder hierarchy
    workspace = smart.Workspaces.get_workspace(
        workspace_id, 
        load_all=True
    )
    assert isinstance(workspace, smartsheet.models.workspace.Workspace)

    for folder in workspace.folders:
        print_folder_hierarchy(folder)

if __name__ == "__main__":
    main()
