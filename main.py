'''
DEVELOPER(S): Linnette Arellano
COLLABORATORS: Lab 12, Loteria lab, My UD 1 and UD 2
DATE: April 25, 2026
'''

"""
A generator that creates playlist based off of energy and mood or user can personalize one


"""

import random

def get_choice():
    choice = input("\nDo you wish to generate a (R)eccomended playlist or (C)ustom playlist? (R/C)? ")
    choice = choice.upper()

    ## If user input 'custom' or 'do it yourself' or 'diy'. the code will only focus on the first letter
    if choice == "R" or choice == "RECcomended":
        return "R"
    elif choice == "C" or choice == "CUSTOM":
        return "C"
    else:
        print("Invalid response, please try again.") #recursion
        return get_choice()

def get_user_info():
    #name
    name = input("\nWhat is your name? ")
    return name

def get_mood_energy():
    #mood
    mood = ""
    while mood not in ["happy", "calm", "sad"]:
        mood = input("How are you feeling today? (happy, calm, or sad) ").lower()
        if mood not in ["happy", "calm", "sad"]:
            print(" Please enter one choice: happy, calm, or sad.")
    #energy level
    energy_lvl = "N/A"
    if mood != "sad":
        while True:
            energy_input = input("Rate your energy from 1 to 10: ")
            if energy_input.isdigit() and 1 <= int(energy_input) <= 10:
                energy_lvl = int(energy_input)
                break
            print("Just type a number 1-10.")
    return  mood, energy_lvl


#program's custom playlist
def generate_playlist(mood, energy_lvl):
    #I used a dictionary because I found it easier to see 'key' values
    playlists = {
        "happy_high": {
            "title": " -- Happy + Energetic -- ",
            "songs": ["Juice by Iyla", "Todo de Ti by Rauw Alejandro", "Slide by Calvin Harris", "IDOL by BTS"]
        },
        "happy_low": {
            "title": " -- Chill + On Repeat -- ",
            "songs": ["Nice to Each Other by Olivia Dean", "Naive by The Kooks", "Ayonha by Hamid Al Shaeri"]
        },
        "calm_high": {
            "title": " -- Lazy Sunday Vibes! -- ",
            "songs": ["Sundays by Emotional Oranges", "Tu by Maye", "The Dress by Dijon"]
        },
        "calm_low": {
            "title": " --- Focus Flow! -- ",
            "songs": ["Intro by STRFKR", "Cerca de Ti", "Friday Morning by Khruangbin"]
        },
        "sad": {
            "title": "-- Don't Listen if You're Heartbroken -- ",
            "songs": ["Feeling Whitney by Post Malone", "Liability by Lorde", "Comedown by Josef"]
        }
    }


    if mood == "happy" and energy_lvl != "N/A" and energy_lvl > 5:
        key = "happy_high"
    elif mood == "happy":
        key = "happy_low"
    elif mood == "calm" and energy_lvl != "N/A" and energy_lvl > 5:
        key = "calm_high"
    elif mood == "calm":
        key = "calm_low"
    else:
        key = "sad"

    playlist = playlists[key]
    
    #I used a list here in reference to the loteria labm to shuffle the songs
    songs = playlist["songs"][:]
    random.shuffle(songs)

    return playlist["title"], songs

#user's DIY playlist
#user will enter their own songs
def create_diy_playlist():
    songs = []
    print("\nEnter 5 songs for your DIY playlist:")
    for i in range(5):
        song = input(f"Song {i+1}: ")
        songs.append(song)
    return "Your Favs Mix!", songs

def write_to_history(name, mood, energy, title, songs):
    #Saves the session to a text file, matching the encryption and decyption lab
    file = open("playlist_history.txt", "a")
    file.write(f"\nUser: {name} | Mood: {mood} | Energy: {energy}\n")
    file.write(f"Playlist: {title}\n")
    for i, song in enumerate(songs, 1):
        file.write(f"{i}. {song}\n")
    file.write("-" * 25 + "\n")
    file.close()

def ask_to_continue():
    #Recursive once more!
    answer = input("\nWant another playlist? (Yes/No): ")
    answer = answer.upper()
    
    if answer == "Y" or answer == "YES":
        return "Y"
    elif answer == "N" or answer == "NO":
        return "N"
    else:
        print("Invalid response, please type Yes or No.")
        # The 'return' is critical to pass the final result back up the stack
        return ask_to_continue()


# MAIN PROGRAM:

def main():
    print("\nAre you in a music slump?")
    print("I got you\n")

    while True:
        #get user data
        name = get_user_info()
        selection = get_choice()


        if selection == "R":
            mood, energy = get_mood_energy()
            playlist_title, songs = generate_playlist(mood, energy)
        else:
            playlist_title, songs = create_diy_playlist()
            mood, energy = "Custom", "N/A"

        print(f"\nHi {name}!")
        print(f"\n{playlist_title}")

        for i, song in enumerate(songs, 1):
            print(f"{i}. {song}")

        write_to_history(name, mood, energy, playlist_title, songs)

        if ask_to_continue() == "N":
            print("\nok bye, your playlists are saved in playlist_history.txt :D \n")
            break

if __name__ == "__main__":
    main()
