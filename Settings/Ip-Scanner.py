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
    import sys
    import ssl
    import concurrent.futures
    from requests.exceptions import RequestException
except Exception as e:
    ErrorModule(e)
    
Title("Ip Scanner")

try:

    def ip_type(ip):
        if ':' in ip:
            type = "ipv6"
        elif '.' in ip:
            type = "ipv4"
        else:
            type = "Unknown"
            return
        
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} IP Type: {secondary}{type}{primary}")

    def ip_ping(ip):
        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
            else:
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
            if result.returncode == 0:
                ping = "Succeed"
            else:
                ping = "Fail"
        except:
            ping = "Fail"

        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Ping: {secondary}{ping}{primary}")

    def ip_port(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "blueis",
            1521: "Oracle DB", 3389: "RDP"
        }

        port_list = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]

        def scan_port(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = identify_protocol(ip, port)
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Port: {secondary}{port}{primary} Status: {secondary}Open{primary} {tr('Protocol')}: {secondary}{protocol}{primary}")
                sock.close()
            except:
                pass

        def identify_protocol(ip, port):
            try:
                if port in port_protocol_map:
                    return port_protocol_map[port]
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    sock.connect((ip, port))
                    
                    sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
                    response = sock.recv(100).decode('utf-8')
                    if "HTTP" in response:
                        return "HTTP"

                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "FTP" in response:
                        return "FTP"

                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "SSH" in response:
                        return "SSH"

                    return "Unknown"
            except:
                return "Unknown"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(scan_port, ip, port): port for port in port_list}
        concurrent.futures.wait(results)

    def ip_dns(ip):
        try:
            dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except:
            dns = "None"
        if dns != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS: {secondary}{dns}{primary}")

    def ip_host_info(ip):
        api_url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(api_url)
            api = response.json()
        except RequestException:
            api = {}

        host_country = api.get('country', 'None')
        if host_country != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host Country: {secondary}{host_country}{primary}")

        host_name = api.get('hostname', 'None')
        if host_name != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host Name: {secondary}{host_name}{primary}")

        host_isp = api.get('org', 'None')
        if host_isp != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host ISP: {secondary}{host_isp}{primary}")

        host_as = api.get('asn', 'None')
        if host_as != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host AS: {secondary}{host_as}{primary}")

    def ssl_certificate_check(ip):
        port = 443
        try:
            sock = socket.create_connection((ip, port), timeout=1)
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=ip) as ssock:
                cert = ssock.getpeercert()
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {tr('SSLCertifOn')} {secondary}{cert}{primary}")
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {tr('SSLCertifOff')} {secondary}{e}{primary}")


    Slow(scan_banner)
    ip = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('tool_infos_recovery')}{reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Ip: {secondary}{ip}{primary}")
    ip_type(ip)
    ip_ping(ip)
    ip_dns(ip)
    ip_port(ip)
    ip_host_info(ip)
    ssl_certificate_check(ip)
    Continue()
    Reset()
except Exception as e:
    Error(e)
