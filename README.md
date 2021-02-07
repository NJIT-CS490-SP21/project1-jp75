
Sign up for Spotify Developer Account
_________________________________________________________________________________________________________
1. go to the link https://developer.spotify.com/dashboard/login and login or signup
2. click create an app or click on an existing app that you created to get the Client and Secret key
3. save the Client ID and Client Secret keys as you're going to need them to get the application working.

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
4. In app.py from line 10-13 you're more than welcomed to add/change any of the artist_IDs 

Run Application
_________________________________________________________________________________________________________
1. Run command in terminal python app.py. If that doesn't work view the app.py file and click run on the top of cloud 9
2. Preview web page in browser and refresh to view another song.

Future additions
_________________________________________________________________________________________________________
1. Will be implementing a play button on the bottom of the preview page to hear a song preview. To do this task I will need to create a button that acts as a link to play the song in the provided url link without having it go to a new page. This will involve HTML/CSS and i'm planning on using https://www.w3schools.com/tags/tag_audio.asp. The approach I will try to use test it out is below.
<audio controls>
  <source src="https://www.exaple.mp3" />
</audio>
2. I am planning on implementing a way for people to see what genre of music the person they're listening to is. If they happen to like the type of music they could click that link and it'll give them a list of the top artists in that genre. The way I would have to go about doing this is to use Artist API in spotify developer and get the genre catagory id. I would have to parse through using .json() like with the top tracks In order to get that I would have to create a get method in my spotify_api.py and implement te following code.
def searchGenre(id):
    userInfo = []
    genreUser = requests.get("https://api.spotify.com/v1/browse/categories/" + id, headers=headers).json()
    for i in genreUser:
        userInfo.append(i)
This isn't 100% though through but this will be the approach I start to take.


Technical issues
________________________________________________________________________________________________________
1. The first technical issue I was having issues with was figuring out how to get the access token to work. This link defintely helped me https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow. Although it took me many hours to figure it out I also viewed a few youtube videos and tried to see how they approached it. This link guided me in the right direction even though it was a different flow https://www.youtube.com/watch?v=yAXoOolPvjU&t=774s&ab_channel=API-University. The reason I believe it was hard for me was because I started this part before we learned how to use apis in class so that might have been a reason that it took me so long, but I finally figured it out and one of the most helpful things was figuring out the grant type and figuring out how to give authorization.
2. Another technical issue I ran into was displaying the top track info using .json(). When I would try to get the name of the song, name of the artist, album image, and song preview I was having trouble navigating through. The approach I took to get through this was to go one by one to find the information I needed. I started with ['album'] and then compiled to see what I got, then went to ['album']['artist'] and checked,etc. This approach helped me because for a while I was just guessing and it took me over 30 minutes to figure it out. Once I started that new approach I finished a lot quicker with tthe issue and got it to work.
2. Another problem I had was with the preview url. Sometimes I would encounter an artist where their song would not have a preview url and every other song would come up as an error. The way I first encountered it was if the url wasn't there it would simply go to another song that had a preview url and display it. After working around this for sometime I finally figured it out that I had to make a condition that stated if ther was no preview url to append 'no preview url' rather than it going to a new artist who had a url link.