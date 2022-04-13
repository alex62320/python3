# complexité == efficacité
# efficacité:
# - temps d'execution 
# - espace mémoire 

# notation de landau : O( ) (lettre O, pas le chiffre 0)
# pas une fonction mais un ensemble

# O(c) (c == constante)
# O(1)
# + - * **2 / //


# n est la quantité de donnée à traiter
result= 123 + 42
print(result)

words = ['ananas','banane','cerise','durian','kiwi','orange','pomme']

#recherche par dicothomie
#recherche d'un fruit dont la lettre commence par un c
# O(log(n))
# log == logarythme naturel



numbers = [123, 42, 3.14]

for number in numbers:
    result= number * 2
    print(result) 

#O(n * m) == O(n * n) == O(n²)
# n est la quantité de donnée a traité de la premiere liste
# m est la quantité de donnée a traité de la deuxieme liste
numbers =[123, 42, 3.14]
more_numbers = [2.71, 3.14, 0, 53]
common_numbers = []

for number in numbers:
    # if number in more_numbers:
    #     common_numbers.append(number)
    for more_number in more_numbers:
        if number == more_number:
            common_numbers.append(number)

# O(n²) == O(n * n)
matrix= [
    [123, 42, 3.14]
    [2.71, 3.14, 0]
    [1, 2, 3]
]

for line in matrix:
    for number in line:
        result= number * 2
        print(result)
# # O(n * n * n) == O(n³)
cube= [
    ["a1","a2","a3"]
    ["a4","a5","a6"]
    ["a7","a8","a9"]
],
[
    ["b1","b2","b3"]
    ["b4","b5","b6"]
    ["b7","b8","b9"]
],
[
    ["c1","c2","c3"]
    ["c4","c5","c6"]
    ["c7","c8","c9"]
]

for square in cube:
    for line in square:
        for spot in line:
            print(spot)

# algo pas efficace du tout
# O(n ** n)
# O(n!) == O(n * (n-1) * (n-2) * (n-3) )
# 5! == 5 * 4 * 3 * 2 * 1

# exemple d'optimisation


#exo 1 determiner la complexcité algorithimique de ce programme
#O(n)
numbers = [4, 10, 42, 3.14]
my_list= []

for n in numbers:
    #puissance 2
    result = n ** 2
    my_list.append(result)


#exo 2 determiner la complexcité algorithimique de ce programme
#O(?)
numbers = [4, 10, 42, 3.14]
my_list= []

while True:
    number = numbers.pop()
    my_list.append(number)

    if len(numbers) == 0:
        break
