# Logic to match songs to emotions 

import json
import random

# Load songs from the JSON database
# Returns a list of song dicts

def load_songs(db_path='songs_db.json'):
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['songs']

# Recommend a random song matching the given mood
# Returns a song dict or None if no match found

def recommend_song(mood, db_path='songs_db.json'):
    songs = load_songs(db_path)
    # Filter songs by mood (case-insensitive)
    mood_songs = [song for song in songs if song['mood'].lower() == mood.lower()]
    if not mood_songs:
        return None
    return random.choice(mood_songs) 