import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_return_joy(self):
        # 1: Test on joy
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')

        #2: Test on anger
        self.assertEqual(emotion_detector('I am really mad about this')['dominant_emotion'], 'anger')
        
        #3: Test on disgust
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')

        #4: Test on sadness
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness')

        #5: Test on fear
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
