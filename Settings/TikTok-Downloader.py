from Config.Util import *
from Config.Config import *
from Config.Translates import *
import os
import subprocess

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{tr('DirectoryCreated')} {path}")
    else:
        print(f"\n")

def download_tiktok_video(tiktok_url, save_path):
    try:
        result = subprocess.run(
            ['yt-dlp', '-o', save_path, tiktok_url],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO}{primary}{tr('DownloadDoneFile')} {save_path}")
        Continue()
        Reset()
    except subprocess.CalledProcessError as e:
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO}{primary}{tr('ErrorDownloadVideo')}{e.stderr.decode('utf-8')}")
        Continue()
        Reset()

if __name__ == "__main__":
    tiktok_url = input(f"\n{primary}{INPUT} {tr('URLVideo')} -> {reset}")

    base_directory = '/1-Output/VideoDownload/TikTok/'
    create_directory(base_directory)
    
    filename_without_extension = input(f"\n{primary}{INPUT} {tr('FileName')} -> {reset}")
    filename = f"{filename_without_extension}.mp4"
    save_path = os.path.join(base_directory, filename)
    
    download_tiktok_video(tiktok_url, save_path)
