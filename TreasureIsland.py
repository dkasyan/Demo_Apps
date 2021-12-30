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
    

while k == True:
    print("Widzisz fose co robisz? ")
    b = input("Chose swim or wait: ")
    if a == "swim" or a == "wait":
        k == False
    else:
        print("Powtórz")

#if b == "swim":
#    ending()


