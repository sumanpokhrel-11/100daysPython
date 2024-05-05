from bs4 import BeautifulSoup
with open("100daysbootcamp\day 45\website.html", encoding="utf-8") as file:
    contents = file.read()


# for extracting html file use html.parser and for xml file use xml.parser
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
list_tag = soup.find_all(name = 'li')
for li in list_tag:
    print(li.getText())

# get all the content of attribute
anchor_tag = soup.find_all(name="a")
for tag in anchor_tag:
    print(tag.get("href"))


# we can use the parameters id, class for specific output
head = soup.find(name='h1', id= 'name')
print(head)


# this is the way of getting the data of class using class_ 
sec_head = soup.find(name="h3", class_ = "heading")
print(sec_head)


# selecting the specific elements in a website where there could be thousands of same tag

my_url = soup.select_one(selector="p a")
print(my_url)

# selecting the data based on class which is be stored in list format
print(soup.select(".heading"))