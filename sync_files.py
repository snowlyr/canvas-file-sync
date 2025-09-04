import os
import requests
import json
from logger import Logger
from configs import *

# Your details
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Folder to sync files into
os.makedirs(FILE_PATH, exist_ok=True)
logger = Logger(os.path.join(FILE_PATH,LOG_FILENAME))
logger.info(f"========== Start syncing files for {COURSE_CODES} ==========", alert=True)
logger.info(f"========== At file dir: {FILE_PATH} ==========", alert=True)
def fetch_all(url) -> dict:
    """Fetch all paginated results from Canvas API."""
    results = []
    while url:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        results.extend(resp.json())
        url = resp.links["next"]["url"] if "next" in resp.links else None
    return results

def filter_course_id(json_res : dict, courses : list) -> dict:
    res = {}
    for hm in json_res:
        course_code = hm.get("course_code",None)
        if course_code and course_code in courses:
            res[course_code] = hm.get("id")
    return res

json_resp = fetch_all(f"{API_URL}/courses?per_page=100")
course_ids = filter_course_id(json_resp, COURSE_CODES)

def sync_files(course_code : str, course_id : str) -> None:
    logger.info(f"Syncing course: {course_code}...", alert=True)
    # 1. Fetch all folders
    folders = fetch_all(f"{API_URL}/courses/{course_id}/folders?per_page=100")
    folder_map = {f["id"]: f for f in folders}
    # 2. Fetch all files
    files = fetch_all(f"{API_URL}/courses/{course_id}/files?per_page=100")
    # 3. Download each file into its folder
    dest_folder = os.path.join(FILE_PATH, course_code)

    for f in files:
        # Get folder info
        folder_id = f["folder_id"]
        folder_info = folder_map.get(folder_id, None)
        # Resolve folder path
        if folder_info:
            canvas_dir = folder_info["full_name"][13:]
            canvas_file_path = os.path.join(canvas_dir, f["filename"])
            folder_path = os.path.join(dest_folder, canvas_dir)
        else:
            canvas_file_path = f["filename"]
            folder_path = dest_folder  # fallback if no folder info
        canvas_file_path = os.path.join(course_code,canvas_file_path)

        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f["filename"])

        # Skip if already synced
        if os.path.exists(file_path) and os.path.getsize(file_path) == f["size"]:
            logger.info(f"Skipping: {canvas_file_path}, already synced.")
            continue

        if f["url"]: 
            logger.info(f"Downloading: {canvas_file_path}...", alert=True)
            file_resp = requests.get(f["url"], headers=HEADERS)
            file_resp.raise_for_status()
            with open(file_path, "wb") as out:
                out.write(file_resp.content)
        else:
            logger.err(f"Skipping: {canvas_file_path}, missing url.")
    logger.info(f"========== Sync Completed for {course_code}! ==========",alert=True)

for key, val in course_ids.items():
    sync_files(key, val)

logger.write()
