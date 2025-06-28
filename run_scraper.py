# Simple script to run the song scraper
# This makes it easy to scrape songs and update the database

from song_scraper import SongScraper, update_songs_database

def run_scraper():
    """
    Run the song scraper with a simple interface
    """
    print("🎵 Indie Song Scraper and Mood Categorizer")
    print("=" * 50)
    
    # Get Genius API token from user
    genius_token = input("Enter your Genius API token (or press Enter to skip): ").strip()
    
    if not genius_token:
        print("No token provided. You can get one from: https://genius.com/api-clients")
        print("For now, we'll use a demo mode with limited functionality.")
        return
    
    # Initialize scraper
    try:
        scraper = SongScraper(genius_token)
        print("✅ Scraper initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing scraper: {e}")
        return
    
    # Define search queries (Hindi/Urdu indie artists)
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
    
    print(f"\n🔍 Will search for songs by: {', '.join(search_queries)}")
    
    # Ask user for number of songs per artist
    try:
        songs_per_artist = int(input("How many songs per artist? (default: 3): ") or "3")
    except ValueError:
        songs_per_artist = 3
    
    print(f"\n🚀 Starting to scrape {songs_per_artist} songs per artist...")
    print("This may take a few minutes. Please be patient!")
    
    try:
        # Scrape and categorize songs
        new_songs = scraper.scrape_and_categorize(search_queries, songs_per_artist)
        
        if new_songs:
            print(f"\n✅ Successfully scraped {len(new_songs)} songs!")
            
            # Show summary
            mood_counts = {}
            for song in new_songs:
                mood = song['mood']
                mood_counts[mood] = mood_counts.get(mood, 0) + 1
            
            print("\n📊 Mood Distribution:")
            for mood, count in mood_counts.items():
                print(f"  {mood}: {count} songs")
            
            # Update database
            print("\n💾 Updating database...")
            update_songs_database(new_songs)
            
        else:
            print("❌ No songs were scraped. Check your API token and internet connection.")
            
    except Exception as e:
        print(f"❌ Error during scraping: {e}")
        print("This might be due to API rate limits or network issues.")

if __name__ == "__main__":
    run_scraper() 