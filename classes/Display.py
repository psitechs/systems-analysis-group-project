from Controller import *


class InHouseDisplay:
    #Describes the dimensions of the screen
    screen = str
    #Describes the values currently in the buffer cache of the display's keypad 
    keypad = list[str]

    def __init__(self, screenDimension: str, keypadEntry: list[int]) -> None:
        self.keypad = screenDimension
        self.screen = keypadEntry
        print("Display Initialized...")