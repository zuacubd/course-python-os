#! /usr/bin/env python3
#encoding: UTF-8

from os import *
import traceback
import sys, tempfile



try:
    f = tempfile.TemporaryFile()
    oldstderr = dup(sys.stderr.fileno())
    dup2(f.fileno(),sys.stderr.fileno())
    traceback.print_stack()
    dup2(oldstderr,sys.stderr.fileno())
    f.seek(0)
    # or : lseek(f.fileno(), 0, SEEK_SET)
    x = f.readlines()
    print(x)
    f.close()

except OSError as e:
    traceback.print_exc()
    print(e.strerror)
    exit(1)


