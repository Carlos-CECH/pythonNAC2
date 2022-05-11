#!/usr/bin/python 
#-*- coding: utf-8 -*-

import cv2

window = cv2.namedWindow('Feed')
cap = cv2.VideoCapture('q1.mp4')

if cap.isOpened() == False:  
  print("Error opening video file") 

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        
        # Seu código aqui. 
        
        # Exibe resultado
        cv2.imshow('Feed', frame)

        # Wait for key 'ESC' to quit
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
            break
    
    else:
        break
# That's how you exit
cap.release()
cv2.destroyAllWindows()