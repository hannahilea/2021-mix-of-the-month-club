
## {{page.month}}'s Mix
{% for playlist in site.data.playlists %}
{% if playlist.month == page.month and playlist.year == page.year %}

<iframe src="https://open.spotify.com/embed/playlist/{{playlist.playlistID}}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>

[_[direct link to this same playlist on Spotify]_](https://open.spotify.com/playlist/{{playlist.playlistID}}?si=GpSW_X-NRZG97Jx_NCPm3Q)

{% if playlist.image_loc %}
#### Playlist Characteristics


![{{ playlist.month }}-{{ playlist.year }} Radar Chart]({{ playlist.image_loc | prepend: ".." }})
{% endif %}
{% endif %}
{% endfor %}
