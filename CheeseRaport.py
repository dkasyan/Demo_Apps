name_roquefort = "roquefort"
price_roquefort = 12.50
name_stilton = "stilton"
price_stilton = 11.24
name_brie = "brie"
price_brie = 9.30
name_gouda = "gouda"
price_gouda = 8.55
name_edam = "edam"
price_edam = 11
name_parmezan = "parmezan"
price_parmezan = 16.50
name_mozzarella = "mozzarella"
price_mozzarella = 14
name_czechoslovak_sheep_cheese = "czechosłowacki ser z owczego mleka"
price_czechoslovak_sheep_cheese = 122.32
text = "Kupiłem {} w cenie {} zł"

print("####################### SHOP LIST #######################")
#print( "Kupiłem %s w cenie %d zł" % (name_roquefort, price_roquefort))
print( f"Kupiłem {name_roquefort} w cenie {price_roquefort:.2f} zł")
print( f"Kupiłem {name_stilton} w cenie {price_stilton:.2f} zł")
print( f"Kupiłem {name_brie} w cenie {price_brie:.2f} zł")
#print( "Kupiłem %s w cenie %s zł" % (name_gouda, price_gouda))
print( f"Kupiłem {name_gouda} w cenie {price_gouda:.2f} zł")
#print( text.format(name_edam, price_edam))
print( f"Kupiłem {name_edam} w cenie {price_edam:.2f} zł")
#print( text.format(name_parmezan, price_parmezan))
print( f"Kupiłem {name_parmezan} w cenie {price_parmezan:.2f} zł")
#print( "Kupiłem %s w cenie %s zł" % (name_mozzarella, price_mozzarella))
print( f"Kupiłem {name_mozzarella} w cenie {price_mozzarella:.2f} zł" )
print( text.format(name_czechoslovak_sheep_cheese, price_czechoslovak_sheep_cheese:.2f))
#print( f"Kupiłem {name_czechoslovak_sheep_cheese} w cenie {price_czechoslovak_sheep_cheese:.2f} zł")
