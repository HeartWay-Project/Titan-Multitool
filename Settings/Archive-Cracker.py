from Config.Util import *
from Config.Config import *
from Config.Translates import *
import os
import subprocess

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def list_wordlists(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def main():
    if not os.path.exists(r"C:\Program Files\7-Zip"):
        print(f"{tr('7ZipNotHere')}")
        Continue()
        Reset()
    
    archive = input(f"\n{BEFORE + current_time_hour() + AFTER}{INPUT}{primary}{tr('7Path')} -> {reset}")
    if not os.path.exists(archive):
        print(f"{BEFORE + current_time_hour() + AFTER} {tr('ArchiveNotFound')}")
        Continue()
        Reset()
    
    wordlist_dir = r"2-Input/Passwords/"

    wordlists = list_wordlists(wordlist_dir)

    if not wordlists:
        print(f"{BEFORE + current_time_hour() + AFTER} {tr('WordlistFound')} {wordlist_dir}")
        Continue()
        Reset()

    print(f"\n{BEFORE + current_time_hour() + AFTER}{WAIT}{primary}Wordlists :\n")
    for index, filename in enumerate(wordlists, start=1):
        print(f"{primary}[{secondary}{index}{primary}] {filename}")

    choice = input(f"\n{INPUT}{primary}{tr('NumWordlist')} -> {reset}")

    try:
        choice = int(choice)
        if 1 <= choice <= len(wordlists):
            wordlist = os.path.join(wordlist_dir, wordlists[choice - 1])
        else:
            ErrorChoice()
    except ValueError:
        print(f"Entrée invalide.")
        Continue()
        Reset()

    if not os.path.exists(wordlist):
        print(f"{BEFORE + current_time_hour() + AFTER} {tr('WordlistNotFound')}")
        Continue()
        Reset()

    print(f"\n{BEFORE + current_time_hour() + AFTER}{WAIT}{primary}Cracking...\n")

    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            if attempt_crack(archive, password):
                print(f"\n{BEFORE + current_time_hour() + AFTER} {tr('PasswdFound')}: {valid}{password}")
                Continue()
                Reset()
    
    print(f"Shitty wordlist dumbass")
    Continue()
    Reset()

def attempt_crack(archive, password):
    result = subprocess.run(
        [r"C:\Program Files\7-Zip\7z.exe", 'x', f'-p{password}', archive, '-o"cracked"', '-y'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    print(f"{BEFORE + current_time_hour() + AFTER}{WAIT}{tr('ATTEMPT')} : {password}")
    return result.returncode == 0

if __name__ == "__main__":
    main()
