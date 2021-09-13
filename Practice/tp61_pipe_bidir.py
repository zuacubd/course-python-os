from os import *
import traceback
import sys

size=256
try:
    (rd, wd) = pipe()
    (rd2, wd2) = pipe()

    if fork():
        if fork():
            close(rd)
            close(wd)
            close(rd2)
            close(wd2)
            wait()
            wait()
            exit(0)
        else:
            #p1 send
            close(rd)
            f = open("gg.txt", O_RDONLY)
            r = read(f, size)
            while len(r):
                assert write(wd, r) == len(r)
                r = read(f, size)
            close(wd)

            #p1 rec
            close(wd2)
            r = read(rd2, size)
            while len(r):
                assert write(1, r) == len(r)
                r = read(rd2, size)
            close(rd2)
            exit(0)
    else:
        #p2 send
        close(rd2)
        f = open("ff.txt", O_RDONLY)
        r = read(f, size)
        while len(r):
            assert write(wd2, r) == len(r)
            r = read(f, size)
        close(wd2)

        #p2 rec
        close(wd)
        r = read(rd, size)
        while len(r):
            assert write(2, r) == len(r)
            r = read(rd, size)
        close(rd)
        exit(0)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
