from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option("detach", True)
DRIVER = webdriver.Chrome(options = OPTIONS)
DRIVER.get("http://orteil.dashnet.org/experiments/cookie/")
COOKIE = DRIVER.find_element(By.ID, "cookie")
COOKIE_COUNTER = DRIVER.find_element(By.ID, "money").text
STORE = DRIVER.find_element(By.ID, "store")
ITEMS = DRIVER.find_elements(by=By.CSS_SELECTOR, value="#store div")
STORE_ITEMS = DRIVER.find_element(By.ID, "store").text.strip().split()
START = time.time()
PAUSE = 5

item_ids = [item.get_attribute("id") for item in ITEMS]
timeout = 0

def store_prices():
    prices = []
    for item in STORE_ITEMS:
        if item.isdigit():
            prices.append(int(item))
    return sorted(prices, reverse = True)

def click_cookie():
    COOKIE.click()


#TODO: Start from scratch
prices_sorted = store_prices()
cookie_upgrades = {}
for n in range(len(prices_sorted)):
    cookie_upgrades[prices_sorted[n]] = item_ids[n]
print(cookie_upgrades)

while True:
    click_cookie()
    # if time.time() > START + PAUSE:
    # if timeout == PAUSE:
    #     for price, upgrade_id in cookie_upgrades.items():
    #         if int(COOKIE_COUNTER) >= price:
    #             DRIVER.find_element(By.ID, upgrade_id).click()
    #             timeout = 0

# driver.close()