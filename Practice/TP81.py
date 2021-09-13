#! /usr/bin/env python3
#encoding: UTF-8

import threading, random, time

# Exemple lancement de thread
#  def f(x, y):
#     # fonction à exécuter sur un thread à part
#     # ...
#     pass
#
def tri_bulle(list, lock):
    if len(list) <= 1:
        return
    temp = 0
    while temp != None:
        temp = None
        for i in range(len(list)-2, -1, -1):
            if lock:
                lock.acquire()
            if list[i] > list[i+1]:
                # permutation => temp != None
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
            if lock:
                lock.release()

def tri_sable(list, lock):
    if len(list) <= 1:
        return
    temp = 0
    while temp != None:
        temp = None
        for i in range(len(list)-1):

            if lock:
                lock.acquire()

            if list[i] > list[i+1]:
                # permutation => temp != None
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
            if lock:
                lock.release()

# création liste non-ordonnée pour les tests
N = 1000
liste = []
for i in range(N):
    liste.insert(random.randint(0, i), i)
print(liste)

# tri
td = time.process_time()
#tri_bulle(liste)

l = threading.Lock()

# # création du thread
th1 = threading.Thread(target=tri_bulle, kwargs={'list':liste, 'lock':l})
# # démarrage du thread
th1.start()
# # attente de la fin du thread
#th1.join()
#print("times:", td, te, te-td)
# # création du thread
th2 = threading.Thread(target=tri_sable, kwargs={'list':liste, 'lock':l})
# # démarrage du thread
th2.start()
# # attente de la fin du thread
th2.join()
th1.join()

#
te = time.process_time()
print("times:", td, te, te-td)


print(liste)
for i in range(N):
    if i not in liste:
        print (i, "not in list")
