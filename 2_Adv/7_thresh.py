import cv2 as cv

# Thresholding is the binarization of the image. Pixels are converted to black(0) or white(1)

img = cv.imread('./Resources/Photos/cats.jpg')
# cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)
print(threshold) # same as the threshold parameter in above function

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
                                      # img, max threshold value, adaptive method, threshold type, block size(kernel size), c value
                # c-value - an integer that is subtracted from the mean.
                # threshold type - cv.THRESH_BINARY_INV, cv.THRESH_BINARY
                # adaptive type - cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.ADAPTIVE_THRESH_MEAN_C
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
cv.destroyAllWindows()