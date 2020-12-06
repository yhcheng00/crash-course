import cv2
import numpy as np

# Load in the input ijmage
img = cv2.imread('base.jpg')
cv2.imshow('hw4', img)
cv2.waitKey(0)

# You'll want to do some preprocessing on img - create an unraveled array of 3 dimensional colors in float32
# YOUR CODE HERE

# Our hyperparameters for k means - feel free to play around!
max_iter = 10
eps = 1.0
K = 8
attempts = 10

criteria = # YOUR CODE HERE
# Run k means with the input image and parameters
# YOUR CODE HERE

# How should we apply the labels back to the original image?
# YOUR CODE HERE
cv2.imshow('hw4',img)
cv2.waitKey(0)
