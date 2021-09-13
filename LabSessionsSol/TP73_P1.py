#! /usr/bin/env python3
#encoding: UTF-8

import os,sys,mmap, posix_ipc, traceback, time, random

try:
    shm = posix_ipc.SharedMemory("/shmTP73", posix_ipc.O_CREAT, size=os.sysconf("SC_PAGE_SIZE"))
    sem = posix_ipc.Semaphore("/semTP73", 0, 0o600, 0)
    mm = mmap.mmap(shm.fd, os.sysconf("SC_PAGE_SIZE"), prot=mmap.PROT_READ | mmap.PROT_WRITE)
    index = 1
    while True:
        x = input('Saisir un nombre entier (ou "end") pour finir :')
        if x=="end":
            break
        else:
            try:
                mm[index] = int(x)
                index += 1
            except ValueError as ve:
                print(ve)
                continue

    mm[0] = (index-1)
    sem.release()
    mm.close()
    shm.close_fd()
    sem.close()
    # shm.unlink()

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)