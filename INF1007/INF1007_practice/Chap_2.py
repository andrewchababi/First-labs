

def majuscule_minuscule(lettre):
    if 65 <= ord(lettre) <= 90:
        lettre = chr(ord(lettre) + 32)
        return lettre
    elif 97 <= ord(lettre) <= 122: 
        lettre = chr(ord(lettre) - 32)
        return lettre
    else: 
        return "n'est pas une lettre valable"
    
'''x = y = None
if x is None:
    x = 5
if y is not None:
    x = 7
print(x)'''

'''x = 11
y = 2
z = x // y
zz = z / y
print(z, zz)'''

'''x = 5 < 5
print(x)
print(not x)'''