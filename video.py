import cv2
import os

cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('1.mp4')
while True:
    ret, im = cap.read()
    cv2.imshow("test", im)
    print(ret)
    cv2.waitKey(10)
    if not os.path.exists('cap.png'):
        cv2.imwrite('cap.png', im)

