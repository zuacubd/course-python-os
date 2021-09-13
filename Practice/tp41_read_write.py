from os import *
import traceback
import sys

if len(sys.argv) !=2:
    print ("Usage: %s" % sys.argv[0])
    quit(0)

SIZE=256

try:
    f = open(sys.argv[1], O_RDONLY)
    bs = read(f, SIZE)
    while len(bs)>0:
        write(sys.stdout.fileno(), bs)
        bs = read(f, SIZE)
    close(f)
except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit()
