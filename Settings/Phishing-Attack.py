from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import os
    import requests
    from bs4 import BeautifulSoup
    import re
    from urllib.parse import urljoin
except Exception as e:
    ErrorModule(e)

Title("Phishing Attack")

try:
    Slow(phishing_banner)
    website_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('Website_url')} -> {reset}")
    Censored(website_url)
    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    def css_and_js(html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('CssRecovery')}")
        css_links = soup.find_all('link', rel='stylesheet')
        all_css = ""

        for link in css_links:
            css_url = urljoin(base_url, link['href'])
            try:
                css_response = requests.get(css_url)
                if css_response.status_code == 200:
                    all_css += css_response.text + "\n"
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorCss')}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorCss')}")
        
        if all_css:
            style_tag = soup.new_tag('style')
            style_tag.string = all_css
            soup.head.append(style_tag)
            for link in css_links:
                link.decompose()

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('JSRecovery')}")
        script_links = soup.find_all('script', src=True)
        all_js = ""

        for script in script_links:
            js_url = urljoin(base_url, script['src'])
            try:
                js_response = requests.get(js_url)
                if js_response.status_code == 200:
                    all_js += js_response.text + "\n"
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorJS')}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('ErrorJS')}")
        
        if all_js:
            script_tag = soup.new_tag('script')
            script_tag.string = all_js
            soup.body.append(script_tag)
            for script in script_links:
                script.decompose()

        return soup.prettify()

    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('HTMLRecovery')}")
    response = requests.get(website_url, timeout=5)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        file_name = re.sub(r'[\\/:*?"<>|]', '-', soup.title.string if soup.title else 'page_sans_titre')

        file_html_relative = f'./1-Output/PhishingAttack/{file_name}.html'
        file_html = os.path.abspath(file_html_relative)

        final_html = css_and_js(html_content, website_url)

        with open(file_html, 'w', encoding='utf-8') as file:
            file.write(final_html)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {tr('PhishingSucces')} \"{secondary}{file_html_relative}{primary}\"")
        Continue()
        Reset()
    else:
        ErrorUrl()
except Exception as e:
    Error(e)