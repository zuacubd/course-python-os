#! /usr/bin/env python3
#encoding: UTF-8

import os,sys,mmap, posix_ipc, traceback, time

try:
    shm = posix_ipc.SharedMemory("/tii", size=os.sysconf("SC_PAGE_SIZE"))
    mm = mmap.mmap(shm.fd, os.sysconf("SC_PAGE_SIZE"), prot=mmap.PROT_READ | mmap.PROT_WRITE)
    print("taille:",mm[0])
    print("contenu:", [c for c in mm[1:mm[0]+1]])
    mm.close()

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)