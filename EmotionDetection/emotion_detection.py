"""Module to connect and get response from IBM Watson NLP Library."""

import json
import requests

def emotion_detector(text_to_analyze):
    """Connect to Watson Library and receive response"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1' \
            '/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=5)
        response_text = json.loads(response.text)
        if 'emotionPredictions' in response_text:
            emotion_scores = response_text['emotionPredictions'][0]['emotion']
            emotion_max = max(emotion_scores.values())
            for key in emotion_scores.keys():
                if emotion_scores[key] == emotion_max:
                    emotion_scores['dominant_emotion'] = key
                    break
            return emotion_scores
        elif response.status_code == 400:
            emotion_scores = {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
            return emotion_scores
        raise Exception
    except Exception as e:
        response_text = {'Error': e}
    return response_text

# if __name__ == "__main__":
#     print(emotion_detector("I love this new technology"))
