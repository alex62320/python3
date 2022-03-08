from operator import truediv
import random

# if True:
#     print("ce message sera toujours affiché")

# if False:
#     print("ce messsage ne sera jamais affiché")

# if True:
#     print("ce message sera toujours affiché(if True)")

# else:
#     print("ce messsage ne sera jamais affiché(if True)")

# if False:
#     print("ce messsage ne sera jamais affiché(if False)")

# else:
#     print("ce message sera toujours affiché(if False)")

# fruits = ['banana', 'apple', 'cherry']
# if 'apple' in fruits:
#     print("il y a des pommes ")
# else:
#     print("il n'y a pas de pommes ")

# if 'orange' in fruits:
#     print("il ya des oranges")
# else:
#     print("il n'y a pas d'orange")

# is_authentificated = True
# if is_authentificated:
#      print("L'utilisateur peut acceder au pages")
# else:
#     print("vous n'êtes pas connecter")

# user_password = "123"
# user_password_in_db = "abc"

# if user_password == user_password_in_db:
#     print("L'utilisateur peux acceder au backoffice")
# else:
#     print("donnée incorrecte")

# is_authentificated = True
# users_in_db =['toto', 'titi','tata','tutu']
# tutu_password_in_db = "abc"

# user_name_in_form = 'tutu'
# user_password_in_form ="123"

# if is_authentificated or (user_name_in_form in users_in_db and user_password_in_form == tutu_password_in_db):
#     print("Vous etes connecter")
# else:
#     print("Donnée incorrecte")

# electricity = bool(random.randint(0, 1))
# water = bool(random.randint(0, 1))
# gaz = bool(random.randint(0, 1))

# print('electricity:',electricity)
# print('water:',water)
# print('gaz:',gaz)

#verifiez que toutes source sont couper 
#si c'est le cas affichez le message "vous pouvez partir en weekend"
#sino affichez le message "Il reste des source a couper"

# if electricity and gaz and water :
#     print("Vous pouvez partir en weekend")
# else:
#     print("Il reste des source a coupé")

#     if not electricity:
#         print("coupez l'electricité")
#     if not water:
#         print("coupez l'eau")
#     if not gaz: 
#         print("coupez le gaz")


# has_cash = bool(random.randint(0, 1))
# has_card = bool(random.randint(0, 1))
# has_check = bool(random.randint(0, 1))
# print('carte:',has_card)
# print('cash',has_cash)
# print('cheque:',has_check)

# if has_check or has_card or has_cash:
#     print("vous pouvez payer")
#     if has_card:
#         print("vous avez une carte")
#     if has_cash:
#         print("vous avez du cash")
#     if has_check:
#         print("vous avez un cheque")
# else:
#     print("vous avez pas de quoi payer")
    
age = random.randint(0, 100)

# 0-5 bébé
#6-11 enfant
#12-25 ado et jeune adulte
#26-59 adulte
#60+ senior

if age <= 5:
        print("bébé")
elif 6 <= age <= 11 :
        print("enfant")
elif 12 <= age <= 25 :
        print("ado ou jeune adulte")
elif 26 <= age <= 59 :
        print("adultes")
elif age >= 60 :
        print("sénior")

if 123: 
    #le message s'afficheras car bool(123) == True
    print("il y a une valeur numérique positive")


if 0: 
    #le message s'afficheras pas car bool(0) == False
    print("il y a une valeur nul")


if -123:
    print("il y a une valeur negatif")