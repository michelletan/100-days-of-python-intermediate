from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Timer
from homepage import HomePage

# Strategy: Check for upgrades and buy the most expensive upgrade every 5s

TARGET_URL = "https://orteil.dashnet.org/experiments/cookie/"
GAME_LENGTH = 300.0 # secs
INTERVAL_LENGTH = 5.0 # secs

class CookieGameEngine():
    def __init__(self) -> None:
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(TARGET_URL)
        
        self.page = HomePage(self.driver)
        self.start()

    def start(self):
        # Start timer of 5 mins
        # Every 5s, check to see what can be bought
        # At the end of game, check final score
        self.is_game_on = True

        end_timer = Timer(GAME_LENGTH, self.game_over)
        end_timer.daemon = True
        end_timer.start()

        self.buy_items()

        while self.is_game_on:
            self.page.click_cookie()

    def buy_items(self):
        # Schedule timer for next check
        game_timer = Timer(INTERVAL_LENGTH, self.buy_items)
        game_timer.daemon = True
        game_timer.start()

        items = self.page.get_available_items()
        if len(items) > 0:
            items[-1].click()

    def game_over(self):
        self.is_game_on = False
        score = self.page.get_cookie_rate()
        print(f"Game Over! Your score is {score}")
        self.driver.quit()
        quit()

if __name__ == "__main__":
    game = CookieGameEngine()
    game.start()