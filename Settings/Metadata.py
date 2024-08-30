from Config.Util import *
from Config.Config import *
from pymediainfo import MediaInfo
import subprocess
import os

def view_metadata(file_path: str):
    if not os.path.exists(file_path):
        print(f"{ERROR} Le fichier n'existe pas.")
        Error(e)
    
    media_info = MediaInfo.parse(file_path)
    print(f"\n {INFO} Métadonnées pour {reset}{file_path}:\n")

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
        print(f"{ERROR} Le fichier n'existe pas.")
        Error(e)
    
    try:
        command = f'exiftool -{tag}="{value}" "{file_path}"'
        subprocess.run(command, shell=True, check=True)
        print(f"\n{INFO} Métadonnée {tag} mise à jour avec succès à {value}.")
    
    except subprocess.CalledProcessError as e:
        print(f"\n {ERROR} Erreur lors de la mise à jour des métadonnées : {e}")

def main():
    while True:
        print(f"\n{secondary}[{primary}1{secondary}] {primary}Voir les métadonnées d'un fichier")
        print(f"{secondary}[{primary}2{secondary}] {primary}Modifier les métadonnées d'un fichier")
        print(f"{secondary}[{primary}3{secondary}] {primary}Quitter")
        choix = input(f"\n{INPUT} Choose an option -> {reset}")

        if choix == '1':
            file_path = input(f"\n{INPUT} Chemin du fichier -> {reset}")
            view_metadata(file_path)

        elif choix == '2':
            file_path = input(f"{INPUT} Chemin du fichier -> {reset}")
            tag = input(f"{INPUT} Nom du champ à modifier -> {reset}")
            value = input(f"{INPUT} Nouvelle valeur pour {tag} -> {reset}")
            modify_metadata(file_path, tag, value)

        elif choix == '3':
            Continue()
            Reset()

        else:
            Error(e)

if __name__ == "__main__":
    main()
