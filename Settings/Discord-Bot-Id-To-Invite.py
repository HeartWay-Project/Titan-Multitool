from Config.Util import *
from Config.Config import *
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

            choice = input(f"\n{INPUT} Open the Internet? (y/n) -> {reset}")
            if choice.lower() in ['y', 'yes']:
                webbrowser.open_new_tab(URLBot)
                Slow(f"\n{valid}Opening the URL in your browser...{reset}")
            else:
                Slow(f"\n{color.YELLOW}URL not opened.{color.RESET}")

            next_action = input(f"\n{INPUT} Would you like to enter another ID? (y/n) -> {reset}")
            if next_action.lower() not in ['y', 'yes']:
                Slow(f"{primary}Quitting...{reset}")
                break

            Reset()
        except Exception as e:
            Error(e)
            continue

if __name__ == "__main__":
    main()
