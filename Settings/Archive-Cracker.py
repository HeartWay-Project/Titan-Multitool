from Config.Util import *
from Config.Config import *
import os
import subprocess

def list_wordlists(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def main():
    if not os.path.exists(r"C:\Program Files\7-Zip"):
        print("7-Zip not installed!")
        Continue()
        Reset()
    
    archive = input(f"\n{BEFORE + current_time_hour() + AFTER}{INPUT}{primary}Archive Path -> {reset}")
    if not os.path.exists(archive):
        print("{BEFORE + current_time_hour() + AFTER} Archive not found!")
        Continue()
        Reset()
    
    wordlist_dir = r"2-Input/Passwords/"

    wordlists = list_wordlists(wordlist_dir)

    if not wordlists:
        print(f"{BEFORE + current_time_hour() + AFTER} No wordlists found in {wordlist_dir}")
        Continue()
        Reset()

    print(f"\n{BEFORE + current_time_hour() + AFTER}{WAIT}{primary}Wordlists :\n")
    for index, filename in enumerate(wordlists, start=1):
        print(f"{primary}[{secondary}{index}{primary}] {filename}")

    choice = input(f"\n{INPUT}{primary}Entrez le numéro de la wordlist -> {reset}")

    try:
        choice = int(choice)
        if 1 <= choice <= len(wordlists):
            wordlist = os.path.join(wordlist_dir, wordlists[choice - 1])
        else:
            print("Choix invalide.")
            Continue()
            Reset()
    except ValueError:
        print("Entrée invalide.")
        Continue()
        Reset()

    if not os.path.exists(wordlist):
        print("{BEFORE + current_time_hour() + AFTER} Wordlist not found!")
        Continue()
        Reset()

    print(f"\n{BEFORE + current_time_hour() + AFTER}{WAIT}{primary}Cracking...\n")

    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            if attempt_crack(archive, password):
                print(f"\n{BEFORE + current_time_hour() + AFTER} Success! Password Found: {valid}{password}")
                Continue()
                Reset()
    
    print("Shitty wordlist dumbass")
    input("Press Enter to exit...")

def attempt_crack(archive, password):
    result = subprocess.run(
        [r"C:\Program Files\7-Zip\7z.exe", 'x', f'-p{password}', archive, '-o"cracked"', '-y'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    print(f"{BEFORE + current_time_hour() + AFTER}{WAIT}ATTEMPT : {password}")
    return result.returncode == 0

if __name__ == "__main__":
    main()
