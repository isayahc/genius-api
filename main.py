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

api_key = os.getenv('GENIUS_API_KEY')
song_title = "Bohemian Rhapsody"
artist_name = "Queen"

get_lyrics(api_key, song_title, artist_name)
