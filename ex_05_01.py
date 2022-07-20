total = 0
count = 0
average = 0
while True:
    line = input('> ')
    if line == 'done':
        break
    else:
        try:
            num = float(line)
            total = total+num
            count = count+1
        except:
            print(" Enter either a number or type done ")


print(total)
print(count)
if count==0:
    print("Average can not be computed")
else:
    average = total/count
    print(average)
