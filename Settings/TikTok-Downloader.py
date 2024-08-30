from Config.Util import *
from Config.Config import *
import os
import subprocess

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Répertoire créé : {path}")
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
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO}{primary}Download done in file {save_path}")
        Continue()
        Reset()
    except subprocess.CalledProcessError as e:
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO}{primary}Error to download the video{e.stderr.decode('utf-8')}")
        Continue()
        Reset()

if __name__ == "__main__":
    tiktok_url = input(f"\n{primary}{INPUT} URL of the video -> {reset}")

    base_directory = '/1-Output/VideoDownload/TikTok/'
    create_directory(base_directory)
    
    filename_without_extension = input(f"\n{primary}{INPUT} File name -> {reset}")
    filename = f"{filename_without_extension}.mp4"
    save_path = os.path.join(base_directory, filename)
    
    download_tiktok_video(tiktok_url, save_path)
