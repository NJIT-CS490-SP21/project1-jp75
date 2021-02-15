from flask import Flask, render_template
import os,random
from spotify_api import topTracks, relatedGenres
from genius_api import getLyrics

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    artist_IDs = ['74XFHRwlV6OrjEM0A2NCMF', #Paramore
    '6XyY86QOPPrYVGvF9ch6wz',            #Linkin Park
    '4MCBfE4596Uoi2O4DtmEMz'            #Juice WRLD
    ]
    
    artist_id = random.choice(artist_IDs)       #picks a random artist
    random_tracks = topTracks(artist_id)        #gets top tracks of random artist form spotify api
    related = relatedGenres(artist_id)          #gets related genres from spotify api
    
    num_genres = len(related['related_genres']) #gets the len of num genres to make a for loop in html
    
    #print(random_tracks)
    
    numSongs = len(random_tracks['song'])       #gets num of songs in top tracks for an artist
    #print(numSongs)
    
    randNum = random.randint(0,numSongs-1)      #choses a random # from 0- number of songs -1 so we dont get an out of bounds error
    
    
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
        artist = artist,                            #did it this way so I could make it neater with found lyrics, need to declare song and artist before getting lyrics. This is the best way I could get it to work.
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