# Song Scraper and Mood Categorizer
# Fetches songs from Genius API, analyzes lyrics sentiment, and categorizes by mood

import requests
import json
import time
from typing import List, Dict, Optional
import re

class SongScraper:
    def __init__(self, genius_token: str):
        """
        Initialize the scraper with Genius API token
        Args:
            genius_token: Genius API access token
        """
        self.genius_token = genius_token
        self.base_url = "https://api.genius.com"
        self.headers = {
            "Authorization": f"Bearer {genius_token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
    def search_songs(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for songs using Genius API
        Args:
            query: Search query (artist name, song title, etc.)
            limit: Maximum number of results to return
        Returns:
            List of song dictionaries with basic info
        """
        try:
            url = f"{self.base_url}/search"
            params = {"q": query}
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            songs = []
            
            for hit in data['response']['hits'][:limit]:
                song_info = hit['result']
                songs.append({
                    'id': song_info['id'],
                    'title': song_info['title'],
                    'artist': song_info['primary_artist']['name'],
                    'url': song_info['url'],
                    'lyrics_url': song_info['url']
                })
            
            return songs
            
        except Exception as e:
            print(f"Error searching songs: {e}")
            return []
    
    def get_lyrics(self, lyrics_url: str) -> Optional[str]:
        """
        Extract lyrics from Genius song page
        Args:
            lyrics_url: URL of the song page on Genius
        Returns:
            Cleaned lyrics text or None if failed
        """
        try:
            response = requests.get(lyrics_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            response.raise_for_status()
            
            # Simple regex to extract lyrics (this is basic - could be improved)
            # Look for common lyrics patterns
            html_content = response.text
            
            # Try to find lyrics in various formats
            lyrics_patterns = [
                r'<div class="Lyrics__Container[^"]*">(.*?)</div>',
                r'<div class="lyrics">(.*?)</div>',
                r'<div class="song_body-lyrics">(.*?)</div>'
            ]
            
            for pattern in lyrics_patterns:
                matches = re.findall(pattern, html_content, re.DOTALL)
                if matches:
                    lyrics = matches[0]
                    # Clean HTML tags
                    lyrics = re.sub(r'<[^>]+>', '', lyrics)
                    # Clean extra whitespace
                    lyrics = re.sub(r'\s+', ' ', lyrics).strip()
                    return lyrics
            
            return None
            
        except Exception as e:
            print(f"Error getting lyrics: {e}")
            return None
    
    def analyze_sentiment(self, lyrics: str) -> str:
        """
        Analyze lyrics sentiment and categorize by mood
        Args:
            lyrics: Song lyrics text
        Returns:
            Mood category (happy, sad, energetic, calm, romantic, nostalgic)
        """
        if not lyrics:
            return "unknown"
        
        lyrics_lower = lyrics.lower()
        
        # Define mood keywords (basic sentiment analysis)
        mood_keywords = {
            'happy': ['happy', 'joy', 'smile', 'laugh', 'dance', 'celebrate', 'fun', 'bright', 'sunshine', 'love', 'beautiful'],
            'sad': ['sad', 'cry', 'tears', 'lonely', 'heartbreak', 'pain', 'miss', 'gone', 'dark', 'night', 'alone'],
            'energetic': ['energy', 'fire', 'power', 'strong', 'fight', 'rise', 'move', 'dance', 'beat', 'loud', 'wild'],
            'calm': ['peace', 'quiet', 'gentle', 'soft', 'slow', 'breeze', 'wind', 'water', 'flow', 'serene', 'tranquil'],
            'romantic': ['love', 'heart', 'kiss', 'romance', 'forever', 'together', 'soul', 'passion', 'desire', 'beautiful'],
            'nostalgic': ['remember', 'memory', 'past', 'old', 'childhood', 'yesterday', 'time', 'gone', 'miss', 'back']
        }
        
        # Count keyword matches for each mood
        mood_scores = {}
        for mood, keywords in mood_keywords.items():
            score = sum(1 for keyword in keywords if keyword in lyrics_lower)
            mood_scores[mood] = score
        
        # Find the mood with highest score
        max_score = max(mood_scores.values())
        if max_score > 0:
            for mood, score in mood_scores.items():
                if score == max_score:
                    return mood
        
        # Default return if no mood detected
        return "unknown"
    
    def scrape_and_categorize(self, search_queries: List[str], songs_per_query: int = 5) -> List[Dict]:
        """
        Main function to scrape songs and categorize them by mood
        Args:
            search_queries: List of search terms (artists, songs, etc.)
            songs_per_query: Number of songs to fetch per query
        Returns:
            List of categorized song dictionaries
        """
        all_songs = []
        
        for query in search_queries:
            print(f"Searching for: {query}")
            
            # Search for songs
            songs = self.search_songs(query, songs_per_query)
            
            for song in songs:
                print(f"Processing: {song['title']} by {song['artist']}")
                
                # Get lyrics
                lyrics = self.get_lyrics(song['lyrics_url'])
                
                if lyrics:
                    # Analyze sentiment and categorize
                    mood = self.analyze_sentiment(lyrics)
                    
                    # Create song entry
                    song_entry = {
                        'title': song['title'],
                        'artist': song['artist'],
                        'mood': mood,
                        'url': song['url'],
                        'lyrics_preview': lyrics[:200] + "..." if len(lyrics) > 200 else lyrics
                    }
                    
                    all_songs.append(song_entry)
                    print(f"Categorized as: {mood}")
                else:
                    print(f"Could not get lyrics for: {song['title']}")
                
                # Be respectful to the API
                time.sleep(1)
        
        return all_songs

def update_songs_database(new_songs: List[Dict], db_path: str = 'songs_db.json'):
    """
    Update the songs database with new scraped songs
    Args:
        new_songs: List of new song dictionaries
        db_path: Path to the JSON database file
    """
    try:
        # Load existing database
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add new songs (avoid duplicates)
        existing_titles = {song['title'].lower() for song in data['songs']}
        
        for song in new_songs:
            if song['title'].lower() not in existing_titles:
                data['songs'].append(song)
                print(f"Added: {song['title']} by {song['artist']} (Mood: {song['mood']})")
            else:
                print(f"Skipped duplicate: {song['title']}")
        
        # Save updated database
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Database updated! Total songs: {len(data['songs'])}")
        
    except Exception as e:
        print(f"Error updating database: {e}")

# Example usage function
def main():
    """
    Example of how to use the song scraper
    """
    # You'll need to get a Genius API token from https://genius.com/api-clients
    GENIUS_TOKEN = "YOUR_GENIUS_TOKEN_HERE"
    
    if GENIUS_TOKEN == "YOUR_GENIUS_TOKEN_HERE":
        print("Please set your Genius API token in the script!")
        return
    
    # Initialize scraper
    scraper = SongScraper(GENIUS_TOKEN)
    
    # Define search queries (Hindi/Urdu indie artists and songs)
    search_queries = [
        "Prateek Kuhad",
        "Jasleen Royal",
        "Arijit Singh",
        "Ritviz",
        "Seedhe Maut",
        "Divine",
        "Naezy",
        "Prabh Deep"
    ]
    
    # Scrape and categorize songs
    new_songs = scraper.scrape_and_categorize(search_queries, songs_per_query=3)
    
    # Update database
    update_songs_database(new_songs)
    
    print("Scraping completed!")

if __name__ == "__main__":
    main() 