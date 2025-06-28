# Streamlit UI for Indie Song Recommender Based on User Emotions 

import streamlit as st
from emotion_detect import detect_emotion_from_text
from recommender import recommend_song

# --- Streamlit App ---
st.set_page_config(page_title="Indie Song Recommender", page_icon="🎵")
st.title("🎵 Indie Song Recommender Based on Your Mood")
st.write("Detect your emotion and get a Hindi/Urdu indie song recommendation!")

# Step 1: Choose input mode
input_mode = st.radio("How do you want to provide your mood?", ("Text", "Webcam (coming soon)"))

# Step 2: Get emotion (for now, only text is implemented)
if input_mode == "Text":
    user_text = st.text_input("Describe your mood (e.g., happy, sad):")
    if st.button("Get Recommendation"):
        if user_text.strip() == "":
            st.warning("Please enter your mood.")
        else:
            # Detect emotion (just returns the text for now)
            detected_emotion = detect_emotion_from_text(user_text)
            # Recommend a song
            song = recommend_song(detected_emotion)
            if song:
                st.success(f"**Recommended Song for '{detected_emotion.title()}' Mood:**")
                st.markdown(f"- **{song['title']}** by *{song['artist']}*  ")
                st.markdown(f"[Listen here]({song['url']})")
            else:
                st.info(f"Sorry, no songs found for the mood '{detected_emotion}'. Try 'happy' or 'sad'.")
else:
    st.info("Webcam-based emotion detection will be available in a future version.")
    st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif", caption="Coming soon!")

# --- End of basic app ---
# This is a minimal working prototype. More features and better emotion detection coming soon! 