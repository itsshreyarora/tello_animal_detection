import os
import cv2
import time 
from djitellopy import Tello
import sys
from imageai.Detection import ObjectDetection




S = 60
FPS = 30

tello = Tello()

tello.connect()
tello.set_speed(S)
tello.streamon()
tello.takeoff()

frame_read = tello.get_frame_read()


detectormodel = ObjectDetection()
detectormodel.setModelTypeAsYOLOv3()
detectormodel.setModelPath(os.path.join(os.getcwd() , "yolo.h5"))
detectormodel.loadModel()
custom = detectormodel.CustomObjects(person=True, cat=True,   dog=True,   horse=True,   sheep=True,   cow=True,   elephant=True,   bear=True,   zebra=True,
    giraffe=True, bicycle=True,   car=True,   motorcycle=True)

a = int(input())
for i in range(a):
    tello.move_forward(10)
    frame = frame_read.frame
    detections = detectormodel.detectCustomObjectsFromImage( custom_objects=custom, input_image=frame, minimum_percentage_probability=30)
    cv2.imshow("Video", frame)

    resized=False
    color_index={'':''}

    for obj in detections:
        print(obj["name"] , " : ", obj["percentage_probability"], " : ", obj["box_points"] )
        print("--------------------------------")
        takePicture()


   
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

tello.land()
tello.streamoff()
cv2.destroyAllWindows()
sys.exit()