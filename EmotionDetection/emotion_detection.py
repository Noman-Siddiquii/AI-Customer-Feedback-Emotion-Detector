"""
This module uses Watson NLP cloud service to detect emotions in text.
"""

import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes emotions in the given text using Watson NLP API.

    Parameters:
        text_to_analyze (str): Text input from the user.

    Returns:
        dict: Dictionary containing scores for anger, disgust, fear, joy, sadness,
              and the dominant emotion.
    """
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"Content-Type": "application/json",
               "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
