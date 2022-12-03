class User:
    userType = None

    def __init__(self,userType):
        self.userType = userType

    def userSignOn(self):
        print("Starting user authentication process in controller")

    def userSignOff(self):
        print("Disconnecting from controller...")