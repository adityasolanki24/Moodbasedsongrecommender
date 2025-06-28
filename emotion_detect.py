# Emotion detection functions (face + text)

# For now, this is a placeholder for text-based emotion detection.
# In the future, this could use NLP to analyze the text and return an emotion.
# For the basic app, we just return the text as the detected emotion.

def detect_emotion_from_text(text):
    """
    Returns the input text as the detected emotion (for demo purposes).
    """
    return text.strip().lower() 