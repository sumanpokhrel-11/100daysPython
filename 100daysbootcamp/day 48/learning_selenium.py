from  selenium import webdriver
chrome_path = "C:\Development\chromedriver.exe"


driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

# closes the tab
# driver.close()

# closes the entire browser
driver.quit()