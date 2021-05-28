import os
import pathlib
import requests
import pandas as pd
from math import pi
import matplotlib.pyplot as plt

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

r = requests.get(BASE_URL + 'playlists/'+ PLAYLIST_ID + '/tracks', headers = headers, params=playlistParams).json()
track_ids = [x['track']['id'] for x in r['items']]


#Get Each Song's Attributes
songParams = {
    'ids': ','.join(track_ids)
}
r = requests.get(BASE_URL + 'audio-features', headers = headers, params = songParams )
d = r.json()
df = pd.DataFrame([x for x in d['audio_features']])
df = df.loc[:,['danceability','energy','acousticness','instrumentalness','valence']]

#Calculate Average Attribute Values for Playlist
df_mean = pd.DataFrame(df.mean())
df_mean.index.name = 'Characteristic'
df_mean.reset_index(inplace=True)
df_mean = df_mean.rename(columns = {0:'Value'})

#Create variables for plotting
Attributes = df_mean['Characteristic']
AttNo = len(df_mean['Characteristic'])
values = list(df_mean['Value'])
values += values[:1] #Close loop by adding first characteristic value again

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

#Plot and save radar chart
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1],Attributes)
ax.plot(angles,values)
ax.fill(angles, values, 'purple', alpha=0.5)
ax.yaxis.set_visible(False)
plt.savefig("./docs/assets/radar_plot_" + PLAYLIST_ID)
ax.clear()