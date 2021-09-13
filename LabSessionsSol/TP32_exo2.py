#correction exo1 TP intro python
#python3

from os import *
import sys, random

#ss pg testant si val sont > a seuil et renvoie une liste contenant les éléments supérieurs
def parcoursL (ListVal, seuil):
	listS = []
	i = 0
	while i < len(ListVal):
		if ListVal[i] > seuil:
			listS.append(ListVal[i])
		i = i + 1 
	return listS

#remplissage d'une liste
nbVal = input('Donnez le nb de valeurs à remplir ')

liste = []
#input renvoie une chaine
for i in range(int(nbVal)):
	liste.append(random.randint(0,32))

print(liste) #[6, 13, 25, 7, 18]

#test du seuil
S = input('Donnez le seuil ')

ListeR = parcoursL(liste, int(S))

print(ListeR)

#test syntaxe slices
print (liste[0:5]) #[6, 13, 25, 7, 18]
print (liste[0:]) #[6, 13, 25, 7, 18]
print ( liste[:len(liste)]) #[6, 13, 25, 7, 18]
print ( liste[1:2]) #[13]
print ( liste[-1:-1]) #[]
print ( liste[0:-1]) #[6, 13, 25, 7]
print ( liste[-1:]) #[18]

#Manip de liste en menu
print ("saisir Q pour arreter")
print ("Menu : A(append), I(insert), R(remove), P(pop), C(count), S(sort)")
#- append() ajoute un élément en fin de liste.
#- remove() enlève la première occurrence de la valeur.
#- pop() enlève la valeur à l’index donnée et renvoie cette valeur.
#- extend() ajoute une liste en fin de liste.
#- index() renvoie le premier index de la valeur donnée.
#- count() renvoie le nombre de valeurs égales à la valeur donnée.
#- sort() modifie la liste en la triant.
#- La fonction sorted() renvoie une liste triée sans modifier la liste initiale.
#- reverse() renvoie la liste à l’envers.
#- La fonction len() renvoie la longueur de la liste.

choix = input('Choix ?')
while (choix != "Q"):
	if (choix == "A"):
		val = input('Donnez la valeur ')
		liste.append(int(val))
		print(liste)
	elif (choix == "I"):
		ind = input('Donnez l indice ')
		val = input('Donnez la valeur ')
		liste.insert(int(ind),(int(val)))
		print(liste)
	elif (choix == "R"):
		val = input('Donnez la valeur ')
		liste.remove(int(val))
		print(liste)
	elif (choix == "P"):
		ind = input('Donnez l indice ')
		valSuppr = liste.pop(int(ind))
		print(valSuppr)
		print(liste)
	elif (choix == "S"):
		liste.sort()
		print(liste)
	choix = input('Choix ?')

































