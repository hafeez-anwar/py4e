fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
days_count = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words)<1 or words[0]!='From':
        continue
    else:
        c = words[2]
        days_count[c] = days_count.get(c,0)+1
