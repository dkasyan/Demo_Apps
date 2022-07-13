x = range(101)
even_list = []
no_even_list = [] 
for n in x:
  k = (n % 2)
  if k == 0:
    even_list.append(n)
  else:
    no_even_list.append(n)
print(even_list)
