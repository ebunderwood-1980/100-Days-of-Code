from bs4 import BeautifulSoup as BS
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# Get the HTML text from the website
soup = BS(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

# Lists to hold data from the html parsing
article_texts = []
article_links = []
article_upvotes = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.find(name="a").get("href"))

upvotes = [int(item.getText().split(" ")[0]) for item in soup.find_all(class_="score")]

max_upvotes_index = upvotes.index(max(upvotes))
print(
    f"Text={article_texts[max_upvotes_index]}\nLink={article_links[max_upvotes_index]}\nUpvotes={upvotes[max_upvotes_index]}"
)
