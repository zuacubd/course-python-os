import os
import traceback
import sys
import mmap
import posix_ipc
import time
import random

try:
    shm = posix_ipc.SharedMemory("/shm73", size=os.sysconf("SC_PAGE_SIZE"))
    sem = posix_ipc.Semaphore("/semTP73", posix_ipc.O_CREAT, 0o600, 0)
    mm = mmap.mmap(shm.fd, os.sysconf("SC_PAGE_SIZE"), prot=mmap.PROT_READ | mmap.PROT_WRITE)
    sem.acquire()
    print ("size", mm[0])
    print ("contents", [c for c in mm[1:mm[0]+1]])
    mm.close()
    sem.unlink()
    shm.unlink()

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
