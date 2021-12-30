print("Welcome to Treasure Island. \n Your mission is to find the treasure! \n Chose... left or right")

def ending():
    print("Game Over")
    exit()

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
        k == False
    else:
        print("Powtórz")

#if b == "swim":
#    ending()


