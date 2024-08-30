from Config.Util import *
from Config.Config import *
import requests
import re
import sys

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  
        r'(?::\d+)?'  
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def check_url(url, api_key):
    api_url = "https://www.virustotal.com/vtapi/v2/url/report"
    params = {'apikey': api_key, 'resource': url}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        result = response.json()
        if result['response_code'] == 1:
            positives = result['positives']
            total = result['total']
            return positives, total
        else:
            return None, None
    else:
        print("Error querying the API.\n")
        Continue()
        Reset

def get_api_key(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"{ERROR} Error : The file '{filepath}' could not be found.")
        Continue()
        Reset
    except Exception as e:
        Error()

def main():

    Slow(osint_banner)
    api_key_path = "2-Input/FileCheck/apikey.txt"
    api_key = get_api_key(api_key_path)

    url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter a URL to check -> {reset}").strip()
        
    if validate_url(url):
        positives, total = check_url(url, api_key)
        if positives is not None:
            print(f"{INFO} URL : {reset}{url} - {primary}{positives} / {total} scanners detected this URL as malicious.")
        else:
            print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} No results found for this URL.")
            Continue()
            Reset()
    else:
        Continue()
        Reset()

if __name__ == "__main__":
    main()
