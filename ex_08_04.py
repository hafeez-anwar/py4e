fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds)<1:
        continue
    else:
        for word in wds:
            if word in lst:
                continue
            else:
                lst.append(word)
lst.sort()
print(lst)
