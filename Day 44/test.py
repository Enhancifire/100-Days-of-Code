import requests
from bs4 import BeautifulSoup
import lxml

import smtplib

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
acc_lang = "en-US,en;q=0.9"

headers = {
    "User-Agent": user_agent,
    "Accept-Language": acc_lang,
}
# https://www.amazon.in/Kindle-10th-Gen/dp/B07FQ4Q7MB/ref=sr_1_1?crid=1EFD9I5NW6E9H&keywords=kindle&qid=1643262149&sprefix=kindle%2Caps%2C492&sr=8-1
url = "https://www.amazon.in/Kindle-10th-Gen/dp/B07FQ4Q7MB/"

res = requests.get(
    headers=headers,
    url=url,
)

soup = BeautifulSoup(res.text, "lxml")

elem = soup.select_one("#productTitle").text


print(elem)
