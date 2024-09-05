from Config.Util import *
from Config.Config import *
from Config.Translates import *

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

try:
    import threading
    import time
    import socket
except Exception as e:
   ErrorModule(e)
   
Title("Ip Pinger")

try:
    hostname = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> " + color.RESET)
    try:
        port_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Port (enter for default) -> " + color.RESET)
        if port_input.strip():
            port = int(port_input)
        else:
            port = 80  
        
        bytes_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Bytes (enter for default) -> " + color.RESET)
        if bytes_input.strip():
            bytes = int(bytes_input)
        else:
            bytes = 64

        threads_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} {tr('ThreadsNumber')} (enter for default) -> {color.RESET}")
        if threads_input.strip():
            threads_number = threads_input
        else:
            threads_number = 1
    except:
        ErrorNumber()

    def ping_ip():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            start_time = time.time() 
            sock.connect((hostname, port))
            data = b'\x00' * bytes
            sock.sendall(data)
            end_time = time.time() 
            elapsed_time = (end_time - start_time) * 1000 
            print(f'{BEFORE + current_time_hour() + AFTER} {ADD} Ping to {secondary}{hostname}{invalid}: time={secondary}{elapsed_time:.2f}ms{invalid} port={secondary}{port}{invalid} bytes={secondary}{bytes}{invalid} status={secondary}succeed{invalid}')
        except:
            elapsed_time = 0
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Ping to {secondary}{hostname}{invalid}: time={secondary}{elapsed_time}ms{invalid} port={secondary}{port}{invalid} bytes={secondary}{bytes}{invalid} status={secondary}fail{invalid}')

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=ping_ip)
                t.start()
                threads.append(t)
        except:
            ()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)