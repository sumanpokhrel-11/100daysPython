# cookie clicker game
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()
cookie = driver.find_element(By.ID, 'bigCookie')
for i in range(1000):
    cookie.click()

while True:
    pass
