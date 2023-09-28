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
            return mois_liste.index(mois) + 1
         
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



# Définition d'une fonction pour saisir une date valide
def saisirDateValide():
    # Appelle la fonction saisirDate() pour obtenir une date sous forme de jour, mois et année
    jour , mois, annee = saisirDate()

    # Tant que la date n'est pas valide selon la fonction estDateValide(),
    # continuer à demander à l'utilisateur de saisir une date valide
    while not estDateValide(jour,mois,annee):
        # Affiche un message indiquant que la date n'est pas valide
        print("Vous n'avez pas entre une date valide.")
        
        # Demande à l'utilisateur de saisir une nouvelle date
        jour , mois, annee = saisirDate() 

    # Une fois que l'utilisateur a saisi une date valide, retourne cette date
    return jour, mois, annee




# Définition d'une fonction pour convertir un numéro en jour de la semaine en utilisant différents algorithmes.
def conversionJourSemaine(numero, algorithme):
    #utiliser un try_except pour la gestion des erreurs
    try:
        # Liste des noms des jours de la semaine
        jours_semaine = ['samedi', 'dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']

        # Vérification si le numéro est dans l'intervalle valide (0 à 6 inclus).
        if numero >= 0 and numero <= 6:
            # Choix de l'algorithme de conversion en fonction de l'argument 'algorithme'.
            if algorithme == "zeller":
            # Pour l'algorithme de Zeller, le numéro reste inchangé.
                pass
            # Pour l'algorithme de Schwerdtfeger, on ajuste le numéro en utilisant modulo 7.
            elif algorithme == "schwerdtfeger":
                numero = (numero + 1) % 7
            
            # Si l'algorithme choisi n'est pas reconnu, une exception est levée.
            else:
                print("L'algorithme choisi n'est pas valide.")

            # Récupérer le nom du jour de la semaine à partir de la liste
            jours_semaine = jours_semaine[numero]

            # Renvoyer le jour de la semaine calculé.
            return jours_semaine
        
        # Si le numéro n'est pas dans l'intervalle valide, une exception est levée.
        else:
            raise Exception("Le numero entre n'est pas valide.")

    # Gestion des exceptions en affichant un message d'erreur.
    except Exception as e:
        print(e)


# Définition d'une fonction appelée partieAnnuelleAnnee prenant une année en entrée.
def partieAnnuelleAnnee(annee):
    #utiliser un try_except pour la gestion des erreurs
    try:
        # Vérifie si l'année n'est pas un nombre positif scalaire entier.
        estNombrePositifScalaireEntier()
            # Si ce n'est pas le cas, lève une exception ValueError avec un message explicatif.
        if not estNombrePositifScalaireEntier():
            raise Exception("L'argument doit etre un nombre positif, scalaire et entier")
        # Calcule le reste de la division de l'année par 100.
        return annee % 100
    
    # En cas d'exception ValueError, affiche le message d'erreur.
    except Exception as e:
        print(e)
        

# Cette fonction prend en entrée une année et retourne la partie séculaire de cette année en divisant par 100.
def partieSeculaireAnnee(annee):
    #utiliser un try_except pour la gestion des erreurs
    try:
        # Vérifie si l'année est un nombre positif, scalaire (entier).
        if not estNombrePositifScalaireEntier(annee):
            raise Exception("L'annee doit etre un nombre positif, scalaire et entier")
        # Divise l'année par 100 pour obtenir la partie séculaire.
        return (annee // 100)
    # En cas d'exception ValueError, affiche le message d'erreur..
    except Exception as e:
        print(e)
        
print(partieSeculaireAnnee(-2009))

