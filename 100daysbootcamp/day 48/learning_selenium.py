from  selenium import webdriver
chrome_path = "C:\Development\chromedriver.exe"


driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# close the tab using close and for browser use quit method
# driver.close()
donate = driver.find_element(by = "class_name", value="donate-button")
print(donate.text)
# closes the entire browser
driver.quit()