fname = input("Enter file name: ")
fh = open(fname)
our_dictionary = dict()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds)<1:
        continue
    else:
        for word in wds:
            our_dictionary[word] = 1

while True:
    word_to_check = input("Give your word to check in dictionay: ")
    if word_to_check == 'done':
        print("Ta ta")
        quit()
    else:
        if word_to_check in our_dictionary:
            print(word_to_check,"exists in dictionary")
        else:
            print(word_to_check,"not found in dictionary")
