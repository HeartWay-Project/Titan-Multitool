from Config.Util import *
from Config.Config import *
from Config.Translates import *
from pymediainfo import MediaInfo
import subprocess
import os

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def view_metadata(file_path: str):
    if not os.path.exists(file_path):
        print(f"{ERROR} {tr('File')} {tr('NotExist')}")
        Error(e)
    
    media_info = MediaInfo.parse(file_path)
    print(f"\n {INFO} {tr('Metadatafor')} {reset}{file_path}:\n")

    for track in media_info.tracks:
        if track.track_type == "General":
            print(f"Général:{reset}")
            for key, value in track.to_data().items():
                print(f"{primary}{key}: {reset}{value}")
        elif track.track_type == "Video":
            print("\nVidéo:")
            for key, value in track.to_data().items():
                print(f"{primary}{key}: {reset}{value}")
        elif track.track_type == "Audio":
            print("\nAudio:")
            for key, value in track.to_data().items():
                print(f"{primary}{key}: {reset}{value}")
        elif track.track_type == "Image":
            print("\nImage:")
            for key, value in track.to_data().items():
                print(f"{primary}{key}: {reset}{value}")
        elif track.track_type == "Other":
            print("\nAutres:")
            for key, value in track.to_data().items():
                print(f"{primary}{key}: {reset}{value}")

def modify_metadata(file_path: str, tag: str, value: str):
    if not os.path.exists(file_path):
        print(f"{ERROR} {tr('NotExist')}")
        Error(e)
    
    try:
        command = f'exiftool -{tag}="{value}" "{file_path}"'
        subprocess.run(command, shell=True, check=True)
        print(f"\n{INFO} {tr('Metadata')} {tag} {tr('SuccesUpdate')} {value}.")
    
    except subprocess.CalledProcessError as e:
        print(f"\n {ERROR} {tr('ErrorMetadata')} {e}")

def main():
    while True:
        print(f"\n{secondary}[{primary}1{secondary}] {primary}{tr('ViewMetadata')}")
        print(f"{secondary}[{primary}2{secondary}] {primary}{tr('EditMetadata')}")
        print(f"{secondary}[{primary}3{secondary}] {primary}Quitter")
        choix = input(f"\n{INPUT} {tr('Chose')} -> {reset}")

        if choix == '1':
            file_path = input(f"\n{INPUT} {tr('FilePath')} -> {reset}")
            view_metadata(file_path)

        elif choix == '2':
            file_path = input(f"{INPUT} {tr('FilePath')} -> {reset}")
            tag = input(f"{INPUT} {tr('FiealdModify')} -> {reset}")
            value = input(f"{INPUT} {tr('NewValue')} {tag} -> {reset}")
            modify_metadata(file_path, tag, value)

        elif choix == '3':
            Continue()
            Reset()

        else:
            Error(e)

if __name__ == "__main__":
    main()
