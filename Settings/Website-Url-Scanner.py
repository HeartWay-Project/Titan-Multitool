from Config.Util import *
from Config.Config import *
try:
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import re
except Exception as e:
    ErrorModule(e)

Title("Website Url Scanner")

try:
    all_links = []

    def find_secret_urls(website_url, domain):
        global all_links

        temp_all_links = []

        response = requests.get(website_url)
        if response.status_code != 200:
            pass
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        def is_valid_extension(url):
            return re.search(r'\.(html|xhtml|php|js|css)$', url) or not re.search(r'\.\w+$', url)

        for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe', 'button', 'form']):
            href = tag.get('href')
            src = tag.get('src')
            action = tag.get('action')
            
            if href:
                full_url = urljoin(website_url, href)
                if full_url not in all_links and domain in full_url and is_valid_extension(full_url):
                    temp_all_links.append(full_url)
                    all_links.append(full_url)

            if src:
                full_url = urljoin(website_url, src)
                if full_url not in all_links and domain in full_url and is_valid_extension(full_url):
                    temp_all_links.append(full_url)
                    all_links.append(full_url)

            if action:
                full_url = urljoin(website_url, action)
                if full_url not in all_links and domain in full_url and is_valid_extension(full_url):
                    temp_all_links.append(full_url)
                    all_links.append(full_url)

        for form in soup.find_all('form'):
            action = form.get('action')
            if action:
                full_url = urljoin(website_url, action)
                if full_url not in all_links and domain in full_url and is_valid_extension(full_url):
                    temp_all_links.append(full_url)
                    all_links.append(full_url)

        for script in soup.find_all('script'):
            if script.string:
                urls_in_script = re.findall(r'(https?://\S+)', script.string)
                for url in urls_in_script:
                    if url not in all_links and domain in url and is_valid_extension(url):
                        temp_all_links.append(url)
                        all_links.append(url)

        for link in temp_all_links:
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Url: {secondary}{link}")

    def find_all_secret_urls(website_url, domain):
        find_secret_urls(website_url, domain)

        visited_links = set()
        while True:
            new_links = [link for link in all_links if link not in visited_links]
            if not new_links:
                break
            for link in new_links:
                find_secret_urls(link, domain)
                visited_links.add(link)

    Slow(url_banner)
    website_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Website Url -> {reset}")
    Censored(website_url)

    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url
    domain = re.sub(r'^https?://', '', website_url).split('/')[0]
    
    print(f"""
{secondary}[{invalid}01{secondary}] {invalid}->{secondary} Only "{website_url}"
{secondary}[{invalid}02{secondary}] {invalid}->{secondary} All Website
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Choice -> {reset}")
    print()

    if choice in ['1', '01']:
        find_secret_urls(website_url, domain)

    elif choice in ['2', '02']:
        find_all_secret_urls(website_url, domain)
    
    print()
    Continue()
    Reset()
except Exception as e:
    Error(e)
