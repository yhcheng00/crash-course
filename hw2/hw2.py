# Goal: Given an input image containing a page of a document, 'scan' the page by
# outputting a well-formatted, birds-eye view of the page, the whole page, and
# nothing but the page. 
import cv2
import numpy as np

# Open the image + convert to grayscale in preparation for edge detection
img = # YOUR CODE HERE
gray = # YOUR CODE HERE

cv2.imshow('Homework 2', gray)
cv2.waitKey(0)

# Detect edges with the Canny method (you'll need some time to calibrate your
# thresholds)
edges = # YOUR CODE HERE
cv2.imshow('Homework 2', edges)
cv2.waitKey(0)

# Dilate to strengthen Canny output as a precaution
M = np.ones((3, 3))
edges = cv2.morphologyEx(edges, cv2.MORPH_DILATE, M);
cv2.imshow('Homework 2', edges)
cv2.waitKey(0)

# Identify connected components within Canny output (contours)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    # What function do we use for polynomial estimation of a contour?
    poly = # YOUR CODE HERE

    # What criteria might we want poly to fulfill for it to be considered a page?
    if # YOUR CODE HERE:

        # contours are weirdly formatted (every point is wrapped in another array)
        # so we need to deal with that
        poly = poly[:, 0, :]

        # Some drawing functions to illustrate the page and its four corners
        copy = img.copy()
        cv2.drawContours(copy, contours, i, (0, 255, 0), -1)
        for corner in poly:
            cv2.circle(copy, tuple(corner), 20, (0, 0, 0), -1)

        cv2.imshow('Homework 2', copy)
        cv2.waitKey(0)

        # Determine perspective transform matrix
        # Be very mindful of the exact ordering of points -- the detected top-left
        # corner should be at the same index as the ideal top-left corner, and so
        # on. In the interest of time you are allowed to hardcode the corner values for
        # the supplied test image.
        M = # YOUR CODE HERE

        # Perform the perspective transform
        dst = # YOUR CODE HERE
        break

cv2.imshow('Homework 2', dst)
cv2.waitKey(0)

# SUBMISSION INSTRUCTIONS:
# For this assignment, only this python file is necessary. If you didn't hard-code the
# points and have multiple test images that work, feel free to zip them up and send
# them over!
