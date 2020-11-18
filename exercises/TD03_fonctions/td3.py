# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme
     jour, heure, minute, seconde."""
    secondes = temps[0] * 86400
    secondes += temps[1] * 3600
    secondes += temps[2] * 60
    secondes += temps[3] * 1
    return secondes


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond
    au nombre de seconde passé en argument"""
    jours = seconde // 86400
    reste = seconde % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    return (jours, heures, minutes, reste)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes",
                temps[3], "secondes")


def affichePluriel(mot: str, nombre: int):
    """ Affiche ou non un mot en fonction d'un paramètre.
        Met le mot au pluriel s'il le faut"""
    if nombre > 0:
        print(" ", nombre, mot, end="")

    if nombre > 1:
        print("s", end="")


def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])


# afficheTemps((1,0,14,23))


def demandeTemps():
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1

    while (jours < 0):
        jours = int(input("Entrez un nombre de jours"))

    while (heures < 0 or heures >= 24):
        heures = int(input("Entrez un nombre d'heures"))

    while (minutes < 0 or minutes >= 60):
        minutes = int(input("Entrez un nombre de minutes"))

    while (secondes < 0 or secondes >= 60):
        secondes = int(input("Entrez un nombre de secondes"))

    return (jours, heures, minutes, secondes)


# afficheTemps(demandeTemps())

def sommeTemps(temps1: tuple, temps2: tuple) -> tuple:
    """ fonction qui additionne deux tuples de temps"""
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

# afficheTemps(sommeTemps((2,3,4,25), (5,22,57,1)))


def proportionTemps(temps: tuple, proportion: float) -> tuple:
    """ Fonction qui retourne une proportion du temps"""
    nouveau_temps = proportion * tempsEnSeconde(temps)
    secondeEnTemps(nouveau_temps)

    return secondeEnTemps(nouveau_temps)

# afficheTemps(proportionTemps((2,0,36,0),0.2))
# afficheTemps(proportionTemps(proportion=0.2, temps=(2, 0, 36, 0)))


def tempsEnDate(temps: tuple) -> tuple:
    annees = temps[0] // 365
    jours = temps[0] % 365
    return (1970=annees, 1 + jours, temps[1], temps[2], temps[3])

# afficheDate(date: tuple = ()) :  Cela signifie que la fonction
# prend en paramètre date de type tuple. Ce paramètre peut être
# omis et dans ce cas il prendra la valeur par défaut () qui est
# un tuple vide.


def afficheDate(date: tuple = ()):
    """ Affiche la date passée en paramètre. Si aucune date
        n'est passée, affiche la date du jour. """
    if len(date) == 0:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("Annee", date[0], "jour", date[1], str(date[2]) + ":" + str(date[3])
                            + ":" + str(date[4]))
    ))

# temps = secondeEnTemps(86401)
# afficheTemps(temps)
# afficheDate(tempsEnDate(temps))
# afficheDate()

# print(time.time())
# afficheDate()

def bissextile(jour):
    annee = 1970
    while (jour >= 365):
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            print("L'année" + str(annee) + "est bissextile")
            jour -= 366
        else:
            jour -= 365
        annee += 1

# bissextile(20000)

def nombreBissextile(jour: int) -> int:
    annee = 1970
    compteur_bissextile = 0
    while (jour >= 365):
        if (annee % 4 == 0) and (annee % 100 != 0 or annee % 400 == 0):
            compteur_bissextile += 1
            jour -= 366
        else:
            jour -= 365
        annee += 1
    return compteur_bissextile

def tempsEnDateBissextile(temps):
    jour, heure, minute, seconde = temps
    jour = jour -nombreBissextile(jour)
    temps_ajuste = (jour, heure, minute, seconde)
    return tempsEnDate(temps_ajuste)

    afficheDate(tempsEnDateBissextile(secondeEnTemps(int(time.time()))))