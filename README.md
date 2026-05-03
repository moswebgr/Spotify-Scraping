Spotify Scraping Tool

A Python-based tool for extracting and analyzing music data from Spotify.

This project allows you to scrape (extract) tracks, playlists, and audio features using Spotify’s public endpoints and process them into structured datasets.

🚀 Features
🔎 Scrape tracks from search queries
🎵 Extract playlist data from URLs
📊 Collect audio features (energy, tempo, danceability)
🔥 Detect viral tracks
💾 Export results to CSV
🖥️ Interactive CLI tool
⚙️ How It Works

The tool:

Authenticates with Spotify
Extracts data from:
Search results
Playlists
Audio features endpoints
Merges and analyzes the data
Saves results locally

📦 Installation
git clone https://github.com/moswebgr/Spotify-Scraping.git
cd Spotify-Scraping
pip install requests pandas
🔑 Setup

Create:

config/credentials.txt
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret

config/queries.txt
Eminem
travis scott

config/playlists.txt
https://open.spotify.com/playlist/XXXXXXXX

▶️ Usage
python main.py

🖥️ Menu
1. Search + Analyze Tracks
2. Find Viral Tracks
3. Analyze Playlists
4. Exit
   
📊 Output
File	Description
output/tracks.csv	Scraped tracks + features
output/viral.csv	Viral track detection
output/playlists.csv	Playlist data

📊 Data Collected
Track name
Artist
Popularity
Danceability
Energy
Tempo
Valence

⚠️ Disclaimer
This project is for educational purposes
Uses Spotify public API endpoints
May be subject to Spotify rate limits
Not affiliated with Spotify



📜 License

MIT License

👨‍💻 Author
vasilis moskofidis
