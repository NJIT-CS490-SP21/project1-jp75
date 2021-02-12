import requests,os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

genius_token = os.getenv('genius_token')

headers = {
    'Authorization': 'Bearer ' + genius_token
}
    
def getLyrics(info):
    name_song = info[0]                                 #name of the song from list
    name_artist = info[1]                               #name of the artist from list
    url = 'https://api.genius.com/search'
    data = {'q': name_song + ' ' + name_artist}         #genius api uses q=Kendrick%20Lamar 
    response = requests.get(url, data = data, headers = headers).json()['response']['hits'][0]['result']['url']     #parses lyrics url
    return response

