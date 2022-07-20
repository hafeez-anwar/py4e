str = "X-DSPAM-Confidence:    0.8475"
ipos = str.find(':')
sub_str = str[ipos+1:]
num = float(sub_str)
print(num+42.0)
