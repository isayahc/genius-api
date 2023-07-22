import argparse
from lyricsgenius import Genius
from dotenv import load_dotenv
import os

load_dotenv()

def get_lyrics(api_key, song_title, artist_name):
    genius = Genius(api_key)
    song = genius.search_song(song_title, artist_name)
    if song is not None:
        print(f"Title: {song.title}")
        print(f"Artist: {song.artist}")
        print("Lyrics:\n")
        print(song.lyrics)
    else:
        print("Song not found.")

def main():
    parser = argparse.ArgumentParser(description='Get song lyrics from Genius')
    parser.add_argument('song_title', help='The title of the song')
    parser.add_argument('artist_name', help='The name of the artist')
    
    args = parser.parse_args()
    
    api_key = os.getenv('GENIUS_API_KEY')
    
    get_lyrics(api_key, args.song_title, args.artist_name)

if __name__ == "__main__":
    main()
