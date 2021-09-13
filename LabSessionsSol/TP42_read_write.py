from os import *
import traceback
import sys

if len(sys.argv) != 2:
    print("Utilisation: %s fichier"%(sys.argv[0]))
    exit(0)

SIZE=256

try:
    f=open(sys.argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0o644)

    bs = read(sys.stdin.fileno(), SIZE)
    while len(bs) > 0:
        write(f, bs)
        bs = read(sys.stdin.fileno(), SIZE)
    close(f)

except OSError as e:
    traceback.print_exc()
    print(e.strerror)
    exit(1)


