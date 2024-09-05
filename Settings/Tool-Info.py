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

Title("Tool Info")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('tool_infos_recovery')}{reset}")

    print(f"""
    {INFO_ADD} {tr('Name_Tool')}     :  {secondary}{name_tool}
    {INFO_ADD} Version         :  {secondary}{version_tool}
    {INFO_ADD} Copyright       :  {secondary}{copyright}
    {INFO_ADD} {tr('Coding')}        :  {secondary}{coding_tool}
    {INFO_ADD} {tr('Language')}      :  {secondary}{language_tool}
    {INFO_ADD} {tr('Creator')}       :  {secondary}{creator}
    {INFO_ADD} {tr('Platform')}      :  {secondary}{platform}
    {INFO_ADD} Discord         :  {secondary}https://{discord_server}
    {INFO_ADD} Site            :  {secondary}https://{website}
    {INFO_ADD} GitHub          :  {secondary}https://{github_tool}
    {reset}""")

    license_read = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open 'LICENSE' ? (y/n) -> {reset}")
    if license_read in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webbrowser.open_new_tab(license)
    else:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)