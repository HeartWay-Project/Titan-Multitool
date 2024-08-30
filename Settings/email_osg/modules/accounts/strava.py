from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def strava(target: str):

    req = await Request(f"https://www.strava.com/athletes/email_unique?email={target}").get()

    try:
        if "false" in req.text:
            print(f"{GREEN}>{WHITE} Strava")

        elif "true" in req.text:
            print(f"{RED}>{WHITE} Strava")

        else:
            print(f"{RED}>{WHITE} Strava")
            
    except:
        print(f"{RED}>{WHITE} Strava")