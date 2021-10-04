import os
import pathlib
import requests
import pandas as pd

# Get Playlist Item Ids
AUTH_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID") 
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET") 
PLAYLIST_ID = os.getenv("PLAYLIST_ID")
BASE_URL = 'https://api.spotify.com/v1/'

if not CLIENT_ID:
    print("client id is empty")
if not CLIENT_SECRET:
    print("client secret is empty")
# Authentication 
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# Get tracks in a playlist
playlistParams = {
    'market': 'US',
    'fields': 'items(track(id))'
}

playlist_ids = [x.replace(".png", "").replace("radar_plot_", "") for x in os.listdir(path="docs/assets") if x.startswith("radar_plot")]
monthly_playlists = ""
all_songs = []
for playlist_id in playlist_ids:
    title = requests.get(BASE_URL + 'playlists/'+ playlist_id, headers = headers).json()['name']

    r = requests.get(BASE_URL + 'playlists/'+ playlist_id + '/tracks', headers = headers, params=playlistParams).json()
    track_ids = [x['track']['id'] for x in r['items']]

    # Get each song's attributes
    songParams = {'ids': ','.join(track_ids)}
    r = requests.get(BASE_URL + 'tracks', headers = headers, params = songParams )
    deets = ""
    for t in r.json()["tracks"]:
        song_str = t["name"] + " [" + ', '.join([a["name"] for a in t["artists"]]) + "]"
        deets += song_str + "\n"
        all_songs.append(song_str)
        if len(all_songs) > len(set(all_songs)) + 1: # fergal's tune is known duplicate may+june...
            print("Oh no, non-unique song list as of " + title + "! " + song_str)

    monthly_playlists += title + "\n*******\n" + deets + "\n"
    if len(all_songs) > len(set(all_songs)) + 1:
        print("Oh no, non-unique song list as of " + title + "!")
    else:
        print("...songs unique as of " + title + "...")

# overwrite file
f = open("docs/assets/all_playlists.txt", "w")
f.write(monthly_playlists)
f.close()