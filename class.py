from voiture import Voiture
from camion import Camion

v1 = Voiture("BMW", "Serie 5", "Diesel", 0, "Berline")
# il ne faut pas afficher directement ces variables car elles sont considérées comme ci elles etaient privées 
# c-a-d qu'elles sont toutes prefixes d'un underscore "_"
# print(v1.marque, v1.modele, v1.carburant, v1.type_carroserie, v1.get_vitesse())
print(v1.get_marque())
print(v1.get_modele())
print(v1.get_carburant())
print(v1.get_type_carroserie())

print(v1.get_vitesse())
v1.set_vitesse(10)
print(v1.get_vitesse())

v2 = Voiture("Ford", "Mustang 68", "essence", 0, "muscle car")
print(v2)
print(v2.get_vitesse())
# transmettre une valeur de type autre que int génère l'erreur "Exception: La vitesse doit être un nombre entier"
v2.set_vitesse(50)
print(v2.get_vitesse())
print(v1.get_vitesse())


c1 = Camion("Scania", "?", "Diesel", 100 , 19.0)
print(c1)
c2 = Camion("Mercedes", "?", "Diesel", 100 , 19.0)
print(c2)


my_list = []
my_list.append(v1)
my_list.append(v2)
my_list.append(c1)
my_list.append(c2)

for item in my_list:
    print(item._marque)
    print(item.get_vitesse())
    if type(item) is Camion:
        print(item._ptac)
        print(item.get_ptac)
    if type(item) is Voiture:
        print(item._type_carroserie)
        print(item.get_type_carroserie)

for i in range(0, len(my_list)):
    if my_list[i].get_vitesse() > 50:
        print(my_list[i]._marque)
        print(my_list[i].get_vitesse())

print(c1.get_vitesse())
c1.accelerer()
print(c1.get_vitesse())