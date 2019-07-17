import sys
#sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
n = 0

while(True):

    ret, frame = capture.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == ord('s'):
        IMAGE_PATH = "image/2/" + str(n) +".jpg"
        cv2.imwrite(IMAGE_PATH, frame)
        print("Saved: " + IMAGE_PATH)
        n = n + 1
    elif cv2.waitKey(10) == ord('q'):
        break
capture.release()