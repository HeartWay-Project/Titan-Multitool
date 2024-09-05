from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token House Changer")

try:
    print()
    token = Choice1TokenDiscord()
    print(f"""
    {secondary}[{primary}01{secondary}] {primary}->{secondary} Bravery
    {secondary}[{primary}02{secondary}] {primary}->{secondary} Brilliance
    {secondary}[{primary}03{secondary}] {primary}->{secondary} Balance
    """)

    house = input(f"{primary}{INPUT} House -> {color.RESET}").lstrip("0")

    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        ErrorToken()
    else:
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if house in ["1", "01"]: payload = {'house_id': 1}
        elif house in ["2", "02"]: payload = {'house_id': 2}
        elif house in ["3", "03"]: payload = {'house_id': 3}
        else:
            ErrorChoice()
        r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        if r.status_code == 204:
            print(f"{primary}{INFO} Hypesquad house changed.")
            Continue()
            Reset()
        else:
            print(f"{primary}{ERROR} Hypesquad house has not changed.")
except Exception as e:
    Error(e)