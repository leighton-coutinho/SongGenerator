# Leighton Coutinho Student ID:261016919
import random
import utils
import requests
import json

# idea is to ask user for lyrics then use get_grams_from_files() and generate_text() to build a song

# vari#
# create the file
utils.store_lyrics(utils.get_lyrics("Brent Faiyaz", "stay down"), "brent")
songgram = utils.get_grams_from_files(["brent"], 4)
#print(songgram)
print(utils.generate_text(songgram, 'when', 4, 1250))
