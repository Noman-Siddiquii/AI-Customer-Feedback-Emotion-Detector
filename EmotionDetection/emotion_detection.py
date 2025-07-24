import requests
import json

def emotion_detector(text_to_analyze):
    import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        # Blank input handling
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = "https://sn-watson-emotion.labs.cognitiveclass.ai/emotion"
    params = {"text": text_to_analyze}
    response = requests.get(url, params=params)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_data = response.json()
    emotions = response_data["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

