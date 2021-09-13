#! /usr/bin/env python3
#encoding: UTF-8

import threading, random, time

# Exemple lancement de thread
#  def f(x, y):
#     # fonction à exécuter sur un thread à part
#     # ...
#     pass
#
# # création du thread
# th = threading.Thread(target=f, kwargs={'x' : valeur1, 'y' : valeur2})
# # démarrage du thread
# th.start()
# # attente de la fin du thread
# th.join()

def tri_bulle(list):
    if len(list) <= 1:
        return
    temp = 0
    while temp != None:
        temp = None
        for i in range(len(list)-2, -1, -1):
            if list[i] > list[i+1]:
                # permutation => temp != None
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

def tri_sable(list):
    ...

# création liste non-ordonnée pour les tests
N = 1000
liste = []
for i in range(N):
    liste.insert(random.randint(0, i), i)
print(liste)

# tri
tri_bulle(liste)
print(liste)

