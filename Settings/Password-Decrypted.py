from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import bcrypt
    import hashlib
    import random
    import string
    import threading
    import time
    import base64
    from hashlib import pbkdf2_hmac
except Exception as e:
    ErrorModule(e)
Title(f"Password Decrypted")
try:
    Slow(f"""{decrypted_banner}
{secondary}[{primary}01{secondary}] {primary}->{secondary} BCRYPT
{secondary}[{primary}02{secondary}] {primary}->{secondary} MD5
{secondary}[{primary}03{secondary}] {primary}->{secondary} SHA-1
{secondary}[{primary}04{secondary}] {primary}->{secondary} SHA-256
{secondary}[{primary}05{secondary}] {primary}->{secondary} PBKDF2 (SHA-256)
{secondary}[{primary}06{secondary}] {primary}->{secondary} Base64 Decode
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('EncryptMetod')} -> {reset}")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        ErrorChoice()

    encrypted_password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('EncryptPassword')} -> {secondary}")
    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('ThreadsNumber')} -> {secondary}"))
    except:
        ErrorNumber()
    try:
        characters_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('PasswordCharacters')} -> {secondary}"))
    except:
        ErrorNumber()

    Title(f"Password Decrypted - Encrypted Password: {encrypted_password}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('PasswordCrackBrute')}{reset}")

    password = False
    generated_passwords = set()

    salt = "this_is_a_salt".encode('utf-8')

    all_characters = string.ascii_letters + string.digits + string.punctuation
    all_characters_len = len(all_characters)

    def error_decrypted():
        if choice in ['1', '01']:
            encryption = "BCRYPT"
        elif choice in ['2', '02']:
            encryption = "MD5"
        elif choice in ['3', '03']:
            encryption = "SHA-1"
        elif choice in ['4', '04']:
            encryption = "SHA-256"
        elif choice in ['5', '05']:
            encryption = "PBKDF2 (SHA-256)"
        elif choice in ['6', '06']:
            encryption = "Base64 Decode"
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('Encryption')} "{secondary}{encrypted_password}{primary}" {tr('NotAccept')} "{secondary}{encryption}{primary}".')
        Continue()
        Reset()

    def check_password(password_test):
        global choice, encrypted_password
        if choice in ['1', '01']:
            try:
                return bcrypt.checkpw(password_test.encode('utf-8'), encrypted_password.encode('utf-8'))
            except:
                error_decrypted()
        elif choice in ['2', '02']:
            try:
                return hashlib.md5(password_test.encode('utf-8')).hexdigest() == encrypted_password
            except:
                error_decrypted()
        elif choice in ['3', '03']:
            try:
                return hashlib.sha1(password_test.encode('utf-8')).hexdigest() == encrypted_password
            except:
                error_decrypted()
        elif choice in ['4', '04']:
            try:
                return hashlib.sha256(password_test.encode('utf-8')).hexdigest() == encrypted_password
            except:
                error_decrypted()
        elif choice in ['5', '05']:
            try:
                return pbkdf2_hmac('sha256', password_test.encode('utf-8'), salt, 100000).hex() == encrypted_password
            except:
                error_decrypted()
        elif choice in ['6', '06']:
            try:
                return base64.b64decode(encrypted_password.encode('utf-8')).decode('utf-8') == password_test
            except:
                error_decrypted()
        else:
            return False

    def generate_password(characters_number):
        return ''.join(random.choice(all_characters) for _ in range(random.randint(1, characters_number)))

    def test_decrypted():
        global password
        while not password:
            password_test = generate_password(characters_number)
            if password_test not in generated_passwords:
                generated_passwords.add(password_test)
                if check_password(password_test):
                    password = True
                    print(f'{BEFORE + current_time_hour() + AFTER} {ADD} {tr('Password')}: {secondary}{password_test}{reset}')
                    time.sleep(1)
                    Continue()
                    Reset()

    def request():
        threads = []
        try:
            for _ in range(threads_number):
                t = threading.Thread(target=test_decrypted)
                t.start()
                threads.append(t)
        except Exception as e:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while not password:
        request()
except Exception as e:
    Error(e)