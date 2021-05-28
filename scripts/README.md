#### Instructions for adding a new month
1. Create the mix on Spotify
2. Add a new file: `docs/collections/_months/<##-month>.md
3. Copy in the text from any previous month, and then update all values for the new month.
  - `intro` is an optional field; leave it out if there's nothing to say!
  - Get the `spotify_link_embedded` and `spotify_link_direct` from your Spotify playlist
  - Generate `permalink` for your month, e.g., 
  ```julia
  using UUIDs
  permalink = "01-$(uuid4())/01-january"
  ```
4. Generate the Spotify image for it by running
```
export SPOTIFY_CLIENT_ID=<your_client_id> # generate at https://developer.spotify.com/dashboard/
export SPOTIFY_CLIENT_SECRET=<your_secret> # ditto
export PLAYLIST_ID=<id> # This is the same value as `spotify_link_embedded`, above
python3 scripts/make_radar_plot.py
```