from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def x(target: str):

    r = await Request(f"https://api.twitter.com/i/users/email_available.json?email={target}").get()

    try:
        if r.json()['taken']:
            print(f"{GREEN}>{WHITE} 𝕏")

        else:
            print(f"{RED}>{WHITE} 𝕏")

    except:
        print(f"{RED}>{WHITE} 𝕏")