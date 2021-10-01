import cv2
import numpy as np

img = np.zeros((512, 512, 3))
# print(img.shape)
# print(int(img.shape[0]/2))
# img[0:0] = 255, 0, 0

cv2.line(img, (0,0), (300,300), (0,255,0), 3)
cv2.rectangle(img, (0,0), (250, 350), (0,0,255), 2)
cv2.circle(img, (256, 256), 30, (255,255,255), cv2.FILLED)
cv2.putText(img, "Opencv ROCKS!!!", (int(img.shape[0]/4), int(img.shape[1]/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)