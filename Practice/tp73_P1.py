import os
import traceback
import sys
import mmap
import posix_ipc
import time
import random

try:
    shm = posix_ipc.SharedMemory("/shm73", posix_ipc.O_CREAT, size=os.sysconf("SC_PAGE_SIZE"))
    sem = posix_ipc.Semaphore("/semTP73", 0, 0o600, 0)
    mm = mmap.mmap(shm.fd, os.sysconf("SC_PAGE_SIZE"), prot=mmap.PROT_READ | mmap.PROT_WRITE)
    index = 1
    while 1:
        x = input("enter a number")
        if x == "end":
            break
        else:
            try:
                mm[index] = int(x)
                index = index + 1
            except ValueError as ve:
                print(ve)
                continue
    mm[0]= (index-1)
    sem.release()
    mm.close()
    shm.close_fd()
    sem.close()

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
