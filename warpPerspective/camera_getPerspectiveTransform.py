import sys
#sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
n = 0

IMAGE_PATH = "image/2/0.jpg"
image_src = cv2.imread(IMAGE_PATH, 0)
point1 = np.array([[261,454], [303,383], [385,390], [360,464]], dtype = "float32")
point2 = np.array([[210, 480], [210, 40], [430, 40], [430, 480]], dtype = "float32")
M = cv2.getPerspectiveTransform(point1, point2)

while(True):

    ret, frame = capture.read()

    cv2.imshow('frame', frame)

    image_out = cv2.warpPerspective(frame, M, (640, 480))
    cv2.imshow("Image out", image_out)

    if cv2.waitKey(10) == ord('s'):
        IMAGE_SRC_PATH = "image/2_out/" + str(n) +"_src.jpg"
        cv2.imwrite(IMAGE_SRC_PATH, frame)
        IMAGE_OUT_PATH = "image/2_out/" + str(n) + "_out.jpg"
        cv2.imwrite(IMAGE_OUT_PATH, image_out)
        print("Saved: " + IMAGE_OUT_PATH)
        n = n + 1
    elif cv2.waitKey(10) == ord('q'):
        break

capture.release()