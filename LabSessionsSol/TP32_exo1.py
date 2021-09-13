#correction exo1 TP intro python
#python3

from os import *
import sys

#test recup 1 parametre
if len(sys.argv) != 2:
	print("Utilisation: %s fichier"%(sys.argv[0]))
	exit(0)

#affichage chaine recue
print(sys.argv[1])

#saisie chaine 2
chaine2 = input('Entrer une chaine')

#concatenation
chaineConcat = sys.argv[1] + chaine2

#affichage chaine concatenee
print(chaineConcat)

#affichage longeur 
print(len(chaineConcat))

mots = chaineConcat.split()
for i in range (len(mots)-1):
	print(mots[i] + " & ", end='') # print sans retour a la ligne avec Python 3
print(mots[len(mots)-1])
