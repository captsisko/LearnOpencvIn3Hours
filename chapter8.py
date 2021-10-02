import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 500 :
            cv2.drawContours(imgContour, contour, -1, (255,0,0), 3)
            perimeter = cv2.arcLength(contour, True)
            print(perimeter)
            approximation = cv2.approxPolyDP(contour, 0.02*perimeter, True)
            print(len(approximation))
            objectCorners = len(approximation)
            x, y, w, h = cv2.boundingRect(approximation)
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 2)

            if objectCorners == 3:
                objectType = "triangle"
            elif objectCorners == 4 :
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05 :
                    objectType = "square"
                else :
                    objectType = "reactangle"
            elif objectCorners > 4 :
                objectType = "circle"
            else :
                objectType = "unknown"

            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)

img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50,50) # get image outlines
# imgBlank = np.zeros_like(img)
imgBlank = np.ones_like(img)

getContours(imgCanny)

# cv2.imshow("Image", img)
# cv2.imshow("Image Grey", imgGrey)
# cv2.imshow("Image Blur", imgBlur)

imgStack = stackImages(0.6, ([img, imgGrey, imgBlur], [imgCanny, imgBlank, imgContour]))

cv2.imshow('Images', imgStack)

cv2.waitKey(0)