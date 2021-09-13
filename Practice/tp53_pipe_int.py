from os import *
import traceback
import sys, random

try:
    (rd, wd) = pipe()
    if fork():
        N = random.randint(0, 0xFFFFFFFF)
        print ("sending from", N)
        close(rd)
        write(wd,N.to_bytes(4, sys.byteorder))
        close(wd)
        exit(0)
    else:
        close(wd)
        bN = read(rd, 4)
        N = int.from_bytes(bN, sys.byteorder)
        print ("retriving ...", N)
        close(rd)
        exit(0)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
