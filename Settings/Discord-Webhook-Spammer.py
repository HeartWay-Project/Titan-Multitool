from Config.Util import *
from Config.Config import *
try:
    import requests
    import json
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Webhook Spammer")

try:
    webhook_url = input(f"{color.RED}\n{INPUT} Webhook URL -> {color.RESET}")
    CheckWebhook(webhook_url)
    message = input(f"{color.RED}{INPUT} Message -> {color.RESET}")

    try:
        threads_number = int(input(f"{INPUT} Threads Number -> {color.RESET}"))
    except:
        ErrorNumber()

    def send_webhook():
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            'content': message,
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }
        try:
            response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Message: {color.WHITE}{message}{color.GREEN} | Status: {color.WHITE}Send{color.GREEN}")
        except:
            print(f"{invalid}[{secondary}{current_time_hour()}{invalid}] {GEN_INVALID} Message: {color.WHITE}{message}{color.RED} | Status: {color.WHITE}Rate Limit{color.RED}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=send_webhook)
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