import cv2 as cv
import numpy as np

img = cv.imread("assets/shapes.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# SHI-TOMASI METHOD https://docs.opencv.org/4.x/d4/d8c/tutorial_py_shi_tomasi.html
corners = cv.goodFeaturesToTrack(gray_img, maxCorners=50, qualityLevel=0.1, minDistance=50)
corners = np.int64(corners)

for corner in corners:
    x,y = corner.ravel()
    img = cv.circle(img, center=(x,y), radius=20, color=(0, 255, 0), thickness=-1)


# HARRIS CORNER DETECTION https://docs.opencv.org/4.x/dc/d0d/tutorial_py_features_harris.html
corners = cv.goodFeaturesToTrack(gray_img, maxCorners=50, qualityLevel=0.01, minDistance=50, useHarrisDetector=True, k=0.1)
corners = np.int64(corners)

for corner in corners:
    x,y = corner.ravel()
    img = cv.circle(img, center=(x,y), radius=10, color=(255, 0, 0), thickness=-1)


cv.imshow("Shapes", img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("assets/shapes_corners.png", img)