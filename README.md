# Indie Song Recommender Based on User Emotions

A smart application that detects your emotions through webcam or text input and recommends Hindi/Urdu indie songs that match your current mood.

## 🎵 What it does

- **Emotion Detection**: Analyzes your facial expressions via webcam or processes text input to determine your emotional state
- **Smart Recommendations**: Suggests handpicked Hindi/Urdu indie songs that align with your detected emotion
- **Dual Input Methods**: Choose between webcam-based face emotion detection or text-based emotion analysis
- **Curated Music Database**: Features a carefully selected collection of indie songs tagged with mood categories

## 🛠️ Tech Stack

- **Emotion Detection**: 
  - OpenCV + Deep Learning for facial emotion recognition
  - HuggingFace NLP for text-based emotion analysis
- **Backend**: Python
- **UI**: Streamlit 
- **Data Storage**: JSON-based song database

## 📁 Project Structure

```
├── app.py                    # Streamlit UI
├── emotion_detect.py         # Emotion detection functions (face + text)
├── recommender.py            # Logic to match songs to emotions
├── songs_db.json             # Handpicked indie songs and mood tags
├── requirements.txt          # Python package dependencies
└── assets/
    └── sample_images/        # Optional test images for face emotion
```

## 🚧 Current Status

**Project Status**: 🟡 In Development

- ✅ Project structure created
- ✅ Basic file setup completed
- 🔄 Core functionality implementation in progress
- ⏳ Emotion detection algorithms to be implemented
- ⏳ Song recommendation logic to be developed
- ⏳ Streamlit UI to be built
- ⏳ Song database to be populated

## 🚀 Planned Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Moodbasedsongrecommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🎯 Intended Features

- **Real-time Emotion Detection**: Uses your webcam to analyze facial expressions
- **Text-based Emotion Analysis**: Input your feelings as text for song recommendations
- **Mood-based Song Matching**: Intelligent algorithm to match songs with emotions
- **Hindi/Urdu Indie Focus**: Curated collection of independent music
- **User-friendly Interface**: Clean and intuitive Streamlit interface

## 🎼 Planned Emotion Support

The system will recognize various emotional states including:
- Happy/Joyful
- Sad/Melancholic
- Energetic/Excited
- Calm/Peaceful
- Romantic/Loving
- Nostalgic/Reflective

## 📝 Intended Usage

1. **Webcam Mode**: Allow camera access and let the app detect your facial expression
2. **Text Mode**: Describe your current mood or feelings in text
3. **Get Recommendations**: Receive personalized song suggestions based on your emotion
4. **Explore Music**: Discover new Hindi/Urdu indie artists and songs

## 🔄 Development Roadmap

- [ ] Implement emotion detection using OpenCV and deep learning models
- [ ] Add text-based emotion analysis using HuggingFace NLP
- [ ] Create song recommendation algorithm
- [ ] Build Streamlit user interface
- [ ] Populate songs database with Hindi/Urdu indie songs
- [ ] Add mood tagging system
- [ ] Test and optimize the application
- [ ] Deploy and launch

---

**Note**: This project is currently in development. The emotion detection will be designed for entertainment purposes and should not be used for medical or psychological assessment.
