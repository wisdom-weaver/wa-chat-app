import time
import random
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    try:
        options = Options()
        # options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(e)


base_url = "https://web.whatsapp.com/"
input_box_xpath = "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]"
send_key_xpath = "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]/button"
side_panel_id = "pane-side"
titles_class = "_3Dr46"
contact_search_bar_xpath = "/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]"

msgs = [
    "microsoft", "hello", "amazon", "google", "netflix", "facebook", "toyota", "mountain dew",
    "BKL", "jhantu", "gandu", "kunal", "kutte", "doraemon", "shinchan", "jonny", "dani daniels",
    "skyle", "mia", "elsa gean", "john wick", "pink", "java", "python", "javascript",
    "macchar ki jhant", "tatton ke saudagar", "chutiya", "green mango more", "tatti",
    "jhinguur", "tilchatta"
]


class Bot:
    driver = None

    def __init__(self):
        print("-"*50)
        print("Starting Whatsapp Chat Bot")
        self.driver = get_driver()

    def send_message(self, message):
        input_box = self.driver.find_element_by_xpath(input_box_xpath)
        input_box.send_keys(message)
        send_key = self.driver.find_element_by_xpath(send_key_xpath)
        send_key.click()

    def wait_to_scan(self):
        key_press = input("Scan qr_code and press a key...")
        return key_press

    def search_for_contact(self, contact_name):
        search_bar = self.driver.find_element_by_xpath(
            contact_search_bar_xpath)
        search_bar.send_keys(contact_name)

    def run(self):
        driver = self.driver
        driver.get(base_url)
        self.wait_to_scan()
        self.send_message("."*50)
        self.send_message("Test 3")
        for i in range(1, 50):
            randidx = int(random.random()*len(msgs))
            msg = msgs[randidx]
            self.send_message(f"{randidx} => {msg}")
            time.sleep(1)


bot = Bot()
bot.run()
