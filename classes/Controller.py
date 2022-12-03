import time
from Camera import *
from Microphone import *

microphoneA = Microphone([12,15,33])

class Controller:
    faceID = None
    voiceRecognition = None
    pin = None

    def __init__(self) -> None:
        pass

    def userAuthentication(self, faceIDData = False, voiceRecognitionData=False, pinData=False):
        self.faceID = faceIDData
        self.voiceRecognition = voiceRecognitionData
        self.pin = pinData

        if self.faceID:
            print("Facial scan confirmed. Access granted.")
        else:
            print("Face ID invalid. Provide voice sample...")
            time.sleep(6)
            microphoneA.validateVoice()
            time.sleep(3)
            if self.voiceRecognition:
                print("Voice Validation confirmed. Access granted.")
            else:
                print("Pin confirmed. Access Granted")

    def saveUserProfile(self):
        print("Saving user profile")

    def callUserProfile(self):
        print("Retrieving user profile")
