# Goal: Given an input image containing a page of a document, 'scan' the page by
# outputting a well-formatted, birds-eye view of the page, the whole page, and
# nothing but the page.
import cv2
import numpy as np
import math
# Open the image + convert to grayscale in preparation for edge detection
img = cv2.imread("test2.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Homework 2', gray)
cv2.waitKey(0)

# Detect edges with the Canny method (you'll need some time to calibrate your
# thresholds)
thresh = 100
useless, edges = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow('Homework 2', edges)
cv2.waitKey(0)

# Dilate to strengthen Canny output as a precaution
M = np.ones((3, 3))
edges = cv2.morphologyEx(edges, cv2.MORPH_DILATE, M);
cv2.imshow('Homework 2', edges)
cv2.waitKey(0)

# Identify connected components within Canny output (contours)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
for i in range(len(contours)):
    # What function do we use for polynomial estimation of a contour?
    epsilon = 0.05*cv2.arcLength(contours[i],True)
    poly = cv2.approxPolyDP(contours[i],epsilon,True)
    # What criteria might we want poly to fulfill for it to be considered a page?
    if len(poly) == 4:
        # contours are weirdly formatted (every point is wrapped in another array)
        # so we need to deal with that
        poly = poly[:, 0, :]
        # Some drawing functions to illustrate the page and its four corners
        copy = img.copy()
        cv2.drawContours(copy, contours, i, (0, 255, 0), -1)
        for corner in poly:
            cv2.circle(copy, tuple(corner), 20, (0, 0, 0), -1)
        imS = cv2.resize(copy, (1920, 1080))
        cv2.imshow('Homework 2', imS)
        cv2.waitKey(0)
        # Determine perspective transform matrix
        # Be very mindful of the exact ordering of points -- the detected top-left
        # corner should be at the same index as the ideal top-left corner, and so
        # on. In the interest of time you are allowed to hardcode the corner values for
        # the supplied test image.
        poly = poly[poly[:,1].argsort()]
        top = poly[:2]
        top = top[top[:,0].argsort()]
        topLeft = top[0]
        topRight = top[1]
        bottom = poly[2:]
        bottom = bottom[bottom[:,0].argsort()]
        bottomLeft = bottom[0]
        bottomRight = bottom[1]
        #Get width and height
        widthTop = np.sqrt(((topLeft[0] - topRight[0]) ** 2) + ((topLeft[1] - topRight[1]) ** 2))
        widthBottom = np.sqrt(((bottomLeft[0] - bottomRight[0]) ** 2) + ((bottomLeft[1] - bottomRight[1]) ** 2))
        maxWidth = max(int(widthTop), int(widthBottom))
        heightTop = np.sqrt(((topLeft[0] - bottomLeft[0]) ** 2) + ((topLeft[1] - bottomLeft[1]) ** 2))
        heightBottom = np.sqrt(((bottomRight[0] - topRight[0]) ** 2) + ((bottomRight[1] - topRight[1]) ** 2))
        maxHeight = max(int(heightTop), int(heightBottom))
        src = np.float32([topLeft,topRight,bottomLeft,bottomRight])
        dst = np.float32([[0,0],[maxWidth,0],[0,maxHeight],[maxWidth,maxHeight]])
        M = cv2.getPerspectiveTransform(src, dst)
        # Perform the perspective transform
        dst = cv2.warpPerspective(img,M,(maxWidth, maxHeight),flags=cv2.INTER_LINEAR)
        break
downsizeRatio = min(1920/maxWidth,1080/maxHeight)
display = cv2.resize(dst,(math.floor(maxWidth*downsizeRatio),math.floor(maxHeight*downsizeRatio)))
cv2.imshow('Homework 2', display)
cv2.waitKey(0)

# SUBMISSION INSTRUCTIONS:
# For this assignment, only this python file is necessary. If you didn't hard-code the
# points and have multiple test images that work, feel free to zip them up and send
# them over!
