#! /usr/bin/env python3
#encoding: UTF-8

import os,sys,mmap

if len(sys.argv) != 2:
    print("Utilisation: %s fichier"%(sys.argv[0]))
    exit(0)

try:
    stat = os.stat(sys.argv[1])
    f = os.open(sys.argv[1], os.O_RDWR)
    mm = mmap.mmap(f, stat.st_size)
    i = 0
    while i < stat.st_size:
        tmp = mm[i]
        mm[i] = mm[i+1]
        mm[i+1] = tmp
        i += 2

    os.close(f)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)