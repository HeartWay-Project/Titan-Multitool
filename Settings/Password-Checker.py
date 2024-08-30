import re
import os
import sys
from Config.Util import *
from Config.Config import *

# Charger les mots de passe communs à partir d'un fichier
def load_common_passwords(file_path):
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier {file_path} n'existe pas.")
        sys.exit(1)
    with open(file_path, 'r') as file:
        common_passwords = file.read().splitlines()
    return common_passwords

# Charger les mots du dictionnaire à partir d'un fichier
def load_dictionary(file_path):
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier {file_path} n'existe pas.")
        sys.exit(1)
    with open(file_path, 'r') as file:
        dictionary_words = file.read().splitlines()
    return dictionary_words

# Vérifier la présence de motifs répétitifs ou séquentiels
def has_repetitive_or_sequential_patterns(password):
    return re.search(r'(.)\1{2,}', password) or re.search(r'012|123|234|345|456|567|678|789|890', password)

# Vérifier la présence de séquences de caractères
def has_sequential_characters(password):
    sequences = [
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm',
        'QWERTYUIOP',
        'ASDFGHJKL',
        'ZXCVBNM'
    ]
    for seq in sequences:
        if any(seq[i:i+3] in password for i in range(len(seq)-2)):
            return True
    return False

# Évaluer la force du mot de passe
def evaluate_password_strength(password, common_passwords, dictionary_words):
    # Initialize base scores
    length_score = len(password) * 1.5
    upper_case_score = len(re.findall(r'[A-Z]', password)) * 1.5
    lower_case_score = len(re.findall(r'[a-z]', password)) * 1
    digit_score = len(re.findall(r'\d', password)) * 1.5
    special_char_score = len(re.findall(r'[\W_]', password)) * 2
    
    # Total score
    total_score = length_score + upper_case_score + lower_case_score + digit_score + special_char_score
    
    # Penalty for common passwords
    if password in common_passwords:
        total_score -= 40  # Increase penalty for common passwords

    # Penalty for dictionary words
    if password.lower() in dictionary_words:
        total_score -= 25  # Increase penalty for dictionary words

    # Penalty for repetitive or sequential patterns
    if has_repetitive_or_sequential_patterns(password):
        total_score -= 20  # Increase penalty for repetitive patterns

    # Penalty for sequential characters
    if has_sequential_characters(password):
        total_score -= 20  # Penalty for sequential characters

    # Penalty for short passwords
    if len(password) < 8:
        total_score -= 20  # Penalty for passwords shorter than 8 characters

    # Scale score to a maximum of 100
    max_score = 100
    score_percentage = min(max(total_score, 0), max_score)
    
    if score_percentage < 20:
        strength = 'Faible'
        color = 'Rouge'
    elif score_percentage < 50:
        strength = 'Moyen'
        color = 'Orange'
    else:
        strength = 'Fort'
        color = 'Vert'
    
    return strength, color, score_percentage

def estimate_brute_force_time(password):
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[\W_]', password):
        charset_size += 32
    
    num_combinations = charset_size ** len(password)
    checks_per_second = 1_000_000_000
    time_to_crack_seconds = num_combinations / checks_per_second
    
    time_to_crack = {
        'seconds': time_to_crack_seconds,
        'minutes': time_to_crack_seconds / 60,
        'hours': time_to_crack_seconds / 3600,
        'days': time_to_crack_seconds / 86400,
        'years': time_to_crack_seconds / 31_536_000
    }
    
    return time_to_crack

def display_progress_bar(percentage):
    bar_length = 50
    filled_length = int(bar_length * percentage // 100)
    
    if percentage < 20:
        color = '\033[91m'
    elif percentage < 50:
        color = '\033[93m' 
    else:
        color = '\033[92m'  
    
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    return f'{color}|{bar}| {percentage:.0f}%\033[0m'

def main():
    # Chemins par défaut des fichiers txt
    default_common_passwords_file = '2-Input/Passwords/common_passwords.txt'
    default_dictionary_file = '2-Input/Passwords/dictionary.txt'
    
    # Utiliser des chemins spécifiés par ligne de commande si présents
    common_passwords_file = sys.argv[1] if len(sys.argv) > 1 else default_common_passwords_file
    dictionary_file = sys.argv[2] if len(sys.argv) > 2 else default_dictionary_file
    
    # Charger les mots de passe communs et les mots du dictionnaire
    common_passwords = load_common_passwords(common_passwords_file)
    dictionary_words = load_dictionary(dictionary_file)
    
    password = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Password to evaluate -> {reset}")
    
    strength, color, score_percentage = evaluate_password_strength(password, common_passwords, dictionary_words)
    time_to_crack = estimate_brute_force_time(password)
    
    print(f"\nPassword Strength: {strength}")
    print(display_progress_bar(score_percentage))
    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} Estimated time to crack the password: {reset}\n")
    for unit, time in time_to_crack.items():
        print(f"{BEFORE + current_time_hour() + AFTER}{primary}{unit.capitalize()}: {secondary}{time:.2e}\n")

    Continue()
    Reset()
    
if __name__ == "__main__":
    main()
