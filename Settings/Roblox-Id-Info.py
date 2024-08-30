from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   
   
Title("Roblox User Info")

try:
    user_id = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} ID -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
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
    {INFO_ADD} Username       : {secondary}{username}{invalid}
    {INFO_ADD} Id             : {secondary}{userid}{invalid}
    {INFO_ADD} Display Name   : {secondary}{display_name}{invalid}
    {INFO_ADD} Description    : {secondary}{description}{invalid}
    {INFO_ADD} Created        : {secondary}{created_at}{invalid}
    {INFO_ADD} Banned         : {secondary}{is_banned}{invalid}
    {INFO_ADD} External Name  : {secondary}{external_app_display_name}{invalid}
    {INFO_ADD} Verified Badge : {secondary}{has_verified_badge}{invalid}
    """)
        Continue()
        Reset()
    except:
        ErrorId()
except Exception as e:
    Error(e)