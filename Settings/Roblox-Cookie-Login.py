from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    from selenium import webdriver
except Exception as e:
   ErrorModule(e)
   

Title("Roblox Cookie Login")

try:

    cookie = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {secondary}")
    print(f"""
{secondary}[{invalid}01{secondary}] {invalid}->{secondary} Chrome (Windows / Linux)
{secondary}[{invalid}02{secondary}] {invalid}->{secondary} Edge (Windows)
{secondary}[{invalid}03{secondary}] {invalid}->{secondary} Firefox (Windows)
    """)
    browser = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('Choice')} -> {reset}")
 
    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} {tr('starting')}{primary}")
            driver = webdriver.Chrome()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} {tr('ready')}{primary}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} {tr('error_driver')}")
            Continue()
            Reset()

    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} {tr('starting')}{primary}")
                driver = webdriver.Edge()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} {tr('ready')}{primary}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} {tr('error_driver')}")
                Continue()
                Reset()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} {tr('starting')}{primary}")
                driver = webdriver.Firefox()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} {tr('ready')}{primary}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} {tr('error_driver')}")
                Continue()
                Reset()
    else:
        ErrorChoice()
    
    try:
        driver.get("https://www.roblox.com/Login")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Cookie Connection..{primary}")
        driver.add_cookie({"name" : ".ROBLOSECURITY", "value" : f"{cookie}"})
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Connected Cookie !{primary}")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Refresh The Page..{primary}")
        driver.refresh()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Connected !{primary}")
        time.sleep(1)
        driver.get("https://www.roblox.com/users/profile")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('leave_tool_warning')}{primary}")
        Continue()
        Reset()
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} {tr('error_driver')}")
        Continue()
        Reset()
except Exception as e:
    Error(e)