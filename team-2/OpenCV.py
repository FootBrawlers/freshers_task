
import cv2 as cv
import numpy as np  

def color_highlight(img_location,color):
    
    img = cv.imread(img_location)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 

    boundaries = {
        "Red" : ([0,100,100], [20,255,255]),    #HSV range for Red
        "Green" : ([50,100,100], [70,255,255]),    #HSV range for Green
        "Blue" : ([110,100,100], [130,255,255])     #HSV range for Blue
    }

    mask = cv.inRange(hsv, np.array(boundaries[color][0]), np.array(boundaries[color][1])) 

    res = cv.bitwise_and(img,img, mask= mask) 

    cv.imshow('Image',img)  
    cv.imshow('res',res) 
    
    cv.waitKey(0)