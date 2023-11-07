from selenium import webdriver
from selenium.webdriver.common.by import By

TARGET_URL = "https://www.amazon.com/dp/B075CWJ3T8?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TARGET_URL)

# Example usage of By
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="input_name")
# search_bar.get_attribute("value")
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# driver.close() # Closes tab
# driver.quit() # Quit browser