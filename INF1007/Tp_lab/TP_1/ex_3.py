# Demande à l'utilisateur d'entrer une phrase.
phrase = str(input("Entrez une phrase: "))
# Divise la phrase en mots en utilisant l'espace comme séparateur et compte le nombre de mots
mot_div = phrase.split(" ")
# Affiche le nombre de mots dans la phrase
nbr_mot = len(mot_div)
print("La phrase contient "+ str(nbr_mot) +" mots.")
# Affiche la phrase en lettres majuscules
print("Phrase en majuscules: " + phrase.upper())
