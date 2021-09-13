from os import *
import traceback
import sys, random

try:
    f = open("tmp", O_RDONLY)
    while 1:
        bN = read(f,1)
        if len(bN) == 0:
            print ("No more data")
            exit(0)
        N = int.from_bytes(bN, sys.byteorder)
        print ("recu :", chr(N))

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
