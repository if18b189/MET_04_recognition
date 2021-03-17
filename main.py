"""
sources:

https://www.tutorialspoint.com/template-matching-using-opencv-in-python
https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html

"""

import cv2
import numpy as np
import os

if __name__ == '__main__':

    # reading main image
    main_image = cv2.imread(os.getcwd() + "\\images\\Print_O.jpg")
    # converting to grayscale
    gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

    # reading the template image
    template = cv2.imread(os.getcwd() + "\\images\\Print_M.jpg", 0)
    width, height = template.shape[::-1]  # getting the width and height

    # # rotating the template image 90 degrees, experimenting
    # M = cv2.getRotationMatrix2D(((width/2)-7, height/2), -90, 1)
    # rotatedTemplate = cv2.warpAffine(template, M, (template.shape[0], template.shape[1]))

    # matching the template using cv2.matchTemplate
    match = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED) # matching with horizontal template image
    # match = cv2.matchTemplate(gray_image, rotatedTemplate, cv2.TM_CCOEFF_NORMED) # matching with vertical template image
    threshold = 0.92  # it is critical to tune the threshold, else numbers like 8 will be matched because they match the number 6
    position = np.where(match >= threshold)  # getting the location of template in the image
    for point in zip(*position[::-1]):  # draw the rectangle around the matched template
        cv2.rectangle(main_image, point, (point[0] + width, point[1] + height), (255, 0, 0), 0)
    cv2.imshow('Template Found', main_image)
    cv2.waitKey(0)