import os, traceback, apprise, datetime

from selenium import webdriver
from selenium.webdriver.common.by           import By
from selenium.webdriver.chrome.options      import Options
from webdriver_manager.chrome               import ChromeDriverManager
from selenium.webdriver.chrome.service      import Service

from time                                   import sleep
from dotenv                                 import load_dotenv

load_dotenv()

def apprise_init():
    if APPRISE_ALERTS:
        alerts = apprise.Apprise()
        # Add all services from .env
        for service in APPRISE_ALERTS:
            alerts.add(service)
        return alerts

# Set up Apprise, if enabled
APPRISE_ALERTS = os.environ.get("APPRISE_ALERTS", None)
if APPRISE_ALERTS:
    APPRISE_ALERTS = APPRISE_ALERTS.split(",")
    alerts = apprise_init()

ALLOW_DUPLICATES = True if (os.environ.get("ALLOW_DUPLICATES", "False").lower() == "true") else False

def cached_codes_init():
    if not os.path.isfile("codes.txt"):
        open("codes.txt", "a").close()
        print(f"Created new codes.txt file")
        print()
    else:
        print(f"codes.txt file already exists")
        print()

def check_cached_codes(code):
    with open("codes.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        if str(code) in lines:
            print(f"Code {code} found in cache")
            return True
        else:
            return False

def append_cached_code(code):
    with open("codes.txt", "a") as f:
        f.write(f"{code}\n")
        print(f"Appended {code} to codes.txt")

def close_cached_code():
    print(f"Closing codes.txt")

    with open("codes.txt", "a") as f:
        f.close()

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    try:
        driver = webdriver.Chrome(
                service=Service(ChromeDriverManager(cache_valid_range=30).install()),
                options=chrome_options)
    except Exception as e:
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as ek:
            print(f'Attempted to use webdriver manager, but failed. \n{e}\nAttempted to use local webdriver, failed.\n{ek}')
    return driver

def main():
    print(f'Thanks for using DoorDash Coupon Scraper!\nCreated by: @Prem-ium (https://www.github.com/Prem-ium)\n\n{"-"*70}')
    if not ALLOW_DUPLICATES:
        cached_codes_init()
    driver = getDriver()
    driver.get('https://www.wired.com/coupons/doordash')
    coupons = driver.find_elements(By.CLASS_NAME, 'coupon__aside')

    print(f'{len(coupons)} DoorDash coupons were found!\n\n')

    ids = []
    for i in range(len(coupons)):
        ids.append(coupons[i].get_attribute('href'))

    for i in range(len(ids)):
        URL = "https://www.wired.com/coupons/doordash" + ids[i]
        driver.get(URL)
        driver.refresh()
        try:
            print('-'*50)
            title = driver.find_element(By.XPATH, '//*[@id="my-modal"]/div/div/div/div[1]/div[2]/h3')
            code = driver.find_element(By.XPATH, '//*[@id="my-modal"]/div/div/div/div[2]/span')

            if not ALLOW_DUPLICATES:
                if check_cached_codes(code.text):
                    print(f"Code {code.text} for {title.text} already exists in cache, skipping")
                    continue

            if APPRISE_ALERTS:
                try: 
                    alerts.notify(title=f'{title.text}', body=f'{code.text}')
                except Exception as e: print(e)
            print(f'{title.text}:\n\t{code.text}\t')

            if not ALLOW_DUPLICATES:
                append_cached_code(code.text)

            try:    print(f'{driver.find_element(By.XPATH, value="/html/body/div[9]/div/div/div/div[1]/div[2]/div/span").text}\n')
            except: pass
            print('-'*70)
        except: print('Error retrieving code.')

if __name__ == '__main__':
    main()