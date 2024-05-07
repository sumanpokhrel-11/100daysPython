from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

# Print the page title (optional)
# print(soup.title)

# Get all headlines with class "titleline"
headlines = soup.select(".titleline")
titles = []
links = []
# Loop through each headline
for headline in headlines:
  # Get the text content of the headline (title)
  headlinesss = headline.getText().split()[:-1]
  headliness = " ".join(headlinesss)
  titles.append(headliness)
  # print(headline.getText())
# title = [headline.getText() for headline in soup.select(".titleline")]
  # Find the anchor tag within the current headline
  anchor_tag = headline.find("a")

  # Check if anchor tag exists (might not be present for all headlines)
  if anchor_tag:
    # Extract the link (href attribute)
    href_tag = anchor_tag.get("href")
    links.append(href_tag)
  #   print(f"Link: {href_tag}")
  # else:
  #   print("No link found for this headline.")

  # Find the upvote element within the current headline's parent
  # upvote = soup.find_all("span", class_="score")  # Look for upvote in parent element

  # for vote in upvote:
  #   print(f"Upvote Score: {vote.getText()}")
  my_list = [int(score.getText().split()[0]) for score in soup.find_all("span", class_ = "score")]


#finding the highest score in the list and printing the title and link of that score
my_list.sort()
highest = my_list[-1]
my_list = [int(score.getText().split()[0]) for score in soup.find_all("span", class_ = "score")]
position = my_list.index(highest)
high_title = titles[position]
high_link = links[position]
  

# printing the highest upvoted title, it's link and it's score
print(f"The highest upvoted title is{high_title} and it's link is {high_link} with voting {highest}")
