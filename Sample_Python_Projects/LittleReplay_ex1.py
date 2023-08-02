dic_shop = {
    "Papierniczy": ("ołówek", "kartki", "długopis"),
    "Warzywniak": ("pomidor", "ogórek", "ziemniaki"),
    "Mięsny": ("schabowy", "mielonka")
}
print(dic_shop["Papierniczy"])

numb = 0
for i in dic_shop:
    print(f"Idę do {i}, kupuję tu następujące rzeczy: {list(dic_shop[i])}")
    numb = numb + (len(list(dic_shop[i])))




print(f"W sumie kupuję {numb} produktów.")

#Dodatkowo, używając wbudowanych metod operacji na napisach spowoduj, aby nazwy sklepów i towarów były wypisane z wielkiej litery (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).