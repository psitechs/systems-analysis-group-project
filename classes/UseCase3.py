from Camera import *
from Controller import *
from User import *
from MobileApp import *
from Appliance import Kitchen

lealon = User(userType="owner")
controllerC = Controller()
mobileAppC = MobileApp()
kitchenC = Kitchen("Sink")

lealon.userSignOn()
mobileAppC.connectRemote(controllerC)
controllerC.userAuthentication(False,False,True) 
kitchenC.off()
lealon.userSignOff()