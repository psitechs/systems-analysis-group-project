Vector = list[float]

class Microphone:
    microphoneLocation = [0,0,0]

    def __init__(self,location: Vector) -> None:
        self.microphoneLocation = location

    def listening(self):
        print("I'm listening!")

    def validateVoice(self):
        print("Sending voice Data to Controller")