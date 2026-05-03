import pandas as pd

def merge_features(tracks, features):
    df_tracks = pd.DataFrame(tracks)
    df_feat = pd.DataFrame(features)

    df = df_tracks.merge(df_feat, left_on="id", right_on="id")
    return df

def find_viral(df):
    return df[df["popularity"] > 80].sort_values("popularity", ascending=False)

def save(df, path):
    df.to_csv(path, index=False)
    print(f"[+] Saved -> {path}")