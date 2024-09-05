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
   

Title("Discord Token Joiner")

try:
    print()
    token = Choice1TokenDiscord()
    invite = input(f"{color.RED}{INPUT} Server Invitation -> {color.RESET}")

    invite_code = invite.split("/")[-1]

    try:
        response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
        if response.status_code == 200:
            server_name = response.json().get('guild', {}).get('name')
        else:
            server_name = invite
    except:
        server_name = invite

    try:
            headers = {
                'Authorization': token
            }
            response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)
            
            if response.status_code == 200:
                print(f"\n{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}Joined{primary} | Server: {color.WHITE}{server_name}{primary}\n")
            else:
                print(f"\n{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status: {color.WHITE}{tr('Error')} {response.status_code}{color.RED} | Server: {color.WHITE}{server_name}{color.RED}\n")
    except:
        print(f"\n{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status: {color.WHITE}{tr('Error')}{primary} | Server: {color.WHITE}{server_name}{primary}\n")

    Continue()
    Reset()
except Exception as e:
    Error(e)