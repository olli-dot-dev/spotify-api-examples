#retrieve Spotify API token first, then use it to get track ID
#getting a track ID by searching for artist & track name

import requests, json

#Replace YourTrackName and Your%20artist with your track and artist name
#if either has spaces, replace them with %20 as in the example
#Searching for "YourTrackName" by "Your artist" in this example
#replace DE with your country code
query = "track:YourTrackName%20artist:Your%20artist&type=track&market=DE"
songURL = f"https://api.spotify.com/v1/search?q={query}"
headers = {
    #token is the Spotify API token you retrieved earlier
    "Authorization": "Bearer " + token
}

res = requests.get(url=songURL, headers=headers)

tmp=res.json()
if int(tmp['tracks']['total']) > 0:
    track_id=tmp['tracks']['items'][0]['id']
    print(track_id)
else:
    print("No matching result(s)")