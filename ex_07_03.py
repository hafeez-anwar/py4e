# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    if fname=="na na boo boo":
        print(fname.upper(), "- You have been punk'd!")
    else:
        print("File cannot be opened:",fname)

    quit()

start_string = "X-DSPAM-Confidence:"
spam_ = 0
spam_average = 0
spam_count = 0
for line in fh:
    if not line.startswith(start_string):
        continue
    else:
        ipos = line.find(start_string)
        sub_str = line[ipos+len(start_string):ipos+len(start_string)+7]
        num = float(sub_str)
        spam_ = spam_+num
        spam_count = spam_count+1

spam_average = spam_/spam_count
print("Average spam confidence:",spam_average)
