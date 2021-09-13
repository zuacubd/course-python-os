#! /usr/bin/env python3
# #encoding: UTF-8

from os import *
import traceback
import sys,errno

if len(sys.argv) != 2:
    print ("Utilisation: %s fichier"%(sys.argv[0]))
    exit(0)

try:
    try:
        unlink(sys.argv[1]+"~")
    except OSError as e:
        if e.errno == errno.ENOENT:
            pass
        else:
            raise
    rights = stat(sys.argv[1]).st_mode & 0o777 # anciens droits, pour re-créer avec les mêmes
    link(sys.argv[1],sys.argv[1]+"~")
    unlink(sys.argv[1])
    fmod=open(sys.argv[1], O_WRONLY | O_CREAT, rights)
    f=open(sys.argv[1]+"~", O_RDONLY)

    bs = read(f, 1)
    debut = True
    while len(bs) > 0:
        if chr(bs[0]) != " ":   # en python3 bs[0] est de type byte, conversion avec chr()
            debut = False
        if not debut:
            write(fmod, bs)
        if chr(bs[0]) == "\n":
            debut = True
        bs = read(f,1)
    close(f)
    close(fmod)

except OSError as e:
    traceback.print_exc()
    print(e.strerror)
    exit(1)


