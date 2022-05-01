import cv2
import numpy as np


img = cv2.imread("3.JPG")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
imgblur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgcanny = cv2.Canny(img, 100, 100)


cv2.imshow("canny", imgcanny)
cv2.imshow("gray", imgGray)
cv2.imshow("blur", imgblur)

cv2.waitKey(0)