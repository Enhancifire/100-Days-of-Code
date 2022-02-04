from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(URL).text

soup = BeautifulSoup(res, "html.parser")

# titles = soup.select(".jsx-4245974604 h3")

# print(titles)

# <h3 class="jsx-4245974604">100) Reservoir Dogs</h3>
#
print(soup.prettify())
