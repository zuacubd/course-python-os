#! /usr/bin/env python3
#encoding: UTF-8

from os import *
import traceback
import sys,errno, tempfile, random, time

try:
    f = open("/tmp/fifo", O_WRONLY)
    while 1:
        N = random.randint(32,99)
        print ("envoi de : ", N)
        write(f,N.to_bytes(1, sys.byteorder))
        time.sleep(1)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)


