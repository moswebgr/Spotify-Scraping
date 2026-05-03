import requests
import base64

BASE_URL = "https://api.spotify.com/v1"

def get_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"

    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {"Authorization": f"Basic {auth}"}
    data = {"grant_type": "client_credentials"}

    r = requests.post(url, headers=headers, data=data)
    return r.json().get("access_token")

def search_tracks(token, query):
    url = f"{BASE_URL}/search"
    headers = {"Authorization": f"Bearer {token}"}

    params = {"q": query, "type": "track", "limit": 20}

    r = requests.get(url, headers=headers, params=params)
    items = r.json().get("tracks", {}).get("items", [])

    return [{
        "id": t["id"],
        "track": t["name"],
        "artist": t["artists"][0]["name"],
        "popularity": t["popularity"]
    } for t in items]

def get_audio_features(token, track_ids):
    url = f"{BASE_URL}/audio-features"
    headers = {"Authorization": f"Bearer {token}"}

    params = {"ids": ",".join(track_ids[:100])}

    r = requests.get(url, headers=headers, params=params)
    return r.json().get("audio_features", [])

def get_playlist_tracks(token, playlist_id):
    url = f"{BASE_URL}/playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {token}"}

    r = requests.get(url, headers=headers)
    items = r.json().get("items", [])

    data = []
    for i in items:
        t = i["track"]
        if t:
            data.append({
                "id": t["id"],
                "track": t["name"],
                "artist": t["artists"][0]["name"],
                "popularity": t["popularity"]
            })

    return data