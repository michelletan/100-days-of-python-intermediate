from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TARGET_URL = "https://en.wikipedia.org/wiki/Main_Page"
TARGET_URL = "http://secure-retreat-92358.herokuapp.com/"

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TARGET_URL)

# article_count = driver.find_element(By.XPATH, "//a[contains(@title, 'Special:Statistics')]")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

# EXERCISE: Submit a form
input_first = driver.find_element(By.NAME, "fName")
input_last = driver.find_element(By.NAME, "lName")
input_email = driver.find_element(By.NAME, "email")
input_submit = driver.find_element(By.TAG_NAME, "button")

input_first.send_keys("First")
input_last.send_keys("Last")
input_email.send_keys("first@last.com")
input_submit.click()

success_tag = driver.find_element(By.TAG_NAME, "h1")
success = success_tag.text == "Success!"
print(f"Successful: {success}")