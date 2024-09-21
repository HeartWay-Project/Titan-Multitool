import os
import sys
import subprocess
import webbrowser
import pkg_resources

def check_python_version():
    if sys.version_info >= (3, 12):
        print(f"Python {sys.version_info.major}.{sys.version_info.minor} est déjà installé.")
    else:
        print("Python 3.12 ou plus récent n'est pas installé.")
        response = input("Voulez-vous installer Python 3.12 depuis le Microsoft Store ? (oui/non): ")
        if response.lower() == 'oui':
            install_python_312()
        else:
            print("Installation annulée.")
            sys.exit(1)

def install_python_312():
    install_cmd = 'Get-AppxPackage -Name *Python* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\\AppXManifest.xml"}'
    print("Installation de Python 3.12 depuis le Microsoft Store...")
    try:
        subprocess.run(["powershell", "-Command", install_cmd], check=True)
        update_environment_variables()
    except subprocess.CalledProcessError as e:
        print("L'installation de Python 3.12 a échoué:", e)
        sys.exit(1)

def update_environment_variables():
    python_path = r"C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps\python.exe"
    os.environ["PATH"] += os.pathsep + python_path
    print("Variables d'environnement mises à jour avec le chemin de Python.")

def install_requirements():
    if os.path.exists('requirements.txt'):
        print("Installation des modules requis...")
        with open('requirements.txt', 'r') as req_file:
            for line in req_file:
                module = line.strip()
                if module:
                    try:
                        # Vérifier si le module est déjà installé
                        pkg_resources.get_distribution(module)
                        print(f"Module '{module}' est déjà installé.")
                    except pkg_resources.DistributionNotFound:
                        # Si le module n'est pas installé, essayer de l'installer
                        try:
                            subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)
                            print(f"Module '{module}' installé avec succès.")
                        except subprocess.CalledProcessError:
                            print(f"Erreur lors de l'installation du module '{module}', mais on continue...")
    else:
        print("Le fichier requirements.txt n'existe pas.")
        sys.exit(1)

def open_github_page():
    url = "https://github.com/HeartWay-Project/Titan-Multitool"
    print(f"Ouverture de la page GitHub: {url}")
    webbrowser.open(url)

def run_titan_script():
    titan_script = 'Titan.py'
    if os.path.exists(titan_script):
        print(f"Exécution du script: {titan_script}")
        subprocess.run([sys.executable, titan_script])
    else:
        print(f"Le fichier {titan_script} n'existe pas.")

if __name__ == "__main__":
    check_python_version()
    install_requirements()
    open_github_page()
    run_titan_script()
