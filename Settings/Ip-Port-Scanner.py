from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

Slow(scan_banner)

def tr(key):
    return translations[current_language].get(key, key)

try:
   import socket
   import concurrent.futures
except Exception as e:
   ErrorModule(e)
   
Title("Ip Port Scanner")

try:
    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Ip: {secondary}{ip}{primary} | Status: {secondary}Open{primary} | Port: {secondary}{port}")
            sock.close()
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {tr('Error')} {secondary}{e}")
            return

    def scan_ports(ip, start_port, end_port):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
    
    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {tr('Scan')}")
    start_port = 1
    end_port = 65535

    scan_ports(ip, start_port, end_port)
    Continue()
    Reset()
except Exception as e:
    Error(e)