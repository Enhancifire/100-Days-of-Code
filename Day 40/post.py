import requests

USERNAME = "fs144rules"
TOKEN = "ababbabaababbaba"
URL = "https://pixe.la/v1"
graph_endpoint = f"{URL}/users/{USERNAME}/graphs"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

res = requests.post(url=URL, json=params)
print(res)
print(res.json())
