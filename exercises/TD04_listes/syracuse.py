# n = 3
# 3 est impair donc n*3 +1 = 3*3+1 = 9+1 = 10
# n  10 pair donc n//2 = 10 // 2 = 5
# n = 5 impair donc n*3+1 = 5*3 + 1 = 15 + 1 = 16
# etc...


def syracuse(n):
    """ Retourne la liste de valeurs de la suite en partant de n jusqu'à 1"""

    liste = []
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n//2
            liste.append(n)
        else:
            n = (n*3) + 1
            liste.append(n)
    return liste


# print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, (n_max+1)):
        syracuse(i)
    return (i)

# testeConjecture(1000)

# On appelle temps de vol de l’entier n le nombre d’étapes pour aller de n
# jusqu’à 1. Le temps de vol de 1 est 0, le temps de vol de 3 est 7.
# Écrire une fonction qui, étant donné un paramètre n, renvoie
#  son temps de vol.


def tempsVol(n):
    """ Retourne le temps de vol de n """
    a = (len((syracuse(n))))
    return a

# print("Le temps de vol de", 1, "est", tempsVol(1))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1, n_max)]
     

# print(tempsVolListe(100))

l = tempsVolListe(10000)
max = l[0]
indiceMax = 0
for i in range(len(l)):
    if l[i] > max:
        max = l[i]
        indiceMax = i
print(indiceMax+1,"a le plus grand temps de vol :", max)
