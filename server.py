from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    emotions = ", ".join(f"{k}: {v}" for k, v in list(response.items())[:-2])
    emotion_last = ", ".join(f"{k}: {v}" for k, v in list(response.items())[-2:-1])
    last_key, last_val = list(response.items())[-1]
    dominant = f"{last_key} is {last_val}"

    final_str = "For the given statement, the system response is {} and {}. The {}.".format(emotions, emotion_last, dominant)
    
    return final_str

@app.route("/")
def render_index_page():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)