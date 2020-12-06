import cv2
import numpy as np

cap = cv2.VideoCapture("videoname.mp3")

while True:
    ret, frame = cap.read()
    resize = frame[150:800,300:800]
    blur = cv2.GaussianBlur(resize, (5,5), 0)
    hsv = cv2.cvtColor(blur, cv2.cv2.COLOR_RGB2HSV)

    #sensitivity =100
    low_white = np.array([0,0,255])
    up_white = np.array([175,255,255])
    mask = cv2.inRange(hsv, low_white, up_white)
    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 38, maxLineGap=10)

    if lines is not None:
        for line in lines:
            x, y, w, h = line[0]
            cv2.line(blur, (x, y), (w, h), (0,255,0), 6)
    if not ret:
        cap = cv2.VideoCapture("video3.mp4")
        continue
    cv2.imshow("mask",mask)
    cv2.imshow("blur",blur)

    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
