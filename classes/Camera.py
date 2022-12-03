import time

Vector = list[float]
FaceMap = list[Vector]


class Camera: 
#Class Variables
    #Determines the location of a camera in a modeled 3D space of a home in meters
    cameraLocation = Vector
    #Determines the current zoom level of a camera
    cameraZoom = float

#ClassFunctions
    #Instantiates object of this class
    def __init__(self, location: Vector, zoom: float) -> None:
        self.cameraLocation = location
        self.cameraZoom = zoom 
    
    #Adjusts zoom level of the camera
    def changeZoom(self, zoomLevel: float):
        self.cameraZoom = zoomLevel
        print(f"Camera zoom set to {self.cameraZoom}")

class FacialRecognitionCamera(Camera):
#Class Variables
    #Holds a list of points representing representing the unique 3D information of a user's face
    biometricScanner = None

    def validateFaceID(self,faceMap: FaceMap):
        #captures and sends face map data to controller for authentication
        self.biometricScanner = faceMap
        print("Sending FaceID Data to controller")
        print("Processing...")
        time.sleep(3)



#Deprecated features   
"""class InternalCamera(Camera):
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
"""
