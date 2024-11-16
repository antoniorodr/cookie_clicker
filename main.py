from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option("detach", True)
DRIVER = webdriver.Chrome(options = OPTIONS)
DRIVER.get("http://orteil.dashnet.org/experiments/cookie/")
COOKIE = DRIVER.find_element(By.ID, "cookie")
COOKIE_COUNTER = int(DRIVER.find_element(By.ID, "money").text)
START = time.time()
FIVE_SECONDS = 5


#TODO: Check prices list. Seems it takes "5" from somewhere.

def store_prices():
    STORE_ITEMS = DRIVER.find_element(By.ID, "store").text.strip().split()
    prices = []
    for item in STORE_ITEMS:
        if item.isdigit():
            prices.append(int(item))
    return sorted(prices)

def click_cookie():
    COOKIE.click()


while True:
    click_cookie()
    if time.time() > START + FIVE_SECONDS:
        cookie_upgrades = {}
        for n in range(len(store_prices())):
            items = DRIVER.find_elements(by=By.CSS_SELECTOR, value="#store div")
            item_ids = [item.get_attribute("id") for item in items]
            cookie_upgrades[store_prices()[n]] = item_ids[n]
        # for price, item_id in cookie_upgrades.items():
            # if COOKIE_COUNTER >= price:
        print(cookie_upgrades)
                # DRIVER.find_element(By.ID, item_id).click()


# driver.close()