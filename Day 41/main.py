import os
from bs4 import BeautifulSoup

with open("Day 41/website.html", "r") as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.h1)
