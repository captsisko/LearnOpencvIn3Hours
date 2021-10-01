import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("ShowGrey", imgGray)
cv2.imshow("ShowBlur", imgBlur)
cv2.imshow("ShowCanny", imgCanny)
cv2.imshow("ShowDialtion", imgDialation)
cv2.imshow("ShowErosion", imgCanny)

cv2.waitKey(0)