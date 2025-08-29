import datetime

class Logger:
    def __init__(self, folder_path:str):
        self.file_path = folder_path 
        self.buffer = ""

    def info(self, info_string:str, alert=False):
        tmp = f"[INFO@{str(datetime.datetime.now())[:-7]}] {info_string}"
        self.buffer += tmp+"\n"
        if alert: print(tmp)

    def err(self, err_string:str, alert=True):
        tmp = f"[ERROR@{str(datetime.datetime.now())[:-7]}] {err_string}"
        self.buffer += tmp+"\n"
        if alert: print(tmp)

    def write(self):
        with open(self.file_path, "a") as out:
            out.write(self.buffer)
