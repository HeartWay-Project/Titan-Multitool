from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import bcrypt
    import hashlib
    import base64
    from hashlib import pbkdf2_hmac
except Exception as e:
    ErrorModule(e)

Title(f"Password Encrypted")
try:
    Slow(f"""{encrypted_banner}
{secondary}[{primary}01{secondary}] {primary}->{secondary} BCRYPT
{secondary}[{primary}02{secondary}] {primary}->{secondary} MD5
{secondary}[{primary}03{secondary}] {primary}->{secondary} SHA-1
{secondary}[{primary}04{secondary}] {primary}->{secondary} SHA-256
{secondary}[{primary}05{secondary}] {primary}->{secondary} PBKDF2 (SHA-256)
{secondary}[{primary}06{secondary}] {primary}->{secondary} Base64 Encode
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('CryptMethod')} -> {reset}")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        ErrorChoice()

    password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('EncryptedPasswd')} -> {secondary}")

    def encrypt_password(choice, password):
        if choice in ['1', '01']:
            try:
                salt = bcrypt.gensalt()
                encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                return encrypted_password.decode('utf-8')
            except Exception as e:
                Error()
                Continue()
        elif choice in ['2', '02']:
            try:
                encrypted_password = hashlib.md5(password.encode('utf-8')).hexdigest()
                return encrypted_password
            except Exception as e:
                Error()
                Continue()
        elif choice in ['3', '03']:
            try:
                encrypted_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
                return encrypted_password
            except Exception as e:
                Error()
                Continue()
        elif choice in ['4', '04']:
            try:
                encrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                return encrypted_password
            except Exception as e:
                Error()
                Continue()
        elif choice in ['5', '05']:
            try:
                salt = "this_is_a_salt".encode('utf-8')
                encrypted_password = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
                return encrypted_password
            except Exception as e:
                Error()
                Continue()
        elif choice in ['6', '06']:
            try:
                encrypted_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
                return encrypted_password
            except Exception as e:
                Error()
                Continue()
        else:
            return None

    encrypted_password = encrypt_password(choice, password)
    if encrypted_password:
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {tr('EncryptPassword')}: {secondary}{encrypted_password}{reset}")
        
        save_choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('SavePassEncrypted')} -> {reset}")
        
        if save_choice.lower() in ['y', 'Y', 'Yes', 'YES', 'yes', 'o', 'O', 'Oui', 'OUI', 'oui']:
            file_name = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('FileName')} -> {reset}")
            file_path = f"1-Output/PasswordEncrypted/{file_name}.txt"
            try:
                with open(file_path, 'w') as file:
                    file.write(encrypted_password)
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {tr('ConfirmPasswdSaved')} {file_path}{reset}")
            except Exception as e:
                Error()
                Continue()
        
        Continue()
        Reset()
except Exception as e:
    Error(e)
