from Config.Util import *
from Config.Config import *
try:
    import requests
    import json
except Exception as e:
   ErrorModule(e)
   
Title("Roblox Cookie Info")

try:
    cookie = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {secondary}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        print(info.json())
        information = json.loads(info.text)
        status = "Valid"
    except:
        status = "Invalid"

    try:
        username_roblox = information['UserName']
    except:
        username_roblox = "None"

    try:
        user_id_roblox = information["UserID"]
    except:
        user_id_roblox = "None"

    try:
        robux_roblox = information["RobuxBalance"]
    except:
        robux_roblox = "None"
    try:
        premium_roblox = information["IsPremium"]
    except:
        premium_roblox = "None"

    try:
        avatar_roblox = information["ThumbnailUrl"]
    except:
        avatar_roblox = "None"

    try:
        builders_club_roblox = information["IsAnyBuildersClubMember"]
    except:
        builders_club_roblox = "None"


    print(f"""
    {INFO_ADD} Status        : {secondary}{status}{invalid}
    {INFO_ADD} Username      : {secondary}{username_roblox}{invalid}
    {INFO_ADD} Id            : {secondary}{user_id_roblox}{invalid}
    {INFO_ADD} Robux         : {secondary}{robux_roblox}{invalid}
    {INFO_ADD} Premium       : {secondary}{premium_roblox}{invalid}
    {INFO_ADD} Builders Club : {secondary}{builders_club_roblox}{invalid}
    {INFO_ADD} Avatar        : {secondary}{avatar_roblox}{invalid}
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)