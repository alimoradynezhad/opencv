import cv2

cap = cv2.VideoCapture("5.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
