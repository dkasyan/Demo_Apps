name_list = ("John", "Michael", "Terry", "Eric", "Graham")

name_dictionary = dict()

for name in name_list:
    lenght = (len(name))
 #   name_dictionary[name] = lenght
    name_dictionary.update({name : lenght})

print(name_dictionary)

#### Zadanie drugie ###
leng = name_dictionary.values()
number_list = {1, 2, 3, 5, 6, 11, 12, 18, 19, 21}
print(number_list)
new_number_list = number_list.intersection(leng)
print(new_number_list)

#### Zadanie trzecie ###

weak_days = {'pon','śro','pią','sob'}
print(f"przed zmianami zbiór to {weak_days}")
weak_days.update({"wto", "czwa", "nied"})
print(f"po zmianach zbior to {weak_days}")

#### Zadanie czwarte ###

shopping_list = ["włącz czajnik", "znajdź opakowanie herbaty", "zalej herbatę", "nalej wody do czajnika", "wyjmij kubek", "włóż herbatę do kubka"]

for i in range(len(shopping_list)):
    print(shopping_list[i])



