from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

BEFORED = f'{secondary}[{primary}'
AFTERED = f'{secondary}]'

ADDED = f'{BEFORED}+{AFTERED}'

try:
    import requests
except Exception as e:
   ErrorModule(e)
   
Title("Discord Server Info")

try:
    invite = input(f"{color.RED}\n{INPUT} Server Invitation -> {color.RESET}")
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        data = response.json()
        try:
            code_value = data['code']
        except:
            code_value = "None"
        try:
            inviter_id = data['inviter']['id']
        except:
            inviter_id = "None"
        try:
            inviter_username = data['inviter']['username']
        except:
            inviter_username = "None"
        try:
            inviter_avatar = data['inviter']['avatar']
        except:
            inviter_avatar = "None"
        try:
            inviter_discriminator = data['inviter']['discriminator']
        except:
            inviter_discriminator = "None"
        try:
            inviter_public_flags = data['inviter']['public_flags']
        except:
            inviter_public_flags = "None"
        try:
            inviter_flags = data['inviter']['flags']
        except:
            inviter_flags = "None"
        try:
            inviter_banner = data['inviter']['banner']
        except:
            inviter_banner = "None"
        try:
            inviter_accent_color = data['inviter']['accent_color']
        except:
            inviter_accent_color = "None"
        try:
            inviter_global_name = data['inviter']['global_name']
        except:
            inviter_global_name = "None"
        try:
            inviter_banner_color = data['inviter']['banner_color']
        except:
            inviter_banner_color = "None"
        try:
            expires_at = data['expires_at']
        except:
            expires_at = "None"
        try:
            flags = data['flags']
        except:
            flags = "None"
        try:
            server_id = data['guild_id']
        except:
            server_id = "None"
        try:
            server_name = data['guild']['name']
        except:
            server_name = "None"
        try:
            server_icon = data['guild']['icon']
        except:
            server_icon = "None"
        try:
            server_features = data['guild']['features']
        except:
            server_features = "None"
        try:
            server_verification_level = data['guild']['verification_level']
        except:
            server_verification_level = "None"
        try:
            server_nsfw_level = data['guild']['nsfw_level']
        except:
            server_nsfw_level = "None"
        try:
            server_nsfw = data['guild']['nsfw']
        except:
            server_nsfw = "None"
        try:
            server_premium_subscription_count = data['guild']['premium_subscription_count']
        except:
            server_premium_subscription_count = "None"
        try:
            channel_id = data['channel']['id']
        except:
            channel_id = "None"
        try:
            channel_name = data['channel']['name']
        except:
            channel_name = "None"
    else:
        ErrorUrl()

    print(f"""{primary}
    Invitation Information:
    {ADDED}{primary} Invitation        : {secondary}{invite}{primary}
    {ADDED}{primary} Code              : {secondary}{code_value}{primary}
    {ADDED}{primary} {tr('Expired')}           : {secondary}{expires_at}{primary}
    {ADDED}{primary} Server ID         : {secondary}{server_id}{primary}
    {ADDED}{primary} Server Name       : {secondary}{server_name}{primary}
    {ADDED}{primary} Channel ID        : {secondary}{channel_id}{primary}
    {ADDED}{primary} Channel Name      : {secondary}{channel_name}{primary}
    {ADDED}{primary} Server Icon       : {secondary}{server_icon}{primary}
    {ADDED}{primary} Server Features   : {secondary}{server_features}{primary}
    {ADDED}{primary} Server NSFW Level : {secondary}{server_nsfw_level}{primary}
    {ADDED}{primary} Server NSFW       : {secondary}{server_nsfw}{primary}
    {ADDED}{primary} Flags             : {secondary}{flags}{primary}
    {ADDED}{primary} Server Verification Level         : {secondary}{server_verification_level}{primary}
    {ADDED}{primary} Server Premium Subscription Count : {secondary}{server_premium_subscription_count}{primary}

    Inviter Information:
    {ADDED}{primary} ID            : {secondary}{inviter_id}{primary}
    {ADDED}{primary} {tr('Username')}      : {secondary}{inviter_username}{primary}
    {ADDED}{primary} Global Name   : {secondary}{inviter_global_name}{primary}
    {ADDED}{primary} Avatar        : {secondary}{inviter_avatar}{primary}
    {ADDED}{primary} Discriminator : {secondary}{inviter_discriminator}{primary}
    {ADDED}{primary} Public Flags  : {secondary}{inviter_public_flags}{primary}
    {ADDED}{primary} Flags         : {secondary}{inviter_flags}{primary}
    {ADDED}{primary} Banner        : {secondary}{inviter_banner}{primary}
    {ADDED}{primary} Accent Color  : {secondary}{inviter_accent_color}{primary}
    {ADDED}{primary} {tr('BannerColor')}  : {secondary}{inviter_banner_color}{primary}
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)