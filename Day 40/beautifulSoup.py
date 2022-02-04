from bs4 import BeautifulSoup
import os
import requests

f = requests.get("https://1lib.in/s/alpha?").text
soup = BeautifulSoup(f, "html5lib")
print(soup.a.text)
