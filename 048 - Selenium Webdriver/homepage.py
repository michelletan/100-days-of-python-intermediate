from locators import Locators

class HomePage():
    """Acts as a page object to interact with the cookie clicker game page."""
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_cookie_count(self) -> int:
        return self.driver.find_element(*Locators.COOKIE_COUNT).text

    def get_cookie_rate(self) -> float:
        container = self.driver.find_element(*Locators.COOKIE_RATE)
        return container.text.split(": ")[1]
    
    def get_all_store_items(self) -> list[any]:
        return self.driver.find_elements(*Locators.STORE_ITEMS)
    
    def get_available_items(self) -> list[int]:
        return self.driver.find_elements(*Locators.AVAILABLE_STORE_ITEMS)
    
    def is_items_available(self) -> bool:
        return len(self.driver.find_elements(*Locators.AVAILABLE_STORE_ITEMS)) > 0

    def click_cookie(self):
        self.driver.find_element(*Locators.COOKIE_BUTTON).click()

    def buy_item(self, item_index: int):
        items = self.get_available_items()
        items[item_index].click()

