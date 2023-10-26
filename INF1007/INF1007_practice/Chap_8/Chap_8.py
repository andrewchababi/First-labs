


'''
nom_fichier1 = 'fichier_1.txt'
nom_fichier2 = 'fichier_2.txt'


with open(nom_fichier1, mode= 'r') as f1, open(nom_fichier2, mode='r') as f2:

    while True:
        c1 = f1.read(1)
        c2 = f2.read(1)
        if c1 != c2:
            print(c1,c2, f1.tell())
            break
        if c1 == '' and c2 == '':
            print("end")
            break

f1.close()
f2.close()
'''
#2
"""
with open('fichier_2.txt', mode='r') as f:
    noms_columns = f.readline().split(',')
    donnees = {nom : [] for nom in noms_columns}
    for ligne in f:
        d = ligne.split(",")
        donnees['Jour'].append(d[0])
        donnees['Precip'].append(d[1])
        donnees['Temp'].append(d[2])   
        donnees['Vent\n'].append(d[3])     
print(donnees)
"""    

import csv

with open('fichier_2.csv', mode='r') as f:
    noms_colonnes = f.readline().split(',')
    donnees = {nom.strip("\n"): [] for nom in noms_colonnes}
    print(donnees)
    for ligne in f:
        d  = ligne.split(',')
        donnees['Jour'].append(d[0])
        donnees['Precip'].append(d[1])
        donnees['Temp'].append(d[2])   
        donnees['Vent'].append(d[3].strip("\n"))

print(donnees)        


donee = ["Bonjour",1,2,(3,4,5 )]

import json

import pickle
couleurs = {"lion": " jaune", " chat": " noir"}
pickle.dump(couleurs, open("sauvegarde.p", "wb"))


import pickle
couleurs = pickle.load(open("sauvegarde.p", "rb"))

print(type(donee), donee)