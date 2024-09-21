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

Title("Discord Token Login")
try:
    print()
    token = Choice1TokenDiscord()

    print(f"\n{secondary}[{primary}01{secondary}]{primary} -> Chrome (Windows / Linux)\n{secondary}[{primary}02{secondary}]{primary} -> Edge (Windows)\n{secondary}[{primary}03{secondary}]{primary} -> Firefox (Windows)\n")
    browser = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('input_browser')}{reset}")

    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('starting').format(navigator)}{primary}")
            driver = webdriver.Chrome()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('ready').format(navigator)}{primary}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('error_driver').format(navigator)}")
            Continue()
            Reset()

    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('starting').format(navigator)}{primary}")
                driver = webdriver.Edge()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('ready').format(navigator)}{primary}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('error_driver').format(navigator)}")
                Continue()
                Reset()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('starting').format(navigator)}{primary}")
                driver = webdriver.Firefox()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('ready').format(navigator)}{primary}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('error_driver').format(navigator)}")
                Continue()
                Reset()
    else:
        ErrorChoice()

    try:
        script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }
                """

        driver.get("https://discord.com/login")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('token_connection')}{primary}")
        driver.execute_script(script + f'\nlogin("{token}")')
        time.sleep(4)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('connected_token')}{primary}")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('leave_tool_warning')}{primary}")
        Continue()
        Reset()
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('error_driver').format(navigator)}")
        Continue()
        Reset()
except Exception as e:
    Error(e)
