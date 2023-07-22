import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def get_lyrics(api_key, song_title, artist_name):
    base_url = "https://api.genius.com"
    search_url = f"{base_url}/search"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    params = {
        "q": f"{song_title} {artist_name}"
    }
    
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    
    if response.status_code == 200 and data["meta"]["status"] == 200:
        hits = data["response"]["hits"]
        if hits:
            song_id = hits[0]["result"]["id"]
            song_url = f"{base_url}/songs/{song_id}"
            
            response = requests.get(song_url, headers=headers)
            data = response.json()
            
            if response.status_code == 200 and data["meta"]["status"] == 200:
                song_info = data["response"]["song"]
                title = song_info["title"]
                artist = song_info["primary_artist"]["name"]
                lyrics_url = song_info["url"]

                # Scrape the lyrics using Beautifulsoup
                page = requests.get(lyrics_url)
                html = BeautifulSoup(page.text, 'html.parser')
                lyrics = html.find('div', class_='lyrics').get_text()

                print(f"Title: {title}")
                print(f"Artist: {artist}")
                print("Lyrics:\n")
                print(lyrics)
            else:
                print("Failed to retrieve song data.")
        else:
            print("Song not found.")
    else:
        print("Failed to perform the search.")

if __name__ == '__main__':
    api_key = os.getenv('GENIUS_API_KEY')
    song_title = "Bohemian Rhapsody"
    artist_name = "Queen"

    lyrics = get_lyrics(api_key, song_title, artist_name)
    print(lyrics)
    
