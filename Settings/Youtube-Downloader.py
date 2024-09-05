from Config.Util import *
from Config.Config import *
from Config.Translates import *
import yt_dlp
import os

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def télécharger_vidéo(url):
    try:
        download_dir = '1-Output/VideoDownload/Youtube/'
        os.makedirs(download_dir, exist_ok=True)

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO} {primary}{tr('DownloadDone')}")
        Continue()
        Reset()
    except Exception as e:
        Error(e)

if __name__ == "__main__":
    url = input(f"\n{primary}{INPUT} {tr('URLVideo')} -> {reset}")
    télécharger_vidéo(url)

