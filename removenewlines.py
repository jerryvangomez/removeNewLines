def removeNewLines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(removeNewLines("test.txt"))