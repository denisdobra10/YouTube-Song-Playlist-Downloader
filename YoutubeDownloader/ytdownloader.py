# Auto install dependencies ######################################
import os
import sys
import subprocess

try:
    from pytube import YouTube, Playlist
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytube'])
    from pytube import YouTube, Playlist

os.system('cls' if os.name == 'nt' else 'clear')
##################################################################


# YouTube music downloader by Denis @ 2022



pathToScript = os.path.dirname(__file__)
pathToDownloadsFolder = pathToScript + "\Downloads"


# Single song download function
def DownloadSong(link, path=pathToDownloadsFolder):
    # Setting up the path
    downloadPath = pathToDownloadsFolder

    if(not path == None):
        downloadPath = path
    
    # Proceed to download song
    try:
        song = YouTube(link)
        fileName = song.title + ".mp3"

        # Avoid name errors
        if('"' in fileName):
            fileName = fileName.replace('"', "-")

        print("Starting downloading song: {}...".format(song.title))
        song.streams.first().download(downloadPath, fileName)
        print("Audio has been succesfully downloaded! Name of the file: {}; Location on disk: {}".format(fileName, downloadPath))
    except Exception as e:
        print(e.args)
        print("An error occured! Audio file was not downloaded. There could've been an url misspelling!")
    
    

# Playlist download function
def DownloadPlaylist(link, path=pathToDownloadsFolder):
    # Setting up a counter variable to track how many songs have been successfully downloaded
    counter = 0

    # Setting up the path
    downloadPath = pathToDownloadsFolder

    if(not path == None):
        downloadPath = path
    
    # Proceed to download song
    try:
        playlist = Playlist(link)

        for song in playlist.videos:
            title = song.streams.first().title
            fileName = title + ".mp3"

            # Avoid name errors
            if('"' in fileName):
                fileName = fileName.replace('"', "-")

            if(not "video not available" in title.lower()):
                try:
                    print("Download number {}: Starting downloading song: {}...".format(counter + 1, title))
                    song.streams.first().download(downloadPath, fileName)
                    print("Audio has been succesfully downloaded! Name of the file: {}".format(fileName))
                    counter += 1
                    print("")
                except:
                    print("Unexpected error occured for song {}. This audio file hasn't been downloaded!".format(title))
    except:
        print("An error occured! There could've been an url misspelling!")

    print("The playlist has been successfully downloaded on disk!")
    print("{} files have been downloaded!".format(counter))


def Greet():
    print("Welcome to YouTube Downloader by Denis @ 2022")
    print("")


# Main function for the script
def main():
    Greet()
    print("Current folder to download files: {}".format(pathToDownloadsFolder))
    path = pathToDownloadsFolder

    userInput = ""
    while(userInput.lower() != "yes" and userInput.lower() != "no"):
        userInput = input("Would you like to change the path?(yes or no): ")

    if(userInput.lower() == "yes"):
        path = input("Enter the path: ")

    link = input("Enter URL to YouTube song or playlist: ")

    if("list=" in link):
        print("Script has recognised you are willing to download a playlist!")
        print("Starting...")
        DownloadPlaylist(link, path)
    else:
        DownloadSong(link, path)


# Executing main function and start the script
main()