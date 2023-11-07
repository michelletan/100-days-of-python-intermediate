from selenium.webdriver.common.by import By

class Locators(object):
    COOKIE_COUNT = (By.ID, "money")
    COOKIE_BUTTON = (By.ID, "cookie")
    COOKIE_RATE = (By.ID, "cps")
    STORE_ITEMS = (By.XPATH, "//div[@id = 'store']/div")
    AVAILABLE_STORE_ITEMS = (By.XPATH, "//div[@id = 'store']/div[@class = '']")
