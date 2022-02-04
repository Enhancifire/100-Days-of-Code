import datetime as dt
import requests

response = requests.request("GET", url="https://asurascans.com")
print(response)

now = dt.datetime.now()

year = now.year

print(year)
