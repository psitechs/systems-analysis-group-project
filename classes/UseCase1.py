from Camera import *
from Controller import *
from User import *
from Microphone import *


bianca = User(userType="owner")
controllerA = Controller()
cameraA = FacialRecognitionCamera([12,17,30],1.8)

bianca.userSignOn()
cameraA.validateFaceID([[1,5,19],[45,26,88],[84,15,5]])
controllerA.userAuthentication(False,True,False) 
