hamburger = ["Bułka", "Wołowina", "Pomidor", "Burak", "Bataty", "Ser feta", "Mango" ]
for element in hamburger:
    print(element)

print("innepodejscie#############")

burger_iterator = iter(hamburger)
#print(burger_iterator)
#for u in burger_iterator:
#    print(u)


#print(next(burger_iterator))

#print(next(burger_iterator))

#print(next(burger_iterator))

#print(next(burger_iterator))

#print(next(burger_iterator))

#print(next(burger_iterator))

#print(next(burger_iterator))

#print(next(burger_iterator))

######

shopping = [("buraki", 1.25), ("mleko", 4.0), ("chleb", 3.50), ("wino", 15)]
for product, price in shopping:
    print(product)

#

neighbors = [("Czechy", "Praga"), ("Słowacja", "Bratysława"), ("Ukraina", "Kijow" ), ("Białoruś", "Mińsk"), ("Litwa", "Wilno"), ("Rosja", "Moskwa"), ("Niemcy", "Berlin")]
print(type(neighbors))
neighbors_dict = dict(neighbors)
print(type(neighbors_dict))
for country in neighbors_dict.items():
    print(country)