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
#print(histo)


dist = [[0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 7, 8, 9], [0, 1, 4, 5, 6, 7, 8, 9], [0, 1, 5, 6, 7, 9]]
#print(dist)

def return_3rd_item(sublist):
    return sublist[2]

#print(sorted(dist,key= return_3rd_item,reverse= False))


#ecrir une fonction qui retourn la some des N nombres premier, N est determine par l'utilisatreur



def som_N_premier(N):
    def est_nombre_premier(nombre):
        if nombre < 2:
            return False
        for x in range(2, int(nombre**0.5) + 1):  # Correction here for square root calculation
            if nombre % x == 0:
                return False
        return True
    counter = 0 
    somme = 0 
    nombre = 2
    while counter < N:
        if est_nombre_premier(nombre):
            somme += nombre
            counter += 1
        nombre += 1
    return somme

print(som_N_premier(9))