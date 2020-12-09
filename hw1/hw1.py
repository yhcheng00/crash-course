# Goal: Given an input image with five randomly positioned pure colors, ascertain
# the positions of these colors and return their values in various formats
import cv2
import numpy as np

# For each function, return a list of color representations of the corresponding
# point (1 for getColorOne, 2 for getColorTwo...) in the following format:
# [[R, G, B], [B, G, R], [H, S, V], grayscale]
name = '__main__'
img = cv2.imread("hw1.jpg")
def getColorOne(img):
    lower = np.array([72,130,130])
    upper = np.array([73,255,255])
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thres = cv2.inRange(hsv,lower,upper)
    thres = cv2.bitwise_and(img, img, mask = thres)
    bgr = thres[thres != 0][9:12]
    rgb = [bgr[2],bgr[1],bgr[0]]
    hsv_thres = cv2.cvtColor(thres,cv2.COLOR_BGR2HSV)
    grayscale = cv2.cvtColor(thres,cv2.COLOR_BGR2GRAY)
    gray = grayscale[grayscale != 0][1]
    hsv = hsv_thres[hsv_thres != 0][9:12]
    return [rgb,list(bgr),list(hsv),gray]
def getColorTwo(img):
    lower = np.array([75,130,130])
    upper = np.array([150,255,255])
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thres = cv2.inRange(hsv,lower,upper)
    thres = cv2.bitwise_and(img, img, mask = thres)
    bgr = thres[thres != 0][9:12]
    rgb = [bgr[2],bgr[1],bgr[0]]
    hsv_thres = cv2.cvtColor(thres,cv2.COLOR_BGR2HSV)
    grayscale = cv2.cvtColor(thres,cv2.COLOR_BGR2GRAY)
    gray = grayscale[grayscale != 0][1]
    hsv = hsv_thres[hsv_thres != 0][9:12]
    return [rgb,list(bgr),list(hsv),gray]
def getColorThree(img):
    lower = np.array([150,130,130])
    upper = np.array([255,255,255])
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thres = cv2.inRange(hsv,lower,upper)
    thres = cv2.bitwise_and(img, img, mask = thres)
    bgr = thres[thres != 0][9:12]
    rgb = [bgr[2],bgr[1],bgr[0]]
    hsv_thres = cv2.cvtColor(thres,cv2.COLOR_BGR2HSV)
    grayscale = cv2.cvtColor(thres,cv2.COLOR_BGR2GRAY)
    gray = grayscale[grayscale != 0][1]
    hsv = hsv_thres[hsv_thres != 0][9:12]
    return [rgb,list(bgr),list(hsv),gray]

def getColorFour(img):
    lower = np.array([30,130,130])
    upper = np.array([60,255,255])
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thres = cv2.inRange(hsv,lower,upper)
    thres = cv2.bitwise_and(img, img, mask = thres)
    bgr = thres[thres != 0][9:12]
    rgb = [bgr[2],bgr[1],bgr[0]]
    hsv_thres = cv2.cvtColor(thres,cv2.COLOR_BGR2HSV)
    grayscale = cv2.cvtColor(thres,cv2.COLOR_BGR2GRAY)
    gray = grayscale[grayscale != 0][1]
    hsv = hsv_thres[hsv_thres != 0][9:12]
    return [rgb,list(bgr),list(hsv),gray]

def getColorFive(img):
    lower = np.array([0,130,130])
    upper = np.array([30,255,255])
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thres = cv2.inRange(hsv,lower,upper)
    thres = cv2.bitwise_and(img, img, mask = thres)
    bgr = thres[thres != 0][9:12]
    rgb = [bgr[2],bgr[1],bgr[0]]
    hsv_thres = cv2.cvtColor(thres,cv2.COLOR_BGR2HSV)
    grayscale = cv2.cvtColor(thres,cv2.COLOR_BGR2GRAY)
    gray = grayscale[grayscale != 0][1]
    hsv = hsv_thres[hsv_thres != 0][9:12]
    return [rgb,list(bgr),list(hsv),gray]


if name == '__main__':
    pass
    # Do any testing you need to do here! I suggest opening the image in OpenCV
    # and plugging it into your functions to start with

# SUBMISSION INSTRUCTIONS:
# Upload a zip file containing hw1.py and hw1.jpg to the Gradescope portal.
# Do not modify the names in any way.
