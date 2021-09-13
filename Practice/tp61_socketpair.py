from os import *
import traceback
import socket

size=256
try:
    (s1, s2) = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)
    ns1 = s1.fileno()
    ns2 = s2.fileno()

    if fork():
        if fork():
            close(ns1)
            close(ns2)
            wait()
            wait()
            exit(0)
        else:
            #p1 send
            close(ns2)
            f = open("ff.txt", O_RDONLY)
            r = read(f, size)
            while len(r):
                assert write(ns1, r) == len(r)
                r = read(f, size)
            close(f)

            #p1 rec
            r = read(ns1, size)
            while len(r):
                assert write(1, r) == len(r)
                r = read(ns1, size)
            close(ns1)
            exit(0)
    else:
        #p2 send
        close(ns1)
        f = open("gg.txt", O_RDONLY)
        r = read(f, size)
        while len(r):
            assert write(ns2, r) == len(r)
            r = read(f, size)
        close(f)

        #p2 rec
        r = read(ns2, size)
        while len(r):
            assert write(2, r) == len(r)
            r = read(ns2, size)
        close(ns2)
        exit(0)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
