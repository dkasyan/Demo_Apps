import random

plays = 3
choices = ["rock", "paper", "scissors"]
computer_plays = []
player_plays = []
zero = 0
r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def check_selection(a):
    i = True
    while i != False :
        if a =="r" or a =="p" or a =="s":
            print(f'Wybrałeś {a}')
            i = False
        else:     
            a = input("Ups podaj wlasciwa opcje r/p/s: ")
    return(a)

computer_plays.append(random.choice(choices))


while zero != plays:
    zmienna = input("Podaj")
    twoj_wyb = check_selection(zmienna)
    player_plays.append(twoj_wyb)
    computer_plays.append(random.choice(choices))
    zero = zero + 1

zero = 0
while zero != plays:
    if player_plays[zero] == computer_plays[zero]:
        print ("remis")
    else:
        print("wygrana")
    zero = zero + 1




