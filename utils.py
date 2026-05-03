import os

def load_credentials(path="config/credentials.txt"):
    creds = {}

    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing {path}")

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                creds[key.strip()] = value.strip()

    return creds


def load_queries(path="config/queries.txt"):
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def load_playlists(path="config/playlists.txt"):
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def ensure_output():
    os.makedirs("output", exist_ok=True)
    os.makedirs("config", exist_ok=True)