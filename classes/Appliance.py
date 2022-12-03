class Appliance:
    applianceType = ""

    def __init__(self, applianceType) -> None:
        self.applianceType = applianceType

    def on(self):
        print(f"Turning on {self.applianceType}")

    def off(self):
        print(f"Shutting off {self.applianceType}")
    
    def setTimer(self):
        print(f"Setting Timer for {self.applianceType} to turn off")

class Kitchen(Appliance):
    #Oven temp in degrees
    oven = 75
    #Sink engaged status
    sink = False
    #Sink engaged status
    extractor = False

    def adjustTemp():
        print("Setting Timer for appliance to turn off")
    def setTimer():
        print("Setting Timer for appliance to turn off")