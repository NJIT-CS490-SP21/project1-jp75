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
    tracks = requests.get("https://api.spotify.com/v1/artists/" + id + "/top-tracks?market=US", headers=headers).json()['tracks']
    trackList = []

    for track in tracks:
        trackList.append(track)
    return trackList

def track_info(trackList):
    infol = []
    for i in range(len(trackList)):
        name_song = trackList[i]['name']
        name_artist = trackList[i]['album']['artists'][0]['name'] 
        song_img = trackList[i]['album']['images'][0]['url']
        song_prev = trackList[i]['preview_url']
        
        if song_img != None and song_prev != None:
            infol.append(name_song + ', ' + name_artist + ', ' + song_img + ', ' + song_prev)
        else:
            continue
    return infol