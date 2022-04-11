from voiture import Voiture

v1 = Voiture("BMW", "Serie 5", "Diesel", "Berline", 0)
# il ne faut pas afficher directement ces variables car elles sont considérées comme ci elles etaient privées 
# c-a-d qu'elles sont toutes prefixes d'un underscore "_"
# print(v1.marque, v1.modele, v1.carburant, v1.type_carroserie, v1.get_vitesse())
print(v1.set_vitesse(10))
print(v1.get_vitesse())
print(v1)

v2 = Voiture("Ford", "Mustang 68", "Essence", "muscle car", 0)
print(v2.set_vitesse(100))
print(v2.get_vitesse())

# print(v2.set_vitesse("très vite"))
# # transmettre une valeur autre qu'un int genere l'erreur "Exception"

print(v2)
print(v1.get_vitesse())