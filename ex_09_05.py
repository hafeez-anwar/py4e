fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
email_domain_count = dict()
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
                email = word.split('@')
                email_domain = email[1]
                #print(email_domain)
                email_domain_count[email_domain] = email_domain_count.get(email_domain,0)+1

print(email_domain_count)
