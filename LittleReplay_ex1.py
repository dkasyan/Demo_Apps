dic_shop = {
    "Papierniczy": ("ołówek", "kartki", "długopis"),
    "Warzywniak": ("pomidor", "ogórek", "ziemniaki"),
    "Mięsny": ("schabowy", "mielonka")
}
print(dic_shop["Papierniczy"])

for i in dic_shop:
    print(f"Idę do {i}, kupuję tu następujące rzeczy: {list(dic_shop[i])}")