from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def duolingo(target: str):

    r = await Request(f"https://www.duolingo.com/2017-06-30/users", params={'email': target}).get()

    try:
        if """{"users":[]}""" in r.text:
            print(f"{RED}>{WHITE} Duolingo")

        else:
            valid = r.json()['users'][0]['username']
            
            print(f"{GREEN}>{WHITE} Duolingo")

    except:
        print(f"{RED}>{WHITE} Duolingo")