import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (250, 150))
print(imgResize.shape)

cv2.imshow("imgShow", img)
cv2.imshow("imgResized", imgResize)

cv2.waitKey(0)