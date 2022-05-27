#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture("q1.mp4")

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
            
    print("")
    uni = soma
    resultado = dec + uni
    print("RM", rm[0], "+", rm[1], "+", rm[2], "+", rm[3], "+", rm[4], "=", dec, "+", uni, "=", resultado)

    return resultado

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # Seu código aqui.
    
    '''
    resultado = tirando_rm() 
    
        if resultado == 1 or resultado == 2:
            
        elif resultado == 3 or resultado == 4:

        elif resultado == 5 or resultado == 6:

        elif resultado == 7 or resultado == 8:

        else:
    '''
    
    # Exibe resultado
    cv2.imshow('Feed', frame)

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()