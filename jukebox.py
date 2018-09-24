name = "BrandonDavis"
date = "9/24"
project = "jukebox"
make_jukebox = {
    'artist_one': "J.Cole",
    'artist_two': "Kendrick Lamar",
    'artist_three': "Childish Gambino",
    }
import random
j_cole=["Work Out", "No Role Modelz", "Apparently"]
k_lamar=["Hiiipower", "Swimming Pools", "Hol' Up"]
c_bino=["3005", "Sweatpants", "That Power"]
print (f"Artists are J.Cole, Kendrick Lamar, Childish Gambino.")

while True:
        artist = input("What artist do you choose to listen to? Insert X if you choose to exit.")
        if artist == "J.Cole":
                song = random.choice(j_cole)
                print(f"Now playing...%s" %song)
        elif artist =="Kendrick Lamar":
                songs = random.choice(k_lamar)
                print(f"Now playing...%s" %songs)
        elif artist =="Childish Gambino":
                songz = random.choice(c_bino)
                print(f"Now playing...%s" %songz)
        if artist.strip() == "X":
                break 

    
