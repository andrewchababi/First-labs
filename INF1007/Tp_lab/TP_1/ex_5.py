# Demande à l'utilisateur d'entrer le montant initial de l'investissement
montant = float(input("Entrez le montant initial: "))
# Demande à l'utilisateur d'entrer le taux d'intérêt annuel en pourcentage
interet = float(input("Entrez le taux d'interet annuel (en %): "))/100
# Demande à l'utilisateur d'entrer le nombre d'années de l'investissement
t = float(input("Entrez le nombre d'annees de l'investissement: "))
# Calcule le montant final en utilisant la formule de l'intérêt composé
montant_accumule = montant*(((1+interet)**t))
# Affiche le montant final avec deux décimales
print(f"Montant final apres 25 ans: {round(montant_accumule,2)}")
