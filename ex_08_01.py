def chop(t):
    del t[0]
    del t[-1]
    return None

def middle(t):
    x = t[1:-1]
    return x

t = [1,2,3,4,5,6]

print("New version of t",middle(t))
print("t before chopping:",t)
chop(t)
print("t after chopping:",t)
