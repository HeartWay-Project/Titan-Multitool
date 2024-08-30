from Settings.Config.Config import *
from Settings.Config.Util import *

try:
   import webbrowser
   import re
   import colorama
except:
   ErrorModule()

colorama.init()


#try:
#   content = requests.get(url_config).text
#   match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
#   current_version = match.group(1)
#   if current_version != version_tool:
#      print(f"{INFO} Please download the new version of the tool ! {secondary}{version_tool}{color.LIGHTYELLOW_EX} -> {secondary}{current_version}{primary}")
#      webbrowser.open(github_tool)
#      input(f"{INFO} Enter to still use this version -> {reset}")
#      popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {secondary}{version_tool}{color.LIGHTYELLOW_EX} -> {secondary}{current_version}{primary}"
#   else:
#      popup_version = ""
#except:
popup_version = ""

option_01 = "Parameters"
option_02 = "Tool-Info"
option_03 = "Tool-Websites"
option_04 = "Website-Info-Scanner"
option_05 = "Website-Url-Scanner"
option_06 = "URL-Checker"
option_07 = "Search-In-DataBase"
option_08 = "Get-Your-Ip"
option_09 = "Ip-Info"
option_10 = "Ip-Port-Scanner"
option_11 = "Ip-Pinger"
option_12 = "Ip-Generator"
option_13 = "Ip-Scanner"
option_14 = "Obfuscator"
option_15 = "Virus-Builder"
option_16 = "RAT-Builder"
option_17 = "Sql-Vulnerability"
option_18 = "Phishing-Attack"
option_19 = "Dox-Create"
option_20 = "Dox-Tracker-(Osint)"
option_21 = "Username-Tracker"
option_22 = "Email-Tracker"
option_23 = "Email-Info"
option_24 = "Number-Info"
option_25 = "Password-Encrypted"
option_26 = "Password-Decrypted"
option_27 = "Password-Checker"
option_28 = "Password-Generator"
option_29 = "Password-Generator-(Random)"
option_30 = "Archive-Cracker"
option_31 = "SMB-Cracker" 
option_32 = "Discord-Token-Info"
option_33 = "Discord-Token-Nuker"
option_34 = "Discord-Token-Joiner"
option_35 = "Discord-Token-Leaver"
option_36 = "Discord-Token-Login"
option_37 = "Discord-Token-To-Id-And-Brute"
option_38 = "Discord-Token-Server-Raid"
option_39 = "Discord-Token-Spammer"
option_40 = "Discord-Token-Delete-Friends"
option_41 = "Discord-Token-Block-Friends"
option_42 = "Discord-Token-Mass-Dm"
option_43 = "Discord-Token-Delete-Dm"
option_44 = "Discord-Token-Status-Changer"
option_45 = "Discord-Token-Language-Changer"
option_46 = "Discord-Token-House-Changer"
option_47 = "Discord-Token-Theme-Changer"
option_48 = "Discord-Token-Generator"
option_49 = "Discord-Bot-Server-Backup"
option_50 = "Discord-Bot-Server-Nuker"
option_51 = "Discord-Bot-Server-Invite"
option_52 = "Discord-Bot-Id-to-Invite"
option_53 = "Discord-Server-Info"
option_54 = "Discord-Nitro-Generator"
option_55 = "Discord-Webhook-Info"
option_56 = "Discord-Webhook-Delete"
option_57 = "Discord-Webhook-Spammer"
option_58 = "Discord-Webhook-Generator"
option_59 = "Discord-Id-to-Token-First-Part"
option_60 = "Discord-Grab-Analyze"
option_61 = "Roblox-Cookie-Login"
option_62 = "Roblox-Cookie-Info"
option_63 = "Roblox-User-Info"
option_64 = "Roblox-Id-Info"
option_65 = "Roblox-Robux-Generator"
option_66 = "File-Encryptor"
option_67 = "File-Decryptor"
option_68 = "File-Converter"
option_69 = "File-Scanner"
option_70 = "Facebook-Downloader"
option_71 = "Youtube-Downloader"
option_72 = "TikTok-Downloader"
option_73 = "Site-Downloader"
option_74 = "Dark-Web-Links"
option_75 = "Steganography"
option_76 = "Metadata"
option_77 = "Spoofer"
option_78 = "Winrar-Premium"
option_79 = "Soon"
option_80 = "Soon"
option_81 = "Soon" 
option_82 = "Soon"
option_83 = "Soon"
option_84 = "Soon"
option_85 = "Soon"
option_86 = "Soon"
option_87 = "Soon"
option_88 = "Soon"
option_89 = "Soon"
option_90 = "Soon"
option_91 = "Soon"
option_92 = "Soon"

option_next = "Next Page >>"
option_previous = "<< Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = option_29.ljust(30)[:30].replace("-", " ")
option_30_txt = option_30.ljust(30)[:30].replace("-", " ")
option_31_txt = option_31.ljust(30)[:30].replace("-", " ")
option_32_txt = option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = option_39.ljust(30)[:30].replace("-", " ")
option_40_txt = option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = option_49.ljust(30)[:30].replace("-", " ")
option_50_txt = option_50.ljust(30)[:30].replace("-", " ")
option_51_txt = option_51.ljust(30)[:30].replace("-", " ")
option_52_txt = option_52.ljust(30)[:30].replace("-", " ")
option_53_txt = option_53.ljust(30)[:30].replace("-", " ")
option_54_txt = option_54.ljust(30)[:30].replace("-", " ")
option_55_txt = option_55.ljust(30)[:30].replace("-", " ")
option_56_txt = option_56.ljust(30)[:30].replace("-", " ")
option_57_txt = option_57.ljust(30)[:30].replace("-", " ")
option_58_txt = option_58.ljust(30)[:30].replace("-", " ")
option_59_txt = option_59.ljust(30)[:30].replace("-", " ")
option_60_txt = option_60.ljust(30)[:30].replace("-", " ")
option_61_txt = option_61.ljust(30)[:30].replace("-", " ")
option_62_txt = option_62.ljust(30)[:30].replace("-", " ")
option_63_txt = option_63.ljust(30)[:30].replace("-", " ")
option_64_txt = option_64.ljust(30)[:30].replace("-", " ")
option_65_txt = option_65.ljust(30)[:30].replace("-", " ")
option_66_txt = option_66.ljust(30)[:30].replace("-", " ")
option_67_txt = option_67.ljust(30)[:30].replace("-", " ")
option_68_txt = option_68.ljust(30)[:30].replace("-", " ")
option_69_txt = option_69.ljust(30)[:30].replace("-", " ")
option_70_txt = option_70.ljust(30)[:30].replace("-", " ")
option_71_txt = option_71.ljust(30)[:30].replace("-", " ")
option_72_txt = option_72.ljust(30)[:30].replace("-", " ")
option_73_txt = option_73.ljust(30)[:30].replace("-", " ")
option_74_txt = option_74.ljust(30)[:30].replace("-", " ")
option_75_txt = option_75.ljust(30)[:30].replace("-", " ")
option_76_txt = option_76.ljust(30)[:30].replace("-", " ")
option_77_txt = option_77.ljust(30)[:30].replace("-", " ")
option_78_txt = option_78.ljust(30)[:30].replace("-", " ")
option_79_txt = option_79.ljust(30)[:30].replace("-", " ")
option_80_txt = option_80.ljust(30)[:30].replace("-", " ")
option_81_txt = option_81.ljust(30)[:30].replace("-", " ")
option_82_txt = option_82.ljust(30)[:30].replace("-", " ")
option_83_txt = option_83.ljust(30)[:30].replace("-", " ")
option_84_txt = option_84.ljust(30)[:30].replace("-", " ")
option_85_txt = option_85.ljust(30)[:30].replace("-", " ")
option_86_txt = option_86.ljust(30)[:30].replace("-", " ")
option_87_txt = option_87.ljust(30)[:30].replace("-", " ")
option_88_txt = option_88.ljust(30)[:30].replace("-", " ")
option_89_txt = option_89.ljust(30)[:30].replace("-", " ")
option_90_txt = option_90.ljust(30)[:30].replace("-", " ")
option_91_txt = option_91.ljust(30)[:30].replace("-", " ")
option_92_txt = option_92.ljust(30)[:30].replace("-", " ")

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

menu1 = f"""                                                 {secondary}╔════════════╗
                                                    {secondary}║ {primary}Multi-Tool{secondary} ║
   {primary}┌────────┐                                       {secondary}╚════════════╝
   {primary}│{secondary}Menu n°1{primary}│
   {primary}├────────┴───────────────────────────┬────────────────────────────────────┬────────────────────────────────────┐
   {primary}├{secondary}[{primary}01{secondary}]{primary}-{secondary} {option_01_txt}{primary}├{secondary}[{primary}11{secondary}]{primary}-{secondary} {option_11_txt}{primary}├{secondary}[{primary}21{secondary}]{primary}-{secondary} {option_21_txt}{primary}│
   {primary}├{secondary}[{primary}02{secondary}]{primary}-{secondary} {option_02_txt}{primary}├{secondary}[{primary}12{secondary}]{primary}-{secondary} {option_12_txt}{primary}├{secondary}[{primary}22{secondary}]{primary}-{secondary} {option_22_txt}{primary}│
   {primary}├{secondary}[{primary}03{secondary}]{primary}-{secondary} {option_03_txt}{primary}├{secondary}[{primary}13{secondary}]{primary}-{secondary} {option_13_txt}{primary}├{secondary}[{primary}23{secondary}]{primary}-{secondary} {option_23_txt}{primary}│
   {primary}├{secondary}[{primary}04{secondary}]{primary}-{secondary} {option_04_txt}{primary}├{secondary}[{primary}14{secondary}]{primary}-{secondary} {option_14_txt}{primary}├{secondary}[{primary}24{secondary}]{primary}-{secondary} {option_24_txt}{primary}│
   {primary}├{secondary}[{primary}05{secondary}]{primary}-{secondary} {option_05_txt}{primary}├{secondary}[{primary}15{secondary}]{primary}-{secondary} {option_15_txt}{primary}├{secondary}[{primary}25{secondary}]{primary}-{secondary} {option_25_txt}{primary}│
   {primary}├{secondary}[{primary}06{secondary}]{primary}-{secondary} {option_06_txt}{primary}├{secondary}[{primary}16{secondary}]{primary}-{secondary} {option_16_txt}{primary}├{secondary}[{primary}26{secondary}]{primary}-{secondary} {option_26_txt}{primary}│
   {primary}├{secondary}[{primary}07{secondary}]{primary}-{secondary} {option_07_txt}{primary}├{secondary}[{primary}17{secondary}]{primary}-{secondary} {option_17_txt}{primary}├{secondary}[{primary}27{secondary}]{primary}-{secondary} {option_27_txt}{primary}│
   {primary}├{secondary}[{primary}08{secondary}]{primary}-{secondary} {option_08_txt}{primary}├{secondary}[{primary}18{secondary}]{primary}-{secondary} {option_18_txt}{primary}├{secondary}[{primary}28{secondary}]{primary}-{secondary} {option_28_txt}{primary}│
   {primary}├{secondary}[{primary}09{secondary}]{primary}-{secondary} {option_09_txt}{primary}├{secondary}[{primary}19{secondary}]{primary}-{secondary} {option_19_txt}{primary}├{secondary}[{primary}29{secondary}]{primary}-{secondary} {option_29_txt}{primary}│
   {primary}├{secondary}[{primary}10{secondary}]{primary}-{secondary} {option_10_txt}{primary}├{secondary}[{primary}20{secondary}]{primary}-{secondary} {option_20_txt}{primary}├{secondary}[{primary}30{secondary}]{primary}-{secondary} {option_30_txt}{primary}│
   └────────────────────────────────────┴────────────────────────────────────┼────────────────────────────────────┤
                                                                             │{secondary}[{primary}e{secondary}]{primary}- {option_next_txt} │
                                                                             └────────────────────────────────────┘
{primary}┌───({secondary}{username_pc}@Titan{primary})─[{secondary}~/HeartWay/Menu-1{primary}]""".replace("(Osint)", f"{primary}(Osint){secondary}").replace("(Lookup)", f"{primary}(Lookup){secondary}").replace("(Stealer, Malware)", f"{primary}(Stealer, Malware){secondary}").replace("(Paid)", f"{primary}(Paid){secondary}")

menu2 = f"""                                                 {secondary}╔════════════╗
                                                    {secondary}║ {primary}Multi-Tool{secondary} ║
   {primary}┌────────┐                                       {secondary}╚════════════╝
   {primary}│{secondary}Menu n°2{primary}│
   {primary}├────────┴───────────────────────────┬────────────────────────────────────┬────────────────────────────────────┐
   {primary}├{secondary}[{primary}31{secondary}]{primary}-{secondary} {option_31_txt}{primary}├{secondary}[{primary}41{secondary}]{primary}-{secondary} {option_41_txt}{primary}├{secondary}[{primary}51{secondary}]{primary}-{secondary} {option_51_txt}{primary}│
   {primary}├{secondary}[{primary}32{secondary}]{primary}-{secondary} {option_32_txt}{primary}├{secondary}[{primary}42{secondary}]{primary}-{secondary} {option_42_txt}{primary}├{secondary}[{primary}52{secondary}]{primary}-{secondary} {option_52_txt}{primary}│
   {primary}├{secondary}[{primary}33{secondary}]{primary}-{secondary} {option_33_txt}{primary}├{secondary}[{primary}43{secondary}]{primary}-{secondary} {option_43_txt}{primary}├{secondary}[{primary}53{secondary}]{primary}-{secondary} {option_53_txt}{primary}│
   {primary}├{secondary}[{primary}34{secondary}]{primary}-{secondary} {option_34_txt}{primary}├{secondary}[{primary}44{secondary}]{primary}-{secondary} {option_44_txt}{primary}├{secondary}[{primary}54{secondary}]{primary}-{secondary} {option_54_txt}{primary}│
   {primary}├{secondary}[{primary}35{secondary}]{primary}-{secondary} {option_35_txt}{primary}├{secondary}[{primary}45{secondary}]{primary}-{secondary} {option_45_txt}{primary}├{secondary}[{primary}55{secondary}]{primary}-{secondary} {option_55_txt}{primary}│
   {primary}├{secondary}[{primary}36{secondary}]{primary}-{secondary} {option_36_txt}{primary}├{secondary}[{primary}46{secondary}]{primary}-{secondary} {option_46_txt}{primary}├{secondary}[{primary}56{secondary}]{primary}-{secondary} {option_56_txt}{primary}│
   {primary}├{secondary}[{primary}37{secondary}]{primary}-{secondary} {option_37_txt}{primary}├{secondary}[{primary}47{secondary}]{primary}-{secondary} {option_47_txt}{primary}├{secondary}[{primary}57{secondary}]{primary}-{secondary} {option_57_txt}{primary}│
   {primary}├{secondary}[{primary}38{secondary}]{primary}-{secondary} {option_38_txt}{primary}├{secondary}[{primary}48{secondary}]{primary}-{secondary} {option_48_txt}{primary}├{secondary}[{primary}58{secondary}]{primary}-{secondary} {option_58_txt}{primary}│
   {primary}├{secondary}[{primary}39{secondary}]{primary}-{secondary} {option_39_txt}{primary}├{secondary}[{primary}49{secondary}]{primary}-{secondary} {option_49_txt}{primary}├{secondary}[{primary}59{secondary}]{primary}-{secondary} {option_59_txt}{primary}│
   {primary}├{secondary}[{primary}40{secondary}]{primary}-{secondary} {option_40_txt}{primary}├{secondary}[{primary}50{secondary}]{primary}-{secondary} {option_50_txt}{primary}├{secondary}[{primary}60{secondary}]{primary}-{secondary} {option_60_txt}{primary}│
   ├────────────────────────────────────┼────────────────────────────────────┼────────────────────────────────────┤
   │{secondary}[{primary}a{secondary}]{primary}- {option_previous_txt} │                                    │{secondary}[{primary}d{secondary}]{primary}- {option_next_txt} │
   └────────────────────────────────────┘                                    └────────────────────────────────────┘
{primary}┌───({secondary}{username_pc}@Titan{primary})─[{secondary}~/HeartWay/Menu-2{primary}]""".replace("(Osint)", f"{primary}(Osint){secondary}").replace("(Lookup)", f"{primary}(Lookup){secondary}").replace("(Stealer, Malware)", f"{primary}(Stealer, Malware){secondary}").replace("(Paid)", f"{primary}(Paid){secondary}")

menu3 = f"""                                                 {secondary}╔════════════╗
                                                    {secondary}║ {primary}Multi-Tool{secondary} ║
   {primary}┌────────┐                                       {secondary}╚════════════╝
   {primary}│{secondary}Menu n°3{primary}│
   {primary}├────────┴───────────────────────────┬────────────────────────────────────┬────────────────────────────────────┐
   {primary}├{secondary}[{primary}61{secondary}]{primary}-{secondary} {option_61_txt}{primary}├{secondary}[{primary}71{secondary}]{primary}-{secondary} {option_71_txt}{primary}├{secondary}[{primary}81{secondary}]{primary}-{secondary} {option_81_txt}{primary}│
   {primary}├{secondary}[{primary}62{secondary}]{primary}-{secondary} {option_62_txt}{primary}├{secondary}[{primary}72{secondary}]{primary}-{secondary} {option_72_txt}{primary}├{secondary}[{primary}82{secondary}]{primary}-{secondary} {option_82_txt}{primary}│
   {primary}├{secondary}[{primary}63{secondary}]{primary}-{secondary} {option_63_txt}{primary}├{secondary}[{primary}73{secondary}]{primary}-{secondary} {option_73_txt}{primary}├{secondary}[{primary}83{secondary}]{primary}-{secondary} {option_83_txt}{primary}│
   {primary}├{secondary}[{primary}64{secondary}]{primary}-{secondary} {option_64_txt}{primary}├{secondary}[{primary}74{secondary}]{primary}-{secondary} {option_74_txt}{primary}├{secondary}[{primary}84{secondary}]{primary}-{secondary} {option_84_txt}{primary}│
   {primary}├{secondary}[{primary}65{secondary}]{primary}-{secondary} {option_65_txt}{primary}├{secondary}[{primary}75{secondary}]{primary}-{secondary} {option_75_txt}{primary}├{secondary}[{primary}85{secondary}]{primary}-{secondary} {option_85_txt}{primary}│
   {primary}├{secondary}[{primary}66{secondary}]{primary}-{secondary} {option_66_txt}{primary}├{secondary}[{primary}76{secondary}]{primary}-{secondary} {option_76_txt}{primary}├{secondary}[{primary}86{secondary}]{primary}-{secondary} {option_86_txt}{primary}│
   {primary}├{secondary}[{primary}67{secondary}]{primary}-{secondary} {option_67_txt}{primary}├{secondary}[{primary}77{secondary}]{primary}-{secondary} {option_77_txt}{primary}├{secondary}[{primary}87{secondary}]{primary}-{secondary} {option_87_txt}{primary}│
   {primary}├{secondary}[{primary}68{secondary}]{primary}-{secondary} {option_68_txt}{primary}├{secondary}[{primary}78{secondary}]{primary}-{secondary} {option_78_txt}{primary}├{secondary}[{primary}88{secondary}]{primary}-{secondary} {option_88_txt}{primary}│
   {primary}├{secondary}[{primary}69{secondary}]{primary}-{secondary} {option_69_txt}{primary}├{secondary}[{primary}79{secondary}]{primary}-{secondary} {option_79_txt}{primary}├{secondary}[{primary}89{secondary}]{primary}-{secondary} {option_89_txt}{primary}│
   {primary}├{secondary}[{primary}70{secondary}]{primary}-{secondary} {option_70_txt}{primary}├{secondary}[{primary}80{secondary}]{primary}-{secondary} {option_80_txt}{primary}├{secondary}[{primary}90{secondary}]{primary}-{secondary} {option_90_txt}{primary}│
   ├────────────────────────────────────┼────────────────────────────────────┼────────────────────────────────────┤
   │{secondary}[{primary}q{secondary}]{primary}- {option_previous_txt} │                                    │{secondary}[{primary}c{secondary}]{primary}- {option_next_txt} │
   └────────────────────────────────────┘                                    └────────────────────────────────────┘
{primary}┌───({secondary}{username_pc}@Titan{primary})─[{secondary}~/HeartWay/Menu-3{primary}]""".replace("(Osint)", f"{primary}(Osint){secondary}").replace("(Lookup)", f"{primary}(Lookup){secondary}").replace("(Stealer, Malware)", f"{primary}(Stealer, Malware){secondary}").replace("(Paid)", f"{primary}(Paid){secondary}")

def Menu():
   try:
      with open("./Settings/Config/Menu.txt", "r") as file:
         menu = file.read()
      if menu in ["1"]:
         menu = menu1
         Title("Menu 1")
      elif menu in ["2"]:
         menu = menu2
         Title("Menu 2")
      elif menu in ["3"]:
         menu = menu3
         Title("Menu 3")
      else:
         menu = menu1
         Title("Menu 1")
   except:
      menu = menu1
      Title("Menu 1")

   banner = f"""{popup_version}{primary}                             
{primary}                                     ███      ▄█      ███        ▄████████ ███▄▄▄▄       ┌─────────────────────────────┐
{primary}                                 ▀█████████▄ ███  ▀█████████▄   ███    ███ ███▀▀▀██▄     │ {secondary}{github_tool} {primary}│
{primary}                                    ▀███▀▀██ ███▌    ▀███▀▀██   ███    ███ ███   ███     └─────────────────────────────┘
{primary}                                     ███   ▀ ███▌     ███   ▀   ███    ███ ███   ███ 
{primary}                                     ███     ███▌     ███     ▀███████████ ███   ███ 
{primary}                                     ███     ███      ███       ███    ███ ███   ███ 
{primary}                                     ███     ███      ███       ███    ███ ███   ███ 
{primary}                                   ▄████▀   █▀      ▄████▀     ███    █▀   ▀█   █▀  
                                                    
   {menu}"""
   return banner


while True:
   try:
      Clear()
      Slow(Menu())
      choice = input(f"""└──{secondary}$ {reset}""")

      options = {
         'e': option_next, 'd': option_next, 'a': option_previous, 'q': option_previous,
         '1': option_01, '2': option_02, '3': option_03, '4': option_04,
         '5': option_05, '6': option_06, '7': option_07, '8': option_08,
         '9': option_09, '10': option_10, '11': option_11, '12': option_12,
         '13': option_13, '14': option_14, '15': option_15, '16': option_16,
         '17': option_17, '18': option_18, '19': option_19, '20': option_20,
         '21': option_21, '22': option_22, '23': option_23, '24': option_24,
         '25': option_25, '26': option_26, '27': option_27, '28': option_28,
         '29': option_29, '30': option_next, '31': option_previous, '32': option_32,
         '33': option_33, '34': option_34, '35': option_35, '36': option_36,
         '37': option_37, '38': option_38, '39': option_39, '40': option_40,
         '41': option_41, '42': option_42, '43': option_43, '44': option_44,
         '45': option_45, '46': option_46, '47': option_47, '48': option_48,
         '49': option_49, '50': option_50, '51': option_51, '52': option_52,
         '53': option_53, '54': option_54, '55': option_55, '56': option_56,
         '57': option_57, '58': option_58, '59': option_59, '60': option_next,
         '61': option_previous, '62': option_62, '63': option_63, '64': option_64,
         '65': option_65, '66': option_66, '67': option_67, '68': option_68,
         '69': option_69, '70': option_70, '71': option_71, '72': option_72,
         '73': option_73, '74': option_74, '75': option_75, '76': option_76,
         '77': option_77, '78': option_78, '79': option_79, '80': option_next,
         '81': option_previous, '82': option_82, '83': option_83, '84': option_84,
         '85': option_85, '86': option_86, '87': option_87, '88': option_88,
         '89': option_89, '90': option_next, '91': option_91, '92': option_92,
      }

      if choice in options:
          if choice in ['e']:
              menu = menu2
              with open("./Settings/Config/Menu.txt", "w") as file:
                  file.write("2")
              Title("Menu 2")
          elif choice in ['a']:
              menu = menu1
              with open("./Settings/Config/Menu.txt", "w") as file:
                  file.write("1")
              Title("Menu 1")
          elif choice in ['d']:
              menu = menu3
              with open("./Settings/Config/Menu.txt", "w") as file:
                  file.write("3")
              Title("Menu 3")
          elif choice in ['q']:
              menu = menu2
              with open("./Settings/Config/Menu.txt", "w") as file:
                  file.write("2")
              Title("Menu 2")
          else:
              StartProgram(f"{options[choice]}.py")
      else:
          ErrorChoiceStart()
         
   except Exception as e:
      Error(e)