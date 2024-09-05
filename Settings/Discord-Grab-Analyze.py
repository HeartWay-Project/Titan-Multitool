import os
import re
import requests
import colorama
from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

Title(f"PC Grab Analyze")

def find_python_files():
    python_files = []
    for root, _, files in os.walk('/'):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def scan_file_for_webhook(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            webhook_pattern = r'https://discord.com/api/webhooks/\d{18}/[A-Za-z0-9_\-]{68}'
            if re.search(webhook_pattern, content):
                return True
    except (OSError, UnicodeDecodeError):
        pass
    return False

def generate_report(files_status):
    report = f"{secondary}{tr('AnalyzeRapport')}\n{reset}"
    safe_files = [file for file, status in files_status.items() if status == "safe"]
    suspect_files = [file for file, status in files_status.items() if status == "suspect"]
    
    for file in safe_files:
        report += f"{os.path.basename(file)} : {primary}safe{reset}\n"
    
    for file in suspect_files:
        report += f"{file} : {invalid}suspect{reset}\n"
    
    return report

def ask_for_confirmation():
    response = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('StartAnalyze')} -> {reset}").strip().lower()
    return response == 'y'

def main():

    if ask_for_confirmation():
        python_files = find_python_files()
        files_status = {}

        for file in python_files:
            if scan_file_for_webhook(file):
                files_status[file] = "suspect"
            else:
                files_status[file] = "safe"

        report = generate_report(files_status)
        print(report)
        Continue()
        Reset()
    else:
        print(f"{primary}{tr('AnalysisCancel')}.{reset}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Error(e)
