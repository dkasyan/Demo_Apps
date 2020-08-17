shoping_list = {"jajo", "jako", "jajo", 2, "jajo"}
#print(shoping_list)
#print(type(shoping_list))

tasty_cocktail = [1, "mydło", None, "powidło", 0.1]
#print(tasty_cocktail)


list_of_courses = ["północ", "południe"]
new_list_of_courses = list_of_courses + ["północ"]
#print(list_of_courses)
list_of_courses.append("wschód")
list_of_courses = list_of_courses + ["zachód"]
print(list_of_courses)


#Następnie usuń północ i południe, żeby zostawić tylko 2 kierunki. Do usuwania posłuż się komendą del. Wydrukuj listę 2 elementów, które zostały. Następnie usuń zachód komendą remove. Teraz został Ci tylko wschód (“Na wschód, tam musi być jakaś cywilizacja”). Wydrukuj także tą, jednoelementową listę.

del list_of_courses[0]
del list_of_courses[0]
list_of_courses.remove("zachód")
print(list_of_courses)

#Stwórz listę z liczbami: 3, 6, 17, 4, 0, -20, 20, 100. Następnie posortuj ją. Możesz wykorzystać wbudowaną metodę sort, albo wbudowaną funkcję sorted. Wynik wyświetl na ekranie.
number_list = [3, 6, 17, 4, 0, -20, 20, 100 ]
print(number_list)
sort_number_list = sorted(number_list)
print(sort_number_list)
number_list.sort()
print(f"Lista po sortowaniu: {number_list}")