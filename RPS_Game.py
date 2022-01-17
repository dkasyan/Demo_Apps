import random

plays = 12 #Number of plays
choices = ["r", "p", "s"]
computer_plays = []
player_plays = []
zero = 0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
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

def compare_choice(player,computer):
    if player == computer:
        print(f"{player} vs {computer}\n remis")
    elif( player == "r" and computer =="s"):
        print(f"{rock} vs {scissors}\n Wygrał kamien gracza")
    elif( player == "p" and computer =="r"):
        print(f"{paper} vs {rock}\nWygrały papier gracza")
    elif( player == "s" and computer =="p"):
        print(f"{scissors} vs {paper}\nWygrały norzyce gracza")
    elif( player == "r" and computer =="p"):
        print(f"\nWygrał kamien komputera")
    elif( player == "p" and computer =="s"):
        print(f"\nWygrały papier komputera")
    elif( player == "s" and computer =="r"):
        print(f"\nWygrały norzyce komputera")





while zero != plays:
    player_choice = check_selection(input("Podaj r/p/s:"))
    player_plays.append(player_choice)
    computer_choice = random.choice(choices)
    computer_plays.append(computer_choice)
    compare_choice(player_choice,computer_choice)
    zero = zero + 1

print(player_plays)
print(computer_plays)





