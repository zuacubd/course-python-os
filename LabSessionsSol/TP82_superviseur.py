# encoding: UTF-8

import threading, random, time, sys, numpy, os

lock = threading.Lock()

# pour Q1
# liste est la matrice
# num est le numero du thread
# num represente la ligne de la matrice remplie par le thread sur les indices de colonnes de i=0 a i=9
def capteur(matrice, num):
    global lock
    i = 0
    print(num)

    while 1:
        temperature = random.randint(0, 32)
        lock.acquire()
        matrice[num][i%10] = temperature
        lock.release()
        time.sleep(1)
        i = i + 1


# pour Q2
def stat_capteur(matrice, num):
    global lock
    while 1:
        lock.acquire()
        copie = numpy.copy(matrice[nb, :])
        lock.release()
        maximumC = numpy.amax(copie)
        print("stat ", num, ":", maximumC)
        time.sleep(10)


# pour Q3
fd = os.open("stats_globales.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
# os.dup2(fd, 1)

# main de Q1
N = sys.argv[1]  # nb de capteurs
matrice = numpy.zeros((int(N), 10))
# matrice[0,0] = random.randint(0,32)
print(matrice)

for nb in range(int(N)):
    t = threading.Thread(target=capteur, kwargs={'matrice': matrice, 'num': nb})
    t.start()

for nb in range(int(N)):
    # copie = numpy.copy(matrice[nb, :])
    t = threading.Thread(target=stat_capteur, kwargs={'matrice': matrice, 'num': nb})
    t.start()

while 1:
    lock.acquire()
    copie = numpy.copy(matrice)
    lock.release()
    maximumC = numpy.amax(copie)
    print("Maximum : ", maximumC)
    time.sleep(10)

# attente des threads "capteurs" par le superviseur qui est le thread principal
# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     print('joining', t.getName())
#     t.join()
#
# print(matrice)

# max par capteur
# maxs = []
# for c in range(int(N)):
#     print(matrice[c, :])
#     maxC = numpy.amax(matrice[c, :])
#     print(maxC)
#     maxs.append(maxC)

# max
# maximum = numpy.amax(matrice)
# print(maximum)

# suite main pour Q2
# creation des threads de stats
# for nb in range(int(N)):
#     # copie = numpy.copy(matrice[nb, :])
#     t = threading.Thread(target=stat_capteur, kwargs={'liste': matrice, 'num': nb})
#     t.start()
#
# # attente des threads "stat_capteurs" par le superviseur qui est le thread principal
# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     print('joining ', t.getName())
#     t.join()
#
# print("fin")
