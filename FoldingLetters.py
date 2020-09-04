#Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do 10. Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.

new_list = []
list = [ number ** 3 for number in range(10)]

print(list)

for i in list:
    if i % 2 != 0 :
        new_list.append(i)

print(new_list)

#Dana jest lista: [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]. Zadeklaruj ją w Pythonie, a następnie użyj slicingu, by otrzymać listę, która zawiera tylko zera z tej kolekcji. Potem użyj tej samej techniki do zwrócenia listy, która zawiera wszystkie inne liczby tylko nie zera z tej kolekcji.
slice_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

new_slice_zero = []
new_slice_number = []

new_slice_zero = slice_list[1:4] + slice_list[5:10] + slice_list[-2:]

#new_slice_zero.append(slice_list[1:4])
#new_slice_zero.append(slice_list[5:10])
#new_slice_zero.append(slice_list[-2:])

print(new_slice_zero)
new_slice_number = slice_list[0:0]



#new_slice_number.append(slice_list.remove())
print(new_slice_number)
