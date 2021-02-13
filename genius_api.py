import requests,os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

genius_token = os.getenv('genius_token')

headers = {
    'Authorization': 'Bearer ' + genius_token
}
    
def getLyrics(name, artist):

    url = 'https://api.genius.com/search'
    data = {'q': name + ' ' + artist}         #genius api uses q=Kendrick%20Lamar 
  
    response = requests.get(url, data = data, headers = headers)
    data = response.json()
    link = data['response']
    print(link)
    
    page = link['hits'][0]['result']['url']
    
    return page

