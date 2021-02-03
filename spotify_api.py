import requests,random,os
from dotenv import load_dotenv, find_dotenv

url = 'https://accounts.spotify.com/api/token'

load_dotenv(find_dotenv())
spotify_clientID = os.getenv('spotify_clientID')
spotify_secret = os.getenv('spotify_secret')

grant_type = 'client_credentials'
params = {'grant_type' : grant_type}

response = requests.post(url,
data = params,
auth=(spotify_clientID,spotify_secret)
)

access_token = response.json()['access_token']

headers = {
    'Authorization': 'Bearer ' + access_token
}
    
def topTracks(id):
    tracks = requests.get("https://api.spotify.com/v1/artists/" + id + "/top-tracks?market=US", headers=headers).json()["tracks"]
    trackList = []
    for track in tracks:
        trackList.append(track)
    return random.choice(trackList)