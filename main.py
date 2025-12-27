import os #interacts with the operating system
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame #audio mixer

def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name) #concataneting folder and song name

    if not os.path.exists(file_path):
        print("File not found")
        return
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top")

    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid command")

def main():

    try:
        #initialize pygame audio mixer
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed! ", e)
        return
    
    folder = "music"

    if not os.path.isdir(folder): #checks for the file
        print(f"Folder '{folder}' not found")
        return
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    if not mp3_files:
        print("No .mp3 files found!")

    while True:
        print("********** MP3 PLAYER **********")

        for index, song in enumerate(mp3_files, start=1): #gives a number like in an order
            print(f"{index}. {song}")
        
        choice_input = input("\nEnter the song number to play or 'Q' to quit: ")

        if choice_input.upper() == "Q":
            print("Bye Bye!")
            break

        if not choice_input.isdigit():
            print("Enter a valid number")
            continue

        choice = int(choice_input) - 1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()