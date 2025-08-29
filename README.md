# Installation

## Installing Dependencies
    Run `pip install -r requirements.txt`

## Setting up environment

### Finding Canvas Token
    1. Open up Canvas dashboard and go to Profile > Setting
    [Settings] (https://canvas.nus.edu.sg/profile/settings)
    2. Scroll down to **Approved Integrations** and click **New access token**
    3. Create the token, expiry date can be set to your desired date
    4. Copy the token

### configs.py File
    Create file `configs.py` with the content
    ```
    FILE_PATH = "/path/to/your/folder"
    API_URL = "https://canvas.nus.edu.sg/api/v1"
    TOKEN = "12345~yOurtoKenhEreedawsdwasd"
    LOG_FILENAME = "Canvas_File_Sync_Log.txt"
    COURSE_CODES = ["ST3131", "CS2040S", "CS2030S"]
    ```
    Save the file

## Usage
    Run `python3 sync_files.py`
    Info Messages will be displayed
    All log messages will be stored in the `log_file.txt`
