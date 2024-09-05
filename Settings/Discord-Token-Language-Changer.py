from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
    import time
    import random
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Language Changer")

try:
    print()
    token = Choice1TokenDiscord()

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        try:
            amount = int(input(f"{primary}{INPUT} {tr('CycleNumber')} -> {color.RESET}"))
        except:
            ErrorNumber()

        for i in range(amount):
            try:
                time.sleep(0.6)
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{primary}[{secondary}{current_time_hour()}{invalid}] {ADD} Status: {color.WHITE}{tr('Changed')}{primary} | Language: {color.WHITE}{random_language}{primary}")
            except:
                print(f"{primary}[{secondary}{current_time_hour()}{invalid}] {ERROR} Status:  {color.WHITE}{tr('Error')}{primary}  | Language: {color.WHITE}{random_language}{primary}")
        print(f"\n{primary}{INFO} Finish.")
        Continue()
        Reset()
    else:
        ErrorToken()
except Exception as e:
    Error(e)