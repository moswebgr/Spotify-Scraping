import os
from utils import load_credentials, load_queries, ensure_output
from spotify_api import *
from analyzer import *
import pandas as pd

def extract_playlist_id(url):
    return url.split("playlist/")[1].split("?")[0]

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝   
        PRO MUSIC TOOL
    """)
    print("1. Search + Analyze Tracks")
    print("2. Find Viral Tracks")
    print("3. Analyze Playlists")
    print("4. Exit")

def main():
    ensure_output()
    creds = load_credentials()
    token = get_token(creds["CLIENT_ID"], creds["CLIENT_SECRET"])

    while True:
        menu()
        choice = input("\nSelect: ")

        if choice == "1":
            queries = load_queries()
            all_tracks = []

            for q in queries:
                print(f"[+] {q}")
                all_tracks += search_tracks(token, q)

            features = get_audio_features(token, [t["id"] for t in all_tracks])
            df = merge_features(all_tracks, features)

            save(df, "output/tracks.csv")
            input("Done...")

        elif choice == "2":
            df = pd.read_csv("output/tracks.csv")
            viral = find_viral(df)
            save(viral, "output/viral.csv")
            input("Done...")

        elif choice == "3":
            with open("config/playlists.txt") as f:
                urls = [l.strip() for l in f]

            all_tracks = []
            for url in urls:
                pid = extract_playlist_id(url)
                all_tracks += get_playlist_tracks(token, pid)

            df = pd.DataFrame(all_tracks)
            save(df, "output/playlists.csv")
            input("Done...")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()