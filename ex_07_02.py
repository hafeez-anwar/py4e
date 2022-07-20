# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
spam_ = 0
spam_average = 0
spam_count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        ipos = line.find("X-DSPAM-Confidence:")
        sub_str = line[ipos+len("X-DSPAM-Confidence:"):ipos+26]
        #print(sub_str)
        num = float(sub_str.lstrip())
        spam_ = spam_+num
        spam_count = spam_count+1
    #print(line)
spam_average = spam_/spam_count
print("Average spam confidence:",spam_average)
