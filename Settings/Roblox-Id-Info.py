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
   
   
Title("Roblox User Info")

try:
    user_id = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} ID -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('tool_infos_recovery')}{reset}")
    try:

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()

        try:
            userid = user_info['id']
        except:
            userid = "None"
        
        try:
            display_name = user_info['displayName']
        except:
            display_name = "None"
        
        try:
            username = user_info['name']
        except:
            username = "None"

        try:
            description = user_info['description']
        except:
            description = "None"

        try:
            created_at = user_info['created']
        except:
            created_at = "None"
        
        try:
            is_banned = user_info['isBanned']
        except:
            is_banned = "None"
        
        try:
            external_app_display_name = user_info['externalAppDisplayName']
        except:
            external_app_display_name = "None"

        try:
            has_verified_badge = user_info['hasVerifiedBadge']
        except:
            has_verified_badge = "None"

        print(f"""
    {INFO_ADD} {tr('Username')}       : {secondary}{username}{primary}
    {INFO_ADD} Id             : {secondary}{userid}{primary}
    {INFO_ADD} {tr('DisplayName')}   : {secondary}{display_name}{primary}
    {INFO_ADD} Description    : {secondary}{description}{primary}
    {INFO_ADD} {tr('Created')}        : {secondary}{created_at}{primary}
    {INFO_ADD} {tr('Banned')}         : {secondary}{is_banned}{primary}
    {INFO_ADD} External Name  : {secondary}{external_app_display_name}{primary}
    {INFO_ADD} {tr('VerifBadge')} : {secondary}{has_verified_badge}{primary}
    """)
        Continue()
        Reset()
    except:
        ErrorId()
except Exception as e:
    Error(e)