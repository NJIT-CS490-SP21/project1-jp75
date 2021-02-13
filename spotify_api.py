import requests,os
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
    url = "https://api.spotify.com/v1/artists/" + id + "/top-tracks?market=US"
    response = requests.get(url, headers=headers)
    data = response.json()
    tracks = data['tracks']         #the map
    
    def name_song(tracks):
        return tracks['name']
        
    def name_artist(tracks):
        return tracks['album']['artists'][0]['name'] 
    
    def song_img(tracks):
        return tracks['album']['images'][0]['url']
        
    def song_prev(tracks):
        prev = tracks['preview_url']
        if prev == None:
            return 'preview not available'
        else:
            return prev
            
    song = map(name_song,tracks)
    artist = map(name_artist,tracks)
    img = map(song_img,tracks)
    preview = map(song_prev,tracks)

    return {
        'song': list(song),
        'artist': list(artist),
        'img': list(img),
        'preview': list(preview),
    }
    
 