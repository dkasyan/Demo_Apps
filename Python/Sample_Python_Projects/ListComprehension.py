#Zadanie 1
cube = [number ** 3 for number in range(10)]
for sign in cube:
    if sign % 2 != 0:
        print(sign)
