import requests

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

def imgur(target: str):

    r = requests.post("https://imgur.com/signin/ajax_email_available", data={'email': target})

    try:
        if r.json()['data']['available'] == True:
            print(f"{RED}>{WHITE} Imgur")

        elif r.json()['data']['available'] == False:
            print(f"{GREEN}>{WHITE} Imgur")

        else:
            print(f"{RED}>{WHITE} Imgur")

    except:
        print(f"{RED}>{WHITE} Imgur")