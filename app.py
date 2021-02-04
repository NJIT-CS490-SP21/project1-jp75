from flask import Flask, render_template
import os,random
from spotify_api import topTracks, track_info

app = Flask(__name__)


@app.route('/')
def index():
    artist_IDs = ['74XFHRwlV6OrjEM0A2NCMF', #paramore
    '6XyY86QOPPrYVGvF9ch6wz',            #Linkin Park
    '3TVXtAsR1Inumwj472S9r4'             #Drake
    ]
    
    artist_id = random.choice(artist_IDs)

    random_track = topTracks(artist_id)
    Top_info = track_info(random_track)
    
    try:
        Top_info = random.choice(Top_info)
        #print(Top_info)
    except:
        index()
    
    info = Top_info.split(',')
    #print(type(info))
 
    return render_template(
        "index.html",
       artist_id = random.choice(artist_IDs),
       random_track = topTracks(artist_id),
       displayInfo = info
    )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    )