# Created by: Prem-ium (https://www.github.com/Prem-ium)


import os
import apprise
import datetime
from selenium import webdriver
from datetime import datetime  
from selenium.webdriver.common.by           import By
from selenium.webdriver.chrome.options      import Options
from webdriver_manager.chrome               import ChromeDriverManager
from selenium.webdriver.chrome.service      import Service

from time                                   import sleep
from dotenv                                 import load_dotenv

load_dotenv()

# Enable keep_alive.py if specified in environment
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

# Retrieve environment variables for user preferences
ALLOW_DUPLICATES = True if os.environ.get("ALLOW_DUPLICATES", "False").lower() == "true" else False

RETAILERS = os.environ.get("RETAILERS", None)
if RETAILERS is None:
    print(f"No retailers specified. Please configure your .env to include the names of supported retailers you wish to scrape coupons for. Defaulting to Walmart...")
    RETAILERS = ["walmart"]

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(cache_valid_range=30).install()),
            options=chrome_options)
    except Exception as e:
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as ek:
            print(f'Attempted to use webdriver manager, but failed.\n{e}\nAttempted to use local webdriver, failed.\n{ek}')
    return driver

def cached_codes_init():
    if not os.path.isfile("codes.txt"):
        open("codes.txt", "a").close()
        print(f"Created new codes.txt file\n")
    else:
        today = datetime.now().day
        with open("codes.txt", "r") as f:
            lines = f.readlines()
            if today == 1 and lines:
                print("It's the first day of the month. Clearing the codes.txt file.")
                with open("codes.txt", "w"):
                    pass
            else:
                print(f"codes.txt file already exists\n")

def check_cached_codes(code):
    with open("codes.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        if str(code) in lines:
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
        driver.get(f'https://www.wired.com/coupons/{type}')
        coupons_div = driver.find_element(By.CLASS_NAME, 'coupons-list')

        coupons = coupons_div.find_elements(By.TAG_NAME, 'a')
        print(f'{len(coupons)} {type} coupons were found!\n\n')

        ids = [coupon.get_attribute('href') for coupon in coupons]

        for URL in [f"https://www.wired.com/coupons/{type}{id}" for id in ids]:
            driver.get(URL)
            driver.refresh()
            try:
                print('-' * 25)
                title = driver.find_element(By.XPATH, '//*[@id="my-modal"]/div/div/div/h3')
                code = driver.find_element(By.XPATH, '//*[@id="my-modal"]/div/div/div/div[2]/span')

                if not ALLOW_DUPLICATES:
                    if check_cached_codes(code.text):
                        print(f"Code {code.text} for {title.text} already exists in cache, skipping")
                        continue

                if APPRISE_ALERTS:
                    try:
                        alerts.notify(title=f'{title.text}', body=f'{code.text}')
                    except Exception as e:          print(e)

                print(f'{title.text}:\n\t{code.text}\t')

                if not ALLOW_DUPLICATES:
                    append_cached_code(code.text)

                try:        print(f'{driver.find_element(By.XPATH, value="/html/body/div[9]/div/div/div/div[1]/div[2]/div/span").text}\n')
                except:     pass

                
            except:
                print('Error retrieving code.')
            finally:
                print('-' * 50)
        print(f'Thanks for using Prem-ium\'s Coupon Scraper!\n(https://www.github.com/Prem-ium)\n\n{"-" * 70}')

if __name__ == '__main__':
    main()

    while KEEP_ALIVE:
        main()
        sleep(3600)
