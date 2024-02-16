import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
def func1(flag: bool=False):
    blank[:] = 0,0,255
               # Blue , Green, red
    if flag:
        cv.imshow('Red', blank)

def func2(flag: bool=False):
    blank[200:300, 300:400] = 0,0,255
    if flag:
        cv.imshow('Green', blank)

# 2. Draw a Rectangle
def func3(flag: bool=False):
    # For points tuple, first one is X-axis and 2nd is Y-axis
    cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
              #  image, top-left point(tuple), bottom-right point(tuple), color(tuple), thickness of the border
              #  thickness = -1 OR cv.FILLED ---> For the color filled rectangle/shape
    if flag:
        cv.imshow('Rectangle', blank)

# 3. Draw A circle
def func4(flag: bool=False):
    cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
            # image, centre, radius in pixels, color, thickness
    if flag:
        cv.imshow('Circle', blank)

# 4. Draw a line
def func5(flag: bool=False):
    cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
           # image, top-left point(tuple), bottom-right point(tuple), thickness
    if flag:
        cv.imshow('Line', blank)

# 5. Write text
def func6(flag: bool=False):
    cv.putText(blank, 'Hello, my name is Prat!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
    # image, text, Starting point, Font face/style, Font size, Color, thickness
    if flag:
        cv.imshow('Text', blank)
    
# TEST for each function
# func4(True)

def FullPicture():
    func2()
    func3()
    func4()
    func5()
    func6(True)

FullPicture()

cv.waitKey(0)