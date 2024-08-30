import os
import sys
import ctypes
from Config.Util import *
from Config.Config import *

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print(f"\n{WAIT} Launching the order as administrator...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit()

confirmation = input(f"{INPUT} Would you like to activate winrar premium? (y/n): ").strip().lower()

if confirmation == 'y':
    winrar_dir = "C:\\Program Files\\WinRAR"
    key_file_path = os.path.join(winrar_dir, "rarreg.key")

    key_content = """RAR registration data
Hardik
www.Hardik.live
UID=448c4a899c6cdc1039c5
641221225039c585fc5ef8da12ccf689780883109587752a828ff0
59ae0579fe68942c97d160f361d16f96c8fe03f1f89c66abc25a37
7777a27ec82f103b3d8e05dcefeaa45c71675ca822242858a1c897
c57d0b0a3fe7ac36c517b1d2be385dcc726039e5f536439a806c35
1e180e47e6bf51febac6eaae111343d85015dbd59ba45c71675ca8
2224285927550547c74c826eade52bbdb578741acc1565af60e326
6b5e5eaa169647277b533e8c4ac01535547d1dee14411061928023
"""

    try:
        with open(key_file_path, "w") as key_file:
            key_file.write(key_content)
        print(f"\nWinrar activated successfully")
    except Exception as e:
        print(f"\nError during activation {key_file_path}: {e}")
else:
    print("\nOpération annulée.")
