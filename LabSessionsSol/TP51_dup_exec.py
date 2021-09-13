#! /usr/bin/env python3
#encoding: UTF-8

from os import *
import traceback

try:
    f=open("f.txt", O_WRONLY | O_CREAT, 0o644)
    dup2(f,1)
    execl("/bin/ls", "ls", "-l")

except OSError as e:
    traceback.print_exc()
    print(e.strerror)
    exit(1)


