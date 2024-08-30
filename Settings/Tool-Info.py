from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Tool Info")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")

    print(f"""
    {INFO_ADD} Name Tool     :  {secondary}{name_tool}
    {INFO_ADD} Version       :  {secondary}{version_tool}
    {INFO_ADD} Copyright     :  {secondary}{copyright}
    {INFO_ADD} Coding        :  {secondary}{coding_tool}
    {INFO_ADD} Language      :  {secondary}{language_tool}
    {INFO_ADD} Creator       :  {secondary}{creator}
    {INFO_ADD} Platform      :  {secondary}{platform}
    {INFO_ADD} Discord  [02] :  {secondary}https://{discord_server}
    {INFO_ADD} Site     [02] :  {secondary}https://{website}
    {INFO_ADD} GitHub   [02] :  {secondary}https://{github_tool}
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