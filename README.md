# 🎵 Genius Lyrics Fetcher 🎤

This Python script uses the Genius API to fetch the lyrics for any song from the Genius database. 

## 🚀 Getting Started

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/isayahc/genius-api.git
   ```

2. Install the necessary Python libraries:
   ```bash
   pip install lyricsgenius python-dotenv
   ```

3. Generate an API key from the Genius API [here](https://docs.genius.com/#resources-h1).

4. Create a `.env` file in the root of your project directory and store your API key like so:
   ```bash
   GENIUS_API_KEY='your-api-key'
   ```

## 📝 How to Use

To fetch lyrics for a song, run the script from the command line and pass the song title and artist name as arguments. For example:

```bash
 python get_lyrics.py "Finesse" "Pheelz"
```

Enjoy your favorite lyrics! 🎶