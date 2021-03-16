
import cv2 as cv
import numpy as np
import os

if __name__ == '__main__':

    # read image
    img = cv.imread(os.getcwd() + "\\images\\Print_O.jpg")

    # show image
    cv.imshow('Example - Show image in window', img)

    cv.waitKey(0)  # waits until a key is pressed
    cv.destroyAllWindows()  # destroys the window showing image