# On demande à l'utilisateur d'entrer la longueur du rectangle en tant que nombre décimal (float).
longueur = float(input("Entrez la longueur du rectangle: "))
# On demande à l'utilisateur d'entrer la largeur du rectangle en tant que nombre décimal (float).
largeur = float(input("Entrez la largeur du rectangle: "))
# On calcule le périmètre du rectangle en utilisant la formule : 2 * (longueur + largeur).
périmètre = 2 * (longueur + largeur)
# On calcule l'aire du rectangle en utilisant la formule : longueur * largeur.
aire_rectangle = longueur * largeur
# On affiche le périmètre du rectangle.
print("Le perimetre du rectangle est: "+ str(périmètre))
# On affiche l'aire du rectangle.
print("L'aire du rectangle est: " + str(aire_rectangle))