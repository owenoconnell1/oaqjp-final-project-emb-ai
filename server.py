"""Flask server"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def detect_emotion():
    """Returns detected emotion"""
    text = request.args.get("text")
    if text is None:
        return "Invalid text! Please try again!"
    return jsonify(emotion_detector(text))
if __name__ == "__main__":
    app.run()
