import requests
from bs4 import BeautifulSoup as BS
from ytmusicapi import YTMusic as YT

# --------------------------------------------------------
# Scraping the Billboard Top 100 for September 26, 2026  #
# --------------------------------------------------------
URL = "https://appbrewery.github.io/bakeboard-hot-100"
top_100 = []

desired_year = "2000-08-12"

response = requests.get(f"{URL}/{desired_year}")
billboard_page = response.text

billboard_soup = BS(billboard_page, "html.parser")
songs = billboard_soup.find_all(name="h3", class_="chart-entry__title")
top_100 = [song.getText() for song in songs]
# print(top_100)

# ----------------------------
# YouTube Music API Request #
# ----------------------------
yt = YT("browser.json")
playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")

playlistID = yt.create_playlist(
    f"{desired_year} Billboard 100", "Python API Top 100", privacy_status="PRIVATE"
)
print("Playlist Created")

# Go through top_100 and search through ytmusic, if exists add to list.
for song in top_100:
    try:
        new_song = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlistID, [new_song[0]["videoId"]])
        print(f"Added {song}")
    except Exception as e:
        print(f"Skipped {song} | Reason: {e}")
