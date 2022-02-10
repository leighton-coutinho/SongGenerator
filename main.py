# Leighton Coutinho Student ID:261016919
import random
import utils
import requests
import json
#print(utils.get_lyrics("Brent Faiyaz","Clouded"))
print("Welcome to lyric generator! \n First we must train our generator")
print("In order to do this we need some songs with similar lyrics")
count = 0
myinput = ""
filelist = []
while myinput != "y":
    artistname = input("Please enter the artist name: ")
    songname = input("Please enter the song name: ")
    print("We will now create a lyric file of the song given then proceed to training.")
    myfile = artistname + str(count) + ".txt"
    utils.store_lyrics(utils.get_lyrics(artistname, songname), myfile)
    filelist.append(myfile)
    count += 1
    print("Generator trained with ", songname, " by ", artistname)
    print("Would like to stop? y/n \n (Accuracy will increase with amount of songs given)")
    myinput = input("Your Response: ")
    print("\n ********************************************************************")

mygrams = utils.get_grams_from_files(filelist, 4)
myword = utils.get_first_word(filelist[0])
print("Now printing your song: \n ***************************************************************")
print(utils.generate_text(mygrams, myword, 4, 1350))


'''utils.store_lyrics(utils.get_lyrics("Brent Faiyaz", "stay down"), "brent.txt")
utils.store_lyrics(utils.get_lyrics("Brent Faiyaz", "Let me Know"), "brent2.txt")
songgram = utils.get_grams_from_files(["brent.txt","brent2.txt"], 4)
#print(songgram)
print(utils.generate_text(songgram, 'when', 4, 1250))
'''