import cv2 as cv

# Read in an image
img = cv.imread('./Resources/Photos/park.jpg')
# cv.imshow('Park', img)

# Image Conversions

# Grayscale ---> Shows the Intensity distribution of pixels instead of the color image itself
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cvtColor --> Converts an image from one color space to another
cv.imshow('Gray', gray) 

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
                            # This tuple is kernel size(ksize)
cv.imshow('Blur', blur)

# Edge Cascade --> Canny Edge Detector
# canny = cv.Canny(img, 125, 175) # This Will have way more edges than the blurred one
canny = cv.Canny(blur, 125, 175) # the no.s are threshold values
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# Edged image, kernel size, iterations for dilation
cv.imshow('Dilated', dilated)

# Eroding --> to reverse dilation
eroded = cv.erode(dilated, (7,7), iterations=3) # kernel size and iterations have to the same dilated one to get results
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # default interpolation is cv.INTER_AREA
                    # image, destination size(ignoring the aspect ratio), interpolation
                    # cv.INTER_CUBIC -- slowest
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()