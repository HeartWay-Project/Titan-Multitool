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
   
Title("Discord Token Spammer")

try:
    print()
    token = Choice1TokenDiscord()
    channel = input(f"{primary}{INPUT} {tr('ChannelSpamID')} -> {color.RESET}")
    message = input(f"{primary}{INPUT} {tr('SpamMessage')} -> {color.RESET}")
    message_len = len(message)
    if message_len > 10:
        message_sensur = message[:10]
        message_sensur = message_sensur + "..."
    else:
        message_sensur = message
    try:
        threads_number = int(input(f"{INPUT} {tr('ThreadsNumber')} (recommended: 2, 4) -> {color.RESET}"))
    except:
        ErrorNumber()

    def spam():
        try:
            response = requests.post(
                f"https://discord.com/api/channels/{channel}/messages",
                data={'content': message},
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Authorization': token
                }
            )
            response.raise_for_status()
            print(f"{valid}[{secondary}{current_time_hour()}{valid}] {GEN_VALID} Message: {color.WHITE}{message_sensur}{color.GREEN} | {tr('Channel')}: {color.WHITE}{channel}{color.GREEN} | Status: {color.WHITE}Send{color.GREEN}")
        except:
            print(f"{invalid}[{secondary}{current_time_hour()}{invalid}] {GEN_INVALID} Message: {color.WHITE}{message_sensur}{color.RED} | {tr('Channel')}: {color.WHITE}{channel}{color.RED} | Status: {color.WHITE}{tr('Error')} {response.status_code}{color.RED}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=spam)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)