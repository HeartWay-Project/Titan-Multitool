from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def spotify(target: str):

    r = await Request(f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={target}").get()

    try:
        if r.json()['status'] == 20:
            print(f"{GREEN}>{WHITE} Spotify")

        else:
            print(f"{RED}>{WHITE} Spotify")

    except:
        print(f"{RED}>{WHITE} Spotify")