x = range(101)
even_list = []
no_even_list = []
total = 0 
for n in x:
  k = (n % 2)
  if k == 0:
    even_list.append(n)
  else:
    no_even_list.append(n)
for i in even_list:
    total = i + total
print(total)
