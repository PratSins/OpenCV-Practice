import cv2 as cv

haar_cascade = cv.CascadeClassifier('./3_FaceDetection/haar_face.xml')

def detectFace(location, mn):
    img = cv.imread(location)
    cv.imshow('IMAGE', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Grayed IMAGE', gray)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=mn)

    print(f'Number of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', img)

def try1():
    loc = './Resources/Photos/lady.jpg'
    detectFace(loc, 3)

def try2():
    loc = './Resources/Photos/group 1.jpg'
    detectFace(loc, 1)
    
try1()
    

cv.waitKey(0)