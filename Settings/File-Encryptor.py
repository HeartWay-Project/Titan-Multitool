from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    import os
    import base64
except Exception as e:
    ErrorModule(e)

Title(f"File Encryptior")

def encrypt_file(file_content, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    iv = os.urandom(16)

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_content) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_content = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_file_content = salt + iv + encrypted_content
    return encrypted_file_content

try:
    Slow(f"""{encrypted_banner}
{secondary}[{primary}01{secondary}] {primary}->{secondary} AES 
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('CryptMethod')} -> {reset}")

    if choice not in ['1', '01']:
        ErrorChoice()

    file_path = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('PathFileEncrypt')} -> {secondary}")
    password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('PasswdCrypt')} -> {secondary}")

    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorReadFile')}: {e}")
        raise e

    encrypted_content = encrypt_file(file_content, password)
    if encrypted_content:
        try:
            output_directory = "1-Output/FileEncrypted"
            os.makedirs(output_directory, exist_ok=True)
            file_name = os.path.basename(file_path)
            encrypted_file_path = os.path.join(output_directory, f"{file_name}.enc")
            
            with open(encrypted_file_path, 'wb') as file:
                file.write(encrypted_content)
            
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {tr('SaveFileEncrypt')} {encrypted_file_path}{reset}")
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorEncryptFile')} {e}")

        Continue()
        Reset()
except Exception as e:
    Error(e)
