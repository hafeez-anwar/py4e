
fh = open('mbox-short.txt') # does not read the file, just a handle

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
