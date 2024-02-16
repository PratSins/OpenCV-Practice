import cv2 as cv

# location = '''./1_Basics/naruto.jpeg'''
location = "./Resources/Photos/cat34234.jpg"
# error: (-215:Assertion failed) shows up if the image is not found
       
img = cv.imread(location)
print(type(img), end="\n\n\n")


cv.imshow('Cat', img)   # parameter = Title, image
cv.waitKey(0)
cv.destroyAllWindows()




# https://www.youtube.com/watch?v=oXlwWbU8l2o