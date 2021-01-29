import cv2 as cv
import numpy as np

def colourModifier(col,picture_location = "Sample_pics/6.jpg"):
    img = cv.imread(picture_location)
    img = cv.resize(img,(600,600))
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    if col == 'blue' :
        low = np.array([99, 35, 0])
        high = np.array([125, 255, 255])
    elif col == 'red' :
        low = np.array([0, 44, 0])
        high = np.array([5, 255, 255])
    elif col == 'green' :
        low = np.array([51, 50, 0])
        high= np.array([73, 255, 255])

    mask = cv.inRange(hsv_img, low, high)
    final = cv.bitwise_and(img, img, mask=mask)
    cv.imshow("The orginal img",img)
    cv.imshow("The new Image",final)
    cv.waitKey(0)
    cv.destroyAllWindows()
