# hudsonrock.py

from email_osg.Requests import Request
import json
from datetime import datetime

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

class Cavalier:
    def __init__(self, email: str) -> None:
        self.email = email
        self.api = "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email"

    async def loader(self):
        # Effectuer la requête API
        response = await Request(self.api, headers={'api-key': 'ROCKHUDSONROCK'}, params={'email': self.email}).get()

        try:
            # Récupération des données de la réponse
            data = response.json()

            stealers = data.get('stealers', [])
            if not stealers:
                print(f"[{RED}HudsonRock{WHITE}] Aucun stealer trouvé pour cet email.")
                return

            # Première occurrence des données de stealer
            stealer_data = stealers[0]

            # Affichage des résultats sans masquer les informations
            print(f"[{RED}HudsonRock{WHITE}] Email's result :")
            print("> Total service corporate :", stealer_data.get('total_corporate_services', '/'))
            print("> Total user services :", stealer_data.get('total_user_services', '/'))

            # Traitement et affichage de la date compromise
            time_iso = stealer_data.get('date_compromised')
            if time_iso:
                t_datetime = datetime.fromisoformat(time_iso.replace("Z", "+00:00"))
                date = t_datetime.strftime("%Y-%m-%d %H:%M:%S")
                print("> Date compromised :", date)
            else:
                print("> Date compromised : /")

            # Affichage du nom de l'ordinateur et du système d'exploitation
            print("> Computer name :", stealer_data.get('computer_name', '/'))
            print("> Operating system :", stealer_data.get('operating_system', '/'))
            print("> Ip address :", stealer_data.get('ip', '/'))  # Ne masque plus l'adresse IP

            # Affichage des mots de passe et identifiants sans astérisques
            top_passwords = stealer_data.get('top_passwords', [])
            top_logins = stealer_data.get('top_logins', [])

            # Pas de masquage ici, on affiche les informations telles quelles
            print("> Top passwords :", ', '.join(top_passwords) if top_passwords else '/')
            print("> Top logins :", ', '.join(top_logins) if top_logins else '/')

        except (KeyError, json.JSONDecodeError):
            print(f"[{RED}HudsonRock{WHITE}] Email Safe")
