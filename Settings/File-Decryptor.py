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

Title(f"File Decryptior")

def decrypt_file(encrypted_file_content, password):
    salt = encrypted_file_content[:16]
    iv = encrypted_file_content[16:32]
    encrypted_content = encrypted_file_content[32:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_content) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

try:
    Slow(f"""{encrypted_banner}
{secondary}[{primary}01{secondary}] {primary}->{secondary} {tr('DecryptFile')}
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('Chose')} -> {reset}")

    if choice not in ['1', '01']:
        ErrorChoice()

    file_path = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('PathToDecrypt')} -> {secondary}")
    password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('PasswdForDecrypt')} -> {secondary}")

    try:
        with open(file_path, 'rb') as file:
            encrypted_file_content = file.read()
    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorReadFile')}: {e}")
        raise e

    try:
        decrypted_content = decrypt_file(encrypted_file_content, password)
        output_directory = "1-Output/FileDecrypted"
        os.makedirs(output_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        decrypted_file_path = os.path.join(output_directory, file_name.replace('.enc', ''))
        
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_content)
        
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {tr('DecryptedContent')} {decrypted_file_path}{reset}")
    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorDecrypt')} {e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)
