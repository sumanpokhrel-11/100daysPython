from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create the driver 
driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/recommendation-system-in-python/")

'''after inspecting this website i come to know that the search bar is not directly accessed
so i have to click the search icon to open the search bar'''
button = driver.find_element(By.XPATH, "//button[@class = 'gcse-search__btn not-expanded']")
button.click()

'''after clicking the search button i can access the searchbar and now i get to search whatever i want
'''
elem = driver.find_element(By.CLASS_NAME, "gcse-search-input__wrapper")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
# Set implicit wait for 10 seconds (adjust as needed)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gcse-item-info")))  

# clicks the first link when the item is searched
link = driver.find_element(By.XPATH, "//div[@class = 'gcse-title']/a[1]")
link.click()

# open the browser for unlimited time
while True:
    pass


# driver.close()
