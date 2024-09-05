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
   

Title("Discord Webhook Delete")

try:
    webhook_url = input(f"{color.RED}\n{INPUT} {tr('URLWebhook')} -> {color.RESET}")
    CheckWebhook(webhook_url)
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print(f"{color.RED}{INFO} {tr('WebhookDelete')}")
        Continue()
        Reset()
    except:
        ErrorWebhook()
except Exception as e:
    Error(e)