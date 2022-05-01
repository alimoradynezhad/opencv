import cv2
import numpy as np

img = cv2.imread("3.JPG")
print(img.shape)

imgresiza = cv2.resize(img, (200, 400))
imgcrop = img[0:150, 200:400]

cv2.imshow("image", img)
cv2.imshow("resiza", imgresiza)
cv2.imshow("crop", imgcrop)


cv2.waitKey(0)