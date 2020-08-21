#Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do 10. Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.

new_list = []
list = [ number ** 3 for number in range(10)]

print(list)

for i in list:
    if i % 2 != 0 :
        new_list.append(i)

print(new_list)
