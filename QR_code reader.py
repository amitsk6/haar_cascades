# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:34:39 2020

@author: UA
"""

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import smtplib 
q

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 
  
# Authentication 
s.login("amitskotagi.cs18@rvce.edu.in", "password") 

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    count =0
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
    
        cv2.imshow(frame)
    
        if((obj.data) == b'1'):
    
            message = "test2"
            s.sendmail("amitskotagi.cs18@rvce.edu.in", "amitkotagi@gmail.com", message)
        
        
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
    
        break
pos = obj.data
print(str(obj.data))
cv2.destroyAllWindows()
cap.release()