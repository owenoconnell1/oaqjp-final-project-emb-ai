from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("text")
    return jsonify(emotion_detector(text))
if __name__ == "__main__":
    app.run()