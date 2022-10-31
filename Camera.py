class Camera: 
#Class Variables
    #Determines the color of the camera's outer casing
    casingColor = [0,0,0]
    resolution = "1080p"

#ClassFunctions
    #Instantiates object of this class
    def __init__(self) -> None:
        pass 

    #Uses Nanotech to change camera outer casing's color
    def changeCaseColor(self, R,G,B):
        self.casingColor = [R,G,B]

    
class InternalCamera(Camera):
#Class Variables
    #Indicates whether camera is currently on
    MonitoringIndicatorLight = True

    def shutdownCamera(self):
        #Powers off camera
        self.MonitoringIndicatorLight = False

class ExternalCamera(Camera):
#Class Variables
    #Camera Yaw (i.e. horizontal degree orientation)
    cameraYaw = 90
    #CameraPitch (i.e. vertical degree orientation)
    cameraPitch = 90
    #Denotes whether this external camera is within an armored case
    isArmored = True
    #Denotes whether this external camera is night vision capable
    hasNightVision = False

    #Pans the camera in the specified directions to specified number of degrees
    def panCam(self,degree):
        self.cameraYaw = degree
    
    #Pans the camera in the specified directions to specified number of degrees
    def pitchCam(self,degree):
        self.cameraPitch = degree

