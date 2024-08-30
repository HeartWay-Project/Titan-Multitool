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

async def github(target: str):

    r = await Request(f"https://api.github.com/search/users?q={target}+in:email").get()

    try:
        if '"total_count": 0' in r.text:
            pass

        else:
            try:
                data = r.json()['items'][0]

                api = await Request(f"https://api.github.com/users/{data['login']}").get()

                name = api.json()['name']
                creation = api.json()['created_at']
                update = api.json()['updated_at']

                c_datetime = datetime.fromisoformat(creation.replace("Z", "+00:00"))
                c_date = c_datetime.strftime("%Y-%m-%d %H:%M:%S")

                u_datetime = datetime.fromisoformat(update.replace("Z", "+00:00"))
                u_date = u_datetime.strftime("%Y-%m-%d %H:%M:%S")

                print(f"{GREEN}>{WHITE} Github")
                print(f"  ├──> Username : {data['login']}")
                if name != None:
                    print(f"  ├──> Name : {name}")
                else: 
                    pass
                print(f"  ├──> Id : {data['id']}")
                print(f"  ├──> Avatar : {data['avatar_url']}")
                print(f"  ├──> Created on : {c_date}")
                print(f"  ├──> Update on : {u_date}")
                print(f"  └──> Account : {CYAN}https://github.com/{data['login']}/{WHITE}")
                
            except:
                pass
    
    except:
        pass