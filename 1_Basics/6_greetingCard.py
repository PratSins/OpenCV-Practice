import cv2 as cv

# TEST PROJECT FOR Multimedia Course

location = "./Resources/Photos/greet.jpg"
blank = cv.imread(location)
cv.putText(blank, 'Shubh Janamashthami', (20,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)