import random

rows = range(0,30)

a = []
b = []
trash = []

runMe = (len(rows)/2)

while runMe > 0:
    goingIn = random.choice(rows)
    if goingIn in trash:
        pass
    else:
        a.append(goingIn)
        runMe -=1
        trash.append(goingIn)

for i in rows:
    if i in a:
        pass
    else:
        b.append(i)
        
print "a\n{0}".format(a)
print "b\n{0}".format(b)
