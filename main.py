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
STORE_ITEMS = DRIVER.find_element(By.ID, "store").text.strip().split()
ITEMS = DRIVER.find_elements(by=By.CSS_SELECTOR, value="#store div")
START = time.time()
FIVE_SECONDS = 5

def store_prices():
    prices = []
    for item in STORE_ITEMS:
        if item.isdigit():
            prices.append(int(item))
    return sorted(prices, reverse = True)

def click_cookie():
    COOKIE.click()

item_ids = [item.get_attribute("id") for item in ITEMS]

#TODO: Start from scratch

while True:
    click_cookie()
    if time.time() > START + FIVE_SECONDS:
        cookie_upgrades = {}
        for n in range(len(store_prices())):
            cookie_upgrades[store_prices()[n]] = item_ids[n]
        for price, item_id in cookie_upgrades.items():
            if COOKIE_COUNTER >= price:
                DRIVER.find_element(By.ID, item_id).click()


# driver.close()