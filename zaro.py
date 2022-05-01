import cv2
import numpy as np


img = np.zeros((500, 500, 3))
img2 =np.zeros((700, 500, 3))
print(img.shape)
img[:] = 255, 0, 10
img2[200:400, 300:400] = 255, 0, 0
cv2.imshow("image", img)
cv2.imshow("image2", img2)
cv2.waitKey(0)
input("please enter")