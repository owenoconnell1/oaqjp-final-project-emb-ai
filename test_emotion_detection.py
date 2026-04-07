import unittest
from EmotionDetection.emotion_detection import emotion_detector
joy = "I am glad this happened"
anger = "I am really mad about this"
disgust = "I feel disgusted just hearing about this"
sadness = "I am so sad about this"
fear = "I am really afraid that this will happen"

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector(joy)
        result2 = emotion_detector(anger)
        result3 = emotion_detector(disgust)
        result4 = emotion_detector(sadness)
        result5 = emotion_detector(fear)
        self.assertEqual(result1["dominant_emotion"], "joy")
        self.assertEqual(result2["dominant_emotion"], "anger")
        self.assertEqual(result3["dominant_emotion"], "disgust")
        self.assertEqual(result4["dominant_emotion"], "sadness")
        self.assertEqual(result5["dominant_emotion"], "fear")