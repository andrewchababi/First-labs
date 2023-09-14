# Demander à l'utilisateur de choisir le type de conversion
print("""Type de conversion :
1: Kilometres vers Miles (K vers M)
2: Miles vers Kilometres (M vers K)""")
choix = int(input("Entrez votre choix (1 ou 2): "))

# Demande de la distance à l'utilisateur
distance = float(input("Entrez la distance a convertir: "))


# Vérifie si l'utilisateur a choisi la conversion de kilomètres en miles
choixKmEnMiles = choix == 1

# Conversion de la distance en fonction du choix de l'utilisateur
if choixKmEnMiles:
    # Conversion de kilomètres en miles
    miles= distance*0.621371
    # Affichage du résultat de la conversion
    print(f"{distance} kilometres equivalent a {miles} miles.")

else:
    # Conversion de miles en kilomètres  
     kilometres = distance / 0.621371

    # Affichage du résultat de la conversion
     print(f"{distance} miles equivalent a {kilometres} kilomètres.")