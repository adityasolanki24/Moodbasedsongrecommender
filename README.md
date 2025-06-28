# Indie Song Recommender Based on User Emotions

A smart application that detects your emotions through webcam or text input and recommends Hindi/Urdu indie songs that match your current mood.

---

## 🚀 Current Status: Minimal Working Prototype

- 🟢 **You can now enter a mood (e.g., 'happy', 'sad') and get a song recommendation!**
- 🟢 **NEW: Song scraper that automatically fetches and categorizes songs by mood!**
- 🟡 Webcam-based emotion detection is not yet implemented (placeholder only).
- 🟡 Emotion detection is just based on your text input for now.
- 🟢 Multiple moods supported: happy, sad, energetic, calm, romantic, nostalgic

---

## 🎵 What it does (Basic Version)

- Lets you choose between text input or webcam (webcam is a placeholder)
- Enter your mood as text (e.g., "happy", "sad", "energetic", "calm", "romantic", "nostalgic")
- Recommends a Hindi/Urdu indie song matching your mood from the database
- **NEW: Automatically scrapes songs from Genius API and categorizes them by lyrics sentiment**

---

## 🛠️ Tech Stack

- **UI:** Streamlit
- **Backend:** Python
- **Song Database:** JSON file
- **Song Scraping:** Genius API + Lyrics sentiment analysis
- **HTTP Requests:** Requests library

---

## 📁 Project Structure

```
├── app.py                    # Streamlit UI (basic working prototype)
├── emotion_detect.py         # Placeholder for emotion detection (returns text input)
├── recommender.py            # Loads songs and recommends by mood
├── song_scraper.py           # NEW: Scrapes songs from Genius API and categorizes by mood
├── run_scraper.py            # NEW: Easy-to-use script to run the scraper
├── songs_db.json             # Demo indie songs and mood tags (auto-updated by scraper)
├── requirements.txt          # Python package dependencies
└── assets/
    └── sample_images/        # (Unused in basic version)
```

---

## 📝 How to Run the Basic App

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the app**
   ```bash
   streamlit run app.py
   ```
3. **Usage**
   - Select "Text" as input mode
   - Enter your mood (try "happy", "sad", "energetic", "calm", "romantic", "nostalgic")
   - Click "Get Recommendation" to see a song suggestion
   - "Webcam" mode is a placeholder for future updates

---

## 🆕 How to Use the Song Scraper

The scraper automatically fetches Hindi/Urdu indie songs from Genius API and categorizes them by analyzing lyrics sentiment.

### Prerequisites
1. **Get a Genius API token:**
   - Go to https://genius.com/api-clients
   - Create an account and generate an API token

### Running the Scraper
```bash
python run_scraper.py
```

### What the Scraper Does
1. **Searches for songs** by popular Hindi/Urdu indie artists
2. **Fetches lyrics** from Genius.com
3. **Analyzes sentiment** using keyword-based mood detection
4. **Categorizes songs** into moods: happy, sad, energetic, calm, romantic, nostalgic
5. **Updates the database** automatically, avoiding duplicates

### Supported Artists (in scraper)
- Prateek Kuhad
- Jasleen Royal
- Arijit Singh
- Ritviz
- Seedhe Maut
- Divine
- Naezy
- Prabh Deep

---

## 💡 How it Works (Basic Version)
- The app takes your text input as the mood (no real emotion detection yet)
- It looks up a song with a matching mood in `songs_db.json`
- If found, it shows you the song title, artist, and a link to listen
- If not found, it asks you to try another mood

### How the Scraper Works
- Uses Genius API to search for songs by artist names
- Extracts lyrics from Genius song pages using regex patterns
- Analyzes lyrics using keyword-based sentiment analysis
- Categorizes songs into 6 mood categories based on lyrics content
- Automatically updates the JSON database with new songs

---

## 🔜 Next Steps (Planned)
- Implement real emotion detection (webcam and NLP)
- Improve lyrics extraction accuracy
- Add more sophisticated sentiment analysis using HuggingFace models
- Expand the artist list and song database
- Improve UI and add more features

---

**Note:** This is a minimal working prototype for demonstration and learning purposes. The scraper respects API rate limits and includes proper error handling. More features coming soon!
