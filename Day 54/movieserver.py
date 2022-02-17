import json, requests

apikey = ""


def connect():
    global apikey
    with open("api.json", "r") as f:
        data = json.load(f)
        apikey = data["api_key"]

    return apikey


def search(movie):
    global apikey
    url = "https://api.themoviedb.org/3/search/movie?"
    movie_url = "%20".join(movie.split(" "))
    query = f"{url}api_key={apikey}&query={movie_url}&page=1"

    res = requests.get(query)

    data = res.json()
    results = data["results"]

    movieList = []

    for result in results:
        try:
            temp = [
                result["original_title"],
                result["overview"],
                result["id"],
                result["release_date"],
            ]

            movieList.append(temp)
        except:
            pass

    return movieList
