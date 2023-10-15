import itertools


from random import randint


def magic_numb_game():
    computer_choice = randint(1,10)

    user_choice = int(input("Hey try to guess my number !! "))

    while user_choice != computer_choice:
        if computer_choice < user_choice:
            print("lower")
        else:
            print("higher")
        user_choice = int(input("Try again: "))

    print("You win!")

numbre = 5
result = 1

for i in range(numbre, 1, -1):
    result *= i

print(result)

text = "Le fermier élevait efficacement de magnifiques fleurs près de l'effigie."
words = text.split()
numbre_of_e = 0
numbre_of_f = 0
numbre_of_words = 0

for word in words:
    if word.count("e") >= 2 and "f" in word:
        numbre_of_words += 1
print(numbre_of_words)


                        
#1 Écrire un programme qui lit un nombre et affiche sa valeur absolue

def valeur_absolue(nombre):
    return abs(nombre)

#print(valeur_absolue(-13))


# 2 Dans un conte américain, huit petits canetons 
# s'appellent respectivement : Jack, Kack, Lack, Mack, Nack, Oack, Pack et Qack.
# Écrivez un petit script qui génère tous ces noms à partir 
# des deux chaînes suivantes : prefixes = 'JKLMNOP' et suffixe = 'ack’

def dumb_names():
    prefixes = 'JKLMNOPQ'
    suffixe = 'ack'
    for char in prefixes:
        print(char + suffixe)
    
#dumb_names()


#3 Écrire un programme qui affiche la somme des 100 premiers nombres entiers premiers.

import itertools

def sum_100_nb_premier():
    
    def est_premier(nombre):
        for x in range(2,int(nombre)//2):
            if nombre % x == 0:
                return "n'est pas premier"
        else:
            return True

    
    
    
    nombre_premiers = []
    iterater = itertools.count(2,1)

    while len(nombre_premiers) < 100:
        num = next(iterater)
        if est_premier(num):
            nombre_premiers.append(num)
    
    return sum(nombre_premiers)
            

#print(sum_100_nb_premier())


# 4 Écrire un programme qui calcule le factoriel d’un nombre demandé à l’utilisateur.
def factoriel(nombre):
    for num in range(1,nombre):
        nombre *= num
    return nombre

#print(factoriel(3))
    


#5 Utilisez l’instruction continue pour modifier une boucle for
# d’affichage de tous les entiers de 1 à 10 compris, sauf lorsque la
# variable de boucle vaut 5.

for i in range(11):
    if i == 5:
        continue
    else:
        print(i)

