import requests,os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

genius_clientID = os.getenv('genius_clientID')
genius_secret = os.getenv('genius_secret')
genius_token = os.getenv('genius_token')

headers = {
    'Authorization': 'Bearer ' + genius_token
}
    
def getLyrics(info):
    name_song = info[0]
    name_artist = info[1]
    url = 'https://api.genius.com/search'
    data = {'q': name_song + ' ' + name_artist}
    response = requests.get(url, data = data, headers = headers).json()['response']['hits'][0]['result']['url']
    return response

