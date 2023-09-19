# Demander à l'utilisateur d'entrer les coefficients de l'équation quadratique
coef_a = float((input("Veuillez entrer la valeur de a (coefficient de x^2): ")))

coef_b = float((input("Veuillez entrer la valeur de b (coefficient de x): ")))

coef_c = float((input("Veuillez entrer la valeur de c (terme constant): ")))

# Calculer le discriminant
#Δ = b² - 4ac

delta = coef_b**2 - 4*coef_a*coef_c


# Vérifier si le discriminant est négatif (aucune racine réelle)
naPasDeSolution = delta < 0

if naPasDeSolution:
    # Cette ligne de code sera exécutée si le projectile n'atteint jamais l'altitude désirée.
    print("Le projectile n'atteint jamais l'altitude desiree.")

else:
    # Vérifier si le discriminant est nul (une seule racine réelle)
    aUneSeuleSolution = delta == 0

    if aUneSeuleSolution:
        # Calculer l'instant unique où le projectile atteint l'altitude
        x1 = -coef_b/(2*coef_a)
       

        # Vérifier si l'instant est positif
        estInstantPositif = x1 >= 0
        if estInstantPositif:
            # Afficher l'instant
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print(f"Instant de l'impact:  {x1:.1f}")


        else:
            # Afficher que le projectile n'atteint jamais l'altitude désirée.
            print("Le projectile n'atteint jamais l'altitude desiree.")

    else:
        # Calculer les deux instants où le projectile atteint l'altitude
        x1 = (-coef_b + delta**0.5) / (2*coef_a)
        x2 = (-coef_b - delta**0.5) / (2*coef_a)


        # Vérifier si les instants sont positifs
        estInstant1PositifInstant2Negatif = x1>=0 and x2<0
        estInstant2PositifInstant1Negatif = x2>=0 and x1<0
        estInstant1PositifInstant2Positif = x1 >=0 and x2 >=0
        
        if estInstant1PositifInstant2Negatif:
            # Afficher l'instant positif
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print(f"Instant de l'impact: {x1:.1f}")

        elif estInstant2PositifInstant1Negatif:
            # Afficher l'instant positif
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print(f"Instant de l'impact: {x2:.1f}")

        elif estInstant1PositifInstant2Positif:
            # Afficher les deux instants
            print("Le projectile atteint l'altitude a deux moments distincts.")
            print(f"Instants de l'impact: t1 = {x1:.1f} secondes et t2 = {x2:.1f} secondes.")
            
        else:
            # Afficher que le projectile n'atteint jamais l'altitude désirée.
            print("Le projectile n'atteint jamais l'altitude desiree.")
