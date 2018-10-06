import os
import json
import random

#cmd  = 'curl -X "GET" "https://api.spotify.com/v1/search?q=happy&type=playlist&market=US&limit=1&offset=0" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQCmA_5JRLK-hq8--fg9W2bLGcpYBnGolQfTVgwaJ1_jRsd8Q7nODe4Z4h_M-8L680mrDvwllN4x881WvFkhBYOUb53e1MJAdBsJCgM4SBnCsgoXwl74ZPZut2MeT65a_JGz_XPVlwRnd331yJw3Mf_eQVofVyhhgQ"'
#cmd = cmd  + " >> outputFilezzz.txt"



motivate_list_playlisturls=['https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy','https://open.spotify.com/playlist/37i9dQZF1DXc5e2bJhV6pu','https://open.spotify.com/playlist/37i9dQZF1DX1OY2Lp0bIPp']
motivate_list_imgurls=['https://i.scdn.co/image/d1c8832a052ecb7ba41d01747a0296d756b40436','https://i.scdn.co/image/95112fcace768b32cf5ed7be504dd8839a2ce3cf','https://i.scdn.co/image/69d4e6fe29e8d0a03bd7e216666b71b3dc9cbf56']

happy_list_playlisturls=["https://open.spotify.com/playlist/37i9dQZF1DX84kJlLdo9vT","https://open.spotify.com/playlist/37i9dQZF1DX4uPi2roRUwU","https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU"]
happy_list_imgurls=["https://i.scdn.co/image/908dec5046876b5f72f045970488033df1b41407","https://i.scdn.co/image/a1f8040e8f297fff2d7be6efe8d1a0f250a30490","https://i.scdn.co/image/237dbe5ad6d3e8a60b0d79d5a6303cc531b56440"]

party_list_playlisturls=["https://open.spotify.com/playlist/37i9dQZF1DX5Ozry5U6G0d","https://open.spotify.com/playlist/37i9dQZF1DWVWiyE9VDkCO","https://open.spotify.com/playlist/37i9dQZF1DWTujiC7wfofZ"]
party_list_imgurls=["https://i.scdn.co/image/75c87793eccb82b52c8c3b94c3a4265958ec81c0","https://i.scdn.co/image/9a94da34de4e537c8e52c38765e59a772aa5d03f","https://i.scdn.co/image/25a980e6d5c4ea1bfb904a1288253d0201c2f911"]


#dels='rm outputFile.txt'
#os.system(dels)

#os.system(cmd)
#contentFromFile = open("outputFile.txt", 'r').read()

#jsonObj = json.loads(contentFromFile)
#url  = (jsonObj['playlists']['items'][0]['external_urls']['spotify'])
#imageUrl = (jsonObj['playlists']['items'][0]['images'][0]['url'])
#print(url)
#print(imageUrl)

f=open("score.txt","r")

hq=0
for x in f:
	hq=float(x)

playlist=""
img=""

r=random.randint(1,3)-1;

if hq<=-0.5:	
	playlist=motivate_list_playlisturls[r]
	img=motivate_list_imgurls[r]
elif hq<=0.5:
	playlist=happy_list_playlisturls[r]
	img=happy_list_imgurls[r]
else:
	playlist=party_list_playlisturls[r]
	img=party_list_imgurls[r]


fo=open("songs.txt","w")
fo.write(playlist)
fo.write("\n")
fo.write(img)





