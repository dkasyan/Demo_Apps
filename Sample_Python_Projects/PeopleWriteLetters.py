name_list = ("John", "Michael", "Terry", "Eric", "Graham")

name_dictionary = dict()

for name in name_list:
    lenght = (len(name))
    name_dictionary[name] = lenght
 #   name_dictionary.update({name : lenght})

print(name_dictionary)

#### Zadanie drugie ###
leng = name_dictionary.values()
number_list = {1, 2, 3, 5, 6, 11, 12, 18, 19, 21}
prime_list = []
count_list = []

for number in number_list:
    for i in range(1, number):
        if number % i == 0:
            count_list.append(number)
    if count_list.count(number) == 1:
        prime_list.append(number)
prime_list.append(1)
prime_list.sort()
print(prime_list)

#    print(number)
#    for i in range(2,number - 1):
#    if number % i == 0:
#            print(number)
    

#### Zadanie trzecie ###

week_days = ['pon','śro','pią','sob']
miss_days = ['wto', 'czw', 'nie']

week_days = {'pon':1,'śro':3,'pią':5,'sob':6}
miss_days = {'wto':2, 'czw':4, 'nie':7}
week_days.update(miss_days)
a = sorted(week_days.items(), key=lambda x: x[1]) #Wyjaśnić to na supporcie   
print((a[1:1])[:4])
#days = miss_days + week_days
#day_1, day_3, day_5, day_6, day_2, day_4, day_7 = days
#print(day_1)
#string_day = []
#for day in range(1, 8):

#    string_day.append(f"day_{day}")

#for good_day in string_day:
#    print(good_day)
#print(string_day)
#week_days.sort()
#print(f"przed zmianami zbiór to {week_days}")

#print(f"po zmianach zbior to {days}")

#### Zadanie czwarte ###

shopping_list = ["włącz czajnik", "znajdź opakowanie herbaty", "zalej herbatę", "nalej wody do czajnika", "wyjmij kubek", "włóż herbatę do kubka"]

for i in range(len(shopping_list)):
    print(shopping_list[i])



