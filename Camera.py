class Camera: 
#Class Variables
    #Determines the color of the camera's outer casing
    casingColor = (0,0,0)
    resolution = ""

    def __init__(self) -> None:
        pass 

    #Uses Nanotech to change camera outer casing's color
    
    
class InternalCamera(Camera):
#Class Variables
    #Indicates whether camera is currently on
    MonitoringIndicatorLight = True

    def shutdownCamera(self):
        #Powers off camera
        self.MonitoringIndicatorLight = False

class ExternalCamera(Camera):
#Class Variables
    #Camera Yaw (i.e horizontal degree orientation)
    cameraYaw = 90
    #Pans the camera in the specified directions to specified number of degrees
    def panCam(self,,):
        pass