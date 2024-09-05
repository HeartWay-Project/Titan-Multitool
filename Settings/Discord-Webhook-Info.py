from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   

Title("Discord Webhook Info")

BEFOREINFO = f"{secondary}[{primary}+{secondary}]{primary}"

try:
    def info_webhook(webhook):
            headers = {
                'Content-Type': 'application/json',
            }

            response = requests.get(webhook_url, headers=headers)
            webhook_info = response.json()
            print(f"{color.RED}\nInformation Webhook:")

            print(f"{BEFOREINFO} ID      : {secondary}", webhook_info['id'])
            print(f"{BEFOREINFO} Token   : {secondary}", webhook_info['token'])
            print(f"{BEFOREINFO} Name    : {secondary}", webhook_info['name'])
            print(f"{BEFOREINFO} Avatar  : {secondary}", webhook_info['avatar'])
            print(f"{BEFOREINFO} Type    : {secondary}", "bot" if webhook_info['type'] == 1 else "webhook utilisateur")
            print(f"{BEFOREINFO} Channel ID : {secondary}", webhook_info['channel_id'])
            print(f"{BEFOREINFO} Server ID  : {secondary}", webhook_info['guild_id'])

            print(f"{color.RED}\nUser information associated with the Webhook:")
            if 'user' in webhook_info:
                user_info = webhook_info['user']

                print(f"{BEFOREINFO} ID          : {secondary}", user_info['id'])
                print(f"{BEFOREINFO} Name        : {secondary}", user_info['username'])
                print(f"{BEFOREINFO} DisplayName : {secondary}", user_info['global_name'])
                print(f"{BEFOREINFO} Number      : {secondary}", user_info['discriminator'])
                print(f"{BEFOREINFO} Avatar      : {secondary}", user_info['avatar'])
                print(f"{BEFOREINFO} Flags       : {secondary}", user_info['flags'], " Publique:", user_info['public_flags'])
                print(f"{BEFOREINFO} Color       : {secondary}", user_info['accent_color'])
                print(f"{BEFOREINFO} Decoration  : {secondary}", user_info['avatar_decoration_data'])
                print(f"{BEFOREINFO} Banner      : {secondary}", user_info['banner_color'])
                print("")
            else:
                print("\nNone.")


    webhook_url = input(f"{primary}\n{INPUT} Webhook URL -> {reset}")
    CheckWebhook(webhook_url)
    info_webhook(webhook_url)
    Continue()
    Reset()
except Exception as e:
    Error(e)