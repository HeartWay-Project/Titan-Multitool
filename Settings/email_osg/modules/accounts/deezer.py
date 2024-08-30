from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

def deezer(target: str):
    try:
        s = Request(url=None).Session()

        r = s.post("https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&input=3&api_version=1.0&api_token=&cid=")
        token = r.json()['results']['checkForm']

        params = {
            'method': 'deezer.emailCheck',
            'input': 3,
            'api_version': 1.0,
            'api_token': token,
        }

        api = s.post(f"https://www.deezer.com/ajax/gw-light.php", params=params, data='{"EMAIL":"'+ target +'"}')

        if api.json()['results']['availability'] == True:
            print(f"{RED}>{WHITE} Deezer")

        elif api.json()['results']['availability'] == False:
            print(f"{GREEN}>{WHITE} Deezer")

        else:
            print(f"{RED}>{WHITE} Deezer")

        s.close()

    except:
        s.close()
        pass