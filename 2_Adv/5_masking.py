import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/cats 2.jpg')
# cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
                  #img,  centre, radius, color, thickness

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
                        #img, start point, end point,  white, thickness
weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Circle Shaped Masked Image', masked)

cv.waitKey(0)