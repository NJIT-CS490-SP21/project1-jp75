from flask import Flask, render_template
import os,random
from spotify_api import topTracks, track_info
from genius_api import getLyrics

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    artist_IDs = ['74XFHRwlV6OrjEM0A2NCMF', #paramore
    '6XyY86QOPPrYVGvF9ch6wz',            #Linkin Park
    '3TVXtAsR1Inumwj472S9r4'            #Drake
    ]
    
    artist_id = random.choice(artist_IDs)       #picks a random artist

    random_track = topTracks(artist_id)         #gets the information from spotify api def Toptracks
    Top_info = track_info(random_track)         #parses info of the Toptracks in Track_info
    Top_info = random.choice(Top_info)          #choses a random song and returns the info from it
    info = Top_info.split(',')                  #splits info into song name, artist name, album url, preview url
    
    lyrics = getLyrics(info)                    #gets lyrics url for song
    print(lyrics)                               #sometimes drake songs don't post the right lyric page

 
    return render_template(
        "index.html",
        artist_id = random.choice(artist_IDs),
        random_track = topTracks(artist_id),
        displayInfo = info, 
        lyrics_url = lyrics
    )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    )