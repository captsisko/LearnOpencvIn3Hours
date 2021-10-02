import cv2
import numpy as np

# faceCascade = cv2.CascadeClassifier("Resources/haarcascade/haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier("/Users/sisko/PycharmProjects/OpencvPython/Resources/haarcascades/haarcascade_frontalface_default.xml")
# img = cv2.imread("Resources/lena.png")
img = cv2.imread("Resources/people5.jpeg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces :
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)