  
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
