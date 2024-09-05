from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

def main():
    Title("Discord Invite Bot To Id")
    
    while True:
        try:
            try:
                IdBot = int(input(f"\n{primary}{INPUT} ID bot -> {reset}"))
            except ValueError:
                ErrorId()
                continue

            URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'
            print(f"\n{INFO} URL bot: \"{secondary}{URLBot}{primary}\"{reset}")

            choice = input(f"\n{INPUT} {tr('OpenBrowser')} -> {reset}")
            if choice.lower() in ['y', 'yes']:
                webbrowser.open_new_tab(URLBot)
                Slow(f"\n{valid}{tr('OpenURL')}{reset}")
            else:
                Continue()
                Reset()

        except Exception as e:
            Error(e)
            continue

if __name__ == "__main__":
    main()
