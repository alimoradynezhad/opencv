import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img =cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break