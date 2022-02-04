from turtle import clear
from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news").text

soup = BeautifulSoup(res, "html.parser")

# print(soup.prettify())

titles = soup.select(".titlelink")
scores = [int(score.getText().split()[0]) for score in soup.select(".score")]
title_text = []
title_link = []

for title in titles:
    title_text.append(title.getText())
    title_link.append(title.get("href"))


print(scores)
# for i in range(0, len(title_text)):
#     print(f"{title_text[i]} {title_link[i]} {scores[i].getText()}")

# article_title = soup.find(class_="titlelink")
# article_link = article_title.get("href")
# article_upvotes = soup.find(class_="score")
# print(article_title.getText())
# print(article_link)
# print(article_upvotes.getText())
