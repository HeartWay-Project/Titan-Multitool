from Config.Util import *
from Config.Config import *
from Config.Translates import *
import requests
import time
import sys
import os

current_language = LANGUAGE

Slow(scan_banner)

def tr(key):
    return translations[current_language].get(key, key)

def load_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

def upload_file_to_virustotal(file_path, api_key):
    url = 'https://www.virustotal.com/api/v3/files'
    headers = {
        'x-apikey': api_key
    }
    files = {
        'file': (file_path, open(file_path, 'rb'))
    }
    response = requests.post(url, headers=headers, files=files)
    response_data = response.json()
    return response_data['data']['id']

def get_analysis_results(file_id, api_key):
    url = f'https://www.virustotal.com/api/v3/analyses/{file_id}'
    headers = {
        'x-apikey': api_key
    }
    while True:
        response = requests.get(url, headers=headers)
        response_data = response.json()
        if response_data['data']['attributes']['status'] == 'completed':
            return response_data
        time.sleep(10)

def display_detailed_results(analysis_results):
    stats = analysis_results['data']['attributes']['stats']
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} Scan results for file:\n")
    print(f"{primary}Harmless: {secondary}{stats['harmless']}")
    print(f"{primary}Malicious: {secondary}{stats['malicious']}")
    print(f"{primary}Suspicious: {secondary}{stats['suspicious']}")
    print(f"{primary}Undetected: {secondary}{stats['undetected']}\n")

    if stats['malicious'] > 0:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{primary} The following antivirus engines detected the file as malicious:\n")
        scans = analysis_results['data']['attributes']['results']
        for engine, result in scans.items():
            if result['category'] == 'malicious':
                print(f"{primary}{engine}: {result['result']}")

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1].strip()
    else:
        file_path = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Path to file to scan -> {secondary}").strip()
    
    if not os.path.isfile(file_path):
        print("The specified file does not exist or is not a valid file.")
        return

    api_key = load_api_key('2-Input/FileCheck/apikey.txt')

    try:
        file_id = upload_file_to_virustotal(file_path, api_key)
        print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} File uploaded successfully. Waiting for analysis...{secondary}")
        analysis_results = get_analysis_results(file_id, api_key)
        display_detailed_results(analysis_results)
        Continue()
        Reset()

    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER}{ERROR}{primary} An error occurred: {e}")

        Continue()
        Reset()

if __name__ == "__main__":
    main()
