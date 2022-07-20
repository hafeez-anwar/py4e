fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
email_count = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words)<1 or words[0]!='From':
        continue
    else:
        for word in words:
            if '@' not in word:
                continue
            else:
                email = word
                email_count[email] = email_count.get(email,0)+1

# Print sorted enteries
lst = list(email_count.keys())
lst.sort()
for key in lst:
    print(key,email_count[key])
