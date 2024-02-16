import cv2 as cv

img = cv.imread('./Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img, scale=0.2)
cv.imshow('Resized Pic', resized_img)
cv.waitKey(0)
cv.destroyAllWindows()