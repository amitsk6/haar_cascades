import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#fourcc= cv2.VideoWriter_fourcc(*'XVID')
#out =cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150,150,0])
    upper_red = np.array([180,255,150])
    
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel  = np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(res, -1, kernel)
    
    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res,15)
    #out.write(frame)
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',  mask)
    cv2.imshow('res', res)
    #cv2.imshow('smt', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
#out.release()
cv2.destroyAllWindows()