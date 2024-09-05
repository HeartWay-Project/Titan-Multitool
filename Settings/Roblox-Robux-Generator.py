from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import random
    import string
    import json
    import requests
    import threading
    import keyboard  
except Exception as e:
    ErrorModule(e)

Title("Robux Generator")

running = True  

def stop_program():
    global running
    running = False
    print(f"{tr('ProgramStop')}.")

keyboard.add_hotkey('esc', stop_program)  # Ajout d'un raccourci pour la touche Échap

try:
    try:
        threads_number = int(input(f"\n{INPUT} {tr('ThreadsNumber')} -> {color.RESET}"))
    except:
        ErrorNumber()

    def send_webhook(embed_content):
        payload = {
            'embeds': [embed_content],
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }

        headers = {
            'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    def robux_check():
        code_robux = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(10)])
        url_robux = f'https://roblox.com/gift-codes/{code_robux}'
        response = requests.get(f'https://roblox.com/api/v1/gift-codes/{code_robux}/validate', timeout=1)
        if response.status_code == 200 and response.json().get('valid'):
            if webhook in ['y']:
                embed_content = {
                    'title': f'Robux Valid !',
                    'description': f"**__Robux:__**\n```{url_robux}```",
                    'color': color_webhook,
                    'footer': {
                        "text": username_webhook,
                        "icon_url": avatar_webhook,
                    }
                }
                send_webhook(embed_content)
                print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Robux: {color.WHITE}{url_robux}{color.GREEN}{reset}")
            else:
                print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Robux: {color.WHITE}{url_robux}{color.GREEN}{reset}")
        else:
            print(f"{invalid}[{secondary}{current_time_hour()}{invalid}] {GEN_INVALID} Status: {color.WHITE}Invalid{color.RED} | Robux: {color.WHITE}{url_robux}{color.RED}{reset}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=robux_check)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while running:  
        request()
except Exception as e:
    Error(e)
