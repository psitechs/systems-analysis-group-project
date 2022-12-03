class Door:
    doorType = ""

    def __init__(self, doorType) -> None:
        self.doorType = doorType

    def lock(self):
        print(f"Locking {self.doorType} door")

    def unlock(self):
        print(f"Unlocking {self.doorType} door")