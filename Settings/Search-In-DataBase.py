from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

Title("Search DataBase")

try:
    folder_database_relative = "./2-Input/DataBase"
    folder_database = os.path.abspath(folder_database_relative)

    print(f"""
{BEFORE + current_time_hour() + AFTER} {INFO} {tr('AddDB1')} "{secondary}{folder_database_relative}{primary}".
{BEFORE + current_time_hour() + AFTER} {INFO} {tr('NoDB')} "{secondary}{discord_server}{primary}\".""")
    search = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('Search')} -> {reset}")

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('DBSearch')}")

    def TitleSearch(files_searched, element):
        Title(f"Search DataBase | Total: {files_searched} | File: {element}")

    try:
        files_searched = 0

        def check(folder):
            global files_searched
            results_found = False
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in {secondary}{folder}")
            for element in os.listdir(folder):
                chemin_element = os.path.join(folder, element)
                if os.path.isdir(chemin_element):
                    check(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, 'r', encoding='utf-8') as file:
                            line_number = 0
                            files_searched += 1
                            TitleSearch(files_searched, element)
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(search, f"{color.YELLOW}{search}{secondary}")
                                    print(f"""{primary}
- Folder : {secondary}{folder}{primary}
- File   : {secondary}{element}{primary}
- Line   : {secondary}{line_number}{primary}
- Result : {secondary}{line_info}
    """)
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, 'r', encoding='latin-1') as file:
                                files_searched += 1
                                line_number = 0
                                TitleSearch(files_searched, element)
                                for line in file:
                                    line_number += 1
                                    if search in line:
                                        results_found = True
                                        line_info = line.strip().replace(search, f"{color.YELLOW}{search}{secondary}")
                                        print(f"""{primary}
- Folder : {secondary}{folder}{primary}
- File   : {secondary}{element}{primary}
- Line   : {secondary}{line_number}{primary}
- Result : {secondary}{line_info}
    """)
                        except Exception as e:
                            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorReadFile')} \"{secondary}{element}{primary}\": {secondary}{e}")
                    except Exception as e:
                        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorReadFile')} \"{secondary}{element}{primary}\": {secondary}{e}")
            return results_found

        results_found = check(folder_database)
        if not results_found:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('NoResultSearch')} \"{secondary}{search}{primary}\".")

        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('TotalSearchFile')} {secondary}{files_searched}")

    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorSearch')} {secondary}{e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)