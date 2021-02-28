import cv2 as cv
import numpy as np

def colourModifier(col, picture_location = "Sample_pics/6.jpg"):
    # checking if it is live feed or img location
    is_img = isinstance(picture_location,str)

    # reading the location of the img if it is a file and resizing it.
    if is_img:
        img = cv.imread(picture_location)
        img = cv.resize(img,(300,300))
    # else setting the frame as image
    else :
        img = picture_location

    # displaying the image or frame
    cv.imshow("The orginal img",img)

    # converts rgb image to hsv image
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    # HSV color range for red, green and blue
    if col == 'blue' :
        low = np.array([99, 35, 0])
        high = np.array([125, 255, 255])

    elif col == 'red' :
        # in case of red images seem to contain bits of orange,
        # so to get a better recognization I used two masks
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        low = cv.inRange(hsv_img, lower_red, upper_red)

        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        high = cv.inRange(hsv_img, lower_red, upper_red)

    elif col == 'green' :
        low = np.array([51, 50, 0])
        high= np.array([73, 255, 255])

    # making a mask for the given color.
    mask =  low + high if col == 'red' else cv.inRange(hsv_img, low, high)

    # using the mask to highlight only the input colour
    final = cv.bitwise_and(img, img, mask=mask)

    # using the mask to find the contours.
    contours , _ = cv.findContours(mask , cv.RETR_TREE , cv.CHAIN_APPROX_NONE)

    # finding the biggest contour in the mask (i.e only the ball)
    contour = max(contours , key = cv.contourArea )

    # finding the centre and radius of the ball
    (x,y),radius = cv.minEnclosingCircle(contour)
    x,y,radius = int(x),int(y),int(radius)

    # drawing the contour(outline) on the Image
    con_img = cv.drawContours(img.copy(), contour, -1, (123,123,123), 3)

    # drawing an approximate circle and its centre around the ball
    cir_img = cv.circle(img.copy(),(x,y),radius,(123,123,123), 3)
    cir_img = cv.rectangle(cir_img,(x,y),(x,y),(123,123,123),10)

    # showing the images and output
    cv.imshow("The required colour",final)
    cv.imshow("The image with outline",con_img)
    cv.imshow("The image with centre and circle",cir_img)

    print(f"\nThe centre of the ball is {(x,y)}")
    print(f"& the radius of the ball is {radius}")

    # if it is a image from system it waits for a key to be pressed
    if is_img :
        cv.waitKey(0)
        cv.destroyAllWindows()
    # if it is live feed it will quit when q or Q is pressed
    else :
        key = cv.waitKey(1)
        if key == 81 or key == 113:
            cv.destroyAllWindows()
            return 0

def live_colourModifier(col):

    webcam = cv.VideoCapture(0)
    while True :
        x , frame = webcam.read()
        val = colourModifier(col,frame)
        if val == 0 :
            break

    print("Ta Da!")


"""
The problem with this is, it takes anything in the given colour
and draws a contour to it and finds its centre and radius not just a ball .
"""
