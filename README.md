Copy this repository
_________________________________________________________________________________________________________
1. In Cloud9 terminal, in your home directory, clone the repo:git clone https://github.com/NJIT-CS490-SP21/project1-jp75


Sign up for Spotify Developer Account
_________________________________________________________________________________________________________
1. Go to the link https://developer.spotify.com/dashboard/login and login or signup
2. Click create an app or click on an existing app that you created to get the Client and Secret key
3. Save the Client ID and Client Secret keys as you're going to need them to get the application working.

Sign up for Genius Developer Account
_________________________________________________________________________________________________________
1. Go to the link https://genius.com/developers
2. Create an api client
3. Signup or login to an existing account to so this
3. Get the app website url from your spotify app website
4. Generate token and save it as you're going to need it to get your application to work.


Install Requirements(if you don't already have them)
_________________________________________________________________________________________________________
1. pip install Flask
2. pip install requests
3. pip install python-dotenv


.env file setup
_________________________________________________________________________________________________________
1. Create .env file in your project or environment directory
2. Add your client Id with the line: export spotify_clientID='YOUR_KEY'
3. Add your Secret key with the line: export spotify_secret='YOUR_KEY'
4. Add you genius api access token with the line: export genius_token='YOUR_KEY'


Run Application
_________________________________________________________________________________________________________
1. In app.py from line 10-13 you're more than welcomed to add/change any of the artist_IDs 
2. Run command in terminal python app.py. If that doesn't work view the app.py file and click run on the top of cloud 9
3. Preview web page in browser and refresh to view another song.


If you want to apply it into a heroku server(not required)
_________________________________________________________________________________________________________
1. install "npm install -g heroku" in your terminal
2. go to heroku.com and create an account
3. I already created the Procfile and the requirements file so just login into heroku using "heroku login -i"
4. create a new heroku app by typing in "heroku create"
5. Push the code into your heroku application using "git push heroku main"
6.  go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars"
7.  Copy and paste your keys: "spotify_clientID, spotify_secret, and genius_token" and the key without the '' in your .env file
8.  run your app using heroku open in terminal or going to the website that was provided when creating the heroku app
an example of a running app is right here: https://topify-cs490.herokuapp.com/


Future additions
_________________________________________________________________________________________________________
1. I implemented a way for people to see the similar genres of the current artist that's on the list. If I had more time I would've like to go more in-depth with that by giving a list of artists in the specific genres as if someone likes the song that they're listening to they would possibly like those similar artists. To do this I would have to search more in-depth with Spotify API as the current one I've been using is "https://api.spotify.com/v1/artists/{id}/related-artists" and feel that maybe I could use this to get the artists, and then go through top tracks again to get their top tracks. Then in my HTML file, I could make a list just to get the similar artists top tracks so someone could view it. The way I would go about doing that is to make a loop that goes through the list and prints the name of the songs one by one.
2. I would have liked to add a search feature that would allow people to type in a specific artist's name and then parse or gather their id and put it into the list of artist_IDs. To do this I found some documentation in Spotify API to get a search of an artist using https://api.spotify.com/v1/search. From this, I would need to implement {q: "Name of search" + "&" + "Name of type(Album, Artist, track)"} this will display all info of the search and I saw that I would be able to get the ID's in there and somehow I could return that and then append it into my list and display the song. I could see how this could be an issue because when you refresh your page it re-runs through your list so I would need to make there a way that it includes the new ID to the list, but feel like this is very possible.


Technical issues encountered
________________________________________________________________________________________________________
1. The first technical issue I was having issues with was figuring out how to get the access token to work. This link defintely helped me https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow. Although it took me many hours to figure it out I also viewed a few youtube videos and tried to see how they approached it. This link guided me in the right direction even though it was a different flow https://www.youtube.com/watch?v=yAXoOolPvjU&t=774s&ab_channel=API-University. The reason I believe it was hard for me was because I started this part before we learned how to use apis in class so that might have been a reason that it took me so long, but I finally figured it out and one of the most helpful things was figuring out the grant type and figuring out how to give authorization.
2. Another technical issue I ran into was displaying the top track info using .json(). When I would try to get the name of the song, name of the artist, album image, and song preview I was having trouble navigating through. The approach I took to get through this was to go one by one to find the information I needed. I started with ['album'] and then compiled to see what I got, then went to ['album']['artist'] and checked,etc. This approach helped me because for a while I was just guessing and it took me over 30 minutes to figure it out. Once I started that new approach I finished a lot quicker with tthe issue and got it to work.
3. Another problem I had was with the preview url. Sometimes I would encounter an artist where their song would not have a preview url and every other song would come up as an error. The way I first encountered it was if the url wasn't there it would simply go to another song that had a preview url and display it. After working around this for sometime I finally figured it out that I had to make a condition that stated if there was no preview url to append 'no preview url' rather than it going to a new artist who had a url link.
4. I encountered an issue when I thought I finished my project. After thinking I finished I ended up occasionally getting an error with my app from Heroku and did some investigating only to find out there were certain flaws in my program that wouldn't work. If I gt a Spotify id for someone with only one song it would give me an error because I'm assuming only because they had one song and it would assume top tracks would have 10. Another issue I had was when I put one artist id in the list it would sometimes give me an error I assume because random.choice() would need to be used on something with more than one in a list. Anyways the way I fixed my issues is to scrap the whole top tracks and artist_info fields and I followed a different route from tutorials on the NYT project by defining fields for each category and mapping it out. Then in my app.py file, I got the number of songs from each artist that processed and then randomly chose one. From here I pushed all the info at a random number. This way is definitely more efficient as I feel like my program runs a lot quicker and works with artists with 1 or more songs.
