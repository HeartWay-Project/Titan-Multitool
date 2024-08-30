from email_osg.Requests import *

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def adobe(target: str):
    data = {
        "username": target,
        "usernameType": "EMAIL"
    }

    headers = {
        'x-ims-clientid': 'homepage_milo',
        'content-type': 'application/json'
    }

    r = await Request("https://auth.services.adobe.com/signin/v2/users/accounts", headers=headers, json=data).post()

    try:
        if r.json()[0]['authenticationMethods']:
            print(f"{GREEN}>{WHITE} Adobe")

        else:
            print(f"{RED}>{WHITE} Adobe")

    except:
        print(f"{RED}>{WHITE} Adobe")