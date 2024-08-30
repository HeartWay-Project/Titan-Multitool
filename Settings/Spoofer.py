from Config.Util import *
from Config.Config import *
import os
import platform
import subprocess
import uuid
import ctypes

# Variables globales pour stocker les valeurs d'origine
original_hwid = None
original_mac = {}

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_current_mac(interface: str) -> str:
    os_name = platform.system().lower()
    
    if "windows" in os_name:
        result = subprocess.run(["getmac", "/v", "/fo", "list"], capture_output=True, text=True)
        return result.stdout
    elif "linux" in os_name:
        result = subprocess.run(["cat", f"/sys/class/net/{interface}/address"], capture_output=True, text=True)
        return result.stdout.strip()

def get_current_hwid() -> str:
    if platform.system().lower() == "windows":
        try:
            result = subprocess.run(["wmic", "csproduct", "get", "UUID"], capture_output=True, text=True)
            hwid = result.stdout.strip().split("\n")[1].strip()
            return hwid
        except Exception as e:
            return f"Error retrieving HWID: {e}"
    else:
        return "HWID display is not supported on this OS."

def change_mac_address(interface: str, new_mac: str):
    os_name = platform.system().lower()
    
    if "windows" in os_name:
        subprocess.run(["netsh", "interface", "set", "interface", interface, "disable"])
        subprocess.run(["netsh", "interface", "set", "interface", interface, "new_mac=" + new_mac])
        subprocess.run(["netsh", "interface", "set", "interface", interface, "enable"])
    elif "linux" in os_name:
        subprocess.run(["sudo", "ifconfig", interface, "down"])
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.run(["sudo", "ifconfig", interface, "up"])

def change_hwid():
    global original_hwid
    if platform.system().lower() == "windows":
        if not is_admin():
            print(f"{ERROR} Error: Access denied. Please run this script as an administrator.")
            return
        
        if original_hwid is None:
            original_hwid = get_current_hwid()  # Sauvegarde du HWID original
        print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO} Changing HWID :")
        new_hwid = str(uuid.uuid4())
        try:
            subprocess.run(['reg', 'add', r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001', '/v', 'HwProfileGuid', '/d', new_hwid, '/f'])
            print(f"{INFO} New HWID: {secondary}{new_hwid}")
        except Exception as e:
            print(f"{ERROR} Error changing HWID: {e}")
    else:
        print("HWID spoofing is not supported on this OS.")

def reset_changes():
    global original_hwid, original_mac
    if original_hwid:
        try:
            subprocess.run(['reg', 'add', r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001', '/v', 'HwProfileGuid', '/d', original_hwid, '/f'])
            print(f"\n{INFO} HWID reset to original value: {secondary}{original_hwid}")
        except Exception as e:
            print(f"{ERROR} Error resetting HWID: {e}")

    if original_mac:
        for interface, mac in original_mac.items():
            try:
                change_mac_address(interface, mac)
                print(f"{INFO} MAC Address for {interface} reset to original value: {secondary}{mac}")
            except Exception as e:
                print(f"{ERROR} Error resetting MAC Address: {e}")

def show_current_addresses(interface: str):
    global original_mac

    if interface not in original_mac:
        original_mac[interface] = get_current_mac(interface)  # Sauvegarde de la MAC originale

    print(f"\n{INFO} Current Addresses:{secondary}\n")
    print(f"{INFO} MAC Address ({interface}): {secondary}{get_current_mac(interface)}")
    print(f"{INFO} HWID: {secondary}{get_current_hwid()}")
    Continue()
    Reset()

def menu():
    while True:
        print(f"\n{secondary}[{primary}1{secondary}] {primary}Show Current Addresses")
        print(f"{secondary}[{primary}2{secondary}] {primary}Change MAC Address")
        print(f"{secondary}[{primary}3{secondary}] {primary}Change HWID (Windows only)")
        print(f"{secondary}[{primary}4{secondary}] {primary}Reset Changes")
        print(f"{secondary}[{primary}5{secondary}] {primary}Quit")
        
        choice = input(f"\n{INPUT} Choose an option -> {reset}")
        
        if choice == '1':
            interface = input(f"\n{INPUT} Network interface (e.g., eth0, wlan0) -> {reset}")
            show_current_addresses(interface)
        elif choice == '2':
            interface = input(f"{INPUT} Network interface (e.g., eth0, wlan0) -> {reset}")
            new_mac = input(f"{INPUT} New MAC address (format: XX:XX:XX:XX:XX:XX) -> {reset}")
            change_mac_address(interface, new_mac)
        elif choice == '3':
            change_hwid()
        elif choice == '4':
            reset_changes()
        elif choice == '5':
            Continue()
            Reset()
        else:
            Error()

if __name__ == "__main__":
    menu()
