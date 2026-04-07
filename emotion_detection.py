import json
import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=json_input, headers=headers)
    response_dictionary = json.loads(response.text)
    emotions = response_dictionary["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    score_list = {anger_score, disgust_score, fear_score,joy_score, sadness_score}
    dominant_emotion = max(score_list)
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }


    