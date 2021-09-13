#! /usr/bin/env python3
#encoding: UTF-8

from os import *
import traceback
import sys,errno, tempfile, random

try:
    f = open("/tmp/fifo", O_RDONLY)
    while 1:
        bN = read(f,1)
        if len(bN) == 0:
            print("No more data.")
            exit(0)
        N = int.from_bytes(bN, sys.byteorder)
        print ("reçu : ", chr(N))

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)


