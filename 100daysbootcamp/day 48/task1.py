from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

driver.get("https://en.wikipedia.org/wiki/Main_Page")
num = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text


# we can select specific link by using link_text and the name in the list 
links = driver.find_element(By.LINK_TEXT, num)
links.click()
# while True:
#     pass

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.RETURN)


# automatically form fill up 
driver.get("https://secure-retreat-92358.herokuapp.com/")


fname = driver.find_element(By.NAME, 'fName')
fname.send_keys("suman")

lname = driver.find_element(By.NAME, 'lName')
lname.send_keys("pokhrel")

email = driver.find_element(By.NAME, 'email')
email.send_keys("11pok@gmail.com")

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

# while True:
#     pass

