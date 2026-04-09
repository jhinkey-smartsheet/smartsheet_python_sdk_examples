import argparse
import os
from smartsheet.models import Folder, Sheet, Report, Sight, Template

import smartsheet

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_id", type=int, help="Smartsheet folder ID")
    args = parser.parse_args()

    token = os.getenv("SMARTSHEET_API_TOKEN")
    if not token:
        raise RuntimeError("Missing required environment variable: SMARTSHEET_API_TOKEN")
    folder_id = args.folder_id

    smart = smartsheet.Smartsheet(token)

    folder = None
    folders = []
    sheets = []
    reports = []
    sights = []
    templates = []

    folder_metadata = smart.Folders.get_folder_metadata(folder_id)
    assert isinstance(folder_metadata, smartsheet.models.folder.Folder)

    last_key = None
    while True:
        response = smart.Folders.get_folder_children(
            folder_id, last_key=last_key
        )
        assert isinstance(
            response,
            smartsheet.models.paginated_children_result.PaginatedChildrenResult
        )

        for child in response.data:
            if type(child) is Folder:
                folders.append(child)
            elif type(child) is Sheet:
                sheets.append(child)
            elif type(child) is Report:
                reports.append(child)
            elif type(child) is Sight:
                sights.append(child)
            elif type(child) is Template:
                templates.append(child)

        last_key = getattr(response, "last_key", None)
        if not last_key:
            break

    print(f"parent folder: {folder_metadata}")
    print(f"folders: {folders}")
    print(f"sheets: {sheets}")
    print(f"reports: {reports}")
    print(f"sights: {sights}")
    print(f"templates: {templates}")

if __name__ == "__main__":
    main()
