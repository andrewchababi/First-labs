#Étant donné une phrase par l'utilisateur, écrivez une fonction qui
#construit et affiche l'histogramme des lettres utilisées dans la phrase.

"""def histogramme_de_lettre():
    phrase = str(input("Quelle phrase aimerai vous classe ? "))
    histo = {char: 0 for char in phrase if char in histo histo[char] += 1 else histo[char] = 1}
    for char in phrase:
        if char in histo:
            histo[char] += 1
        else:
            histo[char] = 1
    return histo
"""
#print(histogramme_de_lettre())

phrase = "test this out"
histo = {char: phrase.count(char) for char in phrase}
print(histo)
