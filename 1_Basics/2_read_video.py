import cv2 as cv

capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
# capture = cv.VideoCapture(0)   #---->For webcam
#  U can use higher integers like 1 and so on, for additional cameras connected to the computer.

while True:
    isTrue, frame = capture.read()
    
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately break from the loop 
    # and avoid error: (-215:Assertion failed)
    if isTrue:    
        cv.imshow('Video', frame)
        
        if cv.waitKey(20) & 0xFF==ord('d'):# press d to exit the screen b4 finishing the video
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()