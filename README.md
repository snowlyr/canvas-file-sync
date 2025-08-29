# Installation

## Installing Dependencies
    - Run `pip install -r requirements.txt`

## Setting up environment

### Finding Canvas Token
    - Open up Canvas dashboard and go to Profile > Setting
    - [Settings] (https://canvas.nus.edu.sg/profile/settings)
    - Scroll down to **Approved Integrations** and click **New access token**
    - Create the token, expiry date can be set to your desired date
    - Copy the token

### configs.py File
    - Create file `configs.py` with the content
    ```
    FILE_PATH = "/path/to/your/folder"
    API_URL = "https://canvas.nus.edu.sg/api/v1"
    TOKEN = "12345~yOurtoKenhEreedawsdwasd"
    LOG_FILENAME = "Canvas_File_Sync_Log.txt"
    COURSE_CODES = "ST3131,CS2040S,CS2030S,CS2100,DSA2102"
    ```
    - Save the file

## Usage
    - Run `python3 sync_files.py`
    - Info Messages will be displayed
    - All log messages will be stored in the `log_file.txt`
