from Config.Util import *
from Config.Config import *

Title("Search DataBase")

try:
    folder_database_relative = "./2-Input/DataBase"
    folder_database = os.path.abspath(folder_database_relative)

    print(f"""
{BEFORE + current_time_hour() + AFTER} {INFO} Add DataBase to the "{secondary}{folder_database_relative}{invalid}" folder.
{BEFORE + current_time_hour() + AFTER} {INFO} If you don't have a DataBase you can get one on the Discord Server "{secondary}{discord_server}{invalid}\".""")
    search = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Search -> {reset}")

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in DataBase..")

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
                                    print(f"""{invalid}
- Folder : {secondary}{folder}{invalid}
- File   : {secondary}{element}{invalid}
- Line   : {secondary}{line_number}{invalid}
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
                                        print(f"""{invalid}
- Folder : {secondary}{folder}{invalid}
- File   : {secondary}{element}{invalid}
- Line   : {secondary}{line_number}{invalid}
- Result : {secondary}{line_info}
    """)
                        except Exception as e:
                            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error reading file \"{secondary}{element}{invalid}\": {secondary}{e}")
                    except Exception as e:
                        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error reading file \"{secondary}{element}{invalid}\": {secondary}{e}")
            return results_found

        results_found = check(folder_database)
        if not results_found:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No result found for \"{secondary}{search}{invalid}\".")

        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Total files searched: {secondary}{files_searched}")

    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during search: {secondary}{e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)