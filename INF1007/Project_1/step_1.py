# Définition d'une fonction nommée "estNombreDansIntervalle" qui prend trois paramètres :
    # - min_val : la valeur minimale de l'intervalle
    # - max_val : la valeur maximale de l'intervalle
    # - nombre : le nombre à vérifier s'il est dans l'intervalle

def estNombreDansIntervalle(min_val, max_val, nombre):
    # Vérifier si "min_val" est inférieur ou égal à "nombre"
    # et si "nombre" est inférieur ou égal à "max_val".
    # Cela permet de vérifier si "nombre" se trouve dans l'intervalle [min_val, max_val].

    nombreDansIntervalle = nombre >= min_val and nombre <= max_val

    return nombreDansIntervalle

# Définition d'une fonction nommée "estNombreDansIntervalle" qui prend un paramètre:
    # - nombre : le nombre à vérifier s'il est entier est strictement positive
def estNombrePositifScalaireEntier(nombre):
    # Vérifie si le paramètre 'nombre' est de type int
    # Vérifie si 'nombre' est strictement supérieur à zéro
    
    nombrePositifScalaireEntier = isinstance(nombre, int) and nombre >=0
    
    return nombrePositifScalaireEntier

# Définition d'une fonction pour déterminer si une année est bissextile qui prend un paramètre:
    # - annee : l'année à vérifier si elle est bissextile
def estAnneeBissextile(annee):
    # Utiliser un bloc try_except pour la gestion des erreurs
    try:
    # Vérifie si l'année est un nombre positif, scalaire et entier
        if not estNombrePositifScalaireEntier(annee):
            print("L'annee doit etre un nombre positif, scalaire et entier")
            return False

    # Test pour voir si l'année est bissextile
    # Une année bissextile est soit divisible par 4 mais pas par 100,
    # ou divisible par 400. 
            
        anneeBissextile = ((annee % 4 == 0) and (annee % 100 != 0)) or annee % 400 == 0
            
        
    # En cas d'erreur, afficher l'erreur
       
    except Exception as e:
        print("Erreure : ", e)            
            
        
    return anneeBissextile       


# Fonction pour vérifier si une date est valide qui prend trois paramètres:
    # - jour  : le jour de la date
    # - mois  : le mois de la date
    # - annee : l'année de la date
def estDateValide(jour, mois, annee):
    # Vérifie si jour, mois et année sont tous des nombres entiers positifs
    if estNombrePositifScalaireEntier(jour) and  estNombrePositifScalaireEntier(mois) and  estNombrePositifScalaireEntier(annee):  
        # Vérifie le mois en fonction du nombre de jours qu'il peut avoir
        if mois in [1,3,5,7,8,10,12]:
            # Les mois avec 31 jours
            return estNombreDansIntervalle(1,31, jour)

            # Le mois de février
        elif mois == 2:
            # Si c'est une année bissextile, février a 29 jours
            if estAnneeBissextile(annee):
                return estNombreDansIntervalle(1,29,jour)

            # Sinon, février a 28 jours
            else :
                return estNombreDansIntervalle(1,28,jour)

        # Les mois avec 30 jours
        elif mois in [4,6,9,11]:
            return estNombreDansIntervalle(1,30,jour)

        # Si le mois n'est pas valide (en dehors de la plage 1-12)
        else:
            return False

        # Si l'une des entrées n'est pas un nombre entier positif
    else:
        return False


# Cette fonction vérifie si le jour de la semaine donné en paramètre est valide.
# Elle renvoie True si le jour est l'un des sept jours de la semaine, sinon False.
def estJourValide(jourSemaine):
    # La fonction in permet de vérifier si jourSemaine est présent dans la liste des jours valides.
    # La liste contient les sept noms des jours de la semaine en français.
    # Si jourSemaine est dans cette liste, la fonction renvoie True, sinon elle renvoie False.
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    
    jourValide = jourSemaine in jours
    
    return jourValide


def saisirMois():
    # Liste des noms de mois
    mois_liste = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']

    # Demande à l'utilisateur d'entrer le nom du mois
    choix_de_mois = input("Entrez le nom du mois: ").lower()
    # Recherche la position du mois dans la liste (l'index commence à 0)
    # Si le mois existe dans la liste, renvoie son index, sinon renvoie 0
    for mois in mois_liste:
        if mois == choix_de_mois:
            return mois_liste.index(mois)
         
    return 0
         
         
# Cette fonction permet à l'utilisateur de saisir une date en demandant le jour, le mois et l'année.
def saisirDate():
    # Demande à l'utilisateur de saisir le jour de la date et le convertit en entier.
    jour = int(input("Entrez le jour de la date: "))
    
    # Appelle la fonction saisirMois() pour obtenir le mois de la date.
    mois = saisirMois()
    
    # Demande à l'utilisateur de saisir l'année de la date et la convertit en entier.
    annee = int(input("Entrez l'annee de la date: "))

    # Retourne les trois éléments saisis (jour, mois, année) sous forme de tuple.
    return jour, mois, annee