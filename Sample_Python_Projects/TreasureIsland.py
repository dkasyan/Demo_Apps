print("Welcome to Treasure Island. \n Your mission is to find the treasure! \n Chose... left or right")



k = True
while k == True:
    a = input(": ")
    if a == "left" or a == "right":
        k = False
    else:
        print("Powtórz")

if a == "right":
    print("Game Over")
    exit()

k = True   
while k == True:
    print("Widzisz fose co robisz? ")
    b = input("Chose swim or wait: ")
    if b == "swim" or b == "wait":
        k = False
    else:
        print("Powtórz")


if b == "swim":
    print("Game Over")
    exit()

k = True
while k == True:
    print("Dochodzisz do drzwi o kolorach czerwony, niebieski, zółty.")
    c = input("Które drzwi wybierasz? Blue, Yellow or Red ? : ")
    if c == "Blue" or c == "Yellow" or c == "Red":
        k = False
    else:
        print("Powtórz")

if c == "Red" or c == "Blue":
    print("Game Over")
    exit()
else:
    print("You Win")


