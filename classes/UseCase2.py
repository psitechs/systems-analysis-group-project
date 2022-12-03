from Camera import *
from Controller import *
from User import *
from MobileApp import *
from Door import *

frank = User(userType="owner")
controllerB = Controller()
mobileAppB = MobileApp()
doorB = Door("Front")

frank.userSignOn()
mobileAppB.connectRemote(controllerB)
controllerB.userAuthentication(False,False,True) 
doorB.unlock()
doorB.lock()
frank.userSignOff()
