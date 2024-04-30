        
from pal.products.qcar import QCarCameras
from hal.utilities.image_processing import ImageProcessing
import numpy as np
import cv2

class CSIReader():


    def __init__(self,
            imageSize = [820,410],
            frameRate = 30,
            cameraIndex = 3):


        # List of variables given by students
        self.imageSize      = imageSize

        self.frameRate      = frameRate

        self.sampleRate     = 1/self.frameRate

        self.cameraIndex = cameraIndex

    
        enableCameras = [False, False, False, True]
        enableCameras[cameraIndex] = True

        self.cameraCSI = QCarCameras(
            frameWidth  = self.imageSize[0],
            frameHeight = self.imageSize[1],
            frameRate   = self.frameRate,
            enableRight = enableCameras[0],
            enableBack  = enableCameras[1],
            enableLeft  = enableCameras[2],
            enableFront = enableCameras[3]
        )

        self.image =np.zeros((self.imageSize[0], self.imageSize[0]))



    def readCamera(self):
        self.cameraCSI.readAll()
        self.image = self.cameraCSI.csi[self.cameraIndex].imageData


    def stop_cameras(self):
        # Stopping the image feed for both cameras
        self.cameraCSI.terminate()

    def viewImage(self):
        cv2.imshow("front camera", self.image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()

