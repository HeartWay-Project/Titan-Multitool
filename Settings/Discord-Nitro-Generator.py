import os
from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import keyboard
    import random
    import string
    import json
    import requests
    import threading
except ImportError as e:
    ErrorModule(e)

Title("Discord Nitro Generator")

stop_threads = False

output_dir = "1-Output/Nitro/"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "valid_nitros.txt")

def prompt_webhook():
    webhook = input(f"{primary}\n{INPUT} {tr('WebhookYN')} -> {reset}").lower()
    if webhook in ['y', 'yes']:
        webhook_url = input(f"\n{primary}{INPUT} {tr('URLWebhook')} -> {reset}")
        CheckWebhook(webhook_url)
        return webhook_url
    return None

def get_threads_number():
    try:
        return int(input(f"\n{INPUT} {tr('ThreadsNumber')} -> {reset}"))
    except ValueError:
        ErrorNumber()
        return get_threads_number()

def send_webhook(embed_content, webhook_url):
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    except requests.RequestException as e:
        Error(e)

def generate_nitro_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

def check_nitro_code(webhook_url=None):
    code_nitro = generate_nitro_code()
    url_nitro = f'https://discord.gift/{code_nitro}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)

    if response.status_code == 200:
        log_message = f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Status:  {secondary}Valid{valid}  | Nitro: {secondary}{url_nitro}{valid}{reset}"

        with open(output_file, 'a') as f:
            f.write(f"{url_nitro}\n")

        if webhook_url:
            embed_content = {
                'title': 'Nitro Valid !',
                'description': f"**__Nitro:__**\n```{url_nitro}```",
                'color': color_webhook,
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                }
            }
            send_webhook(embed_content, webhook_url)
    else:
        log_message = f"{primary}[{secondary}{current_time_hour()}{primary}] {GEN_INVALID} Status: {secondary}Invalid{primary} | Nitro: {secondary}{url_nitro}{primary}{reset}"

    print(log_message)

def run_threads(threads_number, webhook_url=None):
    threads = []
    for _ in range(threads_number):
        t = threading.Thread(target=check_nitro_code, args=(webhook_url,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

def main():
    try:
        webhook_url = prompt_webhook()
        threads_number = get_threads_number()

        def monitor_escape_key():
            global stop_threads
            keyboard.wait('esc')
            stop_threads = True
            print(f"{invalid}\n{tr('ProgramStop')}.{reset}")

        esc_thread = threading.Thread(target=monitor_escape_key)
        esc_thread.start()

        while not stop_threads:
            run_threads(threads_number, webhook_url)
    except Exception as e:
        Error(e)

if __name__ == "__main__":
    main()
