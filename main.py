# MIT License
# 
# Copyright (c) 2023 Prem Patel (https://www.github.com/Prem-ium)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, sys, datetime, traceback, apprise

from selenium                               import webdriver
from datetime                               import datetime  
from selenium.webdriver.common.by           import By
from selenium.webdriver.chrome.options      import Options
from webdriver_manager.chrome               import ChromeDriverManager
from selenium.webdriver.chrome.service      import Service

from time                                   import sleep
from dotenv                                 import load_dotenv

load_dotenv()

print(f"\n{'-' * 75}\nWelcome to Wired Coupon Scraper.\n\nAn automation script to retrieve multiple retailer promotion codes and offers from the Wired website.\nCreated by Prem-ium (https://github.com/Prem-ium)\n\n")

# Retrieve CLI Arguments & Environment Variables

if len(sys.argv) == 2:
    RETAILERS = sys.argv[1].split(",")
    print(f"RETAILERS argument received.\nGathering coupon codes for: {RETAILERS}\n{'-' * 50}")
else:
    RETAILERS = os.environ.get("RETAILERS", None)
    if RETAILERS is None:
        print(f"No arguments or environment variables received for RETAILERS... Defaulting to Walmart.\n{'-' * 50}")
        RETAILERS = ["walmart"]

ALLOW_DUPLICATES = True if os.environ.get("ALLOW_DUPLICATES", "False").lower() == "true" else False

if os.environ.get("KEEP_ALIVE", "False").lower() == "true":
    from keep_alive import keep_alive
    keep_alive()
    KEEP_ALIVE = True
else:
    KEEP_ALIVE = False

# Set up Apprise, if enabled
APPRISE_ALERTS = os.environ.get("APPRISE_ALERTS", None)
if APPRISE_ALERTS:
    APPRISE_ALERTS = APPRISE_ALERTS.split(",")
    alerts = apprise.Apprise()
    for service in APPRISE_ALERTS:
        alerts.add(service)

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(cache_valid_range=30).install()),
            options=chrome_options)
    except Exception as e:
        driver = webdriver.Chrome(options=chrome_options)
    return driver

def cached_codes_init():
    if not os.path.isfile("codes.txt"):
        open("codes.txt", "a").close()
        print(f"Created new codes.txt file")
    else:
        with open("codes.txt", "r") as f:
            if datetime.now().day == 1 and f.readlines():
                print("It's the first day of the month. Clearing the codes.txt file.")
                with open("codes.txt", "w"):    pass
            else:
                print(f"codes.txt file already exists")

def check_cached_codes(code):
    with open("codes.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        if f"{str(code)}\n" in lines:
            print(f"Code {code} found in cache")
            return True
        return False

def append_cached_code(code):
    with open("codes.txt", "a") as f:
        f.write(f"{code}\n")
        print(f"Appended {code} to codes.txt")

def main():
    if not ALLOW_DUPLICATES:
        cached_codes_init()

    driver = getDriver()

    for type in RETAILERS:
        print(f'{"-" * 70}\nRetrieving {type.upper()} Promo Code Offers...\n')
        driver.get(f'https://www.wired.com/coupons/{type}')

        coupons = (driver.find_element(By.CLASS_NAME, 'coupons-list')).find_elements(By.TAG_NAME, 'a')
        ids = [coupon.get_attribute('href') for coupon in coupons]

        print(f'{len(coupons)} {type.upper()} Promo Codes/Coupons were found!')
        
        for id in ids:
            driver.get(id)
            driver.refresh()
            try:
                sleep(2)
                print('-' * 50)
                title = driver.find_element(By.XPATH, '//*[@id="my-modal"]/div/div/div/h3')
                code = driver.find_element(By.XPATH, '//*[@id="my-modal"]/div/div/div/div[2]/span')
                try:
                    link = (driver.find_element(By.CLASS_NAME, 'modal-clickout__link')).get_attribute("href")
                except:
                    link = "(Error retrieving link)"
                    print(traceback.format_exc())

                data = f'{title.text}:\n\t{code.text} \n{link}\n'
                print(data)

                if APPRISE_ALERTS:
                   alerts.notify(title=f'{type.upper()} Coupon', body=f'{title.text}\n\n{code.text}\n{link}')

                data = data.replace("\n", " - ")

                if not ALLOW_DUPLICATES:
                    if check_cached_codes(data):
                        print(f"Code {code.text} for {title.text} already exists in cache, skipping")
                        continue
                    else:
                        append_cached_code(data)
            except:
                print(traceback.format_exc())
            finally:
                print('-' * 50)
        print(f'{"-" * 70}\nFinished retrieving promotions.\n{"-" * 70}')

if __name__ == '__main__':
    if not KEEP_ALIVE:
        main()
    else:
        while True:
            main()
            sleep(3600)