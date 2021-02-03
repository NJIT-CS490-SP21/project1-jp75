from flask import Flask, render_template
import os,random

app = Flask(__name__)


@app.route('/')
def index():
    artist_IDs = ['74XFHRwlV6OrjEM0A2NCMF', #paramore
    '6XyY86QOPPrYVGvF9ch6wz',            #Linkin Park
    '0C0XlULifJtAgn6ZNCW2eu'             #The Killers
    ]
 
    return render_template(
        "index.html",
        artist_id = random.choice(artist_IDs)
        
    )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
    )