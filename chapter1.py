import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (250, 150))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("imgShow", img)
cv2.imshow("imgResized", imgResize)
cv2.imshow("imgCropped", imgCropped)

cv2.waitKey(0)