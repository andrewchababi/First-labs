#faire un code qui compare deux listes
#en premier par element donc si les elements sont les memes
#deuxieme et de trouver si les elements sont identique

list_1 = [1,2,3,4,5]
list_2 = [2,4,5,6,7]

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
