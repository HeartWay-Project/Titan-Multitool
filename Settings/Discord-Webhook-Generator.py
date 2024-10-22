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
   
Title("Discord Webhook Generator")

try:
    webhook = input(f"{color.RED}\n{INPUT} {tr('WebhookYN')} -> {color.RESET}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES', 'o', 'O', 'Oui', 'oui', 'OUI']:
        webhook_url = input(f"{color.RED}{INPUT} {tr('URLWebhook')} -> {color.RESET}")
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

    def webhook_check():
        first = ''.join([str(random.randint(0, 9)) for _ in range(19)])
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([68])))
        webhook_test_code = f"{first}/{second}"
        webhook_test_url = f"https://discord.com/api/webhooks/{webhook_test_code}"

        try:
            response = requests.head(webhook_test_url)
            if response.status_code == 200:
                if webhook in ['y']:
                    embed_content = {
                    'title': f'Webhook Valid !',
                    'description': f"**__Webhook:__**\n```{webhook_test_url}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                    }
                    send_webhook(embed_content)
                    print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {secondary}Valid{color.GREEN}  | Webhook: {secondary}{webhook_test_code}{color.GREEN}")
                else:
                    print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {secondary}Valid{color.GREEN}  | Webhook: {secondary}{webhook_test_code}{color.GREEN}")
            else:
                print(f"{invalid}[{secondary}{current_time_hour()}{invalid}] {GEN_INVALID} Status: {secondary}Invalid{color.RED} | Webhook: {secondary}{webhook_test_code}{color.RED}")
        except:
            print(f"{invalid}[{secondary}{current_time_hour()}{invalid}] {GEN_INVALID} Status: {secondary}{tr('Error')}{color.RED} | Webhook: {secondary}{webhook_test_code}{color.RED}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=webhook_check)
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