from bs4 import BeautifulSoup
import requests

def extract_article_info(url):
  """
  Extracts titles, links, and upvote scores for articles in the given URL.

  Args:
      url: The URL of the webpage containing articles.

  Returns:
      A list of dictionaries, where each dictionary represents an article
      with keys 'title', 'link', and 'score'.
  """

  response = requests.get(url)

  if response.status_code == 200:
    yc_webpage = response.text
  else:
    print(f"Error: Failed to get webpage content for {url}.")
    return []  # Empty list on error

  soup = BeautifulSoup(yc_webpage, 'html.parser')

  articles_info = []
  for headline in soup.select(".titleline"):
    article_info = {}

    # Get title
    # here i am using split method in order to remove the last word as it is just domain or half-link
    article1 =  headline.getText().split()[:-1]
    # here i am joining the list of words using space so that the readability occurs
    article_info['title'] =' '.join(article1)

    # Get link
    anchor_tag = headline.find("a")
    if anchor_tag:
      article_info['link'] = anchor_tag.get("href")
    else:
      article_info['link'] = None

    # Get upvote score (assuming only one score per headline)
    my_list = [score.getText() for score in soup.find_all("span", class_ = "score")]
    i = 1
    for i in range(len(my_list)):
      article_info['score'] = my_list[i]
      continue

    i +=1
    articles_info.append(article_info)

  return articles_info

# Example usage
url = "https://news.ycombinator.com/news"
articles_info = extract_article_info(url)

# Print information for each article
for article in articles_info:
  print(f"Title: {article['title']}")
  print(f"Link: {article['link']}")
  print(f"Upvote Score: {article['score']}")
    
  print("---")
