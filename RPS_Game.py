import random


# #1) stwórz pętle 3

# #    2) Stwórz liste trzech opcji
# #    3) Wylosuj za pomoca losowania z listy pierwsza opcje i dodaj ja do listy 
# # Do ilu gramy ?

#1) stwórz pętle 3

# #    2) Stwórz liste trzech opcji
# #    3) Wylosuj za pomoca losowania z listy pierwsza opcje i dodaj ja do listy 
# # Do ilu gramy ?
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


zmienna = input("Podaj")

twoj_wyb = check_selection(zmienna)
print(twoj_wyb)


