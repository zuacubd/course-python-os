#! /usr/bin/env python3
#encoding: UTF-8

import threading, random, time, sys, numpy, os

# Exemple lancement de thread
#  def f(x, y):
#     # fonction à exécuter sur un thread à part
#     # ...
#     pass
#

lock = threading.Lock()

def capteur(matrice, num):
    global lock
    i = 0
    print (num)

    while 1:
        temperature = random.randint(0, 32)
        lock.acquire()
        matrice[num][i%10] = temperature
        lock.release()
        time.sleep(1)
        i = i + 1

def stat_capteur(matrice, num):
    global lock
    while 1:
        lock.acquire()
        copie = numpy.copy(matrice[num, :])
        lock.release()
        maximumC = numpy.amax(copie)
        print("stat ", num, ":", maximumC)
        time.sleep(10)


# création liste non-ordonnée pour les tests
N = sys.argv[1]
matrice = numpy.zeros((int(N),10))
print(matrice)

#Q1
#for nb in range(int(N)):
#    t = threading.Thread(target=capteur, kwargs={'matrice': matrice, 'num': nb})
#    t.start()
#
#
#main_thread = threading.currentThread()
#for t in threading.enumerate():
#    if t is main_thread:
#        continue
#    print ('joining', t.getName())
#    t.join()
#
#print (matrice)


#Q2
#for nb in range(int(N)):
#    t = threading.Thread(target=capteur, kwargs={'matrice': matrice, 'num': nb})
#    t.start()
#
#for nb in range(int(N)):
#    t = threading.Thread(target=stat_capteur, kwargs={'matrice': matrice, 'num': nb})
#    t.start()
#    #time.sleep(30)
#
#main_thread = threading.currentThread()
#for t in threading.enumerate():
#    if t is main_thread:
#        continue
#    print ('joining', t.getName())
#    t.join()

#print (matrice)

#Q3
fd = os.open("stats_globales.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
os.dup2(fd, 1)

for nb in range(int(N)):
    t = threading.Thread(target=capteur, kwargs={'matrice': matrice, 'num': nb})
    t.start()

for nb in range(int(N)):
    t = threading.Thread(target=stat_capteur, kwargs={'matrice': matrice, 'num': nb})
    t.start()
    #time.sleep(30)

while 1:
    lock.acquire()
    copie = numpy.copy(matrice)
    lock.release()
    maximumC = numpy.amax(copie)
    print ('Maximum', maximumC)
    time.sleep(10)

