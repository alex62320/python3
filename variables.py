# ceci est un commentaire

# foo
# bar
# baz

from re import A
from unittest import result


# nombre = 123
# print(nombre)
# print(type(nombre))

# nombre = 123.0
# print(nombre)
# print(type(nombre))

# nombre = 3.14
# print(nombre)
# print(type(nombre))

# nombre = "123"
# print(nombre)
# print(type(nombre))

# text = "lorem ipsum"
# print(text)
# print(type(text))

# is_day = True
# print(is_day)
# print(type(is_day))

# has_sugar = False
# print(has_sugar)

# has_accepted_ula = None
# print(has_accepted_ula)
# print(type(has_accepted_ula))

# html_code = '<h1>titre de mon blog</h1>'
# print(html_code)

# nickname = "John \" dead\" Doe"
# nickname = 'John \'dead\' Doe'
# nickname = ' John O\'Connor'
# print(nickname)

# multiline_text = "foo\nbar\nbaz"
# print(multiline_text)

# multiline_text = """foo
# bar
# baz
# """
# print(multiline_text)

# nombre = "5"
# print(nombre)
# print(type(nombre))
# nombre = int(nombre)
# print(nombre)
# print(type(nombre))

# nombre = "2.71"
# print(nombre)
# print(type(nombre))
# nombre = float(nombre)
# print(nombre)
# print(type(nombre))

# nombre = 3.14
# print(nombre)
# print(type(nombre))
# nombre = int(nombre)
# print(nombre)
# print(type(nombre))

# texte = str(nombre)
# print(texte)
# print(type(texte))

# my_var = 0
# my_var = bool(my_var)
# print(my_var)

# my_var = -123
# my_var = bool(my_var)
# print(my_var)

# my_var = -123
# my_var = bool(my_var)
# print(my_var)

# my_var = "0"
# my_var = bool(my_var)
# print(my_var)

# my_var = ""
# my_var = bool(my_var)
# print(my_var)

# my_var = "123"
# my_var = bool(my_var)
# print(my_var)

# my_var = "-123"
# my_var = bool(my_var)
# print(my_var)

# my_var = [False]
# my_var = bool(my_var)
# print(my_var)

#swap 
a = 42
b = 123

 # a == 123 and b == 42

#methode classique 
c = a 
a = b 
b = c

#destructured assignement
#python et js pas avec php
a, b = b, a

#methode arithmétique
a = a + b
b = a - b 
a = a - b
#resultat
if a == 123 and b == 42:
    print("vous avez réussi à interchanger les valeurs des variables")
#arrondi

import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

Decimal("0.5").quantize(Decimal("1")) # Decimal('1')
Decimal("1.5").quantize(Decimal("1")) # Decimal('2')

print(Decimal("0.5").quantize(Decimal("1")))
print(Decimal("1.5").quantize(Decimal("1")))
