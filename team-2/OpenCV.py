
import cv2 as cv
import numpy as np  


def img_process(color):

    cap = cv.VideoCapture(0,cv.CAP_DSHOW)

    while(True):
        ret, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 

        boundaries = {
            "Red" : ([0,100,100], [5,255,255]),    #HSV range for Red
            "Green" : ([40,100,100], [75,255,255]),    #HSV range for Green
            "Blue" : ([95,100,100], [125,255,255])     #HSV range for Blue
            }

        mask = cv.inRange(hsv, np.array(boundaries[color][0]), np.array(boundaries[color][1])) 

        res = cv.bitwise_and(frame,frame, mask= mask) 

    
        cv.imshow('Input',frame)
        cv.imshow('Output',res)

        c = cv.waitKey(1)
        if c == 27:               #ASCII value of Esc is 27
            break

    cap.release()
    cv.destroyAllWindows()