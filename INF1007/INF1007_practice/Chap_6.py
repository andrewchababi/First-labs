#faire un code qui compare deux listes
#en premier par element donc si les elements sont les memes
#deuxieme et de trouver si les elements sont identique

list_1 = [1,2,3,4,5]
list_2 = [1,2,3,4,5]
"""
#1
if len(list_1)== len(list_2):
    resulta = True
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            resulta = False
            break
else:
    resulta = False
print(resulta)      
    

#2
if len(list_1)== len(list_2):
    resulta = True
    for i in range(len(list_1)):
        if id(list_1[i]) != id(list_2[i]):
            resulta = False
            break
else:
    resulta = False


ma_list = list(range(10))
#print(ma_list)

nouvelle_list = []
for element in ma_list:
    nouvelle_list.append(element*2)
#print(nouvelle_list)

#instead of all that what we could do is:

nouvelle_list = [element*2 for element in ma_list]
#print(nouvelle_list)

mon_dictionaire = {"a":1, "b":2, "c":3}

list_a = []
for key in mon_dictionaire:
    list_a.append((key, mon_dictionaire[key]))
#print(list_a)

list_a = [(key, mon_dictionaire[key]) for key in mon_dictionaire] 
#print(list_a)

#this doesn't really work you almost got it but when not using a dictionary yoou can only be so efficient
#in terms of addressing a large amount of data at once because you have to start accounting for every 
#case yourself

open_bracket_stack = []
text = "[({)]}["

open_bracket_stack = []
for character in text:
    if character in ["(","{","["]:
        open_bracket_stack.append(character)
        print(open_bracket_stack)

    elif character in [")","]","}"]:
        if len(open_bracket_stack) != 0:
            res = open_bracket_stack.pop()
            
            print(open_bracket_stack)
        else:
            print("false")
            break

    else: 
        print("all good")


"""

def is_list_ordered():
    liste = []
    for _ in range(10):
        num = int(input("input 10 numbers"))
        liste.append(num)
    
    sorted_list = sorted(liste)
    
    return liste == sorted_list

#print(is_list_ordered())

test = [1,2,2,3]

def is_doubon(liste):
    return len(liste) != len(set(liste))
#print(is_doubon(test))


# Écrire un programme qui calcule la moyenne des notes rentrées
# dans un dictionnaire ayant pour clés le nom des étudiants. Par la
# suite, le programme doit retourner le nom de l’étudiant ayant la
# meilleure note, dans la même structure de données.

notes_etudiants = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92,
}

moyen = sum(notes_etudiants.values())/ len(notes_etudiants)

highest_note = None
nom = None

for name , note in notes_etudiants.items():
    if highest_note is None or note > highest_note:
        highest_note = note
        nom = name
    
#print(highest_note, nom)



liste_initiale = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_pair = [num if num%2 == 0 else 0 for num in liste_initiale]

liste_initiale = [[0, 'a'], [2, 'b'], [3, 'c']]
nouvelle_liste = []
for i in liste_initiale :
    for n in i :
        nouvelle_liste.append(n*2)

nouvelle_liste = [n*2 for i in liste_initiale for n in i]

#print(nouvelle_liste)


phrase = "sdlfkjwaeoijfdlsakjfosiasjldkhjfa;lsdjfaosijenoa[o8ifhseh]"

hist = {}
for char in phrase:
    if char in hist:
        hist[char] += 1
    else:
        hist[char] = 1

print(hist)

hist = {char: phrase.count(char) for char in phrase}

print(hist)