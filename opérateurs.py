# + - * /
result = 123 + 4.14
print(result)

result = (1 + 2 ) * 3
print(result)



# // % **

#division entiere
result = 1 // 3
print(result)

#modulo
result = 10 % 3
print(result)

#verification de la divisibilité
result = (2512629853 + 1) % 7
print(result)

#puissance 
#dans certains langage c'est : ^, pow()
result = 3**2 
print(result)

#racine carré 
result= 3 ** (1/2)
print(result)
#racine cubique 
result= 3 ** (1/3)
print(result)

# | ou
# & et 
# << decalage vers la gauche
# >> decalage vers la droite

#opérateur boolean "and"
result = True and True #True
result = True and False #False
result = False and True #False
result = False and False #False

# s'il n'y a que des "and", l'ordre n'est pasd important
result= True and False and True and False # False

#opérateur boolean "or"
result = True or True #True
result = True or False #True
result = False or True #True
result = False or False #False

# s'il n'y a que des "or", l'ordre n'est pasd important
result= True or False or True or False # True

#opérateur booléen "xor"
result = True ^ True #False
result = True ^ False #True
result = False ^ True #True
result = False ^ False #False

#opérateur composés (n'existe pas en pyhton)
# c++ <=> c = c + 1

number = 42 
# number = number + 1
number += 1

# comparaison 
# == != < > <= >=
#
#pas en python
# === !==


#operateur == fait ofice de comparaison d'indentité
a = 123
b = 145 
result = a == b


#valeur booleen dans un tableau
fruits = ["apple", "banana", "cherry"]
result= "banana" in fruits
print(result)

fruits = ["apple", "banana", "cherry"]
result = "orange" in fruits
print(result)

#verification de type de donnée
result = type(123) is float
print(result)