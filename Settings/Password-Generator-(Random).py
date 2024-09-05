from Config.Config import *
from Config.Util import *
from Config.Translates import *
import random
import string
import keyboard
import os

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def load_wordlists(filenames):
    word_list = []
    for filename in filenames:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            word_list.extend(words)
    return word_list

def generate_word_password(word_list, min_length=6, max_length=16):
    length = random.randint(min_length, max_length)  
    return ''.join(random.choice(word_list) for _ in range(length))

def generate_numeric_password(min_length=6, max_length=16):
    length = random.randint(min_length, max_length) 
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_complex_password(min_length=6, max_length=16):
    length = random.randint(min_length, max_length)
    
    if length < 4:
        length = 4
    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password.extend(random.choice(all_characters) for _ in range(length - 4))
    
    random.shuffle(password)
    
    complex_password = ''.join(password)
    
    passwords = set([complex_password])
    passwords = add_double_letter(passwords)
    passwords = generate_maj(passwords)
    passwords = start_symbol_digit(passwords, {"a": "@", "e": "€", "s": "$"}, 2)
    passwords = start_symbol_digit(passwords, {"a": "4", "e": "3", "i": "1", "o": "0"}, 2)
    
    complex_password = list(passwords)[0]
    
    return complex_password

def add_double_letter(passwords):
    new_passwords = set()
    for pwd in passwords:
        doubled_pwd = ''.join([char*2 if random.random() > 0.5 else char for char in pwd])
        new_passwords.add(doubled_pwd)
    return new_passwords

def generate_maj(passwords):
    new_passwords = set()
    for pwd in passwords:
        new_passwords.add(pwd.capitalize())
    return new_passwords

def start_symbol_digit(passwords, subs, nb_subs):
    new_passwords = set()
    for pwd in passwords:
        pwd_sub = pwd
        for key, val in subs.items():
            pwd_sub = pwd_sub.replace(key, val, nb_subs)
        new_passwords.add(pwd_sub)
    return new_passwords

def get_file_size_limit():
    sizes = {
        '1': 1 * 1024 * 1024 * 1024,
        '2': 3 * 1024 * 1024 * 1024, 
        '3': 5 * 1024 * 1024 * 1024,  
        '4': 10 * 1024 * 1024 * 1024 
    }
    
    print(f"\n{secondary}[{primary}1{secondary}] {primary}1Go")
    print(f"{secondary}[{primary}2{secondary}] {primary}3Go")
    print(f"{secondary}[{primary}3{secondary}] {primary}5Go")
    print(f"{secondary}[{primary}4{secondary}] {primary}10Go")
    choice = input(f"\n{INPUT} {tr('Choice')} -> {reset}")
    return sizes.get(choice, sizes['1'])

def main():
    filenames = [f'2-Input/Passwords/passlist{i}.txt' for i in range(1, 8)]
    word_list = load_wordlists(filenames)
    
    file_size_limit = get_file_size_limit()
    current_file_size = 0
    
    with open('passwords.txt', 'a') as f: 
        try:
            for word in word_list:
                if current_file_size >= file_size_limit:
                    print(f"\n{tr('FileSizeReached')}.")
                    break
                f.write(word + "\n")
                current_file_size += len(word) + 1  

            while True:
                if keyboard.is_pressed('esc'):  
                    print(f"\n{tr('ProgramStop')}.")
                    Continue()
                    Reset()

                if current_file_size >= file_size_limit:
                    print(f"\n{tr('FileSizeReached')}.")
                    Continue()
                    Reset()

                word_password = generate_word_password(word_list, min_length=6, max_length=16)
                numeric_password = generate_numeric_password(min_length=6, max_length=16)
                complex_password = generate_complex_password(min_length=6, max_length=16)
                
                f.write(f"{word_password}\n")
                f.write(f"{numeric_password}\n")
                f.write(f"{complex_password}\n")
                
                current_file_size += len(word_password) + len(numeric_password) + len(complex_password) + 3

        except Exception as e:
            Error()
            Continue()
        finally:
            f.close() 

if __name__ == "__main__":
    main()
