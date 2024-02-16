import cv2 as cv

capture = cv.VideoCapture(0)   # webcam

def detectFace(img):
    haar_cascade = cv.CascadeClassifier('./3_FaceDetection/haar_face.xml')
    # haar_face.xml is the Haarcascade classifier of frontal face(default)
    faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)

    # print(f'Number of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', img)

while True:
    isTrue, frame = capture.read()
    
    if isTrue:    
        # cv.imshow('Video', frame)
        detectFace(frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()