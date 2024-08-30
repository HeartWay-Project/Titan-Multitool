from Config.Util import *
from Config.Config import *
try:
    import socket
    import requests
except Exception as e:
    ErrorModule(e)

Title("Website Info Scanner")

try:
    def domain_scan(website_url):
        domain = website_url.replace("https://", "").replace("http://", "").split('/')[0]
        return domain
    
    def secure_scan(website_url):
        if website_url.startswith("https://"):
            secure = True
        else:
            secure = False
        return secure

    def status_scan(website_url):
        try:
            response = requests.get(website_url)
            status_code = response.status_code
        except:
            status_code = 404
        return status_code

    def ip_scan(domain):
        try:
            ip = socket.gethostbyname(domain)
        except:
            ip = "None"

        try:
            response = requests.get(f"https://{website}/api/ip/ip={ip}")
            api = response.json()
            status = api['status']
            host_isp = api['isp']
            host_org = api['org']
            host_as = api['as']
        except:
            status = "Invalid"
            host_isp = "None"
            host_org = "None"
            host_as = "None"

        return ip, status, host_isp, host_org, host_as
    
    def port_scan(ip):
        try:
            open_ports = []
            common_ports = {
                80: "HTTP",
                443: "HTTPS",
                21: "FTP",
                22: "SSH",
                25: "SMTP",
                53: "DNS",
                110: "POP3",
                143: "IMAP",
                3306: "MySQL",
                5432: "PostgreSQL",
                6379: "Redis",
                27017: "MongoDB",
                8080: "HTTP-alt"
            }
            
            for port, service in common_ports.items():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                try:
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        open_ports.append((port, service))
                except:
                    return None
                finally:
                    sock.close()
            return ' / '.join([f'{port}:{service}' for port, service in open_ports])
        except:
            return None

    Slow(scan_banner)
    website_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Website Url -> {reset}")
    Censored(website_url)
        
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..{reset}\n")

    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    print(f"    {INFO_ADD} Website     : {secondary}{website_url}{invalid}")

    domain = domain_scan(website_url)
    print(f"    {INFO_ADD} Domain      : {secondary}{domain}{invalid}")

    secure = secure_scan(website_url)
    print(f"    {INFO_ADD} Secure      : {secondary}{secure}{invalid}")

    status_code = status_scan(website_url)
    print(f"    {INFO_ADD} Status Code : {secondary}{status_code}{invalid}")

    ip, ip_status, host_isp, host_org, host_as = ip_scan(domain)
    print(f"""    {INFO_ADD} Ip          : {secondary}{ip}{invalid}
    {INFO_ADD} Ip Status   : {secondary}{ip_status}{invalid}
    {INFO_ADD} Host Isp    : {secondary}{host_isp}{invalid}
    {INFO_ADD} Host Org    : {secondary}{host_org}{invalid}
    {INFO_ADD} Host As     : {secondary}{host_as}{invalid}""")

    open_port = port_scan(ip)
    print(f"    {INFO_ADD} Open Port   : {secondary}{open_port}{reset}")

    print()
    Continue()
    Reset()

except Exception as e:
    Error(e)