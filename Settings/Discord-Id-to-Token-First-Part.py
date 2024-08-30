from Config.Util import *
from Config.Config import *
try:
    import base64
    import os
except Exception as e:
    ErrorModule(e)

Title("Discord Token To Id")
try:
    userid = input(f"{color.RED}\n{INPUT} Victime ID -> {color.RESET}")
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    OnePartToken = str(encodedBytes, "utf-8")
    print(f'{color.RED}{INFO} Part One Token: {color.WHITE}{OnePartToken}.{color.RED}{color.RESET}')
    Continue()
    Reset()
except Exception as e:
    Error(e)
