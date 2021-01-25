import cv2 as cv
def colourModifier(col):
    img = cv.imread('sample_pics/3.jpg')

    cv.imshow("the image",img)
    cv.waitKey(100)

    if col == 'red' :
        img[:,:,1] = 0
        img[:,:,0] = 0
    elif col == 'blue' :
        img[:,:,1] = 0
        img[:,:,2] = 0
    elif col == 'green' :
        img[:,:,0] = 0
        img[:,:,2] = 0

    cv.imshow("The modified Image",img)
    cv.waitKey(100)
