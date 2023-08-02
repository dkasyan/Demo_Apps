name_roquefort = "roquefort"
price_roquefort = 12.50
weight_roquefort = 0.002 * 10 ** 3
name_stilton = "stilton"
price_stilton = 11.24
weight_stilton = 1
name_brie = "brie"
price_brie = 9.30
weight_brie = 1
name_gouda = "gouda"
price_gouda = 8.55
weight_gouda = 1
name_edam = "edam"
price_edam = 11.00
weight_edam = 1
name_parmezan = "parmezan"
price_parmezan = 16.50
weight_parmezan = 3.5
name_mozzarella = "mozzarella"
price_mozzarella = 14.00
weight_mozzarella = 0.13
name_czechoslovak_sheep_cheese = "czechosłowacki ser z owczego mleka"
price_czechoslovak_sheep_cheese = 122.32
weight_czechoslovak_sheep_cheese = 0.220
name_leaf_mint = ("listek miętowy")
price_leaf_mint = 20
weight_leaf_mint = 0.2

text = "Produkt {}, masa w kg {}, cena {:.2f} zł"

Cost =  price_roquefort + price_stilton + price_brie + price_gouda + price_edam + price_parmezan + price_mozzarella + price_czechoslovak_sheep_cheese

print("Raport z zakupów:")
#print( "Kupiłem %s w cenie %d zł" % (name_roquefort, price_roquefort))
print( text.format( name_roquefort, weight_roquefort, price_roquefort))
print( text.format( name_stilton, weight_stilton, price_stilton))
print( text.format( name_brie, weight_brie, price_brie))
print( text.format( name_gouda, weight_gouda, price_gouda))
print( text.format( name_edam, weight_edam, price_edam))
print( text.format( name_parmezan, weight_parmezan, price_parmezan))
print( text.format( name_mozzarella, weight_mozzarella, price_mozzarella))
print( text.format( name_czechoslovak_sheep_cheese, weight_czechoslovak_sheep_cheese, price_czechoslovak_sheep_cheese))
print( text.format( name_leaf_mint, weight_leaf_mint, price_leaf_mint))
print(" ")
print("...")
print("Suma zł:")
print( Cost)