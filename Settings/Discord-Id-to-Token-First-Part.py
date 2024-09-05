from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import base64
    import os
except Exception as e:
    ErrorModule(e)

Title("Discord Token To Id")
try:
    userid = input(f"\n{INPUT} Victime ID -> {color.RESET}\n")
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    OnePartToken = str(encodedBytes, "utf-8")
    print(f'{INFO} {tr('OnePartToken')}: {secondary}{OnePartToken}.{color.RED}{color.RESET}')
    Continue()
    Reset()
except Exception as e:
    Error(e)
