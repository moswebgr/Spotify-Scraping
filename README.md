# 🎧 Spotify Scraping Tool

A Python-based CLI tool for scraping (extracting) music data from Spotify and analyzing it.

This tool collects tracks, playlists, and audio features and transforms them into structured datasets for analysis.

---

## 🚀 Features

* 🔎 Scrape tracks from search queries
* 🎵 Extract playlist data from URLs
* 📊 Fetch audio features (danceability, energy, tempo, etc.)
* 🔥 Detect viral tracks
* 💾 Export results to CSV
* 🖥️ Interactive terminal interface

---

## 📦 Installation

```bash
git clone https://github.com/moswebgr/Spotify-Scraping.git
cd Spotify-Scraping
pip install requests pandas
```

---

## 🔑 Setup

Create the following config files:

### config/credentials.txt

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

### config/queries.txt

```
drake
travis scott
Eminem
```

### config/playlists.txt

```
https://open.spotify.com/playlist/XXXXXXXX
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 🖥️ Menu

```
1. Search + Analyze Tracks
2. Find Viral Tracks
3. Analyze Playlists
4. Exit
```

---

## 📊 Output

* output/tracks.csv → scraped tracks + features
* output/viral.csv → viral tracks
* output/playlists.csv → playlist data

---

## 📊 Data Collected

* Track name
* Artist
* Popularity
* Danceability
* Energy
* Tempo
* Valence

---

## ⚠️ Disclaimer

* For educational purposes only
* Uses Spotify public endpoints
* Subject to rate limits
* Not affiliated with Spotify

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Vasilis Moskofidis
