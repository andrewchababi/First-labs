# Demande à l'utilisateur de saisir le nombre de secondes
secondes_donner = int(input("Entrez le nombre de secondes: "))
# Calcul du nombre d'années contenant ces secondes (en supposant une année de 365 jours)

nbr_sec_annees = int(60*60*24*365)
annees = secondes_donner //  nbr_sec_annees
sec_rest = secondes_donner%nbr_sec_annees

# Calcul du nombre de semaines restantes dans le reste des secondes
nbr_sec_semaines = int(60*60*24*7)
semaines = sec_rest // nbr_sec_semaines
sec_rest = sec_rest%nbr_sec_semaines

# Calcul du nombre de jours restants dans le reste des secondes
nbr_sec_jour = int(60*60*24)
jours = sec_rest//nbr_sec_jour
sec_rest = sec_rest%nbr_sec_jour

# Calcul du nombre d'heures restantes dans le reste des secondes
nbr_sec_heures = int(60*60)
heures = sec_rest//nbr_sec_heures
sec_rest = sec_rest%nbr_sec_heures

# Calcul du nombre de minutes restantes dans le reste des secondes
nbr_sec_minu = 60
minute = sec_rest//nbr_sec_minu
sec_rest = sec_rest%nbr_sec_minu

# Affichage du nombre d'années, de semaines, de jours, d'heures, de minutes et de secondes

estAnneesNonNull   = annees != 0
estSemainesNonNull = semaines != 0 
estJoursNonNull    = jours != 0 
estHeursNonNull    = heures != 0
estMinutesNonNull  = minute != 0

print(f"En {secondes_donner} secondes, on a: " , end="")

if estAnneesNonNull:
    print(str(annees)+" annees, ", end="")
 
if estSemainesNonNull:  
    print(str(semaines)+" semaines, ", end="")

if estJoursNonNull:
    print(str(jours)+" jours, ", end="")

if estHeursNonNull:
    print(str(heures)+" heures, ", end="")

if estMinutesNonNull:
    print(str(minute)+" minutes ", end="")

print("et "+ str(sec_rest)+" secondes. ")
