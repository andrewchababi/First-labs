#1. Concevez un algorithme qui prend un nombre entier et détermine s'il est divisible par 5.

def divisible_par_5(number):
    if number%5 == 0:
        print("Ce nombre est divisible par 5")
    else:
        print("Ce nombre n'est pas divisible par 5")

#divisible_par_5(10)

#2 Créez un algorithme qui saisit un nombre entier et continue à le demander jusqu'à ce qu'il soit divisible par 5.

"""while True:
    number = int(input("Entrez un nombre entier: "))
    if number % 5 == 0:
        print(f"Le nombre {number} est divisible par 5.")
        break
    else:
        print("Le nombre n'est pas divisible par 5. Veuillez réessayer.")"""

#3/ Imaginons une personne souhaitant acheter un article. Créez un algorithme qui prend le coût de l'article et le solde
#du compte de l'utilisateur pour déterminer si l'utilisateur peut se le permetre ou non.

def enough_money(account, price):
    if account/10 >= price:
        print("you can afford a purchase of "+ str(price))
    else:
        print("You can't afford it")

#enough_money(39940,59)

"""#4/ Concoctez un algorithme qui évalue les performances d'un étudiant en fonc�on de sa note :
- Si la note est ≥ 90 : Affiche "Bon"
- Si la note est entre 50 et 89 : Affiche "Moyen"
- Si la note est ≤ 49 : Affiche "Échec"""

def evaluation(grade):
    if (grade>=90):
        print("Bon")
    elif(grade >= 50 and grade<=89):
        print("Moyen")
    elif(grade >= 0 and grade<=50):
        print("Échec")
    else:
        print("Not valid")

#evaluation(-7)

#Créez un algorithme qui prend deux nombres, les mul�plie, et affiche le résultat uniquement s'il est supérieur à 10.

def bigger_10(num1,num2):
    multiple = num1*num2
    if (multiple>10):
        print(multiple)
    else:
        print("the multiple is not bigger than 10")

#bigger_10(1,3)

#6/ Élaborez un algorithme qui compte le nombre de voyelles dans un mot donné

def trouve_voyelles(word):
    voyelles = ["A","a","O","o","I","i","E","e","U","u"]
    count = 0
    for letter in word:
        if letter in voyelles:
            count+=1
        
    print(count)
        
    
#trouve_voyelles("aorudonekjen")

#7/ Développez un algorithme pour calculer l'énergie ciné�que d'un objet en u�lisant la formule E= 1/2 mv^2.

#9/Formulez un algorithme qui prend deux nombres en�ers et détermine si au moins l'un d'entre eux est pair.

def pair(num):
    if (num%2 != 0):
        return True
    else:
        return False        


def au_moin_un_pair(num1, num2):
    if (pair(num1) == False and pair(num2) == False):
        print("Aucun de c'est nombre sont pair")
    else:
        print("Au moin un de c'est nombre son pair")

#au_moin_un_pair(4,5)

#10/ . Créez un algorithme qui saisit 10 nombres de l'u�lisateur et affiche le plus grand et le plus pe�t des nombres saisis.

def num_sort():
    series = []
    for i in range(10):
        number = int(input("Please add a number to sort. "))
        series.append(number)
    sorted_list = sorted(series)
    print(sorted_list)
    



def meter_to_feet():
    meter = float(input("Please enter the measurment in meters"))
    feet = meter*3.28
    return round(feet,2)




def diviser(numerateur, denominateur):
    somme = 0
    for i in range(len(numerateur)):
        somme += denominateur[0] // numerateur[i]
    return somme


def est_bissextile(annee):
    # On suppose que annee > 0
    if annee % 4 == 0:
        if annee % 100 == 0:
            return False
        elif annee % 400:
            return True
        else:
            return True
    else:
        return False
#print(est_bissextile(1999))
       
        
"INF1010 - Programation 1, LOG1000 - Genie Logiciel, INF1040 - PresentionOral"
        
def extrair_Cour(chaine):
    mot_de_chaine = chaine.split(", ")
    liste_de_cour = []
    for liste in mot_de_chaine:
        if liste.startswith("INF"):
            liste_de_cour.append(liste[:7])
    return liste_de_cour

#print(extrair_Cour("INF1010 - Programation 1, LOG1000 - Genie Logiciel, INF1040 - PresentionOral"))
            


def extraireCours(chaine):
    liste_de_cours = []
    mot = chaine.split(" ")
    print(mot)
    for word in mot:
        if word[:3] == "INF":
            liste_de_cours.append(word)
    return liste_de_cours

#print(extraireCours("INF1010 - Programation 1, LOG1000 - Genie Logiciel, INF1040 - PresentionOral"))

liste = [0,0,0,1,1,1,3,3,3,32,2,2]

def compression(liste):
    i = 0
    resultat = []
    while i< len(liste):
        compteur = 0
        for j in range(i, len(liste)):
            if liste[j] != liste[i]:
                break
            compteur += 1
        resultat.append((liste[i],compteur))
        i += compteur
        
    return resultat
print(compression(liste))
        
        
