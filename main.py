# Leighton Coutinho Student ID:261016919
import random
import utils
import requests
import json

# idea is to ask user for lyrics then use get_grams_from_files() and generate_text() to build a song

#variables
artist = "Brent Faiyaz"
song_title = "stay down"
url = "https://api.lyrics.ovh/v1/" + artist + '/' + song_title

#fetch lyrics
response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']
print(lyrics)
