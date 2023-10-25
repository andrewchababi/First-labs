# Affiche un menu d'opérations disponibles
print("""Choisissez une operation:
    1. Addition
    2. Soustraction
    3. Multiplication
    4. Division""")


# Demande à l'utilisateur de saisir le numéro de l'opération choisie
choix = (int(input()))

# Demande à l'utilisateur de saisir deux nombres
nbr_1=(float(input("Entrez le premier nombre: ")))
nbr_2=(float(input("Entrez le second nombre: ")))

# Vérifie si l'opération choisie correspond à l'addition
estAddition = choix == 1
# Vérifie si l'opération choisie correspond à la soustraction
estSoustraction = choix == 2
# Vérifie si l'opération choisie correspond à la multiplication
estMultiplication = choix == 3
# Vérifie si l'opération choisie correspond à la division
estDivision =choix == 4


# Si l'opération choisie est l'addition, affiche le résultat de l'addition
if estAddition:
    answer = nbr_1 + nbr_2
    print("Resultat: " + str(answer))
# Si l'opération choisie est la soustraction, affiche le résultat de la soustraction
elif estSoustraction:
    answer = nbr_1 - nbr_2
    print("Resultat: " + str(answer))
# Si l'opération choisie est la multiplication, affiche le résultat de la multiplication
elif estMultiplication:
    answer = nbr_1 * nbr_2
    print("Resultat: " + str(answer))

# Si l'opération choisie est la division
elif estDivision:
    # Vérifie si la division par zéro est tentée
    conditionDivisionZero = nbr_2 == 0
    # Si la division par zéro est tentée, affiche une erreur
    if conditionDivisionZero:
        print("Erreur: Division par zero.")

    # Sinon, affiche le résultat de la division
    else:
        answer = nbr_1 / nbr_2
        print("Resultat: " + str(answer))
    
# Si l'opération choisie n'est pas valide, affiche un message d'erreur
else:
    print("Erreur: Division par zero.")