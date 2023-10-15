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
print(is_doubon(test))


