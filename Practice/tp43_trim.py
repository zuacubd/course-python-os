from os import *
import traceback
import sys,errno

if len(sys.argv) !=2:
    print ("Usage: %s" % sys.argv[0])
    quit(0)

try:
    try:
        unlink(sys.argv[1]+"~")
    except OSError as e:
        if e.errno == errno.ENOENT:
            pass
        else:
            raise

    rights = stat(sys.argv[1]).st_mode & 0o777
    link(sys.argv[1], sys.argv[1]+"~")
    unlink(sys.argv[1])

    fw = open(sys.argv[1], O_WRONLY | O_CREAT | O_TRUNC, rights)
    f = open(sys.argv[1]+"~", O_RDONLY)

    bs = read(f, 1)
    flag = True
    while len(bs)>0:
        if chr(bs[0]) !=" ":
            flag = False
        if not flag:
            write(fw, bs)
        if chr(bs[0]) == "\n":
            flag = True
        bs = read(f, 1)
    close(f)
    close(fw)
except OSError as e:
    traceback.print_exc()
    print (e.strerror)
    exit()
