import requests, json

def emotion_detector (text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = inputobj, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['emotionPredictions'][0]['emotion']
        dominant = max(label, key=label.get)
        label["dominant emotion"] = dominant
    elif response.status_code == 400:
        label = None
    else:
        label = None

    return  label
