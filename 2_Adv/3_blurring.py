import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur --> More effective in removing noise
median = cv.medianBlur(img, 3) # the function automatically assumes that the ksize is 3x3
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25) # applies blurring but retains the edges in the image.
                              # img, diameter, sigma color, sigma space
# Sigma color - a larger value for it means that more colors in the neighborhood will be considered whenthe blur is computed.
# Sigma space - a larger value for it means that pixels further out from the central pixel will influence the blurring
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()

'''
The kernal size is the size of the window eg, (3x3)

Image Kernel concept in OpenCV:
    When a computation is done over a pixel neighborhood, it is common to represent this with a kernel matrix. 
    This kernel describes how the pixels involved in the computation are combined in order to obtain the desired result.

What is kernel size in image processing?
    In image processing, the kernel size refers to the dimensions of a matrix or array that is used to perform operations such as blurring, sharpening, or edge detection on an image. A kernel is a small matrix or array of values that is convolved with the pixel values of an image.

'''