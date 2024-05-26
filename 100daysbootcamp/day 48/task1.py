from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")


events = {}
for index in range(1, 6):
    date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{index}]/time').text
    event = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{index}]/a').text
    events[index] = {
        "time" : date,
        "event" : event
    }

print(events)

