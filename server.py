from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    response = str(response)

    emotions = response)[:-2]
    emotion_last = response)[-2:-1]
    dominant = response['dominant emotion']

    final_str = "For the given statement, the system response is {} and {}. The dominant emotion is {}.".format(emotions, emotion_last, dominant)
    
    return final_str

@app.route("/")
def render_index_page():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)