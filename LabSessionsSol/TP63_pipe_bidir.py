#! /usr/bin/env python3
#encoding: UTF-8

from os import *
import traceback
import sys,errno, tempfile, random

SIZE = 256

try:
    (rd, wd) = pipe()
    (rd2, wd2) = pipe()
    if fork():
        # père
        if fork():
            close(rd)
            close(wd)
            close(rd2)
            close(wd2)
            wait()
            wait()
            exit(0)
        else:
            # P1
            # send
            close(rd)
            f = open("ff.txt", O_RDONLY)
            r = read(f, SIZE)
            while len(r):
                assert write(wd,r) == len(r)
                r = read(f, SIZE)
            close(wd)
            # recv
            close(wd2)
            r = read(rd2, SIZE)
            while len(r):
                assert write(1,r) == len(r)
                r = read(rd2, SIZE)
            close(rd2)
            exit(0)
    else:
        # P2
        close(rd2)
        f = open("gg.txt", O_RDONLY)
        r = read(f, SIZE)
        while len(r):
            assert write(wd2, r) == len(r)
            r = read(f, SIZE)
        close(wd2)
        # recv
        close(wd)
        r = read(rd, SIZE)
        while len(r):
            assert write(2, r) == len(r)
            r = read(rd, SIZE)
        close(rd)
        exit(0)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)


