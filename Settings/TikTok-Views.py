from Config.Util import *
from Config.Config import *
from Config.Translates import *
import random
import os
import platform
import time
import ctypes

try:
    import undetected_chromedriver as uc
    from colorama import Fore
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
except ImportError:
    input("You do not have all of the modules required installed.")
    os._exit(1)

class zefoy:

    def __init__(self):
        self.driver = uc.Chrome()
        self.captcha_box = '/html/body/div[5]/div[2]/form/div/div'
        self.clear = "clear"

        if platform.system() == "Windows":
            self.clear = "cls"

        self.color = Fore.BLUE
        self.sent = 0
        self.alternate = 0
        self.alternate_send = 0

        self.xpaths = {
            "views": ["/html/body/div[6]/div/div[2]/div/div/div[6]/div/button"],
        }

    def find_element_continuously(self, xpath, check_interval=2):
        element = None
        while element is None:
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                return element
            except NoSuchElementException:
                time.sleep(check_interval)
        return element

    def get_xpath(self, action):
        if action == "views":
            return self.xpaths["views"][0]
        else:
            return random.choice(self.xpaths.get(action, [""]))

    def check_status(self):
        statuses = {}

        for action in self.xpaths:
            value = self.get_xpath(action)
            element = self.find_element_continuously(value)

            if element is None or not element.is_enabled():
                statuses.update({action: f"{Fore.RED}[OFFLINE]"})
            else:
                statuses.update({action: f"{Fore.GREEN}[WORKS]"})

        return statuses

    def send_bot(self, search_button, main_xpath, vid_info, div):
        element = self.find_element_continuously(main_xpath)
        element.clear()
        element.send_keys(vid_info)
    
        search_element = self.find_element_continuously(search_button)
        search_element.click()
        time.sleep(3)

        ratelimit_seconds, full = self.check_submit(div)
        if "(s)" in str(full):
            self.main_sleep(ratelimit_seconds)
            self.find_element_continuously(search_button).click()
            time.sleep(2)

        time.sleep(3)

        send_button = f'/html/body/div[10]/div/div/div[1]/div/form/button'

        self.find_element_continuously(send_button).click()
        self.sent += 1
        print(self._print(f"Sent {self.sent} times.\n"))

        self.wait_for_ready_and_resend(search_button, main_xpath, vid_info, div)

    def wait_for_ready_and_resend(self, search_button, main_xpath, vid_info, div):
        countdown_xpath = '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/span[1]'
        
        print(f"{WAIT} Waiting for countdown..")

        while True:
            try:
                button_element = self.driver.find_element(By.XPATH, countdown_xpath)
                button_text = button_element.text

                if "READY" in button_text:
                    print(f"{INFO} Next Submit: READY...! \n{INFO} Retrying to send..")
                    self.send_bot(search_button, main_xpath, vid_info, div)
                    break
                else:
                    time.sleep(5)

            except NoSuchElementException:
                print("Submit Button Not Found.")
                break

    def main_sleep(self, delay):
        while delay != 0:
            time.sleep(1)
            delay -= 1
            self.change_title(f"TikTok Auto Views")

    def convert(self, min, sec):
        seconds = 0

        if min != 0:
            answer = int(min) * 60
            seconds += answer

        seconds += int(sec) + 5
        return seconds

    def check_submit(self, div):
        remaining = f'//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button'

        try:
            element = self.find_element_continuously(remaining)
        except NoSuchElementException:
            return None, None

        if "READY" in element.text:
            return True, True

        if "seconds for your next submit" in element.text:
            output = element.text.split("Please wait ")[1].split(" for")[0]
            minutes = element.text.split("Please wait ")[1].split(" ")[0]
            seconds = element.text.split("(s) ")[1].split(" ")[0]
            sleep_duration = self.convert(minutes, seconds)

            return sleep_duration, output

        return element.text, None

    def main(self):

        Slow(Tiktok_views_banner)

        self.driver.get("https://zefoy.com")

        self.find_element_continuously(self.get_xpath("views"))

        status = self.check_status()

        print()

        counter = 1
        for action in status:
            print(self._print(f"{action} {status[action]}", counter))
            counter += 1

        print(self._print(f"Quit", "2"))
        option = int(input(f"\n{INPUT} {tr('Choice')} -> {reset}"))

        if option == 1:
            div = "10"
            self.find_element_continuously(self.get_xpath("views")).click()

        else:
            os._exit(1)

        video_url_box = f'/html/body/div[{div}]/div/form/div/input'
        search_box = f'/html/body/div[{div}]/div/form/div/div/button'
        vid_info = input(f"\n{INPUT} Vidéo Url -> {reset}")

        self.send_bot(search_box, video_url_box, vid_info, div)

    def _print(self, msg, status="-"):
        return f" {Fore.WHITE}[{self.color}{status}{Fore.WHITE}] {msg}"

    def change_title(self, arg):
        if self.clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW(arg)


if __name__ == "__main__":
    obj = zefoy()
    obj.main()
    input()
