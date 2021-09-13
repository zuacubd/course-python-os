from os import *
import traceback
import sys, tempfile

try:
    f = tempfile.TemporaryFile()
    oldstderr = dup(sys.stderr.fileno())
    dup2(f.fileno(), sys.stderr.fileno())
    traceback.print_stack()
    dup2(oldstderr,sys.stderr.fileno())
    f.seek(0)
    x=f.readlines()
    print(x)
    #for line in f.readline():
    #    print(line)
    f.close()

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
