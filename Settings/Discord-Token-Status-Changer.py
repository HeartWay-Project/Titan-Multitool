from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
    import time
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Status Changer")

try:
    print()
    token = Choice1TokenDiscord()
    try:
        statue_number = int(input(f"{color.BLUE}{INPUT} {tr('StatusCycle')} -> {color.RESET}"))
    except:
        ErrorNumber()

    statues = []

    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    if statue_number >= 1 and statue_number <= 4:
        for loop in range(0, statue_number):
            choice = str(input(f"{color.RED}{INPUT} Custom Status {loop+1} -> {color.RESET}"))
            statues.append(choice)
    else:
        ErrorNumber()

    while True:
        for i in range(len(statues)):
            CustomStatus = {"custom_status": {"text": statues[i]}}
            try:
                r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Changed')}{color.BLUE} | Status Discord: {color.WHITE}{statues[i]}{color.BLUE}")
                i += 1
                time.sleep(5)
            except Exception as e:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status: {color.WHITE}{tr('Changed')}{color.BLUE} | Status Discord: {color.WHITE}{statues[i]}{color.BLUE}")
                time.sleep(5)
except Exception as e:
    Error(e)