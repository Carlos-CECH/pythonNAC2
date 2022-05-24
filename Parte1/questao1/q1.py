#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


cap = cv2.VideoCapture('./Parte1/questao1/q1.mp4')

def tirando_rm():
    rm = [8, 1, 9, 4, 5]

    soma = 0
    dec = 0
    uni = 0

    for i in range(0, 5):
        soma += rm[i]
        if soma > 10:
            dec += 1
            soma -= 10
        elif i == 5 and soma < 10:
            uni += soma
            soma -= soma
           
    uni = soma
    resultado = dec + uni

    return resultado

while True:
    ret, img = cap.read()

    if not ret:
        break

    # Seu código aqui.
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    resultado = tirando_rm() 

    if resultado == 1 or resultado == 2:

      lower = np.array([0, 0, 50])
      upper = np.array([0, 0, 120])
    
    elif resultado == 3 or resultado == 4:

      lower = np.array([0, 0, 50])
      upper = np.array([0, 0, 120])

    elif resultado == 5 or resultado == 6:

      lower = np.array([0, 0, 50])
      upper = np.array([0, 0, 120])

    elif resultado == 7 or resultado == 8:

      lower = np.array([0, 0, 50])
      upper = np.array([0, 0, 120])

    else:

      lower = np.array([0, 0, 50])
      upper = np.array([0, 0, 120])

    mask = cv2.inRange(image, lower, upper)

    contours, hierarchy = cv2.findContours(
          mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
          if cv2.contourArea(contour) < 500:
              x, y, w, h = cv2.boundingRect(contour)
              cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)

    # Exibe resultado
    cv2.imshow('Mask', mask)
    cv2.imshow('Feed', img)

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(20) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()
