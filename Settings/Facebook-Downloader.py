from Config.Util import *
from Config.Config import *
import yt_dlp
import os

def télécharger_vidéo_facebook(url):
    try:
        download_dir = '1-Output/VideoDownload/Facebook/'
        os.makedirs(download_dir, exist_ok=True)

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO} {primary}Téléchargement terminé !")
        Continue()
        Reset()
    except Exception as e:
        Error(e)

if __name__ == "__main__":
    url = input(f"\n{primary}{INPUT} URL de la vidéo Facebook -> {reset}")
    télécharger_vidéo_facebook(url)