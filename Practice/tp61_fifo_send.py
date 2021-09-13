from os import *
import traceback
import sys, random, time

try:

    f = open("tmp", O_WRONLY)
    while 1:
        N = random.randint(32, 99)
        print ("env:", N)
        write(f,N.to_bytes(1,sys.byteorder))
        time.sleep(1)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
