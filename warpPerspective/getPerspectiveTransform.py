import cv2
import numpy as np

IMAGE_PATH = "image/2/0.jpg"
M_PATH = "image/2/0_2.txt"
image_src = cv2.imread(IMAGE_PATH, 0)

point1 = np.array([[261,454], [303,383], [385,390], [360,464]], dtype = "float32")
point2 = np.array([[210, 480], [210, 40], [430, 40], [430, 480]], dtype = "float32")

M = cv2.getPerspectiveTransform(point1, point2)
print(M)
image_out = cv2.warpPerspective(image_src, M, (640, 480))

cv2.imshow("Image_out", image_out)
cv2.imwrite("image/2/0_2.jpg", image_out)
cv2.waitKey(0)