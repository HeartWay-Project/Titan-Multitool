from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def chess(target: str):

    r = await Request(f"https://www.chess.com/callback/email/available?email={target}").post()

    try:
        if r.json()['isEmailAvailable'] == True:
            print(f"{RED}>{WHITE} Chess")

        elif r.json()['isEmailAvailable'] == False:
            print(f"{GREEN}>{WHITE} Chess")

        else:
            print(f"{RED}>{WHITE} Chess")

    except:
        pass