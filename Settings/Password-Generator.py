import os
from Config.Config import *
from Config.Util import *

Title("Password Generator")

def is_file_valid(file_path):
    return True

def list_files_in_directory(directory):
    try:
        files = [(f, is_file_valid(os.path.join(directory, f))) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except Exception as e:
        print(f"[!] Error listing files in directory {directory}: {e}")
        exit(1)

def select_file(files):
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Available files:{reset}")
    for idx, (file, status) in enumerate(files):
        status_text = "Valid" if status else "Invalid"
        print(f"[{idx + 1}]{primary} -> Status: {secondary}{status_text} {primary}| File: {secondary}{file}")
    while True:
        try:
            choice = int(input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Select file -> {reset}"))
            if 1 <= choice <= len(files):
                return files[choice - 1][0]
            else:
                print(f"Please enter a number between 1 and {len(files)}.")
        except ValueError:
            print("Invalid input, please enter a number.")

def select_mode():
    modes = ["soft", "optimized", "advanced", "deep"]
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Available modes:{reset}")
    for idx, mode in enumerate(modes):
        print(f"{idx + 1}. {mode}")
    while True:
        try:
            choice = int(input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Select mode -> {reset}"))
            if 1 <= choice <= len(modes):
                return modes[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(modes)}.")
        except ValueError:
            print("Invalid input, please enter a number.")

def get_output_filename():
    return input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} The name of the output file (without extension) -> {reset}")

if __name__ == "__main__":
    try:
        from modules_import import check_installation
        check_installation('tqdm')
        check_installation('colorama')
        from all_functions import (read_information_from_file, generate_permutation, generate_maj,
                                   generate_lower, start_symbol_digit, add_char, save_passwords_to_file, 
                                   start_all_upper, start_merge, start_ext_merge, add_double_letter)
        from error_processing import verif_path, keyboard_interruption, check_ext_merge, verif_nb_permutation
        from fmode import mode_config

        import argparse
        from colorama import Fore, Style, init
        from time import time

    except KeyboardInterrupt:
        keyboard_interruption(color=False)
    except Exception as e:
        print(f'[!] Error: {e}.')
        exit(1)

    try:
        init(autoreset=True)

        parser = argparse.ArgumentParser(description=Fore.LIGHTYELLOW_EX + "Description : Powerful tool for generating a personal password list." + Style.RESET_ALL)
        parser.add_argument("-d", "--directory", type=str, default="2-Input/PasswordGen", help="Directory containing information files.")
        
        args = parser.parse_args()

        files = list_files_in_directory(args.directory)
        if not files:
            print(Fore.RED + "[!] No files found in the specified directory.")
            exit(1)

        information_file = select_file(files)
        mode = select_mode()
        output_filename = get_output_filename()
        output_directory = "1-Output/PasswordGen"

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        output_file_path = os.path.join(output_directory, output_filename + ".txt")

        verif_path(os.path.join(args.directory, information_file))
        passwords = read_information_from_file(os.path.join(args.directory, information_file))

        if len(passwords) == 0:
            print(Fore.RED + "[!] Error: You must have at least one piece of information.")
            exit(1)

        combination_length = 2
        nb_symbol = 2
        nb_digit = 2
        first_upper = True
        nb_all_maj = None
        lowercase = True
        character = "1"
        double_letter = True

        combination_length, nb_symbol, nb_digit, first_upper, nb_all_maj, lowercase, character, double_letter = (
            mode_config(passwords, mode, combination_length, nb_symbol, nb_digit, first_upper, nb_all_maj, lowercase, character, double_letter))

        start_time = time()

        combination_length = verif_nb_permutation(combination_length, passwords, True)
        passwords = generate_permutation(passwords, combination_length)
        
        if double_letter:
            passwords = add_double_letter(passwords)

        if lowercase:
            passwords = passwords.union(generate_lower(passwords))

        if nb_all_maj:
            passwords = start_all_upper(passwords, nb_all_maj, lowercase)

        password_initial = passwords
        if nb_symbol:
            password_generated = start_symbol_digit(password_initial, {"a": "@", "e": "€", "s": "$"}, nb_symbol, "[>] Generation with symbols")
            passwords = passwords.union(password_generated)
        
        if nb_digit:
            password_generated = start_symbol_digit(password_initial, {"a": "4", "e": "3", "i": "1", "o": "0"}, nb_digit, "[>] Generation with digits")
            passwords = passwords.union(password_generated)

        if first_upper:
            passwords = passwords.union(generate_maj(passwords))

        if character and character != "0":
            passwords = passwords.union(add_char(passwords, character))

        nb_passwd = len(passwords)
        print(Fore.LIGHTGREEN_EX + f"[>] Wordlist currently being written...\n")
     
        save_passwords_to_file(passwords, output_file_path)
        print(Fore.LIGHTGREEN_EX + "** Wordlist generated successfully **")
        print(Fore.LIGHTYELLOW_EX + f'--> It contains {nb_passwd} passwords.')
        print(Fore.LIGHTYELLOW_EX + "--> Output file :", output_file_path)

        end_time = time()
        print(Fore.LIGHTBLUE_EX + f"\n[+] The program took {round(end_time-start_time,5)} seconds to run.")

        Continue()
        reset()

    except KeyboardInterrupt:
        keyboard_interruption(color=True)
    except Exception as e:
        print(e)
