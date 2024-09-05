from Config.Util import *
from Config.Config import *
from Config.Translates import *
import subprocess
import os

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def download_site():
    url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} {tr('Website_url')} -> {reset}").strip()
    
    if not url.startswith('http'):
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} {tr('ErrorURL')}")
        return
    
    output_directory = "1-Output/Sites/"
    
    os.makedirs(output_directory, exist_ok=True)
    
    wget_command = [
        "wget",
        "--mirror",
        "--convert-links",
        "--adjust-extension",
        "--page-requisites",
        "--no-parent",
        url,
        "-P", output_directory
    ]
    
    try:
        subprocess.run(wget_command, check=True)
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} {tr('1SiteDownload')} {secondary}{url}{primary} {tr('2SiteDownload')} {secondary}{output_directory}{primary}.")
        Continue()
        Reset()
    except subprocess.CalledProcessError as e:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR}{primary} {tr('ErrorDownloadSite')} {e}")
        Continue()
        Reset()

if __name__ == "__main__":
    download_site()
