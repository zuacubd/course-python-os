# encoding: UTF-8

import random, time, sys, numpy, os, mmap, posix_ipc, traceback, signal

# version complete Q2
pid = []


# modif du comportement de signal
def arret(signal, frame):
    global pid
    # on tue les fils créés
    try:
        pids = 0
        while pids < len(pid):
            print(pid[pids])
            os.kill(pid[pids], signal.SIGINT)
            pids = pids + 1
    except:
        # si fils deja mort on ne traite pas exception
        pass

        # le pere desalloue les ress partagees
    mm.close()
    shm.unlink()
    print("fin")
    sys.exit(0)


try:
    shm = posix_ipc.SharedMemory("/sup", posix_ipc.O_CREAT, size=os.sysconf("SC_PAGE_SIZE"))
    # sem = posix_ipc.Semaphore("/semTemp", posix_ipc.O_CREAT, 0o600, 1)

    mm = mmap.mmap(shm.fd, os.sysconf("SC_PAGE_SIZE"), prot=mmap.PROT_READ | mmap.PROT_WRITE)

    N = sys.argv[1]  # nb de capteurs
    p = 1

    # lancement des fils
    # nb est une variable heritee nous servant a savoir dans quelle partie de matrice le capteur ecrit


    for nb in range(int(N)):
        # print("nb "+ str(nb))
        if (p > 0):
            p = os.fork()
            pid.append(p)
            # les fils ont un comportement de capteur
            if (p == 0):
                print("fils de pid avec nb : " + str(os.getpid()) + " " + str(nb))
                i = 0
                while (i < 10):
                    # temperature = random.randint(0,32)
                    # print ("pid "+ str(os.getpid())+ str(temperature))
                    mm[nb * 10 + i] = random.randint(0, 32 * (nb + 1))
                    time.sleep(1)
                    i = i + 1
                print("fin fils")
    if (p > 0):
        # mise en place du handler pour le pere
        signal.signal(signal.SIGINT, arret)
        # le pere attend ses fils
        for pid in range(int(N)):
            os.wait()
            # le pere calcule le max de la temp
        print("affichage par pere des valeurs")
        for t in range(0, int(N) * 10):
            print(mm[t])
        maximum = numpy.amax(mm)
        print(maximum)

        # le pere desalloue les ress partagees
        mm.close()
        shm.unlink()

        # test signal en bouclant
        print("Le programme va boucler...")
        print(pid)
        while True:
            continue


except OSError as e:
    traceback.print_exc()
    print(e.strerror)
    exit(1)
