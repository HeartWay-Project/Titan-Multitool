from Config.Util import *
from Config.Config import *
import subprocess
import os

def download_site():
    url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} Enter the site URL -> {reset}").strip()
    
    if not url.startswith('http'):
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} Please enter a valid URL.")
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
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} The site {secondary}{url}{primary} was successfully downloaded in {secondary}{output_directory}{primary}.")
        Continue()
        Reset()
    except subprocess.CalledProcessError as e:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR}{primary} Error downloading the site: {e}")
        Continue()
        Reset()

if __name__ == "__main__":
    download_site()
