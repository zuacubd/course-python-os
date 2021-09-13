import os
import traceback
import sys
import mmap
import posix_ipc
import time
import random

try:
    shm = posix_ipc.SharedMemory("/tii", size=os.sysconf("SC_PAGE_SIZE"))
    mm = mmap.mmap(shm.fd, os.sysconf("SC_PAGE_SIZE"), prot=mmap.PROT_READ | mmap.PROT_WRITE)
    print ("size", mm[0])
    print ("contents", [c for c in mm[1:mm[0]+1]])
    mm.close()
    #shm.unlink()

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
