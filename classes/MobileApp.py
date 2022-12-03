from Controller import *

class MobileApp:
    OTASoftware= ""
    touchScreen = [0,0,0]

    def __init__(self) -> None:
        pass
    
    def connectRemote(self,controller):
        print(f"Logging on to {controller} with pin")

