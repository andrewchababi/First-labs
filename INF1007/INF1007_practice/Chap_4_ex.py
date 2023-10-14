'''# on parle de list et chain de charctere
#on va commence les problemes 

count = 0
chain = ''

for character in chain:
    if character >= 'a' and character <= 'z':
        count += 1 

if count == len(chain) and len(chain)>0:
    print(True)
else:
    print(False)
    
#option 2

result = True
for charac in chain:
    if 'A' <= charac <= 'Z':
        result = False
        break
    
chaine = 'Hello'
start_check = 'He'
for i in range(len(start_check)):
    print()
    #   
    
print(chaine[:len(start_check)] == start_check)

lettres = 'aslkdjfsd'
for i in range(len(lettres)-1):
    if lettres[i] == lettres[i+1]:
        print(f"{lettres[i]} est egal a {lettres[i+1]}")
    else:
        print(f"{lettres[i]} different egal de {lettres[i+1]}")
        

chain = "Andrew"

var = True
i=0 
while i < len(chain) and var :
    if 'a' == chain[i]:
        var = False
    i += 1 

'''


#practice for test 

#1Écrire un programme qui vérifie si le nombre de caractères d’une chaîne de caractères est pair.

def is_len_chaine_paire(chaine):
    return len(chaine) % 2 == 0

#print(is_len_chaine_paire("12345678"))


#2 Écrire un programme qui supprime le 3ème caractère d’une chaîne de caractères.
def suprimer_3eme_char(chain):
    return chain[:2] + chain[3:]

#print(suprimer_3eme_char("12345"))


#3 Écrire un programme qui remplace un caractère d’une chaîne de caractère par un autre. 

def remplacer_char_dans_chaine(chain, a, b):
    return chain.replace(a,b)

#print(remplacer_char_dans_chaine("12345","1","0"))


#4 Écrire un programme qui renvoie le nombre d’occurrences d’un 
# caractère dans une chaîne de caractères, sans utiliser de fonctions
# avancées.

def nomb_occurance(chaine, char):
    return len([occ for occ in chaine if occ == char])

#print(nomb_occurance("hello", "l"))

#5 Écrire un programme qui recherche le nombre de mots dans une phrase donnée.
def nmb_mot_phrase(phrase):
    return len(phrase.split())

#print(nmb_mot_phrase("mon nom est Andrew"))

#without split
def nmb_mot_sans_split(phrase):
    nmb_espace = 0
    for espace in phrase :
        if espace == " ":
            nmb_espace += 1
    return nmb_espace + 1 if phrase else 0 

def nmb_mot_phrase_une_ligne(chaine):
    return  len([space for space in chaine if space == " "]) +1 if chaine else 0 
        
#print(nmb_mot_phrase_une_ligne("mon nom est Andrew"))
