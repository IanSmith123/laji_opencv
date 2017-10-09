import cv2
import matplotlib
import numpy as np

img = cv2.imread("1.png")
print(type(img))

cv2.imwrite("result.jpg", img)
cv2.imwrite("result.png", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("result.png", gray)
## cv2.imshow('opencv', img)
#cv2.waitKey()


#cv2.medianBlur()
#cv2.findContours()
#cv2.minAreaRect()
#cv2.ROTATION()
