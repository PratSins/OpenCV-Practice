import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
# cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
# These display as grayscale. The lighter region is for higher concentration of that color.
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(blank.shape) # the 1st two are height and the width
print(img.shape) # the third element represents the no. of color channels, which is 3 in this case.
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
cv.destroyAllWindows()