import cv2
import numpy as np

img = cv2.resize(cv2.imread("Resources/lena.png"), (250,250))
img2 = cv2.resize(cv2.imread("Resources/lambo.png"), (250,250))

imgHor = np.hstack((img, img2))
imgVer = np.vstack((img, img2))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)

cv2.waitKey(0)