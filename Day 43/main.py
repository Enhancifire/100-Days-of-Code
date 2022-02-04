import requests, spotipy, json
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


def retConObject():
    with open("client.json") as f:
        jsonified = json.load(f)

    clientId = jsonified["clientId"]
    clientSecret = jsonified["clientSecret"]
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=clientId,
            client_secret=clientSecret,
            redirect_uri="http://example.com",
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path="token.txt",
        )
    )
    currentUser = sp.current_user()
    user_id = currentUser["id"]
    return sp, user_id


def search(sp, date, titles):
    song_uri = []
    year = date.split("-")[0]

    for title in titles:
        res = sp.search(q=f"track:{title} year:{year}", type="track")
        try:
            uri = res["tracks"]["items"][0]["uri"]
            song_uri.append(uri)
        except IndexError:
            print(f"Song {title} doesn't exist on Spotify. Skipping")

    return song_uri


def createPlaylist(sp, user_id, date, uri_list):
    description = f"Contains the Top 100 songs for {date}"
    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"{date}'s Top 100 Songs",
        public=False,
        description=description,
    )
    try:
        sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
    except:
        print("Exception Thrown")


def main():
    sp, user_id = retConObject()
    date = input(
        "Which date do you want to be reminded of? Enter the date in the YYYY-MM-DD format: "
    )

    res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text

    soup = BeautifulSoup(res, "html.parser")

    h3list = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")
    titles = [title.getText().replace("\n", "") for title in h3list]
    song_uri = search(sp, date, titles)

    createPlaylist(sp, user_id, date, song_uri)


if __name__ == "__main__":
    main()
