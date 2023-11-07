from selenium import webdriver
from selenium.webdriver.common.by import By

# Task: Grab the list of upcoming events from python.org and save it to a dictionary

TARGET_URL = "https://www.python.org"

driver = webdriver.Chrome()
driver.get(TARGET_URL)

table = driver.find_element(By.XPATH, "//h2[@class='widget-title' and contains(text(), 'Upcoming Events')]/../ul")
event_times = table.find_elements(By.TAG_NAME, "time")
event_names = table.find_elements(By.TAG_NAME, "a")

events = []
for i in range(len(event_times)):
    e = {}
    e['time'] = event_times[i].get_attribute("datetime")
    e['name'] = event_names[i].text
    events.append(e)

print(events)
