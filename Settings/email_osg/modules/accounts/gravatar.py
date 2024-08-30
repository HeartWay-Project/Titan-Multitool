from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

import hashlib

async def gravatar(target: str):

    encoded_email = target.lower().encode('utf-8')
    hashed_email = hashlib.sha256(encoded_email).hexdigest()

    r = await Request(f"https://en.gravatar.com/{hashed_email}.json").get()

    try:
        if "User not found" in r.text:
            print(f"{RED}>{WHITE} Gravatar")

        else:
            data = r.json()['entry'][0]

            print(f"{GREEN}>{WHITE} Gravatar")
            print(f"  ├──> Username : {data['displayName']}")

            try:
                avatar_url_seaked = data['thumbnailUrl']
                avatar_url = str(avatar_url_seaked).replace("\\", "")

                print(f"  ├──> Avatar : {avatar_url}")

            except:
                pass

            print(f"  └──> Account : {CYAN}https://gravatar.com/{data['displayName']}/{WHITE}")

    except:
        print(f"{RED}>{WHITE} Gravatar")