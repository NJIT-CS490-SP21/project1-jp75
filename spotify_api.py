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
        return tracks['name']           #get song name 
        
        
    def name_artist(tracks):
        return tracks['album']['artists'][0]['name']        #get name artist
    
    def song_img(tracks):
        return tracks['album']['images'][0]['url']          #ger song img
        
    def song_prev(tracks):
        prev = tracks['preview_url']            #get preview url
        if prev == None:
            return 'preview not available'      #if no song  return preview not available
        else:
            return prev 
            
    song = map(name_song,tracks)                #maps out all songs
    artist = map(name_artist,tracks)            #maps out all artist names
    img = map(song_img,tracks)                  #maps out all img urls
    preview = map(song_prev,tracks)             #maps out all preview urls

    return {
        'song': list(song),                     #creates a list of songs
        'artist': list(artist),                 #creates a list of artists
        'img': list(img),                       #creates a list of img urls
        'preview': list(preview),               #creates a list of preview urls
    }
    
    
def relatedGenres(id):
    url = "https://api.spotify.com/v1/artists/" + id + "/related-artists"
    response = requests.get(url,headers=headers)
    data = response.json()
    related = data['artists']
    
    
    genres = related[0]['genres']
    print(genres)
    
    if genres == []:
        genres = related[1]['genres']                   #all genres were already in a list some artists didn't have a related genere list at the 0th postion

        
    return {
        'related_genres': genres,                       #returned related genres that we got
    }
    
 