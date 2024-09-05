import sys
import argparse
import re
import asyncio
from Config.Util import *
from Config.Config import *
from Config.Translates import *
from email_osg.modules.accounts.adobe import adobe
from email_osg.modules.accounts.twitter import x
from email_osg.modules.accounts.gravatar import gravatar
from email_osg.modules.accounts.spotify import spotify
from email_osg.modules.accounts.duolingo import duolingo
from email_osg.modules.accounts.pinterest import pinterest
from email_osg.modules.accounts.github import github
from email_osg.modules.accounts.strava import strava
from email_osg.modules.accounts.pornhub import pornhub
from email_osg.modules.accounts.chess import chess
from email_osg.modules.accounts.deezer import deezer
from email_osg.modules.accounts.imgur import imgur
from email_osg.modules.accounts.instagram import instagram
from email_osg.modules.accounts.protonmail import protonmail
from email_osg.modules.accounts.flickr import flickr
from email_osg.modules.breaches.pastedumper import Pastebin_Dumper
from email_osg.modules.breaches.hudsonrock import Cavalier
from email_osg.emails_gen import Email_Gen

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

Title("Email Tracker (Osint)")

Slow(osint_banner)

async def perform_search(target):
    EMAIL_REGEX = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
    if re.match(EMAIL_REGEX, target):
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('tool_infos_recovery')}{reset}")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('LeakSearch')}\n{reset}")
        await Pastebin_Dumper(target).paste_check()
        print()
        await Cavalier(target).loader()
        print(f"\n\n{BEFORE + current_time_hour() + AFTER} {INFO} {tr('AccountSearch')}\n{reset}")
        await adobe(target)
        await chess(target)
        deezer(target)
        await duolingo(target)
        await flickr(target)
        await github(target)
        await gravatar(target)
        imgur(target)
        await instagram(target)
        await pinterest(target)
        await protonmail(target)
        pornhub(target)
        await spotify(target)
        await strava(target)
        await x(target)
        print(f"\n\n{BEFORE + current_time_hour() + AFTER} {INFO} Email generation..\n{reset}")
        Email_Gen(target).printer()
    else:
        print(f"{primary}>{secondary} {tr('NotEmail')}")

async def main():
    email = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Email -> {reset}")
    Censored(email)
    print(f"""
{secondary}[{primary}01{secondary}] {primary}->{secondary} {tr('DataBreachSearch')}
    """)
    choice = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('SearchType')} -> {reset}")

    if choice in ['1', '01']:
        await perform_search(email)
    else:
        print(f"{primary}>{secondary} {tr('ErrorChoiceStart')}")

    Continue()
    Reset()

if __name__ == '__main__':
    sys.dont_write_bytecode = True
    py_version = sys.version_info
    py_require = (3, 10)
    if py_version >= py_require:
        asyncio.run(main())
    else:
        exit(f"{primary}>{secondary} {tr('Only3.12')}")
