from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import requests
    import subprocess
    import socket
    import concurrent.futures
except Exception as e:
   ErrorModule(e)
   
Title("Ip Info (Lookup)")

try:


    def ping_ip(ip):
        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
            elif sys.platform.startswith("linux"):
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
            if result.returncode == 0:
                ping = "Succeed"
            else:
                ping = "Fail"
        except:
            ping = "Fail"

        print(f"    {INFO_ADD} Ping         : {secondary}{ping}{invalid}")

    open_ports = []

    def port_ip(ip):
        def scan_port(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(scan_port, ip, port): port for port in range(1, 1000 + 1)}
        concurrent.futures.wait(results)

        print(f"    {INFO_ADD} {tr('Open_Ports')}  : {secondary}{open_ports}{primary}")

    def dns_ip(ip):
        try:
            dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except:
            dns = "None"
        print(f"    {INFO_ADD} DNS          : {secondary}{dns}{primary}")


    def info_ip(ip):
        try:
            response = requests.get(f"http://ipinfo.io/{ip}/json")
            api = response.json()

            ip = api['ip']
            status = api['status']
            country = api['country']
            country_code = api['country_code']
            region = api['region']
            region_code = api['region_code']
            zip = api['zip']
            city = api['city']
            latitude = api['latitude']
            longitude = api['longitude']
            timezone = api['timezone']
            isp = api['isp']
            org = api['org']
            as_host = api['as']
            loc_url = api['loc_url']
            credit = api['credit']
            copyright = api['copyright']

        except:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            api = response.json()

            try:
                if api['status'] == "success": status = "Valid"
                else: status = "Invalid"
            except: 
                status = "Invalid"

            try: country = api['country']
            except: country = "None"
            try: country_code = api['countryCode']
            except: country_code = "None"
            try: region = api['regionName']
            except: region = "None"
            try: region_code = api['region']
            except: region_code = "None"
            try: zip = api['zip']
            except: zip = "None"
            try: city = api['city']
            except: city = "None"
            try: latitude = api['lat']
            except: latitude = "None"
            try: longitude = api['lon']
            except: longitude = "None"
            try: timezone = api['timezone']
            except: timezone = "None"
            try: isp = api['isp']
            except: isp = "None"
            try: org = api['org']
            except: org = "None"
            try: as_host = api['as']
            except: as_host = "None"
            loc_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

        Slow(f"""    {INFO_ADD} Status       : {secondary}{status}{invalid}
    {INFO_ADD} {tr('Country')}    : {secondary}{country} ({country_code}){invalid}
    {INFO_ADD} Region       : {secondary}{region} ({region_code}){invalid}
    {INFO_ADD} Zip          : {secondary}{zip}{invalid}
    {INFO_ADD} {tr('City')}       : {secondary}{city}{invalid}
    {INFO_ADD} Latitude     : {secondary}{latitude}{invalid}
    {INFO_ADD} Longitude    : {secondary}{longitude}{invalid}
    {INFO_ADD} Timezone     : {secondary}{timezone}{invalid}
    {INFO_ADD} Isp          : {secondary}{isp}{invalid}
    {INFO_ADD} Org          : {secondary}{org}{invalid}
    {INFO_ADD} As           : {secondary}{as_host}{invalid}{reset}""")
        return loc_url
        

    Slow(map_banner)
    ip = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('tool_infos_recovery')}{reset}")
    print(f"\n    {INFO_ADD} Ip           : {secondary}{ip}{invalid}")
    ping_ip(ip)
    dns_ip(ip)
    loc_url = info_ip(ip)
    port_ip(ip)
    print()
    try:
        BrowserPrivate(site=loc_url, title=f"Ip Localisation ({loc_url})", search_bar=False)
    except:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)