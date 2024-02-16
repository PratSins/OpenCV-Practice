import cv2 as cv
import numpy as np

# applies to images, including translation, rotation, resizing, clipping and cropping.

img = cv.imread('./Resources/Photos/park.jpg')
# cv.imshow('Park', img)

# 1. Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    # The translation matrix is a 2x3 matrix where the first row specifies the horizontal translation (x) and the second row specifies the vertical translation (y). 
    # The first two columns [1,0] and [0,1] represent scaling factors (1 for no scaling) and the third column [x, y] represents the translation amounts. 
    # The 0 in the translation matrix represents the absence of scaling in the respective direction.
    # 1 represents translation but no scaling
    # [1, 0] represents scaling in the x-direction and [0, 1] represents scaling in the y-direction
    
    dimensions = (img.shape[1], img.shape[0])
    # This line calculates the dimensions of the input image (img) using its shape attribute. img.shape[1] represents the width of the image (number of columns) and img.shape[0] represents the height of the image (number of rows). These dimensions are stored as a tuple (width, height) in the variable dimensions.
    
    
    # This line uses OpenCV's warpAffine function to perform the actual translation of the image. It takes three parameters: the input image img, the transformation matrix transMat, and the dimensions of the output image dimensions.
    # The warpAffine function applies the geometric transformation specified by the transformation matrix to the input image, resulting in a translated image. Finally, the translated image is returned from the function.
    return cv.warpAffine(img, transMat, dimensions)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100) # translate(img, x, y)
cv.imshow('Translated', translated)

# 2. Rotation
def rotate(img, angle, rotPoint=None):
    # src img, angle of rotation, Point of rotation
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # the 3rd argument is for scaling.
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)
# -ve angle --> Clockwise
# +ve angle --> Anti-clockwise

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# r2 = rotate(img, -90)
r2 = rotate(rotated, -90)
cv.imshow('Rotated Rotated', r2)


# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()