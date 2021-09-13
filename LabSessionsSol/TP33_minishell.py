from os import *
import sys

x=input()
while x != "quit":
    args = x.split()
    if len(args) == 0:
        x = input()
        continue
    bkgnd = 0
    if args[-1].endswith("&"):
        last = args.pop()
        if len(last) > 1:
            args.append(last[0:-1])
        bkgnd = 1

    try:
        child = fork()
    except OSError as e :
        print ("fork:", e.strerror)
        exit(1)
    if child != 0:
        # parent code
        if not bkgnd:
            result = wait()
            print ("process ", result[0], "terminated with code ", result[1] >> 8)
        x = input()
    else:
        try:
            execvp(args[0], args)
        except:
            e = sys.exc_info()[1]
            print ("exec:", e.strerror)
            exit(1)





