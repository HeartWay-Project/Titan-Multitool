from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def pinterest(target: str):

    params={
        "source_url": "/",
        "data": '{"options": {"email": "'+ target +'"}, "context": {}}'
    }

    r = await Request("https://www.pinterest.fr/resource/EmailExistsResource/get/", params=params).get()

    try:
        if r.json()["resource_response"]["data"]:
            print(f"{GREEN}>{WHITE} Pinterest")

        else:
            print(f"{RED}>{WHITE} Pinterest")

    
    except:
        print(f"{RED}>{WHITE} Pinterest")