from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option("detach", True)
DRIVER = webdriver.Chrome(options = OPTIONS)
DRIVER.get("http://orteil.dashnet.org/experiments/cookie/")
COOKIE = DRIVER.find_element(By.ID, "cookie")
START = time.time()
FIVE_SECONDS = 5


#TODO: Got an error with IDs

def store_prices():
    STORE_ITEMS = DRIVER.find_elements(by=By.CSS_SELECTOR, value="#store b")
    item_prices = []
    for item in STORE_ITEMS:
        element_text = item.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)
    return item_prices        

def highest_affordable_upgrade(money: int, upgrades: dict):# -> String:
    affordable = {}
    for price, item_id in upgrades.items():
        if money >= price:
            affordable[price] = item_id
    highest_affordable = max(affordable)
    to_purchase_id = affordable[highest_affordable]
    return to_purchase_id

def click_cookie():
    COOKIE.click()


while True:
    click_cookie()
    if time.time() > START + FIVE_SECONDS:
        cookie_counter = int(DRIVER.find_element(By.ID, "money").text)
        cookie_upgrades = {}
        for n in range(len(store_prices())):
            items = DRIVER.find_elements(by=By.CSS_SELECTOR, value="#store div")
            item_ids = [item.get_attribute("id") for item in items]
            cookie_upgrades[store_prices()[n]] = item_ids[n]
            upgrade_purchase = highest_affordable_upgrade(cookie_counter, cookie_upgrades)
            DRIVER.find_element(by=By.ID, value=upgrade_purchase).click()
            timeout = time.time() + 5



# driver.close()