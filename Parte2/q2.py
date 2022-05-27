#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2, time
import numpy as np
import dlib as d
from math import hypot

def count(event):
    if event == cv2.EVENT_LBUTTONDOWN:
        return 1
    elif event == cv2.EVENT_LBUTTONDOWN * 2:
        return 2
    elif event == cv2.EVENT_LBUTTONDOWN * 3:
        return 3
    elif event == cv2.EVENT_RBUTTONDOWN:
        return 4

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0) 
nose_image = cv2.imread("./assets/img/doggy_nose.png")

detector = d.get_frontal_face_detector()
predictor = d.shape_predictor("./Parte2/trainingShape/shape_predictor_68_face_landmarks.dat")

while True:
    ret, frame = cap.read()
    frame_base = frame.copy()
    frame2 = frame.copy()

    cv2.namedWindow("Feed")
    counter = cv2.setMouseCallback("Feed", count)
    
    if not ret:
        break
    
    # Seu código aqui. 
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(frame_gray,scaleFactor=1.1,minNeighbors=5)

    for x,y,w,h in face:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        img[y:y + h, x:x + w] = cv2.medianBlur(img[y:y + h, x:x + w], 35)

    filtro_blur = frame
    frame = frame2

    faces = detector(frame)
    for face in faces:
        landmarks = predictor(frame_gray, face)

        top_nose = (landmarks.part(29).x, landmarks.part(29).y)
        center_nose = (landmarks.part(30).x, landmarks.part(30).y)
        left_nose = (landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)
        
        nose_width = int(hypot(left_nose[0] - right_nose[0],
                               left_nose[1] - right_nose[1]) * 2.7)

        nose_height = int(nose_width * 0.58)
        
        top_left = (int(center_nose[0] - nose_width / 2), 
                    int(center_nose[1] - nose_height / 2))


        bottom_right = (int(center_nose[0] + nose_width / 2), 
                        int(center_nose[1] + nose_height / 2))
        #cv2.circle(frame, top_nose, 3, (255, 0, 0), -1)
        nose_dog = cv2.resize(nose_image, (nose_width, nose_height))
        nose_dog_gray = cv2.cvtColor(nose_dog, cv2.COLOR_BGR2GRAY)
        ret, nose_mask = cv2.threshold(nose_dog_gray, 25, 255, cv2.THRESH_BINARY_INV)

        nose_area = frame[top_left[1]: top_left[1] + nose_height,
                          top_left[0]: top_left[0] + nose_width]

        nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
        final_nose = cv2.add(nose_area_no_nose, nose_dog)

        
        frame[top_left[1]: top_left[1] + nose_height,
             top_left[0]: top_left[0] + nose_width] =  final_nose

    
    # Exibe resultado
    if counter == 1:
        cv2.imshow("Feed", frame)
    elif counter == 2:
        cv2.imshow("Feed", frame)
    elif counter == 3:
        cv2.imshow("Feed", frame)
    elif counter == 4:
        cv2.imshow("Feed", frame_base)

    cv2.imshow("Filtro 1", filtro_blur)
    cv2.imshow("Filtro 2", frame)
    cv2.imshow("Sem filtro", frame_base)
    #cv2.imshow("Dog nose", nose_dog)

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()