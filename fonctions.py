# le scores des 5 joueurs
scores = [433, 562, 574, 800, 953]

# données en entrée : une liste d'int
# données de sorties : un int

def int_average(numbers: list) -> int:
    """
    Cette fonction renvoie un arrondie de la moyennes des nombres passés en 
    paramètres

    number: list Cette liste contient les nombres (int ou float) ou il faut 
    calculer la moyennes.
    return: int La fonctions renvoient une moyennes arrondis au format int.
    """
    n = len(scores)
    # le nombre de scores


    #initialisation de l'accumulateur
    total = 0

    #existe mais pas pédagogique
    # total = sum(scores)

    for number in numbers:
        total += number

    #moyenne = total / nombre d'elements
    average = total / n
    average = round(average)

    return average


# le scores des 5 joueurs
scores = [302, 102, 956, 987, 931]

average = int_average(scores)
print(average)

# le scores des 5 joueurs
scores = [433, 562, 574, 800, 953]

average = int_average(scores)
print(average)
