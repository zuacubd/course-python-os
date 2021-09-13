from os import *
import traceback
import sys

try:
    (rd, wd) = pipe()

    if fork():
        if fork():
            close(rd)
            close(wd)
            wait()
            wait()
            exit(0)
        else:
            close(rd)
            dup2(wd, 1)
            close(wd)
            execlp("ls","ls","-l")
    else:
        close(wd)
        dup2(rd,0)
        close(rd)
        execlp("grep","grep","e\\.py")
        exit(0)

except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit(1)
