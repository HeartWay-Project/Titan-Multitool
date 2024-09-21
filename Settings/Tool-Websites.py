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

Title("Tool Website")
print(f"""
{secondary}[{primary}01{secondary}] {primary}->{secondary} {tr('Web_Site')}
{secondary}[{primary}02{secondary}] {primary}->{secondary} Discord
{secondary}[{primary}03{secondary}] {primary}->{secondary} Github
""")

try:
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {color.RESET}")
    if choice in ['1', '01']:
        site = f"{website}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('Site_Acces')} \"{secondary}{site}{primary}\"" + color.RESET)
        Continue()
        Reset()
    if choice in ['2', '02']:
        site = f"https://{discord_server}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('Discord_Acces')} \"{secondary}{site}{primary}\"" + color.RESET)
        Continue()
        Reset()

    if choice in ['3', '03']:
        site = f"https://{github_tool}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('Site_Acces')} \"{secondary}{site}{primary}\"" + color.RESET)
        Continue()
        Reset()

except Exception as e:
    Error(e)