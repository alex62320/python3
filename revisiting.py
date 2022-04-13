import random

# Exo 1.1
# Affichez le type de donnée des variables a et b.

a = 3.14
b = 3

# Réponse 1.1
print(type(a))
print(type(b))
# Exo 1.2
# En utilisant les variables a et b, affichez les chiffres après la virgule de la variable a.

a = 3.14
b = 3

# Réponse 1.2

print(a-b)
print(round(a-b ,2))

# Exo 1.3
# Affichez le type de données de la variable n.

n = random.randint(10, 99) / 10

# Réponse 1.3

print(type(n))

# Exo 1.4
# Convertissez n en un nombre entier, stockez le résultat dans une variable et affichez le résultat.

n = random.randint(10, 99) / 10

# Réponse 1.4
result= int(n)
print(result)
print("\n")
# Exo 1.5
# Affichez :
# - les nombres avant la virgule de la variable n
# - les nombres après la virgule de la variable n

n = random.randint(10, 99) / 10

# Réponse 1.5
print(n)
print(int(n))
print(n-int(n))
print("\n")
# Exo 1.6
# Stockez dans une variable si la variable n est un nombre entier ou non.

n = random.randint(10, 99) / 10

# Réponse 1.6
print(n)
result =  n == int(n)
print(result)
print("\n")

#exo 2.1
# afficher le texte "foo" si la variable n est inférieur a 5
toto = random.randint(0,9)
print(toto)

while toto <= 5:
    print("foo")
    toto = random.randint(0,9)
    print(toto)
print("\n")
#exo 2.2
# afficher "foo" le temps que le chiffre tiré au harsard est plus petit que 5 
# vous pouvez utiliser random.int(0, 9) pour tirer au hasard

# réponse 2.2

if random.randint(0, 9) < 5:
    print("foo")
    

print("\n")

#exo 2.x
# afficher "foo" le temps que le chiffre tiré au harsard est plus petit que 5 
# vous pouvez utiliser random.int(0, 9) pour tirer au hasard

# réponse 2.x

while random.randint(0,9) < 5:
    print('foo')

print("\n")

while True:
    if random.randint(0, 9) < 5:
        print("foo")
    else:
        break

print("\n")

while True:
    if random.randint(0, 9) >= 5:
        print("foo")
    else:
        break
