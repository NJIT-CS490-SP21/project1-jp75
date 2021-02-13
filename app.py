from flask import Flask, render_template
import os,random
from spotify_api import topTracks, relatedGenres
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
    random_tracks = topTracks(artist_id)
    related = relatedGenres(artist_id)
    
    num_genres = len(related['related_genres'])
    
    #print(random_tracks)
    
    numSongs = len(random_tracks['song'])
    #print(numSongs)
    
    randNum = random.randint(0,numSongs-1)
    
    
    song = random_tracks['song'][randNum]
    artist = random_tracks['artist'][randNum]
    img = random_tracks['img'][randNum]
    preview = random_tracks['preview'][randNum]
    lyrics = getLyrics(song,artist)
    
    
    
    #print(lyrics)

 
    return render_template(
        "index.html",
        random_track = topTracks(artist_id),
        song = song,
        artist = artist,                            #did it this way so I could make it neater with found lyrics
        img = img,
        preview = preview,
        lyrics = lyrics,   
        related_genres = related['related_genres'],
        num = num_genres
    )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    )