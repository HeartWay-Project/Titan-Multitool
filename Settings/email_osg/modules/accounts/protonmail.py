from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

from datetime import datetime
import re

async def protonmail(target: str):

    target_domain = target.split('@')[1]
    proton_domains = ['pm.me', 'proton.me', 'protonmail.com', 'protonmail.ch']

    if target_domain in proton_domains:

        api = f"https://api.protonmail.ch/pks/lookup?op=index&search={target}"

        r = await Request(api).get()

        match = re.search(r'\b\d{10}\b', r.text)

        if match:
            timestamp = int(match.group())
            date_of_creation = datetime.fromtimestamp(timestamp)

            print(f"{GREEN}>{WHITE} Protonmail")
            print(f"  └──> Created on : {date_of_creation}")

        else:
            print(f"{RED}>{WHITE} Protonmail")

    else:
        print(f"{RED}>{WHITE} Protonmail")