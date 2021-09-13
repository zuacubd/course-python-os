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

def tri_bulle(list, lock):
    if len(list) <= 1:
        return
    temp = 0
    while temp != None:
        temp = None
        for i in range(len(list)-2, -1, -1):
            if  lock:
                lock.acquire()
            # lock[i].acquire()
            if list[i] > list[i+1]:
                # permutation => temp != None
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
            if  lock:
                lock.release()
            # lock[i].release()

def tri_sable(list, lock):
    if len(list) <= 1:
        return True
    temp = 0
    while temp != None:
        temp = None
        for i in range(len(list)-1):
            if  lock:
                lock.acquire()
            # lock[i].acquire()
            if list[i] > list[i+1]:
                # permutation => temp != None
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
            if  lock:
                lock.release()
            # lock[i].release()


# création liste non-ordonnée pour les tests
N = 1000
liste = []
for i in range(N):
    liste.insert(random.randint(0, i), i)
print(liste)

td = time.process_time()

l = threading.Lock()
# l = [threading.Lock() for i in range(N)]
t1 = threading.Thread(target=tri_bulle, kwargs={'list':liste, 'lock':l})
t1.start()
t2 = threading.Thread(target=tri_sable, kwargs={'list':liste, 'lock':l})
t2.start()
t2.join()
t1.join()

te = time.process_time()
print("times:", td, te, te-td)

print(liste)
for i in range(N):
    if i not in liste:
        print (i, " not in liste")




