smallest = None
largest = None
while True:
    line = input('> Enter a number: ')
    if line == 'done':
        break
    else:
        try:
            num = int(line)
        except:
            print("Invalid input ")
            continue

        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest :
            largest = num

print("Maximum is",largest)
print("Minimum is",smallest)
