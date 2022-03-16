from operator import truediv
import random


firstname = "toto"
lastname = "pop"
number = "2"


email = firstname + '.' + lastname + number + '@example.com'
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("vous n'avez pas de nouveaux mails")
elif new_emails == 1:
    print("vous avez reçu un nouveau mail")
else:
    print("Vous avez reçu <strong>" + str(new_emails) + "</strong> nouveaux mails")

stock = random.randint(0, 10)

if stock == 0 :
    print("stock épuisé")
elif stock == 1 :
    print("Stock en tension : 1 piece")
elif 1 < stock < 5 :
    print(f"stock en tension : {stock} pieces")
elif 5 <= stock < 10 :
    print(f"stock confortable : {stock} pieces")
elif 10 <= stock :
    print(f"Stock en surnombre : {stock} pièce")

temperature = 10.1 + 0.1 + 0.1
print(temperature)

print(f"La temperature actuelle est de {temperature:.2}°C")


electricite = False

if electricite :
    # ne pas faire d'interpolation de variable booléennes si votre appli n'est pas en anglais
    print("electricité : vrai")
else : 
    print("electricite : faux ")


print(f"le nombre tiré au hasard est : {random.randint(0, 10)}")

# @todo afficher age a partir de l'année de naissance 

texte = "foo bar baz"
#len == lenght == longueur
print(len(texte))


print(texte.find("banana"))
print(texte.find("baz"))

texte = "Bonjour Toto"


if texte.find("Toto") >= 0:
    print("On as trouvé Toto")
else < 0:
    print("On as pas retrouvé Toto")

if texte.find("Titi") >= 0:
    print("On as trouvé Titi")
else < 0 :
    print("On as pas retrouvé Titi")